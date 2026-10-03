"""Google Cloud Storage synchronization engine for per-user quiz progress and attempts.

Syncs user data to and from:
    gs://haren-agent-storage/inorganic-chemistry-introduction/users/<username>.json

Supports:
1. Official `google-cloud-storage` Python client (used automatically on Cloud Run).
2. Direct Google Cloud Storage JSON REST API via OAuth2 token from:
   - GCE / Cloud Run Metadata Server
   - Application Default Credentials (`~/.config/gcloud/application_default_credentials.json`)
   - `gcloud auth print-access-token`
3. Local filesystem mirror (`.user_data_cache/<username>.json`) for offline/test resilience.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import ssl
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

BUCKET_NAME = os.environ.get("GCS_BUCKET_NAME", "haren-agent-storage")
OBJECT_PREFIX = os.environ.get("GCS_OBJECT_PREFIX", "inorganic-chemistry-introduction/users")
LOCAL_CACHE_DIR = Path(__file__).resolve().parent / ".user_data_cache"

_TOKEN_CACHE: dict[str, Any] = {
    "access_token": None,
    "expires_at": 0.0,
}


def _ssl_context() -> ssl.SSLContext:
    """Build an SSLContext that works on macOS Python 3.12 (using /etc/ssl/cert.pem) as well as Linux/Cloud Run."""
    try:
        import certifi  # type: ignore

        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        pass
    for ca_bundle in ("/etc/ssl/cert.pem", "/etc/ssl/certs/ca-certificates.crt"):
        if os.path.isfile(ca_bundle):
            try:
                return ssl.create_default_context(cafile=ca_bundle)
            except Exception:
                pass
    return ssl.create_default_context()


def normalize_username(raw: str) -> str:
    """Normalize a username into a safe identifier (lowercase alphanumeric, _, ., -)."""
    cleaned = re.sub(r"[^a-z0-9_.-]+", "_", str(raw or "").strip().lower()).strip("._-")
    return cleaned[:64]


def _object_name(username: str) -> str:
    norm = normalize_username(username)
    return f"{OBJECT_PREFIX}/{norm}.json"


def _local_cache_path(username: str) -> Path:
    norm = normalize_username(username)
    LOCAL_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    return LOCAL_CACHE_DIR / f"{norm}.json"


def empty_user_payload(username: str, display_name: str | None = None) -> dict[str, Any]:
    norm = normalize_username(username)
    return {
        "username": norm,
        "display_name": (display_name or username or norm).strip(),
        "updated_at": None,
        "history": {},
        "attempts": [],
        "sessions": {
            "batchByUnitSet": {},
            "singleByUnit": {},
        },
    }


def _get_oauth_access_token() -> str | None:
    """Obtain an OAuth2 access token from Metadata Server, ADC JSON, or gcloud CLI."""
    now = time.time()
    if _TOKEN_CACHE["access_token"] and now < float(_TOKEN_CACHE["expires_at"]) - 30:
        return str(_TOKEN_CACHE["access_token"])

    # 1. Try Cloud Run / GCE Metadata Server
    try:
        req = urllib.request.Request(
            "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token",
            headers={"Metadata-Flavor": "Google"},
            method="GET",
        )
        with urllib.request.urlopen(req, timeout=1.2) as resp:
            if resp.status == 200:
                payload = json.loads(resp.read().decode("utf-8"))
                tok = payload.get("access_token")
                if tok:
                    _TOKEN_CACHE["access_token"] = tok
                    _TOKEN_CACHE["expires_at"] = now + float(payload.get("expires_in", 3000))
                    return str(tok)
    except Exception:
        pass

    # 2. Try Application Default Credentials (ADC) refresh_token exchange
    adc_candidates = [
        os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"),
        str(Path.home() / ".config" / "gcloud" / "application_default_credentials.json"),
    ]
    for adc_path in adc_candidates:
        if not adc_path or not os.path.isfile(adc_path):
            continue
        try:
            with open(adc_path, "r", encoding="utf-8") as f:
                creds = json.load(f)
            if (
                creds.get("type") == "authorized_user"
                and creds.get("client_id")
                and creds.get("client_secret")
                and creds.get("refresh_token")
            ):
                form_data = urllib.parse.urlencode(
                    {
                        "client_id": creds["client_id"],
                        "client_secret": creds["client_secret"],
                        "refresh_token": creds["refresh_token"],
                        "grant_type": "refresh_token",
                    }
                ).encode("utf-8")
                req = urllib.request.Request(
                    "https://oauth2.googleapis.com/token",
                    data=form_data,
                    headers={"Content-Type": "application/x-www-form-urlencoded"},
                    method="POST",
                )
                with urllib.request.urlopen(req, timeout=4.0, context=_ssl_context()) as resp:
                    if resp.status == 200:
                        payload = json.loads(resp.read().decode("utf-8"))
                        tok = payload.get("access_token")
                        if tok:
                            _TOKEN_CACHE["access_token"] = tok
                            _TOKEN_CACHE["expires_at"] = now + float(payload.get("expires_in", 3000))
                            return str(tok)
        except Exception:
            pass

    # 3. Try gcloud CLI if available
    gcloud_bin = shutil.which("gcloud")
    if not gcloud_bin:
        fallback_gcloud = Path.home() / "Downloads" / "google-cloud-sdk" / "bin" / "gcloud"
        if fallback_gcloud.is_file():
            gcloud_bin = str(fallback_gcloud)
    if gcloud_bin:
        try:
            proc = subprocess.run(
                [gcloud_bin, "auth", "print-access-token"],
                capture_output=True,
                text=True,
                timeout=4.0,
                check=False,
            )
            if proc.returncode == 0 and proc.stdout.strip():
                tok = proc.stdout.strip()
                _TOKEN_CACHE["access_token"] = tok
                _TOKEN_CACHE["expires_at"] = now + 1800.0
                return tok
        except Exception:
            pass

    return None


_LAST_GCS_ERROR: str | None = None


def _gcs_read_object(username: str) -> tuple[dict[str, Any] | None, bool]:
    """Read user JSON from gs://<BUCKET_NAME>/inorganic-chemistry-introduction/users/<username>.json.

    Returns (payload_or_none, cloud_reachable).
    """
    global _LAST_GCS_ERROR
    if os.environ.get("DISABLE_GCS_SYNC") == "1":
        _LAST_GCS_ERROR = "DISABLE_GCS_SYNC=1"
        return None, False

    obj_name = _object_name(username)

    # 1. Try google-cloud-storage SDK if installed
    try:
        from google.api_core.exceptions import NotFound  # type: ignore
        from google.cloud import storage  # type: ignore

        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blob = bucket.blob(obj_name)
        try:
            raw_text = blob.download_as_text(encoding="utf-8")
            _LAST_GCS_ERROR = None
            return json.loads(raw_text), True
        except NotFound:
            _LAST_GCS_ERROR = None
            return None, True
    except ImportError:
        pass
    except Exception as exc:
        _LAST_GCS_ERROR = f"SDK read error: {type(exc).__name__}: {exc}"

    # 2. Try GCS JSON REST API with OAuth2 token
    token = _get_oauth_access_token()
    if not token:
        if not _LAST_GCS_ERROR:
            _LAST_GCS_ERROR = "No OAuth2 access token available"
        return None, False

    encoded_name = urllib.parse.quote(obj_name, safe="")
    url = f"https://storage.googleapis.com/storage/v1/b/{BUCKET_NAME}/o/{encoded_name}?alt=media"
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {token}"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=5.0, context=_ssl_context()) as resp:
            if resp.status == 200:
                data = json.loads(resp.read().decode("utf-8"))
                _LAST_GCS_ERROR = None
                return data, True
    except urllib.error.HTTPError as e:
        if e.code == 404:
            _LAST_GCS_ERROR = None
            return None, True
        _LAST_GCS_ERROR = f"REST read HTTP {e.code}: {e.reason}"
    except Exception as exc:
        _LAST_GCS_ERROR = f"REST read error: {type(exc).__name__}: {exc}"

    return None, False


def _gcs_write_object(username: str, payload: dict[str, Any]) -> bool:
    """Write user JSON to gs://<BUCKET_NAME>/inorganic-chemistry-introduction/users/<username>.json."""
    global _LAST_GCS_ERROR
    if os.environ.get("DISABLE_GCS_SYNC") == "1":
        _LAST_GCS_ERROR = "DISABLE_GCS_SYNC=1"
        return False

    obj_name = _object_name(username)
    serialized = json.dumps(payload, ensure_ascii=False, indent=2)

    # 1. Try google-cloud-storage SDK if installed
    try:
        from google.api_core.exceptions import NotFound  # type: ignore
        from google.cloud import storage  # type: ignore

        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blob = bucket.blob(obj_name)
        try:
            blob.upload_from_string(serialized, content_type="application/json")
            _LAST_GCS_ERROR = None
            return True
        except NotFound:
            # Bucket may not exist yet in the project; attempt to create it
            bucket = client.create_bucket(BUCKET_NAME, location="US")
            blob = bucket.blob(obj_name)
            blob.upload_from_string(serialized, content_type="application/json")
            _LAST_GCS_ERROR = None
            return True
    except ImportError:
        pass
    except Exception as exc:
        _LAST_GCS_ERROR = f"SDK write error: {type(exc).__name__}: {exc}"

    # 2. Try GCS JSON REST API with OAuth2 token
    token = _get_oauth_access_token()
    if not token:
        if not _LAST_GCS_ERROR:
            _LAST_GCS_ERROR = "No OAuth2 access token available"
        return False

    encoded_name = urllib.parse.quote(obj_name, safe="")
    url = f"https://storage.googleapis.com/upload/storage/v1/b/{BUCKET_NAME}/o?uploadType=media&name={encoded_name}"
    req = urllib.request.Request(
        url,
        data=serialized.encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=6.0, context=_ssl_context()) as resp:
            if 200 <= resp.status < 300:
                _LAST_GCS_ERROR = None
                return True
    except urllib.error.HTTPError as e:
        _LAST_GCS_ERROR = f"REST write HTTP {e.code}: {e.reason}"
    except Exception as exc:
        _LAST_GCS_ERROR = f"REST write error: {type(exc).__name__}: {exc}"

    return False


