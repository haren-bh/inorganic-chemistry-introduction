UNIT_META = {
    "id": 3,
    "title": "Unit 3: Properties of Substances and Mixtures",
    "short_title": "Properties of Substances & Mixtures",
    "exam_weight": "18–22%",
    "color": "#7c3aed",
    "description": "London dispersion, dipole-dipole, hydrogen bonding, and ion-dipole forces; covalent network, ionic, metallic, and molecular solids; ideal gas law, Dalton's law of partial pressures, Kinetic Molecular Theory, real gas deviations, solutions, chromatography/distillation, spectroscopy (IR, UV-Vis, microwave), photon energy and wavelength calculations, and Beer-Lambert Law.",
    "topics": [
        {"code": "3.1", "title": "Intermolecular and Interparticle Forces"},
        {"code": "3.2", "title": "Properties of Solids"},
        {"code": "3.3", "title": "Solids, Liquids, and Gases"},
        {"code": "3.4", "title": "Ideal Gas Law"},
        {"code": "3.5", "title": "Kinetic Molecular Theory"},
        {"code": "3.6", "title": "Deviation from Ideal Gas Law"},
        {"code": "3.7", "title": "Solutions and Mixtures"},
        {"code": "3.8", "title": "Representations of Solutions"},
        {"code": "3.9", "title": "Separation of Solutions and Mixtures"},
        {"code": "3.10", "title": "Solubility"},
        {"code": "3.11", "title": "Spectroscopy and the Electromagnetic Spectrum"},
        {"code": "3.12", "title": "Properties of Photons"},
        {"code": "3.13", "title": "Beer-Lambert Law"},
    ],
}

