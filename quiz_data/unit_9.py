"""
AP Chemistry — Unit 9: Thermodynamics and Electrochemistry (7–9% of Exam)
60 AP Exam-Level Multiple-Choice Questions covering Topics 9.1–9.11 (Fall 2024 CED).
"""

UNIT_META = {
    "id": 9,
    "title": "Unit 9: Thermodynamics and Electrochemistry",
    "short_title": "Thermodynamics & Electrochemistry",
    "exam_weight": "7–9%",
    "color": "#4f46e5",
    "description": (
        "Entropy and microstates (ΔS°), Gibbs free energy (ΔG° = ΔH° − TΔS°) and thermodynamic "
        "favorability, kinetic vs. thermodynamic control, ΔG° = −RT ln K, free energy of dissolution (Topic 9.6), coupled reactions, "
        "galvanic (voltaic) vs. electrolytic cells, standard cell potentials (E°cell), "
        "ΔG° = −nFE°cell, Nernst equation and nonstandard conditions, and Faraday's Law of electrolysis."
    ),
    "topics": [
        {"code": "9.1", "title": "Introduction to Entropy"},
        {"code": "9.2", "title": "Absolute Entropy and Entropy Change"},
        {"code": "9.3", "title": "Gibbs Free Energy and Thermodynamic Favorability"},
        {"code": "9.4", "title": "Thermodynamic and Kinetic Control"},
        {"code": "9.5", "title": "Free Energy and Equilibrium"},
        {"code": "9.6", "title": "Free Energy of Dissolution"},
        {"code": "9.7", "title": "Coupled Reactions"},
        {"code": "9.8", "title": "Galvanic (Voltaic) and Electrolytic Cells"},
        {"code": "9.9", "title": "Cell Potential and Free Energy"},
        {"code": "9.10", "title": "Cell Potential Under Nonstandard Conditions"},
        {"code": "9.11", "title": "Electrolysis and Faraday's Law"},
    ],
}

