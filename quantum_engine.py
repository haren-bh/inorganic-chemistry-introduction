"""
Quantum element-configuration engine (Module C backend).

Implements, for Z = 1 .. 118:
  * Aufbau filling using the Madelung (n + l, n) rule
  * Pauli exclusion (max 2 electrons per orbital, opposite m_s)
  * Hund's rule of maximum multiplicity for orbital-box diagrams
  * Overrides for experimentally established ground-state exceptions
    (Cr, Cu, Nb, Mo, Ru, Rh, Pd, Ag, La, Gd, Pt, Au, Ac, ... )
  * Full spdf notation, condensed noble-gas notation, orbital boxes with
    individual electron quantum numbers (n, l, m_l, m_s), and statistics.
"""

from __future__ import annotations

L_LETTERS = "spdfghi"
SUPERSCRIPT = str.maketrans("0123456789+-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻")

# --------------------------------------------------------------------------- #
# Element table (symbol, name) indexed by Z - 1
# --------------------------------------------------------------------------- #
ELEMENTS = [
    ("H", "Hydrogen"), ("He", "Helium"), ("Li", "Lithium"), ("Be", "Beryllium"),
    ("B", "Boron"), ("C", "Carbon"), ("N", "Nitrogen"), ("O", "Oxygen"),
    ("F", "Fluorine"), ("Ne", "Neon"), ("Na", "Sodium"), ("Mg", "Magnesium"),
    ("Al", "Aluminium"), ("Si", "Silicon"), ("P", "Phosphorus"), ("S", "Sulfur"),
    ("Cl", "Chlorine"), ("Ar", "Argon"), ("K", "Potassium"), ("Ca", "Calcium"),
    ("Sc", "Scandium"), ("Ti", "Titanium"), ("V", "Vanadium"), ("Cr", "Chromium"),
    ("Mn", "Manganese"), ("Fe", "Iron"), ("Co", "Cobalt"), ("Ni", "Nickel"),
    ("Cu", "Copper"), ("Zn", "Zinc"), ("Ga", "Gallium"), ("Ge", "Germanium"),
    ("As", "Arsenic"), ("Se", "Selenium"), ("Br", "Bromine"), ("Kr", "Krypton"),
    ("Rb", "Rubidium"), ("Sr", "Strontium"), ("Y", "Yttrium"), ("Zr", "Zirconium"),
    ("Nb", "Niobium"), ("Mo", "Molybdenum"), ("Tc", "Technetium"), ("Ru", "Ruthenium"),
    ("Rh", "Rhodium"), ("Pd", "Palladium"), ("Ag", "Silver"), ("Cd", "Cadmium"),
    ("In", "Indium"), ("Sn", "Tin"), ("Sb", "Antimony"), ("Te", "Tellurium"),
    ("I", "Iodine"), ("Xe", "Xenon"), ("Cs", "Caesium"), ("Ba", "Barium"),
    ("La", "Lanthanum"), ("Ce", "Cerium"), ("Pr", "Praseodymium"), ("Nd", "Neodymium"),
    ("Pm", "Promethium"), ("Sm", "Samarium"), ("Eu", "Europium"), ("Gd", "Gadolinium"),
    ("Tb", "Terbium"), ("Dy", "Dysprosium"), ("Ho", "Holmium"), ("Er", "Erbium"),
    ("Tm", "Thulium"), ("Yb", "Ytterbium"), ("Lu", "Lutetium"), ("Hf", "Hafnium"),
    ("Ta", "Tantalum"), ("W", "Tungsten"), ("Re", "Rhenium"), ("Os", "Osmium"),
    ("Ir", "Iridium"), ("Pt", "Platinum"), ("Au", "Gold"), ("Hg", "Mercury"),
    ("Tl", "Thallium"), ("Pb", "Lead"), ("Bi", "Bismuth"), ("Po", "Polonium"),
    ("At", "Astatine"), ("Rn", "Radon"), ("Fr", "Francium"), ("Ra", "Radium"),
    ("Ac", "Actinium"), ("Th", "Thorium"), ("Pa", "Protactinium"), ("U", "Uranium"),
    ("Np", "Neptunium"), ("Pu", "Plutonium"), ("Am", "Americium"), ("Cm", "Curium"),
    ("Bk", "Berkelium"), ("Cf", "Californium"), ("Es", "Einsteinium"), ("Fm", "Fermium"),
    ("Md", "Mendelevium"), ("No", "Nobelium"), ("Lr", "Lawrencium"), ("Rf", "Rutherfordium"),
    ("Db", "Dubnium"), ("Sg", "Seaborgium"), ("Bh", "Bohrium"), ("Hs", "Hassium"),
    ("Mt", "Meitnerium"), ("Ds", "Darmstadtium"), ("Rg", "Roentgenium"), ("Cn", "Copernicium"),
    ("Nh", "Nihonium"), ("Fl", "Flerovium"), ("Mc", "Moscovium"), ("Lv", "Livermorium"),
    ("Ts", "Tennessine"), ("Og", "Oganesson"),
]
assert len(ELEMENTS) == 118