def merge_user_payloads(base: dict[str, Any] | None, incoming: dict[str, Any]) -> dict[str, Any]:
    """Safely merge existing cloud/cached user data with incoming client data so attempts are never lost."""
    norm = normalize_username(incoming.get("username") or (base or {}).get("username") or "")
    display_name = (
        incoming.get("display_name")
        or (base or {}).get("display_name")
        or norm
    )

    merged = empty_user_payload(norm, str(display_name))
    merged["updated_at"] = datetime.now(timezone.utc).isoformat()

    # 1. Merge per-question history (keyed by question uid, e.g. "u1q1")
    hist: dict[str, Any] = {}
    if base and isinstance(base.get("history"), dict):
        hist.update(base["history"])
    if isinstance(incoming.get("history"), dict):
        hist.update(incoming["history"])
    merged["history"] = hist

    # 2. Merge attempts (deduplicate by attempt.id, sort chronologically by timestamp)
    attempts_by_id: dict[str, dict[str, Any]] = {}
    for source in (base or {}, incoming):
        raw_list = source.get("attempts")
        if not isinstance(raw_list, list):
            continue
        for att in raw_list:
            if not isinstance(att, dict):
                continue
            att_id = str(att.get("id") or "")
            if not att_id:
                att_id = f"att_{att.get('timestamp', '')}_{att.get('unitId', '')}_{att.get('mode', '')}_{att.get('scopeKey', '')}"
                att = {**att, "id": att_id}
            attempts_by_id[att_id] = att

    sorted_attempts = sorted(
        attempts_by_id.values(),
        key=lambda a: str(a.get("timestamp") or ""),
    )

    # Recompute sequential attemptNumber per (unitId, mode, scopeKey)
    scope_counts: dict[tuple[Any, Any, Any], int] = {}
    for att in sorted_attempts:
        key = (att.get("unitId"), att.get("mode"), att.get("scopeKey"))
        scope_counts[key] = scope_counts.get(key, 0) + 1
        att["attemptNumber"] = scope_counts[key]

    merged["attempts"] = sorted_attempts

    # 3. Merge active sessions (incoming session takes precedence per key, preserving untouched units)
    batch_sessions: dict[str, Any] = {}
    single_sessions: dict[str, Any] = {}
    last_location: dict[str, Any] | None = None
    if base and isinstance(base.get("sessions"), dict):
        if isinstance(base["sessions"].get("batchByUnitSet"), dict):
            batch_sessions.update(base["sessions"]["batchByUnitSet"])
        if isinstance(base["sessions"].get("singleByUnit"), dict):
            single_sessions.update(base["sessions"]["singleByUnit"])
        if isinstance(base["sessions"].get("lastLocation"), dict):
            last_location = dict(base["sessions"]["lastLocation"])

    if isinstance(incoming.get("sessions"), dict):
        if isinstance(incoming["sessions"].get("batchByUnitSet"), dict):
            batch_sessions.update(incoming["sessions"]["batchByUnitSet"])
        if isinstance(incoming["sessions"].get("singleByUnit"), dict):
            single_sessions.update(incoming["sessions"]["singleByUnit"])
        if isinstance(incoming["sessions"].get("lastLocation"), dict):
            inc_loc = incoming["sessions"]["lastLocation"]
            if not last_location or str(inc_loc.get("updatedAt") or "") >= str(last_location.get("updatedAt") or ""):
                last_location = dict(inc_loc)

    merged["sessions"] = {
        "batchByUnitSet": batch_sessions,
        "singleByUnit": single_sessions,
        "lastLocation": last_location,
    }
    return merged


