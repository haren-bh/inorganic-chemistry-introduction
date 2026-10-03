UNIT_META = {
    "id": 6,
    "title": "Unit 6: Thermochemistry",
    "short_title": "Thermochemistry & Enthalpy",
    "exam_weight": "7–9%",
    "color": "#dc2626",
    "description": "Endothermic and exothermic processes, system vs. surroundings, potential energy diagrams, thermal equilibrium, heat capacity and coffee-cup/bomb calorimetry (q = mcΔT), heating/cooling curves and enthalpy of phase changes, stoichiometric reaction enthalpy, average bond enthalpies, standard enthalpies of formation (ΔH°f), and Hess's Law.",
    "topics": [
        {"code": "6.1", "title": "Endothermic and Exothermic Processes"},
        {"code": "6.2", "title": "Energy Diagrams"},
        {"code": "6.3", "title": "Heat Transfer and Thermal Equilibrium"},
        {"code": "6.4", "title": "Heat Capacity and Calorimetry"},
        {"code": "6.5", "title": "Energy of Phase Changes"},
        {"code": "6.6", "title": "Introduction to Enthalpy of Reaction"},
        {"code": "6.7", "title": "Bond Enthalpies"},
        {"code": "6.8", "title": "Enthalpy of Formation"},
        {"code": "6.9", "title": "Hess's Law"},
    ],
}