NOBLE_GASES = [(2, "He"), (10, "Ne"), (18, "Ar"), (36, "Kr"), (54, "Xe"), (86, "Rn"), (118, "Og")]

# --------------------------------------------------------------------------- #
# Madelung (n + l, n) filling order: 1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f
# 5d 6p 7s 5f 6d 7p  (first 19 subshells with l <= 3 needed up to Z = 118)
# --------------------------------------------------------------------------- #
_all_subshells = [(n, l) for n in range(1, 8) for l in range(0, min(n, 4))]
_all_subshells.sort(key=lambda nl: (nl[0] + nl[1], nl[0]))
MADELUNG_ORDER = _all_subshells[:19]
MADELUNG_INDEX = {nl: i for i, nl in enumerate(MADELUNG_ORDER)}


def subshell_label(n: int, l: int) -> str:
    return f"{n}{L_LETTERS[l]}"


def parse_label(label: str) -> tuple[int, int]:
    return int(label[:-1]), L_LETTERS.index(label[-1])


def capacity(l: int) -> int:
    return 2 * (2 * l + 1)


def madelung_configuration(z: int) -> dict[tuple[int, int], int]:
    """Pure Aufbau prediction: fill subshells in Madelung order."""
    config: dict[tuple[int, int], int] = {}
    remaining = z
    for n, l in MADELUNG_ORDER:
        if remaining <= 0:
            break
        take = min(capacity(l), remaining)
        config[(n, l)] = take
        remaining -= take
    return config