QUESTIONS = [
    # -------------------------------------------------------------------------
    # Topic 9.1: Introduction to Entropy (Q1–Q5)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 1,
        "topic_code": "9.1",
        "topic_title": "Introduction to Entropy",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"Which of the following processes results in the largest increase in entropy ($\Delta S^\circ > 0$) at $298\text{ K}$?"
        ),
        "options": [
            r"$\text{CO}_2(g) \rightarrow \text{CO}_2(s)$",
            r"$\text{N}_2(g) + 3\text{H}_2(g) \rightarrow 2\text{NH}_3(g)$",
            r"$\text{NH}_4\text{NO}_3(s) \rightarrow \text{NH}_4\text{NO}_3(aq)$",
            r"$2\text{H}_2\text{O}_2(l) \rightarrow 2\text{H}_2\text{O}(l) + \text{O}_2(g)$",
        ],
        "correct_index": 3,
        "explanation": (
            r"Decomposing $2\text{ mol}$ of liquid $\text{H}_2\text{O}_2(l)$ produces $2\text{ mol}$ of liquid water plus $1\text{ mol}$ of $\text{O}_2(g)$ ($\Delta n_{\text{gas}} = +1$); forming a gas from condensed phases greatly increases the dispersal of matter ($\Delta S^\circ \approx +126\text{ J mol}_{\text{rxn}}^{-1}\text{ K}^{-1}$ from standard molar entropies). Dissolving $\text{NH}_4\text{NO}_3(s)$ into aqueous ions also increases entropy, but by less ($\Delta S^\circ \approx +109\text{ J mol}_{\text{rxn}}^{-1}\text{ K}^{-1}$) because no gas is formed. The deposition of $\text{CO}_2(g)$ as a solid ($\Delta n_{\text{gas}} = -1$) and the synthesis of $\text{NH}_3$ (gas moles decrease from $4$ to $2$) both have $\Delta S^\circ < 0$."
        ),
    },
    {
        "unit_q_num": 2,
        "topic_code": "9.1",
        "topic_title": "Introduction to Entropy",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"An ideal gas is confined to one bulb of a two-bulb apparatus at constant temperature, while the second bulb of equal volume is evacuated. When the stopcock between the bulbs is opened and the gas expands to fill both bulbs isothermally, which statement correctly describes the change in the system?"
        ),
        "options": [
            r"$\Delta S_{\text{sys}} = 0$ because the temperature of the ideal gas remains constant during free expansion.",
            r"$\Delta S_{\text{sys}} < 0$ because the pressure of the gas decreases by a factor of two.",
            r"$\Delta S_{\text{sys}} > 0$ because the average kinetic energy of the gas molecules increases.",
            r"$\Delta S_{\text{sys}} > 0$ because the gas particles occupy twice the volume and have a greater number of available positional microstates.",
        ],
        "correct_index": 3,
        "explanation": (
            r"During isothermal free expansion of an ideal gas into a vacuum ($V_f = 2V_i$), the particles spread over a larger volume, increasing the number of accessible spatial arrangements (positional microstates $W$), so $\Delta S_{\text{sys}} = nR\ln(V_f/V_i) > 0$. Because $T$ is constant, average kinetic energy does not change."
        ),
    },
    {
        "unit_q_num": 3,
        "topic_code": "9.1",
        "topic_title": "Introduction to Entropy",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r'<table class="quiz-data-table"><thead><tr><th>Sample</th><th>Substance</th><th>Temperature</th><th>Volume</th></tr></thead>'
            r'<tbody><tr><td>1</td><td>$1.0\text{ mol Ne}(g)$</td><td>$300\text{ K}$</td><td>$10\text{ L}$</td></tr>'
            r'<tr><td>2</td><td>$1.0\text{ mol Ne}(g)$</td><td>$300\text{ K}$</td><td>$20\text{ L}$</td></tr>'
            r'<tr><td>3</td><td>$1.0\text{ mol Ne}(g)$</td><td>$600\text{ K}$</td><td>$20\text{ L}$</td></tr></tbody></table>'
        ),
        "question": (
            r"Three samples of $\text{Ne}(g)$ are described in the table above. Which of the following correctly ranks the samples in order of increasing entropy ($S$)?"
        ),
        "options": [
            r"$\text{Sample 1} < \text{Sample 2} < \text{Sample 3}$",
            r"$\text{Sample 3} < \text{Sample 2} < \text{Sample 1}$",
            r"$\text{Sample 1} = \text{Sample 2} < \text{Sample 3}$",
            r"$\text{Sample 2} < \text{Sample 1} < \text{Sample 3}$",
        ],
        "correct_index": 0,
        "explanation": (
            r"Comparing Sample 1 and Sample 2 at $300\text{ K}$, Sample 2 has a larger volume ($20\text{ L}$ vs. $10\text{ L}$), giving more positional microstates ($S_1 < S_2$). Comparing Sample 2 and Sample 3 at $20\text{ L}$, Sample 3 is at a higher temperature ($600\text{ K}$ vs. $300\text{ K}$), broadening the Maxwell-Boltzmann distribution of molecular speeds and thermal energy levels ($S_2 < S_3$). Thus $S_1 < S_2 < S_3$."
        ),
    },
    {
        "unit_q_num": 4,
        "topic_code": "9.1",
        "topic_title": "Introduction to Entropy",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": (
            r"When solid $\text{MgSO}_4(s)$ dissolves in water at $298\text{ K}$, the measured standard entropy of dissolution is negative ($\Delta S_{\text{soln}}^\circ < 0$), even though a crystalline solid is dispersing into mobile aqueous ions. Which of the following best accounts for this observation?"
        ),
        "options": [
            r"Dissolution of $\text{MgSO}_4(s)$ is endothermic, and endothermic processes always have $\Delta S^\circ < 0$.",
            r"$\text{MgSO}_4$ remains completely undissociated as neutral ion pairs in aqueous solution.",
            r"Water molecules form highly ordered hydration shells around the doubly charged $\text{Mg}^{2+}$ and $\text{SO}_4^{2-}$ ions (especially the small $\text{Mg}^{2+}$ ion), decreasing the entropy of the solvent more than the ion dispersal increases it.",
            r"The covalent bonds inside the $\text{SO}_4^{2-}$ polyatomic ion are broken during dissolution.",
        ],
        "correct_index": 2,
        "explanation": (
            r"Doubly charged ions, especially the small, high-charge-density $\text{Mg}^{2+}$ ion, strongly attract polar $\text{H}_2\text{O}$ molecules via ion-dipole forces, locking solvent molecules into tightly ordered hydration spheres. This large decrease in solvent entropy outweighs the increase in solute entropy from lattice breakup, making net $\Delta S_{\text{soln}}^\circ < 0$."
        ),
    },
    {
        "unit_q_num": 5,
        "topic_code": "9.1",
        "topic_title": "Introduction to Entropy",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"For which of the following reactions is $\Delta S_{\text{rxn}}^\circ$ closest to zero?"
        ),
        "options": [
            r"$\text{CaCO}_3(s) \rightarrow \text{CaO}(s) + \text{CO}_2(g)$",
            r"$\text{H}_2(g) + \text{I}_2(g) \rightarrow 2\text{HI}(g)$",
            r"$2\text{SO}_2(g) + \text{O}_2(g) \rightarrow 2\text{SO}_3(g)$",
            r"$\text{Ag}^+(aq) + \text{Cl}^-(aq) \rightarrow \text{AgCl}(s)$",
        ],
        "correct_index": 1,
        "explanation": (
            r"In $\text{H}_2(g) + \text{I}_2(g) \rightarrow 2\text{HI}(g)$, $2\text{ mol}$ of diatomic gas reactants form $2\text{ mol}$ of diatomic gas products ($\Delta n_{\text{gas}} = 0$), so the change in the number of microstates and standard entropy $\Delta S_{\text{rxn}}^\circ$ is very small (close to zero)."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 9.2: Absolute Entropy and Entropy Change (Q6–Q10)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 6,
        "topic_code": "9.2",
        "topic_title": "Absolute Entropy and Entropy Change",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r'<table class="quiz-data-table"><thead><tr><th>Substance</th><th>$S^\circ\ (\text{J mol}^{-1}\text{ K}^{-1})$ at $298\text{ K}$</th></tr></thead>'
            r'<tbody><tr><td>$\text{N}_2(g)$</td><td>$191.6$</td></tr>'
            r'<tr><td>$\text{H}_2(g)$</td><td>$130.7$</td></tr>'
            r'<tr><td>$\text{NH}_3(g)$</td><td>$192.8$</td></tr></tbody></table>'
        ),
        "question": (
            r"Based on the standard molar entropies in the table above, what is $\Delta S_{\text{rxn}}^\circ$ for the reaction $\text{N}_2(g) + 3\text{H}_2(g) \rightarrow 2\text{NH}_3(g)$ at $298\text{ K}$?"
        ),
        "options": [
            r"$+198.1\text{ J mol}_{\text{rxn}}^{-1}\text{ K}^{-1}$",
            r"$+129.5\text{ J mol}_{\text{rxn}}^{-1}\text{ K}^{-1}$",
            r"$-129.5\text{ J mol}_{\text{rxn}}^{-1}\text{ K}^{-1}$",
            r"$-198.1\text{ J mol}_{\text{rxn}}^{-1}\text{ K}^{-1}$",
        ],
        "correct_index": 3,
        "explanation": (
            r"Using $\Delta S_{\text{rxn}}^\circ = \sum n_p S^\circ(\text{products}) - \sum n_r S^\circ(\text{reactants})$: "
            r"$\Delta S_{\text{rxn}}^\circ = [2(192.8)] - [1(191.6) + 3(130.7)] = 385.6 - (191.6 + 392.1) = 385.6 - 583.7 = -198.1\text{ J mol}_{\text{rxn}}^{-1}\text{ K}^{-1}$."
        ),
    },
    {
        "unit_q_num": 7,
        "topic_code": "9.2",
        "topic_title": "Absolute Entropy and Entropy Change",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"At $298\text{ K}$ and $1\text{ atm}$, why is the standard molar entropy $S^\circ$ of $\text{C}_3\text{H}_8(g)$ ($270\text{ J mol}^{-1}\text{ K}^{-1}$) significantly greater than that of $\text{CH}_4(g)$ ($186\text{ J mol}^{-1}\text{ K}^{-1}$)?"
        ),
        "options": [
            r"$\text{C}_3\text{H}_8(g)$ has more atoms and bonds per molecule, providing more rotational and vibrational degrees of freedom (microstates) than $\text{CH}_4(g)$.",
            r"$\text{C}_3\text{H}_8(g)$ has a higher average molar kinetic energy at $298\text{ K}$ than $\text{CH}_4(g)$.",
            r"$\text{CH}_4(g)$ forms intermolecular hydrogen bonds that restrict its molecular motion.",
            r"The standard enthalpy of formation of $\text{CH}_4(g)$ is zero at $298\text{ K}$.",
        ],
        "correct_index": 0,
        "explanation": (
            r"In the same phase at the same $T$ and $P$, larger, more complex polyatomic molecules ($\text{C}_3\text{H}_8$, 11 atoms) possess more vibrational and rotational modes in which thermal energy can be distributed than smaller molecules ($\text{CH}_4$, 5 atoms), giving a higher absolute entropy $S^\circ$."
        ),
    },
    {
        "unit_q_num": 8,
        "topic_code": "9.2",
        "topic_title": "Absolute Entropy and Entropy Change",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"Unlike standard enthalpies of formation ($\Delta H_f^\circ$), the standard molar entropy ($S^\circ$) of a pure element in its standard state at $298\text{ K}$ (such as $\text{O}_2(g)$) is NEVER equal to zero. Which fundamental principle explains this?"
        ),
        "options": [
            r"According to the Third Law of Thermodynamics, the entropy of a pure, perfect crystalline substance is zero only at $0\text{ K}$, so any substance at $298\text{ K}$ has positive thermal disorder ($S^\circ > 0$).",
            r"$\text{O}_2(g)$ is a diatomic molecule, whereas only monatomic noble gases have $S^\circ = 0$ at $298\text{ K}$.",
            r"Standard molar entropy is measured relative to liquid water at $273.15\text{ K}$.",
            r"Oxygen has multiple naturally occurring isotopes that prevent its enthalpy of formation from being zero.",
        ],
        "correct_index": 0,
        "explanation": (
            r"By the Third Law of Thermodynamics, $S = 0$ for a perfect pure crystal at absolute zero ($T = 0\text{ K}$). Heating any substance from $0\text{ K}$ to $298\text{ K}$ adds thermal energy and populates microstates, so $S^\circ(298\text{ K}) > 0$ for all substances, including elements in their standard states."
        ),
    },
    {
        "unit_q_num": 9,
        "topic_code": "9.2",
        "topic_title": "Absolute Entropy and Entropy Change",
        "difficulty": "Challenging",
        "stimulus": (
            r'<table class="quiz-data-table"><thead><tr><th>Reaction</th><td>$2\text{NO}(g) + \text{O}_2(g) \rightarrow 2\text{NO}_2(g)$</td><th>$\Delta S_{\text{rxn}}^\circ = -146.4\text{ J mol}_{\text{rxn}}^{-1}\text{ K}^{-1}$</th></tr></thead>'
            r'<tbody><tr><th>Substance</th><th>$\text{NO}(g)$</th><th>$\text{O}_2(g)$</th></tr>'
            r'<tr><td>$S^\circ\ (\text{J mol}^{-1}\text{ K}^{-1})$</td><td>$210.8$</td><td>$205.0$</td></tr></tbody></table>'
        ),
        "question": (
            r"Using the data in the table above, what is the standard molar entropy $S^\circ$ of $\text{NO}_2(g)$ at $298\text{ K}$?"
        ),
        "options": [
            r"$134.7\text{ J mol}^{-1}\text{ K}^{-1}$",
            r"$240.1\text{ J mol}^{-1}\text{ K}^{-1}$",
            r"$269.4\text{ J mol}^{-1}\text{ K}^{-1}$",
            r"$480.2\text{ J mol}^{-1}\text{ K}^{-1}$",
        ],
        "correct_index": 1,
        "explanation": (
            r"$\Delta S_{\text{rxn}}^\circ = 2S^\circ(\text{NO}_2) - [2S^\circ(\text{NO}) + S^\circ(\text{O}_2)]$. "
            r"Substituting values: $-146.4 = 2S^\circ(\text{NO}_2) - [2(210.8) + 205.0] = 2S^\circ(\text{NO}_2) - 626.6$. "
            r"Thus $2S^\circ(\text{NO}_2) = 626.6 - 146.4 = 480.2$, and $S^\circ(\text{NO}_2) = 240.1\text{ J mol}^{-1}\text{ K}^{-1}$. (Ignoring the coefficients gives $269.4$ or half of it, $134.7$; forgetting to divide by $2$ gives $480.2$.)"
        ),
    },
    {
        "unit_q_num": 10,
        "topic_code": "9.2",
        "topic_title": "Absolute Entropy and Entropy Change",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"Which of the following series correctly lists the substances in order of increasing standard molar entropy ($S^\circ$) at $298\text{ K}$?"
        ),
        "options": [
            r"$\text{C}(\text{diamond}, s) < \text{C}(\text{graphite}, s) < \text{CH}_4(g) < \text{C}_2\text{H}_6(g)$",
            r"$\text{C}(\text{graphite}, s) < \text{C}(\text{diamond}, s) < \text{C}_2\text{H}_6(g) < \text{CH}_4(g)$",
            r"$\text{CH}_4(g) < \text{C}_2\text{H}_6(g) < \text{C}(\text{diamond}, s) < \text{C}(\text{graphite}, s)$",
            r"$\text{C}(\text{diamond}, s) < \text{CH}_4(g) < \text{C}(\text{graphite}, s) < \text{C}_2\text{H}_6(g)$",
        ],
        "correct_index": 0,
        "explanation": (
            r"Diamond is a rigid 3D tetrahedral covalent network ($S^\circ = 2.4\text{ J mol}^{-1}\text{ K}^{-1}$), whereas graphite has delocalized 2D layers that can vibrate more freely ($S^\circ = 5.7\text{ J mol}^{-1}\text{ K}^{-1}$). Gases have much higher entropy than solids, and $\text{C}_2\text{H}_6(g)$ is larger and more complex than $\text{CH}_4(g)$."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 9.3: Gibbs Free Energy and Thermodynamic Favorability (Q11–Q15)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 11,
        "topic_code": "9.3",
        "topic_title": "Gibbs Free Energy and Thermodynamic Favorability",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r"$$\text{CaCO}_3(s) \rightleftharpoons \text{CaO}(s) + \text{CO}_2(g) \qquad \Delta H^\circ = +178\text{ kJ mol}_{\text{rxn}}^{-1},\quad \Delta S^\circ = +160\text{ J mol}_{\text{rxn}}^{-1}\text{ K}^{-1}$$"
        ),
        "question": (
            r"For the thermal decomposition of calcium carbonate shown above, above what minimum temperature (assuming $\Delta H^\circ$ and $\Delta S^\circ$ are independent of temperature) does the reaction become thermodynamically favorable ($\Delta G^\circ < 0$)?"
        ),
        "options": [
            r"$1.11\text{ K}$",
            r"$298\text{ K}$",
            r"$899\text{ K}$",
            r"$1113\text{ K}$",
        ],
        "correct_index": 3,
        "explanation": (
            r"Since both $\Delta H^\circ > 0$ and $\Delta S^\circ > 0$, the reaction becomes thermodynamically favorable above the crossover temperature $T = \Delta H^\circ / \Delta S^\circ$. Converting $\Delta H^\circ$ to joules: $T = \frac{178,000\text{ J mol}^{-1}}{160\text{ J mol}^{-1}\text{ K}^{-1}} = 1112.5\text{ K} \approx 1113\text{ K}$. (Dividing $178$ by $160$ without converting $\text{kJ}$ to $\text{J}$ gives the unit-conversion trap value of $1.11\text{ K}$.)"
        ),
    },
    {
        "unit_q_num": 12,
        "topic_code": "9.3",
        "topic_title": "Gibbs Free Energy and Thermodynamic Favorability",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"A chemical reaction is thermodynamically favorable at all temperatures under standard conditions. What must be the signs of $\Delta H^\circ$ and $\Delta S^\circ$ for this reaction?"
        ),
        "options": [
            r"$\Delta H^\circ > 0$ and $\Delta S^\circ > 0$",
            r"$\Delta H^\circ < 0$ and $\Delta S^\circ > 0$",
            r"$\Delta H^\circ < 0$ and $\Delta S^\circ < 0$",
            r"$\Delta H^\circ > 0$ and $\Delta S^\circ < 0$",
        ],
        "correct_index": 1,
        "explanation": (
            r"From $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$, since absolute temperature $T > 0$, having $\Delta H^\circ < 0$ (exothermic) and $\Delta S^\circ > 0$ (entropy-increasing) guarantees that both terms are negative at every temperature $T$, so $\Delta G^\circ < 0$ at all temperatures."
        ),
    },
    {
        "unit_q_num": 13,
        "topic_code": "9.3",
        "topic_title": "Gibbs Free Energy and Thermodynamic Favorability",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r'<table class="quiz-data-table"><thead><tr><th>Process</th><th>$\Delta H^\circ\ (\text{kJ mol}_{\text{rxn}}^{-1})$</th><th>$\Delta S^\circ\ (\text{J mol}_{\text{rxn}}^{-1}\text{ K}^{-1})$</th></tr></thead>'
            r'<tbody><tr><td>Reaction X</td><td>$-85.0$</td><td>$-200.0$</td></tr></tbody></table>'
        ),
        "question": (
            r"Based on the data in the table above, what is the value of $\Delta G^\circ$ for Reaction X at $300.\text{ K}$, and is the reaction thermodynamically favorable at this temperature?"
        ),
        "options": [
            r"$\Delta G^\circ = -145\text{ kJ mol}_{\text{rxn}}^{-1}$; thermodynamically favorable",
            r"$\Delta G^\circ = -25.0\text{ kJ mol}_{\text{rxn}}^{-1}$; thermodynamically favorable",
            r"$\Delta G^\circ = +25.0\text{ kJ mol}_{\text{rxn}}^{-1}$; thermodynamically unfavorable",
            r"$\Delta G^\circ = +59,915\text{ kJ mol}_{\text{rxn}}^{-1}$; thermodynamically unfavorable",
        ],
        "correct_index": 1,
        "explanation": (
            r"Convert $\Delta S^\circ$ to $\text{kJ mol}^{-1}\text{ K}^{-1}$: $\Delta S^\circ = -0.200\text{ kJ mol}^{-1}\text{ K}^{-1}$. "
            r"Then $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ = -85.0 - (300.)(-0.200) = -85.0 + 60.0 = -25.0\text{ kJ mol}_{\text{rxn}}^{-1}$. "
            r"Because $\Delta G^\circ < 0$, the reaction is thermodynamically favorable at $300.\text{ K}$."
        ),
    },
    {
        "unit_q_num": 14,
        "topic_code": "9.3",
        "topic_title": "Gibbs Free Energy and Thermodynamic Favorability",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"When liquid water freezes to ice at $1\text{ atm}$ and $-10^\circ\text{C}$ ($263\text{ K}$), the process is thermodynamically favored ($\Delta G < 0$). Which statement correctly explains what drives this process?"
        ),
        "options": [
            r"The process is entropy-driven because crystalline ice has higher positional entropy than liquid water.",
            r"Freezing of water is endothermic ($\Delta H > 0$), so low temperatures make $\Delta G < 0$.",
            r"At $-10^\circ\text{C}$, $\Delta G = 0$ because solid and liquid water are at equilibrium.",
            r"The process is enthalpy-driven ($\Delta H < 0$ and $\Delta S < 0$); below $273\text{ K}$, $|\Delta H| > |T\Delta S|$, so the heat released to the surroundings increases $\Delta S_{\text{surr}}$ more than $\Delta S_{\text{sys}}$ decreases.",
        ],
        "correct_index": 3,
        "explanation": (
            r"Freezing is bond/IMF-forming and orders molecules into a crystal lattice, so $\Delta H < 0$ and $\Delta S < 0$. At temperatures below the freezing point ($T < 273\text{ K}$), the magnitude of the negative $\Delta H$ term exceeds $-T\Delta S$, making $\Delta G = \Delta H - T\Delta S < 0$ (enthalpy-driven)."
        ),
    },
    {
        "unit_q_num": 15,
        "topic_code": "9.3",
        "topic_title": "Gibbs Free Energy and Thermodynamic Favorability",
        "difficulty": "Challenging",
        "stimulus": (
            r'<table class="quiz-data-table"><thead><tr><th>Substance</th><th>$\Delta G_f^\circ\ (\text{kJ mol}^{-1})$ at $298\text{ K}$</th></tr></thead>'
            r'<tbody><tr><td>$\text{CH}_4(g)$</td><td>$-50.8$</td></tr>'
            r'<tr><td>$\text{CO}_2(g)$</td><td>$-394.4$</td></tr>'
            r'<tr><td>$\text{H}_2\text{O}(l)$</td><td>$-237.1$</td></tr></tbody></table>'
        ),
        "question": (
            r"Using the standard Gibbs free energies of formation above, what is $\Delta G_{\text{rxn}}^\circ$ at $298\text{ K}$ for the complete combustion of methane: $\text{CH}_4(g) + 2\text{O}_2(g) \rightarrow \text{CO}_2(g) + 2\text{H}_2\text{O}(l)$?"
        ),
        "options": [
            r"$-580.7\text{ kJ mol}_{\text{rxn}}^{-1}$",
            r"$-817.8\text{ kJ mol}_{\text{rxn}}^{-1}$",
            r"$-919.4\text{ kJ mol}_{\text{rxn}}^{-1}$",
            r"$+817.8\text{ kJ mol}_{\text{rxn}}^{-1}$",
        ],
        "correct_index": 1,
        "explanation": (
            r"Since $\text{O}_2(g)$ is an element in its standard state, $\Delta G_f^\circ(\text{O}_2(g)) = 0$. "
            r"$\Delta G_{\text{rxn}}^\circ = [\Delta G_f^\circ(\text{CO}_2) + 2\Delta G_f^\circ(\text{H}_2\text{O})] - [\Delta G_f^\circ(\text{CH}_4) + 0] = [-394.4 + 2(-237.1)] - (-50.8) = -868.6 + 50.8 = -817.8\text{ kJ mol}_{\text{rxn}}^{-1}$."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 9.4: Thermodynamic and Kinetic Control (Q16–Q20)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 16,
        "topic_code": "9.4",
        "topic_title": "Thermodynamic and Kinetic Control",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r"$$\text{C}(\text{diamond}) \rightarrow \text{C}(\text{graphite}) \qquad \Delta G^\circ_{298} = -2.90\text{ kJ mol}_{\text{rxn}}^{-1}$$"
        ),
        "question": (
            r"Although the conversion of diamond to graphite has a negative standard free energy change ($\Delta G^\circ < 0$) at $298\text{ K}$ and $1\text{ atm}$, diamonds do not noticeably convert into graphite over human lifetimes at room temperature. Which statement best explains this observation?"
        ),
        "options": [
            r"The reaction is under kinetic control because breaking the strong 3D network of $\text{C}-\text{C}$ covalent bonds in diamond requires a very large activation energy ($E_a$).",
            r"A negative $\Delta G^\circ$ indicates that the reverse reaction is faster than the forward reaction.",
            r"The entropy change $\Delta S^\circ$ for converting diamond to graphite is negative, preventing the reaction from occurring.",
            r"At $298\text{ K}$, the equilibrium constant $K$ for the conversion is much less than $1$.",
        ],
        "correct_index": 0,
        "explanation": (
            r"A reaction with $\Delta G^\circ < 0$ is thermodynamically favorable ($K > 1$), but if it proceeds at a negligible rate, it is under <strong>kinetic control</strong> due to a high activation energy barrier ($E_a$) associated with rearranging covalent network bonds."
        ),
    },
    {
        "unit_q_num": 17,
        "topic_code": "9.4",
        "topic_title": "Thermodynamic and Kinetic Control",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"A mixture of $\text{H}_2(g)$ and $\text{O}_2(g)$ can be stored in a sealed glass vessel at $298\text{ K}$ for years with no measurable formation of $\text{H}_2\text{O}(l)$, even though $\Delta G_{\text{rxn}}^\circ = -474\text{ kJ mol}_{\text{rxn}}^{-1}$. However, introducing a tiny platinum wire or a spark causes an immediate explosion. What is the role of the platinum wire?"
        ),
        "options": [
            r"It makes $\Delta G_{\text{rxn}}^\circ$ more negative so that the reaction becomes thermodynamically favorable.",
            r"It shifts the equilibrium constant $K$ toward the products.",
            r"It provides an alternative reaction pathway with a lower activation energy ($E_a$), overcoming kinetic control without changing $\Delta G_{\text{rxn}}^\circ$.",
            r"It increases the enthalpy of the products relative to the reactants.",
        ],
        "correct_index": 2,
        "explanation": (
            r"The $\text{H}_2 + \text{O}_2$ reaction is thermodynamically favorable ($\Delta G^\circ \ll 0$) but kinetically hindered by the high $E_a$ of breaking $\text{H}-\text{H}$ and $\text{O}=\text{O}$ bonds. Platinum acts as a heterogeneous catalyst, lowering $E_a$ without altering state functions ($\Delta G^\circ, \Delta H^\circ, \Delta S^\circ$) or $K$."
        ),
    },
    {
        "unit_q_num": 18,
        "topic_code": "9.4",
        "topic_title": "Thermodynamic and Kinetic Control",
        "difficulty": "Challenging",
        "stimulus": (
            r'<table class="quiz-data-table"><thead><tr><th>Reaction</th><th>$\Delta G^\circ_{298}\ (\text{kJ mol}_{\text{rxn}}^{-1})$</th><th>$E_a\ (\text{kJ mol}^{-1})$</th></tr></thead>'
            r'<tbody><tr><td>I</td><td>$-30$</td><td>$20$</td></tr>'
            r'<tr><td>II</td><td>$+40$</td><td>$50$</td></tr>'
            r'<tr><td>III</td><td>$-150$</td><td>$190$</td></tr>'
            r'<tr><td>IV</td><td>$+25$</td><td>$240$</td></tr></tbody></table>'
        ),
        "question": (
            r"The table above gives the standard free energy change at $298\text{ K}$ and the activation energy of the forward reaction for four different reactions. When the reactants of each reaction are mixed at $298\text{ K}$, which reaction is best described as being under kinetic control?"
        ),
        "options": [
            r"Reaction I, because its small activation energy means that its progress is determined by its rate rather than by $\Delta G^\circ$.",
            r"Reaction II, because a reaction with $\Delta G^\circ > 0$ cannot proceed at a measurable rate.",
            r"Reaction III, because it is thermodynamically favored ($\Delta G^\circ < 0$), but its large activation energy makes its rate negligible at $298\text{ K}$.",
            r"Reaction IV, because it has the largest activation energy and therefore cannot proceed at a measurable rate at $298\text{ K}$.",
        ],
        "correct_index": 2,
        "explanation": (
            r"A process is under <strong>kinetic control</strong> when it is thermodynamically favored ($\Delta G^\circ < 0$, so $K > 1$) but does not proceed at a measurable rate, most often because its activation energy is high. Reaction III meets both conditions: $\Delta G^\circ = -150\text{ kJ mol}_{\text{rxn}}^{-1}$ ($K \gg 1$), yet with $E_a = 190\text{ kJ mol}^{-1}$ almost no collisions at $298\text{ K}$ have enough energy to react. A mixture of its reactants that shows no measurable change is therefore not at equilibrium. Reaction IV also has a large $E_a$, but its products are not thermodynamically favored ($K < 1$), so the term does not apply. Reaction II is limited by thermodynamics ($K \ll 1$), not by its rate, and Reaction I, which is favored and has a small $E_a$, proceeds readily."
        ),
    },
    {
        "unit_q_num": 19,
        "topic_code": "9.4",
        "topic_title": "Thermodynamic and Kinetic Control",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"Hydrogen peroxide decomposes according to $2\text{H}_2\text{O}_2(aq) \rightarrow 2\text{H}_2\text{O}(l) + \text{O}_2(g)$ with $\Delta H^\circ = -189\text{ kJ mol}_{\text{rxn}}^{-1}$ and $\Delta S^\circ = +57\text{ J mol}_{\text{rxn}}^{-1}\text{ K}^{-1}$. Why can aqueous $\text{H}_2\text{O}_2$ be sold in pharmacies and stored for months in dark plastic bottles?"
        ),
        "options": [
            r"Although the decomposition is thermodynamically favorable at all temperatures ($\Delta H^\circ < 0, \Delta S^\circ > 0$), the uncatalyzed activation energy is high at room temperature in the absence of light or transition-metal catalysts.",
            r"The decomposition is thermodynamically unfavorable below $373\text{ K}$ because $\Delta S^\circ$ is positive.",
            r"The dark bottle increases the equilibrium constant $K$ of the reverse reaction.",
            r"At room temperature, $\Delta G^\circ = 0$ for the decomposition of $\text{H}_2\text{O}_2(aq)$.",
        ],
        "correct_index": 0,
        "explanation": (
            r"Since $\Delta H^\circ < 0$ and $\Delta S^\circ > 0$, $\Delta G^\circ < 0$ at all temperatures. Its long shelf life in dark bottles is due to kinetic control: the uncatalyzed reaction has a high $E_a$, and blocking UV light prevents photochemical homolytic cleavage of the $\text{O}-\text{O}$ bond."
        ),
    },
    {
        "unit_q_num": 20,
        "topic_code": "9.4",
        "topic_title": "Thermodynamic and Kinetic Control",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"Which of the following statements about a thermodynamically unfavorable reaction ($\Delta G^\circ > 0$) is ALWAYS true?"
        ),
        "options": [
            r"The activation energy of the forward reaction is smaller than the activation energy of the reverse reaction.",
            r"The reaction must be endothermic ($\Delta H^\circ > 0$) and have $\Delta S^\circ > 0$.",
            r"Adding a catalyst will change the sign of $\Delta G^\circ$ from positive to negative.",
            r"The equilibrium constant $K$ is less than $1$, regardless of whether a catalyst is added.",
        ],
        "correct_index": 3,
        "explanation": (
            r"From $\Delta G^\circ = -RT\ln K$, whenever $\Delta G^\circ > 0$, $\ln K < 0$ and therefore $K < 1$. A catalyst lowers $E_{a,\text{fwd}}$ and $E_{a,\text{rev}}$ equally and cannot change $\Delta G^\circ$ or $K$."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 9.5: Free Energy and Equilibrium (Q21–Q25)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 21,
        "topic_code": "9.5",
        "topic_title": "Free Energy and Equilibrium",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"For a reversible reaction at $298\text{ K}$, the standard Gibbs free energy change is $\Delta G^\circ = 0\text{ kJ mol}_{\text{rxn}}^{-1}$. What is the value of the thermodynamic equilibrium constant $K$ at $298\text{ K}$?"
        ),
        "options": [
            r"$K = 0$",
            r"$K = 1$",
            r"$K = 8.314$",
            r"$K = 298$",
        ],
        "correct_index": 1,
        "explanation": (
            r"Since $\Delta G^\circ = -RT\ln K$, setting $\Delta G^\circ = 0$ gives $\ln K = 0$, which means $K = e^0 = 1$."
        ),
    },
    {
        "unit_q_num": 22,
        "topic_code": "9.5",
        "topic_title": "Free Energy and Equilibrium",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r'<table class="quiz-data-table"><thead><tr><th>Acid</th><th>$K_a$ at $298\text{ K}$</th></tr></thead>'
            r'<tbody><tr><td>$\text{HF}(aq)$</td><td>$6.8 \times 10^{-4}$</td></tr>'
            r'<tr><td>$\text{CH}_3\text{COOH}(aq)$</td><td>$1.8 \times 10^{-5}$</td></tr>'
            r'<tr><td>$\text{HCN}(aq)$</td><td>$6.2 \times 10^{-10}$</td></tr></tbody></table>'
        ),
        "question": (
            r"Based on the acid dissociation constants ($K_a$) at $298\text{ K}$ given above, what is true about $\Delta G^\circ$ for the ionization of these three weak acids in water ($\text{HA}(aq) + \text{H}_2\text{O}(l) \rightleftharpoons \text{H}_3\text{O}^+(aq) + \text{A}^-(aq)$)?"
        ),
        "options": [
            r"$\Delta G^\circ < 0$ for all three acids, and $\text{HF}$ has the most negative $\Delta G^\circ$.",
            r"$\Delta G^\circ = 0$ for all three acids because each system reaches equilibrium.",
            r"$\Delta G^\circ > 0$ for all three acids, and $\text{HCN}$ has the most positive $\Delta G^\circ$.",
            r"$\Delta G^\circ > 0$ for $\text{HCN}$, but $\Delta G^\circ < 0$ for $\text{HF}$.",
        ],
        "correct_index": 2,
        "explanation": (
            r"For all three weak acids, $K_a < 1$, so $\ln K_a < 0$ and $\Delta G^\circ = -RT\ln K_a > 0$. Because $\text{HCN}$ has the smallest $K_a$ ($6.2 \times 10^{-10}$), $\ln K_a$ is the most negative, making $\Delta G^\circ$ the most positive."
        ),
    },
    {
        "unit_q_num": 23,
        "topic_code": "9.5",
        "topic_title": "Free Energy and Equilibrium",
        "difficulty": "Challenging",
        "stimulus": (
            r"$$\text{N}_2\text{O}_4(g) \rightleftharpoons 2\text{NO}_2(g) \qquad \Delta G^\circ_{298} = +4.73\text{ kJ mol}_{\text{rxn}}^{-1}$$"
        ),
        "question": (
            r"At $298\text{ K}$, a rigid vessel initially contains $P_{\text{N}_2\text{O}_4} = 1.0\text{ atm}$ and $P_{\text{NO}_2} = 1.0\text{ atm}$. Which statement correctly describes the values of $\Delta G^\circ$, $\Delta G$, and the direction of net reaction at this initial moment?"
        ),
        "options": [
            r"$\Delta G^\circ = +4.73\text{ kJ mol}^{-1}$ and $\Delta G = +4.73\text{ kJ mol}^{-1}$; the reaction proceeds toward the reactants ($\text{N}_2\text{O}_4$) because $Q = 1 > K$.",
            r"$\Delta G^\circ = +4.73\text{ kJ mol}^{-1}$ and $\Delta G = 0$; the system is already at equilibrium because all partial pressures are $1.0\text{ atm}$.",
            r"$\Delta G^\circ = 0$ and $\Delta G = +4.73\text{ kJ mol}^{-1}$; the reaction proceeds toward the products ($\text{NO}_2$).",
            r"$\Delta G^\circ = +4.73\text{ kJ mol}^{-1}$ and $\Delta G < 0$; the reaction proceeds toward the products until $P_{\text{N}_2\text{O}_4} = 0$.",
        ],
        "correct_index": 0,
        "explanation": (
            r"When all gases are at $1.0\text{ atm}$ (standard state), $Q_p = \frac{(1.0)^2}{1.0} = 1.0$, so $\Delta G = \Delta G^\circ + RT\ln Q = \Delta G^\circ + 0 = +4.73\text{ kJ mol}^{-1}$. Since $\Delta G^\circ > 0$, $K_p < 1$. Therefore $Q_p = 1 > K_p$ (and $\Delta G > 0$), meaning the reverse reaction (toward $\text{N}_2\text{O}_4$) is thermodynamically favored until $Q_p = K_p$ and $\Delta G = 0$."
        ),
    },
    {
        "unit_q_num": 24,
        "topic_code": "9.5",
        "topic_title": "Free Energy and Equilibrium",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"For a reaction with $\Delta G^\circ = -17.1\text{ kJ mol}_{\text{rxn}}^{-1}$ at $298\text{ K}$ ($RT \approx 2.48\text{ kJ mol}^{-1}$), what is the approximate value of the equilibrium constant $K$? (Note: $\ln(1000) \approx 6.9$)"
        ),
        "options": [
            r"$K \approx 1 \times 10^{-3}$",
            r"$K \approx 0.993$",
            r"$K \approx 6.9$",
            r"$K \approx 1 \times 10^{3}$",
        ],
        "correct_index": 3,
        "explanation": (
            r"Using $\ln K = -\frac{\Delta G^\circ}{RT} = -\frac{-17.1\text{ kJ mol}^{-1}}{2.48\text{ kJ mol}^{-1}} \approx +6.90$. Since $\ln(10^3) = 3\ln(10) \approx 6.91$, $K = e^{6.90} \approx 1 \times 10^3$."
        ),
    },
    {
        "unit_q_num": 25,
        "topic_code": "9.5",
        "topic_title": "Free Energy and Equilibrium",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"As a reversible chemical reaction proceeds toward equilibrium at constant temperature and pressure, how do $\Delta G$ (instantaneous free energy change) and $\Delta G^\circ$ (standard free energy change) behave?"
        ),
        "options": [
            r"Both $\Delta G$ and $\Delta G^\circ$ approach zero as equilibrium is reached.",
            r"$\Delta G$ approaches zero as $Q$ approaches $K$, while $\Delta G^\circ$ remains constant.",
            r"$\Delta G$ remains constant while $\Delta G^\circ$ approaches zero.",
            r"$\Delta G$ becomes increasingly negative until all reactants are consumed.",
        ],
        "correct_index": 1,
        "explanation": (
            r"$\Delta G^\circ = -RT\ln K$ is a constant at a given temperature because it refers to fixed standard states ($Q = 1$). In contrast, $\Delta G = \Delta G^\circ + RT\ln Q = RT\ln(Q/K)$ changes as concentrations change, reaching $\Delta G = 0$ at equilibrium ($Q = K$)."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 9.7: Coupled Reactions (Q26–Q30)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 26,
        "topic_code": "9.7",
        "topic_title": "Coupled Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r'<table class="quiz-data-table"><thead><tr><th>Reaction</th><th>$\Delta G^\circ\ (\text{kJ mol}_{\text{rxn}}^{-1})$ at $298\text{ K}$</th></tr></thead>'
            r'<tbody><tr><td>$\text{Fe}_2\text{O}_3(s) \rightarrow 2\text{Fe}(s) + \frac{3}{2}\text{O}_2(g)$</td><td>$+742$</td></tr>'
            r'<tr><td>$\text{CO}(g) + \frac{1}{2}\text{O}_2(g) \rightarrow \text{CO}_2(g)$</td><td>$-257$</td></tr></tbody></table>'
        ),
        "question": (
            r"Direct thermal decomposition of $\text{Fe}_2\text{O}_3(s)$ is thermodynamically unfavorable ($\Delta G^\circ = +742\text{ kJ mol}_{\text{rxn}}^{-1}$). In a blast furnace, this reaction is coupled with the oxidation of $\text{CO}(g)$ to $\text{CO}_2(g)$: $\text{Fe}_2\text{O}_3(s) + 3\text{CO}(g) \rightarrow 2\text{Fe}(s) + 3\text{CO}_2(g)$. What is $\Delta G^\circ$ for the overall coupled reaction?"
        ),
        "options": [
            r"$-1028\text{ kJ mol}_{\text{rxn}}^{-1}$",
            r"$-29\text{ kJ mol}_{\text{rxn}}^{-1}$",
            r"$+485\text{ kJ mol}_{\text{rxn}}^{-1}$",
            r"$+1513\text{ kJ mol}_{\text{rxn}}^{-1}$",
        ],
        "correct_index": 1,
        "explanation": (
            r"To cancel $\frac{3}{2}\text{O}_2(g)$, multiply the second reaction by $3$: $3\text{CO}(g) + \frac{3}{2}\text{O}_2(g) \rightarrow 3\text{CO}_2(g)$ with $\Delta G_2^\circ = 3(-257) = -771\text{ kJ mol}_{\text{rxn}}^{-1}$. Adding to the first reaction gives $\Delta G_{\text{overall}}^\circ = +742 + (-771) = -29\text{ kJ mol}_{\text{rxn}}^{-1}$, making iron smelting thermodynamically favorable!"
        ),
    },
    {
        "unit_q_num": 27,
        "topic_code": "9.7",
        "topic_title": "Coupled Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r'<table class="quiz-data-table"><thead><tr><th>Biochemical Reaction at $298\text{ K}$ ($\text{pH } 7$)</th><th>$\Delta G^{\circ\prime}\ (\text{kJ mol}_{\text{rxn}}^{-1})$</th></tr></thead>'
            r'<tbody><tr><td>$\text{Glutamate} + \text{NH}_4^+ \rightarrow \text{Glutamine} + \text{H}_2\text{O}$</td><td>$+14.2$</td></tr>'
            r'<tr><td>$\text{ATP} + \text{H}_2\text{O} \rightarrow \text{ADP} + \text{P}_i$</td><td>$-30.5$</td></tr></tbody></table>'
        ),
        "question": (
            r"In living cells, the synthesis of glutamine from glutamate and ammonium ion is coupled to the hydrolysis of $\text{ATP}$ via a shared phosphorylated intermediate. What is $\Delta G^{\circ\prime}$ for the net coupled reaction, and why is coupling necessary?"
        ),
        "options": [
            r"$\Delta G^{\circ\prime} = +44.7\text{ kJ mol}_{\text{rxn}}^{-1}$; ATP acts only as a catalyst to lower activation energy.",
            r"$\Delta G^{\circ\prime} = -16.3\text{ kJ mol}_{\text{rxn}}^{-1}$; ATP hydrolysis changes the $\Delta G^{\circ\prime}$ of the isolated glutamate reaction to $-14.2\text{ kJ mol}_{\text{rxn}}^{-1}$.",
            r"$\Delta G^{\circ\prime} = -16.3\text{ kJ mol}_{\text{rxn}}^{-1}$; coupling pairs an unfavorable reaction ($\Delta G^{\circ\prime} > 0$) with a more strongly favorable reaction ($\Delta G^{\circ\prime} \ll 0$) through a shared intermediate so net $\Delta G^{\circ\prime} < 0$.",
            r"$\Delta G^{\circ\prime} = -433\text{ kJ mol}_{\text{rxn}}^{-1}$; the free energies are multiplied when reactions are coupled.",
        ],
        "correct_index": 2,
        "explanation": (
            r"By Hess's Law for state functions, summing the two reactions gives $\Delta G_{\text{net}}^{\circ\prime} = +14.2 + (-30.5) = -16.3\text{ kJ mol}_{\text{rxn}}^{-1} < 0$. Coupling works when a thermodynamically unfavorable step shares a common intermediate with a thermodynamically favorable step whose $|\Delta G^\circ|$ is larger."
        ),
    },
    {
        "unit_q_num": 28,
        "topic_code": "9.7",
        "topic_title": "Coupled Reactions",
        "difficulty": "Challenging",
        "stimulus": (
            r"$$\text{Cu}_2\text{S}(s) \rightarrow 2\text{Cu}(s) + \text{S}(s) \qquad \Delta G^\circ = +86.2\text{ kJ mol}_{\text{rxn}}^{-1}$$"
            r"$$\text{S}(s) + \text{O}_2(g) \rightarrow \text{SO}_2(g) \qquad \Delta G^\circ = -300.1\text{ kJ mol}_{\text{rxn}}^{-1}$$"
        ),
        "question": (
            r"Based on the two equations above, what is the equilibrium constant $K$ expression and thermodynamic favorability for the coupled roasting of chalcocite ore: $\text{Cu}_2\text{S}(s) + \text{O}_2(g) \rightleftharpoons 2\text{Cu}(s) + \text{SO}_2(g)$?"
        ),
        "options": [
            r"$\Delta G_{\text{net}}^\circ = +386.3\text{ kJ mol}_{\text{rxn}}^{-1}$ (unfavorable) and $K_{\text{net}} = K_1 + K_2$",
            r"$\Delta G_{\text{net}}^\circ = -213.9\text{ kJ mol}_{\text{rxn}}^{-1}$ (favorable) and $K_{\text{net}} = K_1 \times K_2$",
            r"$\Delta G_{\text{net}}^\circ = -213.9\text{ kJ mol}_{\text{rxn}}^{-1}$ (favorable) and $K_{\text{net}} = K_1 + K_2$",
            r"$\Delta G_{\text{net}}^\circ = +213.9\text{ kJ mol}_{\text{rxn}}^{-1}$ (unfavorable) and $K_{\text{net}} = K_1 / K_2$",
        ],
        "correct_index": 1,
        "explanation": (
            r"Adding the two reactions cancels $\text{S}(s)$, giving $\Delta G_{\text{net}}^\circ = \Delta G_1^\circ + \Delta G_2^\circ = +86.2 + (-300.1) = -213.9\text{ kJ mol}_{\text{rxn}}^{-1} < 0$. When reactions are added, their $\Delta G^\circ$ values add and their equilibrium constants multiply ($K_{\text{net}} = K_1 \times K_2$)."
        ),
    },
    {
        "unit_q_num": 29,
        "topic_code": "9.7",
        "topic_title": "Coupled Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"Suppose Reaction 1 has $\Delta G_1^\circ = +45\text{ kJ mol}_{\text{rxn}}^{-1}$. Which of the following reactions could be coupled in a 1:1 stoichiometric ratio with Reaction 1 (via a shared intermediate) to make the overall coupled process thermodynamically favorable under standard conditions?"
        ),
        "options": [
            r"Reaction A with $\Delta G^\circ = -30\text{ kJ mol}_{\text{rxn}}^{-1}$",
            r"Reaction B with $\Delta G^\circ = +60\text{ kJ mol}_{\text{rxn}}^{-1}$",
            r"Reaction C with $\Delta G^\circ = -55\text{ kJ mol}_{\text{rxn}}^{-1}$",
            r"Reaction D with $\Delta G^\circ = 0\text{ kJ mol}_{\text{rxn}}^{-1}$",
        ],
        "correct_index": 2,
        "explanation": (
            r"For the overall coupled reaction to be thermodynamically favorable ($\Delta G_{\text{overall}}^\circ = \Delta G_1^\circ + \Delta G_2^\circ < 0$), we need $\Delta G_2^\circ < -45\text{ kJ mol}_{\text{rxn}}^{-1}$. Reaction C ($\Delta G^\circ = -55\text{ kJ mol}_{\text{rxn}}^{-1}$) gives $\Delta G_{\text{overall}}^\circ = +45 - 55 = -10\text{ kJ mol}_{\text{rxn}}^{-1} < 0$."
        ),
    },
    {
        "unit_q_num": 30,
        "topic_code": "9.7",
        "topic_title": "Coupled Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"In an electrolytic cell, an external power supply is used to drive the thermodynamically unfavorable decomposition of molten $\text{NaCl}(l)$ into $\text{Na}(l)$ and $\text{Cl}_2(g)$ ($\Delta G^\circ > 0$). How is this process an example of coupling?"
        ),
        "options": [
            r"The external voltage lowers the standard enthalpy of formation of $\text{NaCl}(l)$ to zero.",
            r"The electrical current reverses the sign of $\Delta S^\circ$ for $\text{Cl}_2(g)$ formation.",
            r"The electrodes act purely as chemical catalysts that change $K$ without supplying energy.",
            r"Electrical work supplied by the external source (where $\Delta G_{\text{source}} < 0$ and $|\Delta G_{\text{source}}| > \Delta G_{\text{rxn}}^\circ$) is coupled to the unfavorable redox reaction to drive it forward.",
        ],
        "correct_index": 3,
        "explanation": (
            r"External electrical energy (or light in photosynthesis/photochemistry) can be coupled to a thermodynamically unfavorable reaction ($\Delta G^\circ > 0$) to drive the net process forward, provided the external energy input exceeds $\Delta G^\circ$."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 9.8: Galvanic (Voltaic) and Electrolytic Cells (Q31–Q35)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 31,
        "topic_code": "9.8",
        "topic_title": "Galvanic (Voltaic) and Electrolytic Cells",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r'<table class="quiz-data-table"><thead><tr><th>Half-Reaction</th><th>$E^\circ\ (\text{V})$</th></tr></thead>'
            r'<tbody><tr><td>$\text{Ag}^+(aq) + e^- \rightarrow \text{Ag}(s)$</td><td>$+0.80$</td></tr>'
            r'<tr><td>$\text{Ni}^{2+}(aq) + 2e^- \rightarrow \text{Ni}(s)$</td><td>$-0.25$</td></tr></tbody></table>'
        ),
        "question": (
            r"A standard galvanic cell is constructed using a $\text{Ni}(s)|\text{Ni}^{2+}(aq)$ half-cell and an $\text{Ag}(s)|\text{Ag}^+(aq)$ half-cell connected by a $\text{KNO}_3(aq)$ salt bridge. Which of the following statements is correct as the cell operates?"
        ),
        "options": [
            r"Electrons flow through the salt bridge from the $\text{Ag}$ electrode to the $\text{Ni}$ electrode.",
            r"The mass of the $\text{Ni}$ electrode increases while the mass of the $\text{Ag}$ electrode decreases.",
            r"Electrons flow through the external wire from the $\text{Ni}$ electrode to the $\text{Ag}$ electrode, and $\text{NO}_3^-$ ions migrate through the salt bridge into the $\text{Ni}^{2+}$ half-cell.",
            r"$\text{K}^+$ ions migrate through the salt bridge into the $\text{Ni}^{2+}$ anode compartment.",
        ],
        "correct_index": 2,
        "explanation": (
            r"Because $\text{Ag}^+$ has the more positive reduction potential ($+0.80\text{ V} > -0.25\text{ V}$), $\text{Ag}$ is the cathode (reduction: $\text{Ag}^+ + e^- \rightarrow \text{Ag}$) and $\text{Ni}$ is the anode (oxidation: $\text{Ni} \rightarrow \text{Ni}^{2+} + 2e^-$). Electrons flow through the external wire from anode ($\text{Ni}$) to cathode ($\text{Ag}$). To maintain charge neutrality as $\text{Ni}^{2+}$ cations are produced at the anode, $\text{NO}_3^-$ anions flow from the salt bridge into the $\text{Ni}^{2+}$ compartment."
        ),
    },
    {
        "unit_q_num": 32,
        "topic_code": "9.8",
        "topic_title": "Galvanic (Voltaic) and Electrolytic Cells",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"If the salt bridge is removed from an operating galvanic cell, what happens immediately to the cell voltage and why?"
        ),
        "options": [
            r"The voltage drops to zero because charge builds up rapidly in both half-cells (excess positive charge in the anode solution and excess negative charge in the cathode solution), opposing further electron flow.",
            r"The voltage doubles because the internal resistance of the salt bridge is eliminated.",
            r"Electrons begin flowing directly through the aqueous solutions between the beakers.",
            r"The anode and cathode swap polarities and the cell runs in reverse.",
        ],
        "correct_index": 0,
        "explanation": (
            r"Without ion migration through the salt bridge to balance the charge of cations produced at the anode and consumed at the cathode, local charge accumulation immediately halts electron transfer, dropping $E_{\text{cell}}$ to $0\text{ V}$."
        ),
    },
    {
        "unit_q_num": 33,
        "topic_code": "9.8",
        "topic_title": "Galvanic (Voltaic) and Electrolytic Cells",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"Which statement is true for BOTH a galvanic (voltaic) cell and an electrolytic cell?"
        ),
        "options": [
            r"The cell potential $E_{\text{cell}}^\circ$ is positive and $\Delta G^\circ$ is negative.",
            r"Electrons flow through the solutions and the salt bridge from the cathode back to the anode to complete the circuit.",
            r"Reduction occurs at the anode and oxidation occurs at the cathode.",
            r"Oxidation occurs at the anode, reduction occurs at the cathode, and electrons flow through the external circuit from the anode to the cathode.",
        ],
        "correct_index": 3,
        "explanation": (
            r"By definition in all electrochemical cells, oxidation occurs at the anode (<strong>An Ox</strong>) and reduction at the cathode (<strong>Red Cat</strong>), and electrons always travel through the external wire from the anode (where they are lost) to the cathode (where they are gained). Inside the cell, the circuit is completed by the migration of ions, not electrons. A positive $E_{\text{cell}}^\circ$ and negative $\Delta G^\circ$ describe only galvanic cells; electrolytic cells have $E_{\text{cell}}^\circ < 0$ and $\Delta G^\circ > 0$."
        ),
    },
    {
        "unit_q_num": 34,
        "topic_code": "9.8",
        "topic_title": "Galvanic (Voltaic) and Electrolytic Cells",
        "difficulty": "Challenging",
        "stimulus": (
            r'<table class="quiz-data-table"><thead><tr><th>Half-Reaction</th><th>$E^\circ\ (\text{V})$</th></tr></thead>'
            r'<tbody><tr><td>$\text{Cl}_2(g) + 2e^- \rightarrow 2\text{Cl}^-(aq)$</td><td>$+1.36$</td></tr>'
            r'<tr><td>$\text{O}_2(g) + 4\text{H}^+(aq) + 4e^- \rightarrow 2\text{H}_2\text{O}(l)$</td><td>$+1.23$</td></tr>'
            r'<tr><td>$\text{Cu}^{2+}(aq) + 2e^- \rightarrow \text{Cu}(s)$</td><td>$+0.34$</td></tr>'
            r'<tr><td>$2\text{H}_2\text{O}(l) + 2e^- \rightarrow \text{H}_2(g) + 2\text{OH}^-(aq)$</td><td>$-0.83$</td></tr>'
            r'<tr><td>$\text{Na}^+(aq) + e^- \rightarrow \text{Na}(s)$</td><td>$-2.71$</td></tr></tbody></table>'
        ),
        "question": (
            r"An aqueous solution of $1.0\text{ M NaCl}$ is electrolyzed using inert platinum electrodes. Based on the standard reduction potentials in the table above, what substance is produced at the cathode?"
        ),
        "options": [
            r"$\text{Na}(s)$ metal, because $\text{Na}^+$ is in $1.0\text{ M}$ concentration.",
            r"$\text{Cl}_2(g)$, because chloride ions are reduced at the cathode.",
            r"$\text{H}_2(g)$ and $\text{OH}^-(aq)$, because water has a much less negative reduction potential ($-0.83\text{ V}$) than $\text{Na}^+(aq)$ ($-2.71\text{ V}$).",
            r"$\text{O}_2(g)$, because water is oxidized at the cathode.",
        ],
        "correct_index": 2,
        "explanation": (
            r"At the cathode (reduction) in aqueous $\text{NaCl}(aq)$, the two competing reducible species are $\text{Na}^+(aq)$ ($E^\circ = -2.71\text{ V}$) and $\text{H}_2\text{O}(l)$ ($E^\circ = -0.83\text{ V}$). The species with the higher (less negative) reduction potential is reduced first, so $\text{H}_2\text{O}$ is reduced to $\text{H}_2(g)$ and $\text{OH}^-(aq)$. Forming $\text{Cl}_2$ from $\text{Cl}^-$ and forming $\text{O}_2$ from $\text{H}_2\text{O}$ are oxidations, which can occur only at the anode."
        ),
    },
    {
        "unit_q_num": 35,
        "topic_code": "9.8",
        "topic_title": "Galvanic (Voltaic) and Electrolytic Cells",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r"$$\text{Zn}(s) + \text{Cu}^{2+}(aq) \rightarrow \text{Zn}^{2+}(aq) + \text{Cu}(s) \qquad E_{\text{cell}}^\circ = +1.10\text{ V}$$"
        ),
        "question": (
            r"In a standard $\text{Zn}-\text{Cu}$ galvanic cell operating according to the reaction above, how do the masses of the two metal electrodes change after $0.10\text{ mol}$ of electrons have passed through the external wire?"
        ),
        "options": [
            r"The $\text{Zn}$ anode loses $0.10\text{ mol}$ ($6.54\text{ g}$) of $\text{Zn}$, and the $\text{Cu}$ cathode gains $0.10\text{ mol}$ ($6.36\text{ g}$) of $\text{Cu}$.",
            r"The $\text{Zn}$ anode loses $0.050\text{ mol}$ ($3.27\text{ g}$) of $\text{Zn}$, and the $\text{Cu}$ cathode gains $0.050\text{ mol}$ ($3.18\text{ g}$) of $\text{Cu}$.",
            r"The $\text{Zn}$ electrode gains $3.27\text{ g}$ and the $\text{Cu}$ electrode loses $3.18\text{ g}$.",
            r"Neither electrode changes mass because electrons have negligible mass.",
        ],
        "correct_index": 1,
        "explanation": (
            r"Each half-reaction transfers $2e^-$ per mole of metal ($\text{Zn} \rightarrow \text{Zn}^{2+} + 2e^-$ and $\text{Cu}^{2+} + 2e^- \rightarrow \text{Cu}$). Thus $0.10\text{ mol } e^-$ corresponds to $0.050\text{ mol}$ of $\text{Zn}$ oxidized ($0.050 \times 65.38 = 3.27\text{ g}$ lost at anode) and $0.050\text{ mol}$ of $\text{Cu}$ plated out ($0.050 \times 63.55 = 3.18\text{ g}$ gained at cathode)."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 9.9: Cell Potential and Free Energy (Q36–Q40)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 36,
        "topic_code": "9.9",
        "topic_title": "Cell Potential and Free Energy",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r'<table class="quiz-data-table"><thead><tr><th>Half-Reaction</th><th>$E^\circ\ (\text{V})$</th></tr></thead>'
            r'<tbody><tr><td>$\text{Au}^{3+}(aq) + 3e^- \rightarrow \text{Au}(s)$</td><td>$+1.50$</td></tr>'
            r'<tr><td>$\text{Fe}^{2+}(aq) + 2e^- \rightarrow \text{Fe}(s)$</td><td>$-0.44$</td></tr></tbody></table>'
        ),
        "question": (
            r"Using the standard reduction potentials above, what are the standard cell potential $E_{\text{cell}}^\circ$ and the number of moles of electrons $n$ transferred in the balanced equation for the thermodynamically favorable reaction between $\text{Au}^{3+}(aq)$ and $\text{Fe}(s)$?"
        ),
        "options": [
            r"$E_{\text{cell}}^\circ = +1.94\text{ V}$ and $n = 6$",
            r"$E_{\text{cell}}^\circ = +4.32\text{ V}$ and $n = 6$",
            r"$E_{\text{cell}}^\circ = +1.06\text{ V}$ and $n = 5$",
            r"$E_{\text{cell}}^\circ = -1.94\text{ V}$ and $n = 6$",
        ],
        "correct_index": 0,
        "explanation": (
            r"Standard reduction potential is an <strong>intensive property</strong> ($\text{V} = \text{J/C}$), so stoichiometric coefficients do NOT multiply $E^\circ$: $E_{\text{cell}}^\circ = E_{\text{cathode}}^\circ - E_{\text{anode}}^\circ = +1.50 - (-0.44) = +1.94\text{ V}$. Balancing electrons between $3e^-$ and $2e^-$ gives $2\text{Au}^{3+} + 3\text{Fe} \rightarrow 2\text{Au} + 3\text{Fe}^{2+}$, so $n = 6\text{ mol } e^-$."
        ),
    },
    {
        "unit_q_num": 37,
        "topic_code": "9.9",
        "topic_title": "Cell Potential and Free Energy",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r"$$2\text{Al}(s) + 3\text{Cu}^{2+}(aq) \rightarrow 2\text{Al}^{3+}(aq) + 3\text{Cu}(s) \qquad E_{\text{cell}}^\circ = +2.00\text{ V}$$"
        ),
        "question": (
            r"For the reaction shown above at $298\text{ K}$ ($F = 96,485\text{ C mol}^{-1}$), what is the value of $\Delta G_{\text{rxn}}^\circ$?"
        ),
        "options": [
            r"$+1158\text{ kJ mol}_{\text{rxn}}^{-1}$",
            r"$-193\text{ kJ mol}_{\text{rxn}}^{-1}$",
            r"$-386\text{ kJ mol}_{\text{rxn}}^{-1}$",
            r"$-1158\text{ kJ mol}_{\text{rxn}}^{-1}$",
        ],
        "correct_index": 3,
        "explanation": (
            r"The balanced equation transfers $n = 6\text{ mol } e^-$ per mole of reaction ($2\text{Al} \rightarrow 2\text{Al}^{3+} + 6e^-$). Using $\Delta G^\circ = -nFE_{\text{cell}}^\circ = -(6\text{ mol } e^-)(96,485\text{ C mol}^{-1})(2.00\text{ J C}^{-1}) = -1,157,820\text{ J mol}_{\text{rxn}}^{-1} \approx -1158\text{ kJ mol}_{\text{rxn}}^{-1}$."
        ),
    },
    {
        "unit_q_num": 38,
        "topic_code": "9.9",
        "topic_title": "Cell Potential and Free Energy",
        "difficulty": "Challenging",
        "stimulus": (
            r'<table class="quiz-data-table"><thead><tr><th>Half-Reaction</th><th>$E^\circ\ (\text{V})$</th></tr></thead>'
            r'<tbody><tr><td>$\text{Br}_2(l) + 2e^- \rightarrow 2\text{Br}^-(aq)$</td><td>$+1.07$</td></tr>'
            r'<tr><td>$\text{Fe}^{3+}(aq) + e^- \rightarrow \text{Fe}^{2+}(aq)$</td><td>$+0.77$</td></tr>'
            r'<tr><td>$\text{I}_2(s) + 2e^- \rightarrow 2\text{I}^-(aq)$</td><td>$+0.54$</td></tr></tbody></table>'
        ),
        "question": (
            r"Based on the standard reduction potentials in the table above, which species will react with $\text{Fe}^{3+}(aq)$ in a thermodynamically favorable reaction under standard conditions, reducing it to $\text{Fe}^{2+}(aq)$?"
        ),
        "options": [
            r"$\text{I}^-(aq)$ only, because oxidizing $\text{I}^-$ to $\text{I}_2$ ($E_{\text{anode}}^\circ = +0.54\text{ V}$) gives $E_{\text{cell}}^\circ = 0.77 - 0.54 = +0.23\text{ V} > 0$.",
            r"$\text{Br}^-(aq)$ only, because $\text{Br}_2$ has the highest reduction potential ($+1.07\text{ V}$).",
            r"$\text{I}_2(s)$ only, because $\text{I}_2$ has a lower reduction potential than $\text{Fe}^{3+}$.",
            r"Both $\text{Br}^-(aq)$ and $\text{I}^-(aq)$.",
        ],
        "correct_index": 0,
        "explanation": (
            r"For $\text{Fe}^{3+}$ to be reduced ($E_{\text{cathode}}^\circ = +0.77\text{ V}$), the other reactant must be a species that can be oxidized (a species on the right side of the table) with $E_{\text{anode}}^\circ < +0.77\text{ V}$. $\text{I}^-(aq)$ can be oxidized to $\text{I}_2(s)$ with $E_{\text{cell}}^\circ = 0.77 - 0.54 = +0.23\text{ V} > 0$. Oxidizing $\text{Br}^-(aq)$ would give $E_{\text{cell}}^\circ = 0.77 - 1.07 = -0.30\text{ V} < 0$ (not thermodynamically favorable), so neither the “$\text{Br}^-$ only” nor the “both” choice is correct. $\text{I}_2(s)$ is already the oxidized form of iodine; it can only gain electrons, so it cannot reduce $\text{Fe}^{3+}$."
        ),
    },
    {
        "unit_q_num": 39,
        "topic_code": "9.9",
        "topic_title": "Cell Potential and Free Energy",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"If all stoichiometric coefficients in a balanced redox equation are doubled: $2\text{Ag}^+(aq) + \text{Cu}(s) \rightarrow 2\text{Ag}(s) + \text{Cu}^{2+}(aq)$ vs. $4\text{Ag}^+(aq) + 2\text{Cu}(s) \rightarrow 4\text{Ag}(s) + 2\text{Cu}^{2+}(aq)$, how are $E_{\text{cell}}^\circ$ and $\Delta G_{\text{rxn}}^\circ$ affected?"
        ),
        "options": [
            r"Both $E_{\text{cell}}^\circ$ and $\Delta G_{\text{rxn}}^\circ$ double.",
            r"Both $E_{\text{cell}}^\circ$ and $\Delta G_{\text{rxn}}^\circ$ remain unchanged.",
            r"$E_{\text{cell}}^\circ$ remains unchanged (intensive property), while $\Delta G_{\text{rxn}}^\circ$ doubles (extensive property because $n$ doubles).",
            r"$E_{\text{cell}}^\circ$ doubles while $\Delta G_{\text{rxn}}^\circ$ remains unchanged.",
        ],
        "correct_index": 2,
        "explanation": (
            r"Voltage $E_{\text{cell}}^\circ = -\Delta G^\circ / (nF)$ is the ratio of two extensive quantities ($\Delta G^\circ$ and $n$), making $E_{\text{cell}}^\circ$ intensive (unchanged when coefficients double). $\Delta G_{\text{rxn}}^\circ = -nFE_{\text{cell}}^\circ$ is extensive and doubles when $n$ doubles from $2$ to $4$."
        ),
    },
    {
        "unit_q_num": 40,
        "topic_code": "9.9",
        "topic_title": "Cell Potential and Free Energy",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"Which combination of thermodynamic and electrochemical parameters correctly describes a redox reaction that is thermodynamically UNFAVORABLE under standard conditions?"
        ),
        "options": [
            r"$\Delta G^\circ < 0,\quad E_{\text{cell}}^\circ > 0,\quad K > 1$",
            r"$\Delta G^\circ > 0,\quad E_{\text{cell}}^\circ > 0,\quad K < 1$",
            r"$\Delta G^\circ < 0,\quad E_{\text{cell}}^\circ < 0,\quad K > 1$",
            r"$\Delta G^\circ > 0,\quad E_{\text{cell}}^\circ < 0,\quad K < 1$",
        ],
        "correct_index": 3,
        "explanation": (
            r"By the fundamental bridge equations $\Delta G^\circ = -nFE_{\text{cell}}^\circ = -RT\ln K$, a thermodynamically unfavorable reaction has $\Delta G^\circ > 0$, which requires $E_{\text{cell}}^\circ < 0$ and $K < 1$."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 9.10: Cell Potential Under Nonstandard Conditions (Q41–Q45)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 41,
        "topic_code": "9.10",
        "topic_title": "Cell Potential Under Nonstandard Conditions",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r"$$\text{Zn}(s) + \text{Cu}^{2+}(aq) \rightarrow \text{Zn}^{2+}(aq) + \text{Cu}(s) \qquad E_{\text{cell}}^\circ = +1.10\text{ V}$$"
        ),
        "question": (
            r"A $\text{Zn}-\text{Cu}$ galvanic cell is constructed at $298\text{ K}$ with $[\text{Cu}^{2+}] = 2.0\text{ M}$ and $[\text{Zn}^{2+}] = 0.010\text{ M}$. How does the initial cell potential $E_{\text{cell}}$ compare to $E_{\text{cell}}^\circ = +1.10\text{ V}$, and why?"
        ),
        "options": [
            r"$E_{\text{cell}} < +1.10\text{ V}$, because $Q = \frac{[\text{Cu}^{2+}]}{[\text{Zn}^{2+}]} = 200 > 1$.",
            r"$E_{\text{cell}} > +1.10\text{ V}$, because $Q = \frac{[\text{Zn}^{2+}]}{[\text{Cu}^{2+}]} = 0.0050 < 1$, so $\ln Q < 0$ and $E_{\text{cell}} = E_{\text{cell}}^\circ - \frac{RT}{nF}\ln Q > E_{\text{cell}}^\circ$.",
            r"$E_{\text{cell}} = +1.10\text{ V}$, because cell potential depends only on the identity of the metal electrodes.",
            r"$E_{\text{cell}} = 0\text{ V}$, because the concentrations are not equal.",
        ],
        "correct_index": 1,
        "explanation": (
            r"For $\text{Zn}(s) + \text{Cu}^{2+}(aq) \rightarrow \text{Zn}^{2+}(aq) + \text{Cu}(s)$, solids are omitted from $Q$, so $Q = \frac{[\text{Zn}^{2+}]}{[\text{Cu}^{2+}]} = \frac{0.010}{2.0} = 0.0050 < 1$. Because $Q < 1$, $\ln Q < 0$, and the Nernst equation $E_{\text{cell}} = E_{\text{cell}}^\circ - \frac{RT}{nF}\ln Q$ yields $E_{\text{cell}} > E_{\text{cell}}^\circ$ ($+1.10\text{ V}$)."
        ),
    },
    {
        "unit_q_num": 42,
        "topic_code": "9.10",
        "topic_title": "Cell Potential Under Nonstandard Conditions",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r"$$\text{Pb}(s) + 2\text{Ag}^+(aq) \rightarrow \text{Pb}^{2+}(aq) + 2\text{Ag}(s) \qquad E_{\text{cell}}^\circ = +0.93\text{ V}$$"
        ),
        "question": (
            r"For the galvanic cell above initially at standard conditions ($[\text{Ag}^+] = 1.0\text{ M}$ and $[\text{Pb}^{2+}] = 1.0\text{ M}$), which of the following changes will DECREASE the measured cell voltage $E_{\text{cell}}$?"
        ),
        "options": [
            r"Adding distilled water to the anode compartment to dilute $[\text{Pb}^{2+}]$.",
            r"Increasing the surface area of the solid $\text{Ag}(s)$ cathode.",
            r"Adding $\text{NaCl}(s)$ to the cathode compartment to precipitate $\text{AgCl}(s)$ and lower $[\text{Ag}^+]$.",
            r"Adding more $\text{AgNO}_3(s)$ to the cathode compartment.",
        ],
        "correct_index": 2,
        "explanation": (
            r"Here $Q = \frac{[\text{Pb}^{2+}]}{[\text{Ag}^+]^2}$. Adding $\text{Cl}^-$ to the cathode precipitates $\text{AgCl}(s)$, sharply decreasing $[\text{Ag}^+]$. This makes $Q$ much larger ($Q > 1$), which makes $-\frac{RT}{nF}\ln Q$ negative and decreases $E_{\text{cell}}$. Diluting $[\text{Pb}^{2+}]$ or adding $\text{AgNO}_3$ makes $Q < 1$ (increasing $E_{\text{cell}}$), and solid electrode mass/area does not appear in $Q$."
        ),
    },
    {
        "unit_q_num": 43,
        "topic_code": "9.10",
        "topic_title": "Cell Potential Under Nonstandard Conditions",
        "difficulty": "Challenging",
        "stimulus": (
            r'<table class="quiz-data-table"><thead><tr><th>Half-Cell</th><th>Electrode</th><th>Electrolyte Concentration</th></tr></thead>'
            r'<tbody><tr><td>Half-Cell 1</td><td>$\text{Cu}(s)$</td><td>$0.0010\text{ M Cu(NO}_3)_2(aq)$</td></tr>'
            r'<tr><td>Half-Cell 2</td><td>$\text{Cu}(s)$</td><td>$1.0\text{ M Cu(NO}_3)_2(aq)$</td></tr></tbody></table>'
        ),
        "question": (
            r"A concentration cell is constructed at $298\text{ K}$ using the two copper half-cells described in the table above. Which half-cell serves as the anode, and what drives the positive voltage of this cell?"
        ),
        "options": [
            r"Half-Cell 2 ($1.0\text{ M}$) is the anode because it has the higher concentration of $\text{Cu}^{2+}$ ions.",
            r"Neither half-cell is the anode because $E_{\text{cell}}^\circ = 0.00\text{ V}$ and no current can flow.",
            r"Half-Cell 1 is the cathode because $\text{Cu}^{2+}$ ions plate out in the more dilute solution.",
            r"Half-Cell 1 ($0.0010\text{ M}$) is the anode; although $E_{\text{cell}}^\circ = 0.00\text{ V}$, the reaction $\text{Cu}^{2+}(1.0\text{ M}) \rightarrow \text{Cu}^{2+}(0.0010\text{ M})$ has $Q = 0.0010 < 1$, so $E_{\text{cell}} > 0\text{ V}$ until the concentrations equalize.",
        ],
        "correct_index": 3,
        "explanation": (
            r"In a concentration cell, the thermodynamically favorable process equalizes the two concentrations. Thus the dilute half-cell ($0.0010\text{ M}$) undergoes oxidation ($\text{Cu}(s) \rightarrow \text{Cu}^{2+} + 2e^-$, <strong>anode</strong>) to increase its $[\text{Cu}^{2+}]$, while the concentrated half-cell ($1.0\text{ M}$) undergoes reduction ($\text{Cu}^{2+} + 2e^- \rightarrow \text{Cu}(s)$, <strong>cathode</strong>) to decrease its $[\text{Cu}^{2+}]$. With $E^\circ = 0\text{ V}$ and $Q = \frac{0.0010}{1.0} = 10^{-3} < 1$, $E_{\text{cell}} = -\frac{RT}{2F}\ln(10^{-3}) \approx +0.089\text{ V} > 0$. So the concentrated half-cell is the cathode (copper plates out there, not in the dilute solution), and $E^\circ = 0$ does not mean zero voltage, because $Q \neq 1$."
        ),
    },
    {
        "unit_q_num": 44,
        "topic_code": "9.10",
        "topic_title": "Cell Potential Under Nonstandard Conditions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"When a galvanic cell (battery) has discharged completely and is 'dead' ($E_{\text{cell}} = 0.00\text{ V}$), which of the following statements is true?"
        ),
        "options": [
            r"$Q = K$ and $\Delta G = 0$, while $E_{\text{cell}}^\circ$ remains unchanged at its positive standard value.",
            r"$Q = 1$, $\Delta G^\circ = 0$, and $E_{\text{cell}}^\circ = 0.00\text{ V}$.",
            r"All reactant ions have reached a concentration of exactly $0.00\text{ M}$.",
            r"$Q = 0$ and $\Delta G = \Delta G^\circ$.",
        ],
        "correct_index": 0,
        "explanation": (
            r"A dead battery has reached chemical equilibrium: the reaction quotient $Q$ has grown to equal the equilibrium constant $K$, so $\Delta G = 0$ and $E_{\text{cell}} = 0.00\text{ V}$. Standard constants $E_{\text{cell}}^\circ$ and $\Delta G^\circ$ depend only on standard states ($Q = 1$) and do not change as the cell discharges."
        ),
    },
    {
        "unit_q_num": 45,
        "topic_code": "9.10",
        "topic_title": "Cell Potential Under Nonstandard Conditions",
        "difficulty": "Challenging",
        "stimulus": (
            r"$$\text{Ni}(s) + \text{Sn}^{2+}(aq) \rightarrow \text{Ni}^{2+}(aq) + \text{Sn}(s) \qquad E_{\text{cell}}^\circ = +0.11\text{ V}$$"
        ),
        "question": (
            r"In a standard $\text{Ni}-\text{Sn}$ galvanic cell ($[\text{Ni}^{2+}] = [\text{Sn}^{2+}] = 1.0\text{ M}$), a student doubles the mass of the solid $\text{Ni}(s)$ anode while keeping all solution concentrations and temperature constant. How does this affect $E_{\text{cell}}$ and the total time the cell can deliver current?"
        ),
        "options": [
            r"$E_{\text{cell}}$ increases because there are more $\text{Ni}$ atoms available to lose electrons.",
            r"$E_{\text{cell}}$ decreases because $Q$ doubles when the mass of $\text{Ni}(s)$ doubles.",
            r"$E_{\text{cell}}$ remains unchanged at $+0.11\text{ V}$ because pure solids do not appear in $Q$, though the cell can operate longer before the $\text{Ni}$ anode is consumed (if $\text{Ni}$ was limiting).",
            r"Both $E_{\text{cell}}$ and $E_{\text{cell}}^\circ$ double to $+0.22\text{ V}$.",
        ],
        "correct_index": 2,
        "explanation": (
            r"Pure solids and liquids have constant activity ($1$) and are excluded from the reaction quotient $Q = [\text{Ni}^{2+}]/[\text{Sn}^{2+}]$. Therefore, changing the mass or surface area of the $\text{Ni}(s)$ electrode has zero effect on $E_{\text{cell}}$, though a larger electrode provides more moles of reactant for longer battery life."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 9.11: Electrolysis and Faraday's Law (Q46–Q50)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 46,
        "topic_code": "9.11",
        "topic_title": "Electrolysis and Faraday's Law",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"A steady current of $5.00\text{ A}$ is passed through an electrolytic cell containing molten $\text{MgCl}_2(l)$ for $1,930\text{ s}$ ($F = 96,485\text{ C mol}^{-1}$). How many grams of $\text{Mg}(l)$ ($\text{molar mass } = 24.3\text{ g mol}^{-1}$) are produced at the cathode?"
        ),
        "options": [
            r"$0.100\text{ g}$",
            r"$1.22\text{ g}$",
            r"$2.43\text{ g}$",
            r"$4.86\text{ g}$",
        ],
        "correct_index": 1,
        "explanation": (
            r"First calculate total charge: $q = I \times t = (5.00\text{ C s}^{-1})(1930\text{ s}) = 9650\text{ C}$. "
            r"Moles of electrons: $n_{e^-} = \frac{9650\text{ C}}{96,485\text{ C mol}^{-1}} = 0.100\text{ mol } e^-$. "
            r"Since $\text{Mg}^{2+} + 2e^- \rightarrow \text{Mg}$ requires $2\text{ mol } e^-$ per mole of $\text{Mg}$, $\text{mol Mg} = \frac{0.100}{2} = 0.0500\text{ mol}$. "
            r"Mass of $\text{Mg} = 0.0500\text{ mol} \times 24.3\text{ g mol}^{-1} = 1.215\text{ g} \approx 1.22\text{ g}$."
        ),
    },
    {
        "unit_q_num": 47,
        "topic_code": "9.11",
        "topic_title": "Electrolysis and Faraday's Law",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"Three electrolytic cells connected in series (so that the exact same electrical charge $q$ passes through all three cells) contain aqueous solutions of $\text{AgNO}_3$, $\text{CuSO}_4$, and $\text{AuCl}_3$, respectively. What is the mole ratio of metals plated out at the three cathodes, $\text{mol Ag} : \text{mol Cu} : \text{mol Au}$?"
        ),
        "options": [
            r"$6 : 3 : 2$",
            r"$1 : 2 : 3$",
            r"$1 : 1 : 1$",
            r"$3 : 2 : 1$",
        ],
        "correct_index": 0,
        "explanation": (
            r"The cathode half-reactions are $\text{Ag}^+ + 1e^- \rightarrow \text{Ag}$, $\text{Cu}^{2+} + 2e^- \rightarrow \text{Cu}$, and $\text{Au}^{3+} + 3e^- \rightarrow \text{Au}$. For $6\text{ mol}$ of electrons passing through all three cells in series, $6\text{ mol Ag}$, $3\text{ mol Cu}$, and $2\text{ mol Au}$ are deposited, giving a mole ratio of $6 : 3 : 2$."
        ),
    },
    {
        "unit_q_num": 48,
        "topic_code": "9.11",
        "topic_title": "Electrolysis and Faraday's Law",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": (
            r"When an aqueous solution of a gold salt is electrolyzed with a current of $2.00\text{ A}$ for $4,825\text{ s}$ ($F = 96,500\text{ C mol}^{-1}$), $6.57\text{ g}$ of metallic gold ($\text{molar mass } = 197\text{ g mol}^{-1}$) is deposited at the cathode. What is the oxidation state of gold in the salt?"
        ),
        "options": [
            r"$+1$",
            r"$+2$",
            r"$+3$",
            r"$+4$",
        ],
        "correct_index": 2,
        "explanation": (
            r"Moles of electrons passed: $n_{e^-} = \frac{I \cdot t}{F} = \frac{(2.00\text{ A})(4825\text{ s})}{96,500\text{ C mol}^{-1}} = \frac{9650}{96,500} = 0.100\text{ mol } e^-$. "
            r"Moles of $\text{Au}$ deposited: $n_{\text{Au}} = \frac{6.57\text{ g}}{197\text{ g mol}^{-1}} = 0.0333\text{ mol Au}$. "
            r"The ratio $\frac{\text{mol } e^-}{\text{mol Au}} = \frac{0.100}{0.0333} = 3$, so the gold ion is $\text{Au}^{3+}$ (oxidation state $+3$)."
        ),
    },
    {
        "unit_q_num": 49,
        "topic_code": "9.11",
        "topic_title": "Electrolysis and Faraday's Law",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"During the electrolysis of acidified water ($2\text{H}_2\text{O}(l) \rightarrow 2\text{H}_2(g) + \text{O}_2(g)$), $0.40\text{ mol}$ of electrons pass through the cell. How many moles of $\text{O}_2(g)$ are produced at the anode?"
        ),
        "options": [
            r"$0.80\text{ mol O}_2$",
            r"$0.40\text{ mol O}_2$",
            r"$0.20\text{ mol O}_2$",
            r"$0.10\text{ mol O}_2$",
        ],
        "correct_index": 3,
        "explanation": (
            r"The anode oxidation half-reaction for water is $2\text{H}_2\text{O}(l) \rightarrow \text{O}_2(g) + 4\text{H}^+(aq) + 4e^-$, which requires $4\text{ mol } e^-$ per $1\text{ mol O}_2(g)$. Thus $0.40\text{ mol } e^- \times \frac{1\text{ mol O}_2}{4\text{ mol } e^-} = 0.10\text{ mol O}_2(g)$."
        ),
    },
    {
        "unit_q_num": 50,
        "topic_code": "9.11",
        "topic_title": "Electrolysis and Faraday's Law",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"How much time (in seconds) is required to plate out $1.00\text{ mol}$ of $\text{Cr}(s)$ from an aqueous $\text{Cr}^{3+}(aq)$ electroplating bath using a constant current of $10.0\text{ A}$? ($F = 96,485\text{ C mol}^{-1}$)"
        ),
        "options": [
            r"$9,649\text{ s}$",
            r"$19,297\text{ s}$",
            r"$28,946\text{ s}$",
            r"$96,485\text{ s}$",
        ],
        "correct_index": 2,
        "explanation": (
            r"Plating $1.00\text{ mol Cr}(s)$ via $\text{Cr}^{3+}(aq) + 3e^- \rightarrow \text{Cr}(s)$ requires $n_{e^-} = 3.00\text{ mol } e^-$. "
            r"Total charge required: $q = n_{e^-} F = 3.00 \times 96,485\text{ C} = 289,455\text{ C}$. "
            r"Time $t = \frac{q}{I} = \frac{289,455\text{ C}}{10.0\text{ C s}^{-1}} = 28,945.5\text{ s} \approx 28,946\text{ s}$."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 9.6: Free Energy of Dissolution (Q51–Q53)
    # Moved from former Unit 7 topic 7.14 (re-aligned with the Fall 2024 CED).
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 51,
        "topic_code": "9.6",
        "topic_title": "Free Energy of Dissolution",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{NH}_4\\text{NO}_3(s) \\rightleftharpoons \\text{NH}_4^+(aq) + \\text{NO}_3^-(aq) \\quad \\Delta H_{\\text{soln}}^\\circ = +25.7\\text{ kJ/mol}_{rxn}$"
            "</div>"
        ),
        "question": (
            "When solid ammonium nitrate, $\\text{NH}_4\\text{NO}_3(s)$, is dissolved in water in an instant cold pack at "
            "$25^\\circ\\text{C}$, the salt dissolves readily to form a concentrated $> 1\\text{ M}$ solution and the pack becomes "
            "very cold. Which of the following correctly gives the signs of $\\Delta H_{\\text{soln}}^\\circ$, "
            "$\\Delta S_{\\text{soln}}^\\circ$, and $\\Delta G_{\\text{soln}}^\\circ$ for the dissolution of $\\text{NH}_4\\text{NO}_3(s)$ at $25^\\circ\\text{C}$?"
        ),
        "options": [
            "$\\Delta H_{\\text{soln}}^\\circ > 0$, $\\Delta S_{\\text{soln}}^\\circ > 0$, $\\Delta G_{\\text{soln}}^\\circ < 0$",
            "$\\Delta H_{\\text{soln}}^\\circ < 0$, $\\Delta S_{\\text{soln}}^\\circ > 0$, $\\Delta G_{\\text{soln}}^\\circ < 0$",
            "$\\Delta H_{\\text{soln}}^\\circ > 0$, $\\Delta S_{\\text{soln}}^\\circ < 0$, $\\Delta G_{\\text{soln}}^\\circ < 0$",
            "$\\Delta H_{\\text{soln}}^\\circ > 0$, $\\Delta S_{\\text{soln}}^\\circ > 0$, $\\Delta G_{\\text{soln}}^\\circ > 0$",
        ],
        "correct_index": 0,
        "explanation": (
            "Because heat is absorbed from the surroundings (the pack gets cold), the dissolution is endothermic "
            "($\\Delta H_{\\text{soln}}^\\circ > 0$). Because the salt is highly soluble ($K_{\\text{sp}} > 1$), standard dissolution "
            "is thermodynamically favorable ($\\Delta G_{\\text{soln}}^\\circ = -RT\\ln K_{\\text{sp}} < 0$). "
            "For $\\Delta G^\\circ = \\Delta H^\\circ - T\\Delta S^\\circ$ to be negative when $\\Delta H^\\circ > 0$, "
            "the entropy change of dissolution must be positive ($\\Delta S_{\\text{soln}}^\\circ > 0$) and large enough that $T\\Delta S^\\circ > \\Delta H^\\circ$."
        ),
    },
    {
        "unit_q_num": 52,
        "topic_code": "9.6",
        "topic_title": "Free Energy of Dissolution",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{AgCl}(s) \\rightleftharpoons \\text{Ag}^+(aq) + \\text{Cl}^-(aq) \\quad K_{\\text{sp}} = 1.8 \\times 10^{-10}\\text{ at } 298\\text{ K}$"
            "</div>"
        ),
        "question": (
            "For the dissolution of $\\text{AgCl}(s)$ in water at $298\\text{ K}$, $\\Delta G_{\\text{soln}}^\\circ = +55.6\\text{ kJ/mol}_{rxn}$. "
            "Yet when a tiny crystal of $\\text{AgCl}(s)$ is placed in $1.0\\text{ L}$ of pure water at $298\\text{ K}$, some of the "
            "solid dissolves until $[\\text{Ag}^+] = [\\text{Cl}^-] = 1.3 \\times 10^{-5}\\text{ M}$. Which of the following best "
            "explains why some $\\text{AgCl}(s)$ dissolves even though $\\Delta G_{\\text{soln}}^\\circ > 0$?"
        ),
        "options": [
            "$\\Delta G_{\\text{soln}}^\\circ > 0$ only applies to the reverse precipitation reaction.",
            "$\\Delta G_{\\text{soln}}^\\circ > 0$ means $K_{\\text{sp}} < 1$ (standard $1\\text{ M}$ concentrations are not reached), but in pure water $Q_{\\text{sp}} < K_{\\text{sp}}$ so $\\Delta G < 0$ until saturation is reached.",
            "Dissolution of a solid into pure water is always exothermic, overriding $\\Delta G_{\\text{soln}}^\\circ$.",
            r"In pure water the initial ion concentrations are zero, which changes the value of $\Delta G_{\text{soln}}^\circ$ to a negative number.",
        ],
        "correct_index": 1,
        "explanation": (
            r"$\Delta G_{\text{soln}}^\circ = -RT\ln K_{\text{sp}} > 0$ only says that $K_{\text{sp}} \ll 1$: a solution with $1\text{ M}$ ions (standard conditions) is not reached. "
            r"In pure water, $Q_{\text{sp}} = [\text{Ag}^+][\text{Cl}^-] = 0 < K_{\text{sp}}$, so net dissolution is thermodynamically favorable ($\Delta G < 0$) until "
            r"$Q_{\text{sp}} = K_{\text{sp}}$, where $\Delta G = 0$ (saturation, $\sqrt{1.8 \times 10^{-10}} = 1.3 \times 10^{-5}\text{ M}$). "
            r"$\Delta G^\circ$ is a constant at a given temperature; it does not change with the starting concentrations, and it applies to dissolution as written "
            r"(for precipitation, $\Delta G^\circ = -55.6\text{ kJ/mol}_{rxn}$). Dissolution is not always exothermic, and $\Delta H^\circ$ is already included in $\Delta G^\circ$."
        ),
    },
    {
        "unit_q_num": 53,
        "topic_code": "9.6",
        "topic_title": "Free Energy of Dissolution",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Step in Dissolution of $\\text{MX}(s)$</th><th>Enthalpy Change ($\\text{kJ/mol}_{rxn}$)</th></tr></thead>"
            "<tbody>"
            "<tr><td>$\\text{MX}(s) \\rightarrow \\text{M}^+(g) + \\text{X}^-(g)$ (Lattice dissociation)</td><td>$\\Delta H_{\\text{lattice}} = +788$</td></tr>"
            "<tr><td>$\\text{M}^+(g) + \\text{X}^-(g) \\rightarrow \\text{M}^+(aq) + \\text{X}^-(aq)$ (Hydration of ions)</td><td>$\\Delta H_{\\text{hyd}} = -784$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Based on the thermodynamic cycle data in the table above for the dissolution of an ionic solid $\\text{MX}(s)$ "
            "in water, and given that $\\Delta S_{\\text{soln}}^\\circ = +43\\text{ J/(mol}_{rxn}\\cdot\\text{K)}$, what are the values of "
            "$\\Delta H_{\\text{soln}}^\\circ$ and $\\Delta G_{\\text{soln}}^\\circ$ at $298\\text{ K}$?"
        ),
        "options": [
            "$\\Delta H_{\\text{soln}}^\\circ = -4\\text{ kJ/mol}_{rxn}$ and $\\Delta G_{\\text{soln}}^\\circ = -17\\text{ kJ/mol}_{rxn}$",
            "$\\Delta H_{\\text{soln}}^\\circ = +4\\text{ kJ/mol}_{rxn}$ and $\\Delta G_{\\text{soln}}^\\circ = +17\\text{ kJ/mol}_{rxn}$",
            "$\\Delta H_{\\text{soln}}^\\circ = +1572\\text{ kJ/mol}_{rxn}$ and $\\Delta G_{\\text{soln}}^\\circ = +1559\\text{ kJ/mol}_{rxn}$",
            "$\\Delta H_{\\text{soln}}^\\circ = +4\\text{ kJ/mol}_{rxn}$ and $\\Delta G_{\\text{soln}}^\\circ = -9\\text{ kJ/mol}_{rxn}$",
        ],
        "correct_index": 3,
        "explanation": (
            "By Hess's Law, $\\Delta H_{\\text{soln}}^\\circ = \\Delta H_{\\text{lattice}} + \\Delta H_{\\text{hyd}} = "
            "(+788) + (-784) = +4\\text{ kJ/mol}_{rxn}$ (breaking ion-ion attractions in the lattice is endothermic, while forming "
            "ion-dipole attractions during hydration is exothermic). At $298\\text{ K}$, "
            "$\\Delta G_{\\text{soln}}^\\circ = \\Delta H_{\\text{soln}}^\\circ - T\\Delta S_{\\text{soln}}^\\circ = "
            "+4\\text{ kJ/mol}_{rxn} - (298\\text{ K})(0.043\\text{ kJ/(mol}_{rxn}\\cdot\\text{K)}) = 4 - 12.8 \\approx -9\\text{ kJ/mol}_{rxn}$."
        ),
    },
    # -------------------------------------------------------------------------
    # Added 2026-10-03 — Blind-spot coverage (Fall 2024 CED): topics 9.1–9.11
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 54,
        "topic_code": "9.1",
        "topic_title": "Introduction to Entropy",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r"""<figure class="quiz-figure-wrap"><svg class="quiz-figure" viewBox="0 0 520 300" role="img" aria-label="Two Maxwell-Boltzmann distributions of molecular speeds for the same sample of nitrogen gas: at 250 K the curve is narrow with a tall peak near 385 meters per second; at 500 K the curve is broader and flatter with a lower peak near 545 meters per second and a longer high-speed tail. Both curves enclose the same area." font-family="sans-serif" font-size="13" fill="#111827"><line x1="70" y1="250" x2="498" y2="250" stroke="#374151" stroke-width="2"/><line x1="70" y1="250" x2="70" y2="28" stroke="#374151" stroke-width="2"/><line x1="70" y1="250" x2="70" y2="256" stroke="#374151" stroke-width="1.5"/><text x="70" y="271" text-anchor="middle">0</text><line x1="154" y1="250" x2="154" y2="256" stroke="#374151" stroke-width="1.5"/><text x="154" y="271" text-anchor="middle">300</text><line x1="238" y1="250" x2="238" y2="256" stroke="#374151" stroke-width="1.5"/><text x="238" y="271" text-anchor="middle">600</text><line x1="322" y1="250" x2="322" y2="256" stroke="#374151" stroke-width="1.5"/><text x="322" y="271" text-anchor="middle">900</text><line x1="406" y1="250" x2="406" y2="256" stroke="#374151" stroke-width="1.5"/><text x="406" y="271" text-anchor="middle">1200</text><line x1="490" y1="250" x2="490" y2="256" stroke="#374151" stroke-width="1.5"/><text x="490" y="271" text-anchor="middle">1500</text><polyline fill="none" stroke="#111827" stroke-width="2.5" points="70.0,250.0 74.2,249.2 78.4,246.9 82.6,243.1 86.8,237.8 91.0,231.2 95.2,223.3 99.4,214.4 103.6,204.5 107.8,193.9 112.0,182.7 116.2,171.2 120.4,159.4 124.6,147.6 128.8,136.0 133.0,124.8 137.2,114.1 141.4,104.0 145.6,94.8 149.8,86.5 154.0,79.2 158.2,73.1 162.4,68.1 166.6,64.3 170.8,61.7 175.0,60.3 179.2,60.1 183.4,61.0 187.6,63.0 191.8,66.0 196.0,69.9 200.2,74.7 204.4,80.2 208.6,86.4 212.8,93.1 217.0,100.2 221.2,107.7 225.4,115.4 229.6,123.3 233.8,131.2 238.0,139.2 242.2,147.0 246.4,154.7 250.6,162.2 254.8,169.4 259.0,176.3 263.2,182.9 267.4,189.2 271.6,195.1 275.8,200.6 280.0,205.7 284.2,210.5 288.4,214.9 292.6,218.9 296.8,222.5 301.0,225.8 305.2,228.8 309.4,231.5 313.6,233.9 317.8,236.1 322.0,238.0 326.2,239.6 330.4,241.1 334.6,242.4 338.8,243.5 343.0,244.5 347.2,245.4 351.4,246.1 355.6,246.7 359.8,247.3 364.0,247.7 368.2,248.1 372.4,248.4 376.6,248.7 380.8,248.9 385.0,249.1 389.2,249.3 393.4,249.4 397.6,249.5 401.8,249.6 406.0,249.7 410.2,249.8 414.4,249.8 418.6,249.8 422.8,249.9 427.0,249.9 431.2,249.9 435.4,249.9 439.6,250.0 443.8,250.0 448.0,250.0 452.2,250.0 456.4,250.0 460.6,250.0 464.8,250.0 469.0,250.0 473.2,250.0 477.4,250.0 481.6,250.0 485.8,250.0 490.0,250.0"/><polyline fill="none" stroke="#2563eb" stroke-width="2.5" stroke-dasharray="8 5" points="70.0,250.0 74.2,249.7 78.4,248.9 82.6,247.5 86.8,245.6 91.0,243.2 95.2,240.3 99.4,236.9 103.6,233.1 107.8,228.9 112.0,224.3 116.2,219.4 120.4,214.3 124.6,208.9 128.8,203.2 133.0,197.5 137.2,191.6 141.4,185.8 145.6,179.9 149.8,174.0 154.0,168.3 158.2,162.6 162.4,157.2 166.6,152.0 170.8,147.0 175.0,142.3 179.2,137.9 183.4,133.9 187.6,130.2 191.8,126.9 196.0,124.1 200.2,121.6 204.4,119.6 208.6,118.0 212.8,116.8 217.0,116.0 221.2,115.7 225.4,115.7 229.6,116.2 233.8,117.1 238.0,118.3 242.2,119.9 246.4,121.8 250.6,124.0 254.8,126.4 259.0,129.2 263.2,132.2 267.4,135.4 271.6,138.7 275.8,142.3 280.0,145.9 284.2,149.7 288.4,153.6 292.6,157.5 296.8,161.4 301.0,165.4 305.2,169.4 309.4,173.3 313.6,177.2 317.8,181.1 322.0,184.9 326.2,188.6 330.4,192.2 334.6,195.7 338.8,199.1 343.0,202.4 347.2,205.6 351.4,208.6 355.6,211.5 359.8,214.3 364.0,216.9 368.2,219.4 372.4,221.8 376.6,224.0 380.8,226.1 385.0,228.1 389.2,229.9 393.4,231.6 397.6,233.2 401.8,234.7 406.0,236.1 410.2,237.4 414.4,238.6 418.6,239.7 422.8,240.7 427.0,241.6 431.2,242.5 435.4,243.2 439.6,243.9 443.8,244.6 448.0,245.2 452.2,245.7 456.4,246.2 460.6,246.6 464.8,247.0 469.0,247.3 473.2,247.6 477.4,247.9 481.6,248.2 485.8,248.4 490.0,248.6"/><line x1="356" y1="50" x2="392" y2="50" stroke="#111827" stroke-width="2.5"/><text x="400" y="55">250 K</text><line x1="356" y1="74" x2="392" y2="74" stroke="#2563eb" stroke-width="2.5" stroke-dasharray="8 5"/><text x="400" y="79">500 K</text><text x="280" y="292" text-anchor="middle">Molecular speed (m/s)</text><text x="0" y="0" transform="translate(40 140) rotate(-90)" text-anchor="middle">Fraction of molecules</text></svg><figcaption>Figure: Distribution of molecular speeds for the same 1.0 mol sample of N₂(g) in a rigid 10.0 L container at 250 K and at 500 K</figcaption></figure>"""
        ),
        "question": (
            r"The figure above shows the distribution of molecular speeds for the same sample of $\text{N}_2(g)$ in the same rigid container at $250\text{ K}$ and at $500\text{ K}$. Which of the following correctly compares the entropy of the sample at the two temperatures?"
        ),
        "options": [
            r"The entropy is greater at $250\text{ K}$, because the taller, narrower peak shows that more of the molecules have nearly the same speed.",
            r"The entropy is greater at $500\text{ K}$, because the broader distribution shows that the kinetic energy of the molecules is dispersed over a wider range of speeds.",
            r"The entropy is the same at both temperatures, because the number of molecules and the volume of the container do not change.",
            r"The entropy is greater at $500\text{ K}$, because the area under the $500\text{ K}$ curve is larger, which shows that more molecules are present.",
        ],
        "correct_index": 1,
        "explanation": (
            r"Entropy increases when energy is dispersed. As the temperature increases, the distribution of molecular speeds (and kinetic energies) broadens, so the total energy of the sample is spread over many more possible arrangements, and the entropy is greater at $500\text{ K}$. "
            r"The tall, narrow $250\text{ K}$ peak means the molecules are confined to a narrower range of speeds, which corresponds to less energy dispersal, not more. "
            r"The amount of gas and the volume are the same, but entropy also depends on how the energy is distributed, so the entropies are not equal. "
            r"Both curves describe the same number of molecules, so the areas under them are equal; the higher entropy comes from the broader spread, not from a larger area."
        ),
    },
    {
        "unit_q_num": 55,
        "topic_code": "9.3",
        "topic_title": "Gibbs Free Energy and Thermodynamic Favorability",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r"""<figure class="quiz-figure-wrap"><svg class="quiz-figure" viewBox="0 0 520 320" role="img" aria-label="Graph of standard free energy change in kilojoules per mole versus temperature in kelvin from 0 to 600 K. The straight line starts at minus 80 kJ per mole at 0 K, rises with constant positive slope, crosses zero at 400 K, and reaches plus 40 kJ per mole at 600 K." font-family="sans-serif" font-size="13" fill="#111827"><line x1="80" y1="30" x2="80" y2="270" stroke="#e5e7eb" stroke-width="1"/><line x1="150" y1="30" x2="150" y2="270" stroke="#e5e7eb" stroke-width="1"/><line x1="220" y1="30" x2="220" y2="270" stroke="#e5e7eb" stroke-width="1"/><line x1="290" y1="30" x2="290" y2="270" stroke="#e5e7eb" stroke-width="1"/><line x1="360" y1="30" x2="360" y2="270" stroke="#e5e7eb" stroke-width="1"/><line x1="430" y1="30" x2="430" y2="270" stroke="#e5e7eb" stroke-width="1"/><line x1="500" y1="30" x2="500" y2="270" stroke="#e5e7eb" stroke-width="1"/><line x1="80" y1="270" x2="500" y2="270" stroke="#e5e7eb" stroke-width="1"/><line x1="80" y1="240" x2="500" y2="240" stroke="#e5e7eb" stroke-width="1"/><line x1="80" y1="210" x2="500" y2="210" stroke="#e5e7eb" stroke-width="1"/><line x1="80" y1="180" x2="500" y2="180" stroke="#e5e7eb" stroke-width="1"/><line x1="80" y1="150" x2="500" y2="150" stroke="#e5e7eb" stroke-width="1"/><line x1="80" y1="120" x2="500" y2="120" stroke="#e5e7eb" stroke-width="1"/><line x1="80" y1="90" x2="500" y2="90" stroke="#e5e7eb" stroke-width="1"/><line x1="80" y1="60" x2="500" y2="60" stroke="#e5e7eb" stroke-width="1"/><line x1="80" y1="30" x2="500" y2="30" stroke="#e5e7eb" stroke-width="1"/><line x1="80" y1="120" x2="500" y2="120" stroke="#6b7280" stroke-width="1.5"/><line x1="80" y1="30" x2="80" y2="270" stroke="#374151" stroke-width="2"/><line x1="80" y1="270" x2="500" y2="270" stroke="#374151" stroke-width="2"/><text x="80" y="288" text-anchor="middle">0</text><text x="150" y="288" text-anchor="middle">100</text><text x="220" y="288" text-anchor="middle">200</text><text x="290" y="288" text-anchor="middle">300</text><text x="360" y="288" text-anchor="middle">400</text><text x="430" y="288" text-anchor="middle">500</text><text x="500" y="288" text-anchor="middle">600</text><text x="72" y="274" text-anchor="end">−100</text><text x="72" y="244" text-anchor="end">−80</text><text x="72" y="214" text-anchor="end">−60</text><text x="72" y="184" text-anchor="end">−40</text><text x="72" y="154" text-anchor="end">−20</text><text x="72" y="124" text-anchor="end">0</text><text x="72" y="94" text-anchor="end">+20</text><text x="72" y="64" text-anchor="end">+40</text><text x="72" y="34" text-anchor="end">+60</text><line x1="80" y1="240" x2="500" y2="60" stroke="#111827" stroke-width="2.5"/><text x="290" y="312" text-anchor="middle">Temperature (K)</text><text x="0" y="0" transform="translate(24 150) rotate(-90)" text-anchor="middle">ΔG° (kJ/mol)</text></svg><figcaption>Figure: ΔG° versus temperature for the reaction (ΔH° and ΔS° assumed independent of temperature)</figcaption></figure>"""
        ),
        "question": (
            r"The graph above shows how $\Delta G^\circ$ for a reaction depends on temperature, assuming that $\Delta H^\circ$ and $\Delta S^\circ$ do not change with temperature. Based on the graph, what is the value of $\Delta S^\circ$ for the reaction?"
        ),
        "options": [
            r"$-200\text{ J/(mol}_{rxn}\cdot\text{K)}$",
            r"$-0.200\text{ J/(mol}_{rxn}\cdot\text{K)}$",
            r"$+0.200\text{ J/(mol}_{rxn}\cdot\text{K)}$",
            r"$+200\text{ J/(mol}_{rxn}\cdot\text{K)}$",
        ],
        "correct_index": 0,
        "explanation": (
            r"Because $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$, a plot of $\Delta G^\circ$ versus $T$ is a straight line with intercept $\Delta H^\circ$ (here $-80\text{ kJ/mol}_{rxn}$) and slope $-\Delta S^\circ$. "
            r"Slope $= \frac{(+40) - (-80)\text{ kJ/mol}_{rxn}}{(600 - 0)\text{ K}} = +0.200\text{ kJ/(mol}_{rxn}\cdot\text{K)}$, so $\Delta S^\circ = -0.200\text{ kJ/(mol}_{rxn}\cdot\text{K)} = -200\text{ J/(mol}_{rxn}\cdot\text{K)}$. "
            r"Check: $\Delta G^\circ = 0$ at $T = \frac{\Delta H^\circ}{\Delta S^\circ} = \frac{-80{,}000\text{ J/mol}_{rxn}}{-200\text{ J/(mol}_{rxn}\cdot\text{K)}} = 400\text{ K}$, as shown. "
            r"Taking the slope itself as $\Delta S^\circ$ gives the wrong sign ($+200$), and the $\pm 0.200$ values leave the slope in kJ while labeling it in J. With $\Delta H^\circ < 0$ and $\Delta S^\circ < 0$, the reaction is favored only below $400\text{ K}$."
        ),
    },
    {
        "unit_q_num": 56,
        "topic_code": "9.6",
        "topic_title": "Free Energy of Dissolution",
        "difficulty": "Challenging",
        "stimulus": (
            r'<table class="quiz-data-table"><thead><tr><th>Salt</th><th>$\Delta H_{\text{soln}}^\circ\ (\text{kJ/mol}_{rxn})$</th><th>$\Delta S_{\text{soln}}^\circ\ (\text{J/(mol}_{rxn}\cdot\text{K)})$</th><th>Solubility in water at $25^\circ\text{C}$</th></tr></thead>'
            r'<tbody><tr><td>$\text{KCl}$</td><td>$+17$</td><td>$+76$</td><td>Very soluble</td></tr>'
            r'<tr><td>$\text{CaCO}_3$</td><td>$-13$</td><td>$-203$</td><td>Very slightly soluble</td></tr></tbody></table>'
        ),
        "question": (
            r"The table above gives standard enthalpy and entropy changes for the dissolution of two ionic solids in water at $298\text{ K}$. Which of the following best explains why $\text{KCl}$ is much more soluble than $\text{CaCO}_3$, even though the dissolution of $\text{CaCO}_3$ is exothermic and the dissolution of $\text{KCl}$ is endothermic?"
        ),
        "options": [
            r"The dissolution of $\text{CaCO}_3$ is thermodynamically favored, but it does not occur at a measurable rate because its activation energy is very large.",
            r"Endothermic dissolution is always thermodynamically favored, because the energy absorbed from the surroundings increases the entropy of the solution.",
            r"Water molecules become highly ordered around the doubly charged $\text{Ca}^{2+}$ and $\text{CO}_3^{2-}$ ions, so $\Delta S_{\text{soln}}^\circ$ is large and negative; at $298\text{ K}$ the $-T\Delta S^\circ$ term outweighs $\Delta H^\circ$, making $\Delta G_{\text{soln}}^\circ > 0$ for $\text{CaCO}_3$ but $\Delta G_{\text{soln}}^\circ < 0$ for $\text{KCl}$.",
            r"Because $\Delta H_{\text{soln}}^\circ$ is negative for $\text{CaCO}_3$, its ions are attracted more strongly to each other than to water molecules, so they remain in the solid.",
        ],
        "correct_index": 2,
        "explanation": (
            r"Use $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$. $\text{KCl}$: $+17 - (298)(0.076) \approx -5.6\text{ kJ/mol}_{rxn}$, favored (entropy-driven). $\text{CaCO}_3$: $-13 - (298)(-0.203) \approx +47.5\text{ kJ/mol}_{rxn}$, not favored, so $K_{\text{sp}} \ll 1$. "
            r"The large negative $\Delta S^\circ$ for $\text{CaCO}_3$ arises because the highly charged ions organize nearby water molecules into ordered hydration shells, more than offsetting the entropy gained when the lattice breaks apart. "
            r"Lattice breaking, solvent reorganization, and ion–solvent attraction each contribute to $\Delta H^\circ$ and $\Delta S^\circ$, and these contributions partly cancel, so the sign of $\Delta H^\circ$ alone cannot predict solubility; endothermic dissolution is favored only when $T\Delta S^\circ > \Delta H^\circ$. "
            r"A negative $\Delta H_{\text{soln}}^\circ$ means hydration releases more energy than is needed to separate the ions, the opposite of the claim that the ions prefer each other. Because $\Delta G^\circ > 0$, the low solubility is a thermodynamic limit, not a slow rate."
        ),
    },
    {
        "unit_q_num": 57,
        "topic_code": "9.7",
        "topic_title": "Coupled Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": (
            r"$$6\text{CO}_2(g) + 6\text{H}_2\text{O}(l) \rightarrow \text{C}_6\text{H}_{12}\text{O}_6(s) + 6\text{O}_2(g) \qquad \Delta G^\circ = +2880\text{ kJ/mol}_{rxn}$$"
        ),
        "question": (
            r"Green plants produce glucose by the overall reaction represented above. Which of the following best explains how plants are able to carry out this process?"
        ),
        "options": [
            r"Chlorophyll acts as a catalyst that lowers the activation energy enough to make $\Delta G^\circ$ for the reaction negative.",
            r"The $\text{O}_2(g)$ produced escapes from the leaves, and removing this product changes the sign of $\Delta G^\circ$ for the reaction from positive to negative.",
            r"The reaction is coupled with its reverse reaction, cellular respiration ($\Delta G^\circ = -2880\text{ kJ/mol}_{rxn}$), so the coupled process has $\Delta G^\circ < 0$.",
            r"Absorbed light supplies energy from an external source that drives the thermodynamically unfavorable conversion; $\Delta G^\circ$ for the reaction itself remains positive, and glucose production stops when the light is removed.",
        ],
        "correct_index": 3,
        "explanation": (
            r"An external source of energy can make a thermodynamically unfavorable process occur. In photosynthesis, light energy drives the overall conversion of $\text{CO}_2$ to glucose, just as electrical energy drives an electrolytic cell or charges a battery. "
            r"$\Delta G^\circ$ is a fixed property of the reaction at a given temperature: a catalyst lowers the activation energy of both the forward and reverse reactions but cannot change $\Delta G^\circ$ or $K$, and removing $\text{O}_2$ changes $Q$, not $\Delta G^\circ$. "
            r"Adding a reaction to its own reverse gives no net change ($\Delta G^\circ = 0$) and produces no glucose; useful coupling requires a different, favorable reaction that shares a common intermediate with the unfavorable one."
        ),
    },
    {
        "unit_q_num": 58,
        "topic_code": "9.8",
        "topic_title": "Galvanic (Voltaic) and Electrolytic Cells",
        "difficulty": "Challenging",
        "stimulus": (
            r"""<figure class="quiz-figure-wrap"><svg class="quiz-figure" viewBox="0 0 540 340" role="img" aria-label="Galvanic cell. Left beaker: a copper electrode in 1.0 M copper(II) nitrate solution. Right beaker: a silver electrode in 1.0 M silver nitrate solution. A KNO3 salt bridge connects the two solutions. A wire from the copper electrode passes through a voltmeter reading 0.46 V to the silver electrode, and an arrow labeled e minus shows electrons flowing through the wire from the copper electrode toward the silver electrode." font-family="sans-serif" font-size="13" fill="#111827"><rect x="52" y="182" width="156" height="122" fill="#e5e7eb"/><rect x="332" y="182" width="156" height="122" fill="#e5e7eb"/><path d="M 170 262 L 170 128 Q 170 104 194 104 L 346 104 Q 370 104 370 128 L 370 262" fill="none" stroke="#374151" stroke-width="22"/><path d="M 170 262 L 170 128 Q 170 104 194 104 L 346 104 Q 370 104 370 128 L 370 262" fill="none" stroke="#f9fafb" stroke-width="17"/><path d="M 50 150 L 50 300 Q 50 306 56 306 L 204 306 Q 210 306 210 300 L 210 150" fill="none" stroke="#374151" stroke-width="2"/><path d="M 330 150 L 330 300 Q 330 306 336 306 L 484 306 Q 490 306 490 300 L 490 150" fill="none" stroke="#374151" stroke-width="2"/><rect x="100" y="120" width="22" height="150" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><rect x="418" y="120" width="22" height="150" fill="#d1d5db" stroke="#374151" stroke-width="1.5"/><text x="92" y="146" text-anchor="end" font-weight="bold">Cu</text><text x="448" y="146" font-weight="bold">Ag</text><polyline points="111,120 111,52 248,52" fill="none" stroke="#111827" stroke-width="2"/><polyline points="292,52 429,52 429,120" fill="none" stroke="#111827" stroke-width="2"/><circle cx="270" cy="52" r="22" fill="#ffffff" stroke="#111827" stroke-width="2"/><text x="270" y="58" text-anchor="middle" font-size="16" font-weight="bold">V</text><text x="270" y="20" text-anchor="middle">0.46 V</text><line x1="140" y1="36" x2="210" y2="36" stroke="#2563eb" stroke-width="2"/><polygon points="218,36 207,31 207,41" fill="#2563eb"/><text x="176" y="28" text-anchor="middle" fill="#2563eb">e⁻</text><text x="270" y="140" text-anchor="middle">Salt bridge</text><text x="270" y="157" text-anchor="middle">KNO₃(aq)</text><text x="130" y="327" text-anchor="middle">1.0 M Cu(NO₃)₂(aq)</text><text x="410" y="327" text-anchor="middle">1.0 M AgNO₃(aq)</text></svg></figure>"""
        ),
        "question": (
            r"The galvanic cell shown above operates at $298\text{ K}$. The voltmeter reads $0.46\text{ V}$, and electrons flow through the wire from the $\text{Cu}$ electrode to the $\text{Ag}$ electrode, as shown by the arrow. The voltmeter is then replaced with a DC power supply that forces electrons through the wire in the opposite direction, from the $\text{Ag}$ electrode to the $\text{Cu}$ electrode. Which of the following correctly describes the cell while the power supply is operating?"
        ),
        "options": [
            r"The cell is electrolytic: $\text{Ag}(s)$ is oxidized at the $\text{Ag}$ electrode, which is now the anode and loses mass, and $\text{Cu}^{2+}(aq)$ is reduced at the $\text{Cu}$ electrode, which is now the cathode and gains mass; the power supply must provide more than $0.46\text{ V}$.",
            r"The cell is still galvanic: $\text{Cu}(s)$ continues to be oxidized at the $\text{Cu}$ anode, which loses mass, because only the reaction with a positive $E_{\text{cell}}^\circ$ can occur.",
            r"$\text{Ag}(s)$ is oxidized and $\text{Cu}^{2+}(aq)$ is reduced, so the $\text{Ag}$ electrode is now the cathode and the $\text{Cu}$ electrode is now the anode.",
            r"No oxidation or reduction occurs at either electrode; the power supply only pushes electrons through the solutions and the salt bridge.",
        ],
        "correct_index": 0,
        "explanation": (
            r"Forcing electrons from $\text{Ag}$ to $\text{Cu}$ drives the reverse of the galvanic reaction: $2\text{Ag}(s) + \text{Cu}^{2+}(aq) \rightarrow 2\text{Ag}^+(aq) + \text{Cu}(s)$, with $E_{\text{cell}}^\circ = -0.46\text{ V}$ ($\Delta G^\circ > 0$). This thermodynamically unfavorable reaction occurs only because the external source supplies more than $0.46\text{ V}$, so the cell is now electrolytic. "
            r"Electrons leave the $\text{Ag}$ electrode because $\text{Ag}$ atoms are oxidized there ($\text{Ag} \rightarrow \text{Ag}^+ + e^-$), so it is the anode and loses mass; electrons arriving at the $\text{Cu}$ electrode reduce $\text{Cu}^{2+}$ ($\text{Cu}^{2+} + 2e^- \rightarrow \text{Cu}$), so it is the cathode and gains mass. "
            r"In every cell oxidation occurs at the anode, so calling the $\text{Ag}$ electrode the cathode is wrong. The original reaction cannot continue against the applied voltage, and electrons never travel through the solutions or the salt bridge; ions carry the current there."
        ),
    },
    {
        "unit_q_num": 59,
        "topic_code": "9.10",
        "topic_title": "Cell Potential Under Nonstandard Conditions",
        "difficulty": "Challenging",
        "stimulus": (
            r"$$\text{Zn}(s) + 2\text{Ag}^+(aq) \rightarrow \text{Zn}^{2+}(aq) + 2\text{Ag}(s) \qquad E_{\text{cell}}^\circ = +1.56\text{ V}$$"
        ),
        "question": (
            r"A galvanic cell based on the reaction above is set up at $298\text{ K}$ with $1.0\text{ M Zn(NO}_3)_2(aq)$ and $1.0\text{ M AgNO}_3(aq)$. A student replaces the solution in the zinc half-cell with $0.010\text{ M Zn(NO}_3)_2(aq)$ and observes that the cell potential increases to about $+1.62\text{ V}$. The student explains: “Lowering $[\text{Zn}^{2+}]$ removes a product, so by Le Châtelier’s principle the equilibrium shifts to the right, which increases $E_{\text{cell}}^\circ$.” Which of the following best evaluates the student’s explanation?"
        ),
        "options": [
            r"The explanation is correct: removing a product shifts the equilibrium toward the products, and this shift increases $E_{\text{cell}}^\circ$.",
            r"The explanation is flawed: the operating cell is not at equilibrium, so Le Châtelier’s principle does not apply. Lowering $[\text{Zn}^{2+}]$ makes $Q < 1$, which moves the cell farther from equilibrium and increases $E_{\text{cell}}$, while $E_{\text{cell}}^\circ$ is unchanged.",
            r"The observation must be in error: lowering $[\text{Zn}^{2+}]$ increases $Q$, so $E_{\text{cell}}$ should decrease below $+1.56\text{ V}$.",
            r"The explanation is flawed: cell potential depends only on the identities of the electrodes, so the increase must have been caused by a change in temperature.",
        ],
        "correct_index": 1,
        "explanation": (
            r"Equilibrium arguments such as Le Châtelier’s principle do not apply to an operating electrochemical cell, because it is not at equilibrium (at equilibrium $E_{\text{cell}} = 0$). "
            r"Instead, use $E = E^\circ - \frac{RT}{nF}\ln Q$ qualitatively, with $Q = \frac{[\text{Zn}^{2+}]}{[\text{Ag}^+]^2}$. Lowering $[\text{Zn}^{2+}]$ from $1.0\text{ M}$ to $0.010\text{ M}$ lowers $Q$ from $1$ to $0.010$, so $\ln Q < 0$ and $E_{\text{cell}} > E_{\text{cell}}^\circ$: the cell is farther from equilibrium ($Q \ll K$), so its driving force is larger. "
            r"$E_{\text{cell}}^\circ$ refers to standard conditions ($Q = 1$) and does not change, so the claim that it increases is wrong. Lowering a product concentration decreases $Q$ (it does not increase it), and concentrations do change $E_{\text{cell}}$ even though the electrodes are the same."
        ),
    },
    {
        "unit_q_num": 60,
        "topic_code": "9.11",
        "topic_title": "Electrolysis and Faraday's Law",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"A student electroplates copper onto a brass key by making the key the cathode in an electrolytic cell containing $\text{CuSO}_4(aq)$. A constant current of $0.500\text{ A}$ is passed for $1{,}930\text{ s}$. When the key is removed and weighed, its mass has increased by $0.281\text{ g}$. Which of the following could account for the difference between the measured mass gain and the theoretical mass gain?"
        ),
        "options": [
            r"The key was weighed while it was still wet with $\text{CuSO}_4(aq)$ solution.",
            r"The actual current was slightly greater than $0.500\text{ A}$ during the experiment.",
            r"Some of the copper that deposited on the key was loosely attached and fell off into the solution before the key was weighed.",
            r"The current was accidentally allowed to flow for longer than $1{,}930\text{ s}$.",
        ],
        "correct_index": 2,
        "explanation": (
            r"Theoretical gain: $q = It = (0.500\text{ A})(1{,}930\text{ s}) = 965\text{ C}$; $\frac{965\text{ C}}{96{,}485\text{ C/mol } e^-} = 0.0100\text{ mol } e^-$. Because $\text{Cu}^{2+} + 2e^- \rightarrow \text{Cu}$, $0.00500\text{ mol Cu} \times 63.55\text{ g/mol} = 0.318\text{ g}$. "
            r"The measured gain ($0.281\text{ g}$) is smaller than predicted, so the error must lower the measured mass: copper that falls off the key is not weighed. "
            r"Weighing a wet key adds the mass of the solution, a larger current delivers more charge, and a longer time also delivers more charge; each of these would make the measured mass greater than $0.318\text{ g}$, not smaller."
        ),
    },
]