QUESTIONS = [
    # -------------------------------------------------------------------------
    # Topic 3.1: Intermolecular and Interparticle Forces (Q1 - Q5)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 1,
        "topic_code": "3.1",
        "topic_title": "Intermolecular and Interparticle Forces",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            '<thead><tr><th>Substance</th><th>Formula</th><th>Molar Mass ($\\text{g/mol}$)</th><th>Normal Boiling Point ($^\\circ\\text{C}$)</th></tr></thead>'
            '<tbody>'
            '<tr><td><i>n</i>-Pentane</td><td>$\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}_2\\text{CH}_3$</td><td>$72.15$</td><td>$36.1$</td></tr>'
            '<tr><td>2,2-Dimethylpropane (Neopentane)</td><td>$\\text{C(CH}_3)_4$</td><td>$72.15$</td><td>$9.5$</td></tr>'
            '</tbody></table>'
        ),
        "question": "Both $n$-pentane and 2,2-dimethylpropane are nonpolar structural isomers with the molecular formula $\\text{C}_5\\text{H}_{12}$. Based on the data in the table, which of the following best accounts for the higher normal boiling point of $n$-pentane?",
        "options": [
            "$n$-Pentane has a larger number of valence electrons, resulting in stronger dipole-dipole attractions.",
            "The elongated, rod-like shape of $n$-pentane provides a greater surface area for contact between molecules, increasing the strength of London dispersion forces.",
            "$n$-Pentane contains terminal $\\text{C}-\\text{H}$ bonds capable of weak hydrogen bonding, whereas 2,2-dimethylpropane is sterically hindered.",
            "The $\\text{C}-\\text{C}$ covalent bonds in $n$-pentane are stronger and require more thermal energy to break during vaporization than those in 2,2-dimethylpropane."
        ],
        "correct_index": 1,
        "explanation": "Both isomers have the exact same formula ($\\text{C}_5\\text{H}_{12}$) and the same number of electrons, and both are nonpolar hydrocarbons experiencing only London dispersion forces (LDFs). However, $n$-pentane has an unbranched, elongated chain structure that allows adjacent molecules to make contact over a larger surface area, which strengthens LDFs compared to the compact, nearly spherical 2,2-dimethylpropane molecules, which can touch each other over only a small area. Note that covalent bonds are not broken during boiling, and neither molecule is polar or able to hydrogen-bond."
    },
    {
        "unit_q_num": 2,
        "topic_code": "3.1",
        "topic_title": "Intermolecular and Interparticle Forces",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            '<thead><tr><th>Halogen</th><th>Total Electrons</th><th>Normal Boiling Point ($\\text{K}$)</th><th>State at $298\\text{ K}, 1\\text{ atm}$</th></tr></thead>'
            '<tbody>'
            '<tr><td>$\\text{F}_2$</td><td>$18$</td><td>$85$</td><td>Gas</td></tr>'
            '<tr><td>$\\text{Cl}_2$</td><td>$34$</td><td>$239$</td><td>Gas</td></tr>'
            '<tr><td>$\\text{Br}_2$</td><td>$70$</td><td>$332$</td><td>Liquid</td></tr>'
            '<tr><td>$\\text{I}_2$</td><td>$106$</td><td>$457$</td><td>Solid</td></tr>'
            '</tbody></table>'
        ),
        "question": "Which of the following statements best explains why $\\text{I}_2$ is a solid at $298\\text{ K}$ and $1\\text{ atm}$, whereas $\\text{F}_2$ is a gas under the same conditions?",
        "options": [
            "$\\text{I}_2$ molecules have a much larger, more diffuse electron cloud that is more easily distorted to form temporary dipoles, resulting in significantly stronger London dispersion forces.",
            "The covalent bond in $\\text{I}_2$ is much longer and weaker than in $\\text{F}_2$, allowing $\\text{I}_2$ atoms to cross-link into a solid network at room temperature.",
            "$\\text{I}_2$ has a higher molecular mass, so gravitational attractions between $\\text{I}_2$ molecules prevent them from escaping into the gas phase at $298\\text{ K}$.",
            "$\\text{F}_2$ is highly electronegative and experiences strong intermolecular electron-electron repulsions that keep its molecules in the gas phase."
        ],
        "correct_index": 0,
        "explanation": "On the AP Chemistry exam, boiling point trends among nonpolar molecules must be explained in terms of electron cloud size and polarizability—never gravitational attraction (mass weight) or intramolecular bond strength. Because $\\text{I}_2$ has $106$ electrons in shells further from the nuclei compared to $18$ electrons in $\\text{F}_2$, the electron cloud of $\\text{I}_2$ is much more polarizable, leading to stronger London dispersion forces."
    },
    {
        "unit_q_num": 3,
        "topic_code": "3.1",
        "topic_title": "Intermolecular and Interparticle Forces",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            '<thead><tr><th>Compound</th><th>Lewis Structure / Formula</th><th>Molar Mass ($\\text{g/mol}$)</th><th>Dipole Moment ($\\text{D}$)</th><th>Vapor Pressure at $25^\\circ\\text{C}$ ($\\text{torr}$)</th></tr></thead>'
            '<tbody>'
            '<tr><td>Propane</td><td>$\\text{CH}_3\\text{CH}_2\\text{CH}_3$</td><td>$44.1$</td><td>$0.08$</td><td>$7150$</td></tr>'
            '<tr><td>Dimethyl ether</td><td>$\\text{CH}_3\\text{OCH}_3$</td><td>$46.1$</td><td>$1.30$</td><td>$4450$</td></tr>'
            '<tr><td>Acetaldehyde</td><td>$\\text{CH}_3\\text{CHO}$</td><td>$44.1$</td><td>$2.70$</td><td>$900$</td></tr>'
            '<tr><td>Ethanol</td><td>$\\text{CH}_3\\text{CH}_2\\text{OH}$</td><td>$46.1$</td><td>$1.69$</td><td>$59$</td></tr>'
            '</tbody></table>'
        ),
        "question": "Although acetaldehyde ($\\text{CH}_3\\text{CHO}$) has a larger permanent dipole moment than ethanol ($\\text{CH}_3\\text{CH}_2\\text{OH}$) and a nearly identical molar mass, ethanol has a much lower vapor pressure at $25^\\circ\\text{C}$. Which of the following best explains this observation?",
        "options": [
            "Acetaldehyde molecules only experience London dispersion forces in the liquid state.",
            "Ethanol has a higher molar mass than acetaldehyde, which decreases the average kinetic energy of ethanol molecules at $25^\\circ\\text{C}$.",
            "Dimethyl ether and ethanol both form hydrogen bonds in the pure liquid, but ethanol has a larger dipole moment.",
            "Ethanol molecules contain an $-\\text{OH}$ group that can both donate and accept intermolecular hydrogen bonds, which are stronger than the dipole-dipole forces between acetaldehyde molecules."
        ],
        "correct_index": 3,
        "explanation": "Vapor pressure at a given temperature is inversely related to the strength of intermolecular forces. While both acetaldehyde and ethanol experience comparable London dispersion forces (similar molar masses/electron counts) and dipole-dipole interactions, pure ethanol has an $\\text{O}-\\text{H}$ bond that allows strong intermolecular hydrogen bonding between the H atom of one molecule and the lone pair on the O atom of a neighboring molecule. Acetaldehyde lacks an $\\text{N}-\\text{H}$, $\\text{O}-\\text{H}$, or $\\text{F}-\\text{H}$ bond and cannot hydrogen-bond with itself."
    },
    {
        "unit_q_num": 4,
        "topic_code": "3.1",
        "topic_title": "Intermolecular and Interparticle Forces",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": "At their normal boiling points, the enthalpy of vaporization ($\\Delta H_{\\text{vap}}$) of $\\text{CS}_2(l)$ (normal boiling point $46^\\circ\\text{C}$) is $26.7\\text{ kJ/mol}$, whereas $\\Delta H_{\\text{vap}}$ of $\\text{COS}(l)$ (normal boiling point $-50^\\circ\\text{C}$) is $18.5\\text{ kJ/mol}$. Both molecules are linear. Why does nonpolar $\\text{CS}_2$ have a larger enthalpy of vaporization than polar $\\text{COS}$?",
        "options": [
            "$\\text{CS}_2$ forms a covalent network in the liquid phase, whereas $\\text{COS}$ consists of discrete molecules.",
            "The $\\text{C}=\\text{S}$ double bonds in $\\text{CS}_2$ have a higher bond enthalpy than the $\\text{C}=\\text{O}$ double bond in $\\text{COS}$.",
            "The greater polarizability of the two sulfur atoms in $\\text{CS}_2$ produces London dispersion forces that are stronger than the combined London dispersion and dipole-dipole forces in $\\text{COS}$.",
            "$\\text{COS}$ can participate in intermolecular hydrogen bonding, which lowers its enthalpy of vaporization."
        ],
        "correct_index": 2,
        "explanation": "Although $\\text{COS}$ is asymmetric and polar (experiencing dipole-dipole forces in addition to LDFs) while $\\text{CS}_2$ is symmetric and nonpolar (experiencing only LDFs), replacing an oxygen atom ($8\\text{ e}^-$) with a larger, more polarizable sulfur atom ($16\\text{ e}^-$) significantly increases the strength of London dispersion forces in $\\text{CS}_2$. In this case, the stronger LDFs in $\\text{CS}_2$ outweigh the weak dipole-dipole attractions in $\\text{COS}$."
    },
    {
        "unit_q_num": 5,
        "topic_code": "3.1",
        "topic_title": "Intermolecular and Interparticle Forces",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "Which of the following lists all of the types of intermolecular forces acting between molecules in a pure liquid sample of $\\text{CH}_2\\text{F}_2$?",
        "options": [
            "London dispersion forces only, because the tetrahedral molecule is symmetric.",
            "London dispersion forces and dipole-dipole forces only.",
            "London dispersion forces, dipole-dipole forces, and hydrogen bonding.",
            "Dipole-dipole forces and hydrogen bonding only."
        ],
        "correct_index": 1,
        "explanation": "$\\text{CH}_2\\text{F}_2$ has a tetrahedral geometry around carbon, but because the $\\text{C}-\\text{F}$ and $\\text{C}-\\text{H}$ bond dipoles do not cancel out, the molecule has a net permanent dipole moment. Therefore, pure $\\text{CH}_2\\text{F}_2(l)$ exhibits both London dispersion forces and dipole-dipole forces. Crucially, the hydrogen atoms are bonded to carbon ($\\text{C}-\\text{H}$), not directly to fluorine ($\\text{F}-\\text{H}$), so pure $\\text{CH}_2\\text{F}_2$ cannot form intermolecular hydrogen bonds."
    },

    # -------------------------------------------------------------------------
    # Topic 3.2: Properties of Solids (Q6 - Q9)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 6,
        "topic_code": "3.2",
        "topic_title": "Properties of Solids",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            '<thead><tr><th>Solid</th><th>Melting Point ($^\\circ\\text{C}$)</th><th>Electrical Conductivity of Solid</th><th>Electrical Conductivity of Liquid (Molten)</th><th>Solubility in Water</th></tr></thead>'
            '<tbody>'
            '<tr><td>$\\text{W}$</td><td>$1610$</td><td>Negligible</td><td>Negligible</td><td>Insoluble</td></tr>'
            '<tr><td>$\\text{X}$</td><td>$801$</td><td>Negligible</td><td>High</td><td>Soluble</td></tr>'
            '<tr><td>$\\text{Y}$</td><td>$114$</td><td>Negligible</td><td>Negligible</td><td>Insoluble</td></tr>'
            '<tr><td>$\\text{Z}$</td><td>$1085$</td><td>High</td><td>High</td><td>Insoluble</td></tr>'
            '</tbody></table>'
        ),
        "question": "The properties of four pure solids—$\\text{W}$, $\\text{X}$, $\\text{Y}$, and $\\text{Z}$—are summarized in the table above. Which of the following correctly identifies the classification of all four solids?",
        "options": [
            "$\\text{W}$: Ionic; $\\text{X}$: Covalent network; $\\text{Y}$: Molecular; $\\text{Z}$: Metallic",
            "$\\text{W}$: Covalent network; $\\text{X}$: Metallic; $\\text{Y}$: Ionic; $\\text{Z}$: Molecular",
            "$\\text{W}$: Molecular; $\\text{X}$: Ionic; $\\text{Y}$: Covalent network; $\\text{Z}$: Metallic",
            "$\\text{W}$: Covalent network; $\\text{X}$: Ionic; $\\text{Y}$: Molecular; $\\text{Z}$: Metallic"
        ],
        "correct_index": 3,
        "explanation": "Solid $\\text{W}$ (e.g., $\\text{SiO}_2$) has a very high melting point, does not conduct electricity as a solid or liquid, and is insoluble in water, characteristic of a covalent network solid. Solid $\\text{X}$ (e.g., $\\text{NaCl}$) has a high melting point and conducts electricity only when melted (or dissolved) because its ions become mobile, characteristic of an ionic solid. Solid $\\text{Y}$ (e.g., $\\text{I}_2$) has a low melting point and is a nonconductor, characteristic of a molecular solid. Solid $\\text{Z}$ (e.g., $\\text{Cu}$) conducts electricity in both solid and liquid states due to delocalized valence electrons, characteristic of a metallic solid."
    },
    {
        "unit_q_num": 7,
        "topic_code": "3.2",
        "topic_title": "Properties of Solids",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            '<thead><tr><th>Compound</th><th>Cation Radius ($\\text{pm}$)</th><th>Anion Radius ($\\text{pm}$)</th><th>Melting Point ($^\\circ\\text{C}$)</th></tr></thead>'
            '<tbody>'
            '<tr><td>$\\text{NaF}$</td><td>$102$</td><td>$133$</td><td>$993$</td></tr>'
            '<tr><td>$\\text{NaCl}$</td><td>$102$</td><td>$181$</td><td>$801$</td></tr>'
            '<tr><td>$\\text{MgO}$</td><td>$72$</td><td>$140$</td><td>$2852$</td></tr>'
            '<tr><td>$\\text{CaO}$</td><td>$100$</td><td>$140$</td><td>$2572$</td></tr>'
            '</tbody></table>'
        ),
        "question": "Based on Coulomb's law and the data in the table, which of the following best explains why the melting point of $\\text{MgO}$ is more than $1800^\\circ\\text{C}$ higher than that of $\\text{NaF}$, whereas the melting point of $\\text{NaF}$ is only $192^\\circ\\text{C}$ higher than that of $\\text{NaCl}$?",
        "options": [
            "$\\text{MgO}$ forms a three-dimensional covalent network lattice, whereas $\\text{NaF}$ and $\\text{NaCl}$ form ionic lattices.",
            "The doubling of ionic charges from $+1/-1$ in $\\text{NaF}$ to $+2/-2$ in $\\text{MgO}$ quadruples the numerator in Coulomb's law ($F \\propto |q_1 q_2|/r^2$), which has a much larger impact on lattice energy than the smaller interionic distance differences between $\\text{NaF}$ and $\\text{NaCl}$.",
            "$\\text{Mg}^{2+}$ and $\\text{O}^{2-}$ have more total electrons than $\\text{Na}^+$ and $\\text{F}^-$, resulting in stronger London dispersion forces in $\\text{MgO}$.",
            "The electronegativity difference between $\\text{Mg}$ and $\\text{O}$ is greater than that between $\\text{Na}$ and $\\text{F}$."
        ],
        "correct_index": 1,
        "explanation": "According to Coulomb's law, electrostatic lattice energy is proportional to $|q_1 q_2|/r$. Going from $\\text{NaF}$ ($+1, -1$) to $\\text{MgO}$ ($+2, -2$) increases $|q_1 q_2|$ by a factor of $4$, and $\\text{Mg}^{2+}$ is also smaller than $\\text{Na}^+$, producing a dramatic increase in lattice energy and melting point. By contrast, $\\text{NaF}$ and $\\text{NaCl}$ have the same ionic charges ($+1, -1$) and differ only in anion radius ($\\text{F}^- < \\text{Cl}^-$)."
    },
    {
        "unit_q_num": 8,
        "topic_code": "3.2",
        "topic_title": "Properties of Solids",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "Both diamond and graphite are allotropes of pure carbon with very high melting points, yet graphite is a good electrical conductor and a soft lubricant whereas diamond is an electrical insulator and one of the hardest known substances. Which of the following structural differences best explains these contrasting properties?",
        "options": [
            "Diamond is a covalent network solid, whereas graphite is an ionic solid containing $\\text{C}^{4+}$ and $\\text{C}^{4-}$ ions.",
            "In diamond, each carbon atom is $sp^3$ hybridized in a rigid 3D tetrahedral network; in graphite, each carbon atom is $sp^2$ hybridized in planar 2D sheets with delocalized $\\pi$ electrons and weak London dispersion forces between layers.",
            "In diamond, carbon atoms are held together by strong covalent bonds; in graphite, carbon atoms within each sheet are held together only by dipole-dipole forces.",
            "Graphite contains mobile interstitial hydrogen atoms that conduct electricity and allow layers to slide past one another."
        ],
        "correct_index": 1,
        "explanation": "In diamond, every carbon atom is $sp^3$ hybridized and covalently bonded to four other carbon atoms in a rigid 3D tetrahedral lattice with localized $\\sigma$ electrons, making it superhard and an electrical insulator. In graphite, carbon atoms are $sp^2$ hybridized in planar hexagonal sheets with delocalized unhybridized $p$ ($\\pi$) electrons that conduct electricity along the sheets, while the sheets are held together only by weak London dispersion forces and can slide easily."
    },
    {
        "unit_q_num": 9,
        "topic_code": "3.2",
        "topic_title": "Properties of Solids",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "Pure iron ($\\text{Fe}$, atomic radius $126\\text{ pm}$) is alloyed with a small percentage of carbon ($\\text{C}$, atomic radius $77\\text{ pm}$) to produce carbon steel. How does the presence of carbon atoms in the iron lattice affect the mechanical properties of the metal?",
        "options": [
            "Carbon atoms replace iron atoms in a substitutional alloy, increasing the malleability and ductility of the metal.",
            "Carbon atoms occupy interstitial spaces between the larger iron atoms, making the lattice more rigid and decreasing malleability by impeding the sliding of metal atom planes.",
            "Carbon transfers its valence electrons to iron to form an ionic compound ($\\text{Fe}_3\\text{C}$) that shatters upon any impact and loses all electrical conductivity.",
            "Carbon atoms form a separate layer on the surface of the iron, which increases ductility by lubricating the metallic bonds."
        ],
        "correct_index": 1,
        "explanation": "Because carbon's atomic radius ($77\\text{ pm}$) is much smaller than iron's ($126\\text{ pm}$), carbon atoms fit into the small holes (interstices) between iron atoms in the metallic crystal lattice, forming an interstitial alloy. These interstitial carbon atoms lock the planes of iron cations in place and make it harder for layers to slide past one another under stress, increasing hardness and tensile strength while reducing malleability and ductility."
    },

    # -------------------------------------------------------------------------
    # Topic 3.3: Solids, Liquids, and Gases (Q10 - Q13)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 10,
        "topic_code": "3.3",
        "topic_title": "Solids, Liquids, and Gases",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            '<thead><tr><th>Temperature ($^\\circ\\text{C}$)</th><th>Vapor Pressure of Diethyl Ether ($\\text{torr}$)</th><th>Vapor Pressure of Ethanol ($\\text{torr}$)</th><th>Vapor Pressure of Water ($\\text{torr}$)</th></tr></thead>'
            '<tbody>'
            '<tr><td>$0$</td><td>$185$</td><td>$12$</td><td>$4.6$</td></tr>'
            '<tr><td>$20$</td><td>$442$</td><td>$44$</td><td>$17.5$</td></tr>'
            '<tr><td>$34.6$</td><td>$760$</td><td>$100$</td><td>$41.2$</td></tr>'
            '<tr><td>$78.3$</td><td>$>2500$</td><td>$760$</td><td>$330$</td></tr>'
            '<tr><td>$100.0$</td><td>$>4500$</td><td>$1690$</td><td>$760$</td></tr>'
            '</tbody></table>'
        ),
        "question": "A mountain laboratory operates at an atmospheric pressure of $442\\text{ torr}$. Based on the vapor pressure data in the table above, which of the following statements is true regarding the three liquids in an open container in this laboratory at $20^\\circ\\text{C}$?",
        "options": [
            "Diethyl ether is at its boiling point at $20^\\circ\\text{C}$, whereas ethanol and water are liquids below their boiling points.",
            "All three liquids will boil at higher temperatures in this laboratory than they do at sea level ($760\\text{ torr}$).",
            "At $34.6^\\circ\\text{C}$ in this laboratory, ethanol has stronger intermolecular forces than water because its vapor pressure is higher.",
            "The normal boiling point of diethyl ether in this laboratory is $20^\\circ\\text{C}$."
        ],
        "correct_index": 0,
        "explanation": "A liquid boils when its equilibrium vapor pressure equals the external atmospheric pressure. Since the external pressure in the mountain lab is $442\\text{ torr}$ and the vapor pressure of diethyl ether at $20^\\circ\\text{C}$ is $442\\text{ torr}$, diethyl ether boils at $20^\\circ\\text{C}$ in this lab. (Note that the 'normal' boiling point is defined specifically at $1\\text{ atm} = 760\\text{ torr}$, which remains $34.6^\\circ\\text{C}$)."
    },
    {
        "unit_q_num": 11,
        "topic_code": "3.3",
        "topic_title": "Solids, Liquids, and Gases",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "When a sample of liquid ammonia, $\\text{NH}_3(l)$, is heated at its boiling point of $-33^\\circ\\text{C}$ and $1\\text{ atm}$ until it is completely converted to a gas at $-33^\\circ\\text{C}$, which of the following occurs at the particulate level?",
        "options": [
            "Covalent $\\text{N}-\\text{H}$ bonds are broken, producing $\\text{N}_2(g)$ and $\\text{H}_2(g)$ molecules that move at higher speeds.",
            "Intermolecular hydrogen bonds and dipole-dipole attractions between $\\text{NH}_3$ molecules are overcome, and the average distance between $\\text{NH}_3$ molecules increases dramatically.",
            "The average kinetic energy of the $\\text{NH}_3$ molecules increases while the potential energy of the system remains constant.",
            "The $\\text{NH}_3$ molecules expand in size until they fill the volume of the container."
        ],
        "correct_index": 1,
        "explanation": "During a phase change (boiling/vaporization) at constant temperature, the thermal energy added goes into increasing the potential energy of the system by overcoming intermolecular forces (hydrogen bonding, dipole-dipole, and LDFs between intact $\\text{NH}_3$ molecules), separating the molecules to much greater average distances. Intramolecular $\\text{N}-\\text{H}$ covalent bonds are NOT broken, and the average kinetic energy remains constant because the temperature remains at $-33^\\circ\\text{C}$."
    },
    {
        "unit_q_num": 12,
        "topic_code": "3.3",
        "topic_title": "Solids, Liquids, and Gases",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": "A rigid, evacuated $2.0\\text{ L}$ vessel is held at a constant temperature of $35^\\circ\\text{C}$. At this temperature, the equilibrium vapor pressure of pure liquid bromine, $\\text{Br}_2(l)$, is $320\\text{ torr}$. First, $0.10\\text{ mol}$ of $\\text{Br}_2(l)$ is injected into the vessel, and liquid $\\text{Br}_2$ remains in equilibrium with $\\text{Br}_2(g)$ at $320\\text{ torr}$. If the volume of the vessel is then slowly expanded to $4.0\\text{ L}$ at constant temperature ($35^\\circ\\text{C}$) and a small pool of $\\text{Br}_2(l)$ is still present at the bottom, what is the final pressure inside the $4.0\\text{ L}$ vessel?",
        "options": [
            "$160\\text{ torr}$",
            "$240\\text{ torr}$",
            "$320\\text{ torr}$",
            "$640\\text{ torr}$"
        ],
        "correct_index": 2,
        "explanation": "Equilibrium vapor pressure depends ONLY on the identity of the liquid (strength of IMFs) and the temperature—it is independent of the container volume or surface area as long as both liquid and vapor phases remain in equilibrium. When the volume doubles from $2.0\\text{ L}$ to $4.0\\text{ L}$ at constant temperature, additional $\\text{Br}_2(l)$ evaporates until the equilibrium vapor pressure is restored to $320\\text{ torr}$."
    },
    {
        "unit_q_num": 13,
        "topic_code": "3.3",
        "topic_title": "Solids, Liquids, and Gases",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "Which of the following best compares the compressibility and particle motion of a substance in the solid, liquid, and gas phases?",
        "options": [
            "Solids and liquids have similar, very low compressibilities because particles are closely packed in both phases, whereas in liquids particles can translate past one another while in solids they only vibrate about fixed lattice positions.",
            "Liquids are nearly as compressible as gases because particles in both phases are in constant random translational motion with no fixed positions.",
            "Solids have particles that are completely motionless above $0\\text{ K}$, whereas liquids and gases have vibrating and translating particles.",
            "Gases have low compressibility because high-speed collisions between gas molecules create strong repulsive forces."
        ],
        "correct_index": 0,
        "explanation": "In both solids and liquids (condensed phases), particles are in close contact with very little empty space between them, making both solids and liquids nearly incompressible. In a solid, particles vibrate about fixed positions; in a liquid, particles are still close together but have enough kinetic energy to slide/translate past one another; in a gas, particles are separated by large distances and are highly compressible."
    },

    # -------------------------------------------------------------------------
    # Topic 3.4: Ideal Gas Law (Q14 - Q18)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 14,
        "topic_code": "3.4",
        "topic_title": "Ideal Gas Law",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            '<thead><tr><th>Measurement</th><th>Recorded Value</th></tr></thead>'
            '<tbody>'
            '<tr><td>Mass of volatile liquid vaporized</td><td>$0.840\\text{ g}$</td></tr>'
            '<tr><td>Volume of Dumas flask</td><td>$0.250\\text{ L}$</td></tr>'
            '<tr><td>Temperature of boiling water bath</td><td>$99.0^\\circ\\text{C}$ ($372\\text{ K}$)</td></tr>'
            '<tr><td>Barometric pressure</td><td>$0.985\\text{ atm}$</td></tr>'
            '</tbody></table>'
        ),
        "question": "A student uses the Dumas bulb method to determine the molar mass of an unknown volatile liquid using the experimental data in the table above. Assuming ideal gas behavior ($R = 0.08206\\text{ L}\\cdot\\text{atm}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-1}$), what is the molar mass of the unknown liquid?",
        "options": [
            "$28.1\\text{ g/mol}$",
            "$84.2\\text{ g/mol}$",
            "$104\\text{ g/mol}$",
            "$120\\text{ g/mol}$"
        ],
        "correct_index": 2,
        "explanation": "Using the ideal gas law $PV = nRT = (m/\\mathcal{M})RT$, we solve for molar mass $\\mathcal{M} = \\frac{mRT}{PV}$. Substituting the given values: $\\mathcal{M} = \\frac{(0.840\\text{ g})(0.08206\\text{ L}\\cdot\\text{atm}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-1})(372\\text{ K})}{(0.985\\text{ atm})(0.250\\text{ L})} = \\frac{25.64}{0.24625} \\approx 104\\text{ g/mol}$."
    },
    {
        "unit_q_num": 15,
        "topic_code": "3.4",
        "topic_title": "Ideal Gas Law",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            '<thead><tr><th>Gas</th><th>Mass in Mixture ($\\text{g}$)</th><th>Molar Mass ($\\text{g/mol}$)</th></tr></thead>'
            '<tbody>'
            '<tr><td>$\\text{He}$</td><td>$1.00$</td><td>$4.00$</td></tr>'
            '<tr><td>$\\text{Ne}$</td><td>$5.00$</td><td>$20.0$</td></tr>'
            '<tr><td>$\\text{Ar}$</td><td>$20.0$</td><td>$40.0$</td></tr>'
            '</tbody></table>'
        ),
        "question": "A rigid steel cylinder contains a mixture of helium, neon, and argon gases in the amounts shown in the table above. If the total pressure in the cylinder at $298\\text{ K}$ is $4.00\\text{ atm}$, what is the partial pressure of neon ($P_{\\text{Ne}}$) in the mixture?",
        "options": [
            "$2.00\\text{ atm}$",
            "$1.33\\text{ atm}$",
            "$1.00\\text{ atm}$",
            "$0.77\\text{ atm}$"
        ],
        "correct_index": 2,
        "explanation": "First calculate the moles of each gas: $n_{\\text{He}} = 1.00 / 4.00 = 0.250\\text{ mol}$, $n_{\\text{Ne}} = 5.00 / 20.0 = 0.250\\text{ mol}$, and $n_{\\text{Ar}} = 20.0 / 40.0 = 0.500\\text{ mol}$. The total moles of gas is $n_{\\text{total}} = 0.250 + 0.250 + 0.500 = 1.000\\text{ mol}$. The mole fraction of $\\text{Ne}$ is $\\chi_{\\text{Ne}} = 0.250 / 1.000 = 0.250$. By Dalton's Law of Partial Pressures, $P_{\\text{Ne}} = \\chi_{\\text{Ne}} P_{\\text{total}} = 0.250 \\times 4.00\\text{ atm} = 1.00\\text{ atm}$."
    },
    {
        "unit_q_num": 16,
        "topic_code": "3.4",
        "topic_title": "Ideal Gas Law",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '$$2\\,\\text{KClO}_3(s) \\xrightarrow{\\text{MnO}_2,\\, \\Delta} 2\\,\\text{KCl}(s) + 3\\,\\text{O}_2(g)$$\n'
            '<table class="quiz-data-table">'
            '<thead><tr><th>Parameter</th><th>Value</th></tr></thead>'
            '<tbody>'
            '<tr><td>Total pressure in collection bottle</td><td>$754.0\\text{ torr}$</td></tr>'
            '<tr><td>Vapor pressure of water at $22.0^\\circ\\text{C}$</td><td>$19.8\\text{ torr}$</td></tr>'
            '<tr><td>Volume of gas collected</td><td>$0.600\\text{ L}$</td></tr>'
            '<tr><td>Temperature</td><td>$22.0^\\circ\\text{C}$ ($295\\text{ K}$)</td></tr>'
            '</tbody></table>'
        ),
        "question": "Oxygen gas produced by the catalytic decomposition of $\\text{KClO}_3(s)$ is collected over water at $22.0^\\circ\\text{C}$ according to the data above. How many moles of pure $\\text{O}_2(g)$ were collected? ($1\\text{ atm} = 760\\text{ torr}$, $R = 0.08206\\text{ L}\\cdot\\text{atm}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-1}$)",
        "options": [
            "$0.326\\text{ mol}$",
            "$0.0246\\text{ mol}$",
            "$0.0239\\text{ mol}$",
            "$0.0156\\text{ mol}$"
        ],
        "correct_index": 2,
        "explanation": "By Dalton's law, the partial pressure of dry $\\text{O}_2(g)$ is $P_{\\text{O}_2} = P_{\\text{total}} - P_{\\text{H}_2\\text{O}} = 754.0\\text{ torr} - 19.8\\text{ torr} = 734.2\\text{ torr}$. Converting to atmospheres gives $P_{\\text{O}_2} = 734.2 / 760 = 0.9661\\text{ atm}$. Using $n = \\frac{PV}{RT}$: $n_{\\text{O}_2} = \\frac{(0.9661\\text{ atm})(0.600\\text{ L})}{(0.08206\\text{ L}\\cdot\\text{atm}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-1})(295\\text{ K})} = \\frac{0.5796}{24.21} = 0.0239\\text{ mol}$."
    },
    {
        "unit_q_num": 17,
        "topic_code": "3.4",
        "topic_title": "Ideal Gas Law",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": "Two rigid bulbs are connected by a closed stopcock of negligible volume at a constant temperature of $300\\text{ K}$. Bulb A has a volume of $2.00\\text{ L}$ and contains $\\text{N}_2(g)$ at $3.00\\text{ atm}$. Bulb B has a volume of $3.00\\text{ L}$ and contains $\\text{Ar}(g)$ at $1.00\\text{ atm}$. When the stopcock is opened and the gases mix completely at $300\\text{ K}$, what is the final total pressure in the system?",
        "options": [
            "$4.00\\text{ atm}$",
            "$2.20\\text{ atm}$",
            "$2.00\\text{ atm}$",
            "$1.80\\text{ atm}$"
        ],
        "correct_index": 3,
        "explanation": "At constant temperature, we can apply Boyle's law ($P_1 V_1 = P_2 V_{\\text{total}}$) to each non-reacting gas independently into the combined volume $V_{\\text{total}} = 2.00\\text{ L} + 3.00\\text{ L} = 5.00\\text{ L}$. For $\\text{N}_2$: $P_{\\text{N}_2} = \\frac{(3.00\\text{ atm})(2.00\\text{ L})}{5.00\\text{ L}} = 1.20\\text{ atm}$. For $\\text{Ar}$: $P_{\\text{Ar}} = \\frac{(1.00\\text{ atm})(3.00\\text{ L})}{5.00\\text{ L}} = 0.60\\text{ atm}$. Thus, $P_{\\text{total}} = 1.20\\text{ atm} + 0.60\\text{ atm} = 1.80\\text{ atm}$."
    },
    {
        "unit_q_num": 18,
        "topic_code": "3.4",
        "topic_title": "Ideal Gas Law",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "Which of the following gases has the greatest density ($\\text{g/L}$) at $298\\text{ K}$ and $1.00\\text{ atm}$, assuming ideal behavior?",
        "options": [
            "$\\text{CH}_4$ ($\\mathcal{M} = 16.0\\text{ g/mol}$)",
            "$\\text{N}_2$ ($\\mathcal{M} = 28.0\\text{ g/mol}$)",
            "$\\text{CO}_2$ ($\\mathcal{M} = 44.0\\text{ g/mol}$)",
            "$\\text{SF}_6$ ($\\mathcal{M} = 146.1\\text{ g/mol}$)"
        ],
        "correct_index": 3,
        "explanation": "Rearranging the ideal gas law $PV = (m/\\mathcal{M})RT$ gives gas density $d = \\frac{m}{V} = \\frac{P\\mathcal{M}}{RT}$. At the same temperature and pressure, the density of an ideal gas is directly proportional to its molar mass ($\\mathcal{M}$). Since $\\text{SF}_6$ has the largest molar mass ($146.1\\text{ g/mol}$), it has the greatest density."
    },

    # -------------------------------------------------------------------------
    # Topic 3.5: Kinetic Molecular Theory (Q19 - Q22)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 19,
        "topic_code": "3.5",
        "topic_title": "Kinetic Molecular Theory",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            '<thead><tr><th>Flask</th><th>Gas</th><th>Molar Mass ($\\text{g/mol}$)</th><th>Volume ($\\text{L}$)</th><th>Pressure ($\\text{atm}$)</th><th>Temperature ($\\text{K}$)</th></tr></thead>'
            '<tbody>'
            '<tr><td>1</td><td>$\\text{H}_2$</td><td>$2.02$</td><td>$1.0$</td><td>$1.0$</td><td>$300$</td></tr>'
            '<tr><td>2</td><td>$\\text{He}$</td><td>$4.00$</td><td>$1.0$</td><td>$2.0$</td><td>$300$</td></tr>'
            '<tr><td>3</td><td>$\\text{O}_2$</td><td>$32.0$</td><td>$1.0$</td><td>$1.0$</td><td>$300$</td></tr>'
            '</tbody></table>'
        ),
        "question": "Three rigid $1.0\\text{ L}$ flasks contain pure gases as described in the table above. Which of the following correctly compares the average kinetic energy ($\\overline{KE}$) and root-mean-square speed ($u_{\\text{rms}}$) of the gas particles in the three flasks?",
        "options": [
            "$\\overline{KE}_1 = \\overline{KE}_2 = \\overline{KE}_3$ and $u_{\\text{rms},1} > u_{\\text{rms},2} > u_{\\text{rms},3}$",
            "$\\overline{KE}_2 > \\overline{KE}_1 = \\overline{KE}_3$ and $u_{\\text{rms},1} = u_{\\text{rms},2} = u_{\\text{rms},3}$",
            "$\\overline{KE}_3 > \\overline{KE}_2 > \\overline{KE}_1$ and $u_{\\text{rms},1} > u_{\\text{rms},2} > u_{\\text{rms},3}$",
            "$\\overline{KE}_1 = \\overline{KE}_2 = \\overline{KE}_3$ and $u_{\\text{rms},3} > u_{\\text{rms},2} > u_{\\text{rms},1}$"
        ],
        "correct_index": 0,
        "explanation": "According to kinetic molecular theory, the average kinetic energy of the particles of any gas is proportional to the Kelvin temperature and does not depend on the identity of the gas or on its pressure. Because all three flasks are at $300\\text{ K}$, $\\overline{KE}_1 = \\overline{KE}_2 = \\overline{KE}_3$; the higher pressure in Flask 2 means that it contains more $\\text{He}$ atoms, not faster ones. Because $KE = \\frac{1}{2}mv^2$ is the same for all three gases, lighter particles must move faster: $u_{\\text{rms}} = \\sqrt{\\frac{3RT}{\\mathcal{M}}}$, which is inversely proportional to the square root of molar mass at constant $T$. Since $\\mathcal{M}_{\\text{H}_2} < \\mathcal{M}_{\\text{He}} < \\mathcal{M}_{\\text{O}_2}$, $u_{\\text{rms},1} > u_{\\text{rms},2} > u_{\\text{rms},3}$."
    },
    {
        "unit_q_num": 20,
        "topic_code": "3.5",
        "topic_title": "Kinetic Molecular Theory",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": "On a Maxwell-Boltzmann molecular speed distribution plot for $\\text{N}_2(g)$ at $300\\text{ K}$ and $600\\text{ K}$ (containing the same total number of molecules), how does the curve at $600\\text{ K}$ compare to the curve at $300\\text{ K}$?",
        "options": [
            "The peak of the $600\\text{ K}$ curve is higher and shifted to a higher molecular speed, and the area under the $600\\text{ K}$ curve is twice as large.",
            "The peak of the $600\\text{ K}$ curve stays at the same most probable speed, but the tail at high speeds extends further to the right.",
            "The peak of the $600\\text{ K}$ curve is shifted to exactly twice the speed of the $300\\text{ K}$ peak, and the curve becomes narrower.",
            "The peak of the $600\\text{ K}$ curve is lower and shifted to a higher molecular speed, the distribution is broader, and the total area under both curves is identical."
        ],
        "correct_index": 3,
        "explanation": "In a Maxwell-Boltzmann distribution, the total area under the curve represents the total number of molecules (or $100\\%$ of the sample), which remains constant when temperature changes. Increasing temperature from $300\\text{ K}$ to $600\\text{ K}$ increases the average speed and broadens the range of speeds; because the area is conserved and the curve spreads out to higher speeds, the peak height must decrease while shifting to the right (by a factor of $\\sqrt{600/300} = \\sqrt{2}$)."
    },
    {
        "unit_q_num": 21,
        "topic_code": "3.5",
        "topic_title": "Kinetic Molecular Theory",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "A rigid, sealed container holds $1.0\\text{ mol}$ of $\\text{Ar}(g)$ at $250\\text{ K}$. When the gas is heated to $500\\text{ K}$, the pressure inside the container doubles. According to Kinetic Molecular Theory, which of the following explains why the pressure increases?",
        "options": [
            "The $\\text{Ar}$ atoms expand to twice their original volume, reducing the free space in the container.",
            "Attractive forces between $\\text{Ar}$ atoms convert into repulsive forces above $300\\text{ K}$.",
            "The $\\text{Ar}$ atoms move with a higher average speed, so they collide with the container walls more frequently and with greater average force per collision.",
            "The number of moles of $\\text{Ar}(g)$ doubles when the absolute temperature is doubled."
        ],
        "correct_index": 2,
        "explanation": "According to Kinetic Molecular Theory, raising the absolute temperature increases the average kinetic energy and average speed of the gas particles. In a rigid container of fixed volume, faster-moving particles strike the walls both more frequently (more collisions per second) and more forcefully (greater momentum transfer per collision), resulting in higher pressure."
    },
    {
        "unit_q_num": 22,
        "topic_code": "3.5",
        "topic_title": "Kinetic Molecular Theory",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"According to kinetic molecular theory, the average kinetic energy of the particles in a gas is proportional to the Kelvin temperature, and the kinetic energy of a particle is related to its speed by $KE = \frac{1}{2}mv^2$. A sample of $\text{He}(g)$ ($\mathcal{M} = 4.0\text{ g/mol}$) is at $150\text{ K}$. At what temperature would the molecules in a sample of $\text{CH}_4(g)$ ($\mathcal{M} = 16.0\text{ g/mol}$) have the same average speed as the $\text{He}$ atoms at $150\text{ K}$?",
        "options": [
            r"$37.5\text{ K}$",
            r"$150\text{ K}$",
            r"$300\text{ K}$",
            r"$600\text{ K}$",
        ],
        "correct_index": 3,
        "explanation": r"For particles moving at the same speed $v$, $KE = \frac{1}{2}mv^2$ is proportional to the particle's mass. A $\text{CH}_4$ molecule is $16.0/4.0 = 4$ times as massive as a $\text{He}$ atom, so at equal average speeds the $\text{CH}_4$ molecules must have $4$ times the average kinetic energy of the $\text{He}$ atoms. Because average kinetic energy is proportional to Kelvin temperature, $T_{\text{CH}_4} = 4 \times 150\text{ K} = 600\text{ K}$. Choosing $150\text{ K}$ confuses equal average kinetic energy (which equal temperatures do give) with equal speed; $300\text{ K}$ comes from scaling by $\sqrt{4}$ instead of $4$ (speed is proportional to $\sqrt{T/\mathcal{M}}$, so $T$ must scale by the full mass ratio); $37.5\text{ K}$ inverts the mass ratio.",
    },

    # -------------------------------------------------------------------------
    # Topic 3.6: Deviation from Ideal Gas Law (Q23 - Q25)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 23,
        "topic_code": "3.6",
        "topic_title": "Deviation from Ideal Gas Law",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "Under which of the following conditions of temperature and pressure will a real gas deviate MOST from ideal gas behavior?",
        "options": [
            "$T = 100\\text{ K}$ and $P = 50\\text{ atm}$",
            "$T = 100\\text{ K}$ and $P = 0.10\\text{ atm}$",
            "$T = 600\\text{ K}$ and $P = 50\\text{ atm}$",
            "$T = 600\\text{ K}$ and $P = 0.10\\text{ atm}$"
        ],
        "correct_index": 0,
        "explanation": "Real gases deviate most from ideal behavior at low temperatures and high pressures. At high pressures ($50\\text{ atm}$), gas molecules are crowded closely together so their finite molecular volume is a significant fraction of the total container volume, and intermolecular distances are short. At low temperatures ($100\\text{ K}$), molecules move slowly with low kinetic energy, making intermolecular attractions significant during collisions."
    },
    {
        "unit_q_num": 24,
        "topic_code": "3.6",
        "topic_title": "Deviation from Ideal Gas Law",
        "difficulty": "Challenging",
        "stimulus": (
            r'<table class="quiz-data-table">'
            r'<thead><tr><th>Gas</th><th>Molar Mass ($\text{g/mol}$)</th><th>Normal Boiling Point ($\text{K}$)</th></tr></thead>'
            r'<tbody>'
            r'<tr><td>$\text{He}$</td><td>$4.0$</td><td>$4$</td></tr>'
            r'<tr><td>$\text{N}_2$</td><td>$28.0$</td><td>$77$</td></tr>'
            r'<tr><td>$\text{CH}_4$</td><td>$16.0$</td><td>$112$</td></tr>'
            r'<tr><td>$\text{NH}_3$</td><td>$17.0$</td><td>$240$</td></tr>'
            r'</tbody></table>'
        ),
        "question": r"Separate samples of the four gases in the table above are each held at $300\text{ K}$ and $1.0\text{ atm}$. Which gas would be expected to deviate the most from ideal gas behavior under these conditions, and why?",
        "options": [
            r"$\text{He}$, because its atoms are the smallest and move the fastest, so they collide with the container walls most often.",
            r"$\text{N}_2$, because it has the greatest molar mass, so its molecules occupy the largest fraction of the container volume.",
            r"$\text{NH}_3$, because hydrogen bonding gives it the strongest intermolecular attractions, which make its molecules strike the walls less often and with less force, so the measured pressure is less than the ideal-gas prediction.",
            r"$\text{NH}_3$, because hydrogen bonding causes its molecules to repel one another, so the measured pressure is greater than the ideal-gas prediction.",
        ],
        "correct_index": 2,
        "explanation": r"Deviations from ideal behavior arise mainly from interparticle attractions, especially at conditions close to condensation. $\text{NH}_3$ has the strongest intermolecular forces of the four gases (hydrogen bonding in addition to dipole-dipole and London dispersion forces), as reflected by its much higher boiling point ($240\text{ K}$, the closest to $300\text{ K}$). These attractions pull molecules toward one another as they approach a wall, so collisions with the walls are less frequent and less forceful, and the measured pressure is lower than $nRT/V$. Hydrogen bonds are attractive, not repulsive, so they cannot make the pressure greater than ideal. At $1.0\text{ atm}$ the volume of the particles themselves is negligible for all four gases, so molar mass or atomic size is not the deciding factor; $\text{He}$, with the weakest attractions, behaves the most ideally.",
    },
    {
        "unit_q_num": 25,
        "topic_code": "3.6",
        "topic_title": "Deviation from Ideal Gas Law",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"A rigid steel cylinder contains $\text{N}_2(g)$ at $300\text{ K}$. More $\text{N}_2$ is pumped into the cylinder until the pressure reaches about $1000\text{ atm}$, still at $300\text{ K}$. Under these conditions, the measured pressure is significantly GREATER than the pressure calculated with the ideal gas law for the same $n$, $V$, and $T$. Which of the following best explains this deviation?",
        "options": [
            r"At such a high pressure, the attractions between $\text{N}_2$ molecules become stronger, causing the molecules to strike the walls with greater force.",
            r"At such a high pressure, the average kinetic energy of the $\text{N}_2$ molecules is greater than it is at low pressure at the same temperature.",
            r"At such a high pressure, some $\text{N}_2$ molecules break apart into $\text{N}$ atoms, increasing the number of gas particles.",
            r"The $\text{N}_2$ molecules themselves occupy a significant fraction of the cylinder's volume, so the space in which they move is smaller than $V$ and they collide with the walls more often than the ideal gas law predicts.",
        ],
        "correct_index": 3,
        "explanation": r"The ideal gas law treats gas particles as points with no volume. That approximation works well at ordinary pressures, but at extremely high pressures the molecules are crowded so closely that their own volume is a substantial part of the container volume. The space actually available for their motion is less than $V$, so the molecules strike the walls more frequently than predicted and the measured pressure exceeds $nRT/V$. Intermolecular attractions have the opposite effect: they reduce the frequency and force of wall collisions and lower the pressure, so they cannot explain a pressure that is greater than ideal. Average kinetic energy depends only on temperature, which is unchanged, and compressing $\text{N}_2$ does not break its strong triple bond.",
    },

    # -------------------------------------------------------------------------
    # Topic 3.7: Solutions and Mixtures (Q26 - Q29)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 26,
        "topic_code": "3.7",
        "topic_title": "Solutions and Mixtures",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "A chemist needs to prepare $250.0\\text{ mL}$ of a $0.200\\text{ M}$ aqueous solution of anhydrous sodium sulfate, $\\text{Na}_2\\text{SO}_4$ ($\\mathcal{M} = 142.04\\text{ g/mol}$). Which of the following laboratory procedures is most accurate?",
        "options": [
            "Weigh out $7.10\\text{ g}$ of $\\text{Na}_2\\text{SO}_4(s)$, transfer it to a $250.0\\text{ mL}$ volumetric flask, dissolve in about $150\\text{ mL}$ of distilled water, swirl to mix, and then add distilled water to the $250.0\\text{ mL}$ calibration mark.",
            "Weigh out $7.10\\text{ g}$ of $\\text{Na}_2\\text{SO}_4(s)$ into a $400\\text{ mL}$ beaker and add exactly $250.0\\text{ mL}$ of distilled water measured with a graduated cylinder.",
            "Weigh out $28.4\\text{ g}$ of $\\text{Na}_2\\text{SO}_4(s)$, transfer it to a $250.0\\text{ mL}$ Erlenmeyer flask, and fill with distilled water to the $250\\text{ mL}$ line.",
            "Weigh out $3.55\\text{ g}$ of $\\text{Na}_2\\text{SO}_4(s)$, transfer it to a $250.0\\text{ mL}$ volumetric flask, and add distilled water to the calibration mark."
        ],
        "correct_index": 0,
        "explanation": "First calculate the required moles and mass: $n = M \\times V = (0.200\\text{ mol/L})(0.2500\\text{ L}) = 0.0500\\text{ mol}$, and $\\text{mass} = 0.0500\\text{ mol} \\times 142.04\\text{ g/mol} = 7.10\\text{ g}$. Because molarity is moles of solute per liter of total solution (and volumes are not strictly additive), the solid must first be dissolved completely in less than $250\\text{ mL}$ of water in a $250.0\\text{ mL}$ volumetric flask and the solution then diluted to the calibration mark. Adding $250.0\\text{ mL}$ of water to the solid gives a total volume that is not exactly $250.0\\text{ mL}$, an Erlenmeyer flask is not a precise volumetric container, and $28.4\\text{ g}$ and $3.55\\text{ g}$ would give $0.800\\text{ M}$ and $0.100\\text{ M}$ solutions."
    },
    {
        "unit_q_num": 27,
        "topic_code": "3.7",
        "topic_title": "Solutions and Mixtures",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": "When $50.0\\text{ mL}$ of $0.30\\text{ M } \\text{AlCl}_3(aq)$ is mixed with $100.0\\text{ mL}$ of $0.15\\text{ M } \\text{CaCl}_2(aq)$ at $25^\\circ\\text{C}$ (assuming no reaction occurs and volumes are additive), what is the final molar concentration of chloride ions, $[\\text{Cl}^-]$, in the resulting solution?",
        "options": [
            "$0.20\\text{ M}$",
            "$0.45\\text{ M}$",
            "$0.50\\text{ M}$",
            "$0.75\\text{ M}$"
        ],
        "correct_index": 2,
        "explanation": "Calculate the total moles of $\\text{Cl}^-$ ions from both soluble salts: From $\\text{AlCl}_3$, each formula unit yields $3\\text{ Cl}^-$, so $n_{\\text{Cl}^-, 1} = (0.0500\\text{ L})(0.30\\text{ M})(3) = 0.045\\text{ mol}$. From $\\text{CaCl}_2$, each formula unit yields $2\\text{ Cl}^-$, so $n_{\\text{Cl}^-, 2} = (0.1000\\text{ L})(0.15\\text{ M})(2) = 0.030\\text{ mol}$. Total moles of $\\text{Cl}^- = 0.045 + 0.030 = 0.075\\text{ mol}$. Total volume $V_{\\text{total}} = 0.0500\\text{ L} + 0.1000\\text{ L} = 0.1500\\text{ L}$. Thus, $[\\text{Cl}^-] = \\frac{0.075\\text{ mol}}{0.1500\\text{ L}} = 0.50\\text{ M}$."
    },
    {
        "unit_q_num": 28,
        "topic_code": "3.7",
        "topic_title": "Solutions and Mixtures",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "What volume of concentrated $12.0\\text{ M } \\text{HCl}(aq)$ stock solution is required to prepare $500.0\\text{ mL}$ of a $0.600\\text{ M } \\text{HCl}(aq)$ solution, and what is the safest procedure for performing this dilution?",
        "options": [
            "$25.0\\text{ mL}$ of $12.0\\text{ M } \\text{HCl}$; slowly add the acid to a volumetric flask already half-filled with distilled water, swirl, and then dilute to the $500.0\\text{ mL}$ mark.",
            "$25.0\\text{ mL}$ of $12.0\\text{ M } \\text{HCl}$; place the concentrated acid in an empty $500.0\\text{ mL}$ volumetric flask and rapidly pour $475.0\\text{ mL}$ of water onto the acid.",
            "$50.0\\text{ mL}$ of $12.0\\text{ M } \\text{HCl}$; slowly add the acid to water and dilute to $500.0\\text{ mL}$.",
            "$10.0\\text{ mL}$ of $12.0\\text{ M } \\text{HCl}$; add water to the acid in a graduated cylinder."
        ],
        "correct_index": 0,
        "explanation": "Using the dilution equation $M_1 V_1 = M_2 V_2$: $V_1 = \\frac{(0.600\\text{ M})(500.0\\text{ mL})}{12.0\\text{ M}} = 25.0\\text{ mL}$. For laboratory safety, concentrated strong acid must always be added slowly to water ('add acid to water') so that the large heat of dilution is absorbed by the larger thermal mass of the water without splattering."
    },
    {
        "unit_q_num": 29,
        "topic_code": "3.7",
        "topic_title": "Solutions and Mixtures",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "Which of the following best distinguishes a homogeneous solution from a heterogeneous mixture at the macroscopic and particulate levels?",
        "options": [
            "A homogeneous solution has a fixed stoichiometric ratio of components like a pure compound, whereas a heterogeneous mixture has variable composition.",
            "A homogeneous solution has uniform composition and properties throughout because solute particles are dispersed at the atomic, ionic, or molecular scale, whereas a heterogeneous mixture has distinct regions with different compositions.",
            "A homogeneous solution can only exist in the liquid state, whereas heterogeneous mixtures can be solids, liquids, or gases.",
            "A homogeneous solution cannot be separated by physical processes such as distillation, whereas a heterogeneous mixture can be separated by filtration."
        ],
        "correct_index": 1,
        "explanation": "A homogeneous mixture (solution)—which can be solid (e.g., brass alloy), liquid (e.g., aqueous $\\text{NaCl}$), or gas (e.g., air)—is uniform throughout at the macroscopic level because its components are intimately mixed at the molecular, atomic, or ionic level. Both homogeneous and heterogeneous mixtures have variable compositions and can be separated by physical means based on differences in physical properties."
    },

    # -------------------------------------------------------------------------
    # Topic 3.8: Representations of Solutions (Q30 - Q33)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 30,
        "topic_code": "3.8",
        "topic_title": "Representations of Solutions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "When solid potassium bromide, $\\text{KBr}(s)$, dissolves in water, water molecules form hydration shells around the dissociated $\\text{K}^+(aq)$ and $\\text{Br}^-(aq)$ ions. Which of the following accurately describes the orientation of water molecules and the primary attractive force involved?",
        "options": [
            "The partially negative oxygen atom of $\\text{H}_2\\text{O}$ points toward $\\text{K}^+$ and the partially positive hydrogen atoms of $\\text{H}_2\\text{O}$ point toward $\\text{Br}^-$ via ion-dipole forces.",
            "The partially positive hydrogen atoms of $\\text{H}_2\\text{O}$ point toward $\\text{K}^+$ and the partially negative oxygen atom of $\\text{H}_2\\text{O}$ points toward $\\text{Br}^-$ via ion-dipole forces.",
            "The oxygen atom of $\\text{H}_2\\text{O}$ forms covalent coordinate bonds with both $\\text{K}^+$ and $\\text{Br}^-$.",
            "Water molecules orient randomly around both $\\text{K}^+$ and $\\text{Br}^-$ because London dispersion forces are nondirectional."
        ],
        "correct_index": 0,
        "explanation": "In a water molecule, oxygen carries a partial negative charge ($\\delta^-$) and the hydrogen atoms carry partial positive charges ($\\delta^+$). By Coulomb's law, opposite charges attract via ion-dipole forces: the $\\delta^-$ oxygen end of $\\text{H}_2\\text{O}$ orients toward the positively charged $\\text{K}^+$ cation, while the $\\delta^+$ hydrogen ends orient toward the negatively charged $\\text{Br}^-$ anion."
    },
    {
        "unit_q_num": 31,
        "topic_code": "3.8",
        "topic_title": "Representations of Solutions",
        "difficulty": "Challenging",
        "stimulus": (
            '$$\\text{Pb(NO}_3)_2(aq) + 2\\,\\text{NaI}(aq) \\rightarrow \\text{PbI}_2(s) + 2\\,\\text{NaNO}_3(aq)$$'
        ),
        "question": "A student mixes $50.0\\text{ mL}$ of $0.10\\text{ M } \\text{Pb(NO}_3)_2(aq)$ with $50.0\\text{ mL}$ of $0.10\\text{ M } \\text{NaI}(aq)$, resulting in the precipitation of yellow $\\text{PbI}_2(s)$. If a particulate diagram of the solution above the solid precipitate is drawn after the reaction goes to completion (omitting water molecules), what should be the relative numbers of ions shown in the solution phase?",
        "options": [
            "$2\\text{ Na}^+$ ions and $2\\text{ NO}_3^-$ ions only",
            "$1\\text{ Pb}^{2+}$ ion, $2\\text{ Na}^+$ ions, and $4\\text{ NO}_3^-$ ions",
            "$2\\text{ Pb}^{2+}$ ions, $2\\text{ I}^-$ ions, $2\\text{ Na}^+$ ions, and $2\\text{ NO}_3^-$ ions",
            "$2\\text{ Na}^+$ ions, $1\\text{ I}^-$ ion, and $1\\text{ NO}_3^-$ ion"
        ],
        "correct_index": 1,
        "explanation": "Initially, equal volumes and concentrations mean we start with equal moles of $\\text{Pb(NO}_3)_2$ and $\\text{NaI}$. Let's represent $0.0050\\text{ mol}$ as $2$ formula units of $\\text{Pb(NO}_3)_2$ ($2\\text{ Pb}^{2+} + 4\\text{ NO}_3^-$) and $2$ formula units of $\\text{NaI}$ ($2\\text{ Na}^+ + 2\\text{ I}^-$). Because the reaction requires $2\\text{ I}^-$ per $1\\text{ Pb}^{2+}$, $\\text{I}^-$ is the limiting reactant: $1\\text{ Pb}^{2+}$ and $2\\text{ I}^-$ precipitate as $\\text{PbI}_2(s)$, leaving $1\\text{ Pb}^{2+}$ (excess), $2\\text{ Na}^+$ (spectator), and $4\\text{ NO}_3^-$ (spectator) in solution. Notice that total charge is balanced: $1(+2) + 2(+1) + 4(-1) = 0$."
    },
    {
        "unit_q_num": 32,
        "topic_code": "3.8",
        "topic_title": "Representations of Solutions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "A particulate representation shows two aqueous solutions of $\\text{CuSO}_4$ in identical beakers. Beaker 1 shows $8\\text{ Cu}^{2+}$ ions and $8\\text{ SO}_4^{2-}$ ions in a liquid volume of $V$. Beaker 2 shows $4\\text{ Cu}^{2+}$ ions and $4\\text{ SO}_4^{2-}$ ions in a liquid volume of $2V$. How does the molarity of $\\text{CuSO}_4$ in Beaker 1 compare to that in Beaker 2?",
        "options": [
            "The molarity in Beaker 1 is equal to the molarity in Beaker 2.",
            "The molarity in Beaker 1 is $2$ times the molarity in Beaker 2.",
            "The molarity in Beaker 1 is $4$ times the molarity in Beaker 2.",
            "The molarity in Beaker 1 is $0.5$ times the molarity in Beaker 2."
        ],
        "correct_index": 2,
        "explanation": "Molarity is proportional to the number of solute particles divided by the solution volume ($N/V$). In Beaker 1, the concentration is proportional to $8 / V$. In Beaker 2, the concentration is proportional to $4 / (2V) = 2 / V$. The ratio of the concentration in Beaker 1 to Beaker 2 is $(8/V) / (2/V) = 4$."
    },
    {
        "unit_q_num": 33,
        "topic_code": "3.8",
        "topic_title": "Representations of Solutions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "When methanol ($\\text{CH}_3\\text{OH}$) dissolves in water, which of the following accurately describes the particulate-level interactions shown in a valid representation of the solution?",
        "options": [
            "$\\text{CH}_3\\text{OH}$ dissociates completely into $\\text{CH}_3^+(aq)$ and $\\text{OH}^-(aq)$ ions surrounded by hydration shells.",
            "Intact $\\text{CH}_3\\text{OH}$ molecules form intermolecular hydrogen bonds with $\\text{H}_2\\text{O}$ molecules between the hydroxyl ($-\\text{OH}$) oxygen and hydrogen atoms of both species.",
            "Hydrogen atoms bonded to carbon in the $-\\text{CH}_3$ group form strong hydrogen bonds with the oxygen atoms of $\\text{H}_2\\text{O}$.",
            "$\\text{CH}_3\\text{OH}$ molecules aggregate into a separate nonpolar layer above the water."
        ],
        "correct_index": 1,
        "explanation": "Methanol ($\\text{CH}_3\\text{OH}$) is a polar molecular compound (nonelectrolyte), so it does not dissociate into ions in water. Instead, intact $\\text{CH}_3\\text{OH}$ molecules mix miscibly with water by forming hydrogen bonds between the $-\\text{OH}$ group of methanol and $\\text{H}_2\\text{O}$ molecules. Remember on the AP exam that $\\text{C}-\\text{H}$ hydrogens never participate in hydrogen bonding."
    },

    # -------------------------------------------------------------------------
    # Topic 3.9: Separation of Solutions and Mixtures (Q34 - Q37)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 34,
        "topic_code": "3.9",
        "topic_title": "Separation of Solutions and Mixtures",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r'<table class="quiz-data-table">'
            r'<thead><tr><th>Dye Component</th><th>Distance Traveled by Spot ($\text{cm}$)</th><th>Distance Traveled by Solvent Front ($\text{cm}$)</th><th>Retention Factor ($R_f$)</th></tr></thead>'
            r'<tbody>'
            r'<tr><td>Dye X</td><td>$1.8$</td><td>$9.0$</td><td>$0.20$</td></tr>'
            r'<tr><td>Dye Y</td><td>$4.5$</td><td>$9.0$</td><td>$0.50$</td></tr>'
            r'<tr><td>Dye Z</td><td>$7.2$</td><td>$9.0$</td><td>$0.80$</td></tr>'
            r'</tbody></table>'
        ),
        "question": r"A mixture of three organic dyes (X, Y, and Z) is separated by thin-layer chromatography (TLC) using a highly polar silica gel ($\text{SiO}_2$) stationary phase and a nonpolar hexane ($\text{C}_6\text{H}_{14}$) mobile phase. Based on the results in the table above, which of the following correctly ranks the dyes from LEAST polar to MOST polar?",
        "options": [
            r"$\text{Dye X} < \text{Dye Y} < \text{Dye Z}$",
            r"$\text{Dye Z} < \text{Dye X} < \text{Dye Y}$",
            r"$\text{Dye Y} < \text{Dye X} < \text{Dye Z}$",
            r"$\text{Dye Z} < \text{Dye Y} < \text{Dye X}$",
        ],
        "correct_index": 3,
        "explanation": r"In chromatography, components separate based on their relative affinities for the stationary phase versus the mobile phase. Here, the stationary phase (silica gel) is polar and the mobile phase (hexane) is nonpolar. Dye Z traveled the farthest ($R_f = 0.80$), meaning it interacted weakest with the polar stationary phase and strongest with the nonpolar mobile phase (least polar). Dye X traveled the shortest distance ($R_f = 0.20$), meaning it was strongly retained by dipole-dipole/H-bonding interactions with the polar silica gel (most polar). Thus, polarity increases in the order $\text{Dye Z} < \text{Dye Y} < \text{Dye X}$; ranking the dyes in order of increasing $R_f$ reverses the correct order.",
    },
    {
        "unit_q_num": 35,
        "topic_code": "3.9",
        "topic_title": "Separation of Solutions and Mixtures",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            '<thead><tr><th>Liquid Component</th><th>Molar Mass ($\\text{g/mol}$)</th><th>Normal Boiling Point ($^\\circ\\text{C}$)</th></tr></thead>'
            '<tbody>'
            '<tr><td>Acetone</td><td>$58.08$</td><td>$56.0$</td></tr>'
            '<tr><td>1-Propanol</td><td>$60.10$</td><td>$97.2$</td></tr>'
            '<tr><td>Ethylene glycol</td><td>$62.07$</td><td>$197.3$</td></tr>'
            '</tbody></table>'
        ),
        "question": "An equimolar liquid mixture of acetone, 1-propanol, and ethylene glycol is heated slowly in a fractional distillation apparatus at $1.0\\text{ atm}$. Which liquid is collected first as the distillate in the receiving flask, and why?",
        "options": [
            "Ethylene glycol, because it has the strongest intermolecular hydrogen bonding and highest boiling point.",
            "Acetone, because it has the weakest intermolecular forces (dipole-dipole and LDFs, no H-bonding between acetone molecules), highest vapor pressure at any given temperature, and lowest boiling point.",
            "1-Propanol, because its boiling point is closest to that of water ($100^\\circ\\text{C}$).",
            "All three liquids distill simultaneously because their molar masses are nearly identical ($58-62\\text{ g/mol}$)."
        ],
        "correct_index": 1,
        "explanation": "Fractional distillation separates miscible liquids based on differences in volatility (vapor pressure and boiling point), which are governed by intermolecular forces. Acetone lacks $-\\text{OH}$ bonds and cannot hydrogen-bond with itself, so it has the weakest IMFs, highest volatility, and lowest boiling point ($56.0^\\circ\\text{C}$). Therefore, acetone vaporizes first and is collected first in the distillate."
    },
    {
        "unit_q_num": 36,
        "topic_code": "3.9",
        "topic_title": "Separation of Solutions and Mixtures",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": "In a reversed-phase liquid chromatography column, the stationary phase consists of nonpolar hydrocarbon chains ($\\text{C}_{18}\\text{H}_{37}$) bonded to silica beads, and the mobile phase is a polar mixture of water and methanol. If a mixture containing benzoic acid ($\\text{C}_6\\text{H}_5\\text{COOH}$), naphthalene ($\\text{C}_{10}\\text{H}_8$), and sodium benzoate ($\\text{C}_6\\text{H}_5\\text{COO}^-\\text{Na}^+$) is injected into the column, which compound will elute LAST (have the longest retention time)?",
        "options": [
            "Sodium benzoate ($\\text{C}_6\\text{H}_5\\text{COO}^-\\text{Na}^+$)",
            "Benzoic acid ($\\text{C}_6\\text{H}_5\\text{COOH}$)",
            "Naphthalene ($\\text{C}_{10}\\text{H}_8$)",
            "All three compounds will elute at the same time."
        ],
        "correct_index": 2,
        "explanation": "In reversed-phase chromatography, the stationary phase is nonpolar ($\\text{C}_{18}$ chains) and the mobile phase is polar (water/methanol). The compound that elutes last (longest retention time) is the one that interacts most strongly with the nonpolar stationary phase. Naphthalene ($\\text{C}_{10}\\text{H}_8$) is completely nonpolar with a large polarizable aromatic surface area, so it experiences strong London dispersion forces with the nonpolar $\\text{C}_{18}$ stationary phase and is retained the longest. Ionic sodium benzoate interacts strongly with the polar mobile phase and elutes first."
    },
    {
        "unit_q_num": 37,
        "topic_code": "3.9",
        "topic_title": "Separation of Solutions and Mixtures",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "A student wants to separate a mixture of solid sand ($\\text{SiO}_2$), solid sodium chloride ($\\text{NaCl}$), and liquid water. Which sequence of laboratory operations will allow the student to recover both pure dry $\\text{SiO}_2(s)$ and pure solid $\\text{NaCl}(s)$?",
        "options": [
            "Pass the mixture through filter paper, wash and dry the residue on the filter paper to recover $\\text{SiO}_2(s)$, and then evaporate the water from the filtrate to recover $\\text{NaCl}(s)$.",
            "Perform paper chromatography on the mixture to separate $\\text{SiO}_2(s)$ from $\\text{NaCl}(s)$.",
            "Evaporate all the water from the original mixture and then use a magnet to separate $\\text{NaCl}(s)$ from $\\text{SiO}_2(s)$.",
            "Pass the mixture through filter paper to collect $\\text{NaCl}(s)$ on the filter paper, and distill the filtrate to collect $\\text{SiO}_2(s)$."
        ],
        "correct_index": 0,
        "explanation": "Because $\\text{SiO}_2$ is an insoluble covalent network solid and $\\text{NaCl}$ is a water-soluble ionic solid, gravity filtration separates the suspended $\\text{SiO}_2(s)$ (retained on the filter paper) from the aqueous $\\text{NaCl}(aq)$ solution (the filtrate). Evaporating the water from the filtrate leaves behind solid $\\text{NaCl}(s)$."
    },

    # -------------------------------------------------------------------------
    # Topic 3.10: Solubility (Q38 - Q40)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 38,
        "topic_code": "3.10",
        "topic_title": "Solubility",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            '<thead><tr><th>Alcohol</th><th>Formula</th><th>Solubility in Water at $20^\\circ\\text{C}$ ($\\text{mol}/100\\text{ g H}_2\\text{O}$)</th><th>Solubility in Hexane at $20^\\circ\\text{C}$ ($\\text{mol}/100\\text{ g C}_6\\text{H}_{14}$)</th></tr></thead>'
            '<tbody>'
            '<tr><td>Methanol</td><td>$\\text{CH}_3\\text{OH}$</td><td>$\\infty$ (miscible)</td><td>$0.12$</td></tr>'
            '<tr><td>1-Propanol</td><td>$\\text{CH}_3(\\text{CH}_2)_2\\text{OH}$</td><td>$\\infty$ (miscible)</td><td>$\\infty$ (miscible)</td></tr>'
            '<tr><td>1-Butanol</td><td>$\\text{CH}_3(\\text{CH}_2)_3\\text{OH}$</td><td>$0.11$</td><td>$\\infty$ (miscible)</td></tr>'
            '<tr><td>1-Hexanol</td><td>$\\text{CH}_3(\\text{CH}_2)_5\\text{OH}$</td><td>$0.0058$</td><td>$\\infty$ (miscible)</td></tr>'
            '</tbody></table>'
        ),
        "question": "Based on the data in the table above, which of the following best explains why the solubility of linear alcohols in water decreases drastically as the carbon chain length increases from methanol to 1-hexanol?",
        "options": [
            "The $-\\text{OH}$ group becomes less polar as more carbon atoms are added, preventing any hydrogen bonding with water.",
            "As the nonpolar hydrocarbon chain grows longer, the energy required to disrupt the extensive hydrogen-bonding network among water molecules to create a cavity for the large nonpolar tail is not compensated by new solute-solvent attractions.",
            "1-Hexanol forms an ionic lattice in the pure liquid that is too strong for water molecules to break apart.",
            "Longer alcohol molecules have higher kinetic energy than shorter alcohol molecules at $20^\\circ\\text{C}$."
        ],
        "correct_index": 1,
        "explanation": "While all four alcohols possess a hydrophilic $-\\text{OH}$ group capable of hydrogen bonding with water, increasing the length of the hydrophobic hydrocarbon chain ($-\\text{C}_n\\text{H}_{2n+1}$) means that dissolving the alcohol in water requires disrupting many strong water-water hydrogen bonds around the nonpolar chain, replacing them only with weaker dipole-induced dipole and London dispersion forces. Conversely, in nonpolar hexane, the longer hydrocarbon chains interact favorably via LDFs."
    },
    {
        "unit_q_num": 39,
        "topic_code": "3.10",
        "topic_title": "Solubility",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "Vitamin C (ascorbic acid, $\\text{C}_6\\text{H}_8\\text{O}_6$) is a small six-carbon molecule with four hydroxyl ($-\\text{OH}$) groups and a polar cyclic ester group, whereas Vitamin A (retinol, $\\text{C}_{20}\\text{H}_{30}\\text{O}$) is a twenty-carbon molecule that is almost entirely hydrocarbon, with only a single $-\\text{OH}$ group. Which statement correctly predicts and explains their relative solubilities in water versus body fat (nonpolar lipids)?",
        "options": [
            "Vitamin C is fat-soluble because it has more oxygen atoms to form London dispersion forces with lipids; Vitamin A is water-soluble.",
            "Vitamin C is water-soluble because its multiple $-\\text{OH}$ groups form extensive hydrogen bonds with water; Vitamin A is fat-soluble because its large nonpolar hydrocarbon region interacts predominantly via London dispersion forces with nonpolar lipid molecules.",
            "Both Vitamin A and Vitamin C are highly water-soluble because any molecule containing an $-\\text{OH}$ group is miscible with water.",
            "Vitamin A is water-soluble because its larger molar mass increases its ion-dipole interactions with water."
        ],
        "correct_index": 1,
        "explanation": "Substances with similar intermolecular forces tend to be soluble in one another. Vitamin C has a high ratio of polar $-\\text{OH}$ groups to carbons, allowing extensive intermolecular hydrogen bonding with water (water-soluble). Vitamin A is dominated by a bulky, nonpolar $\\text{C}_{20}$ hydrocarbon structure that interacts favorably with nonpolar fat/lipid molecules via London dispersion forces (fat-soluble)."
    },
    {
        "unit_q_num": 40,
        "topic_code": "3.10",
        "topic_title": "Solubility",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r'<table class="quiz-data-table">'
            r'<thead><tr><th>Gas</th><th>Molar Mass ($\text{g/mol}$)</th><th>Approximate Solubility in Water at $20^\circ\text{C}$ and $1\text{ atm}$ ($\text{g of gas per kg of H}_2\text{O}$)</th></tr></thead>'
            r'<tbody>'
            r'<tr><td>$\text{N}_2$</td><td>$28.0$</td><td>$0.02$</td></tr>'
            r'<tr><td>$\text{O}_2$</td><td>$32.0$</td><td>$0.04$</td></tr>'
            r'<tr><td>$\text{CH}_4$</td><td>$16.0$</td><td>$0.02$</td></tr>'
            r'<tr><td>$\text{NH}_3$</td><td>$17.0$</td><td>$500$</td></tr>'
            r'</tbody></table>'
        ),
        "question": r"The approximate solubilities of four gases in water are given in the table above. Which of the following best explains why $\text{NH}_3(g)$ is far more soluble in water than the other three gases?",
        "options": [
            r"$\text{NH}_3$ has the smallest molar mass of the four gases, so its molecules fit most easily into the spaces between water molecules.",
            r"$\text{NH}_3$ molecules have the most electrons of the four gases, so they have the strongest London dispersion forces with water molecules.",
            r"$\text{NH}_3$ molecules are polar and form hydrogen bonds with water molecules, interactions similar to those among water molecules themselves, whereas nonpolar $\text{N}_2$, $\text{O}_2$, and $\text{CH}_4$ interact with water only through much weaker dipole-induced dipole and dispersion forces.",
            r"$\text{NH}_3$ molecules form covalent $\text{N}-\text{O}$ bonds with water molecules, whereas the other three gases do not react with water.",
        ],
        "correct_index": 2,
        "explanation": r"Substances with similar intermolecular interactions tend to be soluble in one another. Liquid water is held together by hydrogen bonds; $\text{NH}_3$ is polar, with $\text{N}-\text{H}$ bonds and a lone pair on $\text{N}$, so it can both donate and accept hydrogen bonds with water, and dissolving it replaces water-water hydrogen bonds with comparably strong $\text{NH}_3$-water hydrogen bonds. $\text{N}_2$, $\text{O}_2$, and $\text{CH}_4$ are nonpolar and attract water only through weak dipole-induced dipole and London dispersion forces, which do not compensate for disrupting the hydrogen-bonded network of water, so they are only slightly soluble. $\text{CH}_4$ (not $\text{NH}_3$) has the smallest molar mass, $\text{NH}_3$ has only 10 electrons (fewer than $\text{N}_2$ or $\text{O}_2$), and no $\text{N}-\text{O}$ covalent bonds form when $\text{NH}_3$ dissolves.",
    },

    # -------------------------------------------------------------------------
    # Topic 3.11: Spectroscopy and the Electromagnetic Spectrum (Q41 - Q43)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 41,
        "topic_code": "3.11",
        "topic_title": "Spectroscopy and the Electromagnetic Spectrum",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            '<thead><tr><th>Region of Electromagnetic Spectrum</th><th>Typical Wavelength Range</th><th>Primary Molecular Process Excited</th></tr></thead>'
            '<tbody>'
            '<tr><td>Microwave</td><td>$1\\text{ mm} - 1\\text{ m}$</td><td>Process X</td></tr>'
            '<tr><td>Infrared (IR)</td><td>$700\\text{ nm} - 1\\text{ mm}$</td><td>Process Y</td></tr>'
            '<tr><td>Ultraviolet / Visible (UV-Vis)</td><td>$200\\text{ nm} - 700\\text{ nm}$</td><td>Process Z</td></tr>'
            '</tbody></table>'
        ),
        "question": "Based on the energy of photons in each region of the electromagnetic spectrum shown in the table above, which of the following correctly identifies Process X, Process Y, and Process Z?",
        "options": [
            "Process X: Molecular vibrations; Process Y: Molecular rotations; Process Z: Nuclear spin flips",
            "Process X: Valence electronic transitions; Process Y: Bond vibrations; Process Z: Molecular rotations",
            "Process X: Core electron ionization; Process Y: Valence electronic transitions; Process Z: Molecular rotations",
            "Process X: Molecular rotations; Process Y: Covalent bond vibrations (stretching and bending); Process Z: Valence electronic transitions"
        ],
        "correct_index": 3,
        "explanation": "On the AP Chemistry exam, the three key spectroscopic regions correspond to increasing photon energy ($E = h\\nu = hc/\\lambda$): (1) Microwave radiation (lowest energy, longest $\\lambda$) causes transitions between quantized rotational energy levels of polar molecules (Process X); (2) Infrared (IR) radiation (intermediate energy) causes transitions between quantized vibrational energy levels—bond stretching and bending (Process Y); (3) UV-Vis radiation (highest energy of the three, shortest $\\lambda$) causes transitions of valence electrons between electronic energy levels (Process Z)."
    },
    {
        "unit_q_num": 42,
        "topic_code": "3.11",
        "topic_title": "Spectroscopy and the Electromagnetic Spectrum",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"Carbon dioxide molecules in the atmosphere absorb infrared radiation emitted by Earth's surface, such as photons with a wavelength of $15\ \mu\text{m}$. Which of the following best describes what happens to a $\text{CO}_2$ molecule when it absorbs one of these infrared photons?",
        "options": [
            r"An electron in the molecule is promoted to a higher electronic energy level.",
            r"The molecule moves to a higher rotational energy level without any change in its vibrational energy level.",
            r"An electron is ejected from the molecule, forming a $\text{CO}_2^{\,+}$ ion.",
            r"The molecule moves to a higher vibrational energy level, so its bonds bend or stretch with more energy.",
        ],
        "correct_index": 3,
        "explanation": r"Infrared photons have energies that match the spacing between molecular vibrational energy levels, so absorbing infrared radiation increases a molecule's vibrational energy (here, the $\text{CO}_2$ molecule bends with more energy). The energy of the molecule increases by exactly the energy of the absorbed photon. Promoting an electron to a higher electronic energy level requires more energetic ultraviolet or visible photons, and ejecting an electron (ionization) requires even more energy. Transitions between rotational energy levels alone correspond to lower-energy microwave photons. The vibrationally excited $\text{CO}_2$ molecules then transfer energy to surrounding molecules through collisions, which warms the atmosphere.",
    },
    {
        "unit_q_num": 43,
        "topic_code": "3.11",
        "topic_title": "Spectroscopy and the Electromagnetic Spectrum",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"The absorption spectrum of carbon monoxide gas, $\text{CO}(g)$, contains a series of lines in the microwave region of the electromagnetic spectrum; the lowest-energy line occurs at a wavelength of $2.60\text{ mm}$. Which of the following occurs when a $\text{CO}$ molecule absorbs a photon with a wavelength of $2.60\text{ mm}$?",
        "options": [
            r"An electron in the molecule is promoted to a higher electronic energy level.",
            r"The molecule moves to a higher vibrational energy level, so the $\text{C}\equiv\text{O}$ bond stretches and compresses with more energy.",
            r"The $\text{C}\equiv\text{O}$ bond breaks, producing separate $\text{C}$ and $\text{O}$ atoms.",
            r"The molecule moves to a higher rotational energy level, so it rotates faster.",
        ],
        "correct_index": 3,
        "explanation": r"Photons with wavelengths of millimeters to centimeters are microwave photons, the lowest-energy photons among the microwave, infrared, and ultraviolet/visible regions. Their energies match the small spacing between molecular rotational energy levels, so absorbing a $2.60\text{ mm}$ photon raises the $\text{CO}$ molecule to a higher rotational energy level (it rotates faster). Vibrational transitions require more energetic infrared photons, and electronic transitions require ultraviolet or visible photons. Breaking the very strong $\text{C}\equiv\text{O}$ triple bond requires far more energy than a microwave photon carries.",
    },

    # -------------------------------------------------------------------------
    # Topic 3.12: Properties of Photons (Q44 - Q46)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 44,
        "topic_code": "3.12",
        "topic_title": "Properties of Photons",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '$$E = h\\nu \\qquad c = \\lambda\\nu$$\n'
            '$$h = 6.626 \\times 10^{-34}\\text{ J}\\cdot\\text{s} \\qquad c = 2.998 \\times 10^8\\text{ m/s}$$'
        ),
        "question": "A laser emits monochromatic green light with a wavelength of $\\lambda = 500.\\text{ nm}$ ($5.00 \\times 10^{-7}\\text{ m}$). What is the energy of a single photon of this light, and what is the energy of $1.00\\text{ mol}$ of these photons?",
        "options": [
            "$3.97 \\times 10^{-19}\\text{ J/photon}$ and $239\\text{ kJ/mol}$",
            "$1.33 \\times 10^{-27}\\text{ J/photon}$ and $0.800\\text{ J/mol}$",
            "$3.97 \\times 10^{-28}\\text{ J/photon}$ and $2.39 \\times 10^{-4}\\text{ kJ/mol}$",
            "$9.93 \\times 10^{-19}\\text{ J/photon}$ and $598\\text{ kJ/mol}$"
        ],
        "correct_index": 0,
        "explanation": "Using $E_{\\text{photon}} = \\frac{hc}{\\lambda}$: $E_{\\text{photon}} = \\frac{(6.626 \\times 10^{-34}\\text{ J}\\cdot\\text{s})(2.998 \\times 10^8\\text{ m/s})}{5.00 \\times 10^{-7}\\text{ m}} = 3.97 \\times 10^{-19}\\text{ J}$. Multiplying by Avogadro's number ($6.022 \\times 10^{23}\\text{ mol}^{-1}$) gives the energy per mole: $E_{\\text{mol}} = (3.97 \\times 10^{-19}\\text{ J})(6.022 \\times 10^{23}\\text{ mol}^{-1}) = 2.39 \\times 10^5\\text{ J/mol} = 239\\text{ kJ/mol}$."
    },
    {
        "unit_q_num": 45,
        "topic_code": "3.12",
        "topic_title": "Properties of Photons",
        "difficulty": "Challenging",
        "stimulus": (
            r'<table class="quiz-data-table">'
            r'<thead><tr><th>Energy Level of a Sodium Atom</th><th>Energy ($\text{J}$)</th></tr></thead>'
            r'<tbody>'
            r'<tr><td>$3p$ (excited state)</td><td>$-4.86 \times 10^{-19}$</td></tr>'
            r'<tr><td>$3s$ (ground state)</td><td>$-8.23 \times 10^{-19}$</td></tr>'
            r'</tbody></table>'
        ),
        "question": r"Sodium-vapor lamps emit yellow light when electrons in excited $\text{Na}$ atoms drop from the $3p$ energy level to the $3s$ energy level. Based on the energies in the table above, what is the wavelength of a photon emitted in this transition? ($h = 6.626 \times 10^{-34}\text{ J}\cdot\text{s}$, $c = 2.998 \times 10^{8}\text{ m/s}$)",
        "options": [
            r"$152\text{ nm}$",
            r"$241\text{ nm}$",
            r"$409\text{ nm}$",
            r"$589\text{ nm}$",
        ],
        "correct_index": 3,
        "explanation": r"The emitted photon carries away exactly the energy lost by the atom: $\Delta E = E_{3p} - E_{3s} = (-4.86 \times 10^{-19}\text{ J}) - (-8.23 \times 10^{-19}\text{ J}) = 3.37 \times 10^{-19}\text{ J}$. Then $\nu = \frac{E}{h} = \frac{3.37 \times 10^{-19}\text{ J}}{6.626 \times 10^{-34}\text{ J}\cdot\text{s}} = 5.09 \times 10^{14}\text{ s}^{-1}$ and $\lambda = \frac{c}{\nu} = \frac{2.998 \times 10^{8}\text{ m/s}}{5.09 \times 10^{14}\text{ s}^{-1}} = 5.89 \times 10^{-7}\text{ m} = 589\text{ nm}$ (yellow light). Using the energy of only the $3p$ level ($4.86 \times 10^{-19}\text{ J}$) gives $409\text{ nm}$, using only the $3s$ level gives $241\text{ nm}$, and adding the magnitudes of the two energies gives $152\text{ nm}$; the photon energy equals the difference between the two levels.",
    },
    {
        "unit_q_num": 46,
        "topic_code": "3.12",
        "topic_title": "Properties of Photons",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": "The minimum energy required to break the oxygen-oxygen bond in an $\\text{O}_2(g)$ molecule (the bond dissociation energy) is $498\\text{ kJ/mol}$. What is the longest wavelength of electromagnetic radiation ($\\lambda_{\\text{max}}$) capable of photodissociating a single $\\text{O}_2$ molecule? ($h = 6.626 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$, $c = 2.998 \\times 10^8\\text{ m/s}$, $N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}$)",
        "options": [
            "$498\\text{ nm}$",
            "$400.\\text{ nm}$",
            "$240.\\text{ nm}$",
            "$120.\\text{ nm}$"
        ],
        "correct_index": 2,
        "explanation": "First find the minimum energy needed per single $\\text{O}_2$ molecule (one photon): $E_{\\text{photon}} = \\frac{498 \\times 10^3\\text{ J/mol}}{6.022 \\times 10^{23}\\text{ mol}^{-1}} = 8.270 \\times 10^{-19}\\text{ J}$. Then solve for wavelength $\\lambda = \\frac{hc}{E_{\\text{photon}}} = \\frac{(6.626 \\times 10^{-34}\\text{ J}\\cdot\\text{s})(2.998 \\times 10^8\\text{ m/s})}{8.270 \\times 10^{-19}\\text{ J}} = 2.40 \\times 10^{-7}\\text{ m} = 240.\\text{ nm}$ (in the ultraviolet region)."
    },

    # -------------------------------------------------------------------------
    # Topic 3.13: Beer-Lambert Law (Q47 - Q50)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 47,
        "topic_code": "3.13",
        "topic_title": "Beer-Lambert Law",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '$$A = \\varepsilon b c$$\n'
            '<table class="quiz-data-table">'
            '<thead><tr><th>Standard Solution</th><th>$[\\text{Co(NO}_3)_2]$ ($\\text{M}$)</th><th>Absorbance ($A$) at $510\\text{ nm}$ ($b = 1.00\\text{ cm}$)</th></tr></thead>'
            '<tbody>'
            '<tr><td>1</td><td>$0.020$</td><td>$0.100$</td></tr>'
            '<tr><td>2</td><td>$0.040$</td><td>$0.200$</td></tr>'
            '<tr><td>3</td><td>$0.080$</td><td>$0.400$</td></tr>'
            '<tr><td>4</td><td>$0.120$</td><td>$0.600$</td></tr>'
            '<tr><td>Unknown</td><td>$?$</td><td>$0.350$</td></tr>'
            '</tbody></table>'
        ),
        "question": "A student constructs a Beer-Lambert Law calibration curve for $\\text{Co(NO}_3)_2(aq)$ at $510\\text{ nm}$ using a $1.00\\text{ cm}$ path-length cuvette, obtaining the data in the table above. What is the molar absorptivity $\\varepsilon$ of $\\text{Co}^{2+}(aq)$ at $510\\text{ nm}$, and what is the concentration of the unknown $\\text{Co(NO}_3)_2(aq)$ solution?",
        "options": [
            "$\\varepsilon = 5.0\\text{ M}^{-1}\\cdot\\text{cm}^{-1}$ and $c = 0.070\\text{ M}$",
            "$\\varepsilon = 0.20\\text{ M}^{-1}\\cdot\\text{cm}^{-1}$ and $c = 0.070\\text{ M}$",
            "$\\varepsilon = 5.0\\text{ M}^{-1}\\cdot\\text{cm}^{-1}$ and $c = 0.055\\text{ M}$",
            "$\\varepsilon = 1.75\\text{ M}^{-1}\\cdot\\text{cm}^{-1}$ and $c = 0.200\\text{ M}$"
        ],
        "correct_index": 0,
        "explanation": "From the Beer-Lambert Law $A = \\varepsilon b c$, the molar absorptivity is $\\varepsilon = \\frac{A}{bc} = \\frac{0.100}{(1.00\\text{ cm})(0.020\\text{ M})} = 5.0\\text{ M}^{-1}\\cdot\\text{cm}^{-1}$. Using this slope for the unknown solution with $A = 0.350$: $c = \\frac{A}{\\varepsilon b} = \\frac{0.350}{(5.0\\text{ M}^{-1}\\cdot\\text{cm}^{-1})(1.00\\text{ cm})} = 0.070\\text{ M}$."
    },
    {
        "unit_q_num": 48,
        "topic_code": "3.13",
        "topic_title": "Beer-Lambert Law",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": "A student uses a spectrophotometer and a pre-established Beer-Lambert calibration curve to determine the molarity of an unknown $\\text{CuSO}_4(aq)$ solution. In each of the following scenarios, how would the procedural error affect the student's calculated concentration of the unknown compared to its true concentration?\n\nI. Before filling the cuvette with the unknown $\\text{CuSO}_4(aq)$ solution, the student rinses the cuvette with distilled water and leaves several droplets of water inside.\nII. Before inserting the cuvette into the spectrophotometer, the student forgets to wipe off a smudge of fingerprints on the optical face of the cuvette.",
        "options": [
            "Error I causes the calculated concentration to be too low; Error II causes the calculated concentration to be too high.",
            "Error I causes the calculated concentration to be too high; Error II causes the calculated concentration to be too low.",
            "Both Error I and Error II cause the calculated concentration to be too high.",
            "Both Error I and Error II cause the calculated concentration to be too low."
        ],
        "correct_index": 0,
        "explanation": "This is a classic AP Chemistry error-analysis question. In Error I, residual droplets of distilled water inside the cuvette dilute the unknown $\\text{CuSO}_4(aq)$ sample, lowering its actual concentration in the cuvette, reducing the measured absorbance $A$, and yielding a calculated concentration that is too low. In Error II, fingerprints on the cuvette scatter and block incident light from reaching the detector; the spectrophotometer interprets less transmitted light ($I < I_{\\text{true}}$) as a higher absorbance ($A > A_{\\text{true}}$), yielding a calculated concentration that is too high."
    },
    {
        "unit_q_num": 49,
        "topic_code": "3.13",
        "topic_title": "Beer-Lambert Law",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r'<table class="quiz-data-table">'
            r'<thead><tr><th>Wavelength ($\text{nm}$)</th><th>Region of Spectrum</th><th>Absorbance of $0.050\text{ M } \text{CuSO}_4(aq)$</th><th>Absorbance of $0.050\text{ M } \text{ZnSO}_4(aq)$</th></tr></thead>'
            r'<tbody>'
            r'<tr><td>$430$</td><td>Violet</td><td>$0.01$</td><td>$0.00$</td></tr>'
            r'<tr><td>$520$</td><td>Green</td><td>$0.03$</td><td>$0.00$</td></tr>'
            r'<tr><td>$620$</td><td>Orange</td><td>$0.18$</td><td>$0.00$</td></tr>'
            r'<tr><td>$800$</td><td>Near infrared (just beyond red)</td><td>$0.60$</td><td>$0.00$</td></tr>'
            r'</tbody></table>'
        ),
        "question": r"A chemist wants to use spectrophotometry and the Beer-Lambert law to determine the concentration of $\text{Cu}^{2+}(aq)$ in a mixture that contains both $\text{CuSO}_4(aq)$ and $\text{ZnSO}_4(aq)$. Based on the absorption data in the table above, which wavelength should the chemist select for the analysis, and why?",
        "options": [
            r"$430\text{ nm}$, because blue solutions absorb blue light most strongly.",
            r"$800\text{ nm}$, because $\text{Cu}^{2+}(aq)$ has its maximum absorbance at this wavelength, providing the greatest sensitivity, while colorless $\text{Zn}^{2+}(aq)$ does not absorb and will not interfere.",
            r"$520\text{ nm}$, because an intermediate absorbance prevents detector saturation.",
            r"Spectrophotometry cannot be used unless $\text{Zn}^{2+}(aq)$ is first precipitated out of the solution.",
        ],
        "correct_index": 1,
        "explanation": r"A $\text{CuSO}_4$ solution looks blue because $\text{Cu}^{2+}(aq)$ transmits blue light and absorbs strongly toward the red end of the spectrum; in the table its absorbance is greatest at $800\text{ nm}$, its wavelength of maximum absorbance ($\lambda_{\text{max}}$). Setting the spectrophotometer to $\lambda_{\text{max}}$ gives the largest change in absorbance per unit change in concentration (the highest sensitivity and lowest percent error). Because colorless $\text{Zn}^{2+}(aq)$ has $A = 0.00$ at $800\text{ nm}$, it does not interfere and does not need to be removed. Blue solutions transmit, rather than absorb, blue light, and choosing a wavelength with a smaller absorbance, such as $520\text{ nm}$, would only lower the sensitivity; an absorbance of $0.60$ is well within the range that a spectrophotometer measures accurately.",
    },
    {
        "unit_q_num": 50,
        "topic_code": "3.13",
        "topic_title": "Beer-Lambert Law",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": "At $525\\text{ nm}$, a $2.00 \\times 10^{-4}\\text{ M}$ aqueous solution of potassium permanganate, $\\text{KMnO}_4(aq)$, has an absorbance of $A = 0.440$ when measured in a cuvette with a path length of $b = 1.00\\text{ cm}$. If the same solution is transferred to a wide cuvette with a path length of $b = 2.00\\text{ cm}$ and diluted with an equal volume of distilled water, what will be the new absorbance at $525\\text{ nm}$?",
        "options": [
            "$1.76$",
            "$0.880$",
            "$0.440$",
            "$0.220$"
        ],
        "correct_index": 2,
        "explanation": "According to the Beer-Lambert Law, $A = \\varepsilon b c$. Diluting the solution with an equal volume of water halves the concentration ($c_2 = 0.50\\,c_1$), while transferring it to a $2.00\\text{ cm}$ cuvette doubles the optical path length ($b_2 = 2.00\\,b_1$). Because molar absorptivity $\\varepsilon$ is constant at a given wavelength, the new absorbance is $A_2 = \\varepsilon (2.00\\,b_1)(0.50\\,c_1) = \\varepsilon b_1 c_1 = 0.440$."
    },
    # -------------------------------------------------------------------------
    # Added 2026-10-03 — Blind-spot coverage (Fall 2024 CED): topics 3.1–3.6
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 51,
        "topic_code": "3.1",
        "topic_title": "Intermolecular and Interparticle Forces",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r'<figure class="quiz-figure-wrap">'
            r'<svg class="quiz-figure" viewBox="0 0 520 250" role="img" aria-label="Four panels, each showing two HCl molecules drawn as a small H atom bonded to a larger Cl atom. Arrangement 1: the H atoms of the two molecules face each other. Arrangement 2: the molecules lie side by side pointing the same way, H next to H and Cl next to Cl. Arrangement 3: the Cl atom of one molecule faces the H atom of the other molecule. Arrangement 4: the Cl atoms of the two molecules face each other." font-family="sans-serif">'
            r'<rect x="0" y="0" width="520" height="250" fill="#ffffff"/>'
            r'<rect x="10" y="10" width="245" height="110" rx="6" fill="none" stroke="#9ca3af" stroke-width="1.5"/>'
            r'<text x="22" y="32" font-family="sans-serif" font-size="13" text-anchor="start" fill="#111827">Arrangement 1</text>'
            r'<line x1="89" y1="76" x2="55" y2="76" stroke="#111827" stroke-width="2.5"/>'
            r'<circle cx="89" cy="76" r="11" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="89" y="80.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">H</text>'
            r'<circle cx="55" cy="76" r="16" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="55" y="80.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">Cl</text>'
            r'<line x1="149" y1="76" x2="183" y2="76" stroke="#111827" stroke-width="2.5"/>'
            r'<circle cx="149" cy="76" r="11" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="149" y="80.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">H</text>'
            r'<circle cx="183" cy="76" r="16" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="183" y="80.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">Cl</text>'
            r'<line x1="100" y1="76" x2="138" y2="76" stroke="#2563eb" stroke-width="2" stroke-dasharray="3 4"/>'
            r'<rect x="265" y="10" width="245" height="110" rx="6" fill="none" stroke="#9ca3af" stroke-width="1.5"/>'
            r'<text x="277" y="32" font-family="sans-serif" font-size="13" text-anchor="start" fill="#111827">Arrangement 2</text>'
            r'<line x1="395" y1="53" x2="429" y2="53" stroke="#111827" stroke-width="2.5"/>'
            r'<circle cx="395" cy="53" r="11" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="395" y="57.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">H</text>'
            r'<circle cx="429" cy="53" r="16" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="429" y="57.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">Cl</text>'
            r'<line x1="395" y1="99" x2="429" y2="99" stroke="#111827" stroke-width="2.5"/>'
            r'<circle cx="395" cy="99" r="11" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="395" y="103.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">H</text>'
            r'<circle cx="429" cy="99" r="16" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="429" y="103.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">Cl</text>'
            r'<line x1="395" y1="64" x2="395" y2="88" stroke="#2563eb" stroke-width="2" stroke-dasharray="3 4"/>'
            r'<line x1="429" y1="69" x2="429" y2="83" stroke="#2563eb" stroke-width="2" stroke-dasharray="3 4"/>'
            r'<rect x="10" y="130" width="245" height="110" rx="6" fill="none" stroke="#9ca3af" stroke-width="1.5"/>'
            r'<text x="22" y="152" font-family="sans-serif" font-size="13" text-anchor="start" fill="#111827">Arrangement 3</text>'
            r'<line x1="55" y1="196" x2="89" y2="196" stroke="#111827" stroke-width="2.5"/>'
            r'<circle cx="55" cy="196" r="11" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="55" y="200.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">H</text>'
            r'<circle cx="89" cy="196" r="16" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="89" y="200.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">Cl</text>'
            r'<line x1="149" y1="196" x2="183" y2="196" stroke="#111827" stroke-width="2.5"/>'
            r'<circle cx="149" cy="196" r="11" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="149" y="200.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">H</text>'
            r'<circle cx="183" cy="196" r="16" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="183" y="200.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">Cl</text>'
            r'<line x1="105" y1="196" x2="138" y2="196" stroke="#2563eb" stroke-width="2" stroke-dasharray="3 4"/>'
            r'<rect x="265" y="130" width="245" height="110" rx="6" fill="none" stroke="#9ca3af" stroke-width="1.5"/>'
            r'<text x="277" y="152" font-family="sans-serif" font-size="13" text-anchor="start" fill="#111827">Arrangement 4</text>'
            r'<line x1="310" y1="196" x2="344" y2="196" stroke="#111827" stroke-width="2.5"/>'
            r'<circle cx="310" cy="196" r="11" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="310" y="200.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">H</text>'
            r'<circle cx="344" cy="196" r="16" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="344" y="200.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">Cl</text>'
            r'<line x1="438" y1="196" x2="404" y2="196" stroke="#111827" stroke-width="2.5"/>'
            r'<circle cx="438" cy="196" r="11" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="438" y="200.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">H</text>'
            r'<circle cx="404" cy="196" r="16" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="404" y="200.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">Cl</text>'
            r'<line x1="360" y1="196" x2="388" y2="196" stroke="#2563eb" stroke-width="2" stroke-dasharray="3 4"/>'
            r'</svg>'
            r'<figcaption>Figure: Four possible orientations of a pair of HCl molecules (dotted lines join the atoms that are closest to each other)</figcaption>'
            r'</figure>'
        ),
        "question": r"The diagrams above show four possible orientations of a pair of hydrogen chloride molecules, $\text{HCl}$. Which arrangement results in the strongest attractive dipole-dipole interaction between the two molecules, and why?",
        "options": [
            r"Arrangement 1, because the two H atoms can form a hydrogen bond with each other.",
            r"Arrangement 2, because the two dipoles are side by side and point in the same direction, so they reinforce each other.",
            r"Arrangement 3, because the partially negative Cl end of one molecule is next to the partially positive H end of the other molecule.",
            r"Arrangement 4, because the two Cl atoms, which have the most electrons, are next to each other, which maximizes London dispersion forces.",
        ],
        "correct_index": 2,
        "explanation": r"Cl is more electronegative than H, so in each $\text{HCl}$ molecule the Cl end carries a partial negative charge ($\delta^-$) and the H end a partial positive charge ($\delta^+$). The strength and sign of a dipole-dipole interaction depend on how these partial charges are oriented relative to each other. The attraction is strongest when opposite partial charges are closest, as in the head-to-tail orientation of Arrangement 3, where the $\delta^-$ Cl end of one molecule faces the $\delta^+$ H end of the other. When H faces H, Cl faces Cl, or the two dipoles lie side by side pointing the same way, like partial charges are closest, so the dipole-dipole interaction is repulsive rather than attractive. A hydrogen bond requires H bonded to N, O, or F, so $\text{HCl}$ molecules cannot form one. London dispersion forces are present in every arrangement and are not dipole-dipole interactions, so they do not make the Cl-facing-Cl orientation the strongest dipole-dipole attraction.",
    },
    {
        "unit_q_num": 52,
        "topic_code": "3.1",
        "topic_title": "Intermolecular and Interparticle Forces",
        "difficulty": "Challenging",
        "stimulus": (
            r'<table class="quiz-data-table">'
            r'<thead><tr><th>Gas</th><th>Number of Electrons per Atom</th><th>Approximate Solubility in Water at $25^\circ\text{C}$ ($\text{mmol/L}$, gas at $1\text{ atm}$)</th></tr></thead>'
            r'<tbody>'
            r'<tr><td>$\text{He}$</td><td>$2$</td><td>$0.38$</td></tr>'
            r'<tr><td>$\text{Ne}$</td><td>$10$</td><td>$0.45$</td></tr>'
            r'<tr><td>$\text{Ar}$</td><td>$18$</td><td>$1.4$</td></tr>'
            r'<tr><td>$\text{Kr}$</td><td>$36$</td><td>$2.5$</td></tr>'
            r'<tr><td>$\text{Xe}$</td><td>$54$</td><td>$4.3$</td></tr>'
            r'</tbody></table>'
        ),
        "question": r"The approximate solubilities of the noble gases in water are given in the table above. Which of the following best explains the trend in solubility from $\text{He}$ to $\text{Xe}$?",
        "options": [
            r"Larger noble-gas atoms have larger, more polarizable electron clouds, so the dipoles of nearby water molecules induce larger temporary dipoles in them, which produces stronger dipole-induced dipole attractions between the atoms and water molecules.",
            r"Larger noble-gas atoms form stronger hydrogen bonds with water molecules, because their larger electron clouds attract the hydrogen atoms of water more strongly.",
            r"Larger noble-gas atoms have larger permanent dipoles, so they form stronger dipole-dipole attractions with water molecules.",
            r"Larger noble-gas atoms have lower first ionization energies, so they partially ionize in water and form ion-dipole attractions with water molecules.",
        ],
        "correct_index": 0,
        "explanation": r"Water molecules are polar and noble-gas atoms are nonpolar, so the main solute-solvent attraction is a dipole-induced dipole interaction (along with London dispersion forces). The strength of a dipole-induced dipole attraction increases with the polarizability of the nonpolar particle, and polarizability increases with the number of electrons and the size of the electron cloud. From $\text{He}$ ($2$ electrons) to $\text{Xe}$ ($54$ electrons), the dipole of a neighboring water molecule induces an increasingly large dipole in the atom, so the atoms are attracted more strongly to water and the solubility increases about elevenfold ($4.3 \div 0.38 \approx 11$). A hydrogen bond requires an H atom bonded to N, O, or F to be attracted to an N, O, or F atom, so noble gases cannot hydrogen bond with water. An isolated atom has no permanent dipole, so dipole-dipole forces are impossible. Noble-gas ionization energies remain far too high for the atoms to ionize in water, so no ion-dipole forces form.",
    },
    {
        "unit_q_num": 53,
        "topic_code": "3.1",
        "topic_title": "Intermolecular and Interparticle Forces",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r'<figure class="quiz-figure-wrap">'
            r'<svg class="quiz-figure" viewBox="0 0 520 290" role="img" aria-label="A protein chain drawn as a U-shaped line folded back on itself, with three pairs of side chains pointing toward each other across the fold. Site 1: a CH2-COO minus group on the upper strand faces a (CH2)4-NH3 plus group on the lower strand. Site 2: a CH2-OH group faces another CH2-OH group. Site 3: a CH(CH3)2 group faces a CH2-CH(CH3)2 group. Dotted lines connect the facing groups." font-family="sans-serif">'
            r'<rect x="0" y="0" width="520" height="290" fill="#ffffff"/>'
            r'<path d="M 30 60 L 420 60 A 90 90 0 0 1 420 240 L 30 240" fill="none" stroke="#374151" stroke-width="2.5"/>'
            r'<line x1="12" y1="60" x2="30" y2="60" stroke="#374151" stroke-width="2.5" stroke-dasharray="4 4"/>'
            r'<line x1="12" y1="240" x2="30" y2="240" stroke="#374151" stroke-width="2.5" stroke-dasharray="4 4"/>'
            r'<text x="30" y="46" font-family="sans-serif" font-size="13" text-anchor="start" fill="#111827">Protein chain</text>'
            r'<line x1="100" y1="60" x2="100" y2="79" stroke="#374151" stroke-width="2"/>'
            r'<text x="100" y="91" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">CH₂</text>'
            r'<line x1="100" y1="97" x2="100" y2="109" stroke="#374151" stroke-width="2"/>'
            r'<text x="100" y="121" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">COO<tspan dy="-6" font-size="12">−</tspan></text>'
            r'<line x1="100" y1="240" x2="100" y2="224" stroke="#374151" stroke-width="2"/>'
            r'<text x="100" y="219" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">(CH₂)₄</text>'
            r'<line x1="100" y1="206" x2="100" y2="193" stroke="#374151" stroke-width="2"/>'
            r'<text x="100" y="188" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">NH₃<tspan dy="-6" font-size="12">+</tspan></text>'
            r'<line x1="100" y1="129" x2="100" y2="175" stroke="#2563eb" stroke-width="2" stroke-dasharray="3 4"/>'
            r'<text x="110" y="156" font-family="sans-serif" font-size="13" text-anchor="start" fill="#111827">Site 1</text>'
            r'<line x1="220" y1="60" x2="220" y2="79" stroke="#374151" stroke-width="2"/>'
            r'<text x="220" y="91" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">CH₂</text>'
            r'<line x1="220" y1="97" x2="220" y2="109" stroke="#374151" stroke-width="2"/>'
            r'<text x="220" y="121" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">OH</text>'
            r'<line x1="220" y1="240" x2="220" y2="224" stroke="#374151" stroke-width="2"/>'
            r'<text x="220" y="219" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">CH₂</text>'
            r'<line x1="220" y1="206" x2="220" y2="193" stroke="#374151" stroke-width="2"/>'
            r'<text x="220" y="188" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">OH</text>'
            r'<line x1="220" y1="129" x2="220" y2="175" stroke="#2563eb" stroke-width="2" stroke-dasharray="3 4"/>'
            r'<text x="230" y="156" font-family="sans-serif" font-size="13" text-anchor="start" fill="#111827">Site 2</text>'
            r'<line x1="340" y1="60" x2="340" y2="109" stroke="#374151" stroke-width="2"/>'
            r'<text x="340" y="121" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">CH(CH₃)₂</text>'
            r'<line x1="340" y1="240" x2="340" y2="224" stroke="#374151" stroke-width="2"/>'
            r'<text x="340" y="219" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">CH₂</text>'
            r'<line x1="340" y1="206" x2="340" y2="193" stroke="#374151" stroke-width="2"/>'
            r'<text x="340" y="188" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">CH(CH₃)₂</text>'
            r'<line x1="340" y1="129" x2="340" y2="175" stroke="#2563eb" stroke-width="2" stroke-dasharray="3 4"/>'
            r'<text x="350" y="156" font-family="sans-serif" font-size="13" text-anchor="start" fill="#111827">Site 3</text>'
            r'</svg>'
            r'<figcaption>Figure: Part of a folded protein chain (dotted lines join side chains that are close to each other)</figcaption>'
            r'</figure>'
        ),
        "question": r"The diagram above represents part of a protein chain that has folded back on itself, bringing the side chains at Sites 1, 2, and 3 close together. Which of the following identifies the strongest type of noncovalent interaction between the two side chains at each site?",
        "options": [
            r"Site 1: hydrogen bonding; Site 2: hydrogen bonding; Site 3: dipole-dipole attractions",
            r"Site 1: ion-ion (Coulombic) attraction; Site 2: dipole-induced dipole attractions; Site 3: London dispersion forces",
            r"Site 1: ion-ion (Coulombic) attraction; Site 2: hydrogen bonding; Site 3: hydrogen bonding",
            r"Site 1: ion-ion (Coulombic) attraction; Site 2: hydrogen bonding; Site 3: London dispersion forces",
        ],
        "correct_index": 3,
        "explanation": r"In a large biomolecule, noncovalent interactions can occur between different regions of the same molecule, and these interactions help hold its folded shape. At Site 1, the $-\text{COO}^-$ group carries a full negative charge and the $-\text{NH}_3^+$ group a full positive charge, so the strongest interaction is the Coulombic attraction between oppositely charged ions, which is stronger than a hydrogen bond between neutral groups. At Site 2, each side chain has an O–H group, so the H atom bonded to O on one side chain is attracted to a lone pair on the O atom of the other: a hydrogen bond. This is stronger than a dipole-induced dipole attraction, which occurs between a polar group and a nonpolar group. At Site 3, both side chains contain only C and H atoms; they are essentially nonpolar and have no H bonded to N, O, or F, so they attract each other only through London dispersion forces, not through hydrogen bonds or dipole-dipole attractions.",
    },
    {
        "unit_q_num": 54,
        "topic_code": "3.2",
        "topic_title": "Properties of Solids",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r'<figure class="quiz-figure-wrap">'
            r'<svg class="quiz-figure" viewBox="0 0 540 290" role="img" aria-label="Four panels. Top left, ionic solid before: two rows of alternating positive and negative ions, with each positive ion directly above a negative ion. Top right, ionic solid after the top row has shifted one position to the right: each positive ion is now above a positive ion and each negative ion is above a negative ion. Bottom left, metal before: two rows of positive metal ions surrounded by many small dots that represent mobile electrons. Bottom right, metal after the top row has shifted one position: the positive ions are still surrounded by the mobile electrons." font-family="sans-serif">'
            r'<rect x="0" y="0" width="540" height="290" fill="#ffffff"/>'
            r'<rect x="10" y="10" width="255" height="130" rx="6" fill="none" stroke="#9ca3af" stroke-width="1.5"/>'
            r'<text x="20" y="31" font-family="sans-serif" font-size="13" text-anchor="start" fill="#111827">Ionic solid, before</text>'
            r'<circle cx="50" cy="72" r="10" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="50" y="76.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="82" cy="72" r="15" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="82" y="77" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">−</text>'
            r'<circle cx="114" cy="72" r="10" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="114" y="76.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="146" cy="72" r="15" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="146" y="77" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">−</text>'
            r'<circle cx="178" cy="72" r="10" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="178" y="76.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="210" cy="72" r="15" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="210" y="77" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">−</text>'
            r'<circle cx="50" cy="106" r="15" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="50" y="111" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">−</text>'
            r'<circle cx="82" cy="106" r="10" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="82" y="110.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="114" cy="106" r="15" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="114" y="111" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">−</text>'
            r'<circle cx="146" cy="106" r="10" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="146" y="110.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="178" cy="106" r="15" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="178" y="111" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">−</text>'
            r'<circle cx="210" cy="106" r="10" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="210" y="110.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<rect x="275" y="10" width="255" height="130" rx="6" fill="none" stroke="#9ca3af" stroke-width="1.5"/>'
            r'<text x="285" y="31" font-family="sans-serif" font-size="13" text-anchor="start" fill="#111827">Ionic solid, after shift</text>'
            r'<circle cx="347" cy="72" r="10" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="347" y="76.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="379" cy="72" r="15" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="379" y="77" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">−</text>'
            r'<circle cx="411" cy="72" r="10" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="411" y="76.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="443" cy="72" r="15" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="443" y="77" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">−</text>'
            r'<circle cx="475" cy="72" r="10" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="475" y="76.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="507" cy="72" r="15" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="507" y="77" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">−</text>'
            r'<circle cx="315" cy="106" r="15" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="315" y="111" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">−</text>'
            r'<circle cx="347" cy="106" r="10" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="347" y="110.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="379" cy="106" r="15" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="379" y="111" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">−</text>'
            r'<circle cx="411" cy="106" r="10" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="411" y="110.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="443" cy="106" r="15" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="443" y="111" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111827">−</text>'
            r'<circle cx="475" cy="106" r="10" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="475" y="110.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<line x1="289" y1="72" x2="319" y2="72" stroke="#374151" stroke-width="2"/>'
            r'<polygon points="327,72 317,67 317,77" fill="#374151"/>'
            r'<rect x="10" y="150" width="255" height="130" rx="6" fill="none" stroke="#9ca3af" stroke-width="1.5"/>'
            r'<text x="20" y="171" font-family="sans-serif" font-size="13" text-anchor="start" fill="#111827">Metal, before</text>'
            r'<circle cx="35.3" cy="187.1" r="2.5" fill="#111827"/>'
            r'<circle cx="32.4" cy="203.9" r="2.5" fill="#111827"/>'
            r'<circle cx="31.6" cy="232.6" r="2.5" fill="#111827"/>'
            r'<circle cx="31.1" cy="249.3" r="2.5" fill="#111827"/>'
            r'<circle cx="35" cy="261.8" r="2.5" fill="#111827"/>'
            r'<circle cx="48.4" cy="190.8" r="2.5" fill="#111827"/>'
            r'<circle cx="47" cy="270.1" r="2.5" fill="#111827"/>'
            r'<circle cx="62.1" cy="187.8" r="2.5" fill="#111827"/>'
            r'<circle cx="64.6" cy="263.9" r="2.5" fill="#111827"/>'
            r'<circle cx="76.1" cy="189.9" r="2.5" fill="#111827"/>'
            r'<circle cx="78.4" cy="272.8" r="2.5" fill="#111827"/>'
            r'<circle cx="114.3" cy="193.4" r="2.5" fill="#111827"/>'
            r'<circle cx="130.7" cy="190.8" r="2.5" fill="#111827"/>'
            r'<circle cx="130.2" cy="232.5" r="2.5" fill="#111827"/>'
            r'<circle cx="129.6" cy="256.8" r="2.5" fill="#111827"/>'
            r'<circle cx="131.7" cy="270.8" r="2.5" fill="#111827"/>'
            r'<circle cx="161" cy="201.5" r="2.5" fill="#111827"/>'
            r'<circle cx="158.7" cy="230.7" r="2.5" fill="#111827"/>'
            r'<circle cx="160" cy="260" r="2.5" fill="#111827"/>'
            r'<circle cx="157.3" cy="270.9" r="2.5" fill="#111827"/>'
            r'<circle cx="175.6" cy="193.4" r="2.5" fill="#111827"/>'
            r'<circle cx="189.4" cy="192" r="2.5" fill="#111827"/>'
            r'<circle cx="194" cy="222" r="2.5" fill="#111827"/>'
            r'<circle cx="195.9" cy="234.4" r="2.5" fill="#111827"/>'
            r'<circle cx="193.8" cy="258.2" r="2.5" fill="#111827"/>'
            r'<circle cx="192.4" cy="272.6" r="2.5" fill="#111827"/>'
            r'<circle cx="209.5" cy="192.1" r="2.5" fill="#111827"/>'
            r'<circle cx="223" cy="192.7" r="2.5" fill="#111827"/>'
            r'<circle cx="222.2" cy="231.1" r="2.5" fill="#111827"/>'
            r'<circle cx="226.6" cy="272.8" r="2.5" fill="#111827"/>'
            r'<circle cx="241.7" cy="202.8" r="2.5" fill="#111827"/>'
            r'<circle cx="238.5" cy="216.9" r="2.5" fill="#111827"/>'
            r'<circle cx="238.1" cy="230.9" r="2.5" fill="#111827"/>'
            r'<circle cx="238.6" cy="244.4" r="2.5" fill="#111827"/>'
            r'<circle cx="242.3" cy="263.6" r="2.5" fill="#111827"/>'
            r'<circle cx="240.2" cy="271.3" r="2.5" fill="#111827"/>'
            r'<circle cx="253.3" cy="188.7" r="2.5" fill="#111827"/>'
            r'<circle cx="252.8" cy="214.8" r="2.5" fill="#111827"/>'
            r'<circle cx="255.9" cy="247.4" r="2.5" fill="#111827"/>'
            r'<circle cx="50" cy="212" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="50" y="216.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="82" cy="212" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="82" y="216.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="114" cy="212" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="114" y="216.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="146" cy="212" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="146" y="216.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="178" cy="212" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="178" y="216.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="210" cy="212" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="210" y="216.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="50" cy="246" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="50" y="250.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="82" cy="246" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="82" y="250.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="114" cy="246" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="114" y="250.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="146" cy="246" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="146" y="250.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="178" cy="246" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="178" y="250.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="210" cy="246" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="210" y="250.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<rect x="275" y="150" width="255" height="130" rx="6" fill="none" stroke="#9ca3af" stroke-width="1.5"/>'
            r'<text x="285" y="171" font-family="sans-serif" font-size="13" text-anchor="start" fill="#111827">Metal, after shift</text>'
            r'<circle cx="297.5" cy="233" r="2.5" fill="#111827"/>'
            r'<circle cx="294.7" cy="257.9" r="2.5" fill="#111827"/>'
            r'<circle cx="315.4" cy="193.7" r="2.5" fill="#111827"/>'
            r'<circle cx="311.3" cy="271.8" r="2.5" fill="#111827"/>'
            r'<circle cx="330.9" cy="192.8" r="2.5" fill="#111827"/>'
            r'<circle cx="329.8" cy="235.6" r="2.5" fill="#111827"/>'
            r'<circle cx="329.1" cy="259.4" r="2.5" fill="#111827"/>'
            r'<circle cx="342.4" cy="187.3" r="2.5" fill="#111827"/>'
            r'<circle cx="343.5" cy="271" r="2.5" fill="#111827"/>'
            r'<circle cx="364.3" cy="192.9" r="2.5" fill="#111827"/>'
            r'<circle cx="364.5" cy="263.6" r="2.5" fill="#111827"/>'
            r'<circle cx="363.7" cy="270.8" r="2.5" fill="#111827"/>'
            r'<circle cx="378.5" cy="189.5" r="2.5" fill="#111827"/>'
            r'<circle cx="389.4" cy="230.3" r="2.5" fill="#111827"/>'
            r'<circle cx="395.7" cy="272.9" r="2.5" fill="#111827"/>'
            r'<circle cx="411.7" cy="190.2" r="2.5" fill="#111827"/>'
            r'<circle cx="406.6" cy="270.4" r="2.5" fill="#111827"/>'
            r'<circle cx="422.9" cy="191.1" r="2.5" fill="#111827"/>'
            r'<circle cx="426.3" cy="233.7" r="2.5" fill="#111827"/>'
            r'<circle cx="427.6" cy="262.8" r="2.5" fill="#111827"/>'
            r'<circle cx="439.5" cy="193.1" r="2.5" fill="#111827"/>'
            r'<circle cx="459.5" cy="191.5" r="2.5" fill="#111827"/>'
            r'<circle cx="459.7" cy="232.9" r="2.5" fill="#111827"/>'
            r'<circle cx="457.8" cy="261.7" r="2.5" fill="#111827"/>'
            r'<circle cx="471.8" cy="189.2" r="2.5" fill="#111827"/>'
            r'<circle cx="471.8" cy="271.5" r="2.5" fill="#111827"/>'
            r'<circle cx="487.4" cy="192.4" r="2.5" fill="#111827"/>'
            r'<circle cx="502.6" cy="190.9" r="2.5" fill="#111827"/>'
            r'<circle cx="505.4" cy="231.8" r="2.5" fill="#111827"/>'
            r'<circle cx="503.6" cy="244.7" r="2.5" fill="#111827"/>'
            r'<circle cx="504.4" cy="262.6" r="2.5" fill="#111827"/>'
            r'<circle cx="519.9" cy="258.3" r="2.5" fill="#111827"/>'
            r'<circle cx="520.1" cy="272.8" r="2.5" fill="#111827"/>'
            r'<circle cx="347" cy="212" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="347" y="216.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="379" cy="212" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="379" y="216.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="411" cy="212" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="411" y="216.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="443" cy="212" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="443" y="216.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="475" cy="212" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="475" y="216.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="507" cy="212" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="507" y="216.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="315" cy="246" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="315" y="250.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="347" cy="246" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="347" y="250.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="379" cy="246" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="379" y="250.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="411" cy="246" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="411" y="250.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="443" cy="246" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="443" y="250.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<circle cx="475" cy="246" r="13" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>'
            r'<text x="475" y="250.5" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">+</text>'
            r'<line x1="289" y1="212" x2="319" y2="212" stroke="#374151" stroke-width="2"/>'
            r'<polygon points="327,212 317,207 317,217" fill="#374151"/>'
            r'</svg>'
            r'<figcaption>Figure: Cross sections of an ionic solid and a metal before and after the top layer of particles is shifted by one position (small dots represent mobile valence electrons)</figcaption>'
            r'</figure>'
        ),
        "question": r"The diagrams above represent cross sections of an ionic solid and of a metallic solid before and after a force shifts the top layer of particles by one position. Which of the following is best supported by the diagrams?",
        "options": [
            r"Both solids are malleable, because in both solids the layers can slide past each other without any change in the forces between neighboring particles.",
            r"The ionic solid is brittle, because the shift places ions of like charge next to each other and the resulting repulsions split the crystal, whereas the metal is malleable, because its cations remain surrounded by mobile valence electrons after the shift.",
            r"The metal is brittle, because the shift places positive metal cations next to each other, whereas the ionic solid is malleable, because each ion can move freely within its layer.",
            r"Both solids are brittle, because in both solids the shift breaks the covalent bonds that hold the particles in fixed positions.",
        ],
        "correct_index": 1,
        "explanation": r"In the ionic solid before the shift, each ion is surrounded by ions of opposite charge, so Coulombic attractions hold the layers together. After the top layer moves by one position, each cation sits next to a cation and each anion next to an anion; the strong repulsions between like charges push the layers apart, so the crystal splits. This is why ionic solids are brittle. In the metal, the cations are held together by a sea of mobile valence electrons that are not tied to particular atoms. After the shift, every cation is still surrounded by the electron sea, so the attractions remain and the metal deforms without breaking: it is malleable and ductile. The metal cations are never left next to each other without mobile electrons between them, so the metal does not shatter, and the ions in an ionic solid are not free to move within a layer. Neither solid is held together by covalent bonds between its particles.",
    },
    {
        "unit_q_num": 55,
        "topic_code": "3.2",
        "topic_title": "Properties of Solids",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"$n$-Octane, $\text{CH}_3(\text{CH}_2)_6\text{CH}_3$, and 2,2,3,3-tetramethylbutane, $(\text{CH}_3)_3\text{CC}(\text{CH}_3)_3$, are nonpolar structural isomers with the molecular formula $\text{C}_8\text{H}_{18}$. $n$-Octane melts at $-57^\circ\text{C}$ and boils at $126^\circ\text{C}$, whereas 2,2,3,3-tetramethylbutane melts at $101^\circ\text{C}$ and boils at $106^\circ\text{C}$. Which of the following best accounts for these data?",
        "options": [
            r"The elongated $n$-octane molecules have more contact area with one another, so their London dispersion forces are stronger and $n$-octane boils at a higher temperature; the compact, symmetrical 2,2,3,3-tetramethylbutane molecules pack together very efficiently in the solid, which gives it the higher melting point.",
            r"Melting 2,2,3,3-tetramethylbutane requires breaking some of its covalent C–C bonds, whereas boiling it requires overcoming only London dispersion forces.",
            r"Because the two isomers have the same number of electrons, their London dispersion forces are equally strong, so the differences in melting and boiling points must result from differences in the strengths of their covalent C–H bonds.",
            r"Molecules of 2,2,3,3-tetramethylbutane form hydrogen bonds with one another in the solid but not in the liquid, which raises its melting point without raising its boiling point.",
        ],
        "correct_index": 0,
        "explanation": r"Boiling separates the molecules completely, so boiling point reflects the total strength of the intermolecular forces. Both isomers have $66$ electrons, but the long, unbranched $n$-octane molecules have more surface area in contact with their neighbors, so their London dispersion forces are stronger and $n$-octane boils at the higher temperature ($126^\circ\text{C}$ versus $106^\circ\text{C}$). In melting, the intermolecular interactions are only rearranged, so melting point also depends on how well the molecules fit together in the solid. The nearly spherical, highly symmetrical 2,2,3,3-tetramethylbutane molecules pack into an orderly solid very efficiently, so that solid is unusually stable and melts at $101^\circ\text{C}$, far above $n$-octane ($-57^\circ\text{C}$). Melting and boiling a molecular substance do not break covalent bonds. Equal numbers of electrons do not guarantee equal dispersion forces, because molecular shape affects contact area. Neither compound has H bonded to N, O, or F, so neither forms hydrogen bonds.",
    },
    {
        "unit_q_num": 56,
        "topic_code": "3.2",
        "topic_title": "Properties of Solids",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"An enzyme is a protein that catalyzes a reaction by binding reactant molecules at a region of its folded chain called the active site. A solution of an enzyme is heated to $70^\circ\text{C}$ for $10$ minutes and then cooled back to $37^\circ\text{C}$. After this treatment, the enzyme no longer catalyzes the reaction, even though analysis shows that the sequence of covalently bonded amino acids in its chain is unchanged. Which of the following best explains the loss of catalytic activity?",
        "options": [
            r"Heating broke covalent bonds in the backbone of the protein chain, splitting the enzyme into fragments that are too small to bind the reactant molecules.",
            r"Heating permanently increased the average kinetic energy of the enzyme molecules, so even at $37^\circ\text{C}$ they move too fast to bind the reactant molecules.",
            r"Heating converted the hydrogen bonds within the enzyme into covalent bonds, which made the chain too rigid to bind the reactant molecules.",
            r"Heating disrupted noncovalent interactions, such as hydrogen bonds, between different regions of the chain, so the chain changed shape and the active site no longer has the shape needed to bind the reactant molecules.",
        ],
        "correct_index": 3,
        "explanation": r"The function of a large biomolecule depends strongly on its shape, and that shape is held in place largely by noncovalent interactions (hydrogen bonds, ion-ion attractions, dipole interactions, and London dispersion forces) between different regions of the same chain. These interactions are much weaker than covalent bonds, so the increased molecular motion at $70^\circ\text{C}$ disrupts them; the chain unfolds or refolds into a different shape, and the active site loses the shape that allowed it to bind the reactants. Cooling does not necessarily restore the original arrangement. Breaking backbone covalent bonds is ruled out because the amino-acid sequence is unchanged. The average kinetic energy of particles depends only on the current Kelvin temperature, so after cooling to $37^\circ\text{C}$ the enzyme molecules have the same average kinetic energy as before heating. Heating breaks noncovalent interactions; it does not convert hydrogen bonds into covalent bonds.",
    },
    {
        "unit_q_num": 57,
        "topic_code": "3.3",
        "topic_title": "Solids, Liquids, and Gases",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r'<figure class="quiz-figure-wrap">'
            r'<svg class="quiz-figure" viewBox="0 0 520 230" role="img" aria-label="Two panels of identical circular particles in close contact. In Sample 1 the particles are arranged in a regular, repeating pattern of straight rows. In Sample 2 the particles are close together but arranged irregularly, with no repeating pattern." font-family="sans-serif">'
            r'<rect x="0" y="0" width="520" height="230" fill="#ffffff"/>'
            r'<rect x="10" y="10" width="245" height="210" rx="6" fill="none" stroke="#9ca3af" stroke-width="1.5"/>'
            r'<text x="132.5" y="32" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">Sample 1</text>'
            r'<rect x="265" y="10" width="245" height="210" rx="6" fill="none" stroke="#9ca3af" stroke-width="1.5"/>'
            r'<text x="387.5" y="32" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">Sample 2</text>'
            r'<circle cx="32.8" cy="54.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="53.8" cy="54.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="74.8" cy="54.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="95.8" cy="54.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="116.8" cy="54.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="137.8" cy="54.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="158.8" cy="54.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="179.8" cy="54.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="200.8" cy="54.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="221.8" cy="54.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="43.2" cy="72.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="64.2" cy="72.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="85.2" cy="72.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="106.2" cy="72.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="127.2" cy="72.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="148.2" cy="72.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="169.2" cy="72.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="190.2" cy="72.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="211.2" cy="72.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="232.2" cy="72.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="32.8" cy="90.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="53.8" cy="90.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="74.8" cy="90.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="95.8" cy="90.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="116.8" cy="90.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="137.8" cy="90.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="158.8" cy="90.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="179.8" cy="90.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="200.8" cy="90.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="221.8" cy="90.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="43.2" cy="108.8" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="64.2" cy="108.8" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="85.2" cy="108.8" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="106.2" cy="108.8" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="127.2" cy="108.8" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="148.2" cy="108.8" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="169.2" cy="108.8" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="190.2" cy="108.8" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="211.2" cy="108.8" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="232.2" cy="108.8" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="32.8" cy="127" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="53.8" cy="127" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="74.8" cy="127" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="95.8" cy="127" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="116.8" cy="127" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="137.8" cy="127" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="158.8" cy="127" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="179.8" cy="127" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="200.8" cy="127" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="221.8" cy="127" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="43.2" cy="145.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="64.2" cy="145.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="85.2" cy="145.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="106.2" cy="145.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="127.2" cy="145.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="148.2" cy="145.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="169.2" cy="145.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="190.2" cy="145.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="211.2" cy="145.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="232.2" cy="145.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="32.8" cy="163.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="53.8" cy="163.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="74.8" cy="163.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="95.8" cy="163.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="116.8" cy="163.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="137.8" cy="163.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="158.8" cy="163.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="179.8" cy="163.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="200.8" cy="163.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="221.8" cy="163.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="43.2" cy="181.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="64.2" cy="181.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="85.2" cy="181.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="106.2" cy="181.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="127.2" cy="181.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="148.2" cy="181.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="169.2" cy="181.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="190.2" cy="181.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="211.2" cy="181.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="232.2" cy="181.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="32.8" cy="199.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="53.8" cy="199.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="74.8" cy="199.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="95.8" cy="199.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="116.8" cy="199.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="137.8" cy="199.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="158.8" cy="199.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="179.8" cy="199.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="200.8" cy="199.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="221.8" cy="199.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="435.5" cy="166.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="458.4" cy="201.9" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="437.2" cy="201.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="285.6" cy="116.8" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="489.2" cy="180.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="466.5" cy="74.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="401" cy="76.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="400.1" cy="121.9" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="285.5" cy="74" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="336.6" cy="175.8" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="445.4" cy="74.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="415.6" cy="95" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="285.1" cy="178.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="343.6" cy="71.1" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="468" cy="183.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="404.6" cy="142.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="307.1" cy="201.1" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="413.9" cy="201" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="455.7" cy="92.9" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="363.7" cy="68.3" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="307.4" cy="53.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="343.9" cy="129.3" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="285.8" cy="157.9" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="336.4" cy="99.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="475.7" cy="92.5" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="353.9" cy="109.3" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="418.9" cy="52.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="467.8" cy="52.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="477.7" cy="164" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="303.5" cy="169.8" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="385.4" cy="136.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="286.9" cy="52.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="317.9" cy="184.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="456.7" cy="165.8" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="402" cy="181.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="322.5" cy="161.3" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="447.2" cy="183.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="286.3" cy="201.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="326.4" cy="81.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="391.1" cy="201.5" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="350.8" cy="201.5" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="420" cy="114.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="306.5" cy="75.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="479.2" cy="129.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="375.8" cy="52.3" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="411.1" cy="163.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="393.9" cy="97" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="447.7" cy="52.1" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="309.5" cy="102.8" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="330" cy="201.9" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="489.2" cy="109.9" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="391.3" cy="157.6" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="370.9" cy="200.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="379.7" cy="82.3" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="286.2" cy="96.5" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="357.9" cy="162.3" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="456" cy="129.3" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="341.7" cy="149.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="444.5" cy="112" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="306.4" cy="147.5" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="324.4" cy="138.1" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="359.2" cy="182.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="426" cy="184.3" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="366.7" cy="144.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="488.8" cy="147.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="488.9" cy="201.9" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="446.8" cy="147.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="466.1" cy="111.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="434.3" cy="129.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="377.6" cy="172.8" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="397.2" cy="55.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="329.7" cy="56" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="289" cy="137.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="326.7" cy="118.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="349.9" cy="52" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="468" cy="146.2" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="424.8" cy="146.8" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="435.6" cy="92.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="489.1" cy="52.1" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="307.1" cy="126.4" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="367.6" cy="124" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="353.9" cy="88.7" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="488.7" cy="74.3" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="422.9" cy="74" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'<circle cx="373.5" cy="102.3" r="10" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>'
            r'</svg>'
            r'<figcaption>Figure: Particulate-level views of two solid samples of the same substance</figcaption>'
            r'</figure>'
        ),
        "question": r"The particulate diagrams above represent two solid samples of the same pure substance. Sample 1 was formed by cooling the liquid slowly, and Sample 2 was formed by cooling the liquid very rapidly. Which of the following best describes the two samples?",
        "options": [
            r"Sample 1 is a solid and Sample 2 is a liquid, because the particles in Sample 2 are not arranged in a regular pattern.",
            r"Both samples are crystalline solids, because in both samples each particle is in close contact with neighboring particles.",
            r"Both samples are solids, but the particles in Sample 1 are motionless, whereas the particles in Sample 2 slowly move past one another.",
            r"Sample 1 is a crystalline solid and Sample 2 is an amorphous solid; in both samples the particles vibrate about fixed positions and do not move past one another.",
        ],
        "correct_index": 3,
        "explanation": r"A crystalline solid has its particles arranged in a regular, repeating three-dimensional pattern, as in Sample 1. An amorphous solid, such as a glass, has particles with no regular, orderly arrangement, as in Sample 2. Rapid cooling does not give the particles time to arrange themselves into an ordered structure, so they are locked into a disordered arrangement. In both kinds of solid, the motion of the particles is limited: they vibrate about fixed positions and do not undergo overall translation relative to one another. A disordered arrangement alone does not make a sample a liquid; in a liquid the particles continually move past one another. Close contact between particles occurs in crystalline solids, amorphous solids, and liquids alike, so it does not show that a solid is crystalline. Particles in a solid are never motionless; they always vibrate.",
    },
    {
        "unit_q_num": 58,
        "topic_code": "3.3",
        "topic_title": "Solids, Liquids, and Gases",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r'<table class="quiz-data-table">'
            r'<thead><tr><th>Phase</th><th>Temperature ($^\circ\text{C}$)</th><th>Pressure ($\text{atm}$)</th><th>Density ($\text{g/cm}^3$)</th></tr></thead>'
            r'<tbody>'
            r'<tr><td>$\text{H}_2\text{O}(s)$</td><td>$0$</td><td>$1$</td><td>$0.917$</td></tr>'
            r'<tr><td>$\text{H}_2\text{O}(l)$</td><td>$0$</td><td>$1$</td><td>$1.000$</td></tr>'
            r'<tr><td>$\text{H}_2\text{O}(l)$</td><td>$100$</td><td>$1$</td><td>$0.958$</td></tr>'
            r'<tr><td>$\text{H}_2\text{O}(g)$</td><td>$100$</td><td>$1$</td><td>$0.000598$</td></tr>'
            r'</tbody></table>'
        ),
        "question": r"The densities of $\text{H}_2\text{O}$ (molar mass $18.0\text{ g/mol}$) in three phases are given in the table above. The molar volume of $\text{H}_2\text{O}(g)$ at $100^\circ\text{C}$ and $1\text{ atm}$ is closest to how many times the molar volume of $\text{H}_2\text{O}(l)$ at $100^\circ\text{C}$?",
        "options": [
            r"$1.09$",
            r"$18.8$",
            r"$1.60 \times 10^{3}$",
            r"$3.01 \times 10^{4}$",
        ],
        "correct_index": 2,
        "explanation": r"Molar volume equals molar mass divided by density. For the liquid at $100^\circ\text{C}$: $18.0 \div 0.958 = 18.8\text{ cm}^3\text{/mol}$. For the gas: $18.0 \div 0.000598 = 3.01 \times 10^{4}\text{ cm}^3\text{/mol}$. The ratio is $\dfrac{3.01 \times 10^{4}}{18.8} = 1.60 \times 10^{3}$ (equivalently, $0.958 \div 0.000598$). By contrast, the molar volumes of ice ($18.0 \div 0.917 = 19.6\text{ cm}^3\text{/mol}$) and liquid water at $0^\circ\text{C}$ ($18.0\text{ cm}^3\text{/mol}$) differ by less than $10\%$: in both the solid and the liquid the molecules are in close contact, whereas in the gas they are far apart, so a gas has neither a definite volume nor a definite shape. The value $1.09$ compares the solid with the liquid at $0^\circ\text{C}$, not the gas with the liquid. The values $18.8$ and $3.01 \times 10^{4}$ are the individual molar volumes in $\text{cm}^3\text{/mol}$, not their ratio.",
    },
    {
        "unit_q_num": 59,
        "topic_code": "3.3",
        "topic_title": "Solids, Liquids, and Gases",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A student gently adds one drop of the same food-coloring solution to each of three undisturbed beakers. Beaker 1 contains water at $20^\circ\text{C}$, Beaker 2 contains water at $60^\circ\text{C}$, and Beaker 3 contains glycerol, $\text{C}_3\text{H}_5(\text{OH})_3$, at $20^\circ\text{C}$. The color spreads through Beaker 2 fastest, more slowly through Beaker 1, and extremely slowly through Beaker 3. Which of the following best explains these observations?",
        "options": [
            r"Particles in a liquid are stationary unless the liquid is heated, so in the $20^\circ\text{C}$ liquids the color spreads only because the drop sinks under its own weight.",
            r"Glycerol molecules are much farther apart than water molecules, so the dye particles must travel farther between collisions and therefore spread more slowly.",
            r"Glycerol molecules are larger than water molecules, so glycerol has weaker intermolecular forces, and the dye particles are not pulled through the glycerol.",
            r"Particles in a liquid are in close contact and constantly moving; they move faster at higher temperature, and extensive hydrogen bonding among glycerol molecules, each of which has three $-\text{OH}$ groups, restricts their movement.",
        ],
        "correct_index": 3,
        "explanation": r"The particles of a liquid are in close contact and are continually moving and colliding, and their movement depends on temperature and on the strength of the forces between them. Water at $60^\circ\text{C}$ has a greater average kinetic energy than water at $20^\circ\text{C}$, so its molecules (and the dye particles among them) move about faster and the color spreads sooner. Each glycerol molecule has three $-\text{OH}$ groups and forms many hydrogen bonds with its neighbors; these strong attractions make it much harder for the molecules to move past one another, so the dye spreads extremely slowly. Particles in a liquid move at every temperature, not only when heated. The molecules of liquid glycerol and of liquid water are both in close contact; neither liquid has gas-like spacing. Although glycerol molecules are larger, their extensive hydrogen bonding makes their intermolecular forces stronger, not weaker, than those in water.",
    },
    {
        "unit_q_num": 60,
        "topic_code": "3.4",
        "topic_title": "Ideal Gas Law",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r'<figure class="quiz-figure-wrap">'
            r'<svg class="quiz-figure" viewBox="0 0 520 320" role="img" aria-label="Graph of pressure in atmospheres, from 0 to 6, versus temperature in kelvins, from 0 to 600. Four data points lie at 200 K and 2.00 atm, 300 K and 3.00 atm, 400 K and 4.00 atm, and 500 K and 5.00 atm. A solid straight line passes through the points, and a dashed extension of the line passes through the origin." font-family="sans-serif">'
            r'<rect x="0" y="0" width="520" height="320" fill="#ffffff"/>'
            r'<line x1="140" y1="270" x2="140" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>'
            r'<line x1="210" y1="270" x2="210" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>'
            r'<line x1="280" y1="270" x2="280" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>'
            r'<line x1="350" y1="270" x2="350" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>'
            r'<line x1="420" y1="270" x2="420" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>'
            r'<line x1="490" y1="270" x2="490" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>'
            r'<line x1="70" y1="230" x2="490" y2="230" stroke="#e5e7eb" stroke-width="1.5"/>'
            r'<line x1="70" y1="190" x2="490" y2="190" stroke="#e5e7eb" stroke-width="1.5"/>'
            r'<line x1="70" y1="150" x2="490" y2="150" stroke="#e5e7eb" stroke-width="1.5"/>'
            r'<line x1="70" y1="110" x2="490" y2="110" stroke="#e5e7eb" stroke-width="1.5"/>'
            r'<line x1="70" y1="70" x2="490" y2="70" stroke="#e5e7eb" stroke-width="1.5"/>'
            r'<line x1="70" y1="30" x2="490" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>'
            r'<line x1="70" y1="270" x2="490" y2="270" stroke="#111827" stroke-width="2"/>'
            r'<line x1="70" y1="270" x2="70" y2="30" stroke="#111827" stroke-width="2"/>'
            r'<line x1="70" y1="270" x2="70" y2="276" stroke="#111827" stroke-width="2"/>'
            r'<text x="70" y="292" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#111827">0</text>'
            r'<line x1="140" y1="270" x2="140" y2="276" stroke="#111827" stroke-width="2"/>'
            r'<text x="140" y="292" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#111827">100</text>'
            r'<line x1="210" y1="270" x2="210" y2="276" stroke="#111827" stroke-width="2"/>'
            r'<text x="210" y="292" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#111827">200</text>'
            r'<line x1="280" y1="270" x2="280" y2="276" stroke="#111827" stroke-width="2"/>'
            r'<text x="280" y="292" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#111827">300</text>'
            r'<line x1="350" y1="270" x2="350" y2="276" stroke="#111827" stroke-width="2"/>'
            r'<text x="350" y="292" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#111827">400</text>'
            r'<line x1="420" y1="270" x2="420" y2="276" stroke="#111827" stroke-width="2"/>'
            r'<text x="420" y="292" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#111827">500</text>'
            r'<line x1="490" y1="270" x2="490" y2="276" stroke="#111827" stroke-width="2"/>'
            r'<text x="490" y="292" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#111827">600</text>'
            r'<line x1="64" y1="270" x2="70" y2="270" stroke="#111827" stroke-width="2"/>'
            r'<text x="58" y="274" font-family="sans-serif" font-size="12" text-anchor="end" fill="#111827">0</text>'
            r'<line x1="64" y1="230" x2="70" y2="230" stroke="#111827" stroke-width="2"/>'
            r'<text x="58" y="234" font-family="sans-serif" font-size="12" text-anchor="end" fill="#111827">1</text>'
            r'<line x1="64" y1="190" x2="70" y2="190" stroke="#111827" stroke-width="2"/>'
            r'<text x="58" y="194" font-family="sans-serif" font-size="12" text-anchor="end" fill="#111827">2</text>'
            r'<line x1="64" y1="150" x2="70" y2="150" stroke="#111827" stroke-width="2"/>'
            r'<text x="58" y="154" font-family="sans-serif" font-size="12" text-anchor="end" fill="#111827">3</text>'
            r'<line x1="64" y1="110" x2="70" y2="110" stroke="#111827" stroke-width="2"/>'
            r'<text x="58" y="114" font-family="sans-serif" font-size="12" text-anchor="end" fill="#111827">4</text>'
            r'<line x1="64" y1="70" x2="70" y2="70" stroke="#111827" stroke-width="2"/>'
            r'<text x="58" y="74" font-family="sans-serif" font-size="12" text-anchor="end" fill="#111827">5</text>'
            r'<line x1="64" y1="30" x2="70" y2="30" stroke="#111827" stroke-width="2"/>'
            r'<text x="58" y="34" font-family="sans-serif" font-size="12" text-anchor="end" fill="#111827">6</text>'
            r'<text x="280" y="314" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">Temperature (K)</text>'
            r'<text x="22" y="150" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 22 150)">Pressure (atm)</text>'
            r'<line x1="70" y1="270" x2="210" y2="190" stroke="#374151" stroke-width="2" stroke-dasharray="6 5"/>'
            r'<line x1="210" y1="190" x2="420" y2="70" stroke="#374151" stroke-width="2"/>'
            r'<circle cx="210" cy="190" r="4.5" fill="#111827"/>'
            r'<circle cx="280" cy="150" r="4.5" fill="#111827"/>'
            r'<circle cx="350" cy="110" r="4.5" fill="#111827"/>'
            r'<circle cx="420" cy="70" r="4.5" fill="#111827"/>'
            r'</svg>'
            r'<figcaption>Figure: Pressure versus temperature for a gas sample in a sealed, rigid container</figcaption>'
            r'</figure>'
        ),
        "question": r"The graph above shows the pressure of a $0.500\text{ mol}$ sample of an ideal gas in a sealed, rigid container measured at several temperatures. What is the volume of the container?",
        "options": [
            r"$0.244\text{ L}$",
            r"$4.10\text{ L}$",
            r"$8.21\text{ L}$",
            r"$416\text{ L}$",
        ],
        "correct_index": 1,
        "explanation": r"For a fixed amount of gas in a rigid container, $n$ and $V$ are constant, so $P = \left(\dfrac{nR}{V}\right)T$, and a graph of $P$ versus Kelvin temperature is a straight line through the origin, as shown. The slope is $\dfrac{(5.00 - 2.00)\text{ atm}}{(500 - 200)\text{ K}} = 0.0100\text{ atm/K}$, which equals $\dfrac{nR}{V}$. So $V = \dfrac{nR}{\text{slope}} = \dfrac{(0.500)(0.08206)}{0.0100} = 4.10\text{ L}$. A single point gives the same result: $V = \dfrac{nRT}{P} = \dfrac{(0.500)(0.08206)(400)}{4.00} = 4.10\text{ L}$. The value $8.21\text{ L}$ results from ignoring the $0.500\text{ mol}$ and using $n = 1$. The value $416\text{ L}$ results from using $R = 8.314\text{ J mol}^{-1}\text{ K}^{-1}$ with pressures in atmospheres. The value $0.244$ is the inverted ratio $\dfrac{P}{nRT}$, which does not even have units of volume.",
    },
    {
        "unit_q_num": 61,
        "topic_code": "3.4",
        "topic_title": "Ideal Gas Law",
        "difficulty": "Challenging",
        "stimulus": (
            r'<table class="quiz-data-table">'
            r'<thead><tr><th>Trial</th><th>Volume of Liquid Ethanol Injected ($\text{mL}$)</th><th>Final Total Pressure ($\text{torr}$)</th></tr></thead>'
            r'<tbody>'
            r'<tr><td>$1$</td><td>$0.10$</td><td>$784$</td></tr>'
            r'<tr><td>$2$</td><td>$0.50$</td><td>$811$</td></tr>'
            r'<tr><td>$3$</td><td>$1.00$</td><td>$811$</td></tr>'
            r'</tbody></table>'
        ),
        "question": r"A student investigates the vapor pressure of ethanol, $\text{C}_2\text{H}_5\text{OH}$, at $25.0^\circ\text{C}$. In each trial, a rigid $1.00\text{ L}$ flask containing dry air at $752\text{ torr}$ is sealed, a measured volume of liquid ethanol (density $0.789\text{ g/mL}$) is injected through a rubber septum, and the total pressure is recorded after it stops changing. The temperature is held at $25.0^\circ\text{C}$, and the volume of the injected liquid is negligible compared with the volume of the flask. Which of the following is the best interpretation of the data in the table above?",
        "options": [
            r"The vapor pressure of ethanol at $25.0^\circ\text{C}$ is $59\text{ torr}$; in Trial 1, all of the ethanol evaporated before its partial pressure could reach this value.",
            r"The vapor pressure of ethanol at $25.0^\circ\text{C}$ is $32\text{ torr}$; in Trials 2 and 3, the additional ethanol vapor also increased the partial pressure of the air.",
            r"The vapor pressure of ethanol depends on the amount of liquid present, so it is $32\text{ torr}$ in Trial 1 and $59\text{ torr}$ in Trials 2 and 3.",
            r"The vapor pressure of ethanol at $25.0^\circ\text{C}$ is $811\text{ torr}$, because this is the constant total pressure reached in both Trials 2 and 3.",
        ],
        "correct_index": 0,
        "explanation": r"The air in the flask keeps the same number of moles, volume, and temperature, so its partial pressure stays $752\text{ torr}$; the partial pressure of each gas is independent of the other gases present. Therefore $P_{\text{ethanol}} = P_{\text{total}} - 752\text{ torr}$: $32\text{ torr}$ in Trial 1 and $59\text{ torr}$ in Trials 2 and 3. Because Trials 2 and 3 give the same value even though twice as much ethanol was injected in Trial 3, liquid must have remained in both flasks, so $59\text{ torr}$ is the equilibrium vapor pressure. In Trial 1, only $0.079\text{ g}$ ($1.71 \times 10^{-3}\text{ mol}$) was injected; if it all evaporates, $P = \dfrac{nRT}{V} = 0.0419\text{ atm} = 32\text{ torr}$, matching the data, so no liquid remained and the vapor never reached its vapor pressure. Vapor pressure depends only on the substance and the temperature, not on the amount of liquid. The value $811\text{ torr}$ includes the pressure of the air.",
    },
    {
        "unit_q_num": 62,
        "topic_code": "3.5",
        "topic_title": "Kinetic Molecular Theory",
        "difficulty": "Challenging",
        "stimulus": (
            r'<figure class="quiz-figure-wrap">'
            r'<svg class="quiz-figure" viewBox="0 0 520 310" role="img" aria-label="Graph of fraction of atoms versus kinetic energy in units of 10 to the minus 21 joules, from 0 to 36. Curve 1 rises steeply to a tall, narrow peak at 2 and falls nearly to zero by about 20. Curve 2 rises to a peak half as high at 4, is broader, and extends to higher energies. Dotted vertical lines mark the average kinetic energy of each sample: 6 for Curve 1 and 12 for Curve 2." font-family="sans-serif">'
            r'<rect x="0" y="0" width="520" height="310" fill="#ffffff"/>'
            r'<line x1="70" y1="260" x2="490" y2="260" stroke="#111827" stroke-width="2"/>'
            r'<line x1="70" y1="260" x2="70" y2="30" stroke="#111827" stroke-width="2"/>'
            r'<line x1="70" y1="260" x2="70" y2="266" stroke="#111827" stroke-width="2"/>'
            r'<text x="70" y="281" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#111827">0</text>'
            r'<line x1="140" y1="260" x2="140" y2="266" stroke="#111827" stroke-width="2"/>'
            r'<text x="140" y="281" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#111827">6</text>'
            r'<line x1="210" y1="260" x2="210" y2="266" stroke="#111827" stroke-width="2"/>'
            r'<text x="210" y="281" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#111827">12</text>'
            r'<line x1="280" y1="260" x2="280" y2="266" stroke="#111827" stroke-width="2"/>'
            r'<text x="280" y="281" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#111827">18</text>'
            r'<line x1="350" y1="260" x2="350" y2="266" stroke="#111827" stroke-width="2"/>'
            r'<text x="350" y="281" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#111827">24</text>'
            r'<line x1="420" y1="260" x2="420" y2="266" stroke="#111827" stroke-width="2"/>'
            r'<text x="420" y="281" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#111827">30</text>'
            r'<line x1="490" y1="260" x2="490" y2="266" stroke="#111827" stroke-width="2"/>'
            r'<text x="490" y="281" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#111827">36</text>'
            r'<text x="280" y="302" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827">Kinetic energy (×10⁻²¹ J)</text>'
            r'<text x="24" y="150" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 24 150)">Fraction of atoms</text>'
            r'<line x1="140.1" y1="260" x2="140.1" y2="126.2" stroke="#374151" stroke-width="1.5" stroke-dasharray="2 3"/>'
            r'<line x1="210.1" y1="260" x2="210.1" y2="193.1" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="2 3"/>'
            r'<polyline points="70,260 70.2,225.6 70.5,211.5 70.7,201 70.9,192.2 71.2,184.5 71.4,177.7 71.6,171.6 71.9,166 72.1,160.7 72.3,155.9 72.6,151.4 '
            r'72.8,147.1 73,143.1 73.3,139.3 73.5,135.6 73.7,132.2 74,128.9 74.2,125.8 74.4,122.8 74.7,119.9 74.9,117.2 75.1,114.6 75.4,112 '
            r'75.6,109.6 75.8,107.3 76.1,105 76.3,102.9 76.5,100.8 76.8,98.8 77,96.8 77.2,95 77.5,93.2 77.7,91.4 77.9,89.7 78.2,88.1 '
            r'78.4,86.5 78.6,85 78.9,83.6 79.1,82.1 79.3,80.8 79.6,79.4 79.8,78.2 80,76.9 80.3,75.7 80.5,74.6 80.7,73.5 81,72.4 '
            r'81.2,71.4 81.4,70.3 81.7,69.4 81.9,68.4 82.1,67.5 82.4,66.7 82.6,65.8 82.8,65 83.1,64.2 83.3,63.5 83.5,62.7 83.8,62 '
            r'84,61.4 84.2,60.7 84.5,60.1 84.7,59.5 84.9,58.9 85.2,58.3 85.4,57.8 85.6,57.3 85.9,56.8 86.1,56.3 86.3,55.9 86.6,55.5 '
            r'86.8,55.1 87,54.7 87.3,54.3 87.5,53.9 87.7,53.6 88,53.3 88.2,53 88.4,52.7 88.7,52.4 88.9,52.2 89.1,51.9 89.4,51.7 '
            r'89.6,51.5 89.8,51.3 90.1,51.1 90.3,51 90.5,50.8 90.8,50.7 91,50.6 91.2,50.5 91.5,50.4 91.7,50.3 91.9,50.2 92.2,50.1 '
            r'92.4,50.1 92.6,50.1 92.9,50 93.1,50 93.3,50 94.5,50.1 95.7,50.5 96.8,51.1 98,51.8 99.2,52.8 100.3,53.9 101.5,55.1 '
            r'102.7,56.5 103.8,58 105,59.6 106.2,61.4 107.3,63.2 108.5,65 109.7,67 110.8,69 112,71.1 113.2,73.2 114.3,75.3 115.5,77.5 '
            r'116.7,79.8 117.8,82 119,84.3 120.2,86.6 121.3,89 122.5,91.3 123.7,93.6 124.8,96 126,98.3 127.2,100.7 128.3,103 129.5,105.4 '
            r'130.7,107.7 131.8,110.1 133,112.4 134.2,114.7 135.3,117 136.5,119.3 137.7,121.6 138.8,123.8 140,126.1 141.2,128.3 142.3,130.5 143.5,132.7 '
            r'144.7,134.8 145.8,137 147,139.1 148.2,141.2 149.3,143.2 150.5,145.3 151.7,147.3 152.8,149.3 154,151.3 155.2,153.2 156.3,155.1 157.5,157 '
            r'158.7,158.9 159.8,160.8 161,162.6 162.2,164.4 163.3,166.1 164.5,167.9 165.7,169.6 166.8,171.3 168,173 169.2,174.6 170.3,176.2 171.5,177.8 '
            r'172.7,179.4 173.8,180.9 175,182.5 176.2,183.9 177.3,185.4 178.5,186.9 179.7,188.3 180.8,189.7 182,191.1 183.2,192.4 184.3,193.7 185.5,195 '
            r'186.7,196.3 187.8,197.6 189,198.8 190.2,200 191.3,201.2 192.5,202.4 193.7,203.6 194.8,204.7 196,205.8 197.2,206.9 198.3,208 199.5,209 '
            r'200.7,210.1 201.8,211.1 203,212.1 204.2,213.1 205.3,214 206.5,215 207.7,215.9 208.8,216.8 210,217.7 212.9,219.8 215.8,221.9 218.8,223.8 '
            r'221.7,225.7 224.6,227.5 227.5,229.1 230.4,230.7 233.3,232.3 236.2,233.7 239.2,235.1 242.1,236.4 245,237.6 247.9,238.8 250.8,239.9 253.8,241 '
            r'256.7,242 259.6,243 262.5,243.9 265.4,244.7 268.3,245.5 271.2,246.3 274.2,247.1 277.1,247.8 280,248.4 282.9,249 285.8,249.6 288.8,250.2 '
            r'291.7,250.7 294.6,251.2 297.5,251.7 300.4,252.2 303.3,252.6 306.2,253 309.2,253.4 312.1,253.7 315,254.1 317.9,254.4 320.8,254.7 323.8,255 '
            r'326.7,255.3 329.6,255.5 332.5,255.8 335.4,256 338.3,256.2 341.2,256.5 344.2,256.6 347.1,256.8 350,257 352.9,257.2 355.8,257.3 358.8,257.5 '
            r'361.7,257.6 364.6,257.8 367.5,257.9 370.4,258 373.3,258.1 376.2,258.2 379.2,258.3 382.1,258.4 385,258.5 387.9,258.6 390.8,258.7 393.8,258.7 '
            r'396.7,258.8 399.6,258.9 402.5,258.9 405.4,259 408.3,259.1 411.2,259.1 414.2,259.2 417.1,259.2 420,259.3 422.9,259.3 425.8,259.3 428.8,259.4 '
            r'431.7,259.4 434.6,259.4 437.5,259.5 440.4,259.5 443.3,259.5 446.2,259.6 449.2,259.6 452.1,259.6 455,259.6 457.9,259.7 460.8,259.7 463.8,259.7 '
            r'466.7,259.7 469.6,259.7 472.5,259.7 475.4,259.8 478.3,259.8 481.2,259.8 484.2,259.8 487.1,259.8 490,259.8" fill="none" stroke="#111827" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>'
            r'<polyline points="70,260 70.2,247.8 70.5,242.8 70.7,239 70.9,235.8 71.2,233 71.4,230.5 71.6,228.2 71.9,226.1 72.1,224.1 72.3,222.3 72.6,220.5 '
            r'72.8,218.9 73,217.3 73.3,215.8 73.5,214.4 73.7,213 74,211.7 74.2,210.4 74.4,209.1 74.7,207.9 74.9,206.8 75.1,205.7 75.4,204.6 '
            r'75.6,203.5 75.8,202.5 76.1,201.5 76.3,200.6 76.5,199.6 76.8,198.7 77,197.8 77.2,197 77.5,196.1 77.7,195.3 77.9,194.5 78.2,193.7 '
            r'78.4,192.9 78.6,192.1 78.9,191.4 79.1,190.7 79.3,190 79.6,189.3 79.8,188.6 80,187.9 80.3,187.3 80.5,186.6 80.7,186 81,185.4 '
            r'81.2,184.8 81.4,184.2 81.7,183.6 81.9,183.1 82.1,182.5 82.4,182 82.6,181.4 82.8,180.9 83.1,180.4 83.3,179.9 83.5,179.4 83.8,178.9 '
            r'84,178.4 84.2,177.9 84.5,177.5 84.7,177 84.9,176.6 85.2,176.1 85.4,175.7 85.6,175.3 85.9,174.9 86.1,174.5 86.3,174.1 86.6,173.7 '
            r'86.8,173.3 87,172.9 87.3,172.5 87.5,172.1 87.7,171.8 88,171.4 88.2,171.1 88.4,170.7 88.7,170.4 88.9,170.1 89.1,169.7 89.4,169.4 '
            r'89.6,169.1 89.8,168.8 90.1,168.5 90.3,168.2 90.5,167.9 90.8,167.6 91,167.3 91.2,167 91.5,166.7 91.7,166.5 91.9,166.2 92.2,165.9 '
            r'92.4,165.7 92.6,165.4 92.9,165.2 93.1,164.9 93.3,164.7 94.5,163.5 95.7,162.5 96.8,161.5 98,160.7 99.2,159.9 100.3,159.2 101.5,158.5 '
            r'102.7,157.9 103.8,157.4 105,157 106.2,156.6 107.3,156.2 108.5,155.9 109.7,155.7 110.8,155.5 112,155.3 113.2,155.2 114.3,155.1 115.5,155 '
            r'116.7,155 117.8,155 119,155.1 120.2,155.1 121.3,155.2 122.5,155.4 123.7,155.5 124.8,155.7 126,155.9 127.2,156.1 128.3,156.4 129.5,156.7 '
            r'130.7,156.9 131.8,157.2 133,157.6 134.2,157.9 135.3,158.3 136.5,158.6 137.7,159 138.8,159.4 140,159.8 141.2,160.2 142.3,160.7 143.5,161.1 '
            r'144.7,161.6 145.8,162 147,162.5 148.2,163 149.3,163.5 150.5,164 151.7,164.5 152.8,165 154,165.5 155.2,166.1 156.3,166.6 157.5,167.1 '
            r'158.7,167.7 159.8,168.2 161,168.8 162.2,169.3 163.3,169.9 164.5,170.5 165.7,171 166.8,171.6 168,172.2 169.2,172.7 170.3,173.3 171.5,173.9 '
            r'172.7,174.5 173.8,175.1 175,175.6 176.2,176.2 177.3,176.8 178.5,177.4 179.7,178 180.8,178.6 182,179.2 183.2,179.8 184.3,180.3 185.5,180.9 '
            r'186.7,181.5 187.8,182.1 189,182.7 190.2,183.3 191.3,183.9 192.5,184.5 193.7,185 194.8,185.6 196,186.2 197.2,186.8 198.3,187.4 199.5,187.9 '
            r'200.7,188.5 201.8,189.1 203,189.6 204.2,190.2 205.3,190.8 206.5,191.3 207.7,191.9 208.8,192.5 210,193 212.9,194.4 215.8,195.8 218.8,197.1 '
            r'221.7,198.5 224.6,199.8 227.5,201.1 230.4,202.4 233.3,203.7 236.2,204.9 239.2,206.1 242.1,207.3 245,208.5 247.9,209.7 250.8,210.8 253.8,212 '
            r'256.7,213.1 259.6,214.2 262.5,215.2 265.4,216.3 268.3,217.3 271.2,218.3 274.2,219.3 277.1,220.3 280,221.2 282.9,222.2 285.8,223.1 288.8,224 '
            r'291.7,224.8 294.6,225.7 297.5,226.5 300.4,227.4 303.3,228.2 306.2,228.9 309.2,229.7 312.1,230.5 315,231.2 317.9,231.9 320.8,232.6 323.8,233.3 '
            r'326.7,234 329.6,234.6 332.5,235.3 335.4,235.9 338.3,236.5 341.2,237.1 344.2,237.7 347.1,238.3 350,238.8 352.9,239.4 355.8,239.9 358.8,240.4 '
            r'361.7,240.9 364.6,241.4 367.5,241.9 370.4,242.4 373.3,242.8 376.2,243.3 379.2,243.7 382.1,244.2 385,244.6 387.9,245 390.8,245.4 393.8,245.8 '
            r'396.7,246.1 399.6,246.5 402.5,246.9 405.4,247.2 408.3,247.5 411.2,247.9 414.2,248.2 417.1,248.5 420,248.8 422.9,249.1 425.8,249.4 428.8,249.7 '
            r'431.7,250 434.6,250.2 437.5,250.5 440.4,250.8 443.3,251 446.2,251.2 449.2,251.5 452.1,251.7 455,251.9 457.9,252.2 460.8,252.4 463.8,252.6 '
            r'466.7,252.8 469.6,253 472.5,253.2 475.4,253.3 478.3,253.5 481.2,253.7 484.2,253.9 487.1,254 490,254.2" fill="none" stroke="#2563eb" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>'
            r'<text x="124" y="58" font-family="sans-serif" font-size="13" text-anchor="start" fill="#111827">Curve 1</text>'
            r'<text x="225" y="165" font-family="sans-serif" font-size="13" text-anchor="start" fill="#2563eb">Curve 2</text>'
            r'</svg>'
            r'<figcaption>Figure: Distributions of the kinetic energies of the atoms in two gas samples (dotted lines mark the average kinetic energy of each sample)</figcaption>'
            r'</figure>'
        ),
        "question": r"The graph above shows the distributions of kinetic energies of the atoms in two samples of noble gases. Curve 1 represents a sample of $\text{Ar}(g)$ at $290\text{ K}$, and Curve 2 represents a sample of $\text{He}(g)$. What is the temperature of the $\text{He}(g)$ sample?",
        "options": [
            r"$145\text{ K}$",
            r"$290\text{ K}$",
            r"$580\text{ K}$",
            r"$1160\text{ K}$",
        ],
        "correct_index": 2,
        "explanation": r"The Kelvin temperature of a gas is proportional to the average kinetic energy of its particles, regardless of the identity or mass of the particles. At the same temperature, $\text{He}$ atoms and $\text{Ar}$ atoms have the same distribution of kinetic energies; the lighter $\text{He}$ atoms move faster, but $KE = \tfrac{1}{2}mv^2$ is the same on average. Curve 2 is broader, has a lower peak, and is shifted to higher energies; its average kinetic energy ($12 \times 10^{-21}\text{ J}$) is twice that of Curve 1 ($6 \times 10^{-21}\text{ J}$), so the $\text{He}$ sample is at twice the Kelvin temperature: $2 \times 290\text{ K} = 580\text{ K}$. Choosing $290\text{ K}$ assumes that lighter atoms have more kinetic energy at the same temperature, which confuses a speed distribution with an energy distribution. Choosing $1160\text{ K}$ treats energy as proportional to the square root of temperature, which is true of average speed, not kinetic energy. Choosing $145\text{ K}$ inverts the relationship.",
    },
    {
        "unit_q_num": 63,
        "topic_code": "3.5",
        "topic_title": "Kinetic Molecular Theory",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"Two identical rigid containers are held at $300\text{ K}$. One contains $0.50\text{ mol}$ of $\text{He}(g)$, and the other contains $0.50\text{ mol}$ of $\text{Ar}(g)$. Both gases behave ideally, so the two pressures are equal, even though the average speed of the $\text{He}$ atoms is more than three times the average speed of the $\text{Ar}$ atoms. Which of the following best explains, in terms of kinetic molecular theory, why the pressures are equal?",
        "options": [
            r"The $\text{He}$ atoms collide with the walls more often, but each collision of a more massive $\text{Ar}$ atom exerts a greater force on the wall; because both gases have the same average kinetic energy at $300\text{ K}$, the two effects balance.",
            r"The larger $\text{Ar}$ atoms occupy more of the volume of the container, so they collide with the walls just as often as the faster $\text{He}$ atoms do.",
            r"The faster $\text{He}$ atoms lose more kinetic energy in each collision with the walls, which reduces the force they exert to match the force exerted by the $\text{Ar}$ atoms.",
            r"Pressure results from collisions of gas atoms with one another rather than with the walls, and the larger $\text{Ar}$ atoms collide with one another more often, which makes up for their lower speed.",
        ],
        "correct_index": 0,
        "explanation": r"Gas pressure results from particles colliding with the walls of the container, so it depends on how often the particles strike the walls and how hard each collision pushes on the wall. At the same temperature, both gases have the same average kinetic energy, $\tfrac{1}{2}mv^2$. Because an $\text{He}$ atom has about one-tenth the mass of an $\text{Ar}$ atom, it must move faster (about $\sqrt{10} \approx 3.2$ times as fast) to have the same kinetic energy, so $\text{He}$ atoms strike the walls more often. Each $\text{Ar}$ atom, being more massive, pushes harder on the wall in each collision. These two effects exactly offset, so equal numbers of moles at the same $T$ and $V$ exert equal pressures. In an ideal gas the volume of the particles is negligible, and collisions with the walls are elastic, so no kinetic energy is lost. Collisions between gas particles do not by themselves produce the pressure on the walls.",
    },
    {
        "unit_q_num": 64,
        "topic_code": "3.6",
        "topic_title": "Deviation from Ideal Gas Law",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A rigid $2.00\text{ L}$ container holds $44.0\text{ g}$ of $\text{CO}_2(g)$ at $300\text{ K}$. The measured pressure of the gas is $11.6\text{ atm}$. Which of the following gives the pressure predicted by the ideal gas law and the best explanation for the difference between the measured and predicted pressures?",
        "options": [
            r"$11.2\text{ atm}$; the measured pressure is higher than predicted because the $\text{CO}_2$ molecules occupy part of the volume of the container.",
            r"$12.3\text{ atm}$; the measured pressure is lower than predicted because attractions between $\text{CO}_2$ molecules reduce the frequency and force of their collisions with the walls.",
            r"$12.3\text{ atm}$; the measured pressure is lower than predicted because the $\text{CO}_2$ molecules occupy part of the volume of the container.",
            r"$24.6\text{ atm}$; the measured pressure is lower than predicted because the $\text{CO}_2$ molecules move more slowly than ideal-gas particles at the same temperature.",
        ],
        "correct_index": 1,
        "explanation": r"The sample contains $44.0\text{ g} \div 44.01\text{ g/mol} = 1.00\text{ mol}$ of $\text{CO}_2$, so the ideal-gas pressure is $P = \dfrac{nRT}{V} = \dfrac{(1.00)(0.08206)(300)}{2.00} = 12.3\text{ atm}$. The measured pressure, $11.6\text{ atm}$, is lower. At this fairly high density, attractions between $\text{CO}_2$ molecules are significant: a molecule about to strike a wall is pulled back toward its neighbors, so the molecules hit the walls less often and with less force than ideal particles would. The volume of the molecules has the opposite effect: it reduces the free space in the container and makes the pressure higher, not lower, than predicted. The value $11.2\text{ atm}$ comes from using $273\text{ K}$ instead of $300\text{ K}$, and $24.6\text{ atm}$ comes from leaving out the $2.00\text{ L}$ volume. Average kinetic energy depends only on temperature, so real $\text{CO}_2$ molecules do not move more slowly on average than ideal particles at $300\text{ K}$.",
    },
    {
        "unit_q_num": 65,
        "topic_code": "3.6",
        "topic_title": "Deviation from Ideal Gas Law",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"A student determines the molar mass of butane, $\text{C}_4\text{H}_{10}$ (normal boiling point $-0.5^\circ\text{C}$), by filling a $1.000\text{ L}$ flask with the gas at $25.0^\circ\text{C}$ and $1.000\text{ atm}$ and measuring the mass of the gas, $2.448\text{ g}$. Using the ideal gas law, the student calculates a molar mass of $59.9\text{ g/mol}$, which is greater than the accepted value of $58.12\text{ g/mol}$. Assuming that all measurements were accurate, which of the following best explains why the experimental value is too high?",
        "options": [
            r"The volume of the butane molecules themselves is significant, so fewer molecules fit in the flask than the ideal gas law predicts.",
            r"Attractions between butane molecules are significant at conditions this close to its boiling point, so more molecules are in the flask at $1.000\text{ atm}$ than the ideal gas law predicts.",
            r"Butane molecules form hydrogen bonds with one another, so pairs of molecules behave as single particles with twice the molar mass.",
            r"At $25.0^\circ\text{C}$, butane molecules have a greater average kinetic energy than ideal-gas particles, so they exert a greater pressure than the ideal gas law predicts.",
        ],
        "correct_index": 1,
        "explanation": r"The student's calculation is $n = \dfrac{PV}{RT} = \dfrac{(1.000)(1.000)}{(0.08206)(298.2)} = 0.04087\text{ mol}$, so $M = 2.448\text{ g} \div 0.04087\text{ mol} = 59.9\text{ g/mol}$. At $25^\circ\text{C}$ and $1\text{ atm}$, butane is not far from the conditions at which it condenses, so the London dispersion attractions between its molecules are significant. These attractions reduce the pressure that a given number of molecules exerts, so more molecules (more mass) are needed to produce $1.000\text{ atm}$ than the ideal gas law predicts. The calculated number of moles is therefore too small, and the molar mass is too large. If molecular volume were the main effect, fewer molecules would be present and the molar mass would be too low. Butane is nonpolar and has no H bonded to N, O, or F, so it does not hydrogen bond. Average kinetic energy depends only on temperature; moreover, a greater pressure per molecule would also make the molar mass too low.",
    },

    # -------------------------------------------------------------------------
    # Added 2026-10-03 — Blind-spot coverage (Fall 2024 CED): topics 3.7–3.13
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 66,
        "topic_code": "3.7",
        "topic_title": "Solutions and Mixtures",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table">
