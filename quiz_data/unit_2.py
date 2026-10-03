"""AP Chemistry Unit 2: Molecular and Ionic Compound Structure and Properties."""

UNIT_META = {
    "id": 2,
    "title": "Unit 2: Compound Structure and Properties",
    "short_title": "Compound Structure & Properties",
    "exam_weight": "7–9%",
    "color": "#0891b2",
    "description": (
        "Types of chemical bonds, intramolecular force and potential energy"
        " curves, lattice energy and structure of ionic solids, metallic"
        " bonding and interstitial/substitutional alloys, Lewis diagrams,"
        " resonance and formal charge, VSEPR molecular geometry, bond angles,"
        " polarity, and sigma/pi hybridization."
    ),
    "topics": [
        {"code": "2.1", "title": "Types of Chemical Bonds"},
        {"code": "2.2", "title": "Intramolecular Force and Potential Energy"},
        {"code": "2.3", "title": "Structure of Ionic Solids"},
        {"code": "2.4", "title": "Structure of Metals and Alloys"},
        {"code": "2.5", "title": "Lewis Diagrams"},
        {"code": "2.6", "title": "Resonance and Formal Charge"},
        {"code": "2.7", "title": "VSEPR and Hybridization"},
    ],
}

QUESTIONS = [
    # -------------------------------------------------------------------------
    # Topic 2.1: Types of Chemical Bonds (Q1 - Q7)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 1,
        "topic_code": "2.1",
        "topic_title": "Types of Chemical Bonds",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Element</th><th>Pauling Electronegativity</th></tr></thead>"
            "<tbody>"
            "<tr><td>$\\text{H}$</td><td>$2.20$</td></tr>"
            "<tr><td>$\\text{C}$</td><td>$2.55$</td></tr>"
            "<tr><td>$\\text{N}$</td><td>$3.04$</td></tr>"
            "<tr><td>$\\text{O}$</td><td>$3.44$</td></tr>"
            "<tr><td>$\\text{F}$</td><td>$3.98$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Based on the electronegativity values in the table above, which of"
            " the following covalent bonds has the greatest degree of ionic"
            " character (largest dipole moment per unit bond length)?"
        ),
        "options": [
            "$\\text{C}-\\text{H}$",
            "$\\text{N}-\\text{O}$",
            "$\\text{C}-\\text{F}$",
            "$\\text{O}-\\text{F}$",
        ],
        "correct_index": 2,
        "explanation": (
            "The degree of polarity (partial ionic character) of a covalent"
            " bond increases with the electronegativity difference"
            " ($\\Delta\\text{EN}$) between the two bonded atoms. Calculating"
            " $\\Delta\\text{EN}$ for each pair: $\\text{C}-\\text{H}$ has"
            " $|2.55 - 2.20| = 0.35$; $\\text{N}-\\text{O}$ has $|3.44 - 3.04|"
            " = 0.40$; $\\text{C}-\\text{F}$ has $|3.98 - 2.55| = 1.43$; and"
            " $\\text{O}-\\text{F}$ has $|3.98 - 3.44| = 0.54$. Because"
            " $\\text{C}-\\text{F}$ has the largest $\\Delta\\text{EN}$"
            " ($1.43$), it has the greatest partial ionic character."
        ),
    },
    {
        "unit_q_num": 2,
        "topic_code": "2.1",
        "topic_title": "Types of Chemical Bonds",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Substance</th><th>Melting Point ($^\\circ\\text{C}$)</th>"
            "<th>Electrical Conductivity of Solid</th>"
            "<th>Electrical Conductivity of Liquid</th></tr></thead>"
            "<tbody>"
            "<tr><td>$\\text{W}$</td><td>$801$</td><td>Negligible</td><td>High</td></tr>"
            "<tr><td>$\\text{X}$</td><td>$-114$</td><td>Negligible</td><td>Negligible</td></tr>"
            "<tr><td>$\\text{Y}$</td><td>$1085$</td><td>High</td><td>High</td></tr>"
            "<tr><td>$\\text{Z}$</td><td>$1713$</td><td>Negligible</td><td>Negligible</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Macroscopic properties of four pure substances are given in the"
            " table above. Which choice correctly identifies the primary"
            " type of bonding in substances $\\text{W}$, $\\text{X}$, and"
            " $\\text{Y}$?"
        ),
        "options": [
            "$\\text{W}$: Metallic, $\\text{X}$: Polar covalent, $\\text{Y}$: Ionic",
            "$\\text{W}$: Ionic, $\\text{X}$: Molecular covalent, $\\text{Y}$: Metallic",
            "$\\text{W}$: Network covalent, $\\text{X}$: Ionic, $\\text{Y}$: Metallic",
            "$\\text{W}$: Ionic, $\\text{X}$: Metallic, $\\text{Y}$: Network covalent",
        ],
        "correct_index": 1,
        "explanation": (
            "Substance $\\text{W}$ has a high melting point and conducts"
            " electricity only when molten (liquid), where ions are free to"
            " move—characteristic of an ionic solid (such as $\\text{NaCl}$)."
            " Substance $\\text{X}$ has a low melting point and does not"
            " conduct in either state, characteristic of a discrete molecular"
            " covalent substance (such as $\\text{HCl}$ or ethanol). Substance"
            " $\\text{Y}$ has a high melting point and conducts electricity in"
            " both solid and liquid states due to delocalized valence"
            " electrons, characteristic of metallic bonding (such as $\\text{Cu}$)."
        ),
    },
    {
        "unit_q_num": 3,
        "topic_code": "2.1",
        "topic_title": "Types of Chemical Bonds",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "Which of the following compounds contains BOTH ionic and polar"
            " covalent bonds?"
        ),
        "options": [
            "$\\text{CH}_3\\text{OH}$",
            "$\\text{MgCl}_2$",
            "$\\text{CCl}_4$",
            "$\\text{NH}_4\\text{NO}_3$",
        ],
        "correct_index": 3,
        "explanation": (
            "Ammonium nitrate ($\\text{NH}_4\\text{NO}_3$) consists of"
            " polyatomic ammonium cations ($\\text{NH}_4^+$) and nitrate anions"
            " ($\\text{NO}_3^-$) held together by electrostatic ionic bonds."
            " Within each polyatomic ion, the $\\text{N}-\\text{H}$ and"
            " $\\text{N}-\\text{O}$ bonds are polar covalent bonds between"
            " nonmetals of different electronegativities."
        ),
    },
    {
        "unit_q_num": 4,
        "topic_code": "2.1",
        "topic_title": "Types of Chemical Bonds",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": (
            "Titanium forms two common chlorides: $\\text{TiCl}_2$ (melting"
            " point $1035\\ ^\\circ\\text{C}$, solid at room temperature) and"
            " $\\text{TiCl}_4$ (melting point $-24\\ ^\\circ\\text{C}$, volatile"
            " liquid at room temperature). Which claim about the bonding in"
            " these two compounds is best supported by these properties?"
        ),
        "options": [
            "$\\text{TiCl}_2$ is an extended ionic solid, whereas $\\text{TiCl}_4$ consists of discrete molecules with covalent $\\text{Ti}-\\text{Cl}$ bonds that are held together only by weak intermolecular forces.",
            "$\\text{TiCl}_4$ has a higher lattice energy than $\\text{TiCl}_2$ because $\\text{Ti}^{4+}$ has a greater charge than $\\text{Ti}^{2+}$.",
            "$\\text{TiCl}_2$ forms discrete linear molecules with strong dipole-dipole forces, whereas $\\text{TiCl}_4$ is a nonpolar network solid.",
            "Both compounds must be ionic because each is formed from a metal and a nonmetal; the difference in melting points arises from their different molar masses.",
        ],
        "correct_index": 0,
        "explanation": (
            "Bonds between a metal and a nonmetal are generally ionic, but the"
            " properties of a compound are the best evidence of its type of"
            " bonding. The very low melting point and volatility of"
            " $\\text{TiCl}_4$ show that only weak intermolecular forces hold its"
            " particles together, so it must consist of discrete, covalently"
            " bonded $\\text{TiCl}_4$ molecules (a small, highly charged $+4$ metal"
            " center draws chloride electron density into shared bonds). The high"
            " melting point of $\\text{TiCl}_2$ is consistent with an extended"
            " ionic lattice. A larger lattice energy for $\\text{TiCl}_4$ would"
            " predict a higher, not lower, melting point; discrete molecules of"
            " $\\text{TiCl}_2$ could not melt as high as $1035\\ ^\\circ\\text{C}$,"
            " and a network solid could not melt at $-24\\ ^\\circ\\text{C}$;"
            " molar mass cannot explain the difference either, because the"
            " heavier compound ($\\text{TiCl}_4$) melts more than $1000\\ ^\\circ\\text{C}$ lower."
        ),
    },
    {
        "unit_q_num": 5,
        "topic_code": "2.1",
        "topic_title": "Types of Chemical Bonds",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "Which of the following pairs of elements is most likely to form a"
            " nonpolar covalent bond (or a bond with the least polarity)?"
        ),
        "options": [
            "$\\text{Na}$ and $\\text{Br}$",
            "$\\text{B}$ and $\\text{F}$",
            "$\\text{C}$ and $\\text{S}$",
            "$\\text{Si}$ and $\\text{O}$",
        ],
        "correct_index": 2,
        "explanation": (
            "Carbon ($\\text{EN} = 2.55$) and sulfur ($\\text{EN} = 2.58$) are"
            " both nonmetals with nearly identical electronegativities"
            " ($\\Delta\\text{EN} \\approx 0.03$), resulting in an essentially"
            " nonpolar covalent bond. By contrast, $\\text{Na}$ and $\\text{Br}$"
            " form an ionic bond, while $\\text{B}-\\text{F}$ and"
            " $\\text{Si}-\\text{O}$ have large electronegativity differences."
        ),
    },
    {
        "unit_q_num": 6,
        "topic_code": "2.1",
        "topic_title": "Types of Chemical Bonds",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "In a polar covalent bond between atom $\\text{X}$ and atom"
            " $\\text{Y}$, the bonding electrons are shared unequally, with"
            " greater electron density localized near atom $\\text{Y}$. Which"
            " of the following must be true about atoms $\\text{X}$ and"
            " $\\text{Y}$?"
        ),
        "options": [
            "Atom $\\text{Y}$ has a greater electronegativity than atom $\\text{X}$ and carries a partial negative charge ($\\delta^-$).",
            "Atom $\\text{X}$ carries a partial negative charge ($\\delta^-$) and atom $\\text{Y}$ carries a partial positive charge ($\\delta^+$).",
            "Atom $\\text{Y}$ has a larger atomic radius and lower effective nuclear charge than atom $\\text{X}$.",
            "The bond between $\\text{X}$ and $\\text{Y}$ is purely electrostatic with complete transfer of one or more valence electrons.",
        ],
        "correct_index": 0,
        "explanation": (
            "Because bonding electron density is shifted toward atom"
            " $\\text{Y}$, atom $\\text{Y}$ is more electronegative than atom"
            " $\\text{X}$ and acquires a partial negative charge ($\\delta^-$),"
            " while atom $\\text{X}$ acquires a partial positive charge"
            " ($\\delta^+$). Nothing about the bond requires atom $\\text{Y}$ to"
            " be larger or to have a lower effective nuclear charge, and the"
            " electrons are shared unequally rather than completely transferred,"
            " so the bond is polar covalent, not ionic. (A claim about ionization"
            " energy would also not be guaranteed: carbon is more electronegative"
            " than hydrogen, yet carbon has the lower first ionization energy.)"
        ),
    },
    {
        "unit_q_num": 7,
        "topic_code": "2.1",
        "topic_title": "Types of Chemical Bonds",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Bond</th><th>Dipole Moment ($\\text{D}$)</th>"
            "<th>Bond Length ($\\text{pm}$)</th></tr></thead>"
            "<tbody>"
            "<tr><td>$\\text{H}-\\text{F}$</td><td>$1.82$</td><td>$92$</td></tr>"
            "<tr><td>$\\text{H}-\\text{Cl}$</td><td>$1.08$</td><td>$127$</td></tr>"
            "<tr><td>$\\text{H}-\\text{Br}$</td><td>$0.82$</td><td>$141$</td></tr>"
            "<tr><td>$\\text{H}-\\text{I}$</td><td>$0.44$</td><td>$161$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Using the data in the table above, which statement best explains"
            " why the molecular dipole moment ($\\mu = q \\cdot r$) decreases"
            " from $\\text{HF}$ to $\\text{HI}$ even though the bond length"
            " $r$ increases?"
        ),
        "options": [
            "The polarizability of the hydrogen atom decreases as the halogen size increases.",
            "The number of lone pairs on the halogen atom decreases from $\\text{F}$ to $\\text{I}$.",
            "$\\text{HI}$ forms a three-dimensional ionic lattice rather than discrete diatomic molecules.",
            "The magnitude of the partial charge $q$ decreases much more rapidly than the internuclear distance $r$ increases because halogen electronegativity decreases down the group.",
        ],
        "correct_index": 3,
        "explanation": (
            "The dipole moment is given by $\\mu = q \\cdot r$. As one moves"
            " down Group 17 from $\\text{F}$ to $\\text{I}$, the valence"
            " orbitals of the halogen are in higher principal energy levels"
            " ($n = 2$ to $n = 5$) and farther from the nucleus, reducing"
            " electronegativity. This sharply reduces the unequal sharing of"
            " electrons (partial charge $q$), which outweighs the modest"
            " increase in bond length $r$."
        ),
    },
    # -------------------------------------------------------------------------
    # Topic 2.2: Intramolecular Force and Potential Energy (Q8 - Q14)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 8,
        "topic_code": "2.2",
        "topic_title": "Intramolecular Force and Potential Energy",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "On a graph of potential energy versus internuclear distance for"
            " two hydrogen atoms approaching one another to form an"
            " $\\text{H}_2$ molecule, what causes the potential energy to rise"
            " steeply to positive values when the internuclear distance becomes"
            " smaller than the equilibrium bond length ($74\\text{ pm}$)?"
        ),
        "options": [
            "Destructive interference between the $1s$ and $2p$ orbitals of the hydrogen atoms",
            "Electrostatic repulsion between the two positively charged nuclei and between the overlapping core/valence electron clouds",
            "Complete ionization of both hydrogen atoms into $\\text{H}^+$ and free electrons",
            "A decrease in the kinetic energy of the shared bonding electrons",
        ],
        "correct_index": 1,
        "explanation": (
            "At the equilibrium bond length, attractive forces (between each"
            " nucleus and the shared electron density) balance repulsive"
            " forces. At distances shorter than the equilibrium bond length,"
            " internuclear electrostatic repulsion between the two positively"
            " charged protons increases rapidly ($E \\propto 1/r$), causing the"
            " potential energy to spike sharply upward."
        ),
    },
    {
        "unit_q_num": 9,
        "topic_code": "2.2",
        "topic_title": "Intramolecular Force and Potential Energy",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Diatomic Molecule</th><th>Minimum Potential Energy ($\\text{kJ/mol}$)</th>"
            "<th>Internuclear Distance at Minimum PE ($\\text{pm}$)</th></tr></thead>"
            "<tbody>"
            "<tr><td>Curve 1</td><td>$-945$</td><td>$110$</td></tr>"
            "<tr><td>Curve 2</td><td>$-498$</td><td>$121$</td></tr>"
            "<tr><td>Curve 3</td><td>$-159$</td><td>$142$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "The features of the potential energy versus internuclear distance"
            " curves for three homonuclear diatomic molecules—$\\text{F}_2$,"
            " $\\text{O}_2$, and $\\text{N}_2$—are summarized in the table"
            " above. Which assignment of curves to molecules is correct?"
        ),
        "options": [
            "Curve 1: $\\text{N}_2$, Curve 2: $\\text{O}_2$, Curve 3: $\\text{F}_2$",
            "Curve 1: $\\text{F}_2$, Curve 2: $\\text{O}_2$, Curve 3: $\\text{N}_2$",
            "Curve 1: $\\text{O}_2$, Curve 2: $\\text{N}_2$, Curve 3: $\\text{F}_2$",
            "Curve 1: $\\text{N}_2$, Curve 2: $\\text{F}_2$, Curve 3: $\\text{O}_2$",
        ],
        "correct_index": 0,
        "explanation": (
            "$\\text{N}_2$ has a triple bond (bond order $3$), giving it the"
            " shortest equilibrium bond length ($110\\text{ pm}$) and the"
            " deepest potential energy well ($-945\\text{ kJ/mol}$). $\\text{O}_2$"
            " has a double bond (bond order $2$), giving an intermediate bond"
            " length ($121\\text{ pm}$) and bond energy ($498\\text{ kJ/mol}$)."
            " $\\text{F}_2$ has a single bond (bond order $1$), giving the"
            " longest bond length ($142\\text{ pm}$) and shallowest potential"
            " energy well ($-159\\text{ kJ/mol}$)."
        ),
    },
    {
        "unit_q_num": 10,
        "topic_code": "2.2",
        "topic_title": "Intramolecular Force and Potential Energy",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "Compare the potential energy versus internuclear distance curve"
            " for $\\text{Cl}_2$ with that for $\\text{Br}_2$. Relative to the"
            " minimum on the $\\text{Cl}_2$ curve, the minimum on the"
            " $\\text{Br}_2$ curve is located at:"
        ),
        "options": [
            "A shorter internuclear distance and a lower (more negative) potential energy",
            "A shorter internuclear distance and a higher (less negative) potential energy",
            "A longer internuclear distance and a higher (less negative) potential energy",
            "A longer internuclear distance and a lower (more negative) potential energy",
        ],
        "correct_index": 2,
        "explanation": (
            "A bromine atom ($n = 4$ valence shell) has a larger atomic radius"
            " than a chlorine atom ($n = 3$ valence shell). Because the"
            " bonding orbitals in $\\text{Br}_2$ are more diffuse and the"
            " shared electrons are farther from the nuclei, the"
            " $\\text{Br}-\\text{Br}$ bond is longer ($228\\text{ pm}$ vs."
            " $199\\text{ pm}$ for $\\text{Cl}_2$) and weaker"
            " ($193\\text{ kJ/mol}$ vs. $243\\text{ kJ/mol}$ for"
            " $\\text{Cl}_2$). Thus, the minimum is at a longer distance and a"
            " shallower (less negative / higher) potential energy."
        ),
    },
    {
        "unit_q_num": 11,
        "topic_code": "2.2",
        "topic_title": "Intramolecular Force and Potential Energy",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Carbon-Oxygen Bond</th><th>Average Bond Length ($\\text{pm}$)</th>"
            "<th>Average Bond Enthalpy ($\\text{kJ/mol}$)</th></tr></thead>"
            "<tbody>"
            "<tr><td>$\\text{C}-\\text{O}$</td><td>$143$</td><td>$358$</td></tr>"
            "<tr><td>$\\text{C}=\\text{O}$</td><td>$123$</td><td>$745$</td></tr>"
            "<tr><td>$\\text{C}\\equiv\\text{O}$</td><td>$113$</td><td>$1072$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "In the carbonate ion ($\\text{CO}_3^{2-}$), all three"
            " carbon-oxygen bonds are experimentally found to be identical in"
            " length and strength. Based on the reference table above, which"
            " pair of values is most reasonable for the carbon-oxygen bond"
            " length and bond enthalpy in $\\text{CO}_3^{2-}$?"
        ),
        "options": [
            "$143\\text{ pm}$ and $358\\text{ kJ/mol}$",
            "$129\\text{ pm}$ and $520\\text{ kJ/mol}$",
            "$118\\text{ pm}$ and $910\\text{ kJ/mol}$",
            "$113\\text{ pm}$ and $1072\\text{ kJ/mol}$",
        ],
        "correct_index": 1,
        "explanation": (
            "The carbonate ion ($\\text{CO}_3^{2-}$, $24$ valence electrons)"
            " has three equivalent resonance structures, each containing one"
            " $\\text{C}=\\text{O}$ double bond and two $\\text{C}-\\text{O}$"
            " single bonds. The average C–O bond order is $(2 + 1 + 1)/3 ="
            " 1.33$. Therefore, the bond length must lie between $123\\text{ pm}$"
            " (bond order $2$) and $143\\text{ pm}$ (bond order $1$), and the"
            " bond enthalpy must lie between $358\\text{ kJ/mol}$ and"
            " $745\\text{ kJ/mol}$. Only $129\\text{ pm}$ and $520\\text{ kJ/mol}$"
            " fall in this range."
        ),
    },
    {
        "unit_q_num": 12,
        "topic_code": "2.2",
        "topic_title": "Intramolecular Force and Potential Energy",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "As the internuclear distance $r$ between two isolated neutral"
            " chlorine atoms approaches infinity ($r \\to \\infty$), the"
            " potential energy of the two-atom system approaches $0\\text{ kJ/mol}$."
            " Why does the potential energy become negative as the two atoms"
            " approach each other from a large distance?"
        ),
        "options": [
            "Energy is absorbed from the surroundings to overcome nuclear repulsion.",
            "Core electrons are promoted to higher principal energy levels, releasing photons.",
            "The mass of the chlorine nuclei decreases slightly due to nuclear binding energy.",
            "The attractive Coulombic force between each nucleus and the other atom's valence electrons lowers the potential energy of the system.",
        ],
        "correct_index": 3,
        "explanation": (
            "By convention, two non-interacting separated atoms at $r = \\infty$"
            " define $E_p = 0$. As the atoms approach each other, the"
            " electrostatic attraction between the positively charged nucleus"
            " of each atom and the negatively charged valence electrons of the"
            " other atom exceeds the electron-electron and nucleus-nucleus"
            " repulsions, doing positive work and lowering the potential energy"
            " to negative values."
        ),
    },
    {
        "unit_q_num": 13,
        "topic_code": "2.2",
        "topic_title": "Intramolecular Force and Potential Energy",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "Which of the following correctly ranks the carbon-carbon bond"
            " lengths in ethane ($\\text{C}_2\\text{H}_6$), ethene"
            " ($\\text{C}_2\\text{H}_4$), and ethyne ($\\text{C}_2\\text{H}_2$)"
            " from shortest to longest?"
        ),
        "options": [
            "$\\text{C}_2\\text{H}_2 < \\text{C}_2\\text{H}_4 < \\text{C}_2\\text{H}_6$",
            "$\\text{C}_2\\text{H}_6 < \\text{C}_2\\text{H}_4 < \\text{C}_2\\text{H}_2$",
            "$\\text{C}_2\\text{H}_4 < \\text{C}_2\\text{H}_2 < \\text{C}_2\\text{H}_6$",
            "$\\text{C}_2\\text{H}_2 < \\text{C}_2\\text{H}_6 < \\text{C}_2\\text{H}_4$",
        ],
        "correct_index": 0,
        "explanation": (
            "Ethyne ($\\text{HC}\\equiv\\text{CH}$) has a carbon-carbon triple"
            " bond (bond order $3$, $\\sim 120\\text{ pm}$), ethene"
            " ($\\text{H}_2\\text{C}=\\text{CH}_2$) has a carbon-carbon double"
            " bond (bond order $2$, $\\sim 134\\text{ pm}$), and ethane"
            " ($\\text{H}_3\\text{C}-\\text{CH}_3$) has a carbon-carbon single"
            " bond (bond order $1$, $\\sim 154\\text{ pm}$). Higher shared"
            " electron density between the nuclei pulls them closer together,"
            " so $\\text{C}_2\\text{H}_2 < \\text{C}_2\\text{H}_4 <"
            " \\text{C}_2\\text{H}_6$."
        ),
    },
    {
        "unit_q_num": 14,
        "topic_code": "2.2",
        "topic_title": "Intramolecular Force and Potential Energy",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": (
            "The bond dissociation energy of $\\text{H}_2$ is $436\\text{ kJ/mol}$."
            " Approximately how much energy is required to break the covalent"
            " bond in a SINGLE molecule of $\\text{H}_2(g)$?"
        ),
        "options": [
            "$2.63 \\times 10^{26}\\text{ J}$",
            "$4.36 \\times 10^{5}\\text{ J}$",
            "$7.24 \\times 10^{-19}\\text{ J}$",
            "$7.24 \\times 10^{-22}\\text{ J}$",
        ],
        "correct_index": 2,
        "explanation": (
            "To find the energy per single $\\text{H}_2$ molecule, divide the"
            " molar bond dissociation energy in joules by Avogadro's number:"
            " $\\frac{436 \\times 10^3\\text{ J/mol}}{6.022 \\times 10^{23}\\text{ molecules/mol}}"
            " = 7.24 \\times 10^{-19}\\text{ J}$."
        ),
    },
    # -------------------------------------------------------------------------
    # Topic 2.3: Structure of Ionic Solids (Q15 - Q21)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 15,
        "topic_code": "2.3",
        "topic_title": "Structure of Ionic Solids",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Compound</th><th>Cation Radius ($\\text{pm}$)</th>"
            "<th>Anion Radius ($\\text{pm}$)</th><th>Melting Point ($^\\circ\\text{C}$)</th></tr></thead>"
            "<tbody>"
            "<tr><td>$\\text{NaF}$</td><td>$102$</td><td>$133$</td><td>$993$</td></tr>"
            "<tr><td>$\\text{MgO}$</td><td>$72$</td><td>$140$</td><td>$2852$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Based on Coulomb's law and the data in the table above, which"
            " factor is primarily responsible for the much higher melting"
            " point and lattice energy of $\\text{MgO}$ compared to $\\text{NaF}$?"
        ),
        "options": [
            "The oxide ion ($\\text{O}^{2-}$) has a slightly larger radius than the fluoride ion ($\\text{F}^-$).",
            "$\\text{MgO}$ contains $\\text{Mg}^{2+}$ and $\\text{O}^{2-}$ ions ($|q_1 q_2| = 4$), whereas $\\text{NaF}$ contains $\\text{Na}^+$ and $\\text{F}^-$ ions ($|q_1 q_2| = 1$).",
            "$\\text{MgO}$ forms covalent network molecules in the solid state, whereas $\\text{NaF}$ is ionic.",
            "Sodium has a lower first ionization energy than magnesium.",
        ],
        "correct_index": 1,
        "explanation": (
            "By Coulomb's law, the electrostatic lattice energy of an ionic"
            " solid is proportional to $\\frac{|q_1 q_2|}{r_0}$. Although the"
            " interionic distance $r_0 = r_+ + r_-$ is slightly smaller in"
            " $\\text{MgO}$ ($212\\text{ pm}$) than in $\\text{NaF}$"
            " ($235\\text{ pm}$), the fourfold increase in the product of ionic"
            " charges ($|+2 \\times -2| = 4$ for $\\text{MgO}$ vs."
            " $|+1 \\times -1| = 1$ for $\\text{NaF}$) is the dominant factor"
            " causing $\\text{MgO}$ to have a dramatically higher lattice"
            " energy and melting point."
        ),
    },
    {
        "unit_q_num": 16,
        "topic_code": "2.3",
        "topic_title": "Structure of Ionic Solids",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "Which of the following correctly lists the alkali metal halides"
            " $\\text{LiF}$, $\\text{NaCl}$, $\\text{KBr}$, and $\\text{CsI}$"
            " in order of increasing magnitude of lattice energy?"
        ),
        "options": [
            "$\\text{CsI} < \\text{KBr} < \\text{NaCl} < \\text{LiF}$",
            "$\\text{LiF} < \\text{NaCl} < \\text{KBr} < \\text{CsI}$",
            "$\\text{NaCl} < \\text{LiF} < \\text{CsI} < \\text{KBr}$",
            "$\\text{CsI} < \\text{NaCl} < \\text{KBr} < \\text{LiF}$",
        ],
        "correct_index": 0,
        "explanation": (
            "All four compounds consist of $+1$ cations and $-1$ anions, so"
            " the charge product $|q_1 q_2| = 1$ is identical for all of them."
            " According to Coulomb's law ($E \\propto \\frac{|q_1 q_2|}{r}$),"
            " lattice energy increases as the interionic distance $r$ decreases."
            " Because ionic radii decrease moving up Group 1 and Group 17,"
            " $r(\\text{CsI}) > r(\\text{KBr}) > r(\\text{NaCl}) > r(\\text{LiF})$,"
            " so the magnitude of lattice energy increases in the order"
            " $\\text{CsI} < \\text{KBr} < \\text{NaCl} < \\text{LiF}$."
        ),
    },
    {
        "unit_q_num": 17,
        "topic_code": "2.3",
        "topic_title": "Structure of Ionic Solids",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "Ionic crystals such as $\\text{KCl}(s)$ are hard, have high"
            " melting points, and shatter (cleave) rather than bend when struck"
            " with a hammer. Which particulate-level explanation best accounts"
            " for why an ionic crystal shatters under mechanical stress?"
        ),
        "options": [
            "Mechanical stress causes valence electrons to be ejected from the anions into the conduction band.",
            "Striking the crystal breaks the directional $\\pi$ bonds between adjacent potassium and chloride ions.",
            "The potassium cations are larger than the chloride anions, preventing close packing in the crystal lattice.",
            "Shifting a plane of ions by one atomic spacing brings ions of like charge into alignment, creating strong Coulombic repulsions that split the crystal along the plane.",
        ],
        "correct_index": 3,
        "explanation": (
            "In an ionic lattice, cations and anions alternate in a regular"
            " three-dimensional array to maximize attractions between opposite"
            " charges and minimize repulsions between like charges. When a"
            " shear force displaces one layer of ions by one ion position,"
            " cations align directly next to cations and anions align next to"
            " anions. The resulting strong electrostatic repulsion forces the"
            " layers apart, causing the crystal to cleave (shatter)."
        ),
    },
    {
        "unit_q_num": 18,
        "topic_code": "2.3",
        "topic_title": "Structure of Ionic Solids",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Compound</th><th>Lattice Energy ($\\text{kJ/mol}$)</th></tr></thead>"
            "<tbody>"
            "<tr><td>$\\text{CaO}$</td><td>$3414$</td></tr>"
            "<tr><td>$\\text{SrO}$</td><td>$3217$</td></tr>"
            "<tr><td>$\\text{BaO}$</td><td>$3029$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "The lattice energies of three alkaline earth metal oxides are"
            " shown above. A student claims that $\\text{CaS}$ will have a"
            " larger lattice energy than $\\text{CaO}$ because sulfur has more"
            " protons in its nucleus than oxygen. Do you agree or disagree with"
            " the student's claim, and why?"
        ),
        "options": [
            "Agree, because the greater nuclear charge of $\\text{S}^{2-}$ attracts $\\text{Ca}^{2+}$ more strongly according to Coulomb's law.",
            "Agree, because $\\text{S}^{2-}$ is more polarizable than $\\text{O}^{2-}$, which increases the ionic bond order.",
            "Disagree, because $\\text{S}^{2-}$ has an extra occupied principal energy level ($n=3$) compared to $\\text{O}^{2-}$ ($n=2$), increasing the interionic distance and decreasing the lattice energy.",
            "Disagree, because the sulfide ion has a $-1$ charge whereas the oxide ion has a $-2$ charge.",
        ],
        "correct_index": 2,
        "explanation": (
            "Both $\\text{CaO}$ and $\\text{CaS}$ contain $+2$ cations and $-2$"
            " anions, so the net ionic charges are the same. However,"
            " $\\text{S}^{2-}$ has its valence electrons in the $n=3$ shell"
            " whereas $\\text{O}^{2-}$ has its valence electrons in the $n=2$"
            " shell. Because $\\text{S}^{2-}$ has a larger ionic radius than"
            " $\\text{O}^{2-}$, the center-to-center distance between"
            " $\\text{Ca}^{2+}$ and $\\text{S}^{2-}$ is larger, resulting in a"
            " smaller lattice energy for $\\text{CaS}$ than for $\\text{CaO}$."
        ),
    },
    {
        "unit_q_num": 19,
        "topic_code": "2.3",
        "topic_title": "Structure of Ionic Solids",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "In a particulate diagram of solid sodium fluoride ($\\text{NaF}$),"
            " both $\\text{Na}^+$ and $\\text{F}^-$ are isoelectronic with"
            " neon ($1s^2 2s^2 2p^6$). How should the relative sizes and"
            " arrangement of the ions be represented in the diagram?"
        ),
        "options": [
            "$\\text{Na}^+$ spheres should be drawn smaller than $\\text{F}^-$ spheres, arranged in an alternating 3D lattice with $1:1$ stoichiometry.",
            "$\\text{Na}^+$ spheres should be drawn larger than $\\text{F}^-$ spheres, grouped into discrete diatomic $\\text{NaF}$ molecules.",
            "$\\text{Na}^+$ and $\\text{F}^-$ spheres should be drawn the same size because both ions have $10$ electrons.",
            "$\\text{Na}^+$ spheres should be surrounded by a delocalized sea of $\\text{F}^-$ ions.",
        ],
        "correct_index": 0,
        "explanation": (
            "Both $\\text{Na}^+$ ($Z = 11$) and $\\text{F}^-$ ($Z = 9$) have"
            " $10$ electrons in the same $n=2$ valence shell. Because"
            " $\\text{Na}^+$ has more protons ($11 > 9$), it experiences a"
            " greater effective nuclear charge, pulling its electron cloud"
            " closer to the nucleus ($r_{\\text{Na}^+} = 102\\text{ pm} <"
            " r_{\\text{F}^-} = 133\\text{ pm}$). Furthermore, as an ionic"
            " solid, $\\text{NaF}$ forms a continuous 3D alternating crystal"
            " lattice rather than discrete molecules."
        ),
    },
    {
        "unit_q_num": 20,
        "topic_code": "2.3",
        "topic_title": "Structure of Ionic Solids",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": (
            "Which of the following compounds has the greatest lattice energy"
            " (most exothermic lattice formation enthalpy)?"
        ),
        "options": [
            "$\\text{Na}_2\\text{O}$",
            "$\\text{MgCl}_2$",
            "$\\text{ScN}$",
            "$\\text{CaO}$",
        ],
        "correct_index": 2,
        "explanation": (
            "In $\\text{ScN}$ (scandium nitride), scandium forms the"
            " $\\text{Sc}^{3+}$ cation and nitrogen forms the $\\text{N}^{3-}$"
            " anion. The magnitude of the product of ionic charges is"
            " $|(+3)(-3)| = 9$, compared to $|(+2)(-2)| = 4$ in $\\text{CaO}$"
            " and $|(+2)(-1)| = 2$ or $|(+1)(-2)| = 2$ in $\\text{MgCl}_2$ and"
            " $\\text{Na}_2\\text{O}$. By Coulomb's law, the $+3/-3$ charge"
            " pairing gives $\\text{ScN}$ the largest lattice energy by far."
        ),
    },
    {
        "unit_q_num": 21,
        "topic_code": "2.3",
        "topic_title": "Structure of Ionic Solids",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "Why does solid calcium chloride, $\\text{CaCl}_2(s)$, fail to"
            " conduct an electric current, whereas an aqueous solution"
            " $\\text{CaCl}_2(aq)$ and molten $\\text{CaCl}_2(l)$ are both good"
            " electrical conductors?"
        ),
        "options": [
            "Water and heat ionize covalent $\\text{CaCl}_2$ molecules into $\\text{Ca}^{2+}$ and $\\text{Cl}^-$ ions.",
            "Electrons are delocalized across the crystal only when the temperature exceeds the melting point.",
            "$\\text{CaCl}_2(s)$ contains neutral calcium and chlorine atoms until dissolved or melted.",
            "In $\\text{CaCl}_2(s)$, the $\\text{Ca}^{2+}$ and $\\text{Cl}^-$ ions are held in fixed lattice positions by strong Coulombic forces, whereas in the liquid and aqueous states the ions are mobile.",
        ],
        "correct_index": 3,
        "explanation": (
            "Electrical conductivity requires mobile charged particles. In"
            " $\\text{CaCl}_2(s)$, ions are already present ($\\text{Ca}^{2+}$"
            " and $\\text{Cl}^-$), but they are locked into rigid lattice sites"
            " and can only vibrate in place. Melting or dissolving in water"
            " overcomes the lattice attractions, allowing the ions to move"
            " freely and carry an electric current."
        ),
    },
    # -------------------------------------------------------------------------
    # Topic 2.4: Structure of Metals and Alloys (Q22 - Q28)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 22,
        "topic_code": "2.4",
        "topic_title": "Structure of Metals and Alloys",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Element</th><th>Atomic Radius ($\\text{pm}$)</th></tr></thead>"
            "<tbody>"
            "<tr><td>$\\text{Fe}$</td><td>$126$</td></tr>"
            "<tr><td>$\\text{Cr}$</td><td>$128$</td></tr>"
            "<tr><td>$\\text{Ni}$</td><td>$124$</td></tr>"
            "<tr><td>$\\text{C}$</td><td>$77$</td></tr>"
            "<tr><td>$\\text{N}$</td><td>$75$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Stainless steel is an alloy formed by combining iron ($\\text{Fe}$)"
            " with chromium ($\\text{Cr}$), nickel ($\\text{Ni}$), and a small"
            " percentage of carbon ($\\text{C}$). Based on the atomic radii in"
            " the table above, what roles do $\\text{Cr}$ and $\\text{C}$ play"
            " in the crystal lattice of stainless steel?"
        ),
        "options": [
            "Both $\\text{Cr}$ and $\\text{C}$ occupy interstitial spaces between $\\text{Fe}$ atoms.",
            "Both $\\text{Cr}$ and $\\text{C}$ substitute for $\\text{Fe}$ atoms at regular lattice sites.",
            "$\\text{Cr}$ substitutes for $\\text{Fe}$ atoms at lattice sites, whereas $\\text{C}$ occupies small interstitial holes between the metal atoms.",
            "$\\text{C}$ substitutes for $\\text{Fe}$ atoms at lattice sites, whereas $\\text{Cr}$ occupies interstitial holes.",
        ],
        "correct_index": 2,
        "explanation": (
            "Substitutional alloys form between atoms of comparable radius;"
            " here $\\text{Cr}$ ($128\\text{ pm}$) and $\\text{Fe}$ ($126\\text{ pm}$)"
            " have nearly identical radii, so $\\text{Cr}$ replaces $\\text{Fe}$"
            " at lattice sites. Interstitial alloys form between atoms of"
            " significantly different radii: $\\text{C}$ ($77\\text{ pm}$) is only"
            " about $60\\%$ as large as $\\text{Fe}$ ($77/126 \\approx 0.61$), so it"
            " fits into the interstitial spaces (holes) between the larger iron"
            " atoms instead of replacing them."
        ),
    },
    {
        "unit_q_num": 23,
        "topic_code": "2.4",
        "topic_title": "Structure of Metals and Alloys",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "High-carbon steel is an interstitial alloy of iron and carbon."
            " Compared to pure iron, how does the presence of interstitial"
            " carbon atoms affect the malleability and hardness of the steel,"
            " and why?"
        ),
        "options": [
            "Steel is more malleable and softer because carbon donates extra electrons to the metallic electron sea.",
            "Steel is less malleable and harder (more rigid) because small carbon atoms in the interstices impede the sliding of adjacent planes of iron cations past one another.",
            "Steel is less malleable because carbon oxidizes iron into $\\text{Fe}^{3+}$, creating a brittle ionic lattice.",
            "Steel has identical malleability to pure iron because the crystal packing arrangement is unchanged.",
        ],
        "correct_index": 1,
        "explanation": (
            "In pure iron, planes of uniform $\\text{Fe}$ cations can slide"
            " over one another relatively easily within the delocalized"
            " electron sea when a force is applied. When small carbon atoms"
            " occupy interstitial spaces, they distort the lattice and act as"
            " physical obstacles (pinning dislocations) that prevent planes of"
            " iron atoms from slipping past each other, increasing hardness and"
            " tensile strength while decreasing malleability and ductility."
        ),
    },
    {
        "unit_q_num": 24,
        "topic_code": "2.4",
        "topic_title": "Structure of Metals and Alloys",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "Brass is a homogeneous mixture of approximately $67\\%$ copper"
            " ($r = 128\\text{ pm}$) and $33\\%$ zinc ($r = 134\\text{ pm}$)."
            " Which of the following best describes the bonding and properties"
            " of brass?"
        ),
        "options": [
            "It is a substitutional alloy in which valence electrons remain delocalized in a metallic sea, maintaining electrical conductivity while slightly reducing malleability compared to pure copper.",
            "It is an ionic compound with the fixed empirical formula $\\text{Cu}_2\\text{Zn}$ that shatters when struck.",
            "It is an interstitial alloy in which zinc atoms fit into the spaces (interstices) between copper atoms.",
            "It is a covalent network solid in which each copper atom forms directional $\\sigma$ bonds to four zinc atoms.",
        ],
        "correct_index": 0,
        "explanation": (
            "Because $\\text{Cu}$ ($128\\text{ pm}$) and $\\text{Zn}$"
            " ($134\\text{ pm}$) have very similar atomic radii, zinc atoms"
            " substitute directly for copper atoms in the metallic crystal"
            " lattice, forming a substitutional alloy. A sea of delocalized"
            " valence electrons is retained, so brass remains malleable and"
            " electrically conductive (though slightly harder and less"
            " conductive than pure copper)."
        ),
    },
    {
        "unit_q_num": 25,
        "topic_code": "2.4",
        "topic_title": "Structure of Metals and Alloys",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "Why are pure metals such as silver ($\\text{Ag}$) and aluminum"
            " ($\\text{Al}$) both malleable (able to be hammered into sheets)"
            " and ductile (able to be drawn into wires)?"
        ),
        "options": [
            "Metallic bonds are weak dispersion forces that break easily at room temperature.",
            "Metals consist of discrete two-dimensional layers held together only by hydrogen bonds.",
            "When stress is applied, metal cations gain electrons to become neutral gas atoms that re-condense in a new shape.",
            "Metallic bonding is non-directional; when layers of metal cations slide past one another, the mobile sea of delocalized valence electrons continuously adjusts to maintain electrostatic attraction.",
        ],
        "correct_index": 3,
        "explanation": (
            "In the electron-sea model of metallic bonding, metal cations are"
            " immersed in a uniform, mobile sea of delocalized valence"
            " electrons. Because the electrostatic attraction between cations"
            " and the electron sea is non-directional, shifting one plane of"
            " cations relative to another does not break localized bonds or"
            " create strong like-charge repulsions; the delocalized electrons"
            " immediately redistribute around the shifted cations."
        ),
    },
    {
        "unit_q_num": 26,
        "topic_code": "2.4",
        "topic_title": "Structure of Metals and Alloys",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Metal</th><th>Valence Electron Configuration</th>"
            "<th>Metallic Radius ($\\text{pm}$)</th><th>Melting Point ($^\\circ\\text{C}$)</th></tr></thead>"
            "<tbody>"
            "<tr><td>$\\text{Na}$</td><td>$3s^1$</td><td>$186$</td><td>$98$</td></tr>"
            "<tr><td>$\\text{Mg}$</td><td>$3s^2$</td><td>$160$</td><td>$650$</td></tr>"
            "<tr><td>$\\text{Al}$</td><td>$3s^2 3p^1$</td><td>$143$</td><td>$660$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Based on the electron-sea model of metallic bonding and the data"
            " in the table above, why does magnesium ($\\text{Mg}$) have a much"
            " higher melting point than sodium ($\\text{Na}$)?"
        ),
        "options": [
            "Magnesium forms covalent $\\text{Mg}_2$ dimers in the solid state, whereas sodium is monatomic.",
            "Each $\\text{Mg}$ atom contributes two valence electrons to the delocalized sea, leaving smaller $\\text{Mg}^{2+}$ cores that experience much stronger Coulombic attraction to the denser electron sea than $\\text{Na}^+$ cores.",
            "Sodium has a filled $2p$ subshell that shields the delocalized electrons from the nucleus.",
            "Magnesium has a larger atomic mass than sodium, increasing London dispersion forces between metal atoms.",
        ],
        "correct_index": 1,
        "explanation": (
            "In metallic sodium, each atom contributes $1$ valence electron to"
            " the delocalized sea, leaving $\\text{Na}^+$ cationic cores. In"
            " magnesium, each atom contributes $2$ valence electrons, leaving"
            " smaller, more highly charged $\\text{Mg}^{2+}$ cores immersed in"
            " a sea with twice the electron density. By Coulomb's law, the"
            " electrostatic attraction between $\\text{Mg}^{2+}$ and the"
            " delocalized electron sea is much stronger, resulting in a"
            " substantially higher melting point."
        ),
    },
    {
        "unit_q_num": 27,
        "topic_code": "2.4",
        "topic_title": "Structure of Metals and Alloys",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "How does the density of an interstitial alloy (such as carbon"
            " steel) typically compare to the density of the pure host metal"
            " (iron), assuming the spacing between host metal atoms expands"
            " only minimally?"
        ),
        "options": [
            "The density increases because additional mass (carbon atoms) is packed into the existing interstitial voids of the crystal lattice without significantly increasing the total volume.",
            "The density decreases because carbon has a smaller molar mass than iron.",
            "The density remains exactly constant because interstitial atoms have negligible mass.",
            "The density decreases by $50\\%$ because every carbon atom displaces two iron atoms.",
        ],
        "correct_index": 0,
        "explanation": (
            "In an interstitial alloy, small nonmetal atoms occupy the empty"
            " interstitial holes between the host metal atoms rather than"
            " replacing the host atoms. Because mass is added to the lattice"
            " while its volume increases very little, the overall"
            " density ($\\rho = m/V$) increases relative to the pure host"
            " metal (provided lattice expansion is minimal)."
        ),
    },
    {
        "unit_q_num": 28,
        "topic_code": "2.4",
        "topic_title": "Structure of Metals and Alloys",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": (
            "A student examines two particulate diagrams of binary alloys:"
            " Diagram I shows a regular grid of large gray circles with about"
            " $20\\%$ of the grid positions occupied by similarly sized white"
            " circles. Diagram II shows a regular grid of large gray circles"
            " with small black circles tucked into the spaces between the gray"
            " circles. Which pair of alloys could be represented by Diagram I"
            " and Diagram II, respectively?"
        ),
        "options": [
            "Diagram I: Tungsten carbide ($\\text{WC}$); Diagram II: Sterling silver ($\\text{Ag}/\\text{Cu}$)",
            "Diagram I: Carbon steel ($\\text{Fe}/\\text{C}$); Diagram II: Brass ($\\text{Cu}/\\text{Zn}$)",
            "Diagram I: Sodium chloride ($\\text{NaCl}$); Diagram II: Silicon dioxide ($\\text{SiO}_2$)",
            "Diagram I: Bronze ($\\text{Cu}/\\text{Sn}$); Diagram II: Carbon steel ($\\text{Fe}/\\text{C}$)",
        ],
        "correct_index": 3,
        "explanation": (
            "Diagram I represents a substitutional alloy because similarly"
            " sized atoms replace host metal atoms at regular lattice sites;"
            " bronze ($\\text{Cu}$ and $\\text{Sn}$) and brass ($\\text{Cu}$"
            " and $\\text{Zn}$) are classic substitutional alloys. Diagram II"
            " represents an interstitial alloy because much smaller atoms"
            " occupy the spaces between host metal atoms; carbon steel"
            " ($\\text{Fe}$ with interstitial $\\text{C}$) is a classic"
            " interstitial alloy."
        ),
    },
    # -------------------------------------------------------------------------
    # Topic 2.5: Lewis Diagrams (Q29 - Q35)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 29,
        "topic_code": "2.5",
        "topic_title": "Lewis Diagrams",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "What is the total number of valence electrons that must be shown"
            " in the complete Lewis electron-dot diagram of the sulfite ion,"
            " $\\text{SO}_3^{2-}$?"
        ),
        "options": [
            "$22$",
            "$24$",
            "$26$",
            "$32$",
        ],
        "correct_index": 2,
        "explanation": (
            "Sulfur (Group 16) contributes $6$ valence electrons, each of the"
            " three oxygen atoms (Group 16) contributes $6$ valence electrons,"
            " and the $2-$ ionic charge adds $2$ extra electrons: $6 + 3(6) + 2"
            " = 26$ valence electrons."
        ),
    },
    {
        "unit_q_num": 30,
        "topic_code": "2.5",
        "topic_title": "Lewis Diagrams",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "In the valid Lewis diagram of xenon tetrafluoride, $\\text{XeF}_4$,"
            " how many nonbonding lone pairs of electrons are located on the"
            " central xenon atom?"
        ),
        "options": [
            "$0$",
            "$1$",
            "$2$",
            "$3$",
        ],
        "correct_index": 2,
        "explanation": (
            "$\\text{XeF}_4$ has $8 + 4(7) = 36$ total valence electrons."
            " Forming four single $\\text{Xe}-\\text{F}$ bonds and completing"
            " the octets on the four terminal fluorine atoms uses $4 \\times 8"
            " = 32$ electrons. The remaining $36 - 32 = 4$ electrons are placed"
            " on the central $\\text{Xe}$ atom as $2$ lone pairs (an expanded"
            " valence shell with $12$ electrons around $\\text{Xe}$)."
        ),
    },
    {
        "unit_q_num": 31,
        "topic_code": "2.5",
        "topic_title": "Lewis Diagrams",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "Which of the following molecules has a central atom with an"
            " incomplete octet (fewer than $8$ valence electrons) in its most"
            " stable Lewis representation?"
        ),
        "options": [
            "$\\text{NH}_3$",
            "$\\text{BF}_3$",
            "$\\text{PF}_3$",
            "$\\text{BrF}_3$",
        ],
        "correct_index": 1,
        "explanation": (
            "Boron (Group 13) has $3$ valence electrons. In $\\text{BF}_3$"
            " ($3 + 3(7) = 24$ valence electrons), boron forms three single"
            " covalent bonds to the three fluorine atoms, giving boron $6$"
            " valence electrons (an incomplete octet) and zero formal charge on"
            " all atoms. By contrast, $\\text{NH}_3$ and $\\text{PF}_3$ have"
            " complete octets ($8$ electrons) on the central atom, and"
            " $\\text{BrF}_3$ has an expanded octet ($10$ electrons) on"
            " $\\text{Br}$."
        ),
    },
    {
        "unit_q_num": 32,
        "topic_code": "2.5",
        "topic_title": "Lewis Diagrams",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": (
            "Why does nitrogen form only $\\text{NF}_3$, whereas phosphorus"
            " (directly below nitrogen in Group 15) forms both $\\text{PF}_3$"
            " and $\\text{PF}_5$?"
        ),
        "options": [
            "Nitrogen is a Period 2 element whose valence shell ($n = 2$) contains only $2s$ and $2p$ orbitals (maximum of $8$ valence electrons), whereas Period 3 phosphorus can accommodate more than $8$ valence electrons.",
            "Nitrogen is less electronegative than phosphorus and cannot share five electron pairs.",
            "Fluorine atoms are too small to fit five around a larger phosphorus atom.",
            "$\\text{NF}_3$ is an ionic compound whereas $\\text{PF}_5$ is a metallic alloy.",
        ],
        "correct_index": 0,
        "explanation": (
            "Period 2 elements ($\\text{C}, \\text{N}, \\text{O}, \\text{F}$)"
            " have only four valence orbitals (one $2s$ and three $2p$"
            " orbitals) and therefore cannot exceed an octet (maximum of"
            " $8$ valence electrons). Period 3 and heavier elements (such as"
            " $\\text{P}$ in $n = 3$) are larger and can form hypervalent"
            " (expanded octet) species such as $\\text{PF}_5$ with $10$"
            " valence electrons around the central atom."
        ),
    },
    {
        "unit_q_num": 33,
        "topic_code": "2.5",
        "topic_title": "Lewis Diagrams",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "In the Lewis diagram for the triiodide ion, $\\text{I}_3^-$, how"
            " many lone pairs of electrons are on the CENTRAL iodine atom, and"
            " how many lone pairs are in the ENTIRE ion?"
        ),
        "options": [
            "$2$ on the central atom; $8$ in the entire ion",
            "$2$ on the central atom; $9$ in the entire ion",
            "$3$ on the central atom; $8$ in the entire ion",
            "$3$ on the central atom; $9$ in the entire ion",
        ],
        "correct_index": 3,
        "explanation": (
            "The $\\text{I}_3^-$ ion has $3(7) + 1 = 22$ valence electrons"
            " ($11$ pairs). Two single $\\text{I}-\\text{I}$ bonds use $2$"
            " pairs ($4$ electrons). Each of the two terminal $\\text{I}$"
            " atoms takes $3$ lone pairs ($6$ electrons) to complete its octet,"
            " using $6$ pairs ($12$ electrons). The remaining $11 - 2 - 6 = 3$"
            " lone pairs ($6$ electrons) are placed on the central $\\text{I}$"
            " atom. Thus, there are $3$ lone pairs on the central atom and"
            " $3 + 3 + 3 = 9$ lone pairs in the entire ion."
        ),
    },
    {
        "unit_q_num": 34,
        "topic_code": "2.5",
        "topic_title": "Lewis Diagrams",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Species</th><th>Chemical Formula</th></tr></thead>"
            "<tbody>"
            "<tr><td>Carbon monoxide</td><td>$\\text{CO}$</td></tr>"
            "<tr><td>Nitrogen dioxide</td><td>$\\text{NO}_2$</td></tr>"
            "<tr><td>Nitrous oxide</td><td>$\\text{N}_2\\text{O}$</td></tr>"
            "<tr><td>Sulfur dioxide</td><td>$\\text{SO}_2$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Which of the molecules listed in the table above is an"
            " odd-electron species (free radical) that cannot have all of its"
            " valence electrons paired in a Lewis diagram?"
        ),
        "options": [
            "$\\text{CO}$",
            "$\\text{NO}_2$",
            "$\\text{N}_2\\text{O}$",
            "$\\text{SO}_2$",
        ],
        "correct_index": 1,
        "explanation": (
            "Counting valence electrons for each molecule: $\\text{CO}$ has"
            " $4 + 6 = 10$ (even); $\\text{NO}_2$ has $5 + 2(6) = 17$ (odd);"
            " $\\text{N}_2\\text{O}$ has $2(5) + 6 = 16$ (even); and"
            " $\\text{SO}_2$ has $6 + 2(6) = 18$ (even). Because $\\text{NO}_2$"
            " has $17$ valence electrons, one electron must remain unpaired,"
            " making $\\text{NO}_2$ a free radical."
        ),
    },
    {
        "unit_q_num": 35,
        "topic_code": "2.5",
        "topic_title": "Lewis Diagrams",
        "difficulty": "Challenging",
        "stimulus": (
            '<div class="stimulus-formula">'
            "Condensed Formula of Acetonitrile: $\\text{CH}_3\\text{CN}$"
            "</div>"
        ),
        "question": (
            "When drawing the complete Lewis structure of acetonitrile,"
            " $\\text{CH}_3\\text{CN}$, how many total bonding electron pairs"
            " and how many nonbonding lone pairs are present in the molecule?"
        ),
        "options": [
            "$8$ bonding pairs and $0$ lone pairs",
            "$7$ bonding pairs and $1$ lone pair",
            "$6$ bonding pairs and $2$ lone pairs",
            "$5$ bonding pairs and $3$ lone pairs",
        ],
        "correct_index": 1,
        "explanation": (
            "Acetonitrile ($\\text{CH}_3\\text{CN}$) has $2(4) + 3(1) + 5 = 16$"
            " valence electrons ($8$ pairs). The methyl carbon forms three"
            " $\\text{C}-\\text{H}$ single bonds ($3$ pairs) and one"
            " $\\text{C}-\\text{C}$ single bond ($1$ pair) to the nitrile"
            " carbon, which forms a $\\text{C}\\equiv\\text{N}$ triple bond"
            " ($3$ pairs) to the nitrogen atom. That accounts for $3 + 1 + 3 ="
            " 7$ bonding pairs ($14$ electrons), leaving $1$ lone pair ($2$"
            " electrons) on the nitrogen atom."
        ),
    },
    # -------------------------------------------------------------------------
    # Topic 2.6: Resonance and Formal Charge (Q36 - Q42)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 36,
        "topic_code": "2.6",
        "topic_title": "Resonance and Formal Charge",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Resonance Structure</th><th>Bonds and Lone Pairs</th>"
            "<th>Formal Charges ($\\text{S}, \\text{C}, \\text{N}$)</th></tr></thead>"
            "<tbody>"
            "<tr><td>Structure I</td><td>$[\\text{S}-\\text{C}\\equiv\\text{N}]^-$; lone pairs: $3$ on $\\text{S}$, $1$ on $\\text{N}$</td>"
            "<td>$(-1,\\ 0,\\ 0)$</td></tr>"
            "<tr><td>Structure II</td><td>$[\\text{S}=\\text{C}=\\text{N}]^-$; lone pairs: $2$ on $\\text{S}$, $2$ on $\\text{N}$</td>"
            "<td>$(0,\\ 0,\\ -1)$</td></tr>"
            "<tr><td>Structure III</td><td>$[\\text{S}\\equiv\\text{C}-\\text{N}]^-$; lone pairs: $1$ on $\\text{S}$, $3$ on $\\text{N}$</td>"
            "<td>$(+1,\\ 0,\\ -2)$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Three possible resonance structures for the thiocyanate ion,"
            " $\\text{SCN}^-$ ($16$ valence electrons), are shown in the table"
            " above. Based on formal charge criteria and electronegativity"
            " ($\\text{EN of N} = 3.04$, $\\text{EN of S} = 2.58$), which"
            " statement correctly evaluates their relative contributions to the"
            " resonance hybrid?"
        ),
        "options": [
            "Structure III is the major contributor because sulfur has a $+1$ formal charge.",
            "Structure II is the major contributor because formal charges are minimized and the $-1$ formal charge resides on the more electronegative nitrogen atom.",
            "Structure I is the only valid contributor because carbon cannot form two double bonds.",
            "All three structures contribute equally ($33.3\\%$ each) to the resonance hybrid.",
        ],
        "correct_index": 1,
        "explanation": (
            "In evaluating non-equivalent resonance structures, the most stable"
            " contributor minimizes formal charge magnitudes and places any"
            " unavoidable negative formal charge on the most electronegative"
            " atom. Both Structure I and Structure II have two zero formal"
            " charges and one $-1$ formal charge, whereas Structure III has"
            " larger formal charges ($+1$ and $-2$). Because nitrogen"
            " ($\\text{EN} = 3.04$) is more electronegative than sulfur"
            " ($\\text{EN} = 2.58$), Structure II (with $-1$ on $\\text{N}$) is"
            " the dominant contributor."
        ),
    },
    {
        "unit_q_num": 37,
        "topic_code": "2.6",
        "topic_title": "Resonance and Formal Charge",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "In a Lewis diagram of the sulfate ion, $\\text{SO}_4^{2-}$, drawn"
            " such that the central sulfur atom obeys the strict octet rule"
            " (forming four single $\\text{S}-\\text{O}$ bonds), what are the"
            " formal charges on the sulfur atom and on each oxygen atom?"
        ),
        "options": [
            "$\\text{S}: -2$, each $\\text{O}: 0$",
            "$\\text{S}: 0$, each $\\text{O}: -0.5$",
            "$\\text{S}: +1$, each $\\text{O}: -1$",
            "$\\text{S}: +2$, each $\\text{O}: -1$",
        ],
        "correct_index": 3,
        "explanation": (
            "Using $\\text{Formal Charge} = \\text{Valence } e^- - (\\text{Nonbonding } e^-"
            " + \\frac{1}{2}\\text{Bonding } e^-)$: for sulfur (Group 16, $6$"
            " valence electrons) with $4$ single bonds and $0$ lone pairs,"
            " $\\text{FC}(\\text{S}) = 6 - (0 + 4) = +2$. For each singly"
            " bonded oxygen (Group 16, $6$ valence electrons) with $1$ single"
            " bond and $3$ lone pairs ($6$ nonbonding electrons),"
            " $\\text{FC}(\\text{O}) = 6 - (6 + 1) = -1$. Note that the sum of"
            " formal charges is $+2 + 4(-1) = -2$, matching the overall ion"
            " charge."
        ),
    },
    {
        "unit_q_num": 38,
        "topic_code": "2.6",
        "topic_title": "Resonance and Formal Charge",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Chemical Species</th><th>Formula</th></tr></thead>"
            "<tbody>"
            "<tr><td>Nitrite ion</td><td>$\\text{NO}_2^-$</td></tr>"
            "<tr><td>Nitrate ion</td><td>$\\text{NO}_3^-$</td></tr>"
            "<tr><td>Nitrosyl fluoride (N–O bond)</td><td>$\\text{ONF}$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Based on the Lewis structures and resonance hybrids of the three"
            " nitrogen-oxygen species listed in the table above, which choice"
            " correctly ranks them in order of INCREASING nitrogen-oxygen bond"
            " length?"
        ),
        "options": [
            "$\\text{ONF} < \\text{NO}_2^- < \\text{NO}_3^-$",
            "$\\text{NO}_3^- < \\text{NO}_2^- < \\text{ONF}$",
            "$\\text{NO}_2^- < \\text{ONF} < \\text{NO}_3^-$",
            "$\\text{ONF} < \\text{NO}_3^- < \\text{NO}_2^-$",
        ],
        "correct_index": 0,
        "explanation": (
            "Determine the N–O bond order in each species: In $\\text{ONF}$"
            " ($18$ valence electrons, $\\text{O}=\\text{N}-\\text{F}$ with one"
            " lone pair on $\\text{N}$), the $\\text{N}=\\text{O}$ bond is a"
            " localized double bond (bond order $= 2.0$). In $\\text{NO}_2^-$"
            " ($18$ valence electrons, $2$ resonance structures), the N–O bond"
            " order is $(2 + 1)/2 = 1.5$. In $\\text{NO}_3^-$ ($24$ valence"
            " electrons, $3$ resonance structures), the N–O bond order is"
            " $(2 + 1 + 1)/3 = 1.33$. Because bond length increases as bond"
            " order decreases, the N–O bond length increases in the order:"
            " $\\text{ONF}$ (BO $2.0$) $< \\text{NO}_2^-$ (BO $1.5$) $<"
            " \\text{NO}_3^-$ (BO $1.33$)."
        ),
    },
    {
        "unit_q_num": 39,
        "topic_code": "2.6",
        "topic_title": "Resonance and Formal Charge",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": (
            "Nitrous oxide, $\\text{N}_2\\text{O}$ ($16$ valence electrons),"
            " is a linear molecule with the atomic connectivity"
            " $\\text{N}-\\text{N}-\\text{O}$. Its two major resonance structures"
            " are $\\text{N}\\equiv\\text{N}-\\text{O}$ (one lone pair on the"
            " terminal $\\text{N}$, three lone pairs on $\\text{O}$) and"
            " $\\text{N}=\\text{N}=\\text{O}$ (two lone pairs on each terminal"
            " atom). In both structures, what is the formal charge on the"
            " CENTRAL nitrogen atom?"
        ),
        "options": [
            "$-1$",
            "$0$",
            "$+1$",
            "$+2$",
        ],
        "correct_index": 2,
        "explanation": (
            "In both major resonance structures of $\\text{N}_2\\text{O}$, the"
            " central nitrogen atom forms $4$ covalent bonds ($8$ bonding"
            " electrons) and has $0$ lone pairs. Because nitrogen is in Group"
            " 15 ($5$ valence electrons), the formal charge on the central"
            " nitrogen atom is $5 - (0 + 4) = +1$."
        ),
    },
    {
        "unit_q_num": 40,
        "topic_code": "2.6",
        "topic_title": "Resonance and Formal Charge",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "Which of the following statements best describes the true"
            " electronic structure of a molecule such as ozone, $\\text{O}_3$,"
            " that exhibits resonance?"
        ),
        "options": [
            "Ozone rapidly flips back and forth between two distinct structures, each having one single bond and one double bond.",
            "A sample of ozone gas is a $50:50$ mixture of two different isomers with different bond lengths.",
            "Ozone exists as a single resonance hybrid in which the $\\pi$ bonding electrons are delocalized equally over both $\\text{O}-\\text{O}$ bonds, giving each bond a bond order of $1.5$.",
            "Ozone forms a three-membered cyclic ring with three equivalent $\\text{O}-\\text{O}$ single bonds.",
        ],
        "correct_index": 2,
        "explanation": (
            "Resonance structures do not oscillate or equilibrate; rather, a"
            " single Lewis structure is inadequate to represent delocalized"
            " electrons. The true structure of $\\text{O}_3$ is a single,"
            " static resonance hybrid in which the $\\pi$ bond is delocalized"
            " across all three oxygen atoms, making both $\\text{O}-\\text{O}$"
            " bonds identical in length and strength with a bond order of"
            " $1.5$."
        ),
    },
    {
        "unit_q_num": 41,
        "topic_code": "2.6",
        "topic_title": "Resonance and Formal Charge",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": (
            "The cyanate ion, $\\text{OCN}^-$, and the fulminate ion,"
            " $\\text{CNO}^-$, are structural isomers with $16$ valence"
            " electrons each. Fulminate salts are explosive, whereas cyanate"
            " salts are stable. Based on formal charge analysis of their best"
            " octet-obeying resonance structures, why is $\\text{OCN}^-$ much"
            " more stable than $\\text{CNO}^-$?"
        ),
        "options": [
            "In $\\text{OCN}^-$, all atoms have formal charges of $0$ or $-1$ (with $-1$ on $\\text{O}$), whereas in $\\text{CNO}^-$ the central nitrogen has a $+1$ formal charge and carbon carries a $-1$ or $-2$ formal charge.",
            "$\\text{OCN}^-$ contains $18$ valence electrons whereas $\\text{CNO}^-$ contains only $14$ valence electrons.",
            "$\\text{OCN}^-$ is bent with $sp^3$ hybridization whereas $\\text{CNO}^-$ is linear.",
            "Oxygen can form triple bonds in $\\text{CNO}^-$ with zero formal charge.",
        ],
        "correct_index": 0,
        "explanation": (
            "In the cyanate ion ($\\text{OCN}^-$, connectivity"
            " $\\text{O}-\\text{C}-\\text{N}$), the major resonance contributor"
            " $[\\text{O}-\\text{C}\\equiv\\text{N}]^-$ (three lone pairs on $\\text{O}$, one on $\\text{N}$) has formal"
            " charges of $-1$ on the highly electronegative $\\text{O}$ atom"
            " and $0$ on both $\\text{C}$ and $\\text{N}$. In the fulminate"
            " ion ($\\text{CNO}^-$, connectivity $\\text{C}-\\text{N}-\\text{O}$),"
            " every octet-satisfying resonance structure has nonzero formal"
            " charges on multiple atoms, including $+1$ on the central"
            " $\\text{N}$ and a negative formal charge ($-1$ or $-2$) on the"
            " less electronegative carbon atom, making $\\text{CNO}^-$ unstable."
        ),
    },
    {
        "unit_q_num": 42,
        "topic_code": "2.6",
        "topic_title": "Resonance and Formal Charge",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "In the formate ion, $\\text{HCO}_2^-$, the central carbon atom is"
            " bonded to one hydrogen atom and two oxygen atoms. What is the"
            " carbon-oxygen bond order in $\\text{HCO}_2^-$?"
        ),
        "options": [
            "$1.0$",
            "$1.33$",
            "$1.5$",
            "$2.0$",
        ],
        "correct_index": 2,
        "explanation": (
            "The formate ion ($\\text{HCO}_2^-$) has $1 + 4 + 2(6) + 1 = 18$"
            " valence electrons. Carbon forms a single bond to $\\text{H}$ and"
            " is bonded to two equivalent oxygen atoms via two equally"
            " contributing resonance structures (one $\\text{C}=\\text{O}$"
            " double bond and one $\\text{C}-\\text{O}^-$ single bond). The"
            " delocalized $\\pi$ bond gives each $\\text{C}-\\text{O}$ bond an"
            " identical bond order of $(2 + 1)/2 = 1.5$."
        ),
    },
    # -------------------------------------------------------------------------
    # Topic 2.7: VSEPR and Hybridization (Q43 - Q50)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 43,
        "topic_code": "2.7",
        "topic_title": "VSEPR and Hybridization",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Molecule</th><th>Total Valence Electrons</th>"
            "<th>Electron Domains on Central Atom</th></tr></thead>"
            "<tbody>"
            "<tr><td>$\\text{SF}_4$</td><td>$34$</td><td>$5$</td></tr>"
            "<tr><td>$\\text{XeF}_4$</td><td>$36$</td><td>$6$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Using VSEPR theory and the information in the table above, what"
            " are the molecular geometries of $\\text{SF}_4$ and $\\text{XeF}_4$,"
            " and which of the two molecules is polar?"
        ),
        "options": [
            "$\\text{SF}_4$ is tetrahedral and nonpolar; $\\text{XeF}_4$ is seesaw and polar.",
            "$\\text{SF}_4$ is seesaw and polar; $\\text{XeF}_4$ is square planar and nonpolar.",
            "$\\text{SF}_4$ is square planar and nonpolar; $\\text{XeF}_4$ is octahedral and nonpolar.",
            "Both $\\text{SF}_4$ and $\\text{XeF}_4$ are seesaw and polar.",
        ],
        "correct_index": 1,
        "explanation": (
            "In $\\text{SF}_4$ ($34$ valence electrons), the central $\\text{S}$"
            " atom has $4$ bonding pairs and $1$ lone pair ($5$ electron"
            " domains, trigonal bipyramidal electron-domain geometry). The lone"
            " pair occupies an equatorial position, producing an asymmetrical"
            " seesaw molecular geometry in which the bond dipoles do not cancel"
            " (polar). In $\\text{XeF}_4$ ($36$ valence electrons), the central"
            " $\\text{Xe}$ atom has $4$ bonding pairs and $2$ lone pairs ($6$"
            " electron domains, octahedral electron-domain geometry). The two"
            " lone pairs occupy opposite (trans, $180^\\circ$) positions,"
            " producing a symmetrical square planar molecular geometry in which"
            " all four $\\text{Xe}-\\text{F}$ bond dipoles cancel (nonpolar)."
        ),
    },
    {
        "unit_q_num": 44,
        "topic_code": "2.7",
        "topic_title": "VSEPR and Hybridization",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Hydride</th><th>Formula</th></tr></thead>"
            "<tbody>"
            "<tr><td>Methane</td><td>$\\text{CH}_4$</td></tr>"
            "<tr><td>Ammonia</td><td>$\\text{NH}_3$</td></tr>"
            "<tr><td>Water</td><td>$\\text{H}_2\\text{O}$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "All three hydrides in the table above have $4$ electron domains"
            " (tetrahedral electron-domain geometry) around the central atom."
            " Which choice gives their correct bond angles and explains the"
            " trend?"
        ),
        "options": [
            "$\\text{H}_2\\text{O} (104.5^\\circ) < \\text{NH}_3 (107^\\circ) < \\text{CH}_4 (109.5^\\circ)$, because nonbonding lone pairs occupy more space than bonding pairs and compress the bonding angles.",
            "$\\text{CH}_4 (109.5^\\circ) < \\text{NH}_3 (120^\\circ) < \\text{H}_2\\text{O} (180^\\circ)$, because having fewer hydrogen atoms allows the bonds to spread out.",
            "$\\text{CH}_4 = \\text{NH}_3 = \\text{H}_2\\text{O} = 109.5^\\circ$, because all three central atoms are $sp^3$ hybridized.",
            "$\\text{NH}_3 (90^\\circ) < \\text{H}_2\\text{O} (104.5^\\circ) < \\text{CH}_4 (109.5^\\circ)$, because nitrogen has the highest electronegativity.",
        ],
        "correct_index": 0,
        "explanation": (
            "$\\text{CH}_4$ has $0$ lone pairs ($109.5^\\circ$), $\\text{NH}_3$"
            " has $1$ lone pair ($\\sim 107^\\circ$), and $\\text{H}_2\\text{O}$"
            " has $2$ lone pairs ($\\sim 104.5^\\circ$). Because a nonbonding"
            " lone pair is attracted by only one nucleus rather than two, its"
            " electron cloud spreads out over a larger angular volume near the"
            " central atom. Repulsions follow the order: lone pair–lone pair $>$"
            " lone pair–bonding pair $>$ bonding pair–bonding pair, compressing"
            " the $\\text{H}-\\text{X}-\\text{H}$ bond angle as the number of"
            " lone pairs increases."
        ),
    },
    {
        "unit_q_num": 45,
        "topic_code": "2.7",
        "topic_title": "VSEPR and Hybridization",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="stimulus-formula">'
            "Structural Formula of Acrylonitrile: "
            "$\\text{H}_2\\text{C}_a=\\text{C}_b\\text{H}-\\text{C}_c\\equiv\\text{N}:$"
            "</div>"
        ),
        "question": (
            "Consider the structural formula of acrylonitrile,"
            " $\\text{H}_2\\text{C}=\\text{CH}-\\text{C}\\equiv\\text{N}$,"
            " shown above. What are the hybridizations of carbon atoms"
            " $\\text{C}_a$ and $\\text{C}_c$, and what are the total numbers"
            " of $\\sigma$ (sigma) and $\\pi$ (pi) bonds in one molecule of"
            " acrylonitrile?"
        ),
        "options": [
            "$\\text{C}_a: sp^2$, $\\text{C}_c: sp$; $6\\ \\sigma$ bonds and $3\\ \\pi$ bonds",
            "$\\text{C}_a: sp^3$, $\\text{C}_c: sp^2$; $6\\ \\sigma$ bonds and $2\\ \\pi$ bonds",
            "$\\text{C}_a: sp^2$, $\\text{C}_c: sp$; $5\\ \\sigma$ bonds and $4\\ \\pi$ bonds",
            "$\\text{C}_a: sp$, $\\text{C}_c: sp^2$; $9\\ \\sigma$ bonds and $0\\ \\pi$ bonds",
        ],
        "correct_index": 0,
        "explanation": (
            "Carbon $\\text{C}_a$ is bonded to $3$ atoms ($2\\ \\text{H}$ and"
            " $\\text{C}_b$) with $0$ lone pairs ($3$ electron domains), so it"
            " is $sp^2$ hybridized. Carbon $\\text{C}_c$ is bonded to $2$ atoms"
            " ($\\text{C}_b$ and $\\text{N}$) with $0$ lone pairs ($2$ electron"
            " domains), so it is $sp$ hybridized. Counting $\\sigma$ and $\\pi$"
            " bonds: there are three $\\text{C}-\\text{H}$ single bonds ($3\\ \\sigma$),"
            " one $\\text{C}_b-\\text{C}_c$ single bond ($1\\ \\sigma$), one"
            " $\\text{C}_a=\\text{C}_b$ double bond ($1\\ \\sigma + 1\\ \\pi$),"
            " and one $\\text{C}_c\\equiv\\text{N}$ triple bond ($1\\ \\sigma +"
            " 2\\ \\pi$). In total, there are $3 + 1 + 1 + 1 = 6\\ \\sigma$"
            " bonds and $1 + 2 = 3\\ \\pi$ bonds."
        ),
    },
    {
        "unit_q_num": 46,
        "topic_code": "2.7",
        "topic_title": "VSEPR and Hybridization",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "Which of the following molecules has polar covalent bonds but a"
            " net molecular dipole moment of zero (is a nonpolar molecule)?"
        ),
        "options": [
            "$\\text{SO}_2$",
            "$\\text{CH}_2\\text{Cl}_2$",
            "$\\text{NF}_3$",
            "$\\text{PF}_5$",
        ],
        "correct_index": 3,
        "explanation": (
            "In $\\text{PF}_5$ ($40$ valence electrons), the central"
            " phosphorus atom is surrounded by $5$ identical $\\text{P}-\\text{F}$"
            " bonding pairs and $0$ lone pairs in a symmetrical trigonal"
            " bipyramidal geometry. The three equatorial $\\text{P}-\\text{F}$"
            " bond dipoles ($120^\\circ$ apart) cancel in the horizontal plane,"
            " and the two axial $\\text{P}-\\text{F}$ bond dipoles ($180^\\circ$"
            " apart) cancel vertically, giving a net dipole moment of zero."
            " By contrast, $\\text{SO}_2$ (bent), $\\text{CH}_2\\text{Cl}_2$"
            " (tetrahedral with non-identical substituents), and $\\text{NF}_3$"
            " (trigonal pyramidal) are all polar molecules."
        ),
    },
    {
        "unit_q_num": 47,
        "topic_code": "2.7",
        "topic_title": "VSEPR and Hybridization",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": (
            "What is the molecular geometry and the approximate"
            " $\\text{F}-\\text{Cl}-\\text{F}$ bond angle in chlorine"
            " trifluoride, $\\text{ClF}_3$?"
        ),
        "options": [
            "Trigonal planar; $120^\\circ$",
            "Trigonal pyramidal; $107^\\circ$",
            "Seesaw; $90^\\circ$ and $120^\\circ$",
            "T-shaped; slightly less than $90^\\circ$ (and $<180^\\circ$)",
        ],
        "correct_index": 3,
        "explanation": (
            "$\\text{ClF}_3$ has $7 + 3(7) = 28$ valence electrons. After"
            " forming $3\\ \\text{Cl}-\\text{F}$ single bonds and completing"
            " octets on the $3\\ \\text{F}$ atoms ($24$ electrons), $4$"
            " electrons ($2$ lone pairs) remain on the central $\\text{Cl}$"
            " atom. With $3$ bonding domains and $2$ lone pairs ($5$ total"
            " electron domains, trigonal bipyramidal electron-domain geometry),"
            " the two lone pairs occupy equatorial positions to minimize"
            " $90^\\circ$ repulsions, leaving the three $\\text{F}$ atoms in a"
            " T-shaped molecular geometry with axial-equatorial"
            " $\\text{F}-\\text{Cl}-\\text{F}$ bond angles compressed slightly"
            " below $90^\\circ$."
        ),
    },
    {
        "unit_q_num": 48,
        "topic_code": "2.7",
        "topic_title": "VSEPR and Hybridization",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="stimulus-formula">'
            "Structural Formula of Acetic Acid: "
            "$\\text{H}_3\\text{C}_1-\\text{C}_2(=\\text{O}_a)-\\text{O}_b-\\text{H}$"
            "</div>"
        ),
        "question": (
            "In the acetic acid molecule ($\\text{CH}_3\\text{COOH}$) shown"
            " above, what are the hybridizations of $\\text{C}_1$, $\\text{C}_2$,"
            " and the hydroxyl oxygen $\\text{O}_b$ (which has two lone pairs)?"
        ),
        "options": [
            "$\\text{C}_1: sp^3$, $\\text{C}_2: sp^2$, $\\text{O}_b: sp^3$",
            "$\\text{C}_1: sp^3$, $\\text{C}_2: sp^3$, $\\text{O}_b: sp^2$",
            "$\\text{C}_1: sp^2$, $\\text{C}_2: sp^2$, $\\text{O}_b: sp$",
            "$\\text{C}_1: sp^3$, $\\text{C}_2: sp$, $\\text{O}_b: sp^3$",
        ],
        "correct_index": 0,
        "explanation": (
            "Count the electron domains around each specified atom: $\\text{C}_1$"
            " is bonded to $3\\ \\text{H}$ atoms and $\\text{C}_2$ ($4$"
            " electron domains $\\rightarrow sp^3$). $\\text{C}_2$ is bonded to"
            " $\\text{C}_1$, $\\text{O}_a$ (via a double bond), and"
            " $\\text{O}_b$ ($3$ electron domains $\\rightarrow sp^2$). The"
            " hydroxyl oxygen $\\text{O}_b$ is bonded to $\\text{C}_2$ and"
            " $\\text{H}$ and has $2$ lone pairs ($2 + 2 = 4$ electron domains"
            " in standard VSEPR counting $\\rightarrow sp^3$)."
        ),
    },
    {
        "unit_q_num": 49,
        "topic_code": "2.7",
        "topic_title": "VSEPR and Hybridization",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": (
            "In 2-butene, $\\text{CH}_3\\text{CH}=\\text{CHCH}_3$, the"
            " cis isomer and trans isomer do not interconvert at room"
            " temperature, whereas rotation around the central"
            " $\\text{C}-\\text{C}$ bond in butane,"
            " $\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}_3$, occurs freely."
            " Why is rotation around the $\\text{C}=\\text{C}$ double bond in"
            " 2-butene restricted?"
        ),
        "options": [
            "The $\\sigma$ bond in a double bond is formed by $d$-orbital overlap, which locks the nuclei in place.",
            "The two methyl groups form an ionic bond across the double bond.",
            "$sp^2$ hybridized carbon atoms have no valence electrons available for rotation.",
            "Rotating one $\\text{CH}_3\\text{CH}$ group by $90^\\circ$ relative to the other requires breaking the side-by-side overlap of the unhybridized $p$ orbitals that form the $\\pi$ bond.",
        ],
        "correct_index": 3,
        "explanation": (
            "A $\\sigma$ bond has cylindrical symmetry along the internuclear"
            " axis, so rotation around a single bond does not reduce orbital"
            " overlap. By contrast, a $\\pi$ bond is formed by the side-by-side"
            " overlap of parallel unhybridized $p$ orbitals above and below the"
            " internuclear axis. Rotating one carbon relative to the other"
            " twists the $p$ orbitals out of parallel alignment, destroying"
            " the $\\pi$ overlap and requiring a large input of energy"
            " ($\\sim 260\\text{ kJ/mol}$)."
        ),
    },
    {
        "unit_q_num": 50,
        "topic_code": "2.7",
        "topic_title": "VSEPR and Hybridization",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Species</th><th>Formula</th></tr></thead>"
            "<tbody>"
            "<tr><td>Carbon dioxide</td><td>$\\text{CO}_2$</td></tr>"
            "<tr><td>Azide ion</td><td>$\\text{N}_3^-$</td></tr>"
            "<tr><td>Ozone</td><td>$\\text{O}_3$</td></tr>"
            "<tr><td>Xenon difluoride</td><td>$\\text{XeF}_2$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Which of the triatomic species in the table above have a LINEAR"
            " molecular geometry?"
        ),
        "options": [
            "$\\text{CO}_2$ and $\\text{N}_3^-$ only",
            "$\\text{CO}_2$, $\\text{N}_3^-$, and $\\text{XeF}_2$ only",
            "$\\text{O}_3$ and $\\text{XeF}_2$ only",
            "$\\text{CO}_2$, $\\text{N}_3^-$, $\\text{O}_3$, and $\\text{XeF}_2$",
        ],
        "correct_index": 1,
        "explanation": (
            "Evaluate the electron domains on the central atom of each species:"
            " $\\text{CO}_2$ ($16\\ e^-$) and $\\text{N}_3^-$ ($16\\ e^-$) are"
            " isoelectronic, with $2$ bonding domains and $0$ lone pairs on the"
            " central atom $\\rightarrow$ linear ($180^\\circ$). $\\text{O}_3$"
            " ($18\\ e^-$) has $2$ bonding domains and $1$ lone pair on the"
            " central $\\text{O}$ atom ($3$ electron domains, trigonal planar"
            " electron-domain geometry) $\\rightarrow$ bent ($<120^\\circ$)."
            " $\\text{XeF}_2$ ($22\\ e^-$) has $2$ bonding domains and $3$ lone"
            " pairs on the central $\\text{Xe}$ atom ($5$ electron domains,"
            " trigonal bipyramidal electron-domain geometry); the $3$ lone"
            " pairs occupy the three equatorial positions, leaving the two"
            " $\\text{F}$ atoms in the axial positions $\\rightarrow$ linear"
            " ($180^\\circ$). Thus, $\\text{CO}_2$, $\\text{N}_3^-$, and"
            " $\\text{XeF}_2$ are linear."
        ),
    },
    # -------------------------------------------------------------------------
    # Added 2026-10-03 — Blind-spot coverage (Fall 2024 CED): topics 2.1–2.7
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 51,
        "topic_code": "2.1",
        "topic_title": "Types of Chemical Bonds",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"The electronegativities of nitrogen, oxygen, and sulfur are $3.04$, $3.44$, and $2.58$, respectively. Which of the following best explains why oxygen is more electronegative than both nitrogen and sulfur?"
        ),
        "options": [
            r"Oxygen has the greatest number of protons of the three atoms, so its nucleus attracts bonding electrons most strongly.",
            r"Oxygen has more valence electrons than either nitrogen or sulfur, so it attracts bonding electrons more strongly.",
            r"An $\text{O}$ atom has one more proton than an $\text{N}$ atom but the same number of core electrons, and its valence electrons are closer to the nucleus than those of an $\text{S}$ atom ($n = 2$ vs. $n = 3$), so $\text{O}$ attracts bonding electrons more strongly than either atom does.",
            r"Oxygen has the fewest electrons of the three atoms, so it has the smallest radius and attracts bonding electrons most strongly.",
        ],
        "correct_index": 2,
        "explanation": (
            r"By Coulomb's law, an atom's attraction for bonding electrons increases with the net nuclear charge felt by its valence electrons and decreases as their distance from the nucleus increases. $\text{N}$ ($7$ protons) and $\text{O}$ ($8$ protons) both have $2$ core electrons ($1s^2$) and valence electrons in the $n = 2$ shell, so the valence electrons of $\text{O}$ feel a greater net nuclear charge at a similar distance. $\text{S}$ has more protons ($16$) but also $10$ core electrons, and its valence electrons are in the $n = 3$ shell, farther from the nucleus, so its attraction is weaker. Proton count alone fails ($\text{S}$ has more protons than $\text{O}$), $\text{O}$ and $\text{S}$ have the same number of valence electrons ($6$), and $\text{N}$ ($7$ electrons) has fewer electrons than $\text{O}$ ($8$)."
        ),
    },
    {
        "unit_q_num": 52,
        "topic_code": "2.1",
        "topic_title": "Types of Chemical Bonds",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"A student is given two unlabeled white crystalline solids. One is sodium chloride, $\text{NaCl}$, and the other is sucrose, $\text{C}_{12}\text{H}_{22}\text{O}_{11}$. Both solids dissolve readily in water. Which of the following procedures would best allow the student to identify the sample of the ionic compound?"
        ),
        "options": [
            r"Test whether each solid conducts electricity at room temperature.",
            r"Add each solid to water and observe whether it dissolves.",
            r"Examine each solid with a magnifying lens to determine whether it consists of crystals with flat faces.",
            r"Dissolve each solid in distilled water and test whether the resulting solution conducts electricity.",
        ],
        "correct_index": 3,
        "explanation": (
            r"Examining properties is the best way to characterize the type of bonding in a substance, but the property tested must differ between the two samples. Dissolving $\text{NaCl}$ releases mobile $\text{Na}^+$ and $\text{Cl}^-$ ions, so its solution conducts electricity; sucrose dissolves as neutral molecules, so its solution does not conduct. Testing the solids at room temperature does not distinguish them: the ions in solid $\text{NaCl}$ are held in fixed positions, so neither solid conducts. Both solids are already known to dissolve, and both are crystalline, so solubility and crystal shape give no distinction. Distilled water is used so that ions dissolved in tap water do not make both solutions conduct."
        ),
    },
    {
        "unit_q_num": 53,
        "topic_code": "2.2",
        "topic_title": "Intramolecular Force and Potential Energy",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<figure class="quiz-figure-wrap">'
            r'<svg xmlns="http://www.w3.org/2000/svg" class="quiz-figure" viewBox="0 0 520 320" role="img" aria-label="Graph of potential energy in kJ per mol versus internuclear distance in pm for an H atom and a Cl atom. The curve falls steeply from high positive values, crosses zero near 90 pm, reaches a minimum of minus 431 kJ per mol at 127 pm, then rises gradually toward zero at large distances.">'
            r'<line x1="70" y1="120" x2="490" y2="120" stroke="#9ca3af" stroke-width="1" stroke-dasharray="4 4"/>'
            r'<line x1="70" y1="30" x2="70" y2="270" stroke="#374151" stroke-width="1.5"/>'
            r'<line x1="70" y1="270" x2="490" y2="270" stroke="#374151" stroke-width="1.5"/>'
            r'<line x1="70" y1="270" x2="70" y2="275" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="70" y="288" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="middle">0</text>'
            r'<line x1="122.5" y1="270" x2="122.5" y2="275" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="122.5" y="288" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="middle">50</text>'
            r'<line x1="175" y1="270" x2="175" y2="275" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="175" y="288" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="middle">100</text>'
            r'<line x1="227.5" y1="270" x2="227.5" y2="275" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="227.5" y="288" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="middle">150</text>'
            r'<line x1="280" y1="270" x2="280" y2="275" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="280" y="288" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="middle">200</text>'
            r'<line x1="332.5" y1="270" x2="332.5" y2="275" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="332.5" y="288" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="middle">250</text>'
            r'<line x1="385" y1="270" x2="385" y2="275" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="385" y="288" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="middle">300</text>'
            r'<line x1="437.5" y1="270" x2="437.5" y2="275" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="437.5" y="288" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="middle">350</text>'
            r'<line x1="490" y1="270" x2="490" y2="275" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="490" y="288" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="middle">400</text>'
            r'<line x1="65" y1="270" x2="70" y2="270" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="62" y="274" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="end">−500</text>'
            r'<line x1="65" y1="240" x2="70" y2="240" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="62" y="244" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="end">−400</text>'
            r'<line x1="65" y1="210" x2="70" y2="210" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="62" y="214" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="end">−300</text>'
            r'<line x1="65" y1="180" x2="70" y2="180" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="62" y="184" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="end">−200</text>'
            r'<line x1="65" y1="150" x2="70" y2="150" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="62" y="154" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="end">−100</text>'
            r'<line x1="65" y1="120" x2="70" y2="120" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="62" y="124" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="end">0</text>'
            r'<line x1="65" y1="90" x2="70" y2="90" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="62" y="94" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="end">100</text>'
            r'<line x1="65" y1="60" x2="70" y2="60" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="62" y="64" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="end">200</text>'
            r'<line x1="65" y1="30" x2="70" y2="30" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="62" y="34" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="end">300</text>'
            r'<text x="280" y="308" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Internuclear distance (pm)</text>'
            r'<text x="20" y="150" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle" transform="rotate(-90 20 150)">Potential energy (kJ/mol)</text>'
            r'<polyline points="156.5,30 157.1,37.2 157.6,44.1 158.1,50.9 158.6,57.5 159.2,64 159.7,70.3 160.2,76.4 160.7,82.3 161.3,88.1 161.8,93.8 162.3,99.2 162.8,104.6 163.4,109.8 163.9,114.8 164.4,119.7 164.9,124.5 165.5,129.1 166,133.7 166.5,138 167,142.3 167.6,146.4 168.1,150.5 168.6,154.4 169.1,158.2 169.7,161.8 170.2,165.4 170.7,168.9 171.2,172.2 171.8,175.5 172.3,178.6 172.8,181.7 173.3,184.7 173.9,187.5 174.4,190.3 174.9,193 175.4,195.6 176,198.1 176.5,200.6 177,202.9 177.5,205.2 178.1,207.4 178.6,209.5 179.1,211.6 179.6,213.6 180.2,215.5 180.7,217.3 181.2,219.1 181.7,220.8 182.3,222.4 182.8,224 183.3,225.5 183.8,226.9 184.4,228.3 184.9,229.7 185.4,231 185.9,232.2 186.5,233.4 187,234.5 187.5,235.5 188,236.6 188.6,237.5 189.1,238.5 189.6,239.3 190.1,240.2 190.7,241 191.2,241.7 191.7,242.4 192.2,243.1 192.8,243.7 193.3,244.3 193.8,244.9 194.3,245.4 194.9,245.8 195.4,246.3 195.9,246.7 196.4,247.1 197,247.4 197.5,247.7 198,248 198.5,248.3 199.1,248.5 199.6,248.7 200.1,248.8 200.6,249 201.2,249.1 201.7,249.2 202.2,249.2 202.7,249.3 203.3,249.3 203.8,249.3 204.3,249.3 204.8,249.2 205.4,249.1 205.9,249 206.4,248.9 206.9,248.8 207.5,248.7 208,248.5 208.5,248.3 209,248.1 209.6,247.9 210.1,247.7 210.6,247.4 211.1,247.1 211.7,246.9 212.2,246.6 212.7,246.3 213.2,245.9 213.8,245.6 214.3,245.3 214.8,244.9 215.3,244.5 215.9,244.1 216.4,243.8 216.9,243.4 217.4,242.9 218,242.5 218.5,242.1 219,241.6 219.5,241.2 220.1,240.7 220.6,240.3 221.1,239.8 221.6,239.3 222.2,238.8 222.7,238.3 223.2,237.8 223.7,237.3 224.3,236.8 224.8,236.3 225.3,235.8 225.8,235.2 226.4,234.7 226.9,234.2 227.4,233.6 227.9,233.1 228.5,232.5 229,231.9 229.5,231.4 230,230.8 230.6,230.2 231.1,229.7 231.6,229.1 232.1,228.5 232.7,227.9 233.2,227.3 233.7,226.8 234.2,226.2 234.8,225.6 235.3,225 235.8,224.4 236.3,223.8 236.9,223.2 237.4,222.6 237.9,222 238.4,221.4 239,220.8 239.5,220.2 240,219.6 240.5,219 241.1,218.4 241.6,217.8 242.1,217.2 242.6,216.6 243.2,216 243.7,215.4 244.2,214.8 244.7,214.1 245.3,213.5 245.8,212.9 246.3,212.3 246.8,211.7 247.4,211.1 247.9,210.5 248.4,209.9 248.9,209.3 253.1,204.6 257.3,200 261.5,195.5 265.7,191.1 269.9,186.9 274.1,182.9 278.3,179.1 282.5,175.4 286.7,171.9 290.9,168.6 295.1,165.5 299.3,162.6 303.5,159.8 307.7,157.2 311.9,154.7 316.1,152.4 320.3,150.2 324.5,148.2 328.7,146.2 332.9,144.4 337.1,142.8 341.3,141.2 345.5,139.7 349.7,138.4 353.9,137.1 358.1,135.9 362.3,134.8 366.5,133.8 370.7,132.8 374.9,131.9 379.1,131.1 383.3,130.3 387.5,129.5 391.7,128.9 395.9,128.2 400.1,127.7 404.3,127.1 408.5,126.6 412.7,126.1 416.9,125.7 421.1,125.3 425.3,124.9 429.5,124.6 433.7,124.2 437.9,123.9 442.1,123.7 446.3,123.4 450.5,123.1 454.7,122.9 458.9,122.7 463.1,122.5 467.3,122.3 471.5,122.2 475.7,122 479.9,121.9 484.1,121.7 488.3,121.6 490,121.6" fill="none" stroke="#111827" stroke-width="2.2" stroke-linejoin="round"/>'
            r'<line x1="203.3" y1="249.3" x2="203.3" y2="270" stroke="#374151" stroke-width="1.2" stroke-dasharray="3 3"/>'
            r'<line x1="70" y1="249.3" x2="203.3" y2="249.3" stroke="#374151" stroke-width="1.2" stroke-dasharray="3 3"/>'
            r'<circle cx="203.3" cy="249.3" r="3.5" fill="#111827"/>'
            r'<text x="217.3" y="261.3" font-family="sans-serif" font-size="12" fill="#111827">minimum: 127 pm, −431 kJ/mol</text>'
            r'</svg>'
            r'<figcaption>Figure: Potential energy of an H atom and a Cl atom as a function of the distance between their nuclei</figcaption>'
            '</figure>'
        ),
        "question": (
            r"The graph above shows the potential energy of a system of one hydrogen atom and one chlorine atom as a function of the distance between their nuclei. Which of the following is best supported by the graph?"
        ),
        "options": [
            r"The $\text{H}-\text{Cl}$ bond length is $127\text{ pm}$, and $431\text{ kJ}$ of energy must be absorbed to break $1$ mol of $\text{H}-\text{Cl}$ bonds.",
            r"The $\text{H}-\text{Cl}$ bond length is $127\text{ pm}$, and $431\text{ kJ}$ of energy is released when $1$ mol of $\text{H}-\text{Cl}$ bonds is broken.",
            r"The $\text{H}-\text{Cl}$ bond length is $90\text{ pm}$, and $431\text{ kJ}$ of energy must be absorbed to break $1$ mol of $\text{H}-\text{Cl}$ bonds.",
            r"The $\text{H}-\text{Cl}$ bond length is $90\text{ pm}$, and $431\text{ kJ}$ of energy is released when $1$ mol of $\text{H}-\text{Cl}$ bonds is broken.",
        ],
        "correct_index": 0,
        "explanation": (
            r"The equilibrium bond length is the internuclear distance at which the potential energy is lowest, $127\text{ pm}$. Near $90\text{ pm}$ the curve only crosses zero on its steep repulsive side, where repulsion between the nuclei dominates; that distance is not the bond length. Separated atoms (large distance) have a potential energy of $0$, and the bonded atoms lie $431\text{ kJ/mol}$ lower at the minimum, so separating the atoms requires an input of $431\text{ kJ}$ per mole of bonds. Breaking a bond always absorbs energy; energy is released when bonds form, not when they break."
        ),
    },
    {
        "unit_q_num": 54,
        "topic_code": "2.2",
        "topic_title": "Intramolecular Force and Potential Energy",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<figure class="quiz-figure-wrap">'
            r'<svg xmlns="http://www.w3.org/2000/svg" class="quiz-figure" viewBox="0 0 520 320" role="img" aria-label="Graph of potential energy in kJ per mol versus internuclear distance in pm. Curve 1, for two H atoms, has a minimum of minus 436 kJ per mol at 74 pm. Curve 2, for two He atoms, is positive at all distances: it rises steeply below about 100 pm and approaches zero at large distances without a minimum.">'
            r'<line x1="70" y1="120" x2="490" y2="120" stroke="#9ca3af" stroke-width="1" stroke-dasharray="4 4"/>'
            r'<line x1="70" y1="30" x2="70" y2="270" stroke="#374151" stroke-width="1.5"/>'
            r'<line x1="70" y1="270" x2="490" y2="270" stroke="#374151" stroke-width="1.5"/>'
            r'<line x1="70" y1="270" x2="70" y2="275" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="70" y="288" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="middle">0</text>'
            r'<line x1="140" y1="270" x2="140" y2="275" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="140" y="288" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="middle">50</text>'
            r'<line x1="210" y1="270" x2="210" y2="275" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="210" y="288" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="middle">100</text>'
            r'<line x1="280" y1="270" x2="280" y2="275" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="280" y="288" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="middle">150</text>'
            r'<line x1="350" y1="270" x2="350" y2="275" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="350" y="288" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="middle">200</text>'
            r'<line x1="420" y1="270" x2="420" y2="275" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="420" y="288" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="middle">250</text>'
            r'<line x1="490" y1="270" x2="490" y2="275" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="490" y="288" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="middle">300</text>'
            r'<line x1="65" y1="270" x2="70" y2="270" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="62" y="274" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="end">−500</text>'
            r'<line x1="65" y1="240" x2="70" y2="240" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="62" y="244" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="end">−400</text>'
            r'<line x1="65" y1="210" x2="70" y2="210" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="62" y="214" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="end">−300</text>'
            r'<line x1="65" y1="180" x2="70" y2="180" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="62" y="184" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="end">−200</text>'
            r'<line x1="65" y1="150" x2="70" y2="150" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="62" y="154" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="end">−100</text>'
            r'<line x1="65" y1="120" x2="70" y2="120" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="62" y="124" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="end">0</text>'
            r'<line x1="65" y1="90" x2="70" y2="90" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="62" y="94" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="end">100</text>'
            r'<line x1="65" y1="60" x2="70" y2="60" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="62" y="64" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="end">200</text>'
            r'<line x1="65" y1="30" x2="70" y2="30" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="62" y="34" font-family="sans-serif" font-size="12" fill="#374151" text-anchor="end">300</text>'
            r'<text x="280" y="308" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Internuclear distance (pm)</text>'
            r'<text x="20" y="150" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle" transform="rotate(-90 20 150)">Potential energy (kJ/mol)</text>'
            r'<polyline points="113.5,30 114.2,37.5 114.9,44.8 115.6,51.8 116.3,58.7 117,65.4 117.7,72 118.4,78.3 119.1,84.5 119.8,90.5 120.5,96.3 121.2,102 121.9,107.5 122.6,112.9 123.3,118.1 124,123.1 124.7,128.1 125.4,132.8 126.1,137.5 126.8,141.9 127.5,146.3 128.2,150.5 128.9,154.6 129.6,158.6 130.3,162.5 131,166.2 131.7,169.8 132.4,173.4 133.1,176.8 133.8,180 134.5,183.2 135.2,186.3 135.9,189.3 136.6,192.2 137.3,195 138,197.7 138.7,200.3 139.4,202.8 140.1,205.2 140.8,207.5 141.5,209.8 142.2,212 142.9,214.1 143.6,216.1 144.3,218 145,219.9 145.7,221.7 146.4,223.4 147.1,225.1 147.8,226.7 148.5,228.2 149.2,229.7 149.9,231.1 150.6,232.4 151.3,233.7 152,234.9 152.7,236.1 153.4,237.2 154.1,238.2 154.8,239.2 155.5,240.2 156.2,241.1 156.9,242 157.6,242.8 158.3,243.5 159,244.2 159.7,244.9 160.4,245.5 161.1,246.1 161.8,246.7 162.5,247.2 163.2,247.7 163.9,248.1 164.6,248.5 165.3,248.9 166,249.2 166.7,249.5 167.4,249.8 168.1,250 168.8,250.2 169.5,250.4 170.2,250.5 170.9,250.6 171.6,250.7 172.3,250.8 173,250.8 173.7,250.8 174.4,250.8 175.1,250.7 175.8,250.7 176.5,250.6 177.2,250.5 177.9,250.4 178.6,250.2 179.3,250 180,249.9 180.7,249.6 181.4,249.4 182.1,249.2 182.8,248.9 183.5,248.6 184.2,248.4 184.9,248 185.6,247.7 186.3,247.4 187,247 187.7,246.7 188.4,246.3 189.1,245.9 189.8,245.5 190.5,245.1 191.2,244.7 191.9,244.2 192.6,243.8 193.3,243.3 194,242.9 194.7,242.4 195.4,241.9 196.1,241.4 196.8,240.9 197.5,240.4 198.2,239.9 198.9,239.3 199.6,238.8 200.3,238.3 201,237.7 201.7,237.2 202.4,236.6 203.1,236.1 203.8,235.5 204.5,234.9 205.2,234.3 205.9,233.8 206.6,233.2 207.3,232.6 208,232 208.7,231.4 209.4,230.8 210.1,230.2 210.8,229.6 211.5,229 212.2,228.3 212.9,227.7 213.6,227.1 214.3,226.5 215,225.9 215.7,225.2 216.4,224.6 217.1,224 217.8,223.3 218.5,222.7 219.2,222.1 219.9,221.5 220.6,220.8 221.3,220.2 222,219.6 222.7,218.9 223.4,218.3 224.1,217.7 224.8,217 225.5,216.4 226.2,215.7 226.9,215.1 227.6,214.5 228.3,213.9 229,213.2 229.7,212.6 230.4,212 231.1,211.3 231.8,210.7 232.5,210.1 233.2,209.5 233.9,208.8 234.6,208.2 235.3,207.6 236,207 236.7,206.3 237.4,205.7 238.1,205.1 238.8,204.5 239.5,203.9 240.2,203.3 240.9,202.7 241.6,202.1 242.3,201.5 243,200.9 243.7,200.3 244.4,199.7 245.1,199.1 245.8,198.5 246.5,197.9 247.2,197.3 247.9,196.7 248.6,196.2 249.3,195.6 250,195 250.7,194.4 251.4,193.9 252.1,193.3 256.3,189.9 260.5,186.7 264.7,183.5 268.9,180.5 273.1,177.6 277.3,174.8 281.5,172.1 285.7,169.5 289.9,167 294.1,164.6 298.3,162.3 302.5,160.2 306.7,158.1 310.9,156.1 315.1,154.2 319.3,152.4 323.5,150.7 327.7,149.1 331.9,147.5 336.1,146.1 340.3,144.7 344.5,143.3 348.7,142.1 352.9,140.9 357.1,139.8 361.3,138.7 365.5,137.7 369.7,136.7 373.9,135.8 378.1,134.9 382.3,134.1 386.5,133.3 390.7,132.6 394.9,131.9 399.1,131.2 403.3,130.6 407.5,130 411.7,129.5 415.9,128.9 420.1,128.5 424.3,128 428.5,127.5 432.7,127.1 436.9,126.7 441.1,126.3 445.3,126 449.5,125.7 453.7,125.3 457.9,125 462.1,124.8 466.3,124.5 470.5,124.2 474.7,124 478.9,123.8 483.1,123.6 487.3,123.4 490,123.2" fill="none" stroke="#111827" stroke-width="2.2" stroke-linejoin="round"/>'
            r'<polyline points="167.4,30 168.1,32.2 168.8,34.3 169.5,36.4 170.2,38.5 170.9,40.4 171.6,42.4 172.3,44.3 173,46.1 173.7,47.9 174.4,49.7 175.1,51.4 175.8,53 176.5,54.7 177.2,56.3 177.9,57.8 178.6,59.3 179.3,60.8 180,62.3 180.7,63.7 181.4,65 182.1,66.4 182.8,67.7 183.5,68.9 184.2,70.2 184.9,71.4 185.6,72.6 186.3,73.7 187,74.9 187.7,76 188.4,77 189.1,78.1 189.8,79.1 190.5,80.1 191.2,81.1 191.9,82 192.6,82.9 193.3,83.8 194,84.7 194.7,85.6 195.4,86.4 196.1,87.2 196.8,88 197.5,88.8 198.2,89.6 198.9,90.3 199.6,91 200.3,91.7 201,92.4 201.7,93.1 202.4,93.8 203.1,94.4 203.8,95 204.5,95.6 205.2,96.2 205.9,96.8 206.6,97.4 207.3,97.9 208,98.5 208.7,99 209.4,99.5 210.1,100 210.8,100.5 211.5,101 212.2,101.4 212.9,101.9 213.6,102.3 214.3,102.7 215,103.2 215.7,103.6 216.4,104 217.1,104.4 217.8,104.7 218.5,105.1 219.2,105.5 219.9,105.8 220.6,106.2 221.3,106.5 222,106.8 222.7,107.2 223.4,107.5 224.1,107.8 224.8,108.1 225.5,108.4 226.2,108.7 226.9,108.9 227.6,109.2 228.3,109.5 229,109.7 229.7,110 230.4,110.2 231.1,110.4 231.8,110.7 232.5,110.9 233.2,111.1 233.9,111.3 234.6,111.6 235.3,111.8 236,112 236.7,112.2 237.4,112.3 238.1,112.5 238.8,112.7 239.5,112.9 240.2,113.1 240.9,113.2 241.6,113.4 242.3,113.6 243,113.7 243.7,113.9 244.4,114 245.1,114.2 245.8,114.3 246.5,114.4 247.2,114.6 247.9,114.7 248.6,114.8 249.3,115 250,115.1 250.7,115.2 251.4,115.3 252.1,115.4 252.8,115.6 253.5,115.7 254.2,115.8 254.9,115.9 255.6,116 256.3,116.1 257,116.2 257.7,116.3 258.4,116.3 259.1,116.4 259.8,116.5 260.5,116.6 261.2,116.7 261.9,116.8 262.6,116.8 263.3,116.9 264,117 264.7,117.1 265.4,117.1 266.1,117.2 266.8,117.3 267.5,117.3 268.2,117.4 268.9,117.5 269.6,117.5 270.3,117.6 271,117.7 271.7,117.7 272.4,117.8 273.1,117.8 273.8,117.9 274.5,117.9 275.2,118 275.9,118 276.6,118.1 277.3,118.1 278,118.2 278.7,118.2 279.4,118.3 280.1,118.3 280.8,118.3 281.5,118.4 282.2,118.4 282.9,118.5 283.6,118.5 284.3,118.5 285,118.6 285.7,118.6 286.4,118.6 287.1,118.7 287.8,118.7 288.5,118.7 289.2,118.8 289.9,118.8 290.6,118.8 291.3,118.9 292,118.9 292.7,118.9 293.4,118.9 294.1,119 299.7,119.1 305.3,119.3 310.9,119.4 316.5,119.5 322.1,119.6 327.7,119.7 333.3,119.7 338.9,119.8 344.5,119.8 350.1,119.9 355.7,119.9 361.3,119.9 366.9,119.9 372.5,119.9 378.1,119.9 383.7,120 389.3,120 394.9,120 400.5,120 406.1,120 411.7,120 417.3,120 422.9,120 428.5,120 434.1,120 439.7,120 445.3,120 450.9,120 456.5,120 462.1,120 467.7,120 473.3,120 478.9,120 484.5,120 490,120" fill="none" stroke="#2563eb" stroke-width="2.4" stroke-dasharray="8 5" stroke-linejoin="round"/>'
            r'<text x="187.6" y="261" font-family="sans-serif" font-size="13" fill="#111827">Curve 1 (H + H)</text>'
            r'<text x="210" y="55.5" font-family="sans-serif" font-size="13" fill="#2563eb">Curve 2 (He + He)</text>'
            r'</svg>'
            r'<figcaption>Figure: Potential energy versus internuclear distance for two H atoms and for two He atoms</figcaption>'
            '</figure>'
        ),
        "question": (
            r"The graph above shows the potential energy of a pair of hydrogen atoms (curve 1) and of a pair of helium atoms (curve 2) as a function of the distance between their nuclei. Which of the following best explains the difference between the two curves?"
        ),
        "options": [
            r"The $\text{He}-\text{He}$ bond is stronger than the $\text{H}-\text{H}$ bond, because each $\text{He}$ atom has two valence electrons available for bonding rather than one.",
            r"Each $\text{H}$ atom has one unpaired $1s$ electron that the two atoms can share in a covalent bond, lowering the potential energy below that of the separated atoms; each $\text{He}$ atom has a filled $1s$ shell, so repulsions dominate at every distance and no stable bond forms.",
            r"Two $\text{He}$ atoms release energy as they are pushed closer together, so two bonded $\text{He}$ atoms are more stable than two separated $\text{He}$ atoms.",
            r"Two $\text{H}$ atoms transfer an electron to form an ionic bond, whereas two $\text{He}$ atoms cannot, because $\text{He}$ has a much higher first ionization energy than $\text{H}$.",
        ],
        "correct_index": 1,
        "explanation": (
            r"A stable bond exists only if the potential energy curve has a minimum below the energy of the separated atoms ($0$). Curve 1 has a minimum of $-436\text{ kJ/mol}$ at $74\text{ pm}$, the bond energy and bond length of $\text{H}_2$: sharing the two unpaired $1s$ electrons lowers the energy. Curve 2 stays above $0$ at every distance and rises steeply as the atoms approach, so two $\text{He}$ atoms are always less stable together than apart; with filled $1s$ shells there are no unpaired electrons to share, and repulsions dominate. A higher curve means a less stable arrangement, not a stronger bond, and pushing $\text{He}$ atoms together requires energy rather than releasing it. Identical atoms have no electronegativity difference, so $\text{H}_2$ is held together by a shared (covalent) electron pair, not by electron transfer."
        ),
    },
    {
        "unit_q_num": 55,
        "topic_code": "2.2",
        "topic_title": "Intramolecular Force and Potential Energy",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": (
            r"Based on Coulomb's law, the strength of the attraction between a cation and an adjacent anion is proportional to $\frac{|q_1 q_2|}{r}$, where $q_1$ and $q_2$ are the charges of the ions and $r$ is the distance between the centers of the ions (the sum of their radii). The radii of $\text{K}^+$, $\text{Ca}^{2+}$, $\text{Cl}^-$, and $\text{O}^{2-}$ are $138$, $100$, $181$, and $140\text{ pm}$, respectively. The attraction between a $\text{Ca}^{2+}$ ion and an adjacent $\text{O}^{2-}$ ion is approximately how many times as strong as the attraction between a $\text{K}^+$ ion and an adjacent $\text{Cl}^-$ ion?"
        ),
        "options": [
            r"$3.0$",
            r"$4.0$",
            r"$5.3$",
            r"$7.1$",
        ],
        "correct_index": 2,
        "explanation": (
            r"Add the radii to find each distance: $r = 100 + 140 = 240\text{ pm}$ for $\text{Ca}^{2+}$ and $\text{O}^{2-}$, and $r = 138 + 181 = 319\text{ pm}$ for $\text{K}^+$ and $\text{Cl}^-$. The ratio is $\frac{(2)(2)/240}{(1)(1)/319} = 4 \times \frac{319}{240} \approx 5.3$. The fourfold larger charge product is reinforced by the shorter distance between the smaller ions, so the ratio exceeds $4.0$, the value obtained by ignoring distance. A ratio of $3.0$ comes from inverting the distance ratio ($4 \times \frac{240}{319}$), as if larger ions attracted more strongly, and $7.1$ comes from squaring the distance ratio, which the given proportionality does not include."
        ),
    },
    {
        "unit_q_num": 56,
        "topic_code": "2.3",
        "topic_title": "Structure of Ionic Solids",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            r"<thead><tr><th>Compound</th><th>Charges of Ions</th><th>Distance Between Ion Centers ($\text{pm}$)</th></tr></thead><tbody>"
            r"<tr><td>$\text{NaF}$</td><td>$+1,\ -1$</td><td>$235$</td></tr>"
            r"<tr><td>$\text{NaCl}$</td><td>$+1,\ -1$</td><td>$283$</td></tr>"
            r"<tr><td>$\text{MgO}$</td><td>$+2,\ -2$</td><td>$212$</td></tr>"
            r"<tr><td>$\text{CaO}$</td><td>$+2,\ -2$</td><td>$240$</td></tr>"
            r"</tbody></table>"
        ),
        "question": (
            r"A student hypothesizes that the magnitude of the charges on the ions affects the melting point of an ionic solid, independent of the sizes of the ions. The student will measure the melting points of two of the compounds listed in the table above. Which pair of compounds provides the best test of this hypothesis?"
        ),
        "options": [
            r"$\text{NaF}$ and $\text{NaCl}$",
            r"$\text{NaCl}$ and $\text{MgO}$",
            r"$\text{NaF}$ and $\text{CaO}$",
            r"$\text{MgO}$ and $\text{CaO}$",
        ],
        "correct_index": 2,
        "explanation": (
            r"The Coulombic attraction between ions depends on both the ion charges and the distance between ion centers, so a fair test of the effect of charge must keep that distance nearly constant while the charges differ. $\text{NaF}$ ($+1/-1$, $235\text{ pm}$) and $\text{CaO}$ ($+2/-2$, $240\text{ pm}$) differ in charge but have almost the same interionic distance, so a difference in their melting points can be attributed to charge. $\text{NaF}$ and $\text{NaCl}$, like $\text{MgO}$ and $\text{CaO}$, have identical charges and differ only in distance, so they test the effect of ion size instead. $\text{NaCl}$ and $\text{MgO}$ differ in both charge and distance ($283$ vs. $212\text{ pm}$), so the two effects cannot be separated."
        ),
    },
    {
        "unit_q_num": 57,
        "topic_code": "2.3",
        "topic_title": "Structure of Ionic Solids",
        "difficulty": "Challenging",
        "stimulus": (
            '<figure class="quiz-figure-wrap">'
            r'<svg xmlns="http://www.w3.org/2000/svg" class="quiz-figure" viewBox="0 0 560 360" role="img" aria-label="Four particulate diagrams of a two-dimensional slice of an ionic solid. Diagram 1: alternating ions with small cations and large anions. Diagram 2: alternating ions with large cations and small anions. Diagram 3: large cations and small anions arranged in separate rows, so like-charged ions sit next to each other. Diagram 4: separate cation-anion pairs with gaps between them.">'
            r'<rect x="10" y="10" width="265" height="165" rx="6" fill="#ffffff" stroke="#9ca3af" stroke-width="1.5"/>'
            r'<text x="20" y="29" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">Diagram 1</text>'
            r'<rect x="285" y="10" width="265" height="165" rx="6" fill="#ffffff" stroke="#9ca3af" stroke-width="1.5"/>'
            r'<text x="295" y="29" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">Diagram 2</text>'
            r'<rect x="10" y="185" width="265" height="165" rx="6" fill="#ffffff" stroke="#9ca3af" stroke-width="1.5"/>'
            r'<text x="20" y="204" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">Diagram 3</text>'
            r'<rect x="285" y="185" width="265" height="165" rx="6" fill="#ffffff" stroke="#9ca3af" stroke-width="1.5"/>'
            r'<text x="295" y="204" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">Diagram 4</text>'
            r'<circle cx="81.5" cy="59" r="13.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="81.5" y="64" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="112" cy="59" r="17" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="112" y="64" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="142.5" cy="59" r="13.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="142.5" y="64" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="173" cy="59" r="17" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="173" y="64" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="203.5" cy="59" r="13.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="203.5" y="64" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="81.5" cy="89.5" r="17" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="81.5" y="94.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="112" cy="89.5" r="13.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="112" y="94.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="142.5" cy="89.5" r="17" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="142.5" y="94.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="173" cy="89.5" r="13.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="173" y="94.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="203.5" cy="89.5" r="17" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="203.5" y="94.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="81.5" cy="120" r="13.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="81.5" y="125" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="112" cy="120" r="17" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="112" y="125" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="142.5" cy="120" r="13.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="142.5" y="125" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="173" cy="120" r="17" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="173" y="125" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="203.5" cy="120" r="13.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="203.5" y="125" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="81.5" cy="150.5" r="17" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="81.5" y="155.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="112" cy="150.5" r="13.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="112" y="155.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="142.5" cy="150.5" r="17" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="142.5" y="155.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="173" cy="150.5" r="13.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="173" y="155.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="203.5" cy="150.5" r="17" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="203.5" y="155.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="356.5" cy="59" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="356.5" y="64" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="387" cy="59" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="387" y="64" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="417.5" cy="59" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="417.5" y="64" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="448" cy="59" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="448" y="64" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="478.5" cy="59" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="478.5" y="64" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="356.5" cy="89.5" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="356.5" y="94.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="387" cy="89.5" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="387" y="94.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="417.5" cy="89.5" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="417.5" y="94.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="448" cy="89.5" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="448" y="94.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="478.5" cy="89.5" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="478.5" y="94.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="356.5" cy="120" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="356.5" y="125" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="387" cy="120" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="387" y="125" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="417.5" cy="120" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="417.5" y="125" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="448" cy="120" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="448" y="125" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="478.5" cy="120" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="478.5" y="125" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="356.5" cy="150.5" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="356.5" y="155.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="387" cy="150.5" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="387" y="155.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="417.5" cy="150.5" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="417.5" y="155.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="448" cy="150.5" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="448" y="155.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="478.5" cy="150.5" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="478.5" y="155.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="74.5" cy="234" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="74.5" y="239" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="108.5" cy="234" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="108.5" y="239" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="142.5" cy="234" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="142.5" y="239" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="176.5" cy="234" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="176.5" y="239" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="210.5" cy="234" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="210.5" y="239" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="74.5" cy="264.5" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="74.5" y="269.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="108.5" cy="264.5" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="108.5" y="269.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="142.5" cy="264.5" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="142.5" y="269.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="176.5" cy="264.5" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="176.5" y="269.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="210.5" cy="264.5" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="210.5" y="269.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="74.5" cy="295" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="74.5" y="300" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="108.5" cy="295" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="108.5" y="300" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="142.5" cy="295" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="142.5" y="300" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="176.5" cy="295" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="176.5" y="300" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="210.5" cy="295" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="210.5" y="300" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="74.5" cy="325.5" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="74.5" y="330.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="108.5" cy="325.5" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="108.5" y="330.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="142.5" cy="325.5" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="142.5" y="330.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="176.5" cy="325.5" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="176.5" y="330.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="210.5" cy="325.5" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="210.5" y="330.5" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="326.2" cy="236" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="326.2" y="241" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="356.8" cy="236" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="356.8" y="241" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="402.2" cy="236" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="402.2" y="241" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="432.8" cy="236" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="432.8" y="241" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="478.2" cy="236" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="478.2" y="241" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="508.8" cy="236" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="508.8" y="241" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="326.2" cy="278" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="326.2" y="283" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="356.8" cy="278" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="356.8" y="283" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="402.2" cy="278" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="402.2" y="283" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="432.8" cy="278" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="432.8" y="283" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="478.2" cy="278" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="478.2" y="283" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="508.8" cy="278" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="508.8" y="283" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="326.2" cy="320" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="326.2" y="325" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="356.8" cy="320" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="356.8" y="325" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="402.2" cy="320" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="402.2" y="325" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="432.8" cy="320" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="432.8" y="325" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'<circle cx="478.2" cy="320" r="17" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="478.2" y="325" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">+</text>'
            r'<circle cx="508.8" cy="320" r="13.5" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="508.8" y="325" font-family="sans-serif" font-size="15" font-weight="bold" fill="#111827" text-anchor="middle">−</text>'
            r'</svg>'
            r'<figcaption>Figure: Four possible particulate diagrams (two-dimensional slices) of an ionic solid</figcaption>'
            '</figure>'
        ),
        "question": (
            r"Each diagram above represents a two-dimensional slice of an ionic solid, in which gray circles labeled $+$ represent cations and white circles labeled $-$ represent anions. Which diagram best represents solid cesium fluoride, $\text{CsF}$?"
        ),
        "options": [
            r"Diagram 1",
            r"Diagram 2",
            r"Diagram 3",
            r"Diagram 4",
        ],
        "correct_index": 1,
        "explanation": (
            r"A $\text{Cs}^+$ ion has the electron configuration of xenon, with its outermost electrons in the $n = 5$ shell, whereas $\text{F}^-$ has the configuration of neon, with its outermost electrons in the $n = 2$ shell. The cation is therefore larger than the anion in this compound (about $167$ vs. $133\text{ pm}$), even though every cation is smaller than its parent atom. In an ionic solid, cations and anions alternate in a three-dimensional array that maximizes attractions between oppositely charged ions and minimizes repulsions between like-charged ions. Diagram 2 shows alternating ions with the larger circles as the cations. Diagram 1 alternates correctly but makes the cation smaller than the anion, Diagram 3 places like-charged ions next to each other in rows, and Diagram 4 shows discrete $\text{CsF}$ pairs (molecules) instead of a continuous lattice."
        ),
    },
    {
        "unit_q_num": 58,
        "topic_code": "2.4",
        "topic_title": "Structure of Metals and Alloys",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<figure class="quiz-figure-wrap">'
            r'<svg xmlns="http://www.w3.org/2000/svg" class="quiz-figure" viewBox="0 0 560 360" role="img" aria-label="Four particulate diagrams, each with six metal particles in two rows of three. Diagram 1: six Mg 2+ ions with six electrons scattered between them. Diagram 2: six neutral Mg atoms joined by six lines around the outside of the group. Diagram 3: six Mg 1+ ions with six electrons scattered between them. Diagram 4: six Mg 2+ ions with twelve electrons scattered between them.">'
            r'<rect x="10" y="10" width="265" height="165" rx="6" fill="#ffffff" stroke="#9ca3af" stroke-width="1.5"/>'
            r'<text x="20" y="29" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">Diagram 1</text>'
            r'<rect x="285" y="10" width="265" height="165" rx="6" fill="#ffffff" stroke="#9ca3af" stroke-width="1.5"/>'
            r'<text x="295" y="29" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">Diagram 2</text>'
            r'<rect x="10" y="185" width="265" height="165" rx="6" fill="#ffffff" stroke="#9ca3af" stroke-width="1.5"/>'
            r'<text x="20" y="204" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">Diagram 3</text>'
            r'<rect x="285" y="185" width="265" height="165" rx="6" fill="#ffffff" stroke="#9ca3af" stroke-width="1.5"/>'
            r'<text x="295" y="204" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">Diagram 4</text>'
            r'<circle cx="78.5" cy="72" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="78.5" y="76.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg²⁺</text>'
            r'<circle cx="142.5" cy="72" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="142.5" y="76.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg²⁺</text>'
            r'<circle cx="206.5" cy="72" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="206.5" y="76.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg²⁺</text>'
            r'<circle cx="78.5" cy="132" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="78.5" y="136.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg²⁺</text>'
            r'<circle cx="142.5" cy="132" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="142.5" y="136.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg²⁺</text>'
            r'<circle cx="206.5" cy="132" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="206.5" y="136.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg²⁺</text>'
            r'<circle cx="44.5" cy="102" r="3.4" fill="#111827"/>'
            r'<circle cx="110.5" cy="72" r="3.4" fill="#111827"/>'
            r'<circle cx="142.5" cy="102" r="3.4" fill="#111827"/>'
            r'<circle cx="174.5" cy="132" r="3.4" fill="#111827"/>'
            r'<circle cx="240.5" cy="102" r="3.4" fill="#111827"/>'
            r'<circle cx="142.5" cy="42" r="3.4" fill="#111827"/>'
            r'<line x1="374.5" y1="72" x2="396.5" y2="72" stroke="#111827" stroke-width="2.2"/>'
            r'<line x1="438.5" y1="72" x2="460.5" y2="72" stroke="#111827" stroke-width="2.2"/>'
            r'<line x1="374.5" y1="132" x2="396.5" y2="132" stroke="#111827" stroke-width="2.2"/>'
            r'<line x1="438.5" y1="132" x2="460.5" y2="132" stroke="#111827" stroke-width="2.2"/>'
            r'<line x1="353.5" y1="93" x2="353.5" y2="111" stroke="#111827" stroke-width="2.2"/>'
            r'<line x1="481.5" y1="93" x2="481.5" y2="111" stroke="#111827" stroke-width="2.2"/>'
            r'<circle cx="353.5" cy="72" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="353.5" y="76.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg</text>'
            r'<circle cx="417.5" cy="72" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="417.5" y="76.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg</text>'
            r'<circle cx="481.5" cy="72" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="481.5" y="76.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg</text>'
            r'<circle cx="353.5" cy="132" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="353.5" y="136.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg</text>'
            r'<circle cx="417.5" cy="132" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="417.5" y="136.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg</text>'
            r'<circle cx="481.5" cy="132" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="481.5" y="136.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg</text>'
            r'<circle cx="78.5" cy="247" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="78.5" y="251.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg⁺</text>'
            r'<circle cx="142.5" cy="247" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="142.5" y="251.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg⁺</text>'
            r'<circle cx="206.5" cy="247" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="206.5" y="251.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg⁺</text>'
            r'<circle cx="78.5" cy="307" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="78.5" y="311.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg⁺</text>'
            r'<circle cx="142.5" cy="307" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="142.5" y="311.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg⁺</text>'
            r'<circle cx="206.5" cy="307" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="206.5" y="311.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg⁺</text>'
            r'<circle cx="44.5" cy="277" r="3.4" fill="#111827"/>'
            r'<circle cx="110.5" cy="247" r="3.4" fill="#111827"/>'
            r'<circle cx="142.5" cy="277" r="3.4" fill="#111827"/>'
            r'<circle cx="174.5" cy="307" r="3.4" fill="#111827"/>'
            r'<circle cx="240.5" cy="277" r="3.4" fill="#111827"/>'
            r'<circle cx="142.5" cy="217" r="3.4" fill="#111827"/>'
            r'<circle cx="353.5" cy="247" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="353.5" y="251.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg²⁺</text>'
            r'<circle cx="417.5" cy="247" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="417.5" y="251.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg²⁺</text>'
            r'<circle cx="481.5" cy="247" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="481.5" y="251.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg²⁺</text>'
            r'<circle cx="353.5" cy="307" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="353.5" y="311.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg²⁺</text>'
            r'<circle cx="417.5" cy="307" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="417.5" y="311.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg²⁺</text>'
            r'<circle cx="481.5" cy="307" r="21.0" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="481.5" y="311.5" font-family="sans-serif" font-size="13" fill="#111827" text-anchor="middle">Mg²⁺</text>'
            r'<circle cx="319.5" cy="277" r="3.4" fill="#111827"/>'
            r'<circle cx="353.5" cy="277" r="3.4" fill="#111827"/>'
            r'<circle cx="385.5" cy="277" r="3.4" fill="#111827"/>'
            r'<circle cx="417.5" cy="277" r="3.4" fill="#111827"/>'
            r'<circle cx="449.5" cy="277" r="3.4" fill="#111827"/>'
            r'<circle cx="481.5" cy="277" r="3.4" fill="#111827"/>'
            r'<circle cx="515.5" cy="277" r="3.4" fill="#111827"/>'
            r'<circle cx="385.5" cy="247" r="3.4" fill="#111827"/>'
            r'<circle cx="449.5" cy="247" r="3.4" fill="#111827"/>'
            r'<circle cx="385.5" cy="307" r="3.4" fill="#111827"/>'
            r'<circle cx="449.5" cy="307" r="3.4" fill="#111827"/>'
            r'<circle cx="417.5" cy="217" r="3.4" fill="#111827"/>'
            r'</svg>'
            r'<figcaption>Figure: Four possible models of solid magnesium. Each small black dot represents one electron; in Diagram 2, each line represents a pair of electrons shared between two atoms.</figcaption>'
            '</figure>'
        ),
        "question": (
            r"Which of the diagrams above best represents the bonding in a sample of solid magnesium?"
        ),
        "options": [
            r"Diagram 1",
            r"Diagram 2",
            r"Diagram 3",
            r"Diagram 4",
        ],
        "correct_index": 3,
        "explanation": (
            r"In the electron-sea model of metallic bonding, every metal atom contributes all of its valence electrons to a sea of electrons delocalized over the whole sample, leaving an array of positive metal ions. A $\text{Mg}$ atom has two valence electrons ($3s^2$), so the model should show $\text{Mg}^{2+}$ ions with two delocalized electrons per ion: $6$ ions and $12$ electrons, an electrically neutral sample, as in Diagram 4. Diagram 1 has only $6$ electrons for $6$ $\text{Mg}^{2+}$ ions, a net charge of $+6$. Diagram 3 is neutral, but it shows each atom contributing only one of its two valence electrons. Diagram 2 shows electrons localized in shared pairs between specific atoms (covalent bonds), which cannot account for the electrical conductivity and malleability of magnesium."
        ),
    },
    {
        "unit_q_num": 59,
        "topic_code": "2.6",
        "topic_title": "Resonance and Formal Charge",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": (
            r"Nitrogen monoxide, $\text{NO}$, has $11$ valence electrons. Which of the following statements about Lewis diagrams for $\text{NO}$ is correct?"
        ),
        "options": [
            r"The best Lewis diagram has an $\text{N}=\text{O}$ double bond and places the unpaired electron on $\text{N}$, giving both atoms a formal charge of $0$; in this diagram $\text{N}$ has only $7$ valence electrons, a limitation of the octet rule for species with an odd number of electrons.",
            r"The best Lewis diagram has an $\text{N}=\text{O}$ double bond and places the unpaired electron on $\text{O}$, because the more electronegative atom should hold more electrons; this gives both atoms a formal charge of $0$.",
            r"A Lewis diagram with an $\text{N}\equiv\text{O}$ triple bond allows both atoms to have complete octets, so the octet rule can be satisfied for $\text{NO}$.",
            r"No Lewis diagram can be drawn for a species with an odd number of electrons, so $\text{NO}$ must be an ionic compound made of $\text{N}^+$ and $\text{O}^-$ ions.",
        ],
        "correct_index": 0,
        "explanation": (
            r"With an odd number of valence electrons ($11$), at least one atom must have an odd electron count, so the octet rule cannot be satisfied for both atoms. After an $\text{N}=\text{O}$ double bond ($4$ electrons), $7$ electrons remain. Placing $3$ nonbonding electrons on $\text{N}$ and $4$ on $\text{O}$ gives $\text{FC}(\text{N}) = 5 - 3 - 2 = 0$ and $\text{FC}(\text{O}) = 6 - 4 - 2 = 0$. Placing the unpaired electron on $\text{O}$ instead leaves $4$ nonbonding electrons on $\text{N}$ and $3$ on $\text{O}$, so $\text{FC}(\text{N}) = -1$ and $\text{FC}(\text{O}) = +1$, which is worse because the positive formal charge sits on the more electronegative atom. A triple bond plus $5$ nonbonding electrons would give one atom at least $9$ electrons, which is impossible for a Period 2 atom. Lewis diagrams can still be drawn for odd-electron species such as the molecular gas $\text{NO}$; they simply reveal the limits of the octet-based model."
        ),
    },
    {
        "unit_q_num": 60,
        "topic_code": "2.7",
        "topic_title": "VSEPR and Hybridization",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            r"<thead><tr><th>Bond</th><th>Average Bond Enthalpy ($\text{kJ/mol}$)</th></tr></thead><tbody>"
            r"<tr><td>$\text{C}-\text{C}$</td><td>$348$</td></tr>"
            r"<tr><td>$\text{C}=\text{C}$</td><td>$614$</td></tr>"
            r"<tr><td>$\text{C}\equiv\text{C}$</td><td>$839$</td></tr>"
            r"</tbody></table>"
        ),
        "question": (
            r"A student claims that a $\pi$ bond is stronger than a $\sigma$ bond because a carbon-carbon double bond is stronger than a carbon-carbon single bond. Which of the following best evaluates the student's claim using the data in the table above?"
        ),
        "options": [
            r"The claim is correct: the $\pi$ bond in $\text{C}=\text{C}$ contributes about $614\text{ kJ/mol}$, which is greater than the $348\text{ kJ/mol}$ of a $\text{C}-\text{C}$ $\sigma$ bond.",
            r"The claim is incorrect: the $\pi$ bond in $\text{C}=\text{C}$ contributes only about $614 - 348 = 266\text{ kJ/mol}$, less than the $348\text{ kJ/mol}$ of a $\sigma$ bond, because the side-by-side overlap of $p$ orbitals in a $\pi$ bond is weaker than the end-to-end overlap in a $\sigma$ bond.",
            r"The claim is correct: the $\pi$ bonding in $\text{C}\equiv\text{C}$ contributes about $839 - 348 = 491\text{ kJ/mol}$, which is greater than the $348\text{ kJ/mol}$ of a $\sigma$ bond.",
            r"The claim is incorrect: the two bonds in $\text{C}=\text{C}$ each contribute $614/2 = 307\text{ kJ/mol}$, so $\sigma$ and $\pi$ bonds are equally strong.",
        ],
        "correct_index": 1,
        "explanation": (
            r"Every multiple bond contains one $\sigma$ bond; the additional bonds are $\pi$ bonds. Subtracting the single-bond enthalpy estimates the first $\pi$ bond: $614 - 348 = 266\text{ kJ/mol}$, and the second $\pi$ bond of the triple bond adds $839 - 614 = 225\text{ kJ/mol}$. Both are smaller than the $348\text{ kJ/mol}$ of the $\sigma$ bond, so a double bond is stronger than a single bond only because it contains an additional bond, not because $\pi$ bonds are stronger. A $\sigma$ bond forms by direct (end-to-end) overlap along the internuclear axis, which is more effective than the side-by-side overlap of a $\pi$ bond. The value $614\text{ kJ/mol}$ is the entire double bond, $491\text{ kJ/mol}$ is the total for two $\pi$ bonds, and splitting $614$ equally assumes, rather than tests, that $\sigma$ and $\pi$ bonds are equal."
        ),
    },
]