# --------------------------------------------------------------------------- #
# Experimentally established exceptions (NIST ground-state configurations).
# "spec" = listed in the specification sheet; "additional" = further measured
# exceptions included for physical accuracy.
# --------------------------------------------------------------------------- #
EXCEPTIONS = {
    24: {"core": "Ar", "valence": {"4s": 1, "3d": 5}, "type": "Half-filled 3d stabilization",
         "source": "spec",
         "reason": "Promoting one 4s electron gives a half-filled 3d⁵ subshell: six parallel spins "
                   "maximise exchange energy, which outweighs the small 4s→3d promotion cost."},
    29: {"core": "Ar", "valence": {"4s": 1, "3d": 10}, "type": "Fully-filled 3d stabilization",
         "source": "spec",
         "reason": "A completely filled 3d¹⁰ shell is spherically symmetric with maximal exchange "
                   "stabilisation; the 3d level drops below 4s once it is nearly full."},
    41: {"core": "Kr", "valence": {"5s": 1, "4d": 4}, "type": "4d / 5s near-degeneracy",
         "source": "spec",
         "reason": "The 5s and 4d energies are almost equal for the second transition row, so the "
                   "configuration with more unpaired d electrons (higher exchange energy) wins."},
    42: {"core": "Kr", "valence": {"5s": 1, "4d": 5}, "type": "Half-filled 4d stabilization",
         "source": "spec",
         "reason": "Analogous to chromium: 5s¹4d⁵ gives six unpaired parallel spins and maximal "
                   "exchange stabilisation."},
    44: {"core": "Kr", "valence": {"5s": 1, "4d": 7}, "type": "4d / 5s near-degeneracy",
         "source": "spec",
         "reason": "Near-degenerate 5s and 4d levels: reduced electron–electron repulsion in 5s¹ "
                   "makes 5s¹4d⁷ lower in energy than 5s²4d⁶."},
    45: {"core": "Kr", "valence": {"5s": 1, "4d": 8}, "type": "4d / 5s near-degeneracy",
         "source": "spec",
         "reason": "Near-degenerate 5s and 4d levels favour 5s¹4d⁸ over the Aufbau 5s²4d⁷."},
    46: {"core": "Kr", "valence": {"4d": 10}, "type": "Fully-filled 4d (empty 5s)",
         "source": "spec",
         "reason": "Palladium is unique: both 5s electrons move into 4d, giving a closed 4d¹⁰ "
                   "shell with no 5s electrons at all."},
    47: {"core": "Kr", "valence": {"5s": 1, "4d": 10}, "type": "Fully-filled 4d stabilization",
         "source": "spec",
         "reason": "Like copper: a closed 4d¹⁰ shell plus a single 5s electron is the lowest-energy "
                   "arrangement."},
    57: {"core": "Xe", "valence": {"6s": 2, "5d": 1}, "type": "5d occupied before 4f",
         "source": "spec",
         "reason": "At Z = 57 the 4f orbital has not yet collapsed inward; 5d is slightly lower, "
                   "so the first post-barium electron enters 5d instead of 4f."},
    58: {"core": "Xe", "valence": {"6s": 2, "4f": 1, "5d": 1}, "type": "4f / 5d near-degeneracy",
         "source": "additional",
         "reason": "4f and 5d are nearly degenerate at cerium; one electron occupies each."},
    64: {"core": "Xe", "valence": {"6s": 2, "4f": 7, "5d": 1}, "type": "Half-filled 4f stabilization",
         "source": "spec",
         "reason": "Keeping a half-filled 4f⁷ shell (8 parallel spins) is so favourable that the "
                   "8th electron goes into 5d rather than pairing in 4f."},
    78: {"core": "Xe", "valence": {"6s": 1, "4f": 14, "5d": 9}, "type": "5d / 6s near-degeneracy (relativistic)",
         "source": "spec",
         "reason": "Relativistic contraction of 6s and expansion of 5d bring the levels close; "
                   "6s¹5d⁹ lies lowest for platinum."},
    79: {"core": "Xe", "valence": {"6s": 1, "4f": 14, "5d": 10}, "type": "Fully-filled 5d stabilization (relativistic)",
         "source": "spec",
         "reason": "A closed 5d¹⁰ shell plus a strongly relativistically-contracted 6s¹ electron — "
                   "the same effect that gives gold its yellow colour."},
    89: {"core": "Rn", "valence": {"7s": 2, "6d": 1}, "type": "6d occupied before 5f",
         "source": "spec",
         "reason": "Analogous to lanthanum: 6d is slightly below 5f at Z = 89."},
    90: {"core": "Rn", "valence": {"7s": 2, "6d": 2}, "type": "6d occupied before 5f",
         "source": "additional",
         "reason": "Thorium's 5f level is still above 6d, so both valence electrons enter 6d."},
    91: {"core": "Rn", "valence": {"7s": 2, "5f": 2, "6d": 1}, "type": "5f / 6d near-degeneracy",
         "source": "additional",
         "reason": "5f and 6d are close in energy in the early actinides."},
    92: {"core": "Rn", "valence": {"7s": 2, "5f": 3, "6d": 1}, "type": "5f / 6d near-degeneracy",
         "source": "additional",
         "reason": "5f and 6d are close in energy in the early actinides."},
    93: {"core": "Rn", "valence": {"7s": 2, "5f": 4, "6d": 1}, "type": "5f / 6d near-degeneracy",
         "source": "additional",
         "reason": "5f and 6d are close in energy in the early actinides."},
    96: {"core": "Rn", "valence": {"7s": 2, "5f": 7, "6d": 1}, "type": "Half-filled 5f stabilization",
         "source": "additional",
         "reason": "Like gadolinium: a half-filled 5f⁷ shell is retained and the extra electron "
                   "enters 6d."},
    103: {"core": "Rn", "valence": {"7s": 2, "5f": 14, "7p": 1}, "type": "Relativistic 7p₁/₂ stabilization",
          "source": "additional",
          "reason": "Strong relativistic stabilisation of the 7p₁/₂ spinor places it below 6d for "
                    "lawrencium (confirmed by ionisation-energy measurements, 2015)."},
}