<thead><tr><th>Mixture</th><th>Physical State</th><th>Density of Sample from Top</th><th>Density of Sample from Middle</th><th>Density of Sample from Bottom</th></tr></thead>
<tbody>
<tr><td>1</td><td>Solid</td><td>$8.47\text{ g/cm}^3$</td><td>$8.47\text{ g/cm}^3$</td><td>$8.47\text{ g/cm}^3$</td></tr>
<tr><td>2</td><td>Liquid</td><td>$1.02\text{ g/mL}$</td><td>$1.09\text{ g/mL}$</td><td>$1.31\text{ g/mL}$</td></tr>
<tr><td>3</td><td>Gas</td><td>$1.18\text{ g/L}$</td><td>$1.18\text{ g/L}$</td><td>$1.18\text{ g/L}$</td></tr>
<tr><td>4</td><td>Liquid</td><td>$1.07\text{ g/mL}$</td><td>$1.07\text{ g/mL}$</td><td>$1.07\text{ g/mL}$</td></tr>
</tbody>
</table>""",
        "question": r"A student measures the density of samples taken from the top, middle, and bottom of each of four different mixtures kept at constant temperature. The results are shown in the table above. Based on the data, which of the mixtures are best classified as solutions (homogeneous mixtures)?",
        "options": [
            r"Mixture 4 only",
            r"Mixtures 3 and 4 only",
            r"Mixtures 1 and 4 only",
            r"Mixtures 1, 3, and 4",
        ],
        "correct_index": 3,
        "explanation": r"In a solution, macroscopic properties such as density are the same throughout the sample; in a heterogeneous mixture they depend on location. Mixtures 1, 3, and 4 have the same density at every location, so each is a solution. The density of mixture 2 increases toward the bottom, so it is a heterogeneous mixture (for example, a suspension whose particles are settling). Solutions can be solids, liquids, or gases: mixture 1 is a solid solution (an alloy such as brass), and mixture 3 is a gaseous solution (such as air). Choices that leave out the solid or the gas reflect the misconception that only liquids can be solutions.",
    },
    {
        "unit_q_num": 67,
        "topic_code": "3.7",
        "topic_title": "Solutions and Mixtures",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"How many potassium ions, $\text{K}^+$, are present in $20.0\text{ mL}$ of $0.250\text{ M } \text{K}_3\text{PO}_4(aq)$? (Avogadro's number $= 6.022 \times 10^{23}\text{ mol}^{-1}$)",
        "options": [
            r"$3.01 \times 10^{21}$",
            r"$9.03 \times 10^{21}$",
            r"$1.20 \times 10^{22}$",
            r"$9.03 \times 10^{24}$",
        ],
        "correct_index": 1,
        "explanation": r"Moles of solute: $n = MV = (0.250\text{ mol/L})(0.0200\text{ L}) = 5.00 \times 10^{-3}\text{ mol K}_3\text{PO}_4$. Each formula unit releases three $\text{K}^+$ ions, so $n_{\text{K}^+} = 3(5.00 \times 10^{-3}\text{ mol}) = 1.50 \times 10^{-2}\text{ mol}$, and the number of ions is $(1.50 \times 10^{-2}\text{ mol})(6.022 \times 10^{23}\text{ mol}^{-1}) = 9.03 \times 10^{21}$. Stopping at formula units of $\text{K}_3\text{PO}_4$ gives $3.01 \times 10^{21}$; also counting the $\text{PO}_4^{3-}$ ions (four ions per formula unit) gives $1.20 \times 10^{22}$; and using $20.0$ instead of $0.0200\text{ L}$ gives an answer $1000$ times too large.",
    },
    {
        "unit_q_num": 68,
        "topic_code": "3.8",
        "topic_title": "Representations of Solutions",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 300" role="img" aria-label="Structural diagram of an acetone molecule, with a carbon-oxygen double bond and two methyl groups, surrounded by four water molecules. Dashed line 1 runs from a hydrogen atom of a water molecule to the oxygen atom of acetone. Dashed line 2 runs from a hydrogen atom of an acetone methyl group to the oxygen atom of a water molecule. Dashed line 3 runs from the oxygen atom of a water molecule to the oxygen atom of acetone. Dashed line 4 runs from a hydrogen atom of a water molecule to the central carbon atom of acetone." font-family="sans-serif">
  <line x1="295.3" y1="132.7" x2="324.7" y2="92.3" stroke="#111827" stroke-width="2"/>
  <line x1="295.3" y1="147.3" x2="324.7" y2="187.7" stroke="#111827" stroke-width="2"/>
  <line x1="322.7" y1="79.7" x2="301.7" y2="64.4" stroke="#111827" stroke-width="2"/>
  <line x1="335.3" y1="77.7" x2="350.6" y2="56.7" stroke="#111827" stroke-width="2"/>
  <line x1="337.3" y1="90.3" x2="358.3" y2="105.6" stroke="#111827" stroke-width="2"/>
  <line x1="337.3" y1="189.7" x2="358.3" y2="174.4" stroke="#111827" stroke-width="2"/>
  <line x1="335.3" y1="202.3" x2="350.6" y2="223.3" stroke="#111827" stroke-width="2"/>
  <line x1="322.7" y1="200.3" x2="301.7" y2="215.6" stroke="#111827" stroke-width="2"/>
  <line x1="118.6" y1="172.5" x2="132.1" y2="168.6" stroke="#111827" stroke-width="2"/>
  <line x1="110.3" y1="184" x2="110.7" y2="198" stroke="#111827" stroke-width="2"/>
  <line x1="437.5" y1="174.9" x2="446.2" y2="163.9" stroke="#111827" stroke-width="2"/>
  <line x1="437.5" y1="189.1" x2="446" y2="200.2" stroke="#111827" stroke-width="2"/>
  <line x1="177.9" y1="49.5" x2="166.9" y2="40.8" stroke="#111827" stroke-width="2"/>
  <line x1="192.1" y1="49.5" x2="203.2" y2="41" stroke="#111827" stroke-width="2"/>
  <line x1="219.7" y1="254.3" x2="227" y2="242.4" stroke="#111827" stroke-width="2"/>
  <line x1="206.4" y1="259.4" x2="193" y2="255.2" stroke="#111827" stroke-width="2"/>
  <line x1="239" y1="136" x2="281" y2="136" stroke="#111827" stroke-width="2"/>
  <line x1="239" y1="144" x2="281" y2="144" stroke="#111827" stroke-width="2"/>
  <line x1="145.5" y1="164.6" x2="221.4" y2="142.5" stroke="#2563eb" stroke-width="2" stroke-dasharray="6 4"/>
  <text x="179.5" y="145.1" font-size="14" text-anchor="middle" font-weight="bold" fill="#2563eb">1</text>
  <line x1="370.9" y1="171.5" x2="423.1" y2="180.5" stroke="#2563eb" stroke-width="2" stroke-dasharray="6 4"/>
  <text x="399.4" y="167.2" font-size="14" text-anchor="middle" font-weight="bold" fill="#2563eb">2</text>
  <line x1="189.2" y1="63" x2="225.8" y2="132" stroke="#2563eb" stroke-width="2" stroke-dasharray="6 4"/>
  <text x="195.1" y="109.1" font-size="14" text-anchor="middle" font-weight="bold" fill="#2563eb">3</text>
  <line x1="234.4" y1="230.5" x2="285.3" y2="147.7" stroke="#2563eb" stroke-width="2" stroke-dasharray="6 4"/>
  <text x="247.9" y="186.7" font-size="14" text-anchor="middle" font-weight="bold" fill="#2563eb">4</text>
  <text x="230" y="145" font-size="14" text-anchor="middle" fill="#111827">O</text>
  <text x="290" y="145" font-size="14" text-anchor="middle" fill="#111827">C</text>
  <text x="330" y="90" font-size="14" text-anchor="middle" fill="#111827">C</text>
  <text x="330" y="200" font-size="14" text-anchor="middle" fill="#111827">C</text>
  <text x="296" y="65.3" font-size="14" text-anchor="middle" fill="#111827">H</text>
  <text x="354.7" y="56" font-size="14" text-anchor="middle" fill="#111827">H</text>
  <text x="364" y="114.7" font-size="14" text-anchor="middle" fill="#111827">H</text>
  <text x="364" y="175.3" font-size="14" text-anchor="middle" fill="#111827">H</text>
  <text x="354.7" y="234" font-size="14" text-anchor="middle" fill="#111827">H</text>
  <text x="296" y="224.7" font-size="14" text-anchor="middle" fill="#111827">H</text>
  <text x="110" y="180" font-size="14" text-anchor="middle" fill="#111827">O</text>
  <text x="138.8" y="171.6" font-size="14" text-anchor="middle" fill="#111827">H</text>
  <text x="110.9" y="210" font-size="14" text-anchor="middle" fill="#111827">H</text>
  <text x="432" y="187" font-size="14" text-anchor="middle" fill="#111827">O</text>
  <text x="450.5" y="163.4" font-size="14" text-anchor="middle" fill="#111827">H</text>
  <text x="450.3" y="210.8" font-size="14" text-anchor="middle" fill="#111827">H</text>
  <text x="185" y="60" font-size="14" text-anchor="middle" fill="#111827">O</text>
  <text x="161.4" y="41.5" font-size="14" text-anchor="middle" fill="#111827">H</text>
  <text x="208.8" y="41.7" font-size="14" text-anchor="middle" fill="#111827">H</text>
  <text x="215" y="267" font-size="14" text-anchor="middle" fill="#111827">O</text>
  <text x="230.7" y="241.4" font-size="14" text-anchor="middle" fill="#111827">H</text>
  <text x="186.3" y="258.2" font-size="14" text-anchor="middle" fill="#111827">H</text>
</svg>
<figcaption>Figure: An acetone molecule and four nearby water molecules (lone pairs not shown). Dashed lines 1–4 are proposed attractions.</figcaption>
</figure>""",
        "question": r"The diagram above represents an acetone molecule, $\text{CH}_3\text{COCH}_3$, and four nearby water molecules in an aqueous solution. Each numbered dashed line connects the two atoms between which an attraction is proposed. Which dashed line correctly represents a hydrogen bond between acetone and water?",
        "options": [
            r"Dashed line 1",
            r"Dashed line 2",
            r"Dashed line 3",
            r"Dashed line 4",
        ],
        "correct_index": 0,
        "explanation": r"A hydrogen bond is an attraction between a hydrogen atom covalently bonded to N, O, or F (here, an $\text{O}-\text{H}$ hydrogen of water, $\delta^+$) and a lone pair on a small, highly electronegative atom (here, the oxygen atom of acetone, $\delta^-$). Only line 1, from a water hydrogen to the acetone oxygen, fits this description. Line 2 starts at a hydrogen atom of a methyl group; $\text{C}-\text{H}$ bonds are nearly nonpolar, so they do not form hydrogen bonds. Line 3 joins two oxygen atoms, which are both $\delta^-$ and repel each other. Line 4 joins a $\delta^+$ water hydrogen to the $\delta^+$ carbon atom of the $\text{C}=\text{O}$ group. Acetone molecules cannot hydrogen-bond to one another, but they accept hydrogen bonds from water, which helps explain why acetone is miscible with water.",
    },
    {
        "unit_q_num": 69,
        "topic_code": "3.8",
        "topic_title": "Representations of Solutions",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 550 330" role="img" aria-label="Five equal-sized square windows showing ions in solution, water molecules not shown. Original window (0.30 M sodium sulfate): 6 sodium ions and 3 sulfate ions. Window W: 4 sodium ions and 2 sulfate ions. Window X: 6 sodium ions and 3 sulfate ions. Window Y: 2 sodium ions and 1 sulfate ion. Window Z: 2 sodium ions and 2 sulfate ions." font-family="sans-serif">
  <text x="275" y="24" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">Original (0.30 M Na₂SO₄)</text>
  <rect x="220" y="34" width="110" height="110" fill="#e5e7eb" stroke="#374151" stroke-width="2"/>
  <circle cx="248" cy="62" r="13" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="248" y="66" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">2−</text>
  <circle cx="300" cy="84" r="13" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="300" y="88" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">2−</text>
  <circle cx="256" cy="116" r="13" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="256" y="120" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">2−</text>
  <circle cx="282" cy="52" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="282" y="56.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="310" cy="52" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="310" y="56.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="238" cy="90" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="238" y="94.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="275" cy="82" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="275" y="86.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="282" cy="118" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="282" y="122.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="308" cy="124" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="308" y="128.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="372" cy="62" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="372" y="66.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <text x="388" y="66.5" font-size="13" fill="#111827">= Na⁺</text>
  <circle cx="372" cy="96" r="13" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="372" y="100" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">2−</text>
  <text x="392" y="100.5" font-size="13" fill="#111827">= SO₄²⁻</text>
  <text x="360" y="134" font-size="12" fill="#374151">Water molecules not shown</text>
  <rect x="25" y="186" width="110" height="110" fill="#e5e7eb" stroke="#374151" stroke-width="2"/>
  <circle cx="57" cy="221" r="13" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="57" y="225" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">2−</text>
  <circle cx="103" cy="258" r="13" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="103" y="262" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">2−</text>
  <circle cx="103" cy="211" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="103" y="215.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="55" cy="271" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="55" y="275.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="80" cy="238" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="80" y="242.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="120" cy="231" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="120" y="235.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <text x="80" y="318" font-size="14" text-anchor="middle" font-weight="bold" fill="#111827">W</text>
  <rect x="155" y="186" width="110" height="110" fill="#e5e7eb" stroke="#374151" stroke-width="2"/>
  <circle cx="183" cy="214" r="13" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="183" y="218" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">2−</text>
  <circle cx="235" cy="236" r="13" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="235" y="240" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">2−</text>
  <circle cx="191" cy="268" r="13" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="191" y="272" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">2−</text>
  <circle cx="217" cy="204" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="217" y="208.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="245" cy="204" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="245" y="208.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="173" cy="242" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="173" y="246.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="210" cy="234" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="210" y="238.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="217" cy="270" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="217" y="274.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="243" cy="276" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="243" y="280.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <text x="210" y="318" font-size="14" text-anchor="middle" font-weight="bold" fill="#111827">X</text>
  <rect x="285" y="186" width="110" height="110" fill="#e5e7eb" stroke="#374151" stroke-width="2"/>
  <circle cx="341" cy="244" r="13" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="341" y="248" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">2−</text>
  <circle cx="313" cy="216" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="313" y="220.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="367" cy="270" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="367" y="274.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <text x="340" y="318" font-size="14" text-anchor="middle" font-weight="bold" fill="#111827">Y</text>
  <rect x="415" y="186" width="110" height="110" fill="#e5e7eb" stroke="#374151" stroke-width="2"/>
  <circle cx="450" cy="221" r="13" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="450" y="225" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">2−</text>
  <circle cx="491" cy="264" r="13" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="491" y="268" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">2−</text>
  <circle cx="495" cy="216" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="495" y="220.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="445" cy="268" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="445" y="272.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <text x="470" y="318" font-size="14" text-anchor="middle" font-weight="bold" fill="#111827">Z</text>
</svg>
<figcaption>Figure: Particulate views of equal small volumes of solution (water molecules not shown).</figcaption>
</figure>""",
        "question": r"The diagram labeled Original represents a small volume of $0.30\text{ M } \text{Na}_2\text{SO}_4(aq)$; water molecules are not shown. A $50.0\text{ mL}$ sample of this solution is diluted with distilled water to a total volume of $150.0\text{ mL}$ and mixed thoroughly. Which diagram best represents the same small volume of the diluted solution?",
        "options": [
            r"Diagram W",
            r"Diagram X",
            r"Diagram Y",
            r"Diagram Z",
        ],
        "correct_index": 2,
        "explanation": r"Diluting to three times the original volume lowers the concentration to one-third: $M_2 = \frac{(0.30\text{ M})(50.0\text{ mL})}{150.0\text{ mL}} = 0.10\text{ M}$. An equal small volume must therefore contain one-third as many solute particles, so the 6 $\text{Na}^+$ and 3 $\text{SO}_4^{2-}$ ions become 2 $\text{Na}^+$ and 1 $\text{SO}_4^{2-}$, as in diagram Y. This keeps the $2:1$ ratio required by the formula $\text{Na}_2\text{SO}_4$ and keeps the solution electrically neutral. Diagram X is identical to the original, which ignores that the same number of ions is now spread through three times the volume. Diagram W (4 $\text{Na}^+$ and 2 $\text{SO}_4^{2-}$) uses the factor $\frac{100.0}{150.0}$ (based on the volume of water added) instead of $\frac{50.0}{150.0}$. Diagram Z has equal numbers of $\text{Na}^+$ and $\text{SO}_4^{2-}$ ions, so it is not electrically neutral.",
    },
    {
        "unit_q_num": 70,
        "topic_code": "3.9",
        "topic_title": "Separation of Solutions and Mixtures",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 310" role="img" aria-label="Developed thin-layer chromatography plate beside a centimeter ruler whose zero mark is at the bottom edge of the plate. The baseline is at 1.0 cm, spot 1 is centered at 3.0 cm, spot 2 is centered at 7.0 cm, and the solvent front is at 9.0 cm." font-family="sans-serif">
  <rect x="196" y="4" width="40" height="300" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <line x1="224" y1="290" x2="236" y2="290" stroke="#374151" stroke-width="1.5"/>
  <text x="213" y="294" font-size="12" text-anchor="middle" fill="#111827">0</text>
  <line x1="230" y1="277" x2="236" y2="277" stroke="#374151" stroke-width="1.5"/>
  <line x1="224" y1="264" x2="236" y2="264" stroke="#374151" stroke-width="1.5"/>
  <text x="213" y="268" font-size="12" text-anchor="middle" fill="#111827">1</text>
  <line x1="230" y1="251" x2="236" y2="251" stroke="#374151" stroke-width="1.5"/>
  <line x1="224" y1="238" x2="236" y2="238" stroke="#374151" stroke-width="1.5"/>
  <text x="213" y="242" font-size="12" text-anchor="middle" fill="#111827">2</text>
  <line x1="230" y1="225" x2="236" y2="225" stroke="#374151" stroke-width="1.5"/>
  <line x1="224" y1="212" x2="236" y2="212" stroke="#374151" stroke-width="1.5"/>
  <text x="213" y="216" font-size="12" text-anchor="middle" fill="#111827">3</text>
  <line x1="230" y1="199" x2="236" y2="199" stroke="#374151" stroke-width="1.5"/>
  <line x1="224" y1="186" x2="236" y2="186" stroke="#374151" stroke-width="1.5"/>
  <text x="213" y="190" font-size="12" text-anchor="middle" fill="#111827">4</text>
  <line x1="230" y1="173" x2="236" y2="173" stroke="#374151" stroke-width="1.5"/>
  <line x1="224" y1="160" x2="236" y2="160" stroke="#374151" stroke-width="1.5"/>
  <text x="213" y="164" font-size="12" text-anchor="middle" fill="#111827">5</text>
  <line x1="230" y1="147" x2="236" y2="147" stroke="#374151" stroke-width="1.5"/>
  <line x1="224" y1="134" x2="236" y2="134" stroke="#374151" stroke-width="1.5"/>
  <text x="213" y="138" font-size="12" text-anchor="middle" fill="#111827">6</text>
  <line x1="230" y1="121" x2="236" y2="121" stroke="#374151" stroke-width="1.5"/>
  <line x1="224" y1="108" x2="236" y2="108" stroke="#374151" stroke-width="1.5"/>
  <text x="213" y="112" font-size="12" text-anchor="middle" fill="#111827">7</text>
  <line x1="230" y1="95" x2="236" y2="95" stroke="#374151" stroke-width="1.5"/>
  <line x1="224" y1="82" x2="236" y2="82" stroke="#374151" stroke-width="1.5"/>
  <text x="213" y="86" font-size="12" text-anchor="middle" fill="#111827">8</text>
  <line x1="230" y1="69" x2="236" y2="69" stroke="#374151" stroke-width="1.5"/>
  <line x1="224" y1="56" x2="236" y2="56" stroke="#374151" stroke-width="1.5"/>
  <text x="213" y="60" font-size="12" text-anchor="middle" fill="#111827">9</text>
  <line x1="230" y1="43" x2="236" y2="43" stroke="#374151" stroke-width="1.5"/>
  <line x1="224" y1="30" x2="236" y2="30" stroke="#374151" stroke-width="1.5"/>
  <text x="213" y="34" font-size="12" text-anchor="middle" fill="#111827">10</text>
  <text x="216" y="18" font-size="12" text-anchor="middle" fill="#111827">cm</text>
  <rect x="240" y="30" width="80" height="260" fill="#e5e7eb" stroke="#374151" stroke-width="2"/>
  <line x1="240" y1="56" x2="320" y2="56" stroke="#111827" stroke-width="1.5" stroke-dasharray="5 4"/>
  <line x1="240" y1="264" x2="320" y2="264" stroke="#111827" stroke-width="1.5"/>
  <ellipse cx="280" cy="108" rx="11" ry="7" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
  <ellipse cx="280" cy="212" rx="11" ry="7" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
  <text x="330" y="60.5" font-size="13" fill="#111827">Solvent front</text>
  <text x="330" y="112.5" font-size="13" fill="#111827">Spot 2</text>
  <text x="330" y="216.5" font-size="13" fill="#111827">Spot 1</text>
  <text x="330" y="268.5" font-size="13" fill="#111827">Baseline (sample applied here)</text>
</svg>
<figcaption>Figure: Developed TLC plate beside a centimeter ruler (0 cm = bottom edge of the plate).</figcaption>
</figure>""",
        "question": r"A mixture of two dyes was separated by thin-layer chromatography on a plate coated with polar silica gel, using a nonpolar mobile phase. The developed plate is shown above beside a centimeter ruler. Which spot was produced by the more polar dye, and what is the retention factor, $R_f$, of that spot?",
        "options": [
            r"Spot 1; $R_f = 0.33$",
            r"Spot 1; $R_f = 0.25$",
            r"Spot 2; $R_f = 0.75$",
            r"Spot 2; $R_f = 0.78$",
        ],
        "correct_index": 1,
        "explanation": r"$R_f = \frac{\text{distance traveled by the spot}}{\text{distance traveled by the solvent}}$, with both distances measured from the baseline, where the sample was applied. The baseline is at $1.0\text{ cm}$ and the solvent front is at $9.0\text{ cm}$, so the solvent traveled $8.0\text{ cm}$. Spot 1 (at $3.0\text{ cm}$) traveled $2.0\text{ cm}$, so $R_f = 2.0/8.0 = 0.25$; spot 2 (at $7.0\text{ cm}$) traveled $6.0\text{ cm}$, so $R_f = 0.75$. The more polar dye is attracted more strongly to the polar silica (dipole–dipole forces and hydrogen bonding) and less strongly to the nonpolar mobile phase, so it travels the shorter distance: spot 1. Measuring from the bottom edge of the plate instead of from the baseline gives the incorrect values $3.0/9.0 = 0.33$ and $7.0/9.0 = 0.78$.",
    },
    {
        "unit_q_num": 71,
        "topic_code": "3.9",
        "topic_title": "Separation of Solutions and Mixtures",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A student uses thin-layer chromatography with a polar silica gel stationary phase to separate a mixture of two polar compounds. With pure hexane, $\text{C}_6\text{H}_{14}$, as the mobile phase, both compounds stay very close to the baseline, with $R_f$ values less than $0.05$. Which change to the procedure would most likely increase the $R_f$ values of both compounds?",
        "options": [
            r"Using a longer TLC plate so that the solvent front travels a greater distance",
            r"Using a stationary phase that is more polar than silica gel",
            r"Applying a larger, more concentrated spot of the mixture to the baseline",
            r"Using a mobile phase that is more polar than hexane, such as ethyl acetate, $\text{CH}_3\text{COOCH}_2\text{CH}_3$",
        ],
        "correct_index": 3,
        "explanation": r"How far each compound travels depends on the competition between its attraction to the stationary phase and its attraction to the mobile phase. The polar compounds are held strongly by the polar silica (dipole–dipole forces and hydrogen bonding), while nonpolar hexane attracts them only through weak London dispersion forces. A more polar mobile phase, such as ethyl acetate, forms dipole–dipole attractions with the compounds and competes with them for the polar sites on the silica. The compounds then spend more time in the mobile phase and travel farther, so their $R_f$ values increase. Because $R_f$ is a ratio of distances, a longer plate does not change it. A more polar stationary phase would hold the compounds even more strongly and lower $R_f$. Overloading the spot causes streaking but does not raise $R_f$.",
    },
    {
        "unit_q_num": 72,
        "topic_code": "3.9",
        "topic_title": "Separation of Solutions and Mixtures",
        "difficulty": "Challenging",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 540 336" role="img" aria-label="Graph of vapor temperature in degrees Celsius versus volume of distillate collected in milliliters, from 0 to 100 mL. The temperature stays constant at 36 degrees from 0 to about 37 mL, rises steeply between about 37 and 46 mL (passing the midpoint of the rise at about 41 mL), and then stays constant at 98 degrees from about 46 mL to 100 mL." font-family="sans-serif">
  <line x1="113" y1="290" x2="113" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="156" y1="290" x2="156" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="199" y1="290" x2="199" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="242" y1="290" x2="242" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="285" y1="290" x2="285" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="328" y1="290" x2="328" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="371" y1="290" x2="371" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="414" y1="290" x2="414" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="457" y1="290" x2="457" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="500" y1="290" x2="500" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="70" y1="261.1" x2="500" y2="261.1" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="70" y1="232.2" x2="500" y2="232.2" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="70" y1="203.3" x2="500" y2="203.3" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="70" y1="174.4" x2="500" y2="174.4" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="70" y1="145.6" x2="500" y2="145.6" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="70" y1="116.7" x2="500" y2="116.7" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="70" y1="87.8" x2="500" y2="87.8" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="70" y1="58.9" x2="500" y2="58.9" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="70" y1="30" x2="500" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="70" y1="290" x2="500" y2="290" stroke="#111827" stroke-width="2"/>
  <line x1="70" y1="290" x2="70" y2="30" stroke="#111827" stroke-width="2"/>
  <line x1="70" y1="290" x2="70" y2="295" stroke="#111827" stroke-width="1.5"/>
  <text x="70" y="307" font-size="12" text-anchor="middle" fill="#111827">0</text>
  <line x1="113" y1="290" x2="113" y2="295" stroke="#111827" stroke-width="1.5"/>
  <text x="113" y="307" font-size="12" text-anchor="middle" fill="#111827">10</text>
  <line x1="156" y1="290" x2="156" y2="295" stroke="#111827" stroke-width="1.5"/>
  <text x="156" y="307" font-size="12" text-anchor="middle" fill="#111827">20</text>
  <line x1="199" y1="290" x2="199" y2="295" stroke="#111827" stroke-width="1.5"/>
  <text x="199" y="307" font-size="12" text-anchor="middle" fill="#111827">30</text>
  <line x1="242" y1="290" x2="242" y2="295" stroke="#111827" stroke-width="1.5"/>
  <text x="242" y="307" font-size="12" text-anchor="middle" fill="#111827">40</text>
  <line x1="285" y1="290" x2="285" y2="295" stroke="#111827" stroke-width="1.5"/>
  <text x="285" y="307" font-size="12" text-anchor="middle" fill="#111827">50</text>
  <line x1="328" y1="290" x2="328" y2="295" stroke="#111827" stroke-width="1.5"/>
  <text x="328" y="307" font-size="12" text-anchor="middle" fill="#111827">60</text>
  <line x1="371" y1="290" x2="371" y2="295" stroke="#111827" stroke-width="1.5"/>
  <text x="371" y="307" font-size="12" text-anchor="middle" fill="#111827">70</text>
  <line x1="414" y1="290" x2="414" y2="295" stroke="#111827" stroke-width="1.5"/>
  <text x="414" y="307" font-size="12" text-anchor="middle" fill="#111827">80</text>
  <line x1="457" y1="290" x2="457" y2="295" stroke="#111827" stroke-width="1.5"/>
  <text x="457" y="307" font-size="12" text-anchor="middle" fill="#111827">90</text>
  <line x1="500" y1="290" x2="500" y2="295" stroke="#111827" stroke-width="1.5"/>
  <text x="500" y="307" font-size="12" text-anchor="middle" fill="#111827">100</text>
  <line x1="65" y1="290" x2="70" y2="290" stroke="#111827" stroke-width="1.5"/>
  <text x="61" y="294" font-size="12" text-anchor="end" fill="#111827">20</text>
  <line x1="65" y1="261.1" x2="70" y2="261.1" stroke="#111827" stroke-width="1.5"/>
  <text x="61" y="265.1" font-size="12" text-anchor="end" fill="#111827">30</text>
  <line x1="65" y1="232.2" x2="70" y2="232.2" stroke="#111827" stroke-width="1.5"/>
  <text x="61" y="236.2" font-size="12" text-anchor="end" fill="#111827">40</text>
  <line x1="65" y1="203.3" x2="70" y2="203.3" stroke="#111827" stroke-width="1.5"/>
  <text x="61" y="207.3" font-size="12" text-anchor="end" fill="#111827">50</text>
  <line x1="65" y1="174.4" x2="70" y2="174.4" stroke="#111827" stroke-width="1.5"/>
  <text x="61" y="178.4" font-size="12" text-anchor="end" fill="#111827">60</text>
  <line x1="65" y1="145.6" x2="70" y2="145.6" stroke="#111827" stroke-width="1.5"/>
  <text x="61" y="149.6" font-size="12" text-anchor="end" fill="#111827">70</text>
  <line x1="65" y1="116.7" x2="70" y2="116.7" stroke="#111827" stroke-width="1.5"/>
  <text x="61" y="120.7" font-size="12" text-anchor="end" fill="#111827">80</text>
  <line x1="65" y1="87.8" x2="70" y2="87.8" stroke="#111827" stroke-width="1.5"/>
  <text x="61" y="91.8" font-size="12" text-anchor="end" fill="#111827">90</text>
  <line x1="65" y1="58.9" x2="70" y2="58.9" stroke="#111827" stroke-width="1.5"/>
  <text x="61" y="62.9" font-size="12" text-anchor="end" fill="#111827">100</text>
  <line x1="65" y1="30" x2="70" y2="30" stroke="#111827" stroke-width="1.5"/>
  <text x="61" y="34" font-size="12" text-anchor="end" fill="#111827">110</text>
  <text x="285" y="328" font-size="13" text-anchor="middle" fill="#111827">Volume of distillate collected (mL)</text>
  <text x="22" y="160" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 22 160)">Vapor temperature (°C)</text>
  <polyline points="70,243.8 78.6,243.8 87.2,243.8 95.8,243.8 104.4,243.8 113,243.8 121.6,243.8 130.2,243.8 138.8,243.8 147.4,243.8 156,243.8 164.6,243.8 173.2,243.8 181.8,243.8 190.4,243.8 199,243.8 207.6,243.7 216.2,243.5 218.3,243.3 220.5,243 222.7,242.6 224.8,241.9 226.9,240.8 229.1,239.2 231.2,236.6 233.4,232.8 235.5,227 237.7,218.8 239.8,207.3 242,192.3 244.2,174.2 246.3,154.2 248.4,134.2 250.6,116.1 252.8,101.1 254.9,89.7 257,81.4 259.2,75.7 261.4,71.8 263.5,69.3 265.6,67.6 267.8,66.5 269.9,65.9 272.1,65.4 274.2,65.2 276.4,65 285,64.7 293.6,64.7 302.2,64.7 310.8,64.7 319.4,64.7 328,64.7 336.6,64.7 345.2,64.7 353.8,64.7 362.4,64.7 371,64.7 379.6,64.7 388.2,64.7 396.8,64.7 405.4,64.7 414,64.7 422.6,64.7 431.2,64.7 439.8,64.7 448.4,64.7 457,64.7 465.6,64.7 474.2,64.7 482.8,64.7 491.4,64.7 500,64.7" fill="none" stroke="#111827" stroke-width="2.5" stroke-linejoin="round"/>
  <text x="147.4" y="234.8" font-size="13" text-anchor="middle" fill="#374151">36 °C</text>
  <text x="379.6" y="55.7" font-size="13" text-anchor="middle" fill="#374151">98 °C</text>