def get_user_data(username: str) -> dict[str, Any]:
    """Fetch user data from Cloud Storage (`haren-agent-storage`) with local cache fallback."""
    norm = normalize_username(username)
    if not norm:
        raise ValueError("Invalid username")

    cloud_data, cloud_ok = _gcs_read_object(norm)
    cache_file = _local_cache_path(norm)
    local_data: dict[str, Any] | None = None
    if cache_file.is_file():
        try:
            local_data = json.loads(cache_file.read_text(encoding="utf-8"))
        except Exception:
            local_data = None

    if cloud_data is not None:
        merged = merge_user_payloads(local_data, cloud_data) if local_data else cloud_data
        try:
            cache_file.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception:
            pass
        return {
            "username": norm,
            "display_name": merged.get("display_name") or username,
            "exists": True,
            "found": True,
            "cloud_synced": True,
            "cloud_error": None,
            "bucket": BUCKET_NAME,
            "storage_bucket": BUCKET_NAME,
            "object_path": f"gs://{BUCKET_NAME}/{_object_name(norm)}",
            "data": merged,
        }

    if local_data is not None:
        # If cloud was reachable and returned 404, push local cache up to cloud
        pushed = False
        if cloud_ok:
            pushed = _gcs_write_object(norm, local_data)
        return {
            "username": norm,
            "display_name": local_data.get("display_name") or username,
            "exists": True,
            "found": True,
            "cloud_synced": pushed or cloud_ok,
            "cloud_error": None if (pushed or cloud_ok) else _LAST_GCS_ERROR,
            "bucket": BUCKET_NAME,
            "storage_bucket": BUCKET_NAME,
            "object_path": f"gs://{BUCKET_NAME}/{_object_name(norm)}",
            "data": local_data,
        }

    empty = empty_user_payload(norm, username)
    return {
        "username": norm,
        "display_name": empty["display_name"],
        "exists": False,
        "found": False,
        "cloud_synced": cloud_ok,
        "cloud_error": None if cloud_ok else _LAST_GCS_ERROR,
        "bucket": BUCKET_NAME,
        "storage_bucket": BUCKET_NAME,
        "object_path": f"gs://{BUCKET_NAME}/{_object_name(norm)}",
        "data": empty,
    }


