"""Sanity tests for quantum_engine (run: python tests/test_quantum_engine.py)."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import quantum_engine as qe  # noqa: E402


def check(z, full=None, condensed=None, unpaired=None):
    d = qe.element_details(z)
    cfg = d["configuration"]
    assert d["stats"]["total_electrons"] == z, (z, d["stats"]["total_electrons"])
    assert len(d["electrons"]) == z
    if full is not None:
        assert cfg["full_plain"] == full, (z, cfg["full_plain"])
    if condensed is not None:
        assert cfg["condensed_plain"] == condensed, (z, cfg["condensed_plain"])
    if unpaired is not None:
        assert d["stats"]["unpaired_electrons"] == unpaired, (z, d["stats"]["unpaired_electrons"])
    return d


def main():
    order = " ".join(s["label"] for s in qe.madelung_sequence())
    assert order == "1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d 7p", order

    for z in range(1, 119):
        check(z)

    check(1, full="1s1", condensed="1s1", unpaired=1)
    check(2, full="1s2", condensed="1s2", unpaired=0)
    check(8, condensed="[He] 2s2 2p4", unpaired=2)
    check(26, full="1s2 2s2 2p6 3s2 3p6 4s2 3d6", condensed="[Ar] 4s2 3d6", unpaired=4)
    check(24, condensed="[Ar] 4s1 3d5", unpaired=6)
    check(29, condensed="[Ar] 4s1 3d10", unpaired=1)
    check(41, condensed="[Kr] 5s1 4d4")
    check(42, condensed="[Kr] 5s1 4d5")
    check(44, condensed="[Kr] 5s1 4d7")
    check(45, condensed="[Kr] 5s1 4d8")
    pd = check(46, condensed="[Kr] 4d10", unpaired=0)
    assert any(b["label"] == "5s" and b["count"] == 0 for b in pd["boxes"]), "Pd should show empty 5s"
    check(47, condensed="[Kr] 5s1 4d10")
    la = check(57, condensed="[Xe] 6s2 5d1")
    assert any(b["label"] == "4f" and b["count"] == 0 for b in la["boxes"]), "La should show empty 4f"
    check(64, condensed="[Xe] 6s2 4f7 5d1", unpaired=8)
    check(78, condensed="[Xe] 6s1 4f14 5d9")
    check(79, condensed="[Xe] 6s1 4f14 5d10")
    check(89, condensed="[Rn] 7s2 6d1")
    check(36, condensed="[Ar] 4s2 3d10 4p6", unpaired=0)
    check(18, condensed="[Ne] 3s2 3p6")
    check(118, condensed="[Rn] 7s2 5f14 6d10 7p6")

    fe = qe.element_details(26)
    assert fe["exception"] is None and fe["block"] == "d" and fe["period"] == 4 and fe["group"] == 8
    cr = qe.element_details(24)
    assert cr["exception"]["aufbau_prediction"] == "[Ar] 4s² 3d⁴"
    assert qe.element_details(58)["block"] == "f"
    assert qe.element_details(2)["block"] == "s"
    assert qe.element_details(118)["predicted"] is True

    # Hund's rule: N 2p3 -> three spin-up electrons in m_l = +1, 0, -1
    n2p = [e for e in qe.element_details(7)["electrons"] if e["subshell"] == "2p"]
    assert [(e["ml"], e["ms"]) for e in n2p] == [(1, 0.5), (0, 0.5), (-1, 0.5)]

    # Unique periodic-table cells
    cells = {(e["row"], e["col"]) for e in qe.all_elements()}
    assert len(cells) == 118
    print("All quantum_engine tests passed.")


if __name__ == "__main__":
    main()