</svg>
<figcaption>Figure: Fractional distillation curve for the pentane–heptane mixture.</figcaption>
</figure>""",
        "question": r"A $100.\text{ mL}$ mixture of pentane, $\text{C}_5\text{H}_{12}$, and heptane, $\text{C}_7\text{H}_{16}$, is separated by fractional distillation. The temperature of the vapor at the top of the fractionating column is recorded as distillate is collected, giving the graph above. Approximately what volume of heptane was in the original mixture, and why does heptane distill at the higher temperature?",
        "options": [
            r"About $60\text{ mL}$; heptane molecules have more electrons and a larger surface area, so their stronger London dispersion forces give heptane a lower vapor pressure.",
            r"About $40\text{ mL}$; heptane molecules have more electrons and a larger surface area, so their stronger London dispersion forces give heptane a lower vapor pressure.",
            r"About $60\text{ mL}$; heptane molecules are polar, so dipole–dipole attractions give heptane a lower vapor pressure than nonpolar pentane.",
            r"About $40\text{ mL}$; more energy is needed to break the greater number of $\text{C}-\text{C}$ and $\text{C}-\text{H}$ covalent bonds in each heptane molecule.",
        ],
        "correct_index": 0,
        "explanation": r"The first plateau (about $36^\circ\text{C}$) is pentane distilling, and it lasts until about $40\text{ mL}$ of distillate has been collected. The second plateau (about $98^\circ\text{C}$) is heptane, collected from about $40\text{ mL}$ to $100\text{ mL}$. So the mixture contained about $40\text{ mL}$ of pentane and about $60\text{ mL}$ of heptane. Both compounds are nonpolar, so only London dispersion forces act between their molecules. Heptane has more electrons ($58$ versus $42$), a more polarizable electron cloud, and more surface contact between molecules, so its dispersion forces are stronger. Its vapor pressure is therefore lower, and a higher temperature is needed to boil it. Distillation separates intact molecules; no covalent bonds are broken.",
    },
    {
        "unit_q_num": 73,
        "topic_code": "3.10",
        "topic_title": "Solubility",
        "difficulty": "Challenging",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 555 296" role="img" aria-label="Four beakers, W, X, Y, and Z, each containing an upper liquid layer and a lower liquid layer. W: upper layer empty; lower layer contains iodine molecules and separate sodium and chloride ions. X: upper layer contains iodine molecules; lower layer contains separate sodium and chloride ions. Y: upper layer contains separate sodium and chloride ions; lower layer contains iodine molecules. Z: upper layer contains iodine molecules; lower layer contains sodium and chloride ions paired together." font-family="sans-serif">
  <rect x="21" y="138" width="108" height="83" fill="#e5e7eb" stroke="none"/>
  <line x1="21" y1="60" x2="129" y2="60" stroke="#374151" stroke-width="1.5"/>
  <line x1="21" y1="138" x2="129" y2="138" stroke="#374151" stroke-width="1.5"/>
  <path d="M20,40 L20,222 L130,222 L130,40" fill="none" stroke="#374151" stroke-width="2"/>
  <circle cx="38" cy="155" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="50" cy="155" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="68" cy="180" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="80" cy="180" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="102" cy="205" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="114" cy="205" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="72" cy="155" r="7" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="72" y="159" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="108" cy="180" r="7" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="108" y="184" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="50" cy="205" r="7" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="50" y="209" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="100" cy="155" r="10" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="100" y="159.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">−</text>
  <circle cx="40" cy="180" r="10" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="40" y="184.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">−</text>
  <circle cx="78" cy="205" r="10" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="78" y="209.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">−</text>
  <text x="75" y="246" font-size="14" text-anchor="middle" font-weight="bold" fill="#111827">W</text>
  <rect x="156" y="138" width="108" height="83" fill="#e5e7eb" stroke="none"/>
  <line x1="156" y1="60" x2="264" y2="60" stroke="#374151" stroke-width="1.5"/>
  <line x1="156" y1="138" x2="264" y2="138" stroke="#374151" stroke-width="1.5"/>
  <path d="M155,40 L155,222 L265,222 L265,40" fill="none" stroke="#374151" stroke-width="2"/>
  <circle cx="179" cy="85" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="191" cy="85" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="227" cy="82" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="239" cy="82" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="203" cy="115" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="215" cy="115" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="215" cy="152" r="7" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="215" y="156" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="173" cy="190" r="7" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="173" y="194" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="235" cy="202" r="7" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="235" y="206" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="180" cy="155" r="10" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="180" y="159.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">−</text>
  <circle cx="241" cy="170" r="10" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="241" y="174.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">−</text>
  <circle cx="200" cy="200" r="10" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="200" y="204.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">−</text>
  <text x="210" y="246" font-size="14" text-anchor="middle" font-weight="bold" fill="#111827">X</text>
  <rect x="291" y="138" width="108" height="83" fill="#e5e7eb" stroke="none"/>
  <line x1="291" y1="60" x2="399" y2="60" stroke="#374151" stroke-width="1.5"/>
  <line x1="291" y1="138" x2="399" y2="138" stroke="#374151" stroke-width="1.5"/>
  <path d="M290,40 L290,222 L400,222 L400,40" fill="none" stroke="#374151" stroke-width="2"/>
  <circle cx="350" cy="75" r="7" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="350" y="79" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="308" cy="112" r="7" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="308" y="116" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="370" cy="122" r="7" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="370" y="126" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="315" cy="78" r="10" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="315" y="82.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">−</text>
  <circle cx="376" cy="92" r="10" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="376" y="96.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">−</text>
  <circle cx="335" cy="120" r="10" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="335" y="124.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">−</text>
  <circle cx="314" cy="158" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="326" cy="158" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="364" cy="165" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="376" cy="165" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="339" cy="198" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="351" cy="198" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <text x="345" y="246" font-size="14" text-anchor="middle" font-weight="bold" fill="#111827">Y</text>
  <rect x="426" y="138" width="108" height="83" fill="#e5e7eb" stroke="none"/>
  <line x1="426" y1="60" x2="534" y2="60" stroke="#374151" stroke-width="1.5"/>
  <line x1="426" y1="138" x2="534" y2="138" stroke="#374151" stroke-width="1.5"/>
  <path d="M425,40 L425,222 L535,222 L535,40" fill="none" stroke="#374151" stroke-width="2"/>
  <circle cx="449" cy="85" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="461" cy="85" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="497" cy="82" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="509" cy="82" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="473" cy="115" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="485" cy="115" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="447" cy="158" r="7" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="447" y="162" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="463" cy="158" r="10" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="463" y="162.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">−</text>
  <circle cx="491" cy="170" r="7" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="491" y="174" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="507" cy="170" r="10" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="507" y="174.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">−</text>
  <circle cx="455" cy="200" r="7" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="455" y="204" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <circle cx="471" cy="200" r="10" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="471" y="204.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">−</text>
  <text x="480" y="246" font-size="14" text-anchor="middle" font-weight="bold" fill="#111827">Z</text>
  <circle cx="38" cy="276" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <circle cx="50" cy="276" r="7" fill="#374151" stroke="#111827" stroke-width="1.5"/>
  <text x="62" y="280.5" font-size="13" fill="#111827">I₂</text>
  <circle cx="112" cy="276" r="7" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="112" y="280" font-size="12" text-anchor="middle" font-weight="bold" fill="#111827">+</text>
  <text x="124" y="280.5" font-size="13" fill="#111827">Na⁺</text>
  <circle cx="178" cy="276" r="10" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
  <text x="178" y="280.5" font-size="13" text-anchor="middle" font-weight="bold" fill="#111827">−</text>
  <text x="194" y="280.5" font-size="13" fill="#111827">Cl⁻</text>
  <text x="250" y="280.5" font-size="12" fill="#374151">Water and hexane molecules are not shown.</text>
</svg>
<figcaption>Figure: Possible distributions of solute particles after shaking (solvent molecules not shown).</figcaption>
</figure>""",
        "question": r"Solid $\text{NaCl}$ and solid $\text{I}_2$ are added to a separatory funnel containing water (density $1.00\text{ g/mL}$) and hexane, $\text{C}_6\text{H}_{14}$ (density $0.66\text{ g/mL}$). Water and hexane are immiscible. The funnel is shaken, and the liquids are allowed to separate into two layers. Which diagram above best represents the distribution of the dissolved solute particles?",
        "options": [
            r"Diagram W",
            r"Diagram X",
            r"Diagram Y",
            r"Diagram Z",
        ],
        "correct_index": 1,
        "explanation": r"Hexane is less dense than water, so hexane forms the upper layer and water forms the lower layer. Nonpolar $\text{I}_2$ molecules attract hexane molecules through London dispersion forces, similar to the attractions within each pure substance. To dissolve in water, $\text{I}_2$ would have to disrupt strong hydrogen bonds between water molecules while forming only weak attractions to water, so most of the $\text{I}_2$ goes into the upper (hexane) layer. $\text{NaCl}$ dissolves as separate $\text{Na}^+$ and $\text{Cl}^-$ ions, each held by strong ion–dipole attractions to polar water molecules. Nonpolar hexane cannot attract ions strongly enough to separate them, so the ions are in the lower layer, as in diagram X. Diagram Y would be correct only if water floated on top of the less dense hexane, diagram W puts the $\text{I}_2$ in the water, and diagram Z shows $\text{Na}^+$ and $\text{Cl}^-$ ions still paired, but dissolved $\text{NaCl}$ exists as separate hydrated ions.",
    },
    {
        "unit_q_num": 74,
        "topic_code": "3.10",
        "topic_title": "Solubility",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table">
<thead><tr><th>Solute</th><th>Solvent</th><th>Observed Solubility at $25^\circ\text{C}$</th></tr></thead>
<tbody>
<tr><td>$\text{I}_2$ (nonpolar)</td><td>Hexane (nonpolar)</td><td>Soluble</td></tr>
<tr><td>$\text{I}_2$ (nonpolar)</td><td>Water (polar)</td><td>Slightly soluble ($0.03\text{ g}$ per $100\text{ g}$ of water)</td></tr>
<tr><td>$\text{NaCl}$ (ionic)</td><td>Water (polar)</td><td>Very soluble ($36\text{ g}$ per $100\text{ g}$ of water)</td></tr>
<tr><td>$\text{NaCl}$ (ionic)</td><td>Hexane (nonpolar)</td><td>Practically insoluble</td></tr>
<tr><td>$\text{AgCl}$ (ionic)</td><td>Water (polar)</td><td>Practically insoluble ($0.0002\text{ g}$ per $100\text{ g}$ of water)</td></tr>
<tr><td>Ethanol, $\text{C}_2\text{H}_5\text{OH}$ (polar)</td><td>Water (polar)</td><td>Miscible in all proportions</td></tr>
</tbody>
</table>""",
        "question": r"A student proposes the following model: 'Polar and ionic solutes dissolve in polar solvents, and nonpolar solutes dissolve in nonpolar solvents.' Which observation in the table above is LEAST consistent with the student's model?",
        "options": [
            r"$\text{I}_2$ is much more soluble in hexane than in water.",
            r"Ethanol and water are miscible in all proportions.",
            r"$\text{AgCl}$ is practically insoluble in water.",
            r"$\text{NaCl}$ is practically insoluble in hexane.",
        ],
        "correct_index": 2,
        "explanation": r"The model accounts for most of the data. Nonpolar $\text{I}_2$ dissolves far better in nonpolar hexane (London dispersion forces) than in polar water; polar ethanol forms hydrogen bonds with water; and nonpolar hexane cannot separate the ions of $\text{NaCl}$. However, $\text{AgCl}$ is ionic, so the model predicts that it should dissolve in polar water, as $\text{NaCl}$ does ($36\text{ g}$ per $100\text{ g}$ of water). Instead, its solubility is more than 100,000 times lower. Whether a solid dissolves depends on how the attractions that must be overcome (here, the strong attractions between $\text{Ag}^+$ and $\text{Cl}^-$ ions in the solid) compare with the solute–solvent attractions that form (ion–dipole attractions to water). The model considers only whether the solute and solvent have similar types of interactions, not how strong the solute–solute attractions are, so it cannot predict that some ionic solids are nearly insoluble in water.",
    },
    {
        "unit_q_num": 75,
        "topic_code": "3.11",
        "topic_title": "Spectroscopy and the Electromagnetic Spectrum",
        "difficulty": "Challenging",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 540 340" role="img" aria-label="Energy-level diagram of a molecule. A ground electronic state has vibrational levels v = 0, 1, and 2, with closely spaced thin rotational levels above v = 0 and v = 1. Much higher is an excited electronic state with vibrational levels v = 0 and 1. Arrow X points upward between two neighboring rotational levels of v = 0. Arrow Y points upward from v = 0 to v = 1 of the ground electronic state. Arrow Z points downward from v = 0 of the excited electronic state to v = 0 of the ground electronic state." font-family="sans-serif">
  <line x1="40" y1="310" x2="40" y2="26" stroke="#111827" stroke-width="2"/>
  <polygon points="40,18 44.5,26 35.5,26" fill="#111827"/>
  <text x="26" y="170" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 26 170)">Energy</text>
  <line x1="170" y1="300" x2="400" y2="300" stroke="#111827" stroke-width="2.5"/>
  <text x="408" y="304.5" font-size="12" fill="#111827">v = 0</text>
  <line x1="200" y1="284" x2="370" y2="284" stroke="#9ca3af" stroke-width="1.5"/>
  <line x1="200" y1="254" x2="370" y2="254" stroke="#9ca3af" stroke-width="1.5"/>
  <line x1="170" y1="230" x2="400" y2="230" stroke="#111827" stroke-width="2.5"/>
  <text x="408" y="234.5" font-size="12" fill="#111827">v = 1</text>
  <line x1="200" y1="214" x2="370" y2="214" stroke="#9ca3af" stroke-width="1.5"/>
  <line x1="200" y1="184" x2="370" y2="184" stroke="#9ca3af" stroke-width="1.5"/>
  <line x1="170" y1="160" x2="400" y2="160" stroke="#111827" stroke-width="2.5"/>
  <text x="408" y="164.5" font-size="12" fill="#111827">v = 2</text>
  <line x1="170" y1="80" x2="400" y2="80" stroke="#111827" stroke-width="2.5"/>
  <text x="408" y="84.5" font-size="12" fill="#111827">v = 0</text>
  <line x1="200" y1="70" x2="370" y2="70" stroke="#9ca3af" stroke-width="1.5"/>
  <line x1="200" y1="52" x2="370" y2="52" stroke="#9ca3af" stroke-width="1.5"/>
  <line x1="170" y1="30" x2="400" y2="30" stroke="#111827" stroke-width="2.5"/>
  <text x="408" y="34.5" font-size="12" fill="#111827">v = 1</text>
  <line x1="158" y1="26" x2="158" y2="84" stroke="#374151" stroke-width="1.5"/>
  <line x1="158" y1="26" x2="164" y2="26" stroke="#374151" stroke-width="1.5"/>
  <line x1="158" y1="84" x2="164" y2="84" stroke="#374151" stroke-width="1.5"/>
  <line x1="158" y1="156" x2="158" y2="304" stroke="#374151" stroke-width="1.5"/>
  <line x1="158" y1="156" x2="164" y2="156" stroke="#374151" stroke-width="1.5"/>
  <line x1="158" y1="304" x2="164" y2="304" stroke="#374151" stroke-width="1.5"/>
  <text x="104" y="50" font-size="12" text-anchor="middle" fill="#111827">Excited</text>
  <text x="104" y="66" font-size="12" text-anchor="middle" fill="#111827">electronic state</text>
  <text x="104" y="226" font-size="12" text-anchor="middle" fill="#111827">Ground</text>
  <text x="104" y="242" font-size="12" text-anchor="middle" fill="#111827">electronic state</text>
  <line x1="215" y1="300" x2="215" y2="291" stroke="#2563eb" stroke-width="2"/>
  <polygon points="215,284 219,291 211,291" fill="#2563eb"/>
  <text x="206" y="297" font-size="14" text-anchor="end" font-weight="bold" fill="#2563eb">X</text>
  <line x1="280" y1="300" x2="280" y2="238" stroke="#2563eb" stroke-width="2"/>
  <polygon points="280,230 284.5,238 275.5,238" fill="#2563eb"/>
  <text x="271" y="270" font-size="14" text-anchor="end" font-weight="bold" fill="#2563eb">Y</text>
  <line x1="345" y1="80" x2="345" y2="292" stroke="#2563eb" stroke-width="2"/>
  <polygon points="345,300 340.5,292 349.5,292" fill="#2563eb"/>
  <text x="354" y="196" font-size="14" font-weight="bold" fill="#2563eb">Z</text>
  <text x="270" y="330" font-size="12" text-anchor="middle" fill="#111827">Thick lines: vibrational levels (v). Thin lines: rotational levels (only some shown).</text>
</svg>
<figcaption>Figure: Some energy levels of a gaseous molecule (spacings not to scale) with transitions X, Y, and Z.</figcaption>
</figure>""",
        "question": r"The diagram above represents some energy levels of a gaseous molecule. Each electronic state contains vibrational levels (thick lines), and each vibrational level contains closely spaced rotational levels (thin lines). The spacings are qualitatively correct but not drawn to scale. Which of the following correctly describes the photon absorbed or emitted in each of the transitions X, Y, and Z?",
        "options": [
            r"X: a microwave photon is absorbed; Y: an infrared photon is absorbed; Z: an ultraviolet or visible photon is emitted.",
            r"X: an infrared photon is absorbed; Y: a microwave photon is absorbed; Z: an ultraviolet or visible photon is emitted.",
            r"X: a microwave photon is absorbed; Y: an infrared photon is absorbed; Z: an ultraviolet or visible photon is absorbed.",
            r"X: an ultraviolet or visible photon is absorbed; Y: an infrared photon is absorbed; Z: a microwave photon is emitted.",
        ],
        "correct_index": 0,
        "explanation": r"The energy of the photon, $E = h\nu = \frac{hc}{\lambda}$, equals the energy difference between the two levels. Transition X, between neighboring rotational levels, has the smallest energy gap and corresponds to a microwave photon (lowest energy, longest wavelength). Transition Y, between vibrational levels of the same electronic state, has an intermediate gap and corresponds to an infrared photon. Transition Z, between two electronic states, has the largest gap and corresponds to an ultraviolet or visible photon. X and Y point upward, so the molecule gains energy by absorbing a photon; Z points downward, so the molecule loses energy by emitting a photon. Swapping the microwave and infrared assignments reverses the order of the rotational and vibrational energy gaps, assigning an ultraviolet or visible photon to X gives the most energetic photon to the smallest gap, and calling Z an absorption ignores the direction of the arrow.",
    },
    {
        "unit_q_num": 76,
        "topic_code": "3.11",
        "topic_title": "Spectroscopy and the Electromagnetic Spectrum",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 560 156" role="img" aria-label="Electromagnetic spectrum drawn on a logarithmic wavelength scale from 10 to the minus 8 meters to 1 meter. Ultraviolet spans 10 to the minus 8 to 4 times 10 to the minus 7 meters, visible spans 4 times 10 to the minus 7 to 7 times 10 to the minus 7 meters, infrared spans 7 times 10 to the minus 7 to 10 to the minus 3 meters, and microwave spans 10 to the minus 3 to 1 meter." font-family="sans-serif">
  <rect x="40" y="50" width="96.1" height="40" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="88.1" y="74.5" font-size="13" text-anchor="middle" fill="#111827">Ultraviolet</text>
  <rect x="136.1" y="50" width="14.6" height="40" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
  <rect x="150.7" y="50" width="189.3" height="40" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
  <text x="245.4" y="74.5" font-size="13" text-anchor="middle" fill="#111827">Infrared</text>
  <rect x="340" y="50" width="180" height="40" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
  <text x="430" y="74.5" font-size="13" text-anchor="middle" fill="#111827">Microwave</text>
  <line x1="143.4" y1="37" x2="143.4" y2="50" stroke="#374151" stroke-width="1.5"/>
  <text x="143.4" y="31" font-size="13" text-anchor="middle" fill="#111827">Visible</text>
  <line x1="40" y1="90" x2="40" y2="98" stroke="#111827" stroke-width="1.5"/>
  <text x="40" y="115" font-size="13" text-anchor="middle" fill="#111827">10⁻⁸</text>
  <line x1="100" y1="90" x2="100" y2="98" stroke="#111827" stroke-width="1.5"/>
  <text x="100" y="115" font-size="13" text-anchor="middle" fill="#111827">10⁻⁷</text>
  <line x1="160" y1="90" x2="160" y2="98" stroke="#111827" stroke-width="1.5"/>
  <text x="160" y="115" font-size="13" text-anchor="middle" fill="#111827">10⁻⁶</text>
  <line x1="220" y1="90" x2="220" y2="98" stroke="#111827" stroke-width="1.5"/>
  <text x="220" y="115" font-size="13" text-anchor="middle" fill="#111827">10⁻⁵</text>
  <line x1="280" y1="90" x2="280" y2="98" stroke="#111827" stroke-width="1.5"/>
  <text x="280" y="115" font-size="13" text-anchor="middle" fill="#111827">10⁻⁴</text>
  <line x1="340" y1="90" x2="340" y2="98" stroke="#111827" stroke-width="1.5"/>
  <text x="340" y="115" font-size="13" text-anchor="middle" fill="#111827">10⁻³</text>
  <line x1="400" y1="90" x2="400" y2="98" stroke="#111827" stroke-width="1.5"/>
  <text x="400" y="115" font-size="13" text-anchor="middle" fill="#111827">10⁻²</text>
  <line x1="460" y1="90" x2="460" y2="98" stroke="#111827" stroke-width="1.5"/>
  <text x="460" y="115" font-size="13" text-anchor="middle" fill="#111827">10⁻¹</text>
  <line x1="520" y1="90" x2="520" y2="98" stroke="#111827" stroke-width="1.5"/>
  <text x="520" y="115" font-size="13" text-anchor="middle" fill="#111827">10⁰</text>
  <text x="280" y="142" font-size="13" text-anchor="middle" fill="#111827">Wavelength (m)</text>
</svg>
<figcaption>Figure: Regions of the electromagnetic spectrum (logarithmic wavelength scale).</figcaption>
</figure>""",
        "question": r"Ozone molecules, $\text{O}_3$, in the stratosphere strongly absorb electromagnetic radiation with a frequency of $1.2 \times 10^{15}\text{ s}^{-1}$. Based on the figure above, in which region of the electromagnetic spectrum is this radiation, and what does its absorption do to an $\text{O}_3$ molecule? ($c = 2.998 \times 10^8\text{ m/s}$)",
        "options": [
            r"Infrared; it increases the vibrational energy of the $\text{O}_3$ molecule.",
            r"Infrared; it promotes an electron in the $\text{O}_3$ molecule to a higher electronic energy level.",
            r"Ultraviolet; it increases the vibrational energy of the $\text{O}_3$ molecule without changing its electronic energy.",
            r"Ultraviolet; it promotes an electron in the $\text{O}_3$ molecule to a higher electronic energy level.",
        ],
        "correct_index": 3,
        "explanation": r"Use $c = \lambda\nu$: $\lambda = \frac{c}{\nu} = \frac{2.998 \times 10^8\text{ m/s}}{1.2 \times 10^{15}\text{ s}^{-1}} = 2.5 \times 10^{-7}\text{ m}$ ($250\text{ nm}$). On the figure, this wavelength lies in the ultraviolet region, which extends to $4 \times 10^{-7}\text{ m}$. Ultraviolet and visible photons have energies that match the spacing between electronic energy levels, so absorbing one promotes an electron to a higher electronic energy level. Infrared photons, with wavelengths of about $7 \times 10^{-7}$ to $10^{-3}\text{ m}$, have lower energies that match vibrational transitions. Choosing infrared usually comes from an exponent error (for example, $2.5 \times 10^{-6}\text{ m}$), and an ultraviolet photon has far more energy than the spacing between vibrational levels.",
    },
    {
        "unit_q_num": 77,
        "topic_code": "3.12",
        "topic_title": "Properties of Photons",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 285" role="img" aria-label="Energy-level diagram of an atom drawn to scale with four levels: E1 = minus 9.0, E2 = minus 5.0, E3 = minus 3.0, and E4 = minus 1.0, all times 10 to the minus 19 joules. Transition I is a downward arrow from E4 to E3. Transition II is an upward arrow from E1 to E4. Transition III is a downward arrow from E3 to E1. Transition IV is a downward arrow from E4 to E2." font-family="sans-serif">
  <line x1="172" y1="55" x2="455" y2="55" stroke="#111827" stroke-width="2.5"/>
  <text x="162" y="59.5" font-size="13" text-anchor="end" fill="#111827">E₄ = −1.0 × 10⁻¹⁹ J</text>
  <line x1="172" y1="105" x2="455" y2="105" stroke="#111827" stroke-width="2.5"/>
  <text x="162" y="109.5" font-size="13" text-anchor="end" fill="#111827">E₃ = −3.0 × 10⁻¹⁹ J</text>
  <line x1="172" y1="155" x2="455" y2="155" stroke="#111827" stroke-width="2.5"/>
  <text x="162" y="159.5" font-size="13" text-anchor="end" fill="#111827">E₂ = −5.0 × 10⁻¹⁹ J</text>
  <line x1="172" y1="255" x2="455" y2="255" stroke="#111827" stroke-width="2.5"/>
  <text x="162" y="259.5" font-size="13" text-anchor="end" fill="#111827">E₁ = −9.0 × 10⁻¹⁹ J</text>
  <line x1="215" y1="55" x2="215" y2="97" stroke="#2563eb" stroke-width="2"/>
  <polygon points="215,105 210.5,97 219.5,97" fill="#2563eb"/>
  <text x="222" y="85" font-size="14" font-weight="bold" fill="#2563eb">I</text>
  <line x1="285" y1="255" x2="285" y2="63" stroke="#2563eb" stroke-width="2"/>
  <polygon points="285,55 289.5,63 280.5,63" fill="#2563eb"/>
  <text x="292" y="210" font-size="14" font-weight="bold" fill="#2563eb">II</text>
  <line x1="355" y1="105" x2="355" y2="247" stroke="#2563eb" stroke-width="2"/>
  <polygon points="355,255 350.5,247 359.5,247" fill="#2563eb"/>
  <text x="362" y="185" font-size="14" font-weight="bold" fill="#2563eb">III</text>
  <line x1="425" y1="55" x2="425" y2="147" stroke="#2563eb" stroke-width="2"/>
  <polygon points="425,155 420.5,147 429.5,147" fill="#2563eb"/>
  <text x="432" y="85" font-size="14" font-weight="bold" fill="#2563eb">IV</text>
  <line x1="495" y1="272" x2="495" y2="38" stroke="#111827" stroke-width="2"/>
  <polygon points="495,30 499.5,38 490.5,38" fill="#111827"/>
  <text x="510" y="150" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 510 150)">Energy</text>
</svg>
<figcaption>Figure: Four energy levels of an atom (drawn to scale) and transitions I–IV.</figcaption>
</figure>""",
        "question": r"The diagram above shows four energy levels of an atom and four transitions between them, labeled I through IV. Which transition results in the emission of a photon with the shortest wavelength?",
        "options": [
            r"Transition I",
            r"Transition II",
            r"Transition III",
            r"Transition IV",
        ],
        "correct_index": 2,
        "explanation": r"When an atom emits a photon, it drops to a lower energy level, and the energy of the photon equals the energy lost: $E_{\text{photon}} = |\Delta E| = h\nu = \frac{hc}{\lambda}$. The shortest wavelength therefore comes from the downward transition with the largest energy change. Transition III ($E_3 \rightarrow E_1$, $6.0 \times 10^{-19}\text{ J}$) releases more energy than transition IV ($E_4 \rightarrow E_2$, $4.0 \times 10^{-19}\text{ J}$) or transition I ($E_4 \rightarrow E_3$, $2.0 \times 10^{-19}\text{ J}$). Transition II has the largest energy change ($8.0 \times 10^{-19}\text{ J}$), but it goes upward, from $E_1$ to $E_4$, so a photon is absorbed rather than emitted. Transition I, the smallest drop, emits the longest wavelength of the three emissions.",
    },
    {
        "unit_q_num": 78,
        "topic_code": "3.12",
        "topic_title": "Properties of Photons",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"An atom in its lowest energy level, level 1, absorbs a photon of wavelength $300.\text{ nm}$ and is excited to level 3. The atom then returns to level 1 in two steps: it emits a photon of wavelength $500.\text{ nm}$ as it drops from level 3 to level 2, and then it emits a second photon as it drops from level 2 to level 1. What is the wavelength of the second photon?",
        "options": [
            r"$188\text{ nm}$",
            r"$200.\text{ nm}$",
            r"$750.\text{ nm}$",
            r"$800.\text{ nm}$",
        ],
        "correct_index": 2,
        "explanation": r"Energy is conserved: the energy absorbed equals the total energy of the two emitted photons, $E_{3\rightarrow1} = E_{3\rightarrow2} + E_{2\rightarrow1}$. Because $E = \frac{hc}{\lambda}$, $\frac{1}{\lambda_{2\rightarrow1}} = \frac{1}{300.\text{ nm}} - \frac{1}{500.\text{ nm}} = \frac{5 - 3}{1500\text{ nm}} = \frac{1}{750.\text{ nm}}$, so $\lambda_{2\rightarrow1} = 750.\text{ nm}$. Check in joules: $E_{3\rightarrow1} = \frac{(6.626 \times 10^{-34}\text{ J s})(2.998 \times 10^8\text{ m/s})}{3.00 \times 10^{-7}\text{ m}} = 6.62 \times 10^{-19}\text{ J}$ and $E_{3\rightarrow2} = 3.97 \times 10^{-19}\text{ J}$; the difference, $2.65 \times 10^{-19}\text{ J}$, corresponds to $\lambda = 7.50 \times 10^{-7}\text{ m}$. Wavelengths are not additive: subtracting them gives $200.\text{ nm}$, adding them gives $800.\text{ nm}$, and adding the two photon energies gives $188\text{ nm}$.",
    },
    {
        "unit_q_num": 79,
        "topic_code": "3.13",
        "topic_title": "Beer-Lambert Law",
        "difficulty": "Challenging",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 328" role="img" aria-label="Calibration graph of absorbance versus dye concentration in units of 10 to the minus 4 molar. Four data points, at 1.0, 2.0, 3.0, and 4.0 with absorbances 0.15, 0.30, 0.45, and 0.60, lie on a straight line through the origin that reaches an absorbance of 0.75 at 5.0." font-family="sans-serif">
  <line x1="160" y1="270" x2="160" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="240" y1="270" x2="240" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="320" y1="270" x2="320" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="400" y1="270" x2="400" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="480" y1="270" x2="480" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="80" y1="240" x2="480" y2="240" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="80" y1="210" x2="480" y2="210" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="80" y1="180" x2="480" y2="180" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="80" y1="150" x2="480" y2="150" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="80" y1="120" x2="480" y2="120" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="80" y1="90" x2="480" y2="90" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="80" y1="60" x2="480" y2="60" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="80" y1="30" x2="480" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="80" y1="270" x2="480" y2="270" stroke="#111827" stroke-width="2"/>
  <line x1="80" y1="270" x2="80" y2="30" stroke="#111827" stroke-width="2"/>
  <line x1="80" y1="270" x2="80" y2="275" stroke="#111827" stroke-width="1.5"/>
  <text x="80" y="289" font-size="12" text-anchor="middle" fill="#111827">0</text>
  <line x1="160" y1="270" x2="160" y2="275" stroke="#111827" stroke-width="1.5"/>
  <text x="160" y="289" font-size="12" text-anchor="middle" fill="#111827">1.0</text>
  <line x1="240" y1="270" x2="240" y2="275" stroke="#111827" stroke-width="1.5"/>
  <text x="240" y="289" font-size="12" text-anchor="middle" fill="#111827">2.0</text>
  <line x1="320" y1="270" x2="320" y2="275" stroke="#111827" stroke-width="1.5"/>
  <text x="320" y="289" font-size="12" text-anchor="middle" fill="#111827">3.0</text>
  <line x1="400" y1="270" x2="400" y2="275" stroke="#111827" stroke-width="1.5"/>
  <text x="400" y="289" font-size="12" text-anchor="middle" fill="#111827">4.0</text>
  <line x1="480" y1="270" x2="480" y2="275" stroke="#111827" stroke-width="1.5"/>
  <text x="480" y="289" font-size="12" text-anchor="middle" fill="#111827">5.0</text>
  <line x1="75" y1="270" x2="80" y2="270" stroke="#111827" stroke-width="1.5"/>
  <text x="71" y="274" font-size="12" text-anchor="end" fill="#111827">0</text>
  <line x1="75" y1="240" x2="80" y2="240" stroke="#111827" stroke-width="1.5"/>
  <text x="71" y="244" font-size="12" text-anchor="end" fill="#111827">0.10</text>
  <line x1="75" y1="210" x2="80" y2="210" stroke="#111827" stroke-width="1.5"/>
  <text x="71" y="214" font-size="12" text-anchor="end" fill="#111827">0.20</text>
  <line x1="75" y1="180" x2="80" y2="180" stroke="#111827" stroke-width="1.5"/>
  <text x="71" y="184" font-size="12" text-anchor="end" fill="#111827">0.30</text>
  <line x1="75" y1="150" x2="80" y2="150" stroke="#111827" stroke-width="1.5"/>
  <text x="71" y="154" font-size="12" text-anchor="end" fill="#111827">0.40</text>
  <line x1="75" y1="120" x2="80" y2="120" stroke="#111827" stroke-width="1.5"/>
  <text x="71" y="124" font-size="12" text-anchor="end" fill="#111827">0.50</text>
  <line x1="75" y1="90" x2="80" y2="90" stroke="#111827" stroke-width="1.5"/>
  <text x="71" y="94" font-size="12" text-anchor="end" fill="#111827">0.60</text>
  <line x1="75" y1="60" x2="80" y2="60" stroke="#111827" stroke-width="1.5"/>
  <text x="71" y="64" font-size="12" text-anchor="end" fill="#111827">0.70</text>
  <line x1="75" y1="30" x2="80" y2="30" stroke="#111827" stroke-width="1.5"/>
  <text x="71" y="34" font-size="12" text-anchor="end" fill="#111827">0.80</text>
  <text x="280" y="316" font-size="13" text-anchor="middle" fill="#111827">Concentration of dye (×10⁻⁴ M)</text>
  <text x="24" y="150" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 24 150)">Absorbance</text>
  <line x1="80" y1="270" x2="480" y2="45" stroke="#374151" stroke-width="2"/>
  <circle cx="160" cy="225" r="5" fill="#111827" stroke="#111827" stroke-width="1.5"/>
  <circle cx="240" cy="180" r="5" fill="#111827" stroke="#111827" stroke-width="1.5"/>
  <circle cx="320" cy="135" r="5" fill="#111827" stroke="#111827" stroke-width="1.5"/>
  <circle cx="400" cy="90" r="5" fill="#111827" stroke="#111827" stroke-width="1.5"/>