# --------------------------------------------------------------------------- #
# Periodic-table layout (18 columns; f-block in rows 9-10)
# --------------------------------------------------------------------------- #

def table_position(z: int) -> dict:
    """Return period, group, grid row/column and block for element Z."""
    if z <= 2:
        period, col = 1, (1 if z == 1 else 18)
    elif z <= 10:
        period, idx = 2, z - 2
        col = idx if idx <= 2 else idx + 10
    elif z <= 18:
        period, idx = 3, z - 10
        col = idx if idx <= 2 else idx + 10
    elif z <= 36:
        period, col = 4, z - 18
    elif z <= 54:
        period, col = 5, z - 36
    elif z <= 86:
        period = 6
        if z <= 56:
            col = z - 54
        elif z <= 71:
            col = None
        else:
            col = z - 68
    else:
        period = 7
        if z <= 88:
            col = z - 86
        elif z <= 103:
            col = None
        else:
            col = z - 100

    if col is None:  # lanthanide / actinide row
        f_row = 9 if period == 6 else 10
        start = 57 if period == 6 else 89
        return {"period": period, "group": None, "row": f_row, "col": 3 + (z - start),
                "block": "f"}

    if col <= 2 or z == 2:
        block = "s"
    elif col >= 13:
        block = "p"
    else:
        block = "d"
    return {"period": period, "group": col, "row": period, "col": col, "block": block}


# --------------------------------------------------------------------------- #
# Configuration builders
# --------------------------------------------------------------------------- #

def ground_state_configuration(z: int) -> dict[tuple[int, int], int]:
    if z in EXCEPTIONS:
        exc = EXCEPTIONS[z]
        core_z = next(nz for nz, sym in NOBLE_GASES if sym == exc["core"])
        config = madelung_configuration(core_z)
        for label, count in exc["valence"].items():
            config[parse_label(label)] = count
        assert sum(config.values()) == z, f"Exception table inconsistent for Z={z}"
        return config
    return madelung_configuration(z)


def _ordered(config: dict[tuple[int, int], int]) -> list[tuple[int, int, int]]:
    return [(n, l, config[(n, l)]) for (n, l) in MADELUNG_ORDER if config.get((n, l), 0) > 0]


def _format(parts: list[tuple[int, int, int]], unicode: bool) -> str:
    if unicode:
        return " ".join(f"{subshell_label(n, l)}{str(c).translate(SUPERSCRIPT)}" for n, l, c in parts)
    return " ".join(f"{subshell_label(n, l)}{c}" for n, l, c in parts)


def previous_noble_gas(z: int) -> tuple[int, str] | None:
    prev = None
    for nz, sym in NOBLE_GASES:
        if nz < z:
            prev = (nz, sym)
    return prev


def notations(config: dict[tuple[int, int], int], z: int) -> dict:
    parts = _ordered(config)
    full_plain = _format(parts, unicode=False)
    full_unicode = _format(parts, unicode=True)
    core = previous_noble_gas(z)
    if core is None:
        cond_parts = parts
        core_symbol = None
    else:
        core_config = madelung_configuration(core[0])
        cond_parts = [(n, l, c) for n, l, c in parts if core_config.get((n, l), 0) != c
                      or (n, l) not in core_config]
        core_symbol = core[1]
    prefix = f"[{core_symbol}] " if core_symbol else ""
    return {
        "full": full_unicode,
        "full_plain": full_plain,
        "condensed": prefix + _format(cond_parts, unicode=True),
        "condensed_plain": prefix + _format(cond_parts, unicode=False),
        "core": core_symbol,
        "subshells": [{"label": subshell_label(n, l), "n": n, "l": l, "count": c,
                       "capacity": capacity(l)} for n, l, c in parts],
        "valence_subshells": [{"label": subshell_label(n, l), "n": n, "l": l, "count": c}
                              for n, l, c in cond_parts],
    }