QUESTIONS = [
    # -------------------------------------------------------------------------
    # 6.1 Endothermic and Exothermic Processes (Q1 - Q6)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 1,
        "topic_code": "6.1",
        "topic_title": "Endothermic and Exothermic Processes",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Experiment</th><th>Solute Added to $100.0\text{ g }\text{H}_2\text{O}(l)$</th><th>Initial Temp ($^\circ\text{C}$)</th><th>Final Temp ($^\circ\text{C}$)</th></tr></thead><tbody><tr><td>1</td><td>$5.00\text{ g }\text{NH}_4\text{NO}_3(s)$</td><td>$22.0$</td><td>$18.2$</td></tr><tr><td>2</td><td>$5.00\text{ g }\text{NaOH}(s)$</td><td>$22.0$</td><td>$34.1$</td></tr></tbody></table>""",
        "question": r"A student dissolves two different ionic solids in separate insulated beakers containing $100.0\text{ g}$ of distilled water and records the temperature changes above. If the dissolved ions and their hydration interactions are defined as the thermodynamic system and the bulk water and beaker are defined as the surroundings, which statement correctly describes Experiment 1?",
        "options": [
            r"The dissolution of $\text{NH}_4\text{NO}_3(s)$ is endothermic; $q_{\text{sys}} > 0$ and $q_{\text{surr}} < 0$.",
            r"The dissolution of $\text{NH}_4\text{NO}_3(s)$ is exothermic; $q_{\text{sys}} < 0$ and $q_{\text{surr}} > 0$.",
            r"The dissolution of $\text{NH}_4\text{NO}_3(s)$ is endothermic; $q_{\text{sys}} < 0$ and $q_{\text{surr}} > 0$.",
            r"The dissolution of $\text{NH}_4\text{NO}_3(s)$ is exothermic; $q_{\text{sys}} > 0$ and $q_{\text{surr}} < 0$.",
        ],
        "correct_index": 0,
        "explanation": r"The thermometer measures the temperature of the aqueous solution (part of the surroundings). Because the temperature drops from $22.0^\circ\text{C}$ to $18.2^\circ\text{C}$, the surroundings lose thermal energy ($q_{\text{surr}} < 0$) and the chemical system absorbs that thermal energy ($q_{\text{sys}} = -q_{\text{surr}} > 0$), which defines an endothermic process.",
    },
    {
        "unit_q_num": 2,
        "topic_code": "6.1",
        "topic_title": "Endothermic and Exothermic Processes",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"When an ideal gas is compressed isothermally inside a cylinder fitted with a movable piston, $450\text{ J}$ of work is done on the gas by the piston while $450\text{ J}$ of heat flows out of the gas into a surrounding water bath. Using the IUPAC sign convention ($\Delta E = q + w$), what are the signs of $q$, $w$, and $\Delta E$ for the gas?",
        "options": [
            r"$q > 0$, $w < 0$, and $\Delta E = 0$",
            r"$q < 0$, $w > 0$, and $\Delta E = 0$",
            r"$q < 0$, $w < 0$, and $\Delta E = -900\text{ J}$",
            r"$q > 0$, $w > 0$, and $\Delta E = +900\text{ J}$",
        ],
        "correct_index": 1,
        "explanation": r"Heat flows out of the system into the surroundings, so $q = -450\text{ J} < 0$ (exothermic). Work is done on the system by compressing the gas ($w = -P_{\text{ext}}\Delta V$ with $\Delta V < 0$), so $w = +450\text{ J} > 0$. Therefore, $\Delta E = q + w = -450\text{ J} + 450\text{ J} = 0\text{ J}$.",
    },
    {
        "unit_q_num": 3,
        "topic_code": "6.1",
        "topic_title": "Endothermic and Exothermic Processes",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Step in Dissolution of $\text{MX}(s)$</th><th>Enthalpy Change ($\text{kJ/mol}$)</th></tr></thead><tbody><tr><td>Separation of $\text{MX}(s)$ into $\text{M}^+(g) + \text{X}^-(g)$</td><td>$\Delta H_1 = +790$</td></tr><tr><td>Separation of $\text{H}_2\text{O}(l)$ molecules to form cavities</td><td>$\Delta H_2 = +115$</td></tr><tr><td>Ion-dipole attraction of $\text{M}^+(g)$ and $\text{X}^-(g)$ with $\text{H}_2\text{O}(l)$</td><td>$\Delta H_3 = -880$</td></tr></tbody></table>""",
        "question": r"The dissolution of the ionic salt $\text{MX}(s)$ in water can be modeled as the three-step thermodynamic cycle shown above. Based on the microscopic interactions and enthalpy values provided, which statement is true when $0.50\text{ mol}$ of $\text{MX}(s)$ dissolves in an insulated container of water?",
        "options": [
            r"The overall dissolution is exothermic ($\Delta H_{\text{soln}}^\circ = -25\text{ kJ/mol}$), and the temperature of the solution increases.",
            r"The overall dissolution is endothermic ($\Delta H_{\text{soln}}^\circ = +25\text{ kJ/mol}$), and $12.5\text{ kJ}$ of thermal energy is absorbed from the solution.",
            r"The ion-dipole attractions release more energy than is required to overcome the ionic lattice and hydrogen bonds.",
            r"The overall dissolution is endothermic ($\Delta H_{\text{soln}}^\circ = +25\text{ kJ/mol}$), causing the temperature of the solution to increase.",
        ],
        "correct_index": 1,
        "explanation": r"Summing the steps gives $\Delta H_{\text{soln}}^\circ = \Delta H_1 + \Delta H_2 + \Delta H_3 = (+790) + (+115) + (-880) = +25\text{ kJ/mol}$. Because $\Delta H_{\text{soln}}^\circ > 0$, the dissolution is endothermic. For $0.50\text{ mol}$ of $\text{MX}(s)$, $q_{\text{rxn}} = (0.50\text{ mol})(+25\text{ kJ/mol}) = +12.5\text{ kJ}$ is absorbed from the surrounding water, causing the solution temperature to decrease.",
    },
    {
        "unit_q_num": 4,
        "topic_code": "6.1",
        "topic_title": "Endothermic and Exothermic Processes",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"Which of the following physical or chemical processes is exothermic ($\Delta H < 0$)?",
        "options": [
            r"$\text{CO}_2(s) \rightarrow \text{CO}_2(g)$",
            r"$\text{Cl}_2(g) \rightarrow 2\,\text{Cl}(g)$",
            r"$\text{H}_2\text{O}(g) \rightarrow \text{H}_2\text{O}(l)$",
            r"$\text{Na}(g) \rightarrow \text{Na}^+(g) + e^-$",
        ],
        "correct_index": 2,
        "explanation": r"Condensation ($\text{H}_2\text{O}(g) \rightarrow \text{H}_2\text{O}(l)$) forms intermolecular hydrogen bonds between water molecules, releasing potential energy as heat ($\Delta H < 0$). Sublimation ($\text{CO}_2(s) \rightarrow \text{CO}_2(g)$), homolytic bond cleavage ($\text{Cl}_2(g) \rightarrow 2\,\text{Cl}(g)$), and ionization ($\text{Na}(g) \rightarrow \text{Na}^+(g) + e^-$) all require energy input to overcome attractive forces ($\Delta H > 0$).",
    },
    {
        "unit_q_num": 5,
        "topic_code": "6.1",
        "topic_title": "Endothermic and Exothermic Processes",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A chemical reaction is carried out in a sealed, rigid steel vessel that is submerged in an insulated water bath. As the reaction proceeds, the temperature of the water bath increases. Which statement accurately describes the energy changes that occur?",
        "options": [
            r"Kinetic energy of the water molecules is converted into chemical potential energy of the reacting species, so the energy of the reaction system increases.",
            r"The reaction creates thermal energy, so the energy of the reaction system and the energy of the water bath both increase.",
            r"The energy of the reaction system remains constant because the sealed vessel prevents any matter from entering or leaving it.",
            r"Chemical potential energy of the reacting species decreases, and this energy is transferred as heat to the water bath, increasing the average kinetic energy of the water molecules.",
        ],
        "correct_index": 3,
        "explanation": r"The rising temperature of the water bath (the surroundings) shows that the average kinetic energy of the water molecules increases, so thermal energy is transferred from the reaction system to the bath ($q_{\text{sys}} < 0$): the reaction is exothermic. That energy comes from a decrease in chemical potential energy, because the products have a lower potential energy than the reactants. Energy is conserved, not created, so the bath gains exactly the energy that the system loses; the energy of both cannot increase. A sealed vessel prevents the transfer of matter but not the transfer of energy as heat through its steel walls, so the system's energy does change. Converting kinetic energy of the water into potential energy of the system would cool the bath (an endothermic process).",
    },
    {
        "unit_q_num": 6,
        "topic_code": "6.1",
        "topic_title": "Endothermic and Exothermic Processes",
        "difficulty": "Challenging",
        "stimulus": r"$$\text{CaO}(s) + \text{H}_2\text{O}(l) \rightarrow \text{Ca(OH)}_2(s) \quad \Delta H^\circ = -65.2\text{ kJ/mol}_{\text{rxn}}$$",
        "question": r"Some self-heating food cans use the reaction of calcium oxide with water shown above. Which statement best explains the source of the thermal energy transferred to the food during this reaction?",
        "options": [
            r"Breaking the bonds in $\text{CaO}(s)$ and $\text{H}_2\text{O}(l)$ releases $65.2\text{ kJ/mol}_{\text{rxn}}$ of thermal energy.",
            r"The total kinetic energy of the system decreases because $\Delta H^\circ$ is negative, cooling the reaction mixture.",
            r"Mass is destroyed during the hydration of $\text{CaO}(s)$ and converted directly into thermal energy according to $q = mc\Delta T$.",
            r"The total potential energy of the products is lower than the total potential energy of the reactants because more energy is released forming bonds in $\text{Ca(OH)}_2(s)$ than is absorbed breaking bonds in the reactants.",
        ],
        "correct_index": 3,
        "explanation": r"Bond breaking is always endothermic and bond formation is always exothermic. A reaction is exothermic ($\Delta H^\circ < 0$) when the energy released in forming stronger bonds/interactions in the products exceeds the energy required to break the bonds/interactions in the reactants, lowering the chemical potential energy of the system.",
    },

    # -------------------------------------------------------------------------
    # 6.2 Energy Diagrams (Q7 - Q11)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 7,
        "topic_code": "6.2",
        "topic_title": "Energy Diagrams",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>State on Potential Energy Profile</th><th>Relative Potential Energy ($\text{kJ/mol}_{\text{rxn}}$)</th></tr></thead><tbody><tr><td>Reactants ($\text{A} + \text{B}$)</td><td>$45$</td></tr><tr><td>Transition State ($\text{AB}^\ddagger$)</td><td>$185$</td></tr><tr><td>Products ($\text{C} + \text{D}$)</td><td>$110$</td></tr></tbody></table>""",
        "question": r"Based on the potential energy profile values in the table above for the elementary reaction $\text{A} + \text{B} \rightleftharpoons \text{C} + \text{D}$, what are the enthalpy change of the forward reaction ($\Delta H_{\text{fwd}}$) and the activation energy of the reverse reaction ($E_{a,\text{rev}}$)?",
        "options": [
            r"$\Delta H_{\text{fwd}} = +65\text{ kJ/mol}_{\text{rxn}}$ and $E_{a,\text{rev}} = 75\text{ kJ/mol}_{\text{rxn}}$",
            r"$\Delta H_{\text{fwd}} = -65\text{ kJ/mol}_{\text{rxn}}$ and $E_{a,\text{rev}} = 140\text{ kJ/mol}_{\text{rxn}}$",
            r"$\Delta H_{\text{fwd}} = +65\text{ kJ/mol}_{\text{rxn}}$ and $E_{a,\text{rev}} = 140\text{ kJ/mol}_{\text{rxn}}$",
            r"$\Delta H_{\text{fwd}} = +140\text{ kJ/mol}_{\text{rxn}}$ and $E_{a,\text{rev}} = 75\text{ kJ/mol}_{\text{rxn}}$",
        ],
        "correct_index": 0,
        "explanation": r"The enthalpy change of the forward reaction is $\Delta H_{\text{fwd}} = E_{\text{products}} - E_{\text{reactants}} = 110 - 45 = +65\text{ kJ/mol}_{\text{rxn}}$ (endothermic). The activation energy of the reverse reaction is the barrier from products to the transition state: $E_{a,\text{rev}} = E_{\text{TS}} - E_{\text{products}} = 185 - 110 = 75\text{ kJ/mol}_{\text{rxn}}$.",
    },
    {
        "unit_q_num": 8,
        "topic_code": "6.2",
        "topic_title": "Energy Diagrams",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"For a certain single-step gas-phase reaction, the activation energy of the forward reaction is $E_{a,\text{fwd}} = 92\text{ kJ/mol}_{\text{rxn}}$ and the activation energy of the reverse reaction is $E_{a,\text{rev}} = 218\text{ kJ/mol}_{\text{rxn}}$. Which of the following correctly gives $\Delta H_{\text{rxn}}^\circ$ for the forward reaction and compares the potential energy of reactants and products?",
        "options": [
            r"$\Delta H_{\text{rxn}}^\circ = +126\text{ kJ/mol}_{\text{rxn}}$; products have higher potential energy than reactants.",
            r"$\Delta H_{\text{rxn}}^\circ = -126\text{ kJ/mol}_{\text{rxn}}$; products have lower potential energy than reactants.",
            r"$\Delta H_{\text{rxn}}^\circ = -310\text{ kJ/mol}_{\text{rxn}}$; products have lower potential energy than reactants.",
            r"$\Delta H_{\text{rxn}}^\circ = +310\text{ kJ/mol}_{\text{rxn}}$; products have higher potential energy than reactants.",
        ],
        "correct_index": 1,
        "explanation": r"On any potential energy diagram, $\Delta H_{\text{rxn}}^\circ = E_{a,\text{fwd}} - E_{a,\text{rev}} = 92\text{ kJ/mol}_{\text{rxn}} - 218\text{ kJ/mol}_{\text{rxn}} = -126\text{ kJ/mol}_{\text{rxn}}$. Because $\Delta H_{\text{rxn}}^\circ < 0$, the reaction is exothermic and the products lie at a lower potential energy than the reactants.",
    },
    {
        "unit_q_num": 9,
        "topic_code": "6.2",
        "topic_title": "Energy Diagrams",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Species / State</th><th>Potential Energy ($\text{kJ/mol}_{\text{rxn}}$)</th></tr></thead><tbody><tr><td>Reactants ($\text{R}$)</td><td>$0$</td></tr><tr><td>First Transition State ($\text{TS}_1$)</td><td>$+85$</td></tr><tr><td>Intermediate ($\text{I}$)</td><td>$+30$</td></tr><tr><td>Second Transition State ($\text{TS}_2$)</td><td>$+60$</td></tr><tr><td>Products ($\text{P}$)</td><td>$-45$</td></tr></tbody></table>""",
        "question": r"A two-step reaction $\text{R} \rightarrow \text{I} \rightarrow \text{P}$ has the potential energy profile summarized in the table above. Which of the following statements about the enthalpy changes of the individual steps and the overall reaction is correct?",
        "options": [
            r"Step 1 is exothermic ($\Delta H_1 = -30\text{ kJ/mol}_{\text{rxn}}$), Step 2 is endothermic ($\Delta H_2 = +75\text{ kJ/mol}_{\text{rxn}}$), and the overall reaction has $\Delta H_{\text{overall}} = -45\text{ kJ/mol}_{\text{rxn}}$.",
            r"The overall enthalpy change depends on the height of $\text{TS}_1$ and equals $+85 - 45 = +40\text{ kJ/mol}_{\text{rxn}}$.",
            r"Step 1 is endothermic ($\Delta H_1 = +30\text{ kJ/mol}_{\text{rxn}}$), Step 2 is exothermic ($\Delta H_2 = -75\text{ kJ/mol}_{\text{rxn}}$), and the overall reaction has $\Delta H_{\text{overall}} = -45\text{ kJ/mol}_{\text{rxn}}$.",
            r"Adding a catalyst that lowers $\text{TS}_1$ from $+85$ to $+50\text{ kJ/mol}_{\text{rxn}}$ makes $\Delta H_{\text{overall}}$ more exothermic by $35\text{ kJ/mol}_{\text{rxn}}$.",
        ],
        "correct_index": 2,
        "explanation": r"For Step 1 ($\text{R} \rightarrow \text{I}$), $\Delta H_1 = 30 - 0 = +30\text{ kJ/mol}_{\text{rxn}}$ (endothermic). For Step 2 ($\text{I} \rightarrow \text{P}$), $\Delta H_2 = -45 - 30 = -75\text{ kJ/mol}_{\text{rxn}}$ (exothermic). The overall enthalpy change is $\Delta H_{\text{overall}} = \Delta H_1 + \Delta H_2 = (+30) + (-75) = -45\text{ kJ/mol}_{\text{rxn}}$; it depends only on the energies of the reactants and products, not on the heights of the transition states or on the presence of a catalyst.",
    },
    {
        "unit_q_num": 10,
        "topic_code": "6.2",
        "topic_title": "Energy Diagrams",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"How does the addition of a homogeneous catalyst alter the potential energy diagram of an exothermic reaction?",
        "options": [
            r"It lowers the potential energy of the products, making $\Delta H_{\text{rxn}}^\circ$ more negative.",
            r"It raises the potential energy of the reactants so that they are closer in energy to the transition state.",
            r"It provides an alternative pathway with a lower-energy transition state, decreasing both $E_{a,\text{fwd}}$ and $E_{a,\text{rev}}$ by the same amount while leaving $\Delta H_{\text{rxn}}^\circ$ unchanged.",
            r"It decreases $E_{a,\text{fwd}}$ for the exothermic direction but increases $E_{a,\text{rev}}$ for the endothermic reverse direction.",
        ],
        "correct_index": 2,
        "explanation": r"The value of $\Delta H_{\text{rxn}}^\circ$ depends only on the potential energies of the reactants and the products. A catalyst provides a different mechanism with a lower-energy transition state, reducing both $E_{a,\text{fwd}}$ and $E_{a,\text{rev}}$ equally without altering the potential energy of reactants or products ($\Delta H_{\text{rxn}}^\circ$ is unchanged).",
    },
    {
        "unit_q_num": 11,
        "topic_code": "6.2",
        "topic_title": "Energy Diagrams",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"Consider the potential energy curve as a function of internuclear distance $r$ for two ground-state hydrogen atoms approaching each other to form an $\text{H}_2(g)$ molecule. If the zero of potential energy ($E_p = 0$) is defined at infinite separation ($r \rightarrow \infty$), and the potential energy minimum at the equilibrium bond length $r_0 = 74\text{ pm}$ is $-436\text{ kJ/mol}$, which statement is correct?",
        "options": [
            r"At $r = 74\text{ pm}$, $436\text{ kJ/mol}$ of energy is absorbed to form the $\text{H}-\text{H}$ covalent bond.",
            r"Moving two $\text{H}$ atoms from $r = 74\text{ pm}$ to $r \rightarrow \infty$ is an exothermic process with $\Delta H = -436\text{ kJ/mol}$.",
            r"At $r = 74\text{ pm}$, there are no electrostatic forces acting between the protons and electrons.",
            r"For $r < 74\text{ pm}$, internuclear repulsive forces dominate and the potential energy rises steeply above $-436\text{ kJ/mol}$.",
        ],
        "correct_index": 3,
        "explanation": r"At the equilibrium bond length $r_0 = 74\text{ pm}$, attractive and repulsive electrostatic forces balance at a potential energy minimum of $-436\text{ kJ/mol}$. Compressing the bond to $r < 74\text{ pm}$ causes nucleus-nucleus and electron-electron repulsions to dominate, sharply increasing potential energy. Dissociating the bond ($r_0 \rightarrow \infty$) requires $+436\text{ kJ/mol}$ (endothermic).",
    },

    # -------------------------------------------------------------------------
    # 6.3 Heat Transfer and Thermal Equilibrium (Q12 - Q16)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 12,
        "topic_code": "6.3",
        "topic_title": "Heat Transfer and Thermal Equilibrium",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A $50.0\text{ g}$ block of copper at $85.0^\circ\text{C}$ is placed in direct thermal contact with a $50.0\text{ g}$ block of aluminum at $25.0^\circ\text{C}$ inside an insulated, evacuated chamber until thermal equilibrium is reached. Which statement accurately describes the particulate-level events during this process?",
        "options": [
            r"Atoms in the copper block transfer kinetic energy to atoms in the aluminum block via collisions at the interface until the atoms of both metals have the same average kinetic energy.",
            r"Electrons and copper atoms diffuse into the aluminum block until both blocks have the same total internal energy.",
            r"Thermal energy flows from the aluminum block into the copper block because aluminum has a higher specific heat capacity than copper.",
            r"At thermal equilibrium, individual copper atoms and aluminum atoms vibrate with the exact same average speed.",
        ],
        "correct_index": 0,
        "explanation": r"Heat flows spontaneously from the higher-temperature object ($\text{Cu}$ at $85.0^\circ\text{C}$) to the lower-temperature object ($\text{Al}$ at $25.0^\circ\text{C}$) via particle collisions at their contact surface. At thermal equilibrium, both blocks reach the same final temperature, meaning their particles have the same average kinetic energy (though not the same average speed, since $m_{\text{Cu}} > m_{\text{Al}}$).",
    },
    {
        "unit_q_num": 13,
        "topic_code": "6.3",
        "topic_title": "Heat Transfer and Thermal Equilibrium",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Gas Sample</th><th>Moles ($n$)</th><th>Temperature ($K$)</th><th>Molar Mass ($\text{g/mol}$)</th></tr></thead><tbody><tr><td>$\text{He}(g)$</td><td>$2.0\text{ mol}$</td><td>$300\text{ K}$</td><td>$4.00$</td></tr><tr><td>$\text{Ar}(g)$</td><td>$1.0\text{ mol}$</td><td>$300\text{ K}$</td><td>$39.95$</td></tr></tbody></table>""",
        "question": r"The two gas samples described in the table above are separated by a rigid, thermally conductive metal partition. Which of the following occurs after the gases are placed in contact across the partition?",
        "options": [
            r"Net heat flows from $\text{He}(g)$ to $\text{Ar}(g)$ because $\text{He}(g)$ contains twice as many moles and twice the total thermal energy.",
            r"Net heat flows from $\text{He}(g)$ to $\text{Ar}(g)$ because $\text{He}$ atoms move at a higher root-mean-square speed and collide more frequently with the partition.",
            r"Net heat flows from $\text{Ar}(g)$ to $\text{He}(g)$ because $\text{Ar}$ atoms have a greater mass and transfer more momentum per collision.",
            r"There is no net transfer of thermal energy between $\text{He}(g)$ and $\text{Ar}(g)$ because both gases are already at $300\text{ K}$ and have the same average kinetic energy per atom.",
        ],
        "correct_index": 3,
        "explanation": r"Temperature is a measure of average translational kinetic energy ($\overline{KE} = \frac{3}{2}k_BT$). Because both $\text{He}(g)$ and $\text{Ar}(g)$ are at $300\text{ K}$, they are already in thermal equilibrium and have the same average kinetic energy per atom; therefore, no net heat transfer ($q = 0$) occurs across the partition.",
    },
    {
        "unit_q_num": 14,
        "topic_code": "6.3",
        "topic_title": "Heat Transfer and Thermal Equilibrium",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"A $100.0\text{ g}$ sample of liquid water at $20.0^\circ\text{C}$ is mixed with a $50.0\text{ g}$ sample of liquid water at $80.0^\circ\text{C}$ in a well-insulated container with negligible heat capacity. Assuming no heat is lost to the surroundings, what is the final temperature of the combined water at thermal equilibrium?",
        "options": [
            r"$40.0^\circ\text{C}$",
            r"$45.0^\circ\text{C}$",
            r"$50.0^\circ\text{C}$",
            r"$60.0^\circ\text{C}$",
        ],
        "correct_index": 0,
        "explanation": r"By conservation of energy, $q_{\text{cold}} + q_{\text{hot}} = 0$. Since both samples are liquid water with identical specific heat capacity $c$, $m_{\text{cold}}(T_f - 20.0) + m_{\text{hot}}(T_f - 80.0) = 0 \implies 100.0(T_f - 20.0) + 50.0(T_f - 80.0) = 0 \implies 150.0\,T_f = 2000 + 4000 = 6000 \implies T_f = 40.0^\circ\text{C}$.",
    },
    {
        "unit_q_num": 15,
        "topic_code": "6.3",
        "topic_title": "Heat Transfer and Thermal Equilibrium",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A piece of iron ($c = 0.449\text{ J/(g}\cdot^\circ\text{C)}$) at $90.0^\circ\text{C}$ is dropped into an insulated cup containing an equal mass of water ($c = 4.184\text{ J/(g}\cdot^\circ\text{C)}$) at $20.0^\circ\text{C}$. When thermal equilibrium is reached, how does the final temperature $T_f$ compare to the midpoint temperature of $55.0^\circ\text{C}$, and how do the magnitudes of heat transferred compare?",
        "options": [
            r"$T_f < 55.0^\circ\text{C}$, and $|q_{\text{Fe}}| > |q_{\text{H}_2\text{O}}|$",
            r"$T_f > 55.0^\circ\text{C}$, and $|q_{\text{Fe}}| = |q_{\text{H}_2\text{O}}|$",
            r"$T_f < 55.0^\circ\text{C}$, and $|q_{\text{Fe}}| = |q_{\text{H}_2\text{O}}|$",
            r"$T_f = 55.0^\circ\text{C}$, and $|q_{\text{Fe}}| = |q_{\text{H}_2\text{O}}|$",
        ],
        "correct_index": 2,
        "explanation": r"By conservation of energy in an insulated system, the thermal energy lost by the iron equals the thermal energy gained by the water ($|q_{\text{Fe}}| = |q_{\text{H}_2\text{O}}|$). Because water has a much larger specific heat capacity than iron ($4.184$ vs. $0.449\text{ J/(g}\cdot^\circ\text{C)}$) and their masses are equal, water undergoes a much smaller temperature change ($\Delta T_{\text{H}_2\text{O}} \ll |\Delta T_{\text{Fe}}|$), so $T_f$ is much closer to $20.0^\circ\text{C}$ ($T_f \approx 26.8^\circ\text{C} < 55.0^\circ\text{C}$).",
    },
    {
        "unit_q_num": 16,
        "topic_code": "6.3",
        "topic_title": "Heat Transfer and Thermal Equilibrium",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Metal</th><th>Atomic Mass ($\text{g/mol}$)</th><th>Specific Heat Capacity ($\text{J/(g}\cdot\text{K)}$)</th></tr></thead><tbody><tr><td>$\text{Al}$</td><td>$26.98$</td><td>$0.900$</td></tr><tr><td>$\text{Fe}$</td><td>$55.85$</td><td>$0.449$</td></tr><tr><td>$\text{Cu}$</td><td>$63.55$</td><td>$0.385$</td></tr><tr><td>$\text{Au}$</td><td>$196.97$</td><td>$0.129$</td></tr></tbody></table>""",
        "question": r"According to the Dulong-Petit law, solid metals near room temperature have approximately the same molar heat capacity ($C_m \approx 25\text{ J/(mol}\cdot\text{K)}$), as illustrated by the data above. Suppose $1.00\text{ mol}$ of $\text{Au}(s)$ at $100.0^\circ\text{C}$ is placed in thermal contact with $1.00\text{ mol}$ of $\text{Al}(s)$ at $20.0^\circ\text{C}$ in an insulated chamber. What will be the approximate final equilibrium temperature?",
        "options": [
            r"$30.0^\circ\text{C}$, because gold has a much lower specific heat capacity than aluminum.",
            r"$60.9^\circ\text{C}$, because equal numbers of moles of the two metals have nearly equal total heat capacities ($nC_m$).",
            r"$90.4^\circ\text{C}$, because $1.00\text{ mol}$ of gold has more than seven times the mass of $1.00\text{ mol}$ of aluminum.",
            r"$45.0^\circ\text{C}$, because aluminum atoms vibrate faster than gold atoms.",
        ],
        "correct_index": 1,
        "explanation": r"For $1.00\text{ mol}$ of $\text{Au}$, the heat capacity is $(196.97\text{ g})(0.129\text{ J/(g}\cdot\text{K)}) = 25.4\text{ J/K}$. For $1.00\text{ mol}$ of $\text{Al}$, the heat capacity is $(26.98\text{ g})(0.900\text{ J/(g}\cdot\text{K)}) = 24.3\text{ J/K}$. Because the two 1.00-mole blocks have nearly identical total heat capacities ($C = mc = nC_m \approx 25\text{ J/K}$), their temperature changes have nearly equal magnitudes, giving a final temperature very close to the midpoint of $60.0^\circ\text{C}$ ($60.9^\circ\text{C}$).",
    },

    # -------------------------------------------------------------------------
    # 6.4 Heat Capacity and Calorimetry (Q17 - Q22)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 17,
        "topic_code": "6.4",
        "topic_title": "Heat Capacity and Calorimetry",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Measurement</th><th>Value</th></tr></thead><tbody><tr><td>Mass of unknown metal sample</td><td>$65.0\text{ g}$</td></tr><tr><td>Initial temperature of metal</td><td>$98.5^\circ\text{C}$</td></tr><tr><td>Mass of water in calorimeter</td><td>$100.0\text{ g}$</td></tr><tr><td>Initial temperature of water</td><td>$22.0^\circ\text{C}$</td></tr><tr><td>Final temperature at thermal equilibrium</td><td>$26.5^\circ\text{C}$</td></tr></tbody></table>""",
        "question": r"A student performs a coffee-cup calorimetry experiment using the data in the table above to determine the specific heat capacity of an unknown metal. Assuming the specific heat capacity of water is $4.184\text{ J/(g}\cdot^\circ\text{C)}$ and the calorimeter absorbs negligible heat, what is the specific heat capacity of the metal?",
        "options": [
            r"$0.294\text{ J/(g}\cdot^\circ\text{C)}$",
            r"$0.402\text{ J/(g}\cdot^\circ\text{C)}$",
            r"$0.518\text{ J/(g}\cdot^\circ\text{C)}$",
            r"$1.09\text{ J/(g}\cdot^\circ\text{C)}$",
        ],
        "correct_index": 1,
        "explanation": r"Heat gained by water: $q_{\text{H}_2\text{O}} = m_{\text{H}_2\text{O}} c_{\text{H}_2\text{O}} \Delta T_{\text{H}_2\text{O}} = (100.0\text{ g})(4.184\text{ J/(g}\cdot^\circ\text{C)})(26.5^\circ\text{C} - 22.0^\circ\text{C}) = +1882.8\text{ J}$. Since $q_{\text{metal}} = -q_{\text{H}_2\text{O}} = -1882.8\text{ J}$ and $\Delta T_{\text{metal}} = 26.5^\circ\text{C} - 98.5^\circ\text{C} = -72.0^\circ\text{C}$, we have $c_{\text{metal}} = \frac{-1882.8\text{ J}}{(65.0\text{ g})(-72.0^\circ\text{C})} = 0.402\text{ J/(g}\cdot^\circ\text{C)}$.",
    },
    {
        "unit_q_num": 18,
        "topic_code": "6.4",
        "topic_title": "Heat Capacity and Calorimetry",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"When $50.0\text{ mL}$ of $1.00\text{ M }\text{HCl}(aq)$ at $21.5^\circ\text{C}$ is mixed with $50.0\text{ mL}$ of $1.00\text{ M }\text{NaOH}(aq)$ at $21.5^\circ\text{C}$ in a coffee-cup calorimeter, the temperature of the resulting solution rises to $28.2^\circ\text{C}$. Assuming the final solution has a density of $1.00\text{ g/mL}$ and a specific heat capacity of $4.18\text{ J/(g}\cdot^\circ\text{C)}$, what is $\Delta H_{\text{rxn}}^\circ$ for the neutralization reaction $\text{H}^+(aq) + \text{OH}^-(aq) \rightarrow \text{H}_2\text{O}(l)$?",
        "options": [
            r"$-2.80\text{ kJ/mol}_{\text{rxn}}$",
            r"$+2.80\text{ kJ/mol}_{\text{rxn}}$",
            r"$-56.0\text{ kJ/mol}_{\text{rxn}}$",
            r"$+56.0\text{ kJ/mol}_{\text{rxn}}$",
        ],
        "correct_index": 2,
        "explanation": r"Total mass of solution $m = (50.0 + 50.0\text{ mL})(1.00\text{ g/mL}) = 100.0\text{ g}$. Heat absorbed by the solution: $q_{\text{soln}} = (100.0\text{ g})(4.18\text{ J/(g}\cdot^\circ\text{C)})(28.2 - 21.5^\circ\text{C}) = +2800.6\text{ J} = +2.80\text{ kJ}$. Thus $q_{\text{rxn}} = -q_{\text{soln}} = -2.80\text{ kJ}$. Moles of reaction: $n = (0.0500\text{ L})(1.00\text{ M}) = 0.0500\text{ mol}_{\text{rxn}}$. Therefore, $\Delta H_{\text{rxn}}^\circ = \frac{-2.80\text{ kJ}}{0.0500\text{ mol}_{\text{rxn}}} = -56.0\text{ kJ/mol}_{\text{rxn}}$.",
    },
    {
        "unit_q_num": 19,
        "topic_code": "6.4",
        "topic_title": "Heat Capacity and Calorimetry",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"In a coffee-cup calorimetry experiment, a student mixes $50.0\text{ mL}$ of $1.00\text{ M }\text{HCl}(aq)$ with $50.0\text{ mL}$ of $1.00\text{ M }\text{NaOH}(aq)$, both initially at $21.5^\circ\text{C}$, and the temperature of the mixture rises by $6.7^\circ\text{C}$. Suppose the student repeats the experiment using $100.0\text{ mL}$ of $1.00\text{ M }\text{HCl}(aq)$ and $100.0\text{ mL}$ of $1.00\text{ M }\text{NaOH}(aq)$, both initially at $21.5^\circ\text{C}$. How will the magnitude of heat released ($|q_{\text{rxn}}|$), the temperature change ($\Delta T$), and the molar enthalpy of neutralization ($\Delta H_{\text{rxn}}^\circ$) compare to the first trial?",
        "options": [
            r"$|q_{\text{rxn}}|$ doubles, $\Delta T$ doubles, and $\Delta H_{\text{rxn}}^\circ$ remains the same.",
            r"$|q_{\text{rxn}}|$ remains the same, $\Delta T$ is halved, and $\Delta H_{\text{rxn}}^\circ$ is halved.",
            r"$|q_{\text{rxn}}|$ doubles, $\Delta T$ remains the same, and $\Delta H_{\text{rxn}}^\circ$ doubles.",
            r"$|q_{\text{rxn}}|$ doubles, $\Delta T$ remains the same, and $\Delta H_{\text{rxn}}^\circ$ remains the same.",
        ],
        "correct_index": 3,
        "explanation": r"Doubling the volumes at the same molarity doubles the moles of limiting reactant ($0.100\text{ mol}$ vs. $0.0500\text{ mol}$), so the heat released $|q_{\text{rxn}}|$ doubles. However, the total mass of the solution also doubles ($200.0\text{ g}$ vs. $100.0\text{ g}$), so $\Delta T = \frac{q_{\text{soln}}}{mc}$ remains unchanged ($6.7^\circ\text{C}$). Because $\Delta H_{\text{rxn}}^\circ = \frac{q_{\text{rxn}}}{n_{\text{rxn}}}$ is an intensive ratio per mole of reaction, it also remains unchanged.",
    },
    {
        "unit_q_num": 20,
        "topic_code": "6.4",
        "topic_title": "Heat Capacity and Calorimetry",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Bomb Calorimetry Parameter</th><th>Value</th></tr></thead><tbody><tr><td>Mass of benzoic acid ($\text{C}_7\text{H}_6\text{O}_2$, $M = 122.12\text{ g/mol}$)</td><td>$1.221\text{ g}$</td></tr><tr><td>Heat capacity of bomb calorimeter ($C_{\text{cal}}$)</td><td>$10.50\text{ kJ/}^\circ\text{C}$</td></tr><tr><td>Initial temperature</td><td>$23.10^\circ\text{C}$</td></tr><tr><td>Final temperature</td><td>$26.17^\circ\text{C}$</td></tr></tbody></table>""",
        "question": r"A $1.221\text{ g}$ sample of benzoic acid ($\text{C}_7\text{H}_6\text{O}_2$) is completely burned in excess oxygen inside a bomb calorimeter, giving the data above. Assuming that all of the heat released by the combustion is absorbed by the calorimeter, what is the molar heat of combustion of benzoic acid ($q_{\text{rxn}}$ per mole of $\text{C}_7\text{H}_6\text{O}_2$ burned)?",
        "options": [
            r"$-32.2\text{ kJ/mol}$",
            r"$+32.2\text{ kJ/mol}$",
            r"$-3220\text{ kJ/mol}$",
            r"$+3220\text{ kJ/mol}$",
        ],
        "correct_index": 2,
        "explanation": r"Heat absorbed by the calorimeter: $q_{\text{cal}} = C_{\text{cal}}\Delta T = (10.50\text{ kJ/}^\circ\text{C})(26.17 - 23.10^\circ\text{C}) = (10.50)(3.07) = +32.235\text{ kJ}$. Therefore, $q_{\text{rxn}} = -q_{\text{cal}} = -32.235\text{ kJ}$. The number of moles of benzoic acid burned is $n = \frac{1.221\text{ g}}{122.12\text{ g/mol}} = 0.01000\text{ mol}$. Dividing gives $\frac{q_{\text{rxn}}}{n} = \frac{-32.235\text{ kJ}}{0.01000\text{ mol}} = -3224\text{ kJ/mol} \approx -3220\text{ kJ/mol}$ (negative because the combustion releases heat). The value $-32.2$ omits dividing by the number of moles, and the positive values have the wrong sign for an exothermic process.",
    },
    {
        "unit_q_num": 21,
        "topic_code": "6.4",
        "topic_title": "Heat Capacity and Calorimetry",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"A student dissolves $5.35\text{ g}$ of $\text{NH}_4\text{Cl}(s)$ ($M = 53.49\text{ g/mol}$, $\Delta H_{\text{soln}}^\circ = +14.8\text{ kJ/mol}$) in $94.65\text{ g}$ of distilled water initially at $25.0^\circ\text{C}$ in a coffee-cup calorimeter. In calculating the final temperature of the solution, which expression uses the most physically rigorous mass $m_{\text{soln}}$ in $q_{\text{soln}} = m_{\text{soln}} c_{\text{soln}} \Delta T$, and what is the resulting final temperature (assuming $c_{\text{soln}} = 4.00\text{ J/(g}\cdot^\circ\text{C)}$ and negligible calorimeter heat capacity)?",
        "options": [
            r"Use $m_{\text{soln}} = 100.0\text{ g}$ (water plus dissolved solute); $T_f = 21.3^\circ\text{C}$.",
            r"Use $m_{\text{soln}} = 100.0\text{ g}$ (water plus dissolved solute); $T_f = 28.7^\circ\text{C}$.",
            r"Use $m_{\text{soln}} = 94.65\text{ g}$ (water only, excluding the solute ions); $T_f = 21.1^\circ\text{C}$.",
            r"Use $m_{\text{soln}} = 94.65\text{ g}$ (water only, excluding the solute ions); $T_f = 28.9^\circ\text{C}$.",
        ],
        "correct_index": 0,
        "explanation": r"When a solid dissolves in water, the resulting aqueous solution includes the mass of both the solvent and the dissolved solute: $m_{\text{soln}} = 94.65\text{ g} + 5.35\text{ g} = 100.0\text{ g}$. Moles of $\text{NH}_4\text{Cl} = \frac{5.35}{53.49} = 0.100\text{ mol}$. Thus $q_{\text{rxn}} = (0.100\text{ mol})(+14.8\text{ kJ/mol}) = +1480\text{ J}$, so $q_{\text{soln}} = -q_{\text{rxn}} = -1480\text{ J}$. Then $\Delta T = \frac{-1480\text{ J}}{(100.0\text{ g})(4.00\text{ J/(g}\cdot^\circ\text{C)})} = -3.7^\circ\text{C}$, giving $T_f = 25.0^\circ\text{C} - 3.7^\circ\text{C} = 21.3^\circ\text{C}$. Using only the mass of the water ($94.65\text{ g}$) gives $\Delta T = -3.9^\circ\text{C}$ and $T_f = 21.1^\circ\text{C}$. Final temperatures above $25.0^\circ\text{C}$ result from a sign error: the dissolution is endothermic ($\Delta H_{\text{soln}}^\circ > 0$), so the solution must cool.",
    },
    {
        "unit_q_num": 22,
        "topic_code": "6.4",
        "topic_title": "Heat Capacity and Calorimetry",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"A student determines the enthalpy of an exothermic dissolution reaction ($\Delta H_{\text{soln}}^\circ < 0$) in a coffee-cup calorimeter, assuming the calorimeter cup and thermometer absorb zero heat ($C_{\text{cal}} = 0$). In reality, the calorimeter cup and thermometer have a heat capacity of $C_{\text{cal}} = 35\text{ J/}^\circ\text{C}$. How does neglecting $C_{\text{cal}}$ affect the student's calculated magnitude of $|\Delta H_{\text{soln}}^\circ|$?",
        "options": [
            r"The calculated $|\Delta H_{\text{soln}}^\circ|$ is too high because the calorimeter cup transferred extra heat into the solution.",
            r"The calculated $|\Delta H_{\text{soln}}^\circ|$ is unaffected because $\Delta T$ of the solution is independent of $C_{\text{cal}}$.",
            r"The calculated $\Delta H_{\text{soln}}^\circ$ changes sign from negative to positive.",
            r"The calculated $|\Delta H_{\text{soln}}^\circ|$ is too low because some of the heat released by the dissolution warmed the calorimeter cup rather than just the solution.",
        ],
        "correct_index": 3,
        "explanation": r"The actual heat released by the reaction is $|q_{\text{rxn}}| = m_{\text{soln}}c_{\text{soln}}\Delta T + C_{\text{cal}}\Delta T$. By ignoring the positive $C_{\text{cal}}\Delta T$ term absorbed by the calorimeter hardware, the student underestimates $|q_{\text{rxn}}|$ and therefore calculates a magnitude $|\Delta H_{\text{soln}}^\circ|$ that is artificially low.",
    },

    # -------------------------------------------------------------------------
    # 6.5 Energy of Phase Changes (Q23 - Q28)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 23,
        "topic_code": "6.5",
        "topic_title": "Energy of Phase Changes",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Property of $\text{H}_2\text{O}$</th><th>Value</th></tr></thead><tbody><tr><td>Specific heat of $\text{H}_2\text{O}(s)$</td><td>$2.09\text{ J/(g}\cdot^\circ\text{C)}$</td></tr><tr><td>Specific heat of $\text{H}_2\text{O}(l)$</td><td>$4.18\text{ J/(g}\cdot^\circ\text{C)}$</td></tr><tr><td>Specific heat of $\text{H}_2\text{O}(g)$</td><td>$2.01\text{ J/(g}\cdot^\circ\text{C)}$</td></tr><tr><td>$\Delta H_{\text{fus}}^\circ$ at $0^\circ\text{C}$</td><td>$6.01\text{ kJ/mol}$</td></tr><tr><td>$\Delta H_{\text{vap}}^\circ$ at $100^\circ\text{C}$</td><td>$40.7\text{ kJ/mol}$</td></tr></tbody></table>""",
        "question": r"Using the data in the table above, calculate the total thermal energy required to convert $36.0\text{ g}$ of ice ($\text{H}_2\text{O}(s)$, $M = 18.0\text{ g/mol}$) at $-10.0^\circ\text{C}$ into liquid water at $50.0^\circ\text{C}$ at $1\text{ atm}$.",
        "options": [
            r"$8.28\text{ kJ}$",
            r"$12.8\text{ kJ}$",
            r"$19.5\text{ kJ}$",
            r"$20.3\text{ kJ}$",
        ],
        "correct_index": 3,
        "explanation": r"The process has three steps for $36.0\text{ g}$ ($2.00\text{ mol}$) of $\text{H}_2\text{O}$: (1) Warm ice from $-10.0^\circ\text{C}$ to $0.0^\circ\text{C}$: $q_1 = (36.0\text{ g})(2.09\text{ J/(g}\cdot^\circ\text{C)})(10.0^\circ\text{C}) = 752\text{ J} = 0.752\text{ kJ}$. (2) Melt ice at $0.0^\circ\text{C}$: $q_2 = (2.00\text{ mol})(6.01\text{ kJ/mol}) = 12.02\text{ kJ}$. (3) Warm liquid water from $0.0^\circ\text{C}$ to $50.0^\circ\text{C}$: $q_3 = (36.0\text{ g})(4.18\text{ J/(g}\cdot^\circ\text{C)})(50.0^\circ\text{C}) = 7524\text{ J} = 7.524\text{ kJ}$. Total heat $q_{\text{total}} = 0.752 + 12.02 + 7.524 = 20.3\text{ kJ}$.",
    },
    {
        "unit_q_num": 24,
        "topic_code": "6.5",
        "topic_title": "Energy of Phase Changes",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"When a pure crystalline solid is heated at a constant rate of $150\text{ J/min}$ at $1\text{ atm}$, its heating curve exhibits two horizontal plateaus: a shorter plateau at its normal melting point ($T_m$) and a much longer plateau at its normal boiling point ($T_b$). Which statement best accounts for both the zero slope of the plateaus and their relative lengths?",
        "options": [
            r"During a plateau, added energy increases the average kinetic energy of the molecules; the boiling plateau is longer because gases have a higher specific heat than liquids.",
            r"During a plateau, added energy increases the potential energy of the system by overcoming intermolecular forces at constant temperature; the boiling plateau is longer because vaporization completely separates molecules whereas melting only partially disrupts the crystal lattice.",
            r"During a plateau, heat is lost to the surroundings at the same rate it is added; the boiling plateau is longer because $T_b > T_m$.",
            r"During a plateau, covalent bonds within the molecules are broken; the boiling plateau is longer because more covalent bonds break at $T_b$.",
        ],
        "correct_index": 1,
        "explanation": r"At a phase transition ($T_m$ or $T_b$), all added thermal energy goes into increasing the potential energy of the substance by overcoming intermolecular attractions rather than increasing average kinetic energy ($\Delta T = 0$). Because vaporization ($\Delta H_{\text{vap}}$) requires completely overcoming intermolecular attractions to separate molecules into the gas phase, whereas fusion ($\Delta H_{\text{fus}}$) only partially disrupts the solid lattice, $\Delta H_{\text{vap}} \gg \Delta H_{\text{fus}}$ and the boiling plateau is much longer.",
    },
    {
        "unit_q_num": 25,
        "topic_code": "6.5",
        "topic_title": "Energy of Phase Changes",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Segment of Heating Curve ($0.500\text{ mol}$ of Substance X)</th><th>Temp Range ($^\circ\text{C}$)</th><th>Time Elapsed ($\text{min}$)</th></tr></thead><tbody><tr><td>Solid heating</td><td>$10.0 \rightarrow 40.0$</td><td>$2.0$</td></tr><tr><td>Melting plateau</td><td>$40.0$</td><td>$5.0$</td></tr><tr><td>Liquid heating</td><td>$40.0 \rightarrow 70.0$</td><td>$4.0$</td></tr></tbody></table>""",
        "question": r"A $0.500\text{ mol}$ sample of pure Substance X is heated at a constant power of $600\text{ J/min}$, yielding the heating curve data above. What are the molar enthalpy of fusion ($\Delta H_{\text{fus}}^\circ$) of Substance X and the ratio of the molar heat capacity of the liquid to that of the solid ($C_{p,l} / C_{p,s}$)?",
        "options": [
            r"$\Delta H_{\text{fus}}^\circ = 3.00\text{ kJ/mol}$ and $C_{p,l} / C_{p,s} = 0.50$",
            r"$\Delta H_{\text{fus}}^\circ = 6.00\text{ kJ/mol}$ and $C_{p,l} / C_{p,s} = 0.50$",
            r"$\Delta H_{\text{fus}}^\circ = 6.00\text{ kJ/mol}$ and $C_{p,l} / C_{p,s} = 2.0$",
            r"$\Delta H_{\text{fus}}^\circ = 3.00\text{ kJ/mol}$ and $C_{p,l} / C_{p,s} = 2.0$",
        ],
        "correct_index": 2,
        "explanation": r"During the $5.0\text{ min}$ melting plateau, total heat absorbed is $q_{\text{fus}} = (600\text{ J/min})(5.0\text{ min}) = 3000\text{ J} = 3.00\text{ kJ}$. For $0.500\text{ mol}$, $\Delta H_{\text{fus}}^\circ = \frac{3.00\text{ kJ}}{0.500\text{ mol}} = 6.00\text{ kJ/mol}$. Both the solid and liquid segments span $\Delta T = 30.0^\circ\text{C}$, but the liquid takes twice as long ($4.0\text{ min}$ vs. $2.0\text{ min}$), absorbing twice as much heat for the same $\Delta T$ and moles. Thus $C_{p,l} / C_{p,s} = 2.0$.",
    },
    {
        "unit_q_num": 26,
        "topic_code": "6.5",
        "topic_title": "Energy of Phase Changes",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"For water at $100^\circ\text{C}$ and $1\text{ atm}$, $\Delta H_{\text{vap}}^\circ = +40.7\text{ kJ/mol}$ and $c_{\text{H}_2\text{O}(l)} = 4.184\text{ J/(g}\cdot^\circ\text{C)}$. Why does a skin burn caused by $1.0\text{ g}$ of steam ($\text{H}_2\text{O}(g)$) at $100^\circ\text{C}$ transfer far more thermal energy to skin (at $37^\circ\text{C}$) than a burn caused by $1.0\text{ g}$ of liquid water at $100^\circ\text{C}$?",
        "options": [
            r"Steam molecules at $100^\circ\text{C}$ have a higher average translational kinetic energy than liquid water molecules at $100^\circ\text{C}$.",
            r"Condensing $1.0\text{ g}$ of steam at $100^\circ\text{C}$ to liquid water at $100^\circ\text{C}$ releases an additional $2.26\text{ kJ}$ of heat before the resulting liquid cools from $100^\circ\text{C}$ to $37^\circ\text{C}$.",
            r"Liquid water at $100^\circ\text{C}$ absorbs heat from the skin as it cools to $37^\circ\text{C}$.",
            r"Steam undergoes an exothermic chemical decomposition into $\text{H}_2(g)$ and $\text{O}_2(g)$ upon contact with skin.",
        ],
        "correct_index": 1,
        "explanation": r"Cooling $1.0\text{ g}$ of $\text{H}_2\text{O}(l)$ from $100^\circ\text{C}$ to $37^\circ\text{C}$ releases $q = (1.0\text{ g})(4.184\text{ J/(g}\cdot^\circ\text{C)})(63^\circ\text{C}) = 264\text{ J} = 0.264\text{ kJ}$. By contrast, $1.0\text{ g}$ of steam ($\frac{1.0}{18.02} = 0.0555\text{ mol}$) first condenses at $100^\circ\text{C}$, releasing $(0.0555\text{ mol})(40.7\text{ kJ/mol}) = 2.26\text{ kJ}$, and then releases $0.264\text{ kJ}$ as the condensed liquid cools to $37^\circ\text{C}$—nearly ten times as much heat!",
    },
    {
        "unit_q_num": 27,
        "topic_code": "6.5",
        "topic_title": "Energy of Phase Changes",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"A $18.0\text{ g}$ ice cube ($\text{H}_2\text{O}(s)$, $M = 18.0\text{ g/mol}$, $\Delta H_{\text{fus}}^\circ = 6.01\text{ kJ/mol}$) at $0.0^\circ\text{C}$ is dropped into $100.0\text{ g}$ of liquid water ($c = 4.184\text{ J/(g}\cdot^\circ\text{C)}$) initially at $30.0^\circ\text{C}$ in an insulated coffee-cup calorimeter. What is the final temperature of the system at thermal equilibrium?",
        "options": [
            r"$11.0^\circ\text{C}$",
            r"$13.3^\circ\text{C}$",
            r"$15.6^\circ\text{C}$",
            r"$25.4^\circ\text{C}$",
        ],
        "correct_index": 1,
        "explanation": r"Melting $18.0\text{ g}$ ($1.00\text{ mol}$) of ice at $0.0^\circ\text{C}$ absorbs $q_{\text{melt}} = +6010\text{ J}$. Then warming the $18.0\text{ g}$ of melted ice from $0.0^\circ\text{C}$ to $T_f$ absorbs $(18.0\text{ g})(4.184)(T_f - 0.0)$. Setting $q_{\text{ice}} + q_{\text{warm water}} = 0$ gives $6010 + (18.0)(4.184)T_f + (100.0)(4.184)(T_f - 30.0) = 0 \implies 6010 + 493.7\,T_f - 12552 = 0 \implies 493.7\,T_f = 6542 \implies T_f = 13.3^\circ\text{C}$.",
    },
    {
        "unit_q_num": 28,
        "topic_code": "6.5",
        "topic_title": "Energy of Phase Changes",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Substance</th><th>Molar Mass ($\text{g/mol}$)</th><th>$\Delta H_{\text{vap}}^\circ$ ($\text{kJ/mol}$)</th></tr></thead><tbody><tr><td>$\text{CH}_3\text{CH}_2\text{OCH}_2\text{CH}_3$ (diethyl ether)</td><td>$74.12$</td><td>$26.5$</td></tr><tr><td>$\text{CH}_3\text{CH}_2\text{CH}_2\text{CH}_2\text{OH}$ ($1$-butanol)</td><td>$74.12$</td><td>$52.4$</td></tr></tbody></table>""",
        "question": r"For a given substance at constant temperature and pressure, $\Delta H_{\text{sub}}^\circ = \Delta H_{\text{fus}}^\circ + \Delta H_{\text{vap}}^\circ$ and $\Delta H_{\text{cond}}^\circ = -\Delta H_{\text{vap}}^\circ$. Based on the data in the table above for two constitutional isomers of $\text{C}_4\text{H}_{10}\text{O}$, which statement is correct?",
        "options": [
            r"Condensing $1.00\text{ mol}$ of $1$-butanol gas releases $52.4\text{ kJ}$ of heat because $1$-butanol forms stronger intermolecular hydrogen bonds than diethyl ether.",
            r"Condensing $1.00\text{ mol}$ of $1$-butanol gas absorbs $52.4\text{ kJ}$ of heat because breaking hydrogen bonds is endothermic.",
            r"Diethyl ether has a smaller $\Delta H_{\text{vap}}^\circ$ because its $\text{C}-\text{O}$ covalent bonds are weaker than the $\text{C}-\text{O}$ bond in $1$-butanol.",
            r"For $1$-butanol, $\Delta H_{\text{fus}}^\circ$ must be greater than $52.4\text{ kJ/mol}$.",
        ],
        "correct_index": 0,
        "explanation": r"Condensation is the reverse of vaporization, so $\Delta H_{\text{cond}}^\circ = -\Delta H_{\text{vap}}^\circ = -52.4\text{ kJ/mol}$ for $1$-butanol (releasing $52.4\text{ kJ/mol}$). $1$-butanol has a much larger $\Delta H_{\text{vap}}^\circ$ than its isomer diethyl ether because $1$-butanol has an $-\text{OH}$ group capable of intermolecular hydrogen bonding, whereas diethyl ether only exhibits dipole-dipole and London dispersion forces.",
    },

    # -------------------------------------------------------------------------
    # 6.6 Introduction to Enthalpy of Reaction (Q29 - Q33)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 29,
        "topic_code": "6.6",
        "topic_title": "Introduction to Enthalpy of Reaction",
        "difficulty": "AP Exam Level",
        "stimulus": r"$$2\,\text{CH}_3\text{OH}(l) + 3\,\text{O}_2(g) \rightarrow 2\,\text{CO}_2(g) + 4\,\text{H}_2\text{O}(l) \quad \Delta H^\circ = -1452\text{ kJ/mol}_{\text{rxn}}$$",
        "question": r"Based on the thermochemical equation above for the combustion of liquid methanol ($\text{CH}_3\text{OH}$, $M = 32.04\text{ g/mol}$), how much heat is released when $16.02\text{ g}$ of $\text{CH}_3\text{OH}(l)$ is completely burned in excess $\text{O}_2(g)$ at constant pressure?",
        "options": [
            r"$181.5\text{ kJ}$",
            r"$363.0\text{ kJ}$",
            r"$726.0\text{ kJ}$",
            r"$1452\text{ kJ}$",
        ],
        "correct_index": 1,
        "explanation": r"First calculate moles of methanol: $n_{\text{CH}_3\text{OH}} = \frac{16.02\text{ g}}{32.04\text{ g/mol}} = 0.5000\text{ mol}$. According to the balanced equation, $1452\text{ kJ}$ of heat is released per $2\text{ mol}$ of $\text{CH}_3\text{OH}(l)$ reacted. Thus, heat released $= (0.5000\text{ mol }\text{CH}_3\text{OH}) \times \frac{1452\text{ kJ}}{2\text{ mol }\text{CH}_3\text{OH}} = 363.0\text{ kJ}$.",
    },
    {
        "unit_q_num": 30,
        "topic_code": "6.6",
        "topic_title": "Introduction to Enthalpy of Reaction",
        "difficulty": "AP Exam Level",
        "stimulus": r"$$\text{N}_2(g) + 3\,\text{H}_2(g) \rightarrow 2\,\text{NH}_3(g) \quad \Delta H^\circ = -92.2\text{ kJ/mol}_{\text{rxn}}$$",
        "question": r"Given the thermochemical equation above, what is the value of $\Delta H^\circ$ for the reaction $\text{NH}_3(g) \rightarrow \frac{1}{2}\,\text{N}_2(g) + \frac{3}{2}\,\text{H}_2(g)$?",
        "options": [
            r"$-184.4\text{ kJ/mol}_{\text{rxn}}$",
            r"$-46.1\text{ kJ/mol}_{\text{rxn}}$",
            r"$+46.1\text{ kJ/mol}_{\text{rxn}}$",
            r"$+92.2\text{ kJ/mol}_{\text{rxn}}$",
        ],
        "correct_index": 2,
        "explanation": r"The target equation is obtained by reversing the given reaction (which changes the sign of $\Delta H^\circ$ from $-92.2$ to $+92.2\text{ kJ/mol}_{\text{rxn}}$) and multiplying all coefficients by $\frac{1}{2}$: $\Delta H^\circ = \frac{1}{2}(+92.2\text{ kJ/mol}_{\text{rxn}}) = +46.1\text{ kJ/mol}_{\text{rxn}}$.",
    },
    {
        "unit_q_num": 31,
        "topic_code": "6.6",
        "topic_title": "Introduction to Enthalpy of Reaction",
        "difficulty": "Challenging",
        "stimulus": r"$$2\,\text{Al}(s) + \text{Fe}_2\text{O}_3(s) \rightarrow \text{Al}_2\text{O}_3(s) + 2\,\text{Fe}(s) \quad \Delta H^\circ = -852\text{ kJ/mol}_{\text{rxn}}$$",
        "question": r"In a thermite reaction, $13.5\text{ g}$ of $\text{Al}(s)$ ($M = 26.98\text{ g/mol}$) is mixed with $31.9\text{ g}$ of $\text{Fe}_2\text{O}_3(s)$ ($M = 159.7\text{ g/mol}$) and ignited. Assuming the reaction goes to completion, what is $q_{\text{rxn}}$ for the reaction mixture?",
        "options": [
            r"$-170\text{ kJ}$",
            r"$-213\text{ kJ}$",
            r"$-426\text{ kJ}$",
            r"$-852\text{ kJ}$",
        ],
        "correct_index": 0,
        "explanation": r"Find the moles of each reactant: $n_{\text{Al}} = \frac{13.5\text{ g}}{26.98\text{ g/mol}} = 0.500\text{ mol}$ (which corresponds to $\frac{0.500}{2} = 0.250\text{ mol}_{\text{rxn}}$), and $n_{\text{Fe}_2\text{O}_3} = \frac{31.9\text{ g}}{159.7\text{ g/mol}} = 0.200\text{ mol}$ (which corresponds to $\frac{0.200}{1} = 0.200\text{ mol}_{\text{rxn}}$). Therefore, $\text{Fe}_2\text{O}_3$ is the limiting reactant ($0.200\text{ mol}_{\text{rxn}}$), and $q_{\text{rxn}} = (0.200\text{ mol}_{\text{rxn}})(-852\text{ kJ/mol}_{\text{rxn}}) = -170\text{ kJ}$. Treating $\text{Al}$ as limiting gives $-213\text{ kJ}$, and using $0.500\text{ mol}$ of $\text{Al}$ without dividing by its coefficient of $2$ gives $-426\text{ kJ}$.",
    },
    {
        "unit_q_num": 32,
        "topic_code": "6.6",
        "topic_title": "Introduction to Enthalpy of Reaction",
        "difficulty": "AP Exam Level",
        "stimulus": r"$$2\,\text{H}_2\text{O}_2(l) \rightarrow 2\,\text{H}_2\text{O}(l) + \text{O}_2(g) \quad \Delta H^\circ = -196\text{ kJ/mol}_{\text{rxn}}$$",
        "question": r"During the catalytic decomposition of liquid hydrogen peroxide shown above, $49.0\text{ kJ}$ of thermal energy is released at $298\text{ K}$ and $1.00\text{ atm}$. What volume of $\text{O}_2(g)$ ($R = 0.08206\text{ L}\cdot\text{atm/(mol}\cdot\text{K)}$) is produced?",
        "options": [
            r"$3.06\text{ L}$",
            r"$6.11\text{ L}$",
            r"$12.2\text{ L}$",
            r"$24.5\text{ L}$",
        ],
        "correct_index": 1,
        "explanation": r"According to the thermochemical equation, $196\text{ kJ}$ of heat is released per $1\text{ mol}$ of $\text{O}_2(g)$ formed. When $49.0\text{ kJ}$ is released, $n_{\text{O}_2} = \frac{49.0\text{ kJ}}{196\text{ kJ/mol }\text{O}_2} = 0.250\text{ mol }\text{O}_2$. Using the ideal gas law, $V = \frac{nRT}{P} = \frac{(0.250\text{ mol})(0.08206\text{ L}\cdot\text{atm/(mol}\cdot\text{K)})(298\text{ K})}{1.00\text{ atm}} = 6.11\text{ L}$.",
    },
    {
        "unit_q_num": 33,
        "topic_code": "6.6",
        "topic_title": "Introduction to Enthalpy of Reaction",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Reaction</th><th>$\Delta H^\circ$ at $298\text{ K}$</th></tr></thead><tbody><tr><td>$\text{CH}_4(g) + 2\,\text{O}_2(g) \rightarrow \text{CO}_2(g) + 2\,\text{H}_2\text{O}(g)$</td><td>$-802\text{ kJ/mol}_{\text{rxn}}$</td></tr><tr><td>$\text{CH}_4(g) + 2\,\text{O}_2(g) \rightarrow \text{CO}_2(g) + 2\,\text{H}_2\text{O}(l)$</td><td>$-890\text{ kJ/mol}_{\text{rxn}}$</td></tr></tbody></table>""",
        "question": r"Why does the combustion of $1.00\text{ mol}$ of $\text{CH}_4(g)$ release $88\text{ kJ}$ more thermal energy when $\text{H}_2\text{O}(l)$ is formed than when $\text{H}_2\text{O}(g)$ is formed?",
        "options": [
            r"Because $\text{H}_2\text{O}(l)$ has a higher potential energy than $\text{H}_2\text{O}(g)$ at $298\text{ K}$.",
            r"Because breaking the $\text{O}-\text{H}$ covalent bonds in $\text{H}_2\text{O}(g)$ releases $44\text{ kJ/mol}$.",
            r"Because $\text{CO}_2(g)$ reacts exothermically with $\text{H}_2\text{O}(l)$ to release $88\text{ kJ}$.",
            r"Because the condensation of $2.00\text{ mol}$ of $\text{H}_2\text{O}(g)$ to $\text{H}_2\text{O}(l)$ is exothermic, releasing $2 \times 44\text{ kJ} = 88\text{ kJ}$ of additional heat.",
        ],
        "correct_index": 3,
        "explanation": r"Subtracting the first equation from the second gives $2\,\text{H}_2\text{O}(g) \rightarrow 2\,\text{H}_2\text{O}(l)$ with $\Delta H^\circ = -890 - (-802) = -88\text{ kJ/mol}_{\text{rxn}}$. Condensing $2\text{ mol}$ of water vapor into liquid water forms intermolecular hydrogen bonds and releases $88\text{ kJ}$ ($44\text{ kJ/mol }\text{H}_2\text{O}$) of additional heat.",
    },

    # -------------------------------------------------------------------------
    # 6.7 Bond Enthalpies (Q34 - Q39)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 34,
        "topic_code": "6.7",
        "topic_title": "Bond Enthalpies",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Bond</th><th>Average Bond Enthalpy ($\text{kJ/mol}$)</th></tr></thead><tbody><tr><td>$\text{H}-\text{H}$</td><td>$436$</td></tr><tr><td>$\text{Cl}-\text{Cl}$</td><td>$243$</td></tr><tr><td>$\text{H}-\text{Cl}$</td><td>$432$</td></tr></tbody></table>""",
        "question": r"Using the average bond enthalpies in the table above, calculate $\Delta H_{\text{rxn}}^\circ$ for the synthesis of hydrogen chloride gas: $\text{H}_2(g) + \text{Cl}_2(g) \rightarrow 2\,\text{HCl}(g)$.",
        "options": [
            r"$-247\text{ kJ/mol}_{\text{rxn}}$",
            r"$-185\text{ kJ/mol}_{\text{rxn}}$",
            r"$+185\text{ kJ/mol}_{\text{rxn}}$",
            r"$+247\text{ kJ/mol}_{\text{rxn}}$",
        ],
        "correct_index": 1,
        "explanation": r"Using $\Delta H_{\text{rxn}}^\circ = \sum \Delta H_{\text{bonds broken}} - \sum \Delta H_{\text{bonds formed}}$: Bonds broken $= 1(\text{H}-\text{H}) + 1(\text{Cl}-\text{Cl}) = 436 + 243 = 679\text{ kJ}$. Bonds formed $= 2(\text{H}-\text{Cl}) = 2(432) = 864\text{ kJ}$. Thus $\Delta H_{\text{rxn}}^\circ = 679 - 864 = -185\text{ kJ/mol}_{\text{rxn}}$.",
    },
    {
        "unit_q_num": 35,
        "topic_code": "6.7",
        "topic_title": "Bond Enthalpies",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Bond</th><th>Average Bond Enthalpy ($\text{kJ/mol}$)</th></tr></thead><tbody><tr><td>$\text{C}=\text{C}$</td><td>$614$</td></tr><tr><td>$\text{C}-\text{C}$</td><td>$348$</td></tr><tr><td>$\text{C}-\text{H}$</td><td>$413$</td></tr><tr><td>$\text{H}-\text{Br}$</td><td>$366$</td></tr><tr><td>$\text{C}-\text{Br}$</td><td>$276$</td></tr></tbody></table>""",
        "question": r"Based on the bond enthalpies in the table above, estimate $\Delta H_{\text{rxn}}^\circ$ for the gas-phase hydrobromination of ethene: $\text{H}_2\text{C}=\text{CH}_2(g) + \text{HBr}(g) \rightarrow \text{CH}_3\text{CH}_2\text{Br}(g)$.",
        "options": [
            r"$-57\text{ kJ/mol}_{\text{rxn}}$",
            r"$+57\text{ kJ/mol}_{\text{rxn}}$",
            r"$-147\text{ kJ/mol}_{\text{rxn}}$",
            r"$+147\text{ kJ/mol}_{\text{rxn}}$",
        ],
        "correct_index": 0,
        "explanation": r"Notice that the four $\text{C}-\text{H}$ bonds in $\text{H}_2\text{C}=\text{CH}_2$ remain intact in $\text{CH}_3\text{CH}_2\text{Br}$. Net bonds broken $= 1(\text{C}=\text{C}) + 1(\text{H}-\text{Br}) = 614 + 366 = 980\text{ kJ}$. Net bonds formed $= 1(\text{C}-\text{C}) + 1(\text{C}-\text{H}) + 1(\text{C}-\text{Br}) = 348 + 413 + 276 = 1037\text{ kJ}$. Therefore, $\Delta H_{\text{rxn}}^\circ = 980 - 1037 = -57\text{ kJ/mol}_{\text{rxn}}$.",
    },
    {
        "unit_q_num": 36,
        "topic_code": "6.7",
        "topic_title": "Bond Enthalpies",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Bond</th><th>Average Bond Enthalpy ($\text{kJ/mol}$)</th></tr></thead><tbody><tr><td>$\text{N}\equiv\text{N}$</td><td>$945$</td></tr><tr><td>$\text{H}-\text{H}$</td><td>$436$</td></tr><tr><td>$\text{N}-\text{N}$</td><td>$160$</td></tr></tbody></table>""",
        "question": r"The reaction of nitrogen and hydrogen gases to form gaseous hydrazine ($\text{H}_2\text{N}-\text{NH}_2$) has an enthalpy change of: $$\text{N}_2(g) + 2\,\text{H}_2(g) \rightarrow \text{N}_2\text{H}_4(g) \quad \Delta H_{\text{rxn}}^\circ = +93\text{ kJ/mol}_{\text{rxn}}$$ Using the bond enthalpies in the table above, what is the average $\text{N}-\text{H}$ bond enthalpy in $\text{N}_2\text{H}_4(g)$?",
        "options": [
            r"$782\text{ kJ/mol}$",
            r"$431\text{ kJ/mol}$",
            r"$391\text{ kJ/mol}$",
            r"$282\text{ kJ/mol}$",
        ],
        "correct_index": 2,
        "explanation": r"In $\text{N}_2\text{H}_4(g)$, there is $1$ $\text{N}-\text{N}$ single bond and $4$ $\text{N}-\text{H}$ single bonds. Using $\Delta H_{\text{rxn}}^\circ = \sum \Delta H_{\text{broken}} - \sum \Delta H_{\text{formed}}$: $+93 = [945 + 2(436)] - [160 + 4\,D(\text{N}-\text{H})] \implies +93 = 1817 - 160 - 4\,D(\text{N}-\text{H}) \implies 4\,D(\text{N}-\text{H}) = 1657 - 93 = 1564 \implies D(\text{N}-\text{H}) = 391\text{ kJ/mol}$. Omitting the $\text{N}-\text{N}$ bond formed gives $431\text{ kJ/mol}$, breaking only one $\text{H}-\text{H}$ bond gives $282\text{ kJ/mol}$, and assuming hydrazine has only two $\text{N}-\text{H}$ bonds gives $782\text{ kJ/mol}$.",
    },
    {
        "unit_q_num": 37,
        "topic_code": "6.7",
        "topic_title": "Bond Enthalpies",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Bond</th><th>Average Bond Enthalpy ($\text{kJ/mol}$)</th></tr></thead><tbody><tr><td>$\text{C}-\text{H}$</td><td>$413$</td></tr><tr><td>$\text{O}=\text{O}$</td><td>$498$</td></tr><tr><td>$\text{C}=\text{O}$ (in $\text{CO}_2$)</td><td>$799$</td></tr><tr><td>$\text{O}-\text{H}$</td><td>$463$</td></tr></tbody></table>""",
        "question": r"Using the average bond enthalpies in the table above, estimate $\Delta H_{\text{rxn}}^\circ$ for the complete combustion of methane to form gaseous water: $$\text{CH}_4(g) + 2\,\text{O}_2(g) \rightarrow \text{CO}_2(g) + 2\,\text{H}_2\text{O}(g)$$",
        "options": [
            r"$-802\text{ kJ/mol}_{\text{rxn}}$",
            r"$+802\text{ kJ/mol}_{\text{rxn}}$",
            r"$-39\text{ kJ/mol}_{\text{rxn}}$",
            r"$-1604\text{ kJ/mol}_{\text{rxn}}$",
        ],
        "correct_index": 0,
        "explanation": r"Bonds broken in reactants: $4(\text{C}-\text{H}) + 2(\text{O}=\text{O}) = 4(413) + 2(498) = 1652 + 996 = 2648\text{ kJ}$. Bonds formed in products ($\text{O}=\text{C}=\text{O}$ has $2$ $\text{C}=\text{O}$ bonds, and $2\,\text{H}_2\text{O}$ has $4$ $\text{O}-\text{H}$ bonds): $2(799) + 4(463) = 1598 + 1852 = 3450\text{ kJ}$. Therefore, $\Delta H_{\text{rxn}}^\circ = 2648 - 3450 = -802\text{ kJ/mol}_{\text{rxn}}$.",
    },
    {
        "unit_q_num": 38,
        "topic_code": "6.7",
        "topic_title": "Bond Enthalpies",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"Why does calculating $\Delta H_{\text{rxn}}^\circ$ from tabulated average bond enthalpies often give a slightly different value than calculating $\Delta H_{\text{rxn}}^\circ$ from standard enthalpies of formation ($\Delta H_f^\circ$)?",
        "options": [
            r"Standard enthalpies of formation ignore the energy required to break covalent bonds in the reactants.",
            r"Bond enthalpies are measured at $0\text{ K}$, whereas standard enthalpies of formation are measured at $298\text{ K}$.",
            r"Hess's law applies only to standard enthalpies of formation and not to bond dissociation enthalpies.",
            r"Tabulated bond enthalpies are averages across many different gas-phase molecules and do not account for intermolecular forces in liquids or solids, whereas $\Delta H_f^\circ$ values are experimentally measured for specific compounds in their exact standard states.",
        ],
        "correct_index": 3,
        "explanation": r"Average bond enthalpies are averaged over many different gaseous compounds (where the exact bond strength varies slightly with molecular environment) and apply strictly to gas-phase species. Standard enthalpies of formation ($\Delta H_f^\circ$) are exact experimental values for specific compounds in their actual standard states (solid, liquid, or gas) at $1\text{ atm}$ and $298\text{ K}$.",
    },
    {
        "unit_q_num": 39,
        "topic_code": "6.7",
        "topic_title": "Bond Enthalpies",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Carbon-Oxygen Bond Type</th><th>Bond Order</th><th>Bond Length ($\text{pm}$)</th><th>Bond Enthalpy ($\text{kJ/mol}$)</th></tr></thead><tbody><tr><td>$\text{C}-\text{O}$ (in $\text{CH}_3\text{OH}$)</td><td>$1$</td><td>$143$</td><td>$358$</td></tr><tr><td>$\text{C}=\text{O}$ (in $\text{H}_2\text{CO}$)</td><td>$2$</td><td>$121$</td><td>$745$</td></tr><tr><td>$\text{C}\equiv\text{O}$ (in $\text{CO}$)</td><td>$3$</td><td>$113$</td><td>$1072$</td></tr></tbody></table>""",
        "question": r"Based on the data in the table above and Coulombic principles of chemical bonding, which statement correctly explains the relationship among bond order, bond length, and bond enthalpy for carbon-oxygen bonds?",
        "options": [
            r"As bond order increases, higher electron density between the nuclei increases attraction, decreasing bond length and increasing the energy required to break the bond.",
            r"As bond order increases, greater electron-electron repulsion pushes the nuclei farther apart, increasing both bond length and bond enthalpy.",
            r"Forming a $\text{C}\equiv\text{O}$ triple bond from gaseous $\text{C}$ and $\text{O}$ atoms is an endothermic process with $\Delta H = +1072\text{ kJ/mol}$.",
            r"The $\text{C}-\text{O}$ single bond is the most thermodynamically stable because it has the lowest bond enthalpy.",
        ],
        "correct_index": 0,
        "explanation": r"Higher bond order places greater shared electron density between the two positively charged nuclei, increasing Coulombic attraction. This pulls the nuclei closer together (shorter bond length) and deepens the potential energy well, requiring more energy input (higher bond enthalpy) to cleave the bond.",
    },

    # -------------------------------------------------------------------------
    # 6.8 Enthalpy of Formation (Q40 - Q44)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 40,
        "topic_code": "6.8",
        "topic_title": "Enthalpy of Formation",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"For which of the following thermochemical equations at $298\text{ K}$ and $1\text{ atm}$ is the enthalpy of reaction ($\Delta H_{\text{rxn}}^\circ$) equal to the standard enthalpy of formation ($\Delta H_f^\circ$) of the product?",
        "options": [
            r"$2\,\text{C}(s,\text{graphite}) + 3\,\text{H}_2(g) \rightarrow \text{C}_2\text{H}_6(g)$",
            r"$\text{C}(s,\text{diamond}) + \text{O}_2(g) \rightarrow \text{CO}_2(g)$",
            r"$\text{N}_2(g) + 3\,\text{H}_2(g) \rightarrow 2\,\text{NH}_3(g)$",
            r"$\text{CaO}(s) + \text{CO}_2(g) \rightarrow \text{CaCO}_3(s)$",
        ],
        "correct_index": 0,
        "explanation": r"By definition, $\Delta H_f^\circ$ is the enthalpy change for forming exactly $1\text{ mol}$ of a substance from its constituent elements in their most stable standard states at $298\text{ K}$ and $1\text{ atm}$. The ethane equation forms $1\text{ mol}$ of $\text{C}_2\text{H}_6(g)$ from $\text{C}(s,\text{graphite})$ and $\text{H}_2(g)$, so it qualifies. The $\text{CO}_2$ equation starts from diamond, which is not the standard state of carbon; the ammonia equation forms $2\text{ mol}$ of product, so its $\Delta H^\circ$ equals $2\Delta H_f^\circ$; and the $\text{CaCO}_3$ equation starts from compounds ($\text{CaO}$ and $\text{CO}_2$) rather than from elements.",
    },
    {
        "unit_q_num": 41,
        "topic_code": "6.8",
        "topic_title": "Enthalpy of Formation",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"Which of the following substances has a non-zero standard enthalpy of formation ($\Delta H_f^\circ \neq 0$) at $298\text{ K}$ and $1\text{ atm}$?",
        "options": [
            r"$\text{Br}_2(l)$",
            r"$\text{Hg}(l)$",
            r"$\text{I}_2(g)$",
            r"$\text{O}_2(g)$",
        ],
        "correct_index": 2,
        "explanation": r"At $298\text{ K}$ and $1\text{ atm}$, the standard state of iodine is the crystalline solid $\text{I}_2(s)$ ($\Delta H_f^\circ = 0$). Forming $\text{I}_2(g)$ from $\text{I}_2(s)$ requires the enthalpy of sublimation ($\Delta H_f^\circ[\text{I}_2(g)] = +62.4\text{ kJ/mol} \neq 0$). By contrast, $\text{Br}_2(l)$, $\text{Hg}(l)$, and $\text{O}_2(g)$ are all elements in their most stable standard states at $298\text{ K}$.",
    },
    {
        "unit_q_num": 42,
        "topic_code": "6.8",
        "topic_title": "Enthalpy of Formation",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Substance</th><th>$\Delta H_f^\circ$ ($\text{kJ/mol}$)</th></tr></thead><tbody><tr><td>$\text{NH}_3(g)$</td><td>$-46.1$</td></tr><tr><td>$\text{NO}(g)$</td><td>$+90.3$</td></tr><tr><td>$\text{H}_2\text{O}(g)$</td><td>$-241.8$</td></tr></tbody></table>""",
        "question": r"The Ostwald process begins with the catalytic oxidation of ammonia: $$4\,\text{NH}_3(g) + 5\,\text{O}_2(g) \rightarrow 4\,\text{NO}(g) + 6\,\text{H}_2\text{O}(g)$$ Using the standard enthalpies of formation in the table above, what is $\Delta H_{\text{rxn}}^\circ$ for this reaction?",
        "options": [
            r"$-1274.0\text{ kJ/mol}_{\text{rxn}}$",
            r"$-1089.6\text{ kJ/mol}_{\text{rxn}}$",
            r"$-905.2\text{ kJ/mol}_{\text{rxn}}$",
            r"$+905.2\text{ kJ/mol}_{\text{rxn}}$",
        ],
        "correct_index": 2,
        "explanation": r"Using $\Delta H_{\text{rxn}}^\circ = \sum n_p \Delta H_f^\circ(\text{products}) - \sum n_r \Delta H_f^\circ(\text{reactants})$ and noting $\Delta H_f^\circ[\text{O}_2(g)] = 0$: $\sum n_p \Delta H_f^\circ(\text{products}) = 4(+90.3) + 6(-241.8) = +361.2 - 1450.8 = -1089.6\text{ kJ}$. $\sum n_r \Delta H_f^\circ(\text{reactants}) = 4(-46.1) + 5(0) = -184.4\text{ kJ}$. Thus $\Delta H_{\text{rxn}}^\circ = (-1089.6) - (-184.4) = -905.2\text{ kJ/mol}_{\text{rxn}}$.",
    },
    {
        "unit_q_num": 43,
        "topic_code": "6.8",
        "topic_title": "Enthalpy of Formation",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Substance</th><th>$\Delta H_f^\circ$ ($\text{kJ/mol}$)</th></tr></thead><tbody><tr><td>$\text{CO}_2(g)$</td><td>$-393.5$</td></tr><tr><td>$\text{H}_2\text{O}(l)$</td><td>$-285.8$</td></tr></tbody></table>""",
        "question": r"The standard enthalpy of combustion of liquid ethanol ($\text{C}_2\text{H}_5\text{OH}(l)$) is given by: $$\text{C}_2\text{H}_5\text{OH}(l) + 3\,\text{O}_2(g) \rightarrow 2\,\text{CO}_2(g) + 3\,\text{H}_2\text{O}(l) \quad \Delta H_{\text{rxn}}^\circ = -1366.8\text{ kJ/mol}_{\text{rxn}}$$ Using the data in the table above, what is the standard enthalpy of formation ($\Delta H_f^\circ$) of $\text{C}_2\text{H}_5\text{OH}(l)$?",
        "options": [
            r"$+277.6\text{ kJ/mol}$",
            r"$-3011.2\text{ kJ/mol}$",
            r"$-687.5\text{ kJ/mol}$",
            r"$-277.6\text{ kJ/mol}$",
        ],
        "correct_index": 3,
        "explanation": r"We have $\Delta H_{\text{rxn}}^\circ = [2\,\Delta H_f^\circ(\text{CO}_2(g)) + 3\,\Delta H_f^\circ(\text{H}_2\text{O}(l))] - [\Delta H_f^\circ(\text{C}_2\text{H}_5\text{OH}(l)) + 3(0)]$. Substituting the values: $-1366.8 = [2(-393.5) + 3(-285.8)] - \Delta H_f^\circ(\text{C}_2\text{H}_5\text{OH}(l)) = (-787.0 - 857.4) - \Delta H_f^\circ(\text{C}_2\text{H}_5\text{OH}(l)) = -1644.4 - \Delta H_f^\circ(\text{C}_2\text{H}_5\text{OH}(l))$. Solving gives $\Delta H_f^\circ(\text{C}_2\text{H}_5\text{OH}(l)) = -1644.4 + 1366.8 = -277.6\text{ kJ/mol}$.",
    },
    {
        "unit_q_num": 44,
        "topic_code": "6.8",
        "topic_title": "Enthalpy of Formation",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Species</th><th>$\Delta H_f^\circ$ ($\text{kJ/mol}$)</th></tr></thead><tbody><tr><td>$\text{CaCO}_3(s)$</td><td>$-1207.6$</td></tr><tr><td>$\text{Ca}^{2+}(aq)$</td><td>$-542.8$</td></tr><tr><td>$\text{CO}_2(g)$</td><td>$-393.5$</td></tr><tr><td>$\text{H}_2\text{O}(l)$</td><td>$-285.8$</td></tr></tbody></table>""",
        "question": r"Consider the net ionic equation for the reaction of solid calcium carbonate with strong acid: $$\text{CaCO}_3(s) + 2\,\text{H}^+(aq) \rightarrow \text{Ca}^{2+}(aq) + \text{CO}_2(g) + \text{H}_2\text{O}(l)$$ Given that by convention $\Delta H_f^\circ[\text{H}^+(aq)] = 0\text{ kJ/mol}$, what is $\Delta H_{\text{rxn}}^\circ$ for this reaction?",
        "options": [
            r"$+14.5\text{ kJ/mol}_{\text{rxn}}$",
            r"$-2429.7\text{ kJ/mol}_{\text{rxn}}$",
            r"$+271.3\text{ kJ/mol}_{\text{rxn}}$",
            r"$-14.5\text{ kJ/mol}_{\text{rxn}}$",
        ],
        "correct_index": 3,
        "explanation": r"Using $\Delta H_{\text{rxn}}^\circ = \sum n_p \Delta H_f^\circ(\text{products}) - \sum n_r \Delta H_f^\circ(\text{reactants})$: $\sum n_p \Delta H_f^\circ(\text{products}) = (-542.8) + (-393.5) + (-285.8) = -1222.1\text{ kJ}$. $\sum n_r \Delta H_f^\circ(\text{reactants}) = (-1207.6) + 2(0) = -1207.6\text{ kJ}$. Thus $\Delta H_{\text{rxn}}^\circ = -1222.1 - (-1207.6) = -14.5\text{ kJ/mol}_{\text{rxn}}$.",
    },

    # -------------------------------------------------------------------------
    # 6.9 Hess's Law (Q45 - Q50)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 45,
        "topic_code": "6.9",
        "topic_title": "Hess's Law",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Reaction</th><th>$\Delta H^\circ$ ($\text{kJ/mol}_{\text{rxn}}$)</th></tr></thead><tbody><tr><td>$\text{C}(s,\text{graphite}) + \text{O}_2(g) \rightarrow \text{CO}_2(g)$</td><td>$-393.5$</td></tr><tr><td>$\text{CO}(g) + \frac{1}{2}\,\text{O}_2(g) \rightarrow \text{CO}_2(g)$</td><td>$-283.0$</td></tr></tbody></table>""",
        "question": r"Using the thermochemical equations in the table above, calculate $\Delta H^\circ$ for the incomplete combustion of graphite to carbon monoxide: $$\text{C}(s,\text{graphite}) + \frac{1}{2}\,\text{O}_2(g) \rightarrow \text{CO}(g)$$",
        "options": [
            r"$-676.5\text{ kJ/mol}_{\text{rxn}}$",
            r"$-110.5\text{ kJ/mol}_{\text{rxn}}$",
            r"$+110.5\text{ kJ/mol}_{\text{rxn}}$",
            r"$+676.5\text{ kJ/mol}_{\text{rxn}}$",
        ],
        "correct_index": 1,
        "explanation": r"Keep Reaction 1 as written ($\Delta H_1^\circ = -393.5\text{ kJ/mol}_{\text{rxn}}$) and reverse Reaction 2 ($\text{CO}_2(g) \rightarrow \text{CO}(g) + \frac{1}{2}\,\text{O}_2(g)$, $\Delta H_2^\circ = +283.0\text{ kJ/mol}_{\text{rxn}}$). Adding the two equations cancels $\text{CO}_2(g)$ and $\frac{1}{2}\,\text{O}_2(g)$ to yield $\text{C}(s,\text{graphite}) + \frac{1}{2}\,\text{O}_2(g) \rightarrow \text{CO}(g)$ with $\Delta H^\circ = -393.5 + 283.0 = -110.5\text{ kJ/mol}_{\text{rxn}}$.",
    },
    {
        "unit_q_num": 46,
        "topic_code": "6.9",
        "topic_title": "Hess's Law",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Step</th><th>Reaction</th><th>$\Delta H^\circ$ ($\text{kJ/mol}_{\text{rxn}}$)</th></tr></thead><tbody><tr><td>1</td><td>$2\,\text{NO}(g) \rightarrow \text{N}_2(g) + \text{O}_2(g)$</td><td>$-180.6$</td></tr><tr><td>2</td><td>$2\,\text{NO}(g) + \text{O}_2(g) \rightarrow 2\,\text{NO}_2(g)$</td><td>$-114.2$</td></tr></tbody></table>""",
        "question": r"Based on the reactions above, what is $\Delta H^\circ$ for the formation of $1\text{ mol}$ of $\text{NO}_2(g)$ from its elements: $$\frac{1}{2}\,\text{N}_2(g) + \text{O}_2(g) \rightarrow \text{NO}_2(g)$$",
        "options": [
            r"$-147.4\text{ kJ/mol}_{\text{rxn}}$",
            r"$-33.2\text{ kJ/mol}_{\text{rxn}}$",
            r"$+33.2\text{ kJ/mol}_{\text{rxn}}$",
            r"$+66.4\text{ kJ/mol}_{\text{rxn}}$",
        ],
        "correct_index": 2,
        "explanation": r"Reverse Reaction 1 and multiply by $\frac{1}{2}$: $\frac{1}{2}\,\text{N}_2(g) + \frac{1}{2}\,\text{O}_2(g) \rightarrow \text{NO}(g)$ with $\Delta H^\circ = \frac{1}{2}(+180.6) = +90.3\text{ kJ/mol}_{\text{rxn}}$. Multiply Reaction 2 by $\frac{1}{2}$: $\text{NO}(g) + \frac{1}{2}\,\text{O}_2(g) \rightarrow \text{NO}_2(g)$ with $\Delta H^\circ = \frac{1}{2}(-114.2) = -57.1\text{ kJ/mol}_{\text{rxn}}$. Summing the two gives $\frac{1}{2}\,\text{N}_2(g) + \text{O}_2(g) \rightarrow \text{NO}_2(g)$ with $\Delta H^\circ = +90.3 + (-57.1) = +33.2\text{ kJ/mol}_{\text{rxn}}$.",
    },
    {
        "unit_q_num": 47,
        "topic_code": "6.9",
        "topic_title": "Hess's Law",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Equation</th><th>Reaction</th><th>$\Delta H^\circ$ ($\text{kJ/mol}_{\text{rxn}}$)</th></tr></thead><tbody><tr><td>1</td><td>$2\,\text{B}(s) + \frac{3}{2}\,\text{O}_2(g) \rightarrow \text{B}_2\text{O}_3(s)$</td><td>$-1273$</td></tr><tr><td>2</td><td>$\text{B}_2\text{H}_6(g) + 3\,\text{O}_2(g) \rightarrow \text{B}_2\text{O}_3(s) + 3\,\text{H}_2\text{O}(l)$</td><td>$-2166$</td></tr><tr><td>3</td><td>$\text{H}_2(g) + \frac{1}{2}\,\text{O}_2(g) \rightarrow \text{H}_2\text{O}(l)$</td><td>$-286$</td></tr><tr><td>4</td><td>$\text{H}_2\text{O}(l) \rightarrow \text{H}_2\text{O}(g)$</td><td>$+44$</td></tr></tbody></table>""",
        "question": r"Using the four thermochemical equations in the table above, calculate $\Delta H^\circ$ for the synthesis of gaseous diborane ($\text{B}_2\text{H}_6(g)$) from its elements: $$2\,\text{B}(s) + 3\,\text{H}_2(g) \rightarrow \text{B}_2\text{H}_6(g)$$",
        "options": [
            r"$-35\text{ kJ/mol}_{\text{rxn}}$",
            r"$+35\text{ kJ/mol}_{\text{rxn}}$",
            r"$+167\text{ kJ/mol}_{\text{rxn}}$",
            r"$+607\text{ kJ/mol}_{\text{rxn}}$",
        ],
        "correct_index": 1,
        "explanation": r"To obtain $2\,\text{B}(s) + 3\,\text{H}_2(g) \rightarrow \text{B}_2\text{H}_6(g)$: Keep Equation 1 ($-1273\text{ kJ}$), reverse Equation 2 ($\text{B}_2\text{O}_3(s) + 3\,\text{H}_2\text{O}(l) \rightarrow \text{B}_2\text{H}_6(g) + 3\,\text{O}_2(g)$, $+2166\text{ kJ}$), and multiply Equation 3 by $3$ ($3\,\text{H}_2(g) + \frac{3}{2}\,\text{O}_2(g) \rightarrow 3\,\text{H}_2\text{O}(l)$, $3(-286) = -858\text{ kJ}$). Note that Equation 4 is a distractor and is not needed because $\text{H}_2\text{O}(l)$ cancels directly between Equations 2 and 3. Summing gives $\Delta H^\circ = -1273 + 2166 - 858 = +35\text{ kJ/mol}_{\text{rxn}}$.",
    },
    {
        "unit_q_num": 48,
        "topic_code": "6.9",
        "topic_title": "Hess's Law",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Step in Born-Haber Cycle for $\text{LiF}(s)$</th><th>$\Delta H^\circ$ ($\text{kJ/mol}$)</th></tr></thead><tbody><tr><td>Sublimation of $\text{Li}(s)$: $\text{Li}(s) \rightarrow \text{Li}(g)$</td><td>$+161$</td></tr><tr><td>First ionization of $\text{Li}(g)$: $\text{Li}(g) \rightarrow \text{Li}^+(g) + e^-$</td><td>$+520$</td></tr><tr><td>Bond dissociation of $\text{F}_2(g)$: $\text{F}_2(g) \rightarrow 2\,\text{F}(g)$</td><td>$+158$</td></tr><tr><td>Electron affinity of $\text{F}(g)$: $\text{F}(g) + e^- \rightarrow \text{F}^-(g)$</td><td>$-328$</td></tr><tr><td>Lattice formation of $\text{LiF}(s)$: $\text{Li}^+(g) + \text{F}^-(g) \rightarrow \text{LiF}(s)$</td><td>$-1047$</td></tr></tbody></table>""",
        "question": r"Using the Born-Haber cycle data in the table above and Hess's law, calculate the standard enthalpy of formation ($\Delta H_f^\circ$) of $\text{LiF}(s)$: $$\text{Li}(s) + \frac{1}{2}\,\text{F}_2(g) \rightarrow \text{LiF}(s)$$",
        "options": [
            r"$-536\text{ kJ/mol}$",
            r"$-615\text{ kJ/mol}$",
            r"$+615\text{ kJ/mol}$",
            r"$-1271\text{ kJ/mol}$",
        ],
        "correct_index": 1,
        "explanation": r"Carefully note that forming $1\text{ mol}$ of $\text{F}(g)$ from $\frac{1}{2}\,\text{F}_2(g)$ requires half of the $\text{F}_2$ bond dissociation enthalpy: $\frac{1}{2}(+158) = +79\text{ kJ/mol}$. Summing all steps in the Born-Haber cycle gives $\Delta H_f^\circ[\text{LiF}(s)] = (+161) + (+520) + (+79) + (-328) + (-1047) = -615\text{ kJ/mol}$.",
    },
    {
        "unit_q_num": 49,
        "topic_code": "6.9",
        "topic_title": "Hess's Law",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Reaction</th><th>$\Delta H^\circ$ ($\text{kJ/mol}_{\text{rxn}}$)</th></tr></thead><tbody><tr><td>$\text{Fe}_2\text{O}_3(s) + 3\,\text{CO}(g) \rightarrow 2\,\text{Fe}(s) + 3\,\text{CO}_2(g)$</td><td>$-24.8$</td></tr><tr><td>$3\,\text{Fe}_2\text{O}_3(s) + \text{CO}(g) \rightarrow 2\,\text{Fe}_3\text{O}_4(s) + \text{CO}_2(g)$</td><td>$-47.2$</td></tr><tr><td>$\text{Fe}_3\text{O}_4(s) + \text{CO}(g) \rightarrow 3\,\text{FeO}(s) + \text{CO}_2(g)$</td><td>$+19.4$</td></tr></tbody></table>""",
        "question": r"Using the three blast-furnace reactions in the table above, calculate $\Delta H^\circ$ for the reduction of iron(II) oxide by carbon monoxide: $$\text{FeO}(s) + \text{CO}(g) \rightarrow \text{Fe}(s) + \text{CO}_2(g)$$",
        "options": [
            r"$-17.7\text{ kJ/mol}_{\text{rxn}}$",
            r"$-66.0\text{ kJ/mol}_{\text{rxn}}$",
            r"$-11.0\text{ kJ/mol}_{\text{rxn}}$",
            r"$+11.0\text{ kJ/mol}_{\text{rxn}}$",
        ],
        "correct_index": 2,
        "explanation": r"To eliminate $\text{Fe}_2\text{O}_3(s)$ and $\text{Fe}_3\text{O}_4(s)$: Multiply Reaction 1 by $3$ ($\Delta H = 3(-24.8) = -74.4\text{ kJ}$), reverse Reaction 2 ($\Delta H = +47.2\text{ kJ}$), and reverse Reaction 3 multiplied by $2$ ($\Delta H = 2(-19.4) = -38.8\text{ kJ}$). Summing these gives $6\,\text{FeO}(s) + 6\,\text{CO}(g) \rightarrow 6\,\text{Fe}(s) + 6\,\text{CO}_2(g)$ with $\Delta H^\circ = -74.4 + 47.2 - 38.8 = -66.0\text{ kJ/mol}_{\text{rxn}}$. Dividing the equation and $\Delta H^\circ$ by $6$ gives $\Delta H^\circ = \frac{-66.0}{6} = -11.0\text{ kJ/mol}_{\text{rxn}}$.",
    },
    {
        "unit_q_num": 50,
        "topic_code": "6.9",
        "topic_title": "Hess's Law",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Reaction</th><th>$\Delta H^\circ$</th></tr></thead><tbody><tr><td>$\text{A} + 2\,\text{B} \rightarrow \text{C}$</td><td>$\Delta H_1^\circ$</td></tr><tr><td>$\text{C} \rightarrow 2\,\text{D} + \text{E}$</td><td>$\Delta H_2^\circ$</td></tr></tbody></table>""",
        "question": r"Given the two hypothetical reactions above, which algebraic expression gives $\Delta H^\circ$ for the reaction $\text{D} + \frac{1}{2}\,\text{E} \rightarrow \frac{1}{2}\,\text{A} + \text{B}$?",
        "options": [
            r"$\frac{1}{2}(\Delta H_1^\circ + \Delta H_2^\circ)$",
            r"$\frac{1}{2}(\Delta H_2^\circ - \Delta H_1^\circ)$",
            r"$-2(\Delta H_1^\circ + \Delta H_2^\circ)$",
            r"$-\frac{1}{2}(\Delta H_1^\circ + \Delta H_2^\circ)$",
        ],
        "correct_index": 3,
        "explanation": r"Adding the two given reactions cancels intermediate $\text{C}$ to yield $\text{A} + 2\,\text{B} \rightarrow 2\,\text{D} + \text{E}$ with $\Delta H^\circ = \Delta H_1^\circ + \Delta H_2^\circ$. The target reaction $\text{D} + \frac{1}{2}\,\text{E} \rightarrow \frac{1}{2}\,\text{A} + \text{B}$ is the reverse of this overall reaction multiplied by $\frac{1}{2}$, so its enthalpy change is $-\frac{1}{2}(\Delta H_1^\circ + \Delta H_2^\circ)$.",
    },

    # -------------------------------------------------------------------------
    # Added 2026-10-03 — Blind-spot coverage (Fall 2024 CED): topics 6.1–6.9
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 51,
        "topic_code": "6.1",
        "topic_title": "Endothermic and Exothermic Processes",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A hot pack contains solid calcium chloride, $\text{CaCl}_2(s)$, and a separate pouch of water. When the pouch is broken and the solid dissolves, the temperature of the mixture increases. Which statement best explains this observation in terms of the interactions that are broken and formed during the dissolution?",
        "options": [
            r"Separating the $\text{Ca}^{2+}$ and $\text{Cl}^-$ ions from the crystal lattice releases energy, and this energy warms the water.",
            r"Separating water molecules from one another releases energy because hydrogen bonds between the water molecules are broken.",
            r"The energy released when ion–dipole attractions form between the ions and water molecules is greater than the energy required to separate the ions in the solid and to separate the water molecules.",
            r"The dissolution is endothermic: the dissolving $\text{CaCl}_2$ absorbs thermal energy, and this is why the thermometer reading increases.",
        ],
        "correct_index": 2,
        "explanation": r"Dissolving $\text{CaCl}_2$ requires energy to overcome the attractions between the ions in the lattice and the hydrogen bonds between water molecules (breaking attractions always requires energy), and it releases energy as new ion–dipole attractions form between the ions and water molecules (forming attractions always releases energy). The rising temperature shows that thermal energy is transferred to the solution (the surroundings), so the dissolution is exothermic: the energy released in forming the ion–dipole attractions exceeds the energy absorbed in separating the ions and the water molecules. The statements claiming that separating the ions or breaking hydrogen bonds releases energy reverse the energetics of breaking attractions. Calling the process endothermic confuses the system with the surroundings; an endothermic dissolution absorbs energy from the water, so the thermometer reading would decrease.",
    },
    {
        "unit_q_num": 52,
        "topic_code": "6.2",
        "topic_title": "Energy Diagrams",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 560 265" role="img" font-family="sans-serif" aria-label="Two potential energy diagrams plotted against reaction progress. In Diagram I the products are at a lower potential energy than the reactants, with an energy barrier between them. In Diagram II the products are at a higher potential energy than the reactants, with an energy barrier between them.">
<line x1="50" y1="230" x2="260" y2="230" stroke="#111827" stroke-width="2"/>
<line x1="50" y1="230" x2="50" y2="40" stroke="#111827" stroke-width="2"/>
<polyline points="60,132 61,132 61.9,132 62.9,132 63.8,132 64.8,132 65.7,132 66.7,132 67.6,132 68.5,132 69.5,132 70.5,132 71.4,132 72.3,132 73.3,132 74.2,132 75.2,132 76.2,132 77.1,132 78,132 79,132 80,132 80.9,132 81.8,132 82.8,132 83.8,132 84.7,132 85.7,132 86.6,132 87.5,132 88.5,132 89.5,132 90.4,132 91.3,132 92.3,132 93.2,132 94.2,132 95.2,132 96.1,132 97.1,132 98,132 98.9,132 99.9,132 100.8,132 101.8,132 102.8,132 103.7,132 104.7,132 105.6,132 106.5,132 107.5,132 108.5,131.9 109.4,131.7 110.3,131.4 111.3,130.9 112.2,130.3 113.2,129.5 114.2,128.6 115.1,127.6 116,126.4 117,125.2 117.9,123.8 118.9,122.3 119.8,120.7 120.8,119 121.8,117.3 122.7,115.4 123.7,113.5 124.6,111.5 125.5,109.5 126.5,107.4 127.5,105.3 128.4,103.2 129.3,101 130.3,98.9 131.2,96.8 132.2,94.6 133.2,92.5 134.1,90.5 135.1,88.5 136,86.5 136.9,84.6 137.9,82.8 138.8,81.1 139.8,79.4 140.8,77.9 141.7,76.5 142.7,75.2 143.6,74 144.6,73 145.5,72.1 146.4,71.4 147.4,70.8 148.4,70.3 149.3,70.1 150.2,70 151.2,70 152.1,70.3 153.1,70.7 154.1,71.2 155,72 155.9,72.9 156.9,74 157.9,75.3 158.8,76.7 159.8,78.3 160.7,80.1 161.7,82 162.6,84.1 163.6,86.3 164.5,88.7 165.4,91.2 166.4,93.8 167.3,96.6 168.3,99.4 169.2,102.4 170.2,105.4 171.1,108.5 172.1,111.7 173.1,115 174,118.3 174.9,121.7 175.9,125 176.8,128.4 177.8,131.8 178.8,135.2 179.7,138.6 180.7,142 181.6,145.3 182.6,148.6 183.5,151.8 184.4,154.9 185.4,157.9 186.4,160.9 187.3,163.7 188.2,166.5 189.2,169.1 190.2,171.5 191.1,173.8 192,176 193,178 193.9,179.9 194.9,181.5 195.8,183 196.8,184.3 197.8,185.4 198.7,186.4 199.7,187.1 200.6,187.6 201.6,187.9 202.5,188 203.4,188 204.4,188 205.3,188 206.3,188 207.2,188 208.2,188 209.2,188 210.1,188 211.1,188 212,188 213,188 213.9,188 214.8,188 215.8,188 216.8,188 217.7,188 218.7,188 219.6,188 220.5,188 221.5,188 222.4,188 223.4,188 224.3,188 225.3,188 226.2,188 227.2,188 228.2,188 229.1,188 230.1,188 231,188 232,188 232.9,188 233.8,188 234.8,188 235.8,188 236.7,188 237.7,188 238.6,188 239.5,188 240.5,188 241.4,188 242.4,188 243.3,188 244.3,188 245.2,188 246.2,188 247.2,188 248.1,188 249.1,188 250,188" fill="none" stroke="#111827" stroke-width="2.2" stroke-linejoin="round"/>
<text x="83.8" y="149" font-size="12" text-anchor="middle" fill="#111827">Reactants</text>
<text x="226.2" y="205" font-size="12" text-anchor="middle" fill="#111827">Products</text>
<text x="155" y="26" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">Diagram I</text>
<text x="155" y="252" font-size="13" text-anchor="middle" fill="#111827">Reaction Progress</text>
<text x="36" y="135" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 36 135)">Potential Energy</text>
<line x1="320" y1="230" x2="530" y2="230" stroke="#111827" stroke-width="2"/>
<line x1="320" y1="230" x2="320" y2="40" stroke="#111827" stroke-width="2"/>
<polyline points="330,188 330.9,188 331.9,188 332.9,188 333.8,188 334.8,188 335.7,188 336.6,188 337.6,188 338.6,188 339.5,188 340.4,188 341.4,188 342.4,188 343.3,188 344.2,188 345.2,188 346.1,188 347.1,188 348.1,188 349,188 349.9,188 350.9,188 351.9,188 352.8,188 353.8,188 354.7,188 355.6,188 356.6,188 357.6,188 358.5,188 359.4,188 360.4,188 361.4,188 362.3,188 363.2,188 364.2,188 365.1,188 366.1,188 367.1,188 368,188 368.9,188 369.9,188 370.9,188 371.8,188 372.8,188 373.7,188 374.6,188 375.6,188 376.6,188 377.5,188 378.4,187.9 379.4,187.6 380.4,187.1 381.3,186.4 382.2,185.4 383.2,184.3 384.1,183 385.1,181.5 386.1,179.9 387,178 387.9,176 388.9,173.8 389.9,171.5 390.8,169.1 391.8,166.5 392.7,163.7 393.6,160.9 394.6,157.9 395.6,154.9 396.5,151.8 397.4,148.6 398.4,145.3 399.4,142 400.3,138.6 401.2,135.2 402.2,131.8 403.1,128.4 404.1,125 405.1,121.7 406,118.3 406.9,115 407.9,111.7 408.9,108.5 409.8,105.4 410.8,102.4 411.7,99.4 412.6,96.6 413.6,93.8 414.6,91.2 415.5,88.7 416.4,86.3 417.4,84.1 418.4,82 419.3,80.1 420.2,78.3 421.2,76.7 422.1,75.3 423.1,74 424.1,72.9 425,72 425.9,71.2 426.9,70.7 427.9,70.3 428.8,70 429.8,70 430.7,70.1 431.6,70.3 432.6,70.8 433.6,71.4 434.5,72.1 435.4,73 436.4,74 437.4,75.2 438.3,76.5 439.2,77.9 440.2,79.4 441.1,81.1 442.1,82.8 443.1,84.6 444,86.5 444.9,88.5 445.9,90.5 446.9,92.5 447.8,94.6 448.8,96.8 449.7,98.9 450.6,101 451.6,103.2 452.6,105.3 453.5,107.4 454.4,109.5 455.4,111.5 456.4,113.5 457.3,115.4 458.2,117.3 459.2,119 460.1,120.7 461.1,122.3 462,123.8 463,125.2 463.9,126.4 464.9,127.6 465.9,128.6 466.8,129.5 467.8,130.3 468.7,130.9 469.6,131.4 470.6,131.7 471.6,131.9 472.5,132 473.4,132 474.4,132 475.4,132 476.3,132 477.2,132 478.2,132 479.1,132 480.1,132 481.1,132 482,132 483,132 483.9,132 484.9,132 485.8,132 486.8,132 487.7,132 488.6,132 489.6,132 490.5,132 491.5,132 492.4,132 493.4,132 494.4,132 495.3,132 496.2,132 497.2,132 498.1,132 499.1,132 500.1,132 501,132 502,132 502.9,132 503.9,132 504.8,132 505.8,132 506.7,132 507.6,132 508.6,132 509.5,132 510.5,132 511.4,132 512.4,132 513.4,132 514.3,132 515.2,132 516.2,132 517.1,132 518.1,132 519,132 520,132" fill="none" stroke="#111827" stroke-width="2.2" stroke-linejoin="round"/>
<text x="353.8" y="205" font-size="12" text-anchor="middle" fill="#111827">Reactants</text>
<text x="496.2" y="149" font-size="12" text-anchor="middle" fill="#111827">Products</text>
<text x="425" y="26" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">Diagram II</text>
<text x="425" y="252" font-size="13" text-anchor="middle" fill="#111827">Reaction Progress</text>
<text x="306" y="135" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 306 135)">Potential Energy</text>
</svg>
<figcaption>Figure: Potential energy diagrams for two processes</figcaption>
</figure>""",
        "question": r"When solid barium hydroxide octahydrate, $\text{Ba(OH)}_2\cdot 8\text{H}_2\text{O}(s)$, and solid ammonium chloride, $\text{NH}_4\text{Cl}(s)$, are mixed in a flask at room temperature, they react, and the outside of the flask becomes cold enough to freeze a thin layer of water onto it. Which diagram above represents this reaction, and what is the direction of the thermal energy transfer?",
        "options": [
            r"Diagram I, because thermal energy is transferred from the reacting system to the flask and the surroundings.",
            r"Diagram I, because the decrease in temperature shows that the reacting system loses energy as it forms products.",
            r"Diagram II, because thermal energy is transferred from the reacting system to the flask and the surroundings.",
            r"Diagram II, because thermal energy is transferred from the flask and the surroundings into the reacting system.",
        ],
        "correct_index": 3,
        "explanation": r"The flask, which is part of the surroundings, becomes colder, so thermal energy flows from the surroundings into the reacting system ($q_{\text{surr}} < 0$ and $q_{\text{sys}} > 0$). The reaction is therefore endothermic, and its products must lie at a higher potential energy than its reactants, as in Diagram II. Diagram I shows products below reactants, which represents an exothermic reaction that would warm the flask. A falling temperature does not mean that the system loses energy: the flask and the frozen water respond to the surroundings, which lose the energy that the system gains. Pairing Diagram II with energy flowing out of the system contradicts the diagram, because raising the potential energy of the system requires an input of energy.",
    },
    {
        "unit_q_num": 53,
        "topic_code": "6.3",
        "topic_title": "Heat Transfer and Thermal Equilibrium",
        "difficulty": "Challenging",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 320" role="img" font-family="sans-serif" aria-label="Graph of temperature in degrees Celsius versus time in minutes from 0 to 8 minutes. The metal curve starts at 90 degrees and decreases, leveling off at 30 degrees. The water curve, dashed, starts at 20 degrees and increases, leveling off at 30 degrees. Both curves reach 30 degrees by about 6 minutes and stay there.">
<line x1="70" y1="270" x2="490" y2="270" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="248" x2="490" y2="248" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="226" x2="490" y2="226" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="204" x2="490" y2="204" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="182" x2="490" y2="182" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="160" x2="490" y2="160" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="138" x2="490" y2="138" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="116" x2="490" y2="116" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="94" x2="490" y2="94" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="72" x2="490" y2="72" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="50" x2="490" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="270" x2="70" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="122.5" y1="270" x2="122.5" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="175" y1="270" x2="175" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="227.5" y1="270" x2="227.5" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="280" y1="270" x2="280" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="332.5" y1="270" x2="332.5" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="385" y1="270" x2="385" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="437.5" y1="270" x2="437.5" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="490" y1="270" x2="490" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="270" x2="490" y2="270" stroke="#111827" stroke-width="2"/>
<line x1="70" y1="270" x2="70" y2="50" stroke="#111827" stroke-width="2"/>
<line x1="64" y1="270" x2="70" y2="270" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="274" font-size="12" text-anchor="end" fill="#111827">0</text>
<line x1="64" y1="248" x2="70" y2="248" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="252" font-size="12" text-anchor="end" fill="#111827">10</text>
<line x1="64" y1="226" x2="70" y2="226" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="230" font-size="12" text-anchor="end" fill="#111827">20</text>
<line x1="64" y1="204" x2="70" y2="204" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="208" font-size="12" text-anchor="end" fill="#111827">30</text>
<line x1="64" y1="182" x2="70" y2="182" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="186" font-size="12" text-anchor="end" fill="#111827">40</text>
<line x1="64" y1="160" x2="70" y2="160" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="164" font-size="12" text-anchor="end" fill="#111827">50</text>
<line x1="64" y1="138" x2="70" y2="138" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="142" font-size="12" text-anchor="end" fill="#111827">60</text>
<line x1="64" y1="116" x2="70" y2="116" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="120" font-size="12" text-anchor="end" fill="#111827">70</text>
<line x1="64" y1="94" x2="70" y2="94" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="98" font-size="12" text-anchor="end" fill="#111827">80</text>
<line x1="64" y1="72" x2="70" y2="72" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="76" font-size="12" text-anchor="end" fill="#111827">90</text>
<line x1="64" y1="50" x2="70" y2="50" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="54" font-size="12" text-anchor="end" fill="#111827">100</text>
<line x1="70" y1="270" x2="70" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="70" y="291" font-size="12" text-anchor="middle" fill="#111827">0</text>
<line x1="122.5" y1="270" x2="122.5" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="122.5" y="291" font-size="12" text-anchor="middle" fill="#111827">1</text>
<line x1="175" y1="270" x2="175" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="175" y="291" font-size="12" text-anchor="middle" fill="#111827">2</text>
<line x1="227.5" y1="270" x2="227.5" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="227.5" y="291" font-size="12" text-anchor="middle" fill="#111827">3</text>
<line x1="280" y1="270" x2="280" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="280" y="291" font-size="12" text-anchor="middle" fill="#111827">4</text>
<line x1="332.5" y1="270" x2="332.5" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="332.5" y="291" font-size="12" text-anchor="middle" fill="#111827">5</text>
<line x1="385" y1="270" x2="385" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="385" y="291" font-size="12" text-anchor="middle" fill="#111827">6</text>
<line x1="437.5" y1="270" x2="437.5" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="437.5" y="291" font-size="12" text-anchor="middle" fill="#111827">7</text>
<line x1="490" y1="270" x2="490" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="490" y="291" font-size="12" text-anchor="middle" fill="#111827">8</text>
<polyline points="70,72 72.6,77.4 75.2,82.6 77.9,87.5 80.5,92.3 83.1,96.8 85.8,101.2 88.4,105.4 91,109.4 93.6,113.3 96.2,117 98.9,120.5 101.5,123.9 104.1,127.2 106.8,130.3 109.4,133.3 112,136.2 114.6,139 117.2,141.6 119.9,144.2 122.5,146.6 125.1,149 127.8,151.2 130.4,153.4 133,155.4 135.6,157.4 138.2,159.3 140.9,161.1 143.5,162.9 146.1,164.6 148.8,166.2 151.4,167.7 154,169.2 156.6,170.6 159.2,172 161.9,173.3 164.5,174.5 167.1,175.7 169.8,176.9 172.4,178 175,179.1 177.6,180.1 180.2,181.1 182.9,182 185.5,182.9 188.1,183.8 190.8,184.6 193.4,185.4 196,186.1 198.6,186.9 201.2,187.6 203.9,188.2 206.5,188.9 209.1,189.5 211.8,190.1 214.4,190.7 217,191.2 219.6,191.7 222.3,192.2 224.9,192.7 227.5,193.2 230.1,193.6 232.8,194 235.4,194.4 238,194.8 240.6,195.2 243.2,195.6 245.9,195.9 248.5,196.2 251.1,196.6 253.8,196.9 256.4,197.1 259,197.4 261.6,197.7 264.2,198 266.9,198.2 269.5,198.4 272.1,198.7 274.8,198.9 277.4,199.1 280,199.3 282.6,199.5 285.2,199.7 287.9,199.8 290.5,200 293.1,200.2 295.8,200.3 298.4,200.5 301,200.6 303.6,200.8 306.2,200.9 308.9,201 311.5,201.1 314.1,201.3 316.8,201.4 319.4,201.5 322,201.6 324.6,201.7 327.2,201.8 329.9,201.9 332.5,202 335.1,202 337.8,202.1 340.4,202.2 343,202.3 345.6,202.3 348.3,202.4 350.9,202.5 353.5,202.5 356.1,202.6 358.8,202.7 361.4,202.7 364,202.8 366.6,202.8 369.2,202.9 371.9,202.9 374.5,202.9 377.1,203 379.8,203 382.4,203.1 385,203.1 387.6,203.1 390.2,203.2 392.9,203.2 395.5,203.2 398.1,203.3 400.8,203.3 403.4,203.3 406,203.4 408.6,203.4 411.2,203.4 413.9,203.4 416.5,203.5 419.1,203.5 421.8,203.5 424.4,203.5 427,203.5 429.6,203.6 432.2,203.6 434.9,203.6 437.5,203.6 440.1,203.6 442.8,203.6 445.4,203.7 448,203.7 450.6,203.7 453.3,203.7 455.9,203.7 458.5,203.7 461.1,203.7 463.8,203.7 466.4,203.8 469,203.8 471.6,203.8 474.2,203.8 476.9,203.8 479.5,203.8 482.1,203.8 484.8,203.8 487.4,203.8 490,203.8" fill="none" stroke="#111827" stroke-width="2.4" stroke-linejoin="round"/>
<polyline points="70,226 72.6,225.1 75.2,224.2 77.9,223.4 80.5,222.6 83.1,221.9 85.8,221.1 88.4,220.4 91,219.8 93.6,219.1 96.2,218.5 98.9,217.9 101.5,217.3 104.1,216.8 106.8,216.3 109.4,215.8 112,215.3 114.6,214.8 117.2,214.4 119.9,214 122.5,213.6 125.1,213.2 127.8,212.8 130.4,212.4 133,212.1 135.6,211.8 138.2,211.4 140.9,211.1 143.5,210.9 146.1,210.6 148.8,210.3 151.4,210 154,209.8 156.6,209.6 159.2,209.3 161.9,209.1 164.5,208.9 167.1,208.7 169.8,208.5 172.4,208.3 175,208.2 177.6,208 180.2,207.8 182.9,207.7 185.5,207.5 188.1,207.4 190.8,207.2 193.4,207.1 196,207 198.6,206.9 201.2,206.7 203.9,206.6 206.5,206.5 209.1,206.4 211.8,206.3 214.4,206.2 217,206.1 219.6,206 222.3,206 224.9,205.9 227.5,205.8 230.1,205.7 232.8,205.7 235.4,205.6 238,205.5 240.6,205.5 243.2,205.4 245.9,205.3 248.5,205.3 251.1,205.2 253.8,205.2 256.4,205.1 259,205.1 261.6,205.1 264.2,205 266.9,205 269.5,204.9 272.1,204.9 274.8,204.9 277.4,204.8 280,204.8 282.6,204.8 285.2,204.7 287.9,204.7 290.5,204.7 293.1,204.6 295.8,204.6 298.4,204.6 301,204.6 303.6,204.5 306.2,204.5 308.9,204.5 311.5,204.5 314.1,204.5 316.8,204.4 319.4,204.4 322,204.4 324.6,204.4 327.2,204.4 329.9,204.4 332.5,204.3 335.1,204.3 337.8,204.3 340.4,204.3 343,204.3 345.6,204.3 348.3,204.3 350.9,204.3 353.5,204.2 356.1,204.2 358.8,204.2 361.4,204.2 364,204.2 366.6,204.2 369.2,204.2 371.9,204.2 374.5,204.2 377.1,204.2 379.8,204.2 382.4,204.2 385,204.1 387.6,204.1 390.2,204.1 392.9,204.1 395.5,204.1 398.1,204.1 400.8,204.1 403.4,204.1 406,204.1 408.6,204.1 411.2,204.1 413.9,204.1 416.5,204.1 419.1,204.1 421.8,204.1 424.4,204.1 427,204.1 429.6,204.1 432.2,204.1 434.9,204.1 437.5,204.1 440.1,204.1 442.8,204.1 445.4,204.1 448,204.1 450.6,204.1 453.3,204.1 455.9,204 458.5,204 461.1,204 463.8,204 466.4,204 469,204 471.6,204 474.2,204 476.9,204 479.5,204 482.1,204 484.8,204 487.4,204 490,204" fill="none" stroke="#2563eb" stroke-width="2.4" stroke-linejoin="round" stroke-dasharray="7 4"/>
<text x="144.9" y="135.8" font-size="13" text-anchor="start" fill="#111827">Metal</text>
<text x="148.8" y="237" font-size="13" text-anchor="start" fill="#2563eb">Water</text>
<text x="280" y="309" font-size="13" text-anchor="middle" fill="#111827">Time (min)</text>
<text x="22" y="160" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 22 160)">Temperature (°C)</text>
</svg>
<figcaption>Figure: Temperatures of the metal block and the water versus time</figcaption>
</figure>""",
        "question": r"A $100.0\text{ g}$ block of a metal at $90.0^\circ\text{C}$ is placed into $100.0\text{ g}$ of water at $20.0^\circ\text{C}$ in an insulated container. The temperatures of the metal and of the water were recorded over time, as shown in the graph above. Which of the following statements is supported by the data?",
        "options": [
            r"Before $t = 6\text{ min}$, collisions transfer energy from the metal atoms, which have the greater average kinetic energy, to the water molecules; the specific heat capacity of the metal is about $\frac{1}{6}$ that of water.",
            r"Energy is transferred from the metal to the water until both contain the same total thermal energy; the specific heat capacity of the metal is about $\frac{1}{6}$ that of water.",
            r"Before $t = 6\text{ min}$, collisions transfer energy from the metal atoms, which have the greater average kinetic energy, to the water molecules; the specific heat capacity of the metal is about $6$ times that of water.",
            r"After $t = 6\text{ min}$, the water molecules have a greater average kinetic energy than the metal atoms, because water has the larger specific heat capacity.",
        ],
        "correct_index": 0,
        "explanation": r"From the graph, the metal cools from $90.0^\circ\text{C}$ to $30.0^\circ\text{C}$ ($|\Delta T| = 60.0^\circ\text{C}$) while the water warms from $20.0^\circ\text{C}$ to $30.0^\circ\text{C}$ ($\Delta T = 10.0^\circ\text{C}$). In an insulated container the heat lost by the metal equals the heat gained by the water: $m c_{\text{metal}}(60.0^\circ\text{C}) = m c_{\text{water}}(10.0^\circ\text{C})$, so with equal masses $c_{\text{metal}} = \frac{1}{6}c_{\text{water}} \approx 0.70\text{ J/(g}\cdot^\circ\text{C)}$. The substance with the smaller specific heat capacity undergoes the larger temperature change, so the claim that the metal's value is $6$ times larger inverts the ratio. While the metal is hotter, its atoms have the greater average kinetic energy, and collisions at the surface transfer energy to the water. Transfer stops when the temperatures, and therefore the average kinetic energies of the particles, become equal, not when the total thermal energies are equal; after $6\text{ min}$ both are at $30.0^\circ\text{C}$.",
    },
    {
        "unit_q_num": 54,
        "topic_code": "6.4",
        "topic_title": "Heat Capacity and Calorimetry",
        "difficulty": "Challenging",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 320" role="img" font-family="sans-serif" aria-label="Graph of solution temperature in degrees Celsius, from 20 to 30, versus time in minutes, from 0 to 10. Data points are constant at 21.0 degrees from 0 to 2.0 minutes, when the salt is added. The temperature then rises quickly to a highest reading of 28.6 degrees at 4.0 minutes and afterward falls linearly by 0.1 degree every half minute, reaching 27.4 degrees at 10 minutes. A dashed straight line fitted to the cooling points is extended back across the whole graph; it passes through 29.0 degrees at 2.0 minutes and 29.4 degrees at 0 minutes.">
<line x1="70" y1="270" x2="490" y2="270" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="248" x2="490" y2="248" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="226" x2="490" y2="226" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="204" x2="490" y2="204" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="182" x2="490" y2="182" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="160" x2="490" y2="160" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="138" x2="490" y2="138" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="116" x2="490" y2="116" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="94" x2="490" y2="94" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="72" x2="490" y2="72" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="50" x2="490" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="270" x2="70" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="112" y1="270" x2="112" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="154" y1="270" x2="154" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="196" y1="270" x2="196" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="238" y1="270" x2="238" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="280" y1="270" x2="280" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="322" y1="270" x2="322" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="364" y1="270" x2="364" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="406" y1="270" x2="406" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="448" y1="270" x2="448" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="490" y1="270" x2="490" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="270" x2="490" y2="270" stroke="#111827" stroke-width="2"/>
<line x1="70" y1="270" x2="70" y2="50" stroke="#111827" stroke-width="2"/>
<line x1="64" y1="270" x2="70" y2="270" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="274" font-size="12" text-anchor="end" fill="#111827">20</text>
<line x1="64" y1="248" x2="70" y2="248" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="252" font-size="12" text-anchor="end" fill="#111827">21</text>
<line x1="64" y1="226" x2="70" y2="226" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="230" font-size="12" text-anchor="end" fill="#111827">22</text>
<line x1="64" y1="204" x2="70" y2="204" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="208" font-size="12" text-anchor="end" fill="#111827">23</text>
<line x1="64" y1="182" x2="70" y2="182" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="186" font-size="12" text-anchor="end" fill="#111827">24</text>
<line x1="64" y1="160" x2="70" y2="160" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="164" font-size="12" text-anchor="end" fill="#111827">25</text>
<line x1="64" y1="138" x2="70" y2="138" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="142" font-size="12" text-anchor="end" fill="#111827">26</text>
<line x1="64" y1="116" x2="70" y2="116" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="120" font-size="12" text-anchor="end" fill="#111827">27</text>
<line x1="64" y1="94" x2="70" y2="94" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="98" font-size="12" text-anchor="end" fill="#111827">28</text>
<line x1="64" y1="72" x2="70" y2="72" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="76" font-size="12" text-anchor="end" fill="#111827">29</text>
<line x1="64" y1="50" x2="70" y2="50" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="54" font-size="12" text-anchor="end" fill="#111827">30</text>
<line x1="70" y1="270" x2="70" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="70" y="291" font-size="12" text-anchor="middle" fill="#111827">0</text>
<line x1="112" y1="270" x2="112" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="112" y="291" font-size="12" text-anchor="middle" fill="#111827">1</text>
<line x1="154" y1="270" x2="154" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="154" y="291" font-size="12" text-anchor="middle" fill="#111827">2</text>
<line x1="196" y1="270" x2="196" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="196" y="291" font-size="12" text-anchor="middle" fill="#111827">3</text>
<line x1="238" y1="270" x2="238" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="238" y="291" font-size="12" text-anchor="middle" fill="#111827">4</text>
<line x1="280" y1="270" x2="280" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="280" y="291" font-size="12" text-anchor="middle" fill="#111827">5</text>
<line x1="322" y1="270" x2="322" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="322" y="291" font-size="12" text-anchor="middle" fill="#111827">6</text>
<line x1="364" y1="270" x2="364" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="364" y="291" font-size="12" text-anchor="middle" fill="#111827">7</text>
<line x1="406" y1="270" x2="406" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="406" y="291" font-size="12" text-anchor="middle" fill="#111827">8</text>
<line x1="448" y1="270" x2="448" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="448" y="291" font-size="12" text-anchor="middle" fill="#111827">9</text>
<line x1="490" y1="270" x2="490" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="490" y="291" font-size="12" text-anchor="middle" fill="#111827">10</text>
<line x1="70" y1="63.2" x2="490" y2="107.2" stroke="#374151" stroke-width="1.8" stroke-dasharray="8 5"/>
<line x1="154" y1="270" x2="154" y2="50" stroke="#9ca3af" stroke-width="1.5" stroke-dasharray="3 4"/>
<text x="154" y="42" font-size="12" text-anchor="middle" fill="#111827">salt added (t = 2.0 min)</text>
<circle cx="70" cy="248" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="91" cy="248" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="112" cy="248" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="133" cy="248" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="154" cy="248" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="175" cy="138" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="196" cy="94" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="217" cy="83" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="238" cy="80.8" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="259" cy="83" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="280" cy="85.2" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="301" cy="87.4" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="322" cy="89.6" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="343" cy="91.8" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="364" cy="94" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="385" cy="96.2" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="406" cy="98.4" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="427" cy="100.6" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="448" cy="102.8" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="469" cy="105" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<circle cx="490" cy="107.2" r="3.6" fill="#374151" stroke="#111827" stroke-width="1"/>
<text x="280" y="309" font-size="13" text-anchor="middle" fill="#111827">Time (min)</text>
<text x="24" y="160" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 24 160)">Temperature (°C)</text>
</svg>
<figcaption>Figure: Temperature of the calorimeter contents versus time</figcaption>
</figure>""",
        "question": r"A student dissolves $0.0500\text{ mol}$ of a soluble salt in water in a coffee-cup calorimeter, forming $100.0\text{ g}$ of solution. The salt is added at $t = 2.0\text{ min}$, and the highest temperature recorded is $28.6^\circ\text{C}$. Because the calorimeter slowly loses thermal energy to the room, the student extends the straight cooling portion of the data backward (dashed line). Assuming that the solution has a specific heat capacity of $4.18\text{ J/(g}\cdot^\circ\text{C)}$ and that the calorimeter absorbs a negligible amount of heat, what is the best estimate of $\Delta H_{\text{soln}}$ for the salt?",
        "options": [
            r"$-70.2\text{ kJ/mol}$",
            r"$-66.9\text{ kJ/mol}$",
            r"$-63.5\text{ kJ/mol}$",
            r"$-53.5\text{ kJ/mol}$",
        ],
        "correct_index": 1,
        "explanation": r"The temperature the solution would have reached with no heat loss is found where the extrapolated cooling line crosses the time of mixing, $t = 2.0\text{ min}$: $29.0^\circ\text{C}$. Thus $\Delta T = 29.0 - 21.0 = 8.0^\circ\text{C}$ and $q_{\text{soln}} = (100.0\text{ g})(4.18\text{ J/(g}\cdot^\circ\text{C)})(8.0^\circ\text{C}) = 3344\text{ J}$. The dissolution released this energy, so $q_{\text{rxn}} = -3.344\text{ kJ}$ and $\Delta H_{\text{soln}} = \frac{-3.344\text{ kJ}}{0.0500\text{ mol}} = -66.9\text{ kJ/mol}$. Using the highest recorded temperature ($\Delta T = 7.6^\circ\text{C}$, giving $-63.5\text{ kJ/mol}$) or the last reading at $10\text{ min}$ ($\Delta T = 6.4^\circ\text{C}$, giving $-53.5\text{ kJ/mol}$) underestimates the energy released, because heat was already escaping before those readings were taken. Reading the dashed line at $t = 0$ ($29.4^\circ\text{C}$, giving $-70.2\text{ kJ/mol}$) overcorrects, because the salt had not yet been added at that time.",
    },
    {
        "unit_q_num": 55,
        "topic_code": "6.4",
        "topic_title": "Heat Capacity and Calorimetry",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A student uses a coffee-cup calorimeter to determine $\Delta H$ for an exothermic reaction in aqueous solution. The student calculates the heat absorbed by the solution using $q = mc\Delta T$ with $c = 4.18\text{ J/(g}\cdot^\circ\text{C)}$ and then divides by the number of moles of the limiting reactant. Which of the following would cause the magnitude of the student's calculated $\Delta H$ to be greater than the true value?",
        "options": [
            r"Thermal energy escaped through the uncovered top of the calorimeter during the reaction.",
            r"Some of the limiting reactant did not react, but the student calculated the number of moles from the full mass of the limiting reactant added.",
            r"The thermometer was miscalibrated and read $0.5^\circ\text{C}$ higher than the true temperature for every measurement.",
            r"The actual specific heat capacity of the solution was less than $4.18\text{ J/(g}\cdot^\circ\text{C)}$.",
        ],
        "correct_index": 3,
        "explanation": r"The student calculates $|\Delta H| = \frac{mc\Delta T}{n}$. If the actual specific heat capacity of the solution is less than $4.18\text{ J/(g}\cdot^\circ\text{C)}$, the measured $\Delta T$ corresponds to less heat than the student calculates, so $q$, and therefore $|\Delta H|$, is overestimated. Heat escaping through the uncovered top makes the measured $\Delta T$ too small, so the calculated $|\Delta H|$ is too small. If some of the limiting reactant did not react, less heat was released than the student's mole value implies, so $q/n$ is again too small. A thermometer that reads high by the same amount at every temperature does not change $\Delta T$, because the offset cancels in the subtraction, so the result is unaffected.",
    },
    {
        "unit_q_num": 56,
        "topic_code": "6.5",
        "topic_title": "Energy of Phase Changes",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 320" role="img" font-family="sans-serif" aria-label="Cooling curve: temperature in degrees Celsius versus time in minutes. Point U is at 0 minutes and 120 degrees. The temperature falls linearly to point V at 1 minute and 80 degrees, stays constant at 80 degrees until point W at 8 minutes, falls linearly to point X at 11 minutes and 10 degrees, stays constant at 10 degrees until point Y at 13 minutes, and then falls to point Z at 14 minutes and minus 20 degrees.">
<line x1="70" y1="270" x2="490" y2="270" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="256.2" x2="490" y2="256.2" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="242.5" x2="490" y2="242.5" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="228.8" x2="490" y2="228.8" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="215" x2="490" y2="215" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="201.2" x2="490" y2="201.2" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="187.5" x2="490" y2="187.5" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="173.8" x2="490" y2="173.8" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="160" x2="490" y2="160" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="146.2" x2="490" y2="146.2" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="132.5" x2="490" y2="132.5" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="118.8" x2="490" y2="118.8" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="105" x2="490" y2="105" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="91.2" x2="490" y2="91.2" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="77.5" x2="490" y2="77.5" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="63.8" x2="490" y2="63.8" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="50" x2="490" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="270" x2="70" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="100" y1="270" x2="100" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="130" y1="270" x2="130" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="160" y1="270" x2="160" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="190" y1="270" x2="190" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="220" y1="270" x2="220" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="250" y1="270" x2="250" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="280" y1="270" x2="280" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="310" y1="270" x2="310" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="340" y1="270" x2="340" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="370" y1="270" x2="370" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="400" y1="270" x2="400" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="430" y1="270" x2="430" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="460" y1="270" x2="460" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="490" y1="270" x2="490" y2="50" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="270" x2="490" y2="270" stroke="#111827" stroke-width="2"/>
<line x1="70" y1="270" x2="70" y2="50" stroke="#111827" stroke-width="2"/>
<line x1="64" y1="270" x2="70" y2="270" stroke="#111827" stroke-width="1.5"/>
<line x1="64" y1="256.2" x2="70" y2="256.2" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="260.2" font-size="12" text-anchor="end" fill="#111827">−20</text>
<line x1="64" y1="242.5" x2="70" y2="242.5" stroke="#111827" stroke-width="1.5"/>
<line x1="64" y1="228.8" x2="70" y2="228.8" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="232.8" font-size="12" text-anchor="end" fill="#111827">0</text>
<line x1="64" y1="215" x2="70" y2="215" stroke="#111827" stroke-width="1.5"/>
<line x1="64" y1="201.2" x2="70" y2="201.2" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="205.2" font-size="12" text-anchor="end" fill="#111827">20</text>
<line x1="64" y1="187.5" x2="70" y2="187.5" stroke="#111827" stroke-width="1.5"/>
<line x1="64" y1="173.8" x2="70" y2="173.8" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="177.8" font-size="12" text-anchor="end" fill="#111827">40</text>
<line x1="64" y1="160" x2="70" y2="160" stroke="#111827" stroke-width="1.5"/>
<line x1="64" y1="146.2" x2="70" y2="146.2" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="150.2" font-size="12" text-anchor="end" fill="#111827">60</text>
<line x1="64" y1="132.5" x2="70" y2="132.5" stroke="#111827" stroke-width="1.5"/>
<line x1="64" y1="118.8" x2="70" y2="118.8" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="122.8" font-size="12" text-anchor="end" fill="#111827">80</text>
<line x1="64" y1="105" x2="70" y2="105" stroke="#111827" stroke-width="1.5"/>
<line x1="64" y1="91.2" x2="70" y2="91.2" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="95.2" font-size="12" text-anchor="end" fill="#111827">100</text>
<line x1="64" y1="77.5" x2="70" y2="77.5" stroke="#111827" stroke-width="1.5"/>
<line x1="64" y1="63.8" x2="70" y2="63.8" stroke="#111827" stroke-width="1.5"/>
<text x="60" y="67.8" font-size="12" text-anchor="end" fill="#111827">120</text>
<line x1="64" y1="50" x2="70" y2="50" stroke="#111827" stroke-width="1.5"/>
<line x1="70" y1="270" x2="70" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="70" y="291" font-size="12" text-anchor="middle" fill="#111827">0</text>
<line x1="100" y1="270" x2="100" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="100" y="291" font-size="12" text-anchor="middle" fill="#111827">1</text>
<line x1="130" y1="270" x2="130" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="130" y="291" font-size="12" text-anchor="middle" fill="#111827">2</text>
<line x1="160" y1="270" x2="160" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="160" y="291" font-size="12" text-anchor="middle" fill="#111827">3</text>
<line x1="190" y1="270" x2="190" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="190" y="291" font-size="12" text-anchor="middle" fill="#111827">4</text>
<line x1="220" y1="270" x2="220" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="220" y="291" font-size="12" text-anchor="middle" fill="#111827">5</text>
<line x1="250" y1="270" x2="250" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="250" y="291" font-size="12" text-anchor="middle" fill="#111827">6</text>
<line x1="280" y1="270" x2="280" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="280" y="291" font-size="12" text-anchor="middle" fill="#111827">7</text>
<line x1="310" y1="270" x2="310" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="310" y="291" font-size="12" text-anchor="middle" fill="#111827">8</text>
<line x1="340" y1="270" x2="340" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="340" y="291" font-size="12" text-anchor="middle" fill="#111827">9</text>
<line x1="370" y1="270" x2="370" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="370" y="291" font-size="12" text-anchor="middle" fill="#111827">10</text>
<line x1="400" y1="270" x2="400" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="400" y="291" font-size="12" text-anchor="middle" fill="#111827">11</text>
<line x1="430" y1="270" x2="430" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="430" y="291" font-size="12" text-anchor="middle" fill="#111827">12</text>
<line x1="460" y1="270" x2="460" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="460" y="291" font-size="12" text-anchor="middle" fill="#111827">13</text>
<line x1="490" y1="270" x2="490" y2="276" stroke="#111827" stroke-width="1.5"/>
<text x="490" y="291" font-size="12" text-anchor="middle" fill="#111827">14</text>
<polyline points="70,63.8 100,118.8 310,118.8 400,215 460,215 490,256.2" fill="none" stroke="#111827" stroke-width="2.4" stroke-linejoin="round"/>
<circle cx="70" cy="63.8" r="3.2" fill="#111827"/>
<text x="79" y="59.8" font-size="13" text-anchor="start" fill="#111827" font-weight="bold">U</text>
<circle cx="100" cy="118.8" r="3.2" fill="#111827"/>
<text x="100" y="109.8" font-size="13" text-anchor="middle" fill="#111827" font-weight="bold">V</text>
<circle cx="310" cy="118.8" r="3.2" fill="#111827"/>
<text x="310" y="109.8" font-size="13" text-anchor="middle" fill="#111827" font-weight="bold">W</text>
<circle cx="400" cy="215" r="3.2" fill="#111827"/>
<text x="400" y="234" font-size="13" text-anchor="middle" fill="#111827" font-weight="bold">X</text>
<circle cx="460" cy="215" r="3.2" fill="#111827"/>
<text x="460" y="234" font-size="13" text-anchor="middle" fill="#111827" font-weight="bold">Y</text>
<circle cx="490" cy="256.2" r="3.2" fill="#111827"/>
<text x="500" y="260.2" font-size="13" text-anchor="start" fill="#111827" font-weight="bold">Z</text>
<text x="280" y="309" font-size="13" text-anchor="middle" fill="#111827">Time (min)</text>
<text x="22" y="160" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 22 160)">Temperature (°C)</text>
</svg>
<figcaption>Figure: Cooling curve for the sample (thermal energy removed at a constant rate)</figcaption>
</figure>""",
        "question": r"A $0.200\text{ mol}$ sample of a pure substance, initially a gas at $120^\circ\text{C}$, is cooled at a constant pressure of $1\text{ atm}$ by removing thermal energy at a constant rate of $1.00\text{ kJ/min}$. The resulting cooling curve is shown above. Which of the following gives the molar enthalpy of vaporization, $\Delta H_{\text{vap}}$, of the substance and correctly describes the energy of the sample during segment VW?",
        "options": [
            r"$\Delta H_{\text{vap}} = +35.0\text{ kJ/mol}$; the energy of the sample decreases during segment VW.",
            r"$\Delta H_{\text{vap}} = -35.0\text{ kJ/mol}$; the energy of the sample decreases during segment VW.",
            r"$\Delta H_{\text{vap}} = +35.0\text{ kJ/mol}$; the energy of the sample remains constant during segment VW because its temperature is constant.",
            r"$\Delta H_{\text{vap}} = +7.00\text{ kJ/mol}$; the energy of the sample decreases during segment VW.",
        ],
        "correct_index": 0,
        "explanation": r"Segment VW is the plateau at $80^\circ\text{C}$, where the gas condenses. It lasts $8.0 - 1.0 = 7.0\text{ min}$, so the energy removed is $(1.00\text{ kJ/min})(7.0\text{ min}) = 7.0\text{ kJ}$ for $0.200\text{ mol}$, and $\Delta H_{\text{cond}} = \frac{-7.0\text{ kJ}}{0.200\text{ mol}} = -35.0\text{ kJ/mol}$. Vaporization is the reverse of condensation, so $\Delta H_{\text{vap}} = -\Delta H_{\text{cond}} = +35.0\text{ kJ/mol}$; the value $-35.0\text{ kJ/mol}$ is the enthalpy of condensation, and $7.00\text{ kJ/mol}$ results from not dividing by the number of moles. Energy is removed from the sample throughout segment VW, so the energy of the sample decreases even though its temperature is constant: as intermolecular attractions form during condensation, the potential energy of the particles decreases while their average kinetic energy stays the same.",
    },
    {
        "unit_q_num": 57,
        "topic_code": "6.6",
        "topic_title": "Introduction to Enthalpy of Reaction",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"Solutions of $\text{HCl}(aq)$ and $\text{NaOH}(aq)$, both at room temperature ($22.0^\circ\text{C}$), are mixed in an open beaker. The temperature of the mixture quickly rises to $28.5^\circ\text{C}$ and then, over the next hour, gradually returns to $22.0^\circ\text{C}$. Which statement best describes the energy changes during this process?",
        "options": [
            r"The temperature rises because the neutralization absorbs thermal energy from the surroundings, and it falls as the products release that energy back to the surroundings.",
            r"As $\text{H}^+$ and $\text{OH}^-$ ions combine to form water, chemical potential energy is converted into kinetic energy of the particles, raising the temperature; the warmer mixture then transfers thermal energy to the cooler surroundings until thermal equilibrium is reached.",
            r"Because the final temperature equals the initial temperature, the net thermal energy transferred from the reaction to the surroundings is zero.",
            r"The temperature returns to $22.0^\circ\text{C}$ because the reverse reaction gradually converts $\text{H}_2\text{O}(l)$ back into $\text{H}^+(aq)$ and $\text{OH}^-(aq)$, absorbing the energy that was released.",
        ],
        "correct_index": 1,
        "explanation": r"Forming water from $\text{H}^+$ and $\text{OH}^-$ lowers the chemical potential energy of the system; that energy appears as increased kinetic energy of the particles, so the temperature of the mixture rises (an exothermic reaction). The products are then warmer than the room, so collisions transfer thermal energy to the surroundings until the mixture and the room reach the same temperature. By the time the mixture is back at $22.0^\circ\text{C}$, all of the energy released by the reaction has been transferred to the surroundings, so the net heat transferred is not zero; returning to the starting temperature means only that thermal equilibrium has been re-established. A process that absorbs energy from the surroundings would lower, not raise, the temperature of the mixture, and the neutralization does not reverse to any significant extent, so the cooling is due to heat transfer rather than a reverse reaction.",
    },
    {
        "unit_q_num": 58,
        "topic_code": "6.7",
        "topic_title": "Bond Enthalpies",
        "difficulty": "Challenging",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 280" role="img" font-family="sans-serif" aria-label="Enthalpy diagram for the reaction of 2 H2 gas and O2 gas to form 2 H2O gas. The reactant level is in the middle. An upward arrow labeled Step 1 rises from the reactant level to a high level labeled 4 H(g) + 2 O(g). A longer downward arrow labeled Step 2 falls from that high level to the product level, 2 H2O(g), which lies below the reactant level. A short downward arrow labeled Delta H degree goes from the reactant level to the product level.">
<line x1="34" y1="262" x2="34" y2="30" stroke="#111827" stroke-width="2"/>
<polygon points="34,22 29,33 39,33" fill="#111827"/>
<text x="20" y="150" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 20 150)">Enthalpy</text>
<line x1="60" y1="189" x2="200" y2="189" stroke="#111827" stroke-width="2.5"/>
<line x1="185" y1="52" x2="345" y2="52" stroke="#111827" stroke-width="2.5"/>
<line x1="330" y1="237.2" x2="470" y2="237.2" stroke="#111827" stroke-width="2.5"/>
<line x1="200" y1="189" x2="470" y2="189" stroke="#9ca3af" stroke-width="1.5" stroke-dasharray="5 4"/>
<text x="130" y="207" font-size="13" text-anchor="middle" fill="#111827">2 H₂(g) + O₂(g)</text>
<text x="265" y="42" font-size="13" text-anchor="middle" fill="#111827">4 H(g) + 2 O(g)</text>
<text x="400" y="255.2" font-size="13" text-anchor="middle" fill="#111827">2 H₂O(g)</text>
<line x1="192" y1="189" x2="192" y2="61" stroke="#111827" stroke-width="2"/>
<polygon points="192,52 187,63 197,63" fill="#111827"/>
<text x="184" y="124.5" font-size="13" text-anchor="end" fill="#111827" font-weight="bold">Step 1</text>
<line x1="338" y1="52" x2="338" y2="228.2" stroke="#111827" stroke-width="2"/>
<polygon points="338,237.2 333,226.2 343,226.2" fill="#111827"/>
<text x="346" y="148.6" font-size="13" text-anchor="start" fill="#111827" font-weight="bold">Step 2</text>
<line x1="455" y1="189" x2="455" y2="228.2" stroke="#111827" stroke-width="2"/>
<polygon points="455,237.2 450,226.2 460,226.2" fill="#111827"/>
<text x="462" y="217.1" font-size="13" text-anchor="start" fill="#111827">ΔH°</text>
</svg>
<figcaption>Figure: Energy pathway through gaseous atoms (vertical axis drawn to scale)</figcaption>
</figure>
<table class="quiz-data-table"><thead><tr><th>Bond</th><th>Average Bond Enthalpy ($\text{kJ/mol}$)</th></tr></thead><tbody><tr><td>$\text{H}-\text{H}$</td><td>$436$</td></tr><tr><td>$\text{O}=\text{O}$</td><td>$498$</td></tr><tr><td>$\text{O}-\text{H}$</td><td>$463$</td></tr></tbody></table>""",
        "question": r"The diagram represents the reaction $2\,\text{H}_2(g) + \text{O}_2(g) \rightarrow 2\,\text{H}_2\text{O}(g)$ as two steps: in Step 1 all of the bonds in the reactants are broken to form gaseous atoms, and in Step 2 all of the bonds in the products are formed from those atoms. Based on the average bond enthalpies in the table, which of the following gives the enthalpy change for Step 2 and $\Delta H^\circ$ for the overall reaction as written?",
        "options": [
            r"Step 2: $-926\text{ kJ}$; $\Delta H^\circ = +444\text{ kJ/mol}_{\text{rxn}}$",
            r"Step 2: $-1852\text{ kJ}$; $\Delta H^\circ = -241\text{ kJ/mol}_{\text{rxn}}$",
            r"Step 2: $-1852\text{ kJ}$; $\Delta H^\circ = -482\text{ kJ/mol}_{\text{rxn}}$",
            r"Step 2: $+1852\text{ kJ}$; $\Delta H^\circ = +3222\text{ kJ/mol}_{\text{rxn}}$",
        ],
        "correct_index": 2,
        "explanation": r"Step 1 breaks $2$ $\text{H}-\text{H}$ bonds and $1$ $\text{O}=\text{O}$ bond: $2(436) + 498 = +1370\text{ kJ}$ (energy absorbed). Each $\text{H}_2\text{O}$ molecule contains $2$ $\text{O}-\text{H}$ bonds, so Step 2 forms $4$ $\text{O}-\text{H}$ bonds: $-4(463) = -1852\text{ kJ}$ (energy released). Because energy is conserved, the enthalpy change of the overall reaction equals the sum of the steps: $\Delta H^\circ = +1370 + (-1852) = -482\text{ kJ/mol}_{\text{rxn}}$, an exothermic reaction because more energy is released in forming bonds than is absorbed in breaking them. Counting only one $\text{O}-\text{H}$ bond per water molecule gives $-926\text{ kJ}$ and a positive $\Delta H^\circ$. The value $-241\text{ kJ}$ corresponds to forming $1\text{ mol}$ of $\text{H}_2\text{O}$, not to the reaction as written, which forms $2\text{ mol}$. Bond formation always releases energy, so Step 2 cannot be positive.",
    },
    {
        "unit_q_num": 59,
        "topic_code": "6.8",
        "topic_title": "Enthalpy of Formation",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"At $25^\circ\text{C}$, the standard enthalpy of formation of $\text{H}_2\text{O}(l)$ is $-285.8\text{ kJ/mol}$ and that of $\text{H}_2\text{O}(g)$ is $-241.8\text{ kJ/mol}$. How much thermal energy is absorbed when $9.00\text{ g}$ of liquid water ($M = 18.0\text{ g/mol}$) evaporates at $25^\circ\text{C}$?",
        "options": [
            r"$22.0\text{ kJ}$",
            r"$44.0\text{ kJ}$",
            r"$264\text{ kJ}$",
            r"$396\text{ kJ}$",
        ],
        "correct_index": 0,
        "explanation": r"Vaporization, $\text{H}_2\text{O}(l) \rightarrow \text{H}_2\text{O}(g)$, is a physical process whose enthalpy change can be calculated from enthalpies of formation: $\Delta H^\circ = \Delta H_f^\circ[\text{H}_2\text{O}(g)] - \Delta H_f^\circ[\text{H}_2\text{O}(l)] = (-241.8) - (-285.8) = +44.0\text{ kJ/mol}$. The sample contains $\frac{9.00\text{ g}}{18.0\text{ g/mol}} = 0.500\text{ mol}$, so $q = (0.500\text{ mol})(+44.0\text{ kJ/mol}) = +22.0\text{ kJ}$ is absorbed. The value $44.0\text{ kJ}$ is the energy for $1\text{ mol}$ rather than $0.500\text{ mol}$; $264\text{ kJ}$ results from adding the magnitudes of the two enthalpies of formation instead of subtracting reactant from product; and $396\text{ kJ}$ results from multiplying $44.0\text{ kJ/mol}$ by the mass in grams instead of by the number of moles.",
    },
    {
        "unit_q_num": 60,
        "topic_code": "6.9",
        "topic_title": "Hess's Law",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Reaction</th><th>Equation</th><th>Enthalpy Change</th></tr></thead><tbody><tr><td>1</td><td>$\text{Mg}(s) + 2\,\text{HCl}(aq) \rightarrow \text{MgCl}_2(aq) + \text{H}_2(g)$</td><td>$\Delta H_1$ (measured)</td></tr><tr><td>2</td><td>$\text{MgO}(s) + 2\,\text{HCl}(aq) \rightarrow \text{MgCl}_2(aq) + \text{H}_2\text{O}(l)$</td><td>$\Delta H_2$ (measured)</td></tr><tr><td>3</td><td>$\text{H}_2(g) + \frac{1}{2}\,\text{O}_2(g) \rightarrow \text{H}_2\text{O}(l)$</td><td>$\Delta H_3 = -286\text{ kJ/mol}_{\text{rxn}}$ (accepted value)</td></tr></tbody></table>""",
        "question": r"A student determines the enthalpy of formation of $\text{MgO}(s)$, the enthalpy change for $\text{Mg}(s) + \frac{1}{2}\,\text{O}_2(g) \rightarrow \text{MgO}(s)$, by combining $\Delta H_1$ and $\Delta H_2$, each measured in a coffee-cup calorimeter, with the accepted value of $\Delta H_3$, as shown in the table above. Suppose that during the trial for reaction 2 only, some thermal energy escaped from the calorimeter to the room. How would this error affect the student's calculated enthalpy of formation of $\text{MgO}(s)$?",
        "options": [
            r"It would be less negative than the true value, because heat lost to the surroundings always makes a calculated enthalpy change less exothermic.",
            r"It would be unaffected, because the error in reaction 2 cancels when $\text{MgCl}_2(aq)$ and $\text{HCl}(aq)$ cancel in the sum of the equations.",
            r"It would be more negative than the true value, because the measured $\Delta H_2$ is less negative than the true value and reaction 2 must be reversed in the calculation.",
            r"It would be less negative than the true value, because the measured $\Delta H_2$ is more negative than the true value.",
        ],
        "correct_index": 2,
        "explanation": r"The target equation is the sum of reaction 1, the reverse of reaction 2, and reaction 3 ($\text{MgCl}_2(aq)$, $\text{HCl}(aq)$, $\text{H}_2(g)$, and $\text{H}_2\text{O}(l)$ all cancel), so $\Delta H_f = \Delta H_1 - \Delta H_2 + \Delta H_3$. Heat escaping during reaction 2 makes the measured temperature rise too small, so the measured $\Delta H_2$ is less negative than the true value. Because reaction 2 is reversed, the term $-\Delta H_2$ is then too small a positive number, and the calculated $\Delta H_f$ is more negative than the true value. For example, with $\Delta H_1 = -467\text{ kJ/mol}_{\text{rxn}}$ and a true $\Delta H_2 = -151\text{ kJ/mol}_{\text{rxn}}$, $\Delta H_f = -467 + 151 - 286 = -602\text{ kJ/mol}$, but a measured $\Delta H_2$ of $-140\text{ kJ/mol}_{\text{rxn}}$ gives $-467 + 140 - 286 = -613\text{ kJ/mol}$. The error does not cancel: cancelling species in the equations does not cancel errors in measured $\Delta H$ values, and heat loss makes the measured $\Delta H_2$ less negative, not more negative.",
    },
]