</svg>
<figcaption>Figure: Calibration line for the dye at its wavelength of maximum absorbance (path length 1.00 cm).</figcaption>
</figure>""",
        "question": r"The calibration line above was made for a dye at its wavelength of maximum absorbance, using a cuvette with a path length of $1.00\text{ cm}$. A student pipets $5.00\text{ mL}$ of a dye solution of unknown concentration into a $25.00\text{ mL}$ volumetric flask and dilutes it to the mark with distilled water. Under the same conditions, the diluted solution has an absorbance of $0.36$. What is the concentration of the dye in the original, undiluted solution?",
        "options": [
            r"$1.4 \times 10^{-3}\text{ M}$",
            r"$1.2 \times 10^{-3}\text{ M}$",
            r"$2.4 \times 10^{-4}\text{ M}$",
            r"$4.8 \times 10^{-5}\text{ M}$",
        ],
        "correct_index": 1,
        "explanation": r"The slope of the line is $\varepsilon b = \frac{0.60}{4.0 \times 10^{-4}\text{ M}} = 1.5 \times 10^3\text{ M}^{-1}$. For the diluted solution, $c = \frac{A}{\varepsilon b} = \frac{0.36}{1.5 \times 10^3\text{ M}^{-1}} = 2.4 \times 10^{-4}\text{ M}$, which agrees with reading the graph. Diluting $5.00\text{ mL}$ to a total volume of $25.00\text{ mL}$ lowered the concentration by a factor of $\frac{25.00}{5.00} = 5$, so the original concentration was $5(2.4 \times 10^{-4}\text{ M}) = 1.2 \times 10^{-3}\text{ M}$. Reporting $2.4 \times 10^{-4}\text{ M}$ ignores the dilution, dividing by 5 instead of multiplying gives $4.8 \times 10^{-5}\text{ M}$, and using a factor of 6 (as if $25.00\text{ mL}$ of water had been added) gives $1.4 \times 10^{-3}\text{ M}$.",
    },
    {
        "unit_q_num": 80,
        "topic_code": "3.13",
        "topic_title": "Beer-Lambert Law",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 326" role="img" aria-label="Absorbance spectrum of a red dye solution from 400 to 700 nanometers. The single broad peak has its maximum absorbance of 0.80 at 520 nanometers. At 470 nanometers the absorbance is 0.40. The absorbance falls to nearly zero below 420 and above 620 nanometers." font-family="sans-serif">
  <line x1="146.7" y1="270" x2="146.7" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="213.3" y1="270" x2="213.3" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="280" y1="270" x2="280" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="346.7" y1="270" x2="346.7" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="413.3" y1="270" x2="413.3" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="480" y1="270" x2="480" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="80" y1="222" x2="480" y2="222" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="80" y1="174" x2="480" y2="174" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="80" y1="126" x2="480" y2="126" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="80" y1="78" x2="480" y2="78" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="80" y1="30" x2="480" y2="30" stroke="#e5e7eb" stroke-width="1.5"/>
  <line x1="80" y1="270" x2="480" y2="270" stroke="#111827" stroke-width="2"/>
  <line x1="80" y1="270" x2="80" y2="30" stroke="#111827" stroke-width="2"/>
  <line x1="80" y1="270" x2="80" y2="275" stroke="#111827" stroke-width="1.5"/>
  <text x="80" y="289" font-size="12" text-anchor="middle" fill="#111827">400</text>
  <line x1="146.7" y1="270" x2="146.7" y2="275" stroke="#111827" stroke-width="1.5"/>
  <text x="146.7" y="289" font-size="12" text-anchor="middle" fill="#111827">450</text>
  <line x1="213.3" y1="270" x2="213.3" y2="275" stroke="#111827" stroke-width="1.5"/>
  <text x="213.3" y="289" font-size="12" text-anchor="middle" fill="#111827">500</text>
  <line x1="280" y1="270" x2="280" y2="275" stroke="#111827" stroke-width="1.5"/>
  <text x="280" y="289" font-size="12" text-anchor="middle" fill="#111827">550</text>
  <line x1="346.7" y1="270" x2="346.7" y2="275" stroke="#111827" stroke-width="1.5"/>
  <text x="346.7" y="289" font-size="12" text-anchor="middle" fill="#111827">600</text>
  <line x1="413.3" y1="270" x2="413.3" y2="275" stroke="#111827" stroke-width="1.5"/>
  <text x="413.3" y="289" font-size="12" text-anchor="middle" fill="#111827">650</text>
  <line x1="480" y1="270" x2="480" y2="275" stroke="#111827" stroke-width="1.5"/>
  <text x="480" y="289" font-size="12" text-anchor="middle" fill="#111827">700</text>
  <line x1="75" y1="270" x2="80" y2="270" stroke="#111827" stroke-width="1.5"/>
  <text x="71" y="274" font-size="12" text-anchor="end" fill="#111827">0</text>
  <line x1="75" y1="222" x2="80" y2="222" stroke="#111827" stroke-width="1.5"/>
  <text x="71" y="226" font-size="12" text-anchor="end" fill="#111827">0.20</text>
  <line x1="75" y1="174" x2="80" y2="174" stroke="#111827" stroke-width="1.5"/>
  <text x="71" y="178" font-size="12" text-anchor="end" fill="#111827">0.40</text>
  <line x1="75" y1="126" x2="80" y2="126" stroke="#111827" stroke-width="1.5"/>
  <text x="71" y="130" font-size="12" text-anchor="end" fill="#111827">0.60</text>
  <line x1="75" y1="78" x2="80" y2="78" stroke="#111827" stroke-width="1.5"/>
  <text x="71" y="82" font-size="12" text-anchor="end" fill="#111827">0.80</text>
  <line x1="75" y1="30" x2="80" y2="30" stroke="#111827" stroke-width="1.5"/>
  <text x="71" y="34" font-size="12" text-anchor="end" fill="#111827">1.00</text>
  <text x="280" y="316" font-size="13" text-anchor="middle" fill="#111827">Wavelength (nm)</text>
  <text x="24" y="150" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 24 150)">Absorbance</text>
  <polyline points="80,266.5 82.7,266 85.3,265.4 88,264.8 90.7,264.1 93.3,263.3 96,262.4 98.7,261.5 101.3,260.4 104,259.3 106.7,258 109.3,256.6 112,255.1 114.7,253.4 117.3,251.6 120,249.7 122.7,247.6 125.3,245.3 128,242.9 130.7,240.2 133.3,237.4 136,234.5 138.7,231.3 141.3,227.9 144,224.4 146.7,220.7 149.3,216.7 152,212.6 154.7,208.3 157.3,203.9 160,199.2 162.7,194.4 165.3,189.5 168,184.5 170.7,179.3 173.3,174 176,168.6 178.7,163.2 181.3,157.8 184,152.3 186.7,146.8 189.3,141.3 192,136 194.7,130.7 197.3,125.5 200,120.4 202.7,115.5 205.3,110.8 208,106.3 210.7,102.1 213.3,98.2 216,94.5 218.7,91.2 221.3,88.2 224,85.5 226.7,83.3 229.3,81.4 232,79.9 234.7,78.8 237.3,78.2 240,78 242.7,78.2 245.3,78.8 248,79.9 250.7,81.4 253.3,83.3 256,85.5 258.7,88.2 261.3,91.2 264,94.5 266.7,98.2 269.3,102.1 272,106.3 274.7,110.8 277.3,115.5 280,120.4 282.7,125.5 285.3,130.7 288,136 290.7,141.3 293.3,146.8 296,152.3 298.7,157.8 301.3,163.2 304,168.6 306.7,174 309.3,179.3 312,184.5 314.7,189.5 317.3,194.4 320,199.2 322.7,203.9 325.3,208.3 328,212.6 330.7,216.7 333.3,220.7 336,224.4 338.7,227.9 341.3,231.3 344,234.5 346.7,237.4 349.3,240.2 352,242.9 354.7,245.3 357.3,247.6 360,249.7 362.7,251.6 365.3,253.4 368,255.1 370.7,256.6 373.3,258 376,259.3 378.7,260.4 381.3,261.5 384,262.4 386.7,263.3 389.3,264.1 392,264.8 394.7,265.4 397.3,266 400,266.5 402.7,266.9 405.3,267.3 408,267.6 410.7,268 413.3,268.2 416,268.5 418.7,268.7 421.3,268.9 424,269 426.7,269.2 429.3,269.3 432,269.4 434.7,269.5 437.3,269.6 440,269.6 442.7,269.7 445.3,269.7 448,269.8 450.7,269.8 453.3,269.8 456,269.9 458.7,269.9 461.3,269.9 464,269.9 466.7,269.9 469.3,269.9 472,270 474.7,270 477.3,270 480,270" fill="none" stroke="#111827" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="173.3" y1="270" x2="173.3" y2="174" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="5 4"/>
  <circle cx="173.3" cy="174" r="4" fill="#2563eb" stroke="#2563eb" stroke-width="1.5"/>
  <text x="167.3" y="258" font-size="12" text-anchor="end" fill="#2563eb">470 nm</text>
  <line x1="240" y1="270" x2="240" y2="78" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="5 4"/>
  <circle cx="240" cy="78" r="4" fill="#2563eb" stroke="#2563eb" stroke-width="1.5"/>
  <text x="246" y="258" font-size="12" fill="#2563eb">520 nm</text>
</svg>
<figcaption>Figure: Absorbance spectrum of a solution of the red dye.</figcaption>
</figure>""",
        "question": r"The absorbance spectrum of a solution of a red dye is shown above. A student makes a calibration curve by measuring the absorbance of standard solutions of the dye at $520\text{ nm}$. The student then measures the absorbance of a dye solution of unknown concentration but accidentally sets the spectrophotometer to $470\text{ nm}$, and uses this absorbance with the $520\text{ nm}$ calibration curve. How does this error affect the calculated concentration of the unknown solution?",
        "options": [
            r"The calculated concentration is too low, because the dye absorbs less strongly at $470\text{ nm}$ than at $520\text{ nm}$, so the measured absorbance is smaller.",
            r"The calculated concentration is too high, because photons of $470\text{ nm}$ light have more energy than photons of $520\text{ nm}$ light, so more of the light is absorbed.",
            r"The calculated concentration is too high, because the dye absorbs more strongly at $470\text{ nm}$ than at $520\text{ nm}$, so the measured absorbance is larger.",
            r"The calculated concentration is not affected, because absorbance depends only on the concentration of the dye and the path length.",
        ],
        "correct_index": 0,
        "explanation": r"In $A = \varepsilon bc$, the molar absorptivity $\varepsilon$ depends on wavelength. The spectrum shows that the dye absorbs most strongly at $\lambda_{\text{max}} = 520\text{ nm}$ ($A \approx 0.80$) and only about half as strongly at $470\text{ nm}$ ($A \approx 0.40$); this is why the calibration was done at $520\text{ nm}$, where sensitivity is greatest. At $470\text{ nm}$, $\varepsilon$ is smaller, so the unknown gives a lower absorbance than it would give at $520\text{ nm}$, and the $520\text{ nm}$ calibration curve converts this low absorbance into a concentration that is too low. Higher photon energy does not mean more absorption; the amount of light absorbed depends on $\varepsilon$ at that wavelength. Absorbance does not depend only on concentration and path length, because $\varepsilon$ changes with wavelength.",
    },
]