def orbital_boxes(config: dict[tuple[int, int], int]) -> tuple[list[dict], list[dict]]:
    """
    Build orbital-box diagram data using Pauli + Hund.
    Shows every subshell (in Madelung order) up to the last occupied one,
    including empty ones such as Pd 5s or La 4f.
    Hund: singly occupy m_l = +l .. -l with spin-up first, then pair spin-down.
    """
    occupied_idx = [MADELUNG_INDEX[nl] for nl, c in config.items() if c > 0]
    last = max(occupied_idx) if occupied_idx else -1
    boxes = []
    electrons = []
    fill_order = 0
    for (n, l) in MADELUNG_ORDER[: last + 1]:
        count = config.get((n, l), 0)
        m_values = list(range(l, -l - 1, -1))
        orbitals = [{"ml": m, "electrons": []} for m in m_values]
        for i in range(count):
            slot = i % (2 * l + 1)
            ms = 0.5 if i < 2 * l + 1 else -0.5
            fill_order += 1
            e = {"n": n, "l": l, "ml": m_values[slot], "ms": ms,
                 "subshell": subshell_label(n, l), "order": fill_order}
            orbitals[slot]["electrons"].append(e)
            electrons.append(e)
        unpaired = sum(1 for o in orbitals if len(o["electrons"]) == 1)
        boxes.append({
            "label": subshell_label(n, l), "n": n, "l": l, "count": count,
            "capacity": capacity(l), "orbitals": orbitals, "unpaired": unpaired,
            "madelung_index": MADELUNG_INDEX[(n, l)], "n_plus_l": n + l,
        })
    return boxes, electrons


def element_summary(z: int) -> dict:
    symbol, name = ELEMENTS[z - 1]
    pos = table_position(z)
    return {"z": z, "symbol": symbol, "name": name, **pos, "is_exception": z in EXCEPTIONS}


def element_details(z: int) -> dict:
    if not 1 <= z <= 118:
        raise ValueError("Atomic number must be between 1 and 118")
    config = ground_state_configuration(z)
    boxes, electrons = orbital_boxes(config)
    notes = notations(config, z)

    shells: dict[int, int] = {}
    for (n, _l), c in config.items():
        shells[n] = shells.get(n, 0) + c
    by_l = {L_LETTERS[l]: sum(c for (n, ll), c in config.items() if ll == l) for l in range(4)}
    unpaired = sum(b["unpaired"] for b in boxes)
    n_max = max(n for (n, _l), c in config.items() if c > 0)

    data = {
        **element_summary(z),
        "configuration": notes,
        "boxes": boxes,
        "electrons": electrons,
        "stats": {
            "total_electrons": sum(config.values()),
            "unpaired_electrons": unpaired,
            "paired_electrons": sum(config.values()) - unpaired,
            "electrons_per_shell": [{"n": n, "count": shells[n]} for n in sorted(shells)],
            "electrons_by_l": by_l,
            "outer_shell_n": n_max,
            "outer_shell_electrons": shells[n_max],
            "spin_multiplicity": unpaired + 1,
            "occupied_subshells": len(notes["subshells"]),
        },
        "exception": None,
        "predicted": z >= 104,
    }
    if z in EXCEPTIONS:
        exc = EXCEPTIONS[z]
        aufbau = madelung_configuration(z)
        data["exception"] = {
            "type": exc["type"],
            "reason": exc["reason"],
            "source": exc["source"],
            "aufbau_prediction": notations(aufbau, z)["condensed"],
            "observed": notes["condensed"],
        }
    return data


def all_elements() -> list[dict]:
    return [element_summary(z) for z in range(1, 119)]


def madelung_sequence() -> list[dict]:
    return [{"label": subshell_label(n, l), "n": n, "l": l, "n_plus_l": n + l,
             "capacity": capacity(l)} for n, l in MADELUNG_ORDER]