def save_user_data(username: str, incoming_payload: dict[str, Any], merge: bool = True) -> dict[str, Any]:
    """Save and sync user data to Cloud Storage (`haren-agent-storage`) and local mirror."""
    norm = normalize_username(username)
    if not norm:
        raise ValueError("Invalid username")

    base_data: dict[str, Any] | None = None
    if merge:
        cloud_data, _ = _gcs_read_object(norm)
        cache_file = _local_cache_path(norm)
        local_data: dict[str, Any] | None = None
        if cache_file.is_file():
            try:
                local_data = json.loads(cache_file.read_text(encoding="utf-8"))
            except Exception:
                local_data = None
        if cloud_data and local_data:
            base_data = merge_user_payloads(local_data, cloud_data)
        else:
            base_data = cloud_data or local_data

    incoming_with_user = {
        **(incoming_payload or {}),
        "username": norm,
        "display_name": (incoming_payload or {}).get("display_name") or (base_data or {}).get("display_name") or username,
    }
    final_data = merge_user_payloads(base_data, incoming_with_user) if merge else merge_user_payloads(None, incoming_with_user)

    # Always write local cache
    cache_file = _local_cache_path(norm)
    try:
        cache_file.write_text(json.dumps(final_data, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception:
        pass

    cloud_synced = _gcs_write_object(norm, final_data)
    return {
        "username": norm,
        "display_name": final_data.get("display_name") or username,
        "exists": True,
        "found": True,
        "cloud_synced": cloud_synced,
        "cloud_error": None if cloud_synced else _LAST_GCS_ERROR,
        "bucket": BUCKET_NAME,
        "storage_bucket": BUCKET_NAME,
        "object_path": f"gs://{BUCKET_NAME}/{_object_name(norm)}",
        "data": final_data,
    }

