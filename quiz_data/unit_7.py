UNIT_META = {
    "id": 7,
    "title": "Unit 7: Equilibrium",
    "short_title": "Chemical & Solubility Equilibrium",
    "exam_weight": "7–9%",
    "color": "#0d9488",
    "description": "Reversible reactions and dynamic equilibrium, reaction quotient Q vs. equilibrium constant K (Kc and Kp), ICE tables, magnitude and manipulation of K, particulate and graphical representations of equilibrium, Le Châtelier's Principle (concentration, pressure/volume, temperature, dilution), solubility product Ksp, molar solubility, and the common-ion effect. (Per the Fall 2024 CED, pH and solubility is now Topic 8.11 and free energy of dissolution is Topic 9.6.)",
    "topics": [
        {"code": "7.1", "title": "Introduction to Equilibrium"},
        {"code": "7.2", "title": "Direction of Reversible Reactions"},
        {"code": "7.3", "title": "Reaction Quotient and Equilibrium Constant"},
        {"code": "7.4", "title": "Calculating the Equilibrium Constant"},
        {"code": "7.5", "title": "Magnitude of the Equilibrium Constant"},
        {"code": "7.6", "title": "Properties of the Equilibrium Constant"},
        {"code": "7.7", "title": "Calculating Equilibrium Concentrations"},
        {"code": "7.8", "title": "Representations of Equilibrium"},
        {"code": "7.9", "title": "Introduction to Le Châtelier's Principle"},
        {"code": "7.10", "title": "Reaction Quotient and Le Châtelier's Principle"},
        {"code": "7.11", "title": "Introduction to Solubility Equilibria"},
        {"code": "7.12", "title": "Common-Ion Effect"},
    ],
}

QUESTIONS = [
    # -------------------------------------------------------------------------
    # Topic 7.1: Introduction to Equilibrium (Q1 - Q3)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 1,
        "topic_code": "7.1",
        "topic_title": "Introduction to Equilibrium",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{N}_2\\text{O}_4(g) \\rightleftharpoons 2\\,\\text{NO}_2(g)$"
            "</div>"
        ),
        "question": (
            "Colorless $\\text{N}_2\\text{O}_4(g)$ is placed in a rigid, evacuated glass bulb at a constant temperature "
            "and allowed to decompose into brown $\\text{NO}_2(g)$ according to the equation above. After several minutes, "
            "the intensity of the brown color inside the bulb stops changing and remains constant. Which of the following "
            "statements best describes the system once the color becomes constant?"
        ),
        "options": [
            "The concentrations of $\\text{N}_2\\text{O}_4(g)$ and $\\text{NO}_2(g)$ have become equal.",
            "The forward reaction has stopped completely because all limiting reactant has been consumed.",
            "The rate of decomposition of $\\text{N}_2\\text{O}_4(g)$ is equal to the rate of dimerization of $\\text{NO}_2(g)$.",
            "The forward rate constant $k_f$ has become equal to the reverse rate constant $k_r$.",
        ],
        "correct_index": 2,
        "explanation": (
            "Chemical equilibrium is dynamic: both the forward reaction (decomposition of $\\text{N}_2\\text{O}_4$) and "
            "the reverse reaction (dimerization of $\\text{NO}_2$) continue to occur at equal macroscopic rates "
            "($\\text{Rate}_f = \\text{Rate}_r$), resulting in constant concentrations and constant color intensity. "
            "At equilibrium, reactant and product concentrations are constant, not necessarily equal, and $k_f$ need not equal $k_r$."
        ),
    },
    {
        "unit_q_num": 2,
        "topic_code": "7.1",
        "topic_title": "Introduction to Equilibrium",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Time ($\\text{s}$)</th><th>$[\\text{X}]$ ($\\text{M}$)</th><th>$[\\text{Y}]$ ($\\text{M}$)</th></tr></thead>"
            "<tbody>"
            "<tr><td>0</td><td>1.00</td><td>0.00</td></tr>"
            "<tr><td>20</td><td>0.68</td><td>0.64</td></tr>"
            "<tr><td>40</td><td>0.52</td><td>0.96</td></tr>"
            "<tr><td>60</td><td>0.44</td><td>1.12</td></tr>"
            "<tr><td>80</td><td>0.40</td><td>1.20</td></tr>"
            "<tr><td>100</td><td>0.40</td><td>1.20</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Reactant $\\text{X}(g)$ converts reversibly into product $\\text{Y}(g)$ in a closed rigid container at constant "
            "temperature. Based on the concentration data in the table above, which of the following gives the balanced "
            "chemical equation and the time at which the system first reaches chemical equilibrium?"
        ),
        "options": [
            "$\\text{X}(g) \\rightleftharpoons \\text{Y}(g)$; equilibrium is reached at $t = 40\\text{ s}$.",
            "$\\text{X}(g) \\rightleftharpoons 2\\,\\text{Y}(g)$; equilibrium is reached by $t = 80\\text{ s}$.",
            "$2\\,\\text{X}(g) \\rightleftharpoons \\text{Y}(g)$; equilibrium is reached by $t = 80\\text{ s}$.",
            "$\\text{X}(g) \\rightleftharpoons 3\\,\\text{Y}(g)$; equilibrium is reached at $t = 100\\text{ s}$.",
        ],
        "correct_index": 1,
        "explanation": (
            "From $t = 0$ to $t = 80\\text{ s}$, $\\Delta[\\text{X}] = 1.00 - 0.40 = -0.60\\text{ M}$ while "
            "$\\Delta[\\text{Y}] = 1.20 - 0.00 = +1.20\\text{ M}$. Because $2\\text{ mol}$ of $\\text{Y}$ form for every "
            "$1\\text{ mol}$ of $\\text{X}$ consumed at every time interval, the balanced equation is "
            "$\\text{X}(g) \\rightleftharpoons 2\\,\\text{Y}(g)$. Concentrations cease changing at $t = 80\\text{ s}$, "
            "indicating that equilibrium is established by $t = 80\\text{ s}$."
        ),
    },
    {
        "unit_q_num": 3,
        "topic_code": "7.1",
        "topic_title": "Introduction to Equilibrium",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": (
            "A saturated aqueous solution of $\\text{PbCl}_2(s)$ is in contact with excess undissolved $\\text{PbCl}_2(s)$ "
            "at the bottom of a sealed beaker at $25^\\circ\\text{C}$. A tiny crystal of $\\text{PbCl}_2(s)$ prepared with "
            "radioactive chlorine-36, $\\text{Pb}({}^{36}\\text{Cl})_2(s)$, is added to the beaker without changing the "
            "temperature. After 24 hours, where will the radioactive ${}^{36}\\text{Cl}^-$ ions be found?"
        ),
        "options": [
            "Exclusively in the solid phase at the bottom of the beaker, because the solution is already saturated.",
            "Exclusively in the aqueous solution, because added crystals dissolve completely by displacing unlabeled ions.",
            "Neither in the solid nor in the solution, because isotopic substitution prevents dissolution.",
            "Distributed between both the aqueous solution and the solid precipitate, while the total mass of solid remains constant.",
        ],
        "correct_index": 3,
        "explanation": (
            "In a saturated solution in contact with excess solid, dissolution and precipitation occur simultaneously "
            "at equal rates ($\\text{PbCl}_2(s) \\rightleftharpoons \\text{Pb}^{2+}(aq) + 2\\,\\text{Cl}^-(aq)$). "
            "Because of this dynamic exchange, ${}^{36}\\text{Cl}^-$ ions from the solid continuously dissolve into solution "
            "while $\\text{Cl}^-$ ions from solution precipitate onto the solid, distributing ${}^{36}\\text{Cl}^-$ across both phases. "
            "Because the two rates are equal, the total mass of undissolved solid remains constant."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 7.2: Direction of Reversible Reactions (Q4 - Q6)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 4,
        "topic_code": "7.2",
        "topic_title": "Direction of Reversible Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$2\\,\\text{SO}_2(g) + \\text{O}_2(g) \\rightleftharpoons 2\\,\\text{SO}_3(g) \\quad K_c = 280\\text{ at } 1000\\text{ K}$"
            "</div>"
        ),
        "question": (
            "At $1000\\text{ K}$, a $2.0\\text{ L}$ rigid vessel is charged with $0.40\\text{ mol}$ of $\\text{SO}_2(g)$, "
            "$0.20\\text{ mol}$ of $\\text{O}_2(g)$, and $4.0\\text{ mol}$ of $\\text{SO}_3(g)$. Which of the following "
            "correctly predicts the direction in which the reaction will proceed to reach equilibrium and provides a valid justification?"
        ),
        "options": [
            "The reaction will proceed in the forward direction because $Q_c = 100 < K_c$.",
            "The reaction will proceed in the reverse direction because $Q_c = 1000 > K_c$.",
            "The reaction will proceed in the reverse direction because $Q_c = 500 > K_c$.",
            "The system is already at equilibrium because $Q_c = 280 = K_c$.",
        ],
        "correct_index": 1,
        "explanation": (
            "First calculate the initial molar concentrations in the $2.0\\text{ L}$ vessel: "
            "$[\\text{SO}_2] = 0.40 / 2.0 = 0.20\\text{ M}$, $[\\text{O}_2] = 0.20 / 2.0 = 0.10\\text{ M}$, and "
            "$[\\text{SO}_3] = 4.0 / 2.0 = 2.0\\text{ M}$. Next evaluate the reaction quotient: "
            "$Q_c = \\frac{[\\text{SO}_3]^2}{[\\text{SO}_2]^2[\\text{O}_2]} = \\frac{(2.0)^2}{(0.20)^2(0.10)} = \\frac{4.0}{0.0040} = 1000$. "
            "Since $Q_c = 1000 > K_c = 280$, the ratio of products to reactants is too large, so the net reaction proceeds in the reverse direction."
        ),
    },
    {
        "unit_q_num": 5,
        "topic_code": "7.2",
        "topic_title": "Direction of Reversible Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            "For an elementary reversible reaction $\\text{A}(g) + \\text{B}(g) \\rightleftharpoons \\text{C}(g)$, "
            "at a certain moment in a closed container the forward reaction rate is greater than the reverse reaction rate "
            "($\\text{Rate}_f > \\text{Rate}_r$). Which of the following must be true at that moment?"
        ),
        "options": [
            "$Q_c < K_c$, and the concentration of $\\text{C}(g)$ is increasing over time.",
            "$Q_c > K_c$, and the concentration of $\\text{C}(g)$ is increasing over time.",
            "$Q_c < K_c$, and the forward reaction rate is increasing over time.",
            "$Q_c = K_c$, because the reaction is elementary.",
        ],
        "correct_index": 0,
        "explanation": (
            "When $\\text{Rate}_f > \\text{Rate}_r$, reactants are converted to products faster than products revert to reactants. "
            "Therefore, there is a net forward reaction, $[\\text{C}]$ is increasing, and $Q_c < K_c$. As reactants are consumed, "
            "$\\text{Rate}_f$ decreases while $\\text{Rate}_r$ increases until $\\text{Rate}_f = \\text{Rate}_r$ and $Q_c = K_c$."
        ),
    },
    {
        "unit_q_num": 6,
        "topic_code": "7.2",
        "topic_title": "Direction of Reversible Reactions",
        "difficulty": "Challenging",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{CO}(g) + \\text{H}_2\\text{O}(g) \\rightleftharpoons \\text{CO}_2(g) + \\text{H}_2(g) \\quad K_p = 4.00\\text{ at } 700\\text{ K}$"
            "</div>"
        ),
        "question": (
            "A rigid vessel at $700\\text{ K}$ initially contains $\\text{CO}(g)$, $\\text{H}_2\\text{O}(g)$, "
            "$\\text{CO}_2(g)$, and $\\text{H}_2(g)$, each at a partial pressure of $1.50\\text{ atm}$. As the system "
            "approaches equilibrium at constant temperature, how do the partial pressure of $\\text{CO}(g)$ and the total "
            "pressure inside the vessel change?"
        ),
        "options": [
            "$P_{\\text{CO}}$ decreases and $P_{\\text{total}}$ increases.",
            "$P_{\\text{CO}}$ increases and $P_{\\text{total}}$ remains constant.",
            "$P_{\\text{CO}}$ remains constant because all initial partial pressures are equal.",
            "$P_{\\text{CO}}$ decreases and $P_{\\text{total}}$ remains constant.",
        ],
        "correct_index": 3,
        "explanation": (
            "Calculate $Q_p$: $Q_p = \\frac{P_{\\text{CO}_2} P_{\\text{H}_2}}{P_{\\text{CO}} P_{\\text{H}_2\\text{O}}} = "
            "\\frac{(1.50)(1.50)}{(1.50)(1.50)} = 1.00$. Since $Q_p = 1.00 < K_p = 4.00$, the reaction proceeds in the forward "
            "direction, consuming $\\text{CO}(g)$ so $P_{\\text{CO}}$ decreases. Because $2\\text{ mol}$ of gas react to form "
            "$2\\text{ mol}$ of gas ($\\Delta n_{\\text{gas}} = 0$), the total number of moles of gas and $P_{\\text{total}}$ ($6.00\\text{ atm}$) remain constant."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 7.3: Reaction Quotient and Equilibrium Constant (Q7 - Q10)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 7,
        "topic_code": "7.3",
        "topic_title": "Reaction Quotient and Equilibrium Constant",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{Fe}_3\\text{O}_4(s) + 4\\,\\text{H}_2(g) \\rightleftharpoons 3\\,\\text{Fe}(s) + 4\\,\\text{H}_2\\text{O}(g)$"
            "</div>"
        ),
        "question": (
            "Which of the following is the correct equilibrium constant expression $K_c$ for the heterogeneous "
            "equilibrium shown above?"
        ),
        "options": [
            "$K_c = \\frac{[\\text{Fe}]^3[\\text{H}_2\\text{O}]^4}{[\\text{Fe}_3\\text{O}_4][\\text{H}_2]^4}$",
            "$K_c = \\frac{[\\text{H}_2\\text{O}]^4}{[\\text{H}_2]^4}$",
            "$K_c = \\frac{[\\text{H}_2]^4}{[\\text{H}_2\\text{O}]^4}$",
            "$K_c = \\frac{4[\\text{H}_2\\text{O}]}{4[\\text{H}_2]}$",
        ],
        "correct_index": 1,
        "explanation": (
            "Pure solids ($\\text{Fe}_3\\text{O}_4(s)$ and $\\text{Fe}(s)$) and pure liquids have unit activity ($a = 1$) "
            "and are omitted from reaction quotient and equilibrium constant expressions. Only the gaseous species "
            "$\\text{H}_2\\text{O}(g)$ and $\\text{H}_2(g)$ raised to their stoichiometric coefficients appear: "
            "$K_c = \\frac{[\\text{H}_2\\text{O}]^4}{[\\text{H}_2]^4}$."
        ),
    },
    {
        "unit_q_num": 8,
        "topic_code": "7.3",
        "topic_title": "Reaction Quotient and Equilibrium Constant",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$2\\,\\text{NO}(g) + \\text{Cl}_2(g) \\rightleftharpoons 2\\,\\text{NOCl}(g)$"
            "</div>"
        ),
        "question": (
            "Which of the following gives the correct expression for the pressure-based reaction quotient $Q_p$ "
            "for the reaction above?"
        ),
        "options": [
            "$Q_p = \\frac{P_{\\text{NOCl}}}{P_{\\text{NO}} \\cdot P_{\\text{Cl}_2}}$",
            "$Q_p = \\frac{2\\,P_{\\text{NOCl}}}{2\\,P_{\\text{NO}} \\cdot P_{\\text{Cl}_2}}$",
            "$Q_p = \\frac{(P_{\\text{NOCl}})^2}{(P_{\\text{NO}})^2 \\cdot P_{\\text{Cl}_2}}$",
            "$Q_p = \\frac{(P_{\\text{NO}})^2 \\cdot P_{\\text{Cl}_2}}{(P_{\\text{NOCl}})^2}$",
        ],
        "correct_index": 2,
        "explanation": (
            "For a gas-phase reaction, $Q_p$ is written with the partial pressures of the gaseous products in the numerator "
            "and the partial pressures of the gaseous reactants in the denominator, each raised to the power of its stoichiometric "
            "coefficient in the balanced equation: $Q_p = \\frac{(P_{\\text{NOCl}})^2}{(P_{\\text{NO}})^2(P_{\\text{Cl}_2})}$."
        ),
    },
    {
        "unit_q_num": 9,
        "topic_code": "7.3",
        "topic_title": "Reaction Quotient and Equilibrium Constant",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{CH}_3\\text{COOH}(aq) + \\text{H}_2\\text{O}(l) \\rightleftharpoons \\text{CH}_3\\text{COO}^-(aq) + \\text{H}_3\\text{O}^+(aq)$"
            "</div>"
        ),
        "question": (
            "Why is $[\\text{H}_2\\text{O}]$ omitted from the equilibrium constant expression $K_c$ for the ionization of "
            "acetic acid in dilute aqueous solution shown above?"
        ),
        "options": [
            "Water is a product of neutralization rather than a reactant in acid ionization.",
            "Water has a molar mass that is much smaller than that of acetic acid.",
            "As a pure liquid solvent in a dilute solution, the activity of water is essentially constant and equal to 1.",
            "Water molecules do not collide with $\\text{CH}_3\\text{COOH}$ molecules during the forward reaction.",
        ],
        "correct_index": 2,
        "explanation": (
            "In thermodynamic equilibrium expressions, each species is represented by its activity relative to a standard state. "
            "For a pure liquid (or solvent in a dilute solution), the concentration ($\\approx 55.5\\text{ M}$ for water) remains "
            "virtually constant, so its activity is close to $1$ and is incorporated into the constant $K_c$."
        ),
    },
    {
        "unit_q_num": 10,
        "topic_code": "7.3",
        "topic_title": "Reaction Quotient and Equilibrium Constant",
        "difficulty": "Challenging",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{Zn}(s) + 2\\,\\text{Ag}^+(aq) \\rightleftharpoons \\text{Zn}^{2+}(aq) + 2\\,\\text{Ag}(s)$"
            "</div>"
        ),
        "question": (
            "At $25^\\circ\\text{C}$, a strip of $\\text{Zn}(s)$ is immersed in a solution containing $0.10\\text{ M } \\text{AgNO}_3(aq)$ "
            "and $0.30\\text{ M } \\text{Zn(NO}_3)_2(aq)$. What is the initial value of the reaction quotient $Q_c$ for the net "
            "ionic reaction shown above?"
        ),
        "options": [
            "$0.33$",
            "$3.0$",
            "$9.0$",
            "$30$",
        ],
        "correct_index": 3,
        "explanation": (
            "Omitting pure solids $\\text{Zn}(s)$ and $\\text{Ag}(s)$, the reaction quotient expression is "
            "$Q_c = \\frac{[\\text{Zn}^{2+}]}{[\\text{Ag}^+]^2}$. Substituting $[\\text{Zn}^{2+}] = 0.30\\text{ M}$ and "
            "$[\\text{Ag}^+] = 0.10\\text{ M}$ gives $Q_c = \\frac{0.30}{(0.10)^2} = \\frac{0.30}{0.010} = 30$."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 7.4: Calculating the Equilibrium Constant (Q11 - Q14)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 11,
        "topic_code": "7.4",
        "topic_title": "Calculating the Equilibrium Constant",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{PCl}_5(g) \\rightleftharpoons \\text{PCl}_3(g) + \\text{Cl}_2(g)$"
            "</div>"
        ),
        "question": (
            "A $2.00\\text{ L}$ evacuated flask is filled with $1.00\\text{ mol}$ of $\\text{PCl}_5(g)$ and heated to $523\\text{ K}$. "
            "At equilibrium, the flask is found to contain $0.40\\text{ mol}$ of $\\text{Cl}_2(g)$. What is the value of "
            "$K_c$ for the decomposition of $\\text{PCl}_5(g)$ at $523\\text{ K}$?"
        ),
        "options": [
            "$0.13$",
            "$0.27$",
            "$0.53$",
            "$0.67$",
        ],
        "correct_index": 0,
        "explanation": (
            "In the $2.00\\text{ L}$ flask, the initial concentration of $\\text{PCl}_5$ is $[\\text{PCl}_5]_0 = 1.00 / 2.00 = 0.50\\text{ M}$. "
            "At equilibrium, $[\\text{Cl}_2] = 0.40 / 2.00 = 0.20\\text{ M}$. By $1:1:1$ stoichiometry, $[\\text{PCl}_3] = 0.20\\text{ M}$ "
            "and $[\\text{PCl}_5] = 0.50 - 0.20 = 0.30\\text{ M}$. Therefore, "
            "$K_c = \\frac{[\\text{PCl}_3][\\text{Cl}_2]}{[\\text{PCl}_5]} = \\frac{(0.20)(0.20)}{0.30} = \\frac{0.040}{0.30} = 0.133 \\approx 0.13$."
        ),
    },
    {
        "unit_q_num": 12,
        "topic_code": "7.4",
        "topic_title": "Calculating the Equilibrium Constant",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Species</th><th>Initial Partial Pressure ($\\text{atm}$)</th><th>Equilibrium Partial Pressure ($\\text{atm}$)</th></tr></thead>"
            "<tbody>"
            "<tr><td>$\\text{N}_2(g)$</td><td>$1.00$</td><td>$?$</td></tr>"
            "<tr><td>$\\text{H}_2(g)$</td><td>$3.00$</td><td>$?$</td></tr>"
            "<tr><td>$\\text{NH}_3(g)$</td><td>$0.00$</td><td>$0.80$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Nitrogen and hydrogen react in a rigid container at constant temperature according to the equation "
            "$\\text{N}_2(g) + 3\\,\\text{H}_2(g) \\rightleftharpoons 2\\,\\text{NH}_3(g)$. Based on the pressure data in the "
            "table above, what is the value of $K_p$ at this temperature?"
        ),
        "options": [
            "$K_p = \\frac{(0.80)^2}{(0.60)(1.80)^3}$",
            "$K_p = \\frac{(0.80)^2}{(0.20)(2.20)^3}$",
            "$K_p = \\frac{(0.80)^2}{(0.60)(2.60)^3}$",
            "$K_p = \\frac{0.80}{(0.60)(1.80)}$",
        ],
        "correct_index": 0,
        "explanation": (
            "Since $P_{\\text{NH}_3}$ increases by $+2x = 0.80\\text{ atm}$, we have $x = 0.40\\text{ atm}$. "
            "At equilibrium, $P_{\\text{N}_2} = 1.00 - x = 1.00 - 0.40 = 0.60\\text{ atm}$, and "
            "$P_{\\text{H}_2} = 3.00 - 3x = 3.00 - 3(0.40) = 1.80\\text{ atm}$. "
            "Substituting into $K_p = \\frac{(P_{\\text{NH}_3})^2}{(P_{\\text{N}_2})(P_{\\text{H}_2})^3}$ gives "
            "$\\frac{(0.80)^2}{(0.60)(1.80)^3}$."
        ),
    },
    {
        "unit_q_num": 13,
        "topic_code": "7.4",
        "topic_title": "Calculating the Equilibrium Constant",
        "difficulty": "Challenging",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{NH}_4\\text{HS}(s) \\rightleftharpoons \\text{NH}_3(g) + \\text{H}_2\\text{S}(g)$"
            "</div>"
        ),
        "question": (
            "Excess solid $\\text{NH}_4\\text{HS}$ is placed in an evacuated rigid container at $25^\\circ\\text{C}$ and allowed "
            "to decompose according to the equation above. At equilibrium, the total gas pressure inside the container is "
            "$0.660\\text{ atm}$. What is the value of $K_p$ for this reaction at $25^\\circ\\text{C}$?"
        ),
        "options": [
            "$0.109$",
            "$0.218$",
            "$0.330$",
            "$0.436$",
        ],
        "correct_index": 0,
        "explanation": (
            "Because $\\text{NH}_4\\text{HS}(s)$ is the only source of gas and decomposes in a $1:1$ molar ratio into "
            "$\\text{NH}_3(g)$ and $\\text{H}_2\\text{S}(g)$, at equilibrium $P_{\\text{NH}_3} = P_{\\text{H}_2\\text{S}} = "
            "\\frac{1}{2} P_{\\text{total}} = \\frac{0.660}{2} = 0.330\\text{ atm}$. "
            "Omitting the pure solid, $K_p = P_{\\text{NH}_3} \\cdot P_{\\text{H}_2\\text{S}} = (0.330)(0.330) = 0.1089 \\approx 0.109$."
        ),
    },
    {
        "unit_q_num": 14,
        "topic_code": "7.4",
        "topic_title": "Calculating the Equilibrium Constant",
        "difficulty": "Challenging",
        "stimulus": (
            '<div class="quiz-equation">'
            "$2\\,\\text{A}(g) \\rightleftharpoons \\text{B}(g)$"
            "</div>"
        ),
        "question": (
            "A rigid container is initially filled with pure gas $\\text{A}$ at a pressure of $4.00\\text{ atm}$ at constant "
            "temperature $T$. When the reaction above reaches equilibrium, the total pressure in the container has decreased "
            "to $3.00\\text{ atm}$. What is the value of $K_p$ at temperature $T$?"
        ),
        "options": [
            "$1.00$",
            "$0.75$",
            "$0.50$",
            "$0.25$",
        ],
        "correct_index": 3,
        "explanation": (
            "Set up an ICE table in terms of partial pressure (atm): initial $P_{\\text{A}} = 4.00$, $P_{\\text{B}} = 0$. "
            "Let the change be $-2x$ for $\\text{A}$ and $+x$ for $\\text{B}$. At equilibrium, $P_{\\text{A}} = 4.00 - 2x$ and "
            "$P_{\\text{B}} = x$. The total pressure is $P_{\\text{total}} = (4.00 - 2x) + x = 4.00 - x = 3.00\\text{ atm}$, "
            "so $x = 1.00\\text{ atm}$. Thus, at equilibrium, $P_{\\text{A}} = 4.00 - 2(1.00) = 2.00\\text{ atm}$ and "
            "$P_{\\text{B}} = 1.00\\text{ atm}$. Therefore, $K_p = \\frac{P_{\\text{B}}}{(P_{\\text{A}})^2} = \\frac{1.00}{(2.00)^2} = 0.25$."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 7.5: Magnitude of the Equilibrium Constant (Q15 - Q17)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 15,
        "topic_code": "7.5",
        "topic_title": "Magnitude of the Equilibrium Constant",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Acid</th><th>Ionization Equation</th><th>$K_a$ at $25^\\circ\\text{C}$</th></tr></thead>"
            "<tbody>"
            "<tr><td>Hydrofluoric acid</td><td>$\\text{HF}(aq) \\rightleftharpoons \\text{H}^+(aq) + \\text{F}^-(aq)$</td><td>$6.8 \\times 10^{-4}$</td></tr>"
            "<tr><td>Acetic acid</td><td>$\\text{CH}_3\\text{COOH}(aq) \\rightleftharpoons \\text{H}^+(aq) + \\text{CH}_3\\text{COO}^-(aq)$</td><td>$1.8 \\times 10^{-5}$</td></tr>"
            "<tr><td>Hydrocyanic acid</td><td>$\\text{HCN}(aq) \\rightleftharpoons \\text{H}^+(aq) + \\text{CN}^-(aq)$</td><td>$6.2 \\times 10^{-10}$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "If separate $0.10\\text{ M}$ aqueous solutions of $\\text{HF}$, $\\text{CH}_3\\text{COOH}$, and $\\text{HCN}$ "
            "are prepared at $25^\\circ\\text{C}$, which of the following correctly lists the three solutions in order of "
            "increasing equilibrium concentration of unionized acid molecules?"
        ),
        "options": [
            "$\\text{HCN} < \\text{CH}_3\\text{COOH} < \\text{HF}$",
            "$\\text{HF} < \\text{CH}_3\\text{COOH} < \\text{HCN}$",
            "$\\text{CH}_3\\text{COOH} < \\text{HF} < \\text{HCN}$",
            "All three have the exact same concentration of unionized acid because all three have $K_a < 1$.",
        ],
        "correct_index": 1,
        "explanation": (
            "A larger $K_a$ value indicates a greater extent of forward reaction (ionization) at equilibrium. "
            "Since $K_a(\\text{HF}) > K_a(\\text{CH}_3\\text{COOH}) > K_a(\\text{HCN})$, $\\text{HF}$ ionizes to the greatest extent "
            "and therefore has the smallest equilibrium concentration of unionized acid $[\\text{HA}]$, whereas $\\text{HCN}$ ionizes "
            "the least and retains the largest concentration of unionized acid: $[\\text{HF}] < [\\text{CH}_3\\text{COOH}] < [\\text{HCN}]$."
        ),
    },
    {
        "unit_q_num": 16,
        "topic_code": "7.5",
        "topic_title": "Magnitude of the Equilibrium Constant",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$2\\,\\text{H}_2(g) + \\text{O}_2(g) \\rightleftharpoons 2\\,\\text{H}_2\\text{O}(g) \\quad K_p = 1.2 \\times 10^{80}\\text{ at } 298\\text{ K}$"
            "</div>"
        ),
        "question": (
            "When $\\text{H}_2(g)$ and $\\text{O}_2(g)$ are mixed in a sealed bulb at $298\\text{ K}$ in the absence of a "
            "catalyst or spark, no measurable amount of $\\text{H}_2\\text{O}(g)$ is formed even after several days. "
            "Which of the following best explains this observation?"
        ),
        "options": [
            "A very large $K_p$ value indicates that the reverse reaction is thermodynamically favored.",
            "At $298\\text{ K}$, $Q_p$ is initially much larger than $K_p$, preventing any forward reaction.",
            "Gas-phase reactions with $\\Delta n_{\\text{gas}} < 0$ cannot occur without external compression.",
            "The magnitude of $K_p$ describes the equilibrium position, which strongly favors products, but provides no information about the activation energy or rate of reaction.",
        ],
        "correct_index": 3,
        "explanation": (
            "Because $K_p = 1.2 \\times 10^{80} \\gg 1$, the equilibrium mixture consists almost entirely of products "
            "(the reaction is strongly thermodynamically favored). However, the magnitude of $K$ is a thermodynamic quantity "
            "and says nothing about kinetics; the reaction has a very high activation energy $E_a$ and thus an extremely slow rate at $298\\text{ K}$."
        ),
    },
    {
        "unit_q_num": 17,
        "topic_code": "7.5",
        "topic_title": "Magnitude of the Equilibrium Constant",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{N}_2(g) + \\text{O}_2(g) \\rightleftharpoons 2\\,\\text{NO}(g) \\quad K_c = 4.1 \\times 10^{-31}\\text{ at } 298\\text{ K}$"
            "</div>"
        ),
        "question": (
            "Based on the value of $K_c$ for the reaction above at $298\\text{ K}$, which of the following statements is "
            "correct regarding an equilibrium mixture of $\\text{N}_2(g)$, $\\text{O}_2(g)$, and $\\text{NO}(g)$ at $298\\text{ K}$?"
        ),
        "options": [
            "The equilibrium constant for the decomposition $2\\,\\text{NO}(g) \\rightleftharpoons \\text{N}_2(g) + \\text{O}_2(g)$ at $298\\text{ K}$ is $2.4 \\times 10^{30}$, meaning $\\text{NO}(g)$ is thermodynamically unstable with respect to decomposition.",
            "The equilibrium mixture contains predominantly $\\text{NO}(g)$ and negligible amounts of $\\text{N}_2(g)$ and $\\text{O}_2(g)$.",
            "The forward reaction rate constant $k_f$ must be much larger than the reverse rate constant $k_r$.",
            "Equal molar amounts of $\\text{N}_2(g)$, $\\text{O}_2(g)$, and $\\text{NO}(g)$ coexist at equilibrium.",
        ],
        "correct_index": 0,
        "explanation": (
            "Since $K_c = 4.1 \\times 10^{-31} \\ll 1$, reactants ($\\text{N}_2$ and $\\text{O}_2$) are overwhelmingly favored at equilibrium. "
            "For the reverse reaction ($2\\,\\text{NO}(g) \\rightleftharpoons \\text{N}_2(g) + \\text{O}_2(g)$), "
            "$K_c' = \\frac{1}{4.1 \\times 10^{-31}} = 2.4 \\times 10^{30} \\gg 1$, showing that decomposition of $\\text{NO}$ into "
            "$\\text{N}_2$ and $\\text{O}_2$ is strongly favored thermodynamically at $298\\text{ K}$."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 7.6: Properties of the Equilibrium Constant (Q18 - Q21)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 18,
        "topic_code": "7.6",
        "topic_title": "Properties of the Equilibrium Constant",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{N}_2(g) + 3\\,\\text{H}_2(g) \\rightleftharpoons 2\\,\\text{NH}_3(g) \\quad K_1 = 64\\text{ at } T$"
            "</div>"
        ),
        "question": (
            "Given the equilibrium constant $K_1 = 64$ for the synthesis of ammonia above at temperature $T$, "
            "what is the value of the equilibrium constant $K_2$ for the reaction "
            "$\\text{NH}_3(g) \\rightleftharpoons \\frac{1}{2}\\,\\text{N}_2(g) + \\frac{3}{2}\\,\\text{H}_2(g)$ at the same temperature?"
        ),
        "options": [
            "$0.016$",
            "$0.125$",
            "$8.0$",
            "$32$",
        ],
        "correct_index": 1,
        "explanation": (
            "The target reaction is obtained by reversing the original equation (which inverts $K$) and multiplying the "
            "coefficients by $\\frac{1}{2}$ (which raises $K$ to the $\\frac{1}{2}$ power). Therefore, "
            "$K_2 = K_1^{-1/2} = \\frac{1}{\\sqrt{64}} = \\frac{1}{8} = 0.125$. Inverting without taking the square root gives "
            "$0.016$, taking the square root without inverting gives $8.0$, and multiplying $K_1$ by $\\frac{1}{2}$ instead of "
            "raising it to the $\\frac{1}{2}$ power gives $32$."
        ),
    },
    {
        "unit_q_num": 19,
        "topic_code": "7.6",
        "topic_title": "Properties of the Equilibrium Constant",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Reaction</th><th>Equilibrium Constant at $25^\\circ\\text{C}$</th></tr></thead>"
            "<tbody>"
            "<tr><td>$\\text{AgCl}(s) \\rightleftharpoons \\text{Ag}^+(aq) + \\text{Cl}^-(aq)$</td><td>$K_1 = 1.8 \\times 10^{-10}$</td></tr>"
            "<tr><td>$\\text{Ag}^+(aq) + 2\\,\\text{NH}_3(aq) \\rightleftharpoons [\\text{Ag(NH}_3)_2]^+(aq)$</td><td>$K_2 = 1.6 \\times 10^7$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Based on the information in the table above, what is the value of the equilibrium constant $K_3$ at $25^\\circ\\text{C}$ "
            "for the dissolution of $\\text{AgCl}(s)$ in aqueous ammonia according to the equation "
            "$\\text{AgCl}(s) + 2\\,\\text{NH}_3(aq) \\rightleftharpoons [\\text{Ag(NH}_3)_2]^+(aq) + \\text{Cl}^-(aq)$?"
        ),
        "options": [
            "$1.1 \\times 10^{-17}$",
            "$1.6 \\times 10^7$",
            "$8.9 \\times 10^{16}$",
            "$2.9 \\times 10^{-3}$",
        ],
        "correct_index": 3,
        "explanation": (
            "Adding the two reactions cancels $\\text{Ag}^+(aq)$ on opposite sides and yields the target equation: "
            "$\\text{AgCl}(s) + 2\\,\\text{NH}_3(aq) \\rightleftharpoons [\\text{Ag(NH}_3)_2]^+(aq) + \\text{Cl}^-(aq)$. "
            "When two chemical equations are added, their equilibrium constants are multiplied: "
            "$K_3 = K_1 \\times K_2 = (1.8 \\times 10^{-10})(1.6 \\times 10^7) = 2.88 \\times 10^{-3} \\approx 2.9 \\times 10^{-3}$."
        ),
    },
    {
        "unit_q_num": 20,
        "topic_code": "7.6",
        "topic_title": "Properties of the Equilibrium Constant",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Step</th><th>Equilibrium Equation</th><th>$K_p$ at $1000\\text{ K}$</th></tr></thead>"
            "<tbody>"
            "<tr><td>1</td><td>$\\text{C}(s) + \\text{CO}_2(g) \\rightleftharpoons 2\\,\\text{CO}(g)$</td><td>$K_{p1} = 2.0$</td></tr>"
            "<tr><td>2</td><td>$\\text{CO}(g) + \\text{Cl}_2(g) \\rightleftharpoons \\text{COCl}_2(g)$</td><td>$K_{p2} = 5.0$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Using the equilibrium constants given in the table above, what is the value of $K_p$ at $1000\\text{ K}$ "
            "for the overall reaction $\\text{C}(s) + \\text{CO}_2(g) + 2\\,\\text{Cl}_2(g) \\rightleftharpoons 2\\,\\text{COCl}_2(g)$?"
        ),
        "options": [
            "$10$",
            "$20$",
            "$50$",
            "$100$",
        ],
        "correct_index": 2,
        "explanation": (
            "To obtain the target equation, take Step 1 as written ($K_{p1} = 2.0$) and add $2 \\times \\text{Step 2}$, which "
            "gives $2\\,\\text{CO}(g) + 2\\,\\text{Cl}_2(g) \\rightleftharpoons 2\\,\\text{COCl}_2(g)$ with equilibrium constant "
            "$(K_{p2})^2 = (5.0)^2 = 25$. Multiplying the constants for the summed steps gives "
            "$K_p = K_{p1} \\times (K_{p2})^2 = (2.0)(25) = 50$."
        ),
    },
    {
        "unit_q_num": 21,
        "topic_code": "7.6",
        "topic_title": "Properties of the Equilibrium Constant",
        "difficulty": "Challenging",
        "stimulus": (
            r'<div class="quiz-equation">'
            r"$2\,\text{NO}_2(g) \rightleftharpoons 2\,\text{NO}(g) + \text{O}_2(g) \quad K_c = 4.0 \times 10^{-4}\text{ at } T$"
            r"</div>"
        ),
        "question": (
            r"At temperature $T$, a mixture of $\text{NO}_2(g)$, $\text{NO}(g)$, and $\text{O}_2(g)$ has $Q_c = 1.0 \times 10^{-4}$ "
            r"at a certain instant for the reaction as written above. For the same mixture at the same instant, what is the value "
            r"of $Q_c'$ for the reaction $\text{NO}(g) + \frac{1}{2}\,\text{O}_2(g) \rightleftharpoons \text{NO}_2(g)$, and how "
            r"will $[\text{NO}_2]$ change as the mixture approaches equilibrium?"
        ),
        "options": [
            r"$Q_c' = 1.0 \times 10^{2}$, and $[\text{NO}_2]$ will decrease.",
            r"$Q_c' = 1.0 \times 10^{2}$, and $[\text{NO}_2]$ will increase.",
            r"$Q_c' = 1.0 \times 10^{4}$, and $[\text{NO}_2]$ will decrease.",
            r"$Q_c' = 5.0 \times 10^{-5}$, and $[\text{NO}_2]$ will increase.",
        ],
        "correct_index": 0,
        "explanation": (
            r"The new equation is the given equation reversed (invert) and multiplied by $\frac{1}{2}$ (raise to the "
            r"$\frac{1}{2}$ power). Because $Q$ has the same mathematical form as $K$, the same manipulations apply to $Q$: "
            r"$Q_c' = (1.0 \times 10^{-4})^{-1/2} = 1.0 \times 10^{2}$ and $K_c' = (4.0 \times 10^{-4})^{-1/2} = 50$. "
            r"Since $Q_c' = 100 > K_c' = 50$, the new reaction proceeds in the reverse direction, consuming $\text{NO}_2$, so "
            r"$[\text{NO}_2]$ decreases. This agrees with the original equation: $Q_c = 1.0 \times 10^{-4} < K_c = 4.0 \times 10^{-4}$, "
            r"so the net forward reaction also consumes $\text{NO}_2$. Inverting $Q_c$ without taking the square root gives "
            r"$1.0 \times 10^{4}$, and multiplying $Q_c$ by $\frac{1}{2}$ gives $5.0 \times 10^{-5}$."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 7.7: Calculating Equilibrium Concentrations (Q22 - Q25)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 22,
        "topic_code": "7.7",
        "topic_title": "Calculating Equilibrium Concentrations",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{H}_2(g) + \\text{I}_2(g) \\rightleftharpoons 2\\,\\text{HI}(g) \\quad K_c = 64.0\\text{ at } 700\\text{ K}$"
            "</div>"
        ),
        "question": (
            "If $1.00\\text{ mol}$ of $\\text{H}_2(g)$ and $1.00\\text{ mol}$ of $\\text{I}_2(g)$ are placed in an evacuated "
            "$2.00\\text{ L}$ rigid container at $700\\text{ K}$, what is the concentration of $\\text{HI}(g)$ at equilibrium?"
        ),
        "options": [
            "$0.40\\text{ M}$",
            "$0.64\\text{ M}$",
            "$0.80\\text{ M}$",
            "$1.60\\text{ M}$",
        ],
        "correct_index": 2,
        "explanation": (
            "Initial concentrations are $[\\text{H}_2]_0 = [\\text{I}_2]_0 = \\frac{1.00\\text{ mol}}{2.00\\text{ L}} = 0.50\\text{ M}$ "
            "and $[\\text{HI}]_0 = 0\\text{ M}$. Let $x$ be the change in $[\\text{H}_2]$ and $[\\text{I}_2]$, so at equilibrium "
            "$[\\text{H}_2] = [\\text{I}_2] = 0.50 - x$ and $[\\text{HI}] = 2x$. "
            "Substitute into $K_c$: $\\frac{(2x)^2}{(0.50 - x)^2} = 64.0$. Taking the square root of both sides gives "
            "$\\frac{2x}{0.50 - x} = 8.0 \\implies 2x = 4.0 - 8x \\implies 10x = 4.0 \\implies x = 0.40\\text{ M}$. "
            "Thus, $[\\text{HI}]_{\\text{eq}} = 2x = 2(0.40\\text{ M}) = 0.80\\text{ M}$."
        ),
    },
    {
        "unit_q_num": 23,
        "topic_code": "7.7",
        "topic_title": "Calculating Equilibrium Concentrations",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{COCl}_2(g) \\rightleftharpoons \\text{CO}(g) + \\text{Cl}_2(g) \\quad K_c = 4.0 \\times 10^{-9}\\text{ at } 373\\text{ K}$"
            "</div>"
        ),
        "question": (
            "A rigid vessel is filled with $\\text{COCl}_2(g)$ to an initial concentration of $0.25\\text{ M}$ at $373\\text{ K}$. "
            "What is the equilibrium concentration of $\\text{CO}(g)$ at this temperature?"
        ),
        "options": [
            "$1.0 \\times 10^{-9}\\text{ M}$",
            "$3.2 \\times 10^{-5}\\text{ M}$",
            "$6.3 \\times 10^{-5}\\text{ M}$",
            "$2.0 \\times 10^{-4}\\text{ M}$",
        ],
        "correct_index": 1,
        "explanation": (
            "Set up an ICE table: $[\\text{COCl}_2] = 0.25 - x$ and $[\\text{CO}] = [\\text{Cl}_2] = x$. "
            "Because $K_c = 4.0 \\times 10^{-9}$ is extremely small compared to $0.25\\text{ M}$, $x \\ll 0.25$, so "
            "$0.25 - x \\approx 0.25$. Then $K_c = \\frac{x^2}{0.25} = 4.0 \\times 10^{-9} \\implies "
            "x^2 = 1.0 \\times 10^{-9} = 10 \\times 10^{-10} \\implies x = \\sqrt{10} \\times 10^{-5} \\approx 3.2 \\times 10^{-5}\\text{ M}$. "
            "Check: $\\frac{3.2 \\times 10^{-5}}{0.25} \\approx 0.013\\%$, far below $5\\%$, so the approximation is justified."
        ),
    },
    {
        "unit_q_num": 24,
        "topic_code": "7.7",
        "topic_title": "Calculating Equilibrium Concentrations",
        "difficulty": "Challenging",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{A}(g) + \\text{B}(g) \\rightleftharpoons \\text{C}(g) + \\text{D}(g) \\quad K_c = 9.00\\text{ at } 500\\text{ K}$"
            "</div>"
        ),
        "question": (
            "A reaction mixture in a $1.00\\text{ L}$ container at $500\\text{ K}$ initially contains $1.00\\text{ mol}$ of $\\text{A}(g)$, "
            "$1.00\\text{ mol}$ of $\\text{B}(g)$, $1.00\\text{ mol}$ of $\\text{C}(g)$, and $1.00\\text{ mol}$ of $\\text{D}(g)$. "
            "When the system reaches equilibrium at $500\\text{ K}$, what is the equilibrium concentration of $\\text{C}(g)$?"
        ),
        "options": [
            "$0.50\\text{ M}$",
            "$1.25\\text{ M}$",
            "$1.50\\text{ M}$",
            "$1.75\\text{ M}$",
        ],
        "correct_index": 2,
        "explanation": (
            "Initially, $Q_c = \\frac{(1.00)(1.00)}{(1.00)(1.00)} = 1.00 < K_c = 9.00$, so the reaction shifts forward. "
            "At equilibrium, $[\\text{A}] = [\\text{B}] = 1.00 - x$ and $[\\text{C}] = [\\text{D}] = 1.00 + x$. "
            "Then $K_c = \\frac{(1.00 + x)^2}{(1.00 - x)^2} = 9.00$. Taking the positive square root of both sides: "
            "$\\frac{1.00 + x}{1.00 - x} = 3.00 \\implies 1.00 + x = 3.00 - 3x \\implies 4x = 2.00 \\implies x = 0.50\\text{ M}$. "
            "Therefore, $[\\text{C}]_{\\text{eq}} = 1.00 + 0.50 = 1.50\\text{ M}$."
        ),
    },
    {
        "unit_q_num": 25,
        "topic_code": "7.7",
        "topic_title": "Calculating Equilibrium Concentrations",
        "difficulty": "Challenging",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{SO}_2\\text{Cl}_2(g) \\rightleftharpoons \\text{SO}_2(g) + \\text{Cl}_2(g) \\quad K_p = 2.40\\text{ at } 375\\text{ K}$"
            "</div>"
        ),
        "question": (
            "In an experiment at $375\\text{ K}$, $\\text{SO}_2\\text{Cl}_2(g)$ is placed in a rigid container together with an "
            "initial $\\text{Cl}_2(g)$ partial pressure of $1.20\\text{ atm}$ and no $\\text{SO}_2(g)$. At equilibrium, the partial "
            "pressure of $\\text{SO}_2(g)$ is found to be $0.80\\text{ atm}$. What was the initial partial pressure of "
            "$\\text{SO}_2\\text{Cl}_2(g)$ placed in the container?"
        ),
        "options": [
            "$0.67\\text{ atm}$",
            "$2.00\\text{ atm}$",
            "$2.27\\text{ atm}$",
            "$1.47\\text{ atm}$",
        ],
        "correct_index": 3,
        "explanation": (
            "Let $P_0$ be the initial partial pressure of $\\text{SO}_2\\text{Cl}_2(g)$. Since $P_{\\text{SO}_2}$ increases from $0$ "
            "to $0.80\\text{ atm}$ ($x = 0.80\\text{ atm}$), the equilibrium partial pressures are: "
            "$P_{\\text{SO}_2} = 0.80\\text{ atm}$, $P_{\\text{Cl}_2} = 1.20 + 0.80 = 2.00\\text{ atm}$, and "
            "$P_{\\text{SO}_2\\text{Cl}_2} = P_0 - 0.80\\text{ atm}$. Using $K_p = 2.40$: "
            "$2.40 = \\frac{(0.80)(2.00)}{P_{\\text{SO}_2\\text{Cl}_2}} = \\frac{1.60}{P_{\\text{SO}_2\\text{Cl}_2}} "
            "\\implies P_{\\text{SO}_2\\text{Cl}_2} = \\frac{1.60}{2.40} = 0.67\\text{ atm}$. "
            "Thus, the initial pressure was $P_0 = 0.67 + 0.80 = 1.47\\text{ atm}$."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 7.8: Representations of Equilibrium (Q26 - Q28)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 26,
        "topic_code": "7.8",
        "topic_title": "Representations of Equilibrium",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{X}_2(g) + \\text{Y}_2(g) \\rightleftharpoons 2\\,\\text{XY}(g)$"
            "</div>"
        ),
        "question": (
            "A particulate diagram of an equilibrium mixture for the reaction above in a $1.0\\text{ L}$ rigid vessel "
            "shows $2$ molecules of $\\text{X}_2$, $2$ molecules of $\\text{Y}_2$, and $8$ molecules of $\\text{XY}$. "
            "What is the numerical value of the equilibrium constant $K$ represented by this particulate diagram?"
        ),
        "options": [
            "$2.0$",
            "$4.0$",
            "$8.0$",
            "$16$",
        ],
        "correct_index": 3,
        "explanation": (
            "Because $\\Delta n_{\\text{gas}} = 0$, the volume and conversion factors between molecule counts and molarity "
            "cancel out in the $K_c$ expression: "
            "$K = \\frac{(N_{\\text{XY}})^2}{(N_{\\text{X}_2})(N_{\\text{Y}_2})} = \\frac{8^2}{(2)(2)} = \\frac{64}{4} = 16$."
        ),
    },
    {
        "unit_q_num": 27,
        "topic_code": "7.8",
        "topic_title": "Representations of Equilibrium",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Curve on Concentration vs. Time Graph</th><th>Concentration at $t = 0$ ($\\text{M}$)</th><th>Concentration at Plateau ($t \\ge t_{\\text{eq}}$) ($\\text{M}$)</th></tr></thead>"
            "<tbody>"
            "<tr><td>Species $\\text{A}(g)$</td><td>$0.80$</td><td>$0.20$</td></tr>"
            "<tr><td>Species $\\text{B}(g)$</td><td>$0.00$</td><td>$0.30$</td></tr>"
            "<tr><td>Species $\\text{C}(g)$</td><td>$0.00$</td><td>$0.60$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "A concentration-versus-time graph for a reversible gas-phase reaction shows three curves whose initial and "
            "equilibrium plateau concentrations are summarized in the table above. Which of the following gives the "
            "correct balanced chemical equation and the value of $K_c$?"
        ),
        "options": [
            "$2\\,\\text{A}(g) \\rightleftharpoons \\text{B}(g) + 2\\,\\text{C}(g)$; $K_c = 2.7$",
            "$2\\,\\text{A}(g) \\rightleftharpoons \\text{B}(g) + 2\\,\\text{C}(g)$; $K_c = 0.90$",
            "$3\\,\\text{A}(g) \\rightleftharpoons \\text{B}(g) + 2\\,\\text{C}(g)$; $K_c = 13.5$",
            "$\\text{A}(g) \\rightleftharpoons \\text{B}(g) + \\text{C}(g)$; $K_c = 0.90$",
        ],
        "correct_index": 0,
        "explanation": (
            "From $t = 0$ to equilibrium, $\\Delta[\\text{A}] = -0.60\\text{ M}$, $\\Delta[\\text{B}] = +0.30\\text{ M}$, and "
            "$\\Delta[\\text{C}] = +0.60\\text{ M}$. The stoichiometric ratio $|\\Delta[\\text{A}]| : \\Delta[\\text{B}] : \\Delta[\\text{C}]$ "
            "is $0.60 : 0.30 : 0.60 = 2 : 1 : 2$, giving $2\\,\\text{A}(g) \\rightleftharpoons \\text{B}(g) + 2\\,\\text{C}(g)$. "
            "Substituting the plateau (equilibrium) concentrations gives "
            "$K_c = \\frac{[\\text{B}][\\text{C}]^2}{[\\text{A}]^2} = \\frac{(0.30)(0.60)^2}{(0.20)^2} = \\frac{(0.30)(0.36)}{0.040} = 2.7$."
        ),
    },
    {
        "unit_q_num": 28,
        "topic_code": "7.8",
        "topic_title": "Representations of Equilibrium",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": (
            "Consider the isomerization reaction $\\text{A}(g) \\rightleftharpoons \\text{B}(g)$ with $K_c = 4.0$ at $400\\text{ K}$. "
            "In Experiment 1, a $1.0\\text{ L}$ vessel initially contains $10$ moles of pure $\\text{A}(g)$. "
            "In Experiment 2, an identical $1.0\\text{ L}$ vessel at $400\\text{ K}$ initially contains $10$ moles of pure $\\text{B}(g)$. "
            "How do the particulate representations of the two vessels compare once both reach equilibrium?"
        ),
        "options": [
            "Experiment 1 has $8$ moles of $\\text{A}$ and $2$ moles of $\\text{B}$, whereas Experiment 2 has $2$ moles of $\\text{A}$ and $8$ moles of $\\text{B}$.",
            "Both vessels contain the exact same equilibrium composition: $2$ moles of $\\text{A}(g)$ and $8$ moles of $\\text{B}(g)$.",
            "Both vessels contain $5$ moles of $\\text{A}(g)$ and $5$ moles of $\\text{B}(g)$ at equilibrium.",
            "Experiment 2 cannot reach equilibrium because $Q_c$ is initially undefined.",
        ],
        "correct_index": 1,
        "explanation": (
            "The equilibrium state for a given total number of moles of atoms in a fixed volume at constant temperature is "
            "independent of whether the system starts from pure reactants or pure products. Since $\\frac{[\\text{B}]}{[\\text{A}]} = 4.0$ "
            "and $n_{\\text{A}} + n_{\\text{B}} = 10\\text{ mol}$, both vessels reach $n_{\\text{A}} = 2\\text{ mol}$ and $n_{\\text{B}} = 8\\text{ mol}$."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 7.9: Introduction to Le Châtelier's Principle (Q29 - Q32)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 29,
        "topic_code": "7.9",
        "topic_title": "Introduction to Le Châtelier's Principle",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{Co(H}_2\\text{O)}_6^{2+}(aq) \\text{ (pink)} + 4\\,\\text{Cl}^-(aq) \\rightleftharpoons "
            "\\text{CoCl}_4^{2-}(aq) \\text{ (blue)} + 6\\,\\text{H}_2\\text{O}(l) \\quad \\Delta H^\\circ > 0$"
            "</div>"
        ),
        "question": (
            "An equilibrium mixture of the cobalt complex ions above is purple (a mixture of pink and blue) at room temperature. "
            "Which of the following perturbations will cause the solution to become more blue?"
        ),
        "options": [
            "Placing the reaction vessel in an ice-water bath.",
            "Adding several drops of concentrated $\\text{AgNO}_3(aq)$ to precipitate $\\text{AgCl}(s)$.",
            "Heating the solution in a hot-water bath.",
            "Diluting the solution by adding a large volume of distilled $\\text{H}_2\\text{O}(l)$.",
        ],
        "correct_index": 2,
        "explanation": (
            "Because the forward reaction is endothermic ($\\Delta H^\\circ > 0$), increasing the temperature increases the "
            "equilibrium constant $K$ and causes a net shift in the forward direction, producing more blue $\\text{CoCl}_4^{2-}(aq)$. "
            "Cooling, precipitating $\\text{Cl}^-$ with $\\text{Ag}^+$, or diluting with water all shift the equilibrium toward the pink reactant side."
        ),
    },
    {
        "unit_q_num": 30,
        "topic_code": "7.9",
        "topic_title": "Introduction to Le Châtelier's Principle",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{CaCO}_3(s) \\rightleftharpoons \\text{CaO}(s) + \\text{CO}_2(g) \\quad \\Delta H^\\circ = +178\\text{ kJ/mol}_{rxn}$"
            "</div>"
        ),
        "question": (
            "Solid $\\text{CaCO}_3$, solid $\\text{CaO}$, and $\\text{CO}_2(g)$ are at equilibrium in a rigid sealed container "
            "at $1100\\text{ K}$. If additional solid $\\text{CaCO}_3(s)$ is introduced into the container at constant volume "
            "and temperature ($1100\\text{ K}$), how will the equilibrium partial pressure of $\\text{CO}_2(g)$ be affected?"
        ),
        "options": [
            "$P_{\\text{CO}_2}$ will increase because there is more reactant available to decompose.",
            "$P_{\\text{CO}_2}$ will decrease because the added solid reduces the free gas volume significantly.",
            "$P_{\\text{CO}_2}$ will remain unchanged because $\\text{CaCO}_3(s)$ is a pure solid and $K_p = P_{\\text{CO}_2}$ depends only on temperature.",
            "$P_{\\text{CO}_2}$ will double if the mass of $\\text{CaCO}_3(s)$ is doubled.",
        ],
        "correct_index": 2,
        "explanation": (
            "Because $\\text{CaCO}_3(s)$ and $\\text{CaO}(s)$ are pure solids with unit activity, the equilibrium expression is simply "
            "$K_p = P_{\\text{CO}_2}$. Adding more pure solid $\\text{CaCO}_3(s)$ at constant temperature does not change $Q_p$ or $K_p$, "
            "so the equilibrium partial pressure of $\\text{CO}_2(g)$ remains unchanged."
        ),
    },
    {
        "unit_q_num": 31,
        "topic_code": "7.9",
        "topic_title": "Introduction to Le Châtelier's Principle",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$2\\,\\text{NO}_2(g) \\rightleftharpoons \\text{N}_2\\text{O}_4(g) \\quad \\Delta H^\\circ = -57.2\\text{ kJ/mol}_{rxn}$"
            "</div>"
        ),
        "question": (
            "The reaction above is at equilibrium in a cylinder fitted with a movable piston. Which of the following "
            "changes will increase BOTH the value of the equilibrium constant $K_p$ and the equilibrium mole fraction of "
            "$\\text{N}_2\\text{O}_4(g)$?"
        ),
        "options": [
            "Compressing the gas mixture to half its volume at constant temperature.",
            "Decreasing the temperature of the system at constant pressure.",
            "Adding a platinum catalyst to the cylinder at constant temperature.",
            "Injecting inert $\\text{He}(g)$ into the cylinder while holding the volume constant.",
        ],
        "correct_index": 1,
        "explanation": (
            "Only a change in temperature alters the numerical value of the equilibrium constant $K_p$. "
            "Because the forward reaction is exothermic ($\\Delta H^\\circ < 0$), decreasing the temperature increases $K_p$ "
            "and shifts the equilibrium toward products, increasing the equilibrium mole fraction of $\\text{N}_2\\text{O}_4(g)$."
        ),
    },
    {
        "unit_q_num": 32,
        "topic_code": "7.9",
        "topic_title": "Introduction to Le Châtelier's Principle",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Temperature ($\\text{K}$)</th><th>$K_p$ for $2\\,\\text{SO}_3(g) \\rightleftharpoons 2\\,\\text{SO}_2(g) + \\text{O}_2(g)$</th></tr></thead>"
            "<tbody>"
            "<tr><td>$800$</td><td>$8.0 \\times 10^{-4}$</td></tr>"
            "<tr><td>$1000$</td><td>$0.29$</td></tr>"
            "<tr><td>$1200$</td><td>$16$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Based on the temperature dependence of $K_p$ shown in the table above, which of the following combinations of "
            "conditions will maximize the equilibrium yield of $\\text{SO}_2(g)$ from $\\text{SO}_3(g)$?"
        ),
        "options": [
            "High temperature and high pressure (small volume)",
            "Low temperature and high pressure (small volume)",
            "Low temperature and low pressure (large volume)",
            "High temperature and low pressure (large volume)",
        ],
        "correct_index": 3,
        "explanation": (
            "As temperature increases from $800\\text{ K}$ to $1200\\text{ K}$, $K_p$ increases, showing that the forward "
            "decomposition reaction is endothermic ($\\Delta H^\\circ > 0$) and favored by high temperature. "
            "Furthermore, the reaction converts $2\\text{ mol}$ of gas into $3\\text{ mol}$ of gas ($\\Delta n_{\\text{gas}} = +1$), "
            "so low pressure (large volume) causes $Q_p < K_p$ and shifts the equilibrium toward the side with more moles of gas."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 7.10: Reaction Quotient and Le Châtelier's Principle (Q33 - Q36)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 33,
        "topic_code": "7.10",
        "topic_title": "Reaction Quotient and Le Châtelier's Principle",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{PCl}_3(g) + \\text{Cl}_2(g) \\rightleftharpoons \\text{PCl}_5(g)$"
            "</div>"
        ),
        "question": (
            "The system above is at equilibrium in a cylinder with a movable piston at constant temperature. The volume of the "
            "cylinder is suddenly halved ($V_{\\text{new}} = \\frac{1}{2}V_{\\text{initial}}$), doubling the instantaneous concentration "
            "of each gas. Which of the following correctly compares $Q_c$ immediately after compression to $K_c$ and predicts "
            "the resulting direction of shift?"
        ),
        "options": [
            "$Q_c = 2K_c$; the reaction shifts in the reverse direction.",
            "$Q_c = \\frac{1}{2}K_c$; the reaction shifts in the forward direction.",
            "$Q_c = K_c$; no shift occurs because all concentrations doubled equally.",
            "$Q_c = \\frac{1}{4}K_c$; the reaction shifts in the forward direction.",
        ],
        "correct_index": 1,
        "explanation": (
            "At the initial equilibrium, $K_c = \\frac{[\\text{PCl}_5]}{[\\text{PCl}_3][\\text{Cl}_2]}$. "
            "When the volume is halved, each concentration doubles: "
            "$Q_c = \\frac{2[\\text{PCl}_5]}{(2[\\text{PCl}_3])(2[\\text{Cl}_2])} = \\frac{1}{2} \\frac{[\\text{PCl}_5]}{[\\text{PCl}_3][\\text{Cl}_2]} = \\frac{1}{2}K_c$. "
            "Because $Q_c < K_c$, the system shifts in the forward direction (toward fewer moles of gas) until $Q_c = K_c$."
        ),
    },
    {
        "unit_q_num": 34,
        "topic_code": "7.10",
        "topic_title": "Reaction Quotient and Le Châtelier's Principle",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{Fe}^{3+}(aq) + \\text{SCN}^-(aq) \\rightleftharpoons \\text{FeSCN}^{2+}(aq)$"
            "</div>"
        ),
        "question": (
            "An aqueous solution containing $\\text{Fe}^{3+}(aq)$, $\\text{SCN}^-(aq)$, and red-brown $\\text{FeSCN}^{2+}(aq)$ "
            "is at equilibrium at $25^\\circ\\text{C}$. If the solution is diluted with an equal volume of pure water at "
            "$25^\\circ\\text{C}$ (doubling the total solution volume), how does the number of moles of $\\text{FeSCN}^{2+}(aq)$ "
            "in the beaker change as equilibrium is re-established, and why?"
        ),
        "options": [
            "The number of moles of $\\text{FeSCN}^{2+}$ remains unchanged because water is omitted from the $K_c$ expression.",
            "The number of moles of $\\text{FeSCN}^{2+}$ increases because dilution makes $Q_c = \\frac{1}{2}K_c < K_c$, causing a net forward reaction.",
            "The number of moles of $\\text{FeSCN}^{2+}$ decreases because $K_c$ is halved upon doubling the solution volume.",
            "The number of moles of $\\text{FeSCN}^{2+}$ decreases because dilution makes $Q_c = 2K_c > K_c$, causing a net reverse reaction.",
        ],
        "correct_index": 3,
        "explanation": (
            "At the original equilibrium, $K_c = \\frac{[\\text{FeSCN}^{2+}]}{[\\text{Fe}^{3+}][\\text{SCN}^-]}$. "
            "Doubling the solution volume halves the molarity of every dissolved ion: "
            "$Q_c = \\frac{0.5[\\text{FeSCN}^{2+}]}{(0.5[\\text{Fe}^{3+}])(0.5[\\text{SCN}^-])} = 2K_c$. "
            "Since $Q_c > K_c$, the reaction shifts in the reverse direction (toward the side with more dissolved particles), "
            "decreasing the number of moles of $\\text{FeSCN}^{2+}$."
        ),
    },
    {
        "unit_q_num": 35,
        "topic_code": "7.10",
        "topic_title": "Reaction Quotient and Le Châtelier's Principle",
        "difficulty": "Challenging",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{N}_2(g) + 3\\,\\text{H}_2(g) \\rightleftharpoons 2\\,\\text{NH}_3(g)$"
            "</div>"
        ),
        "question": (
            "A mixture of $\\text{N}_2(g)$, $\\text{H}_2(g)$, and $\\text{NH}_3(g)$ is at equilibrium in a rigid, constant-volume "
            "steel tank at $500\\text{ K}$. If $1.0\\text{ mol}$ of inert $\\text{Ar}(g)$ is injected into the tank at constant "
            "volume and temperature, increasing the total pressure inside the tank, what happens to $Q_p$ and the equilibrium position?"
        ),
        "options": [
            "$Q_p$ becomes smaller than $K_p$, and the reaction shifts forward to produce more $\\text{NH}_3(g)$.",
            "$Q_p$ becomes larger than $K_p$, and the reaction shifts in the reverse direction.",
            "$Q_p$ remains equal to $K_p$, and there is no shift in the equilibrium position because the partial pressures of $\\text{N}_2$, $\\text{H}_2$, and $\\text{NH}_3$ do not change.",
            "$K_p$ increases in proportion to the total pressure, shifting the reaction forward.",
        ],
        "correct_index": 2,
        "explanation": (
            "Because the tank is rigid (constant $V$) and at constant $T$, adding inert $\\text{Ar}(g)$ does not change the molar "
            "concentrations or the individual partial pressures ($P_i = \\frac{n_i RT}{V}$) of $\\text{N}_2$, $\\text{H}_2$, or $\\text{NH}_3$. "
            "Therefore, $Q_p$ remains equal to $K_p$, and no shift in equilibrium occurs."
        ),
    },
    {
        "unit_q_num": 36,
        "topic_code": "7.10",
        "topic_title": "Reaction Quotient and Le Châtelier's Principle",
        "difficulty": "Challenging",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{A}(g) \\rightleftharpoons 2\\,\\text{B}(g) \\quad K_c = 4.0\\text{ at } 400\\text{ K}$"
            "</div>"
        ),
        "question": (
            "In a rigid $1.0\\text{ L}$ vessel at $400\\text{ K}$, an equilibrium mixture contains $[\\text{A}] = 1.0\\text{ M}$ "
            "and $[\\text{B}] = 2.0\\text{ M}$. Immediately after an additional $1.0\\text{ mol}$ of $\\text{B}(g)$ is injected "
            "into the vessel at constant temperature, a new equilibrium is established. Which of the following is true of $[\\text{B}]$ "
            "at the new equilibrium?"
        ),
        "options": [
            "$[\\text{B}] < 2.0\\text{ M}$",
            "$[\\text{B}] = 2.0\\text{ M}$",
            "$2.0\\text{ M} < [\\text{B}] < 3.0\\text{ M}$",
            "$[\\text{B}] > 3.0\\text{ M}$",
        ],
        "correct_index": 2,
        "explanation": (
            "Immediately after injecting $1.0\\text{ mol}$ of $\\text{B}(g)$ into the $1.0\\text{ L}$ vessel, $[\\text{B}]$ jumps "
            "from $2.0\\text{ M}$ to $3.0\\text{ M}$, giving $Q_c = \\frac{(3.0)^2}{1.0} = 9.0 > K_c = 4.0$. "
            "The reaction shifts in the reverse direction ($2\\,\\text{B} \\rightarrow \\text{A}$), consuming some of the added $\\text{B}$ "
            "and increasing $[\\text{A}]$ above $1.0\\text{ M}$. Because $[\\text{A}]_{\\text{new}} > 1.0\\text{ M}$ and "
            "$[\\text{B}]_{\\text{new}} = \\sqrt{4.0[\\text{A}]_{\\text{new}}}$, the final concentration of $\\text{B}$ must remain "
            "greater than its original $2.0\\text{ M}$ but less than the $3.0\\text{ M}$ spike: $2.0\\text{ M} < [\\text{B}] < 3.0\\text{ M}$."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 7.11: Introduction to Solubility Equilibria (Q37 - Q40)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 37,
        "topic_code": "7.11",
        "topic_title": "Introduction to Solubility Equilibria",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{MgF}_2(s) \\rightleftharpoons \\text{Mg}^{2+}(aq) + 2\\,\\text{F}^-(aq) \\quad K_{\\text{sp}} = 4.0 \\times 10^{-9}\\text{ at } 25^\\circ\\text{C}$"
            "</div>"
        ),
        "question": (
            "What is the molar solubility of $\\text{MgF}_2(s)$ in pure water at $25^\\circ\\text{C}$?"
        ),
        "options": [
            "$1.0 \\times 10^{-3}\\text{ M}$",
            "$1.6 \\times 10^{-3}\\text{ M}$",
            "$6.3 \\times 10^{-5}\\text{ M}$",
            "$2.0 \\times 10^{-9}\\text{ M}$",
        ],
        "correct_index": 0,
        "explanation": (
            "Let $s$ be the molar solubility of $\\text{MgF}_2$ in pure water. In a saturated solution, "
            "$[\\text{Mg}^{2+}] = s$ and $[\\text{F}^-] = 2s$. Substituting into the solubility product expression gives "
            "$K_{\\text{sp}} = [\\text{Mg}^{2+}][\\text{F}^-]^2 = (s)(2s)^2 = 4s^3$. "
            "Setting $4s^3 = 4.0 \\times 10^{-9}$ gives $s^3 = 1.0 \\times 10^{-9}$, so $s = 1.0 \\times 10^{-3}\\text{ M}$."
        ),
    },
    {
        "unit_q_num": 38,
        "topic_code": "7.11",
        "topic_title": "Introduction to Solubility Equilibria",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Salt</th><th>Formula</th><th>$K_{\\text{sp}}$ at $25^\\circ\\text{C}$</th></tr></thead>"
            "<tbody>"
            "<tr><td>Silver chloride</td><td>$\\text{AgCl}$</td><td>$1.8 \\times 10^{-10}$</td></tr>"
            "<tr><td>Silver chromate</td><td>$\\text{Ag}_2\\text{CrO}_4$</td><td>$1.1 \\times 10^{-12}$</td></tr>"
            "<tr><td>Calcium fluoride</td><td>$\\text{CaF}_2$</td><td>$3.5 \\times 10^{-11}$</td></tr>"
            "<tr><td>Silver sulfide</td><td>$\\text{Ag}_2\\text{S}$</td><td>$6.0 \\times 10^{-51}$</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Based on the $K_{\\text{sp}}$ values in the table above, which of the four salts has the GREATEST molar "
            "solubility in pure water at $25^\\circ\\text{C}$?"
        ),
        "options": [
            "$\\text{AgCl}$",
            "$\\text{Ag}_2\\text{CrO}_4$",
            "$\\text{CaF}_2$",
            "$\\text{Ag}_2\\text{S}$",
        ],
        "correct_index": 2,
        "explanation": (
            "Because the salts have different stoichiometries ($1:1$ vs $1:2$), we must compare their molar solubilities $s$: "
            "For $\\text{AgCl}$ ($K_{\\text{sp}} = s^2$), $s = \\sqrt{1.8 \\times 10^{-10}} = 1.3 \\times 10^{-5}\\text{ M}$. "
            "For $\\text{Ag}_2\\text{CrO}_4$ ($K_{\\text{sp}} = 4s^3$), $s = (2.75 \\times 10^{-13})^{1/3} \\approx 6.5 \\times 10^{-5}\\text{ M}$. "
            "For $\\text{CaF}_2$ ($K_{\\text{sp}} = 4s^3$), $s = (8.75 \\times 10^{-12})^{1/3} \\approx 2.1 \\times 10^{-4}\\text{ M}$. "
            "For $\\text{Ag}_2\\text{S}$ ($K_{\\text{sp}} = 4s^3$), $s = (1.5 \\times 10^{-51})^{1/3} \\approx 1.1 \\times 10^{-17}\\text{ M}$. "
            "Thus, $\\text{CaF}_2$ has the greatest molar solubility ($2.1 \\times 10^{-4}\\text{ M}$)."
        ),
    },
    {
        "unit_q_num": 39,
        "topic_code": "7.11",
        "topic_title": "Introduction to Solubility Equilibria",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{PbI}_2(s) \\rightleftharpoons \\text{Pb}^{2+}(aq) + 2\\,\\text{I}^-(aq) \\quad K_{\\text{sp}} = 9.8 \\times 10^{-9}\\text{ at } 25^\\circ\\text{C}$"
            "</div>"
        ),
        "question": (
            "A student mixes $100.0\\text{ mL}$ of $2.0 \\times 10^{-3}\\text{ M } \\text{Pb(NO}_3)_2(aq)$ with $100.0\\text{ mL}$ "
            "of $4.0 \\times 10^{-3}\\text{ M } \\text{NaI}(aq)$ at $25^\\circ\\text{C}$. Assuming the volumes are additive, "
            "which of the following correctly predicts whether a precipitate of $\\text{PbI}_2(s)$ will form?"
        ),
        "options": [
            "No precipitate forms because $Q_{\\text{sp}} = 4.0 \\times 10^{-9} < K_{\\text{sp}}$.",
            "A precipitate forms because $Q_{\\text{sp}} = 3.2 \\times 10^{-8} > K_{\\text{sp}}$.",
            "No precipitate forms because $Q_{\\text{sp}} = 2.0 \\times 10^{-6} < K_{\\text{sp}}$.",
            "A precipitate forms because $Q_{\\text{sp}} = 1.6 \\times 10^{-8} > K_{\\text{sp}}$.",
        ],
        "correct_index": 0,
        "explanation": (
            "Mixing equal volumes ($100.0\\text{ mL} + 100.0\\text{ mL} = 200.0\\text{ mL}$) halves the concentration of each ion: "
            "$[\\text{Pb}^{2+}] = 1.0 \\times 10^{-3}\\text{ M}$ and $[\\text{I}^-] = 2.0 \\times 10^{-3}\\text{ M}$. "
            "Calculate $Q_{\\text{sp}}$: $Q_{\\text{sp}} = [\\text{Pb}^{2+}][\\text{I}^-]^2 = (1.0 \\times 10^{-3})(2.0 \\times 10^{-3})^2 = 4.0 \\times 10^{-9}$. "
            "Because $Q_{\\text{sp}} = 4.0 \\times 10^{-9} < K_{\\text{sp}} = 9.8 \\times 10^{-9}$, the solution is unsaturated and no precipitate forms."
        ),
    },
    {
        "unit_q_num": 40,
        "topic_code": "7.11",
        "topic_title": "Introduction to Solubility Equilibria",
        "difficulty": "Challenging",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{La(IO}_3)_3(s) \\rightleftharpoons \\text{La}^{3+}(aq) + 3\\,\\text{IO}_3^-(aq)$"
            "</div>"
        ),
        "question": (
            "A saturated aqueous solution of lanthanum iodate, $\\text{La(IO}_3)_3$, at $25^\\circ\\text{C}$ is found to have "
            "an iodate ion concentration of $[\\text{IO}_3^-] = 3.0 \\times 10^{-3}\\text{ M}$. What is the value of $K_{\\text{sp}}$ "
            "for $\\text{La(IO}_3)_3$ at $25^\\circ\\text{C}$?"
        ),
        "options": [
            "$9.0 \\times 10^{-6}$",
            "$8.1 \\times 10^{-11}$",
            "$7.3 \\times 10^{-10}$",
            "$2.7 \\times 10^{-11}$",
        ],
        "correct_index": 3,
        "explanation": (
            "From the $1:3$ stoichiometry of $\\text{La(IO}_3)_3$ dissolution in pure water, $[\\text{IO}_3^-] = 3s = 3.0 \\times 10^{-3}\\text{ M}$, "
            "so the molar solubility is $s = [\\text{La}^{3+}] = 1.0 \\times 10^{-3}\\text{ M}$. "
            "Substituting into the $K_{\\text{sp}}$ expression: "
            "$K_{\\text{sp}} = [\\text{La}^{3+}][\\text{IO}_3^-]^3 = (1.0 \\times 10^{-3})(3.0 \\times 10^{-3})^3 = 2.7 \\times 10^{-11}$."
        ),
    },

    # -------------------------------------------------------------------------
    # Topic 7.12: Common-Ion Effect (Q41 - Q43)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 41,
        "topic_code": "7.12",
        "topic_title": "Common-Ion Effect",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{BaSO}_4(s) \\rightleftharpoons \\text{Ba}^{2+}(aq) + \\text{SO}_4^{2-}(aq) \\quad K_{\\text{sp}} = 1.1 \\times 10^{-10}\\text{ at } 25^\\circ\\text{C}$"
            "</div>"
        ),
        "question": (
            "What is the molar solubility of $\\text{BaSO}_4(s)$ in a $0.10\\text{ M } \\text{Na}_2\\text{SO}_4(aq)$ solution at $25^\\circ\\text{C}$?"
        ),
        "options": [
            "$1.0 \\times 10^{-5}\\text{ M}$",
            "$1.1 \\times 10^{-9}\\text{ M}$",
            "$1.1 \\times 10^{-10}\\text{ M}$",
            "$1.1 \\times 10^{-11}\\text{ M}$",
        ],
        "correct_index": 1,
        "explanation": (
            "In $0.10\\text{ M } \\text{Na}_2\\text{SO}_4(aq)$, the initial concentration of the common ion is $[\\text{SO}_4^{2-}] = 0.10\\text{ M}$. "
            "Let $s$ be the molar solubility of $\\text{BaSO}_4$: at equilibrium, $[\\text{Ba}^{2+}] = s$ and $[\\text{SO}_4^{2-}] = 0.10 + s \\approx 0.10\\text{ M}$. "
            "Then $K_{\\text{sp}} = (s)(0.10) = 1.1 \\times 10^{-10} \\implies s = 1.1 \\times 10^{-9}\\text{ M}$."
        ),
    },
    {
        "unit_q_num": 42,
        "topic_code": "7.12",
        "topic_title": "Common-Ion Effect",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{PbCl}_2(s) \\rightleftharpoons \\text{Pb}^{2+}(aq) + 2\\,\\text{Cl}^-(aq) \\quad K_{\\text{sp}} = 1.7 \\times 10^{-5}\\text{ at } 25^\\circ\\text{C}$"
            "</div>"
        ),
        "question": (
            "In which of the following aqueous solutions at $25^\\circ\\text{C}$ will $\\text{PbCl}_2(s)$ have the LOWEST molar solubility?"
        ),
        "options": [
            "Pure distilled water",
            "$0.10\\text{ M } \\text{NaNO}_3(aq)$",
            "$0.10\\text{ M } \\text{Pb(NO}_3)_2(aq)$",
            "$0.10\\text{ M } \\text{CaCl}_2(aq)$",
        ],
        "correct_index": 3,
        "explanation": (
            "For $\\text{PbCl}_2(s)$, $K_{\\text{sp}} = [\\text{Pb}^{2+}][\\text{Cl}^-]^2$. "
            "In $0.10\\text{ M } \\text{Pb(NO}_3)_2$, $[\\text{Pb}^{2+}] \\approx 0.10\\text{ M}$, so $4s^2 = \\frac{K_{\\text{sp}}}{0.10} "
            "\\implies s = \\sqrt{\\frac{1.7 \\times 10^{-4}}{4}} \\approx 6.5 \\times 10^{-3}\\text{ M}$. "
            "In $0.10\\text{ M } \\text{CaCl}_2$, $[\\text{Cl}^-] \\approx 0.20\\text{ M}$, and because $[\\text{Cl}^-]$ is squared in $K_{\\text{sp}}$, "
            "$s = \\frac{1.7 \\times 10^{-5}}{(0.20)^2} = \\frac{1.7 \\times 10^{-5}}{0.040} = 4.3 \\times 10^{-4}\\text{ M}$, which is the lowest molar solubility."
            " Check: in $\\text{CaCl}_2$, $2s$ is less than $0.5\\%$ of $0.20\\text{ M}$, so the approximation is justified; "
            "in $\\text{Pb(NO}_3)_2$, $s$ is about $6.5\\%$ of $0.10\\text{ M}$, so the approximation is rough, but solving exactly gives "
            "$s = 6.3 \\times 10^{-3}\\text{ M}$ and the ranking is unchanged."
        ),
    },
    {
        "unit_q_num": 43,
        "topic_code": "7.12",
        "topic_title": "Common-Ion Effect",
        "difficulty": "Challenging",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{SrF}_2(s) \\rightleftharpoons \\text{Sr}^{2+}(aq) + 2\\,\\text{F}^-(aq) \\quad K_{\\text{sp}} = 4.0 \\times 10^{-9}\\text{ at } 25^\\circ\\text{C}$"
            "</div>"
        ),
        "question": (
            "When solid $\\text{NaF}$ is dissolved in a saturated solution of $\\text{SrF}_2(aq)$ that is in contact with excess "
            "$\\text{SrF}_2(s)$ at $25^\\circ\\text{C}$ until $[\\text{F}^-] = 0.020\\text{ M}$, how do the value of $K_{\\text{sp}}$ "
            "and the equilibrium concentration $[\\text{Sr}^{2+}]$ compare to their values in pure water?"
        ),
        "options": [
            "$K_{\\text{sp}}$ remains $4.0 \\times 10^{-9}$, and $[\\text{Sr}^{2+}]$ decreases from $1.0 \\times 10^{-3}\\text{ M}$ to $1.0 \\times 10^{-5}\\text{ M}$.",
            "$K_{\\text{sp}}$ decreases, and $[\\text{Sr}^{2+}]$ decreases to $1.0 \\times 10^{-5}\\text{ M}$.",
            "$K_{\\text{sp}}$ remains $4.0 \\times 10^{-9}$, and $[\\text{Sr}^{2+}]$ decreases from $1.0 \\times 10^{-3}\\text{ M}$ to $2.0 \\times 10^{-7}\\text{ M}$.",
            "$K_{\\text{sp}}$ increases, and $[\\text{Sr}^{2+}]$ remains $1.0 \\times 10^{-3}\\text{ M}$.",
        ],
        "correct_index": 0,
        "explanation": (
            "$K_{\\text{sp}}$ depends only on temperature, so it remains $4.0 \\times 10^{-9}$ at $25^\\circ\\text{C}$. "
            "In pure water, $4s^3 = 4.0 \\times 10^{-9} \\implies [\\text{Sr}^{2+}] = 1.0 \\times 10^{-3}\\text{ M}$. "
            "When $[\\text{F}^-] = 0.020\\text{ M}$, $[\\text{Sr}^{2+}] = \\frac{K_{\\text{sp}}}{[\\text{F}^-]^2} = "
            "\\frac{4.0 \\times 10^{-9}}{(2.0 \\times 10^{-2})^2} = \\frac{4.0 \\times 10^{-9}}{4.0 \\times 10^{-4}} = 1.0 \\times 10^{-5}\\text{ M}$."
        ),
    },

    # -------------------------------------------------------------------------
    # Added 2026-10-03 — Blind-spot coverage (Fall 2024 CED): topics 7.1–7.12
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 44,
        "topic_code": "7.1",
        "topic_title": "Introduction to Equilibrium",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 300" role="img" aria-label="Graph of rate versus time for water sealed in an evacuated flask at constant temperature. The rate of evaporation is a horizontal line. The rate of condensation starts at zero, rises, and becomes equal to the rate of evaporation at time t1; after t1 both rates remain equal and constant." font-family="sans-serif" font-size="13">
<line x1="322.0" y1="250.0" x2="322.0" y2="58.0" stroke="#374151" stroke-width="1.5" stroke-dasharray="5 4"/>
<polyline points="70.0,82.0 490.0,82.0" fill="none" stroke="#374151" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>
<polyline points="70.0,250.0 73.5,237.7 77.0,226.4 80.5,215.8 84.0,206.1 87.5,197.0 91.0,188.6 94.5,180.9 98.0,173.6 101.5,167.0 105.0,160.8 108.5,155.0 112.0,149.7 115.5,144.7 119.0,140.2 122.5,135.9 126.0,132.0 129.5,128.3 133.0,125.0 136.5,121.8 140.0,118.9 143.5,116.2 147.0,113.7 150.5,111.4 154.0,109.3 157.5,107.3 161.0,105.4 164.5,103.7 168.0,102.1 171.5,100.7 175.0,99.3 178.5,98.0 182.0,96.9 185.5,95.8 189.0,94.8 192.5,93.9 196.0,93.0 199.5,92.2 203.0,91.4 206.5,90.8 210.0,90.1 213.5,89.5 217.0,89.0 220.5,88.5 224.0,88.0 227.5,87.6 231.0,87.2 234.5,86.8 238.0,86.4 241.5,86.1 245.0,85.8 248.5,85.5 252.0,85.3 255.5,85.0 259.0,84.8 262.5,84.6 266.0,84.4 269.5,84.2 273.0,84.1 276.5,83.9 280.0,83.8 283.5,83.7 287.0,83.5 290.5,83.4 294.0,83.3 297.5,83.2 301.0,83.1 304.5,83.0 308.0,83.0 311.5,82.9 315.0,82.8 318.5,82.8 322.0,82.7 325.5,82.7 329.0,82.6 332.5,82.6 336.0,82.5 339.5,82.5 343.0,82.5 346.5,82.4 350.0,82.4 353.5,82.4 357.0,82.3 360.5,82.3 364.0,82.3 367.5,82.3 371.0,82.2 374.5,82.2 378.0,82.2 381.5,82.2 385.0,82.2 388.5,82.2 392.0,82.2 395.5,82.1 399.0,82.1 402.5,82.1 406.0,82.1 409.5,82.1 413.0,82.1 416.5,82.1 420.0,82.1 423.5,82.1 427.0,82.1 430.5,82.1 434.0,82.1 437.5,82.1 441.0,82.1 444.5,82.1 448.0,82.0 451.5,82.0 455.0,82.0 458.5,82.0 462.0,82.0 465.5,82.0 469.0,82.0 472.5,82.0 476.0,82.0 479.5,82.0 483.0,82.0 486.5,82.0 490.0,82.0" fill="none" stroke="#2563eb" stroke-width="2.4" stroke-dasharray="7 5" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="70.0" y1="250.0" x2="490.0" y2="250.0" stroke="#111827" stroke-width="1.8"/>
<line x1="70.0" y1="250.0" x2="70.0" y2="32.0" stroke="#111827" stroke-width="1.8"/>
<text x="70.0" y="268.0" font-size="12" text-anchor="middle" fill="#111827">0</text>
<text x="322.0" y="268.0" font-size="14" text-anchor="middle" fill="#111827" font-style="italic">t₁</text>
<text x="280.0" y="290.0" font-size="13" text-anchor="middle" fill="#111827">Time</text>
<text x="48.0" y="145.0" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 48.0 145.0)">Rate (molecules per second)</text>
<text x="84.0" y="69.0" font-size="13" text-anchor="start" fill="#374151" font-weight="bold">Rate of evaporation</text>
<text x="170.0" y="192.0" font-size="13" text-anchor="start" fill="#2563eb" font-weight="bold">Rate of condensation</text>
</svg>
<figcaption>Figure: Rates of evaporation and condensation of water in a sealed flask</figcaption>
</figure>""",
        "question": (
            r"A sample of liquid water is sealed in an evacuated flask that is kept at constant temperature. "
            r"The graph above shows the rate of evaporation and the rate of condensation in the flask as "
            r"functions of time. Which of the following statements is best supported by the graph?"
        ),
        "options": [
            r"After time $t_1$, both evaporation and condensation have stopped, so the amount of liquid water no longer changes.",
            r"After time $t_1$, evaporation and condensation continue at equal, nonzero rates, so the pressure of $\text{H}_2\text{O}(g)$ in the flask remains constant.",
            r"Before time $t_1$, the rate of evaporation decreases because water vapor accumulates in the flask.",
            r"Before time $t_1$, the amount of liquid water remains constant because condensation occurs at the same time as evaporation.",
        ],
        "correct_index": 1,
        "explanation": (
            r"The rate of evaporation stays constant because the temperature and the surface area of the "
            r"liquid do not change. As $\text{H}_2\text{O}(g)$ accumulates, the rate of condensation "
            r"increases until, at $t_1$, it equals the rate of evaporation. Before $t_1$, evaporation is "
            r"faster than condensation, so there is a net conversion of liquid to vapor: the amount of liquid "
            r"decreases and the pressure of the vapor rises. After $t_1$, both processes continue at equal, "
            r"nonzero rates, which is dynamic equilibrium, so there is no net change and the pressure of "
            r"$\text{H}_2\text{O}(g)$ stays constant. The graph shows nonzero rates after $t_1$, so neither "
            r"process has stopped, and it shows a constant rather than a decreasing rate of evaporation "
            r"before $t_1$."
        ),
    },
    {
        "unit_q_num": 45,
        "topic_code": "7.1",
        "topic_title": "Introduction to Equilibrium",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"When aqueous solutions of $\text{Fe(NO}_3)_2$ and $\text{AgNO}_3$ are mixed, a gray deposit of "
            r"silver metal forms according to the equation $\text{Fe}^{2+}(aq) + \text{Ag}^+(aq) "
            r"\rightleftharpoons \text{Fe}^{3+}(aq) + \text{Ag}(s)$. A student claims that this reaction is "
            r"reversible. Which of the following experimental results would provide the best evidence to "
            r"support the claim?"
        ),
        "options": [
            r"Silver forms more rapidly when the two solutions are mixed at a higher temperature.",
            r"The total mass of the reaction mixture is the same before and after the silver forms.",
            r"When more $\text{AgNO}_3(aq)$ is added to a reaction mixture that contains excess $\text{Fe}^{2+}(aq)$, more silver forms.",
            r"When pure $\text{Ag}(s)$ is placed in a solution of $\text{Fe(NO}_3)_3$, $\text{Fe}^{2+}(aq)$ and $\text{Ag}^+(aq)$ are later detected in the solution.",
        ],
        "correct_index": 3,
        "explanation": (
            r"A reaction is reversible if its products can react to re-form the reactants. Starting with only "
            r"the products, $\text{Ag}(s)$ and $\text{Fe}^{3+}(aq)$, and later detecting $\text{Fe}^{2+}$ and "
            r"$\text{Ag}^+$ shows directly that the reverse reaction occurs, so the same equilibrium can be "
            r"approached from either direction (for this system $K \approx 3$ at $25^\circ\text{C}$). A "
            r"faster reaction at a higher temperature is a kinetic observation that is also true of reactions "
            r"that go to completion. Mass is conserved in every chemical reaction, reversible or not. Forming "
            r"more silver when more $\text{Ag}^+$ is added to a mixture with excess $\text{Fe}^{2+}$ would "
            r"also be observed if the reaction proceeded only in the forward direction, because $\text{Ag}^+$ "
            r"would simply be the limiting reactant."
        ),
    },
    {
        "unit_q_num": 46,
        "topic_code": "7.2",
        "topic_title": "Direction of Reversible Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 300" role="img" aria-label="Graph of reaction rate versus time with two curves. Curve X starts at a high rate and decreases; curve Y starts at zero and increases. At time t1, curve X is still well above curve Y. Later the two curves merge at the same constant rate." font-family="sans-serif" font-size="13">
<line x1="133.0" y1="250.0" x2="133.0" y2="50.0" stroke="#374151" stroke-width="1.5" stroke-dasharray="5 4"/>
<polyline points="70.0,65.2 73.5,72.0 77.0,78.4 80.5,84.4 84.0,90.1 87.5,95.5 91.0,100.5 94.5,105.3 98.0,109.8 101.5,114.0 105.0,118.0 108.5,121.7 112.0,125.2 115.5,128.6 119.0,131.7 122.5,134.6 126.0,137.4 129.5,140.0 133.0,142.5 136.5,144.8 140.0,147.0 143.5,149.1 147.0,151.1 150.5,152.9 154.0,154.6 157.5,156.2 161.0,157.8 164.5,159.2 168.0,160.6 171.5,161.9 175.0,163.1 178.5,164.2 182.0,165.3 185.5,166.3 189.0,167.3 192.5,168.2 196.0,169.0 199.5,169.8 203.0,170.6 206.5,171.3 210.0,171.9 213.5,172.6 217.0,173.1 220.5,173.7 224.0,174.2 227.5,174.7 231.0,175.2 234.5,175.6 238.0,176.0 241.5,176.4 245.0,176.8 248.5,177.2 252.0,177.5 255.5,177.8 259.0,178.1 262.5,178.3 266.0,178.6 269.5,178.8 273.0,179.1 276.5,179.3 280.0,179.5 283.5,179.7 287.0,179.9 290.5,180.0 294.0,180.2 297.5,180.3 301.0,180.5 304.5,180.6 308.0,180.7 311.5,180.9 315.0,181.0 318.5,181.1 322.0,181.2 325.5,181.3 329.0,181.4 332.5,181.4 336.0,181.5 339.5,181.6 343.0,181.7 346.5,181.7 350.0,181.8 353.5,181.9 357.0,181.9 360.5,182.0 364.0,182.0 367.5,182.1 371.0,182.1 374.5,182.1 378.0,182.2 381.5,182.2 385.0,182.2 388.5,182.3 392.0,182.3 395.5,182.3 399.0,182.4 402.5,182.4 406.0,182.4 409.5,182.4 413.0,182.5 416.5,182.5 420.0,182.5 423.5,182.5 427.0,182.5 430.5,182.5 434.0,182.6 437.5,182.6 441.0,182.6 444.5,182.6 448.0,182.6 451.5,182.6 455.0,182.6 458.5,182.6 462.0,182.7 465.5,182.7 469.0,182.7 472.5,182.7 476.0,182.7 479.5,182.7 483.0,182.7 486.5,182.7 490.0,182.7" fill="none" stroke="#111827" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
<polyline points="70.0,250.0 73.5,246.1 77.0,242.5 80.5,239.0 84.0,235.8 87.5,232.7 91.0,229.8 94.5,227.1 98.0,224.5 101.5,222.1 105.0,219.9 108.5,217.7 112.0,215.7 115.5,213.8 119.0,212.0 122.5,210.3 126.0,208.7 129.5,207.2 133.0,205.8 136.5,204.5 140.0,203.2 143.5,202.1 147.0,200.9 150.5,199.9 154.0,198.9 157.5,198.0 161.0,197.1 164.5,196.3 168.0,195.5 171.5,194.8 175.0,194.1 178.5,193.4 182.0,192.8 185.5,192.2 189.0,191.7 192.5,191.2 196.0,190.7 199.5,190.2 203.0,189.8 206.5,189.4 210.0,189.0 213.5,188.7 217.0,188.3 220.5,188.0 224.0,187.7 227.5,187.4 231.0,187.1 234.5,186.9 238.0,186.7 241.5,186.4 245.0,186.2 248.5,186.0 252.0,185.8 255.5,185.7 259.0,185.5 262.5,185.3 266.0,185.2 269.5,185.1 273.0,184.9 276.5,184.8 280.0,184.7 283.5,184.6 287.0,184.5 290.5,184.4 294.0,184.3 297.5,184.2 301.0,184.1 304.5,184.0 308.0,184.0 311.5,183.9 315.0,183.8 318.5,183.8 322.0,183.7 325.5,183.7 329.0,183.6 332.5,183.6 336.0,183.5 339.5,183.5 343.0,183.4 346.5,183.4 350.0,183.4 353.5,183.3 357.0,183.3 360.5,183.3 364.0,183.3 367.5,183.2 371.0,183.2 374.5,183.2 378.0,183.2 381.5,183.1 385.0,183.1 388.5,183.1 392.0,183.1 395.5,183.1 399.0,183.0 402.5,183.0 406.0,183.0 409.5,183.0 413.0,183.0 416.5,183.0 420.0,183.0 423.5,183.0 427.0,183.0 430.5,182.9 434.0,182.9 437.5,182.9 441.0,182.9 444.5,182.9 448.0,182.9 451.5,182.9 455.0,182.9 458.5,182.9 462.0,182.9 465.5,182.9 469.0,182.9 472.5,182.9 476.0,182.9 479.5,182.9 483.0,182.9 486.5,182.9 490.0,182.9" fill="none" stroke="#2563eb" stroke-width="2.2" stroke-dasharray="7 5" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="70.0" y1="250.0" x2="490.0" y2="250.0" stroke="#111827" stroke-width="1.8"/>
<line x1="70.0" y1="250.0" x2="70.0" y2="32.0" stroke="#111827" stroke-width="1.8"/>
<text x="70.0" y="268.0" font-size="12" text-anchor="middle" fill="#111827">0</text>
<text x="133.0" y="268.0" font-size="14" text-anchor="middle" fill="#111827" font-style="italic">t₁</text>
<text x="280.0" y="290.0" font-size="13" text-anchor="middle" fill="#111827">Time</text>
<text x="48.0" y="145.0" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 48.0 145.0)">Rate of reaction (M/s)</text>
<text x="88.0" y="74.0" font-size="14" text-anchor="start" fill="#111827" font-weight="bold">X</text>
<text x="104.0" y="244.0" font-size="14" text-anchor="start" fill="#2563eb" font-weight="bold">Y</text>
</svg>
<figcaption>Figure: Rates of the forward and reverse reactions (curves X and Y)</figcaption>
</figure>""",
        "question": (
            r"A rigid vessel at constant temperature initially contains only $\text{HI}(g)$, which reacts to "
            r"establish the equilibrium $\text{H}_2(g) + \text{I}_2(g) \rightleftharpoons 2\,\text{HI}(g)$. "
            r"The graph above shows the rates of the forward and reverse reactions as functions of time. "
            r"Which of the following correctly identifies curve X and describes the system at time $t_1$?"
        ),
        "options": [
            r"Curve X is the rate of the reverse reaction; at $t_1$ there is a net conversion of $\text{HI}$ into $\text{H}_2$ and $\text{I}_2$.",
            r"Curve X is the rate of the forward reaction; at $t_1$ there is a net conversion of $\text{HI}$ into $\text{H}_2$ and $\text{I}_2$.",
            r"Curve X is the rate of the reverse reaction; at $t_1$ there is a net conversion of $\text{H}_2$ and $\text{I}_2$ into $\text{HI}$.",
            r"Curve X is the rate of the forward reaction; at $t_1$ the system is at equilibrium because both reactions are occurring.",
        ],
        "correct_index": 0,
        "explanation": (
            r"The forward reaction, $\text{H}_2 + \text{I}_2 \rightarrow 2\,\text{HI}$, cannot occur until "
            r"some $\text{H}_2$ and $\text{I}_2$ have formed, so its rate starts at zero and increases (curve "
            r"Y). The reverse reaction, $2\,\text{HI} \rightarrow \text{H}_2 + \text{I}_2$, is fastest at the "
            r"start, when $[\text{HI}]$ is greatest, and slows as $\text{HI}$ is consumed (curve X). At $t_1$ "
            r"the reverse rate is still greater than the forward rate, so the reaction proceeds with a net "
            r"conversion of $\text{HI}$ into $\text{H}_2$ and $\text{I}_2$. Equilibrium is reached only "
            r"later, when the two curves merge and the rates are equal; the fact that both reactions are "
            r"occurring does not by itself mean that the system is at equilibrium."
        ),
    },
    {
        "unit_q_num": 47,
        "topic_code": "7.3",
        "topic_title": "Reaction Quotient and Equilibrium Constant",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 300" role="img" aria-label="Graph of reaction quotient Qc versus time in minutes for two trials. Trial 1 starts at Qc = 0 and rises; Trial 2 starts at Qc = 9 and falls. Both curves level off at Qc = 4. A dashed line marks time t1 = 0.8 min, where Trial 1 has Qc of about 1 and Trial 2 has Qc of about 5." font-family="sans-serif" font-size="13">
<line x1="70.0" y1="208.0" x2="490.0" y2="208.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70.0" y1="166.0" x2="490.0" y2="166.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70.0" y1="124.0" x2="490.0" y2="124.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70.0" y1="82.0" x2="490.0" y2="82.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70.0" y1="40.0" x2="490.0" y2="40.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="126.0" y1="250.0" x2="126.0" y2="36.0" stroke="#374151" stroke-width="1.5" stroke-dasharray="5 4"/>
<polyline points="70.0,250.0 72.8,249.2 75.6,248.3 78.4,247.5 81.2,246.6 84.0,245.7 86.8,244.7 89.6,243.8 92.4,242.8 95.2,241.8 98.0,240.8 100.8,239.7 103.6,238.7 106.4,237.6 109.2,236.5 112.0,235.4 114.8,234.2 117.6,233.1 120.4,231.9 123.2,230.7 126.0,229.5 128.8,228.3 131.6,227.1 134.4,225.9 137.2,224.6 140.0,223.4 142.8,222.1 145.6,220.9 148.4,219.6 151.2,218.4 154.0,217.1 156.8,215.8 159.6,214.6 162.4,213.3 165.2,212.1 168.0,210.8 170.8,209.6 173.6,208.4 176.4,207.2 179.2,206.0 182.0,204.8 184.8,203.6 187.6,202.5 190.4,201.4 193.2,200.2 196.0,199.1 198.8,198.1 201.6,197.0 204.4,196.0 207.2,195.0 210.0,194.0 212.8,193.0 215.6,192.0 218.4,191.1 221.2,190.2 224.0,189.3 226.8,188.5 229.6,187.6 232.4,186.8 235.2,186.0 238.0,185.3 240.8,184.5 243.6,183.8 246.4,183.1 249.2,182.4 252.0,181.8 254.8,181.1 257.6,180.5 260.4,179.9 263.2,179.4 266.0,178.8 268.8,178.3 271.6,177.8 274.4,177.3 277.2,176.8 280.0,176.3 282.8,175.9 285.6,175.5 288.4,175.1 291.2,174.7 294.0,174.3 296.8,174.0 299.6,173.6 302.4,173.3 305.2,173.0 308.0,172.7 310.8,172.4 313.6,172.1 316.4,171.8 319.2,171.6 322.0,171.3 324.8,171.1 327.6,170.8 330.4,170.6 333.2,170.4 336.0,170.2 338.8,170.0 341.6,169.8 344.4,169.7 347.2,169.5 350.0,169.3 352.8,169.2 355.6,169.0 358.4,168.9 361.2,168.8 364.0,168.7 366.8,168.5 369.6,168.4 372.4,168.3 375.2,168.2 378.0,168.1 380.8,168.0 383.6,167.9 386.4,167.8 389.2,167.7 392.0,167.7 394.8,167.6 397.6,167.5 400.4,167.4 403.2,167.4 406.0,167.3 408.8,167.2 411.6,167.2 414.4,167.1 417.2,167.1 420.0,167.0 422.8,167.0 425.6,166.9 428.4,166.9 431.2,166.9 434.0,166.8 436.8,166.8 439.6,166.7 442.4,166.7 445.2,166.7 448.0,166.6 450.8,166.6 453.6,166.6 456.4,166.6 459.2,166.5 462.0,166.5 464.8,166.5 467.6,166.5 470.4,166.4 473.2,166.4 476.0,166.4 478.8,166.4 481.6,166.4 484.4,166.3 487.2,166.3 490.0,166.3" fill="none" stroke="#111827" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>
<polyline points="70.0,61.0 72.8,70.4 75.6,78.6 78.4,85.8 81.2,92.2 84.0,97.9 86.8,103.0 89.6,107.6 92.4,111.8 95.2,115.5 98.0,119.0 100.8,122.1 103.6,124.9 106.4,127.6 109.2,130.0 112.0,132.2 114.8,134.3 117.6,136.2 120.4,138.0 123.2,139.6 126.0,141.1 128.8,142.6 131.6,143.9 134.4,145.1 137.2,146.3 140.0,147.4 142.8,148.4 145.6,149.4 148.4,150.3 151.2,151.1 154.0,151.9 156.8,152.6 159.6,153.3 162.4,154.0 165.2,154.6 168.0,155.2 170.8,155.8 173.6,156.3 176.4,156.8 179.2,157.3 182.0,157.7 184.8,158.1 187.6,158.5 190.4,158.9 193.2,159.2 196.0,159.6 198.8,159.9 201.6,160.2 204.4,160.5 207.2,160.8 210.0,161.0 212.8,161.3 215.6,161.5 218.4,161.7 221.2,161.9 224.0,162.1 226.8,162.3 229.6,162.5 232.4,162.7 235.2,162.8 238.0,163.0 240.8,163.1 243.6,163.3 246.4,163.4 249.2,163.5 252.0,163.6 254.8,163.7 257.6,163.9 260.4,164.0 263.2,164.1 266.0,164.1 268.8,164.2 271.6,164.3 274.4,164.4 277.2,164.5 280.0,164.5 282.8,164.6 285.6,164.7 288.4,164.7 291.2,164.8 294.0,164.9 296.8,164.9 299.6,165.0 302.4,165.0 305.2,165.1 308.0,165.1 310.8,165.1 313.6,165.2 316.4,165.2 319.2,165.3 322.0,165.3 324.8,165.3 327.6,165.4 330.4,165.4 333.2,165.4 336.0,165.4 338.8,165.5 341.6,165.5 344.4,165.5 347.2,165.5 350.0,165.6 352.8,165.6 355.6,165.6 358.4,165.6 361.2,165.6 364.0,165.7 366.8,165.7 369.6,165.7 372.4,165.7 375.2,165.7 378.0,165.7 380.8,165.7 383.6,165.8 386.4,165.8 389.2,165.8 392.0,165.8 394.8,165.8 397.6,165.8 400.4,165.8 403.2,165.8 406.0,165.8 408.8,165.8 411.6,165.8 414.4,165.9 417.2,165.9 420.0,165.9 422.8,165.9 425.6,165.9 428.4,165.9 431.2,165.9 434.0,165.9 436.8,165.9 439.6,165.9 442.4,165.9 445.2,165.9 448.0,165.9 450.8,165.9 453.6,165.9 456.4,165.9 459.2,165.9 462.0,165.9 464.8,165.9 467.6,165.9 470.4,165.9 473.2,165.9 476.0,166.0 478.8,166.0 481.6,166.0 484.4,166.0 487.2,166.0 490.0,166.0" fill="none" stroke="#2563eb" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="70.0" y1="250.0" x2="490.0" y2="250.0" stroke="#111827" stroke-width="1.8"/>
<line x1="70.0" y1="250.0" x2="70.0" y2="34.0" stroke="#111827" stroke-width="1.8"/>
<line x1="70.0" y1="250.0" x2="70.0" y2="255.0" stroke="#111827" stroke-width="1.5"/>
<text x="70.0" y="269.0" font-size="12" text-anchor="middle" fill="#111827">0</text>
<line x1="140.0" y1="250.0" x2="140.0" y2="255.0" stroke="#111827" stroke-width="1.5"/>
<text x="140.0" y="269.0" font-size="12" text-anchor="middle" fill="#111827">1</text>
<line x1="210.0" y1="250.0" x2="210.0" y2="255.0" stroke="#111827" stroke-width="1.5"/>
<text x="210.0" y="269.0" font-size="12" text-anchor="middle" fill="#111827">2</text>
<line x1="280.0" y1="250.0" x2="280.0" y2="255.0" stroke="#111827" stroke-width="1.5"/>
<text x="280.0" y="269.0" font-size="12" text-anchor="middle" fill="#111827">3</text>
<line x1="350.0" y1="250.0" x2="350.0" y2="255.0" stroke="#111827" stroke-width="1.5"/>
<text x="350.0" y="269.0" font-size="12" text-anchor="middle" fill="#111827">4</text>
<line x1="420.0" y1="250.0" x2="420.0" y2="255.0" stroke="#111827" stroke-width="1.5"/>
<text x="420.0" y="269.0" font-size="12" text-anchor="middle" fill="#111827">5</text>
<line x1="490.0" y1="250.0" x2="490.0" y2="255.0" stroke="#111827" stroke-width="1.5"/>
<text x="490.0" y="269.0" font-size="12" text-anchor="middle" fill="#111827">6</text>
<line x1="65.0" y1="250.0" x2="70.0" y2="250.0" stroke="#111827" stroke-width="1.5"/>
<text x="61.0" y="254.0" font-size="12" text-anchor="end" fill="#111827">0</text>
<line x1="65.0" y1="208.0" x2="70.0" y2="208.0" stroke="#111827" stroke-width="1.5"/>
<text x="61.0" y="212.0" font-size="12" text-anchor="end" fill="#111827">2</text>
<line x1="65.0" y1="166.0" x2="70.0" y2="166.0" stroke="#111827" stroke-width="1.5"/>
<text x="61.0" y="170.0" font-size="12" text-anchor="end" fill="#111827">4</text>
<line x1="65.0" y1="124.0" x2="70.0" y2="124.0" stroke="#111827" stroke-width="1.5"/>
<text x="61.0" y="128.0" font-size="12" text-anchor="end" fill="#111827">6</text>
<line x1="65.0" y1="82.0" x2="70.0" y2="82.0" stroke="#111827" stroke-width="1.5"/>
<text x="61.0" y="86.0" font-size="12" text-anchor="end" fill="#111827">8</text>
<line x1="65.0" y1="40.0" x2="70.0" y2="40.0" stroke="#111827" stroke-width="1.5"/>
<text x="61.0" y="44.0" font-size="12" text-anchor="end" fill="#111827">10</text>
<text x="126.0" y="30.0" font-size="14" text-anchor="middle" fill="#111827" font-style="italic">t₁</text>
<text x="280.0" y="290.0" font-size="13" text-anchor="middle" fill="#111827">Time (min)</text>
<text x="34.0" y="145.0" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 34.0 145.0)">Reaction quotient, Qc</text>
<text x="165.0" y="112.0" font-size="13" text-anchor="start" fill="#2563eb" font-weight="bold">Trial 2</text>
<text x="232.0" y="226.0" font-size="13" text-anchor="start" fill="#111827" font-weight="bold">Trial 1</text>
</svg>
<figcaption>Figure: Reaction quotient versus time for two trials at the same temperature</figcaption>
</figure>""",
        "question": (
            r"For the reaction $\text{A}(g) \rightleftharpoons \text{B}(g)$, two trials were carried out in "
            r"rigid containers at the same temperature. Trial 1 started with only $\text{A}(g)$, and Trial 2 "
            r"started with a mixture of $\text{A}(g)$ and $\text{B}(g)$. The graph above shows the reaction "
            r"quotient, $Q_c$, for each trial as a function of time. Which of the following statements is "
            r"correct?"
        ),
        "options": [
            r"At $t_1$, the rate of the forward reaction is greater than the rate of the reverse reaction in both trials.",
            r"The value of $K_c$ is greater for Trial 2 than for Trial 1, because Trial 2 started with product present.",
            r"At $t_1$, there is a net conversion of A into B in Trial 1 and a net conversion of B into A in Trial 2.",
            r"After the curves level off at $Q_c = 4.0$, the forward and reverse reactions have stopped in both trials.",
        ],
        "correct_index": 2,
        "explanation": (
            r"Both curves level off at the same value, so $K_c = 4.0$ in both trials; $K$ depends only on "
            r"temperature, not on the starting amounts. At $t_1$, Trial 1 has $Q_c \approx 1 < K_c$, so the "
            r"forward rate is greater than the reverse rate and there is a net conversion of A into B, which "
            r"increases $Q_c = \frac{[\text{B}]}{[\text{A}]}$. Trial 2 has $Q_c \approx 5 > K_c$, so the "
            r"reverse rate is greater and there is a net conversion of B into A, which decreases $Q_c$. A "
            r"decreasing $Q_c$ therefore signals a faster reverse reaction, not a faster forward reaction. "
            r"Once $Q_c = K_c$, both reactions continue at equal rates (dynamic equilibrium); they do not "
            r"stop."
        ),
    },
    {
        "unit_q_num": 48,
        "topic_code": "7.4",
        "topic_title": "Calculating the Equilibrium Constant",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": (
            r"A student determines $K_c$ for the reaction $\text{Fe}^{3+}(aq) + \text{SCN}^-(aq) "
            r"\rightleftharpoons \text{FeSCN}^{2+}(aq)$ by mixing known volumes of standard "
            r"$\text{Fe(NO}_3)_3$ and $\text{KSCN}$ solutions. After equilibrium is established, the student "
            r"measures the absorbance of the red $\text{FeSCN}^{2+}$ ion and uses a calibration curve to "
            r"determine $[\text{FeSCN}^{2+}]$. The equilibrium concentrations of $\text{Fe}^{3+}$ and "
            r"$\text{SCN}^-$ are then calculated by subtracting $[\text{FeSCN}^{2+}]$ from their initial "
            r"concentrations in the mixture. Unknown to the student, the cuvette contained several drops of "
            r"distilled water when the equilibrium mixture was poured into it. How does this error affect the "
            r"calculated value of $K_c$?"
        ),
        "options": [
            r"The calculated $K_c$ is too low, because the measured $[\text{FeSCN}^{2+}]$ is too low and the calculated $[\text{Fe}^{3+}]$ and $[\text{SCN}^-]$ are too high.",
            r"The calculated $K_c$ is too high, because diluting the mixture shifts the equilibrium toward $\text{FeSCN}^{2+}$.",
            r"The calculated $K_c$ is unaffected, because the value of $K_c$ depends only on temperature.",
            r"The calculated $K_c$ is unaffected, because $\text{H}_2\text{O}(l)$ does not appear in the equilibrium expression.",
        ],
        "correct_index": 0,
        "explanation": (
            r"The drops of water dilute the solution in the cuvette, so the measured absorbance, and "
            r"therefore the $[\text{FeSCN}^{2+}]$ read from the calibration curve, is too low. (Dilution also "
            r"shifts the equilibrium slightly toward $\text{Fe}^{3+}$ and $\text{SCN}^-$, not toward "
            r"$\text{FeSCN}^{2+}$, which lowers the absorbance further.) Because the student subtracts this "
            r"too-small value from the known initial concentrations, the calculated equilibrium "
            r"$[\text{Fe}^{3+}]$ and $[\text{SCN}^-]$ are too high. In $K_c = "
            r"\frac{[\text{FeSCN}^{2+}]}{[\text{Fe}^{3+}][\text{SCN}^-]}$, the numerator is too small and the "
            r"denominator is too large, so the calculated $K_c$ is too low. The true $K_c$ depends only on "
            r"temperature, but a calculated value is only as accurate as the measurements used; the absence "
            r"of water from the expression does not stop the water from diluting the solution."
        ),
    },
    {
        "unit_q_num": 49,
        "topic_code": "7.5",
        "topic_title": "Magnitude of the Equilibrium Constant",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 560 250" role="img" aria-label="Four bar graphs labeled I to IV, each showing the concentrations of A, B, and C on a common scale from 0 to 0.50 M. Graph I: A 0.30, B 0.20, C about 0. Graph II: A 0.20, B 0.10, C 0.10. Graph III: A 0.10, B about 0, C 0.20. Graph IV: A about 0, B about 0, C 0.50." font-family="sans-serif" font-size="13">
<line x1="78.0" y1="187.0" x2="188.0" y2="187.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="78.0" y1="152.0" x2="188.0" y2="152.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="78.0" y1="117.0" x2="188.0" y2="117.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="78.0" y1="82.0" x2="188.0" y2="82.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="78.0" y1="47.0" x2="188.0" y2="47.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="78.0" y1="222.0" x2="188.0" y2="222.0" stroke="#111827" stroke-width="1.8"/>
<text x="133.0" y="33.0" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">I</text>
<rect x="89.0" y="117.0" width="22.0" height="105.0" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="100.0" y="239.0" font-size="12" text-anchor="middle" fill="#111827">[A]</text>
<rect x="122.0" y="152.0" width="22.0" height="70.0" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="133.0" y="239.0" font-size="12" text-anchor="middle" fill="#111827">[B]</text>
<rect x="155.0" y="220.0" width="22.0" height="2.0" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="166.0" y="214.0" font-size="12" text-anchor="middle" fill="#374151">≈0</text>
<text x="166.0" y="239.0" font-size="12" text-anchor="middle" fill="#111827">[C]</text>
<line x1="201.0" y1="187.0" x2="311.0" y2="187.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="201.0" y1="152.0" x2="311.0" y2="152.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="201.0" y1="117.0" x2="311.0" y2="117.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="201.0" y1="82.0" x2="311.0" y2="82.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="201.0" y1="47.0" x2="311.0" y2="47.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="201.0" y1="222.0" x2="311.0" y2="222.0" stroke="#111827" stroke-width="1.8"/>
<text x="256.0" y="33.0" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">II</text>
<rect x="212.0" y="152.0" width="22.0" height="70.0" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="223.0" y="239.0" font-size="12" text-anchor="middle" fill="#111827">[A]</text>
<rect x="245.0" y="187.0" width="22.0" height="35.0" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="256.0" y="239.0" font-size="12" text-anchor="middle" fill="#111827">[B]</text>
<rect x="278.0" y="187.0" width="22.0" height="35.0" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="289.0" y="239.0" font-size="12" text-anchor="middle" fill="#111827">[C]</text>
<line x1="324.0" y1="187.0" x2="434.0" y2="187.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="324.0" y1="152.0" x2="434.0" y2="152.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="324.0" y1="117.0" x2="434.0" y2="117.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="324.0" y1="82.0" x2="434.0" y2="82.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="324.0" y1="47.0" x2="434.0" y2="47.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="324.0" y1="222.0" x2="434.0" y2="222.0" stroke="#111827" stroke-width="1.8"/>
<text x="379.0" y="33.0" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">III</text>
<rect x="335.0" y="187.0" width="22.0" height="35.0" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="346.0" y="239.0" font-size="12" text-anchor="middle" fill="#111827">[A]</text>
<rect x="368.0" y="220.0" width="22.0" height="2.0" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="379.0" y="214.0" font-size="12" text-anchor="middle" fill="#374151">≈0</text>
<text x="379.0" y="239.0" font-size="12" text-anchor="middle" fill="#111827">[B]</text>
<rect x="401.0" y="152.0" width="22.0" height="70.0" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="412.0" y="239.0" font-size="12" text-anchor="middle" fill="#111827">[C]</text>
<line x1="447.0" y1="187.0" x2="557.0" y2="187.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="447.0" y1="152.0" x2="557.0" y2="152.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="447.0" y1="117.0" x2="557.0" y2="117.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="447.0" y1="82.0" x2="557.0" y2="82.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="447.0" y1="47.0" x2="557.0" y2="47.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="447.0" y1="222.0" x2="557.0" y2="222.0" stroke="#111827" stroke-width="1.8"/>
<text x="502.0" y="33.0" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">IV</text>
<rect x="458.0" y="220.0" width="22.0" height="2.0" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="469.0" y="214.0" font-size="12" text-anchor="middle" fill="#374151">≈0</text>
<text x="469.0" y="239.0" font-size="12" text-anchor="middle" fill="#111827">[A]</text>
<rect x="491.0" y="220.0" width="22.0" height="2.0" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="502.0" y="214.0" font-size="12" text-anchor="middle" fill="#374151">≈0</text>
<text x="502.0" y="239.0" font-size="12" text-anchor="middle" fill="#111827">[B]</text>
<rect x="524.0" y="47.0" width="22.0" height="175.0" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="535.0" y="239.0" font-size="12" text-anchor="middle" fill="#111827">[C]</text>
<line x1="62.0" y1="222.0" x2="62.0" y2="41.0" stroke="#111827" stroke-width="1.8"/>
<line x1="57.0" y1="222.0" x2="62.0" y2="222.0" stroke="#111827" stroke-width="1.5"/>
<text x="54.0" y="226.0" font-size="12" text-anchor="end" fill="#111827">0.00</text>
<line x1="57.0" y1="187.0" x2="62.0" y2="187.0" stroke="#111827" stroke-width="1.5"/>
<text x="54.0" y="191.0" font-size="12" text-anchor="end" fill="#111827">0.10</text>
<line x1="57.0" y1="152.0" x2="62.0" y2="152.0" stroke="#111827" stroke-width="1.5"/>
<text x="54.0" y="156.0" font-size="12" text-anchor="end" fill="#111827">0.20</text>
<line x1="57.0" y1="117.0" x2="62.0" y2="117.0" stroke="#111827" stroke-width="1.5"/>
<text x="54.0" y="121.0" font-size="12" text-anchor="end" fill="#111827">0.30</text>
<line x1="57.0" y1="82.0" x2="62.0" y2="82.0" stroke="#111827" stroke-width="1.5"/>
<text x="54.0" y="86.0" font-size="12" text-anchor="end" fill="#111827">0.40</text>
<line x1="57.0" y1="47.0" x2="62.0" y2="47.0" stroke="#111827" stroke-width="1.5"/>
<text x="54.0" y="51.0" font-size="12" text-anchor="end" fill="#111827">0.50</text>
<text x="16.0" y="134.5" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 16.0 134.5)">Concentration (M)</text>
</svg>
<figcaption>Figure: Four possible sets of equilibrium concentrations</figcaption>
</figure>""",
        "question": (
            r"For the reaction $\text{A}(aq) + \text{B}(aq) \rightleftharpoons \text{C}(aq)$, $K_c = 1.0 "
            r"\times 10^{10}$ at $25^\circ\text{C}$. A solution is prepared at $25^\circ\text{C}$ with "
            r"initial concentrations $[\text{A}]_0 = 0.30\text{ M}$ and $[\text{B}]_0 = 0.20\text{ M}$ and no "
            r"C present. Which of the bar graphs above best represents the concentrations of A, B, and C "
            r"after the system reaches equilibrium?"
        ),
        "options": [
            r"Graph I",
            r"Graph II",
            r"Graph III",
            r"Graph IV",
        ],
        "correct_index": 2,
        "explanation": (
            r"Because $K_c = 1.0 \times 10^{10}$ is very large, the reaction proceeds essentially to "
            r"completion, limited by the reactant that runs out first. B is limiting: $0.20\text{ M}$ of B "
            r"reacts with $0.20\text{ M}$ of A to form $0.20\text{ M}$ of C, leaving $[\text{A}] = 0.30 - "
            r"0.20 = 0.10\text{ M}$. The tiny amount of B that remains can be found from $K_c$: $[\text{B}] = "
            r"\frac{[\text{C}]}{K_c[\text{A}]} = \frac{0.20}{(1.0 \times 10^{10})(0.10)} = 2.0 \times "
            r"10^{-10}\text{ M} \approx 0$. Graph III matches. Graph I shows no reaction, which would require "
            r"a very small $K$; Graph II corresponds to $K_c = \frac{0.10}{(0.20)(0.10)} = 5.0$; and Graph IV "
            r"shows more C than the limiting reactant can produce, with none of the excess A remaining."
        ),
    },
    {
        "unit_q_num": 50,
        "topic_code": "7.7",
        "topic_title": "Calculating Equilibrium Concentrations",
        "difficulty": "Challenging",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 560 345" role="img" aria-label="Four graphs labeled I to IV of concentration in molar versus time, each starting with [A] = 1.00 M and [B] = 0. Graph I: [A] falls to 0.50 and [B] rises to 0.50. Graph II: [A] falls to 0.50 and [B] rises to 1.00, both leveling off at the same time. Graph III: [A] falls to 0.25 and [B] rises to 1.50. Graph IV: [A] falls quickly to 0.50 and levels off early, while [B] rises slowly to 1.00 and is still increasing after [A] has stopped changing." font-family="sans-serif" font-size="13">
<line x1="62.0" y1="119.1" x2="242.0" y2="119.1" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62.0" y1="86.1" x2="242.0" y2="86.1" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62.0" y1="53.2" x2="242.0" y2="53.2" stroke="#e5e7eb" stroke-width="1"/>
<polyline points="62.0,86.1 64.2,90.0 66.5,93.4 68.8,96.4 71.0,99.1 73.2,101.4 75.5,103.5 77.8,105.3 80.0,106.9 82.2,108.4 84.5,109.6 86.8,110.7 89.0,111.7 91.2,112.6 93.5,113.3 95.8,114.0 98.0,114.6 100.2,115.1 102.5,115.6 104.8,116.0 107.0,116.4 109.2,116.7 111.5,117.0 113.8,117.2 116.0,117.4 118.2,117.6 120.5,117.8 122.8,117.9 125.0,118.1 127.2,118.2 129.5,118.3 131.8,118.4 134.0,118.5 136.2,118.5 138.5,118.6 140.8,118.6 143.0,118.7 145.2,118.7 147.5,118.8 149.8,118.8 152.0,118.8 154.2,118.9 156.5,118.9 158.8,118.9 161.0,118.9 163.2,118.9 165.5,119.0 167.8,119.0 170.0,119.0 172.2,119.0 174.5,119.0 176.8,119.0 179.0,119.0 181.2,119.0 183.5,119.0 185.8,119.0 188.0,119.0 190.2,119.0 192.5,119.0 194.8,119.0 197.0,119.0 199.2,119.0 201.5,119.0 203.8,119.0 206.0,119.0 208.2,119.0 210.5,119.1 212.8,119.1 215.0,119.1 217.2,119.1 219.5,119.1 221.8,119.1 224.0,119.1 226.2,119.1 228.5,119.1 230.8,119.1 233.0,119.1 235.2,119.1 237.5,119.1 239.8,119.1 242.0,119.1" fill="none" stroke="#111827" stroke-width="2.3" stroke-linejoin="round" stroke-linecap="round"/>
<polyline points="62.0,152.0 64.2,148.1 66.5,144.7 68.8,141.7 71.0,139.0 73.2,136.7 75.5,134.6 77.8,132.8 80.0,131.2 82.2,129.8 84.5,128.5 86.8,127.4 89.0,126.4 91.2,125.5 93.5,124.8 95.8,124.1 98.0,123.5 100.2,123.0 102.5,122.5 104.8,122.1 107.0,121.8 109.2,121.4 111.5,121.2 113.8,120.9 116.0,120.7 118.2,120.5 120.5,120.3 122.8,120.2 125.0,120.1 127.2,119.9 129.5,119.8 131.8,119.7 134.0,119.7 136.2,119.6 138.5,119.5 140.8,119.5 143.0,119.4 145.2,119.4 147.5,119.3 149.8,119.3 152.0,119.3 154.2,119.3 156.5,119.2 158.8,119.2 161.0,119.2 163.2,119.2 165.5,119.2 167.8,119.2 170.0,119.1 172.2,119.1 174.5,119.1 176.8,119.1 179.0,119.1 181.2,119.1 183.5,119.1 185.8,119.1 188.0,119.1 190.2,119.1 192.5,119.1 194.8,119.1 197.0,119.1 199.2,119.1 201.5,119.1 203.8,119.1 206.0,119.1 208.2,119.1 210.5,119.1 212.8,119.1 215.0,119.1 217.2,119.1 219.5,119.1 221.8,119.1 224.0,119.1 226.2,119.1 228.5,119.1 230.8,119.1 233.0,119.1 235.2,119.1 237.5,119.1 239.8,119.1 242.0,119.1" fill="none" stroke="#2563eb" stroke-width="2.3" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="62.0" y1="152.0" x2="242.0" y2="152.0" stroke="#111827" stroke-width="1.8"/>
<line x1="62.0" y1="152.0" x2="62.0" y2="36.0" stroke="#111827" stroke-width="1.8"/>
<line x1="58.0" y1="152.0" x2="62.0" y2="152.0" stroke="#111827" stroke-width="1.5"/>
<text x="55.0" y="156.0" font-size="12" text-anchor="end" fill="#111827">0.0</text>
<line x1="58.0" y1="119.1" x2="62.0" y2="119.1" stroke="#111827" stroke-width="1.5"/>
<text x="55.0" y="123.1" font-size="12" text-anchor="end" fill="#111827">0.5</text>
<line x1="58.0" y1="86.1" x2="62.0" y2="86.1" stroke="#111827" stroke-width="1.5"/>
<text x="55.0" y="90.1" font-size="12" text-anchor="end" fill="#111827">1.0</text>
<line x1="58.0" y1="53.2" x2="62.0" y2="53.2" stroke="#111827" stroke-width="1.5"/>
<text x="55.0" y="57.2" font-size="12" text-anchor="end" fill="#111827">1.5</text>
<text x="152.0" y="168.0" font-size="12" text-anchor="middle" fill="#111827">Time</text>
<text x="28.0" y="96.0" font-size="12" text-anchor="middle" fill="#111827" transform="rotate(-90 28.0 96.0)">Conc. (M)</text>
<text x="152.0" y="28.0" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">I</text>
<text x="71.0" y="79.1" font-size="12" text-anchor="start" fill="#111827" font-weight="bold">[A]</text>
<text x="104.0" y="146.0" font-size="12" text-anchor="start" fill="#2563eb" font-weight="bold">[B]</text>
<text x="246.0" y="123.1" font-size="12" text-anchor="start" fill="#111827">0.50</text>
<line x1="340.0" y1="119.1" x2="520.0" y2="119.1" stroke="#e5e7eb" stroke-width="1"/>
<line x1="340.0" y1="86.1" x2="520.0" y2="86.1" stroke="#e5e7eb" stroke-width="1"/>
<line x1="340.0" y1="53.2" x2="520.0" y2="53.2" stroke="#e5e7eb" stroke-width="1"/>
<polyline points="340.0,86.1 342.2,90.0 344.5,93.4 346.8,96.4 349.0,99.1 351.2,101.4 353.5,103.5 355.8,105.3 358.0,106.9 360.2,108.4 362.5,109.6 364.8,110.7 367.0,111.7 369.2,112.6 371.5,113.3 373.8,114.0 376.0,114.6 378.2,115.1 380.5,115.6 382.8,116.0 385.0,116.4 387.2,116.7 389.5,117.0 391.8,117.2 394.0,117.4 396.2,117.6 398.5,117.8 400.8,117.9 403.0,118.1 405.2,118.2 407.5,118.3 409.8,118.4 412.0,118.5 414.2,118.5 416.5,118.6 418.8,118.6 421.0,118.7 423.2,118.7 425.5,118.8 427.8,118.8 430.0,118.8 432.2,118.9 434.5,118.9 436.8,118.9 439.0,118.9 441.2,118.9 443.5,119.0 445.8,119.0 448.0,119.0 450.2,119.0 452.5,119.0 454.8,119.0 457.0,119.0 459.2,119.0 461.5,119.0 463.8,119.0 466.0,119.0 468.2,119.0 470.5,119.0 472.8,119.0 475.0,119.0 477.2,119.0 479.5,119.0 481.8,119.0 484.0,119.0 486.2,119.0 488.5,119.1 490.8,119.1 493.0,119.1 495.2,119.1 497.5,119.1 499.8,119.1 502.0,119.1 504.2,119.1 506.5,119.1 508.8,119.1 511.0,119.1 513.2,119.1 515.5,119.1 517.8,119.1 520.0,119.1" fill="none" stroke="#111827" stroke-width="2.3" stroke-linejoin="round" stroke-linecap="round"/>
<polyline points="340.0,152.0 342.2,144.3 344.5,137.4 346.8,131.4 349.0,126.1 351.2,121.4 353.5,117.2 355.8,113.6 358.0,110.4 360.2,107.5 362.5,105.0 364.8,102.8 367.0,100.8 369.2,99.1 371.5,97.6 373.8,96.2 376.0,95.0 378.2,94.0 380.5,93.1 382.8,92.2 385.0,91.5 387.2,90.9 389.5,90.3 391.8,89.8 394.0,89.4 396.2,89.0 398.5,88.7 400.8,88.4 403.0,88.1 405.2,87.9 407.5,87.7 409.8,87.5 412.0,87.3 414.2,87.2 416.5,87.1 418.8,86.9 421.0,86.8 423.2,86.8 425.5,86.7 427.8,86.6 430.0,86.6 432.2,86.5 434.5,86.5 436.8,86.4 439.0,86.4 441.2,86.4 443.5,86.3 445.8,86.3 448.0,86.3 450.2,86.3 452.5,86.2 454.8,86.2 457.0,86.2 459.2,86.2 461.5,86.2 463.8,86.2 466.0,86.2 468.2,86.2 470.5,86.2 472.8,86.2 475.0,86.2 477.2,86.1 479.5,86.1 481.8,86.1 484.0,86.1 486.2,86.1 488.5,86.1 490.8,86.1 493.0,86.1 495.2,86.1 497.5,86.1 499.8,86.1 502.0,86.1 504.2,86.1 506.5,86.1 508.8,86.1 511.0,86.1 513.2,86.1 515.5,86.1 517.8,86.1 520.0,86.1" fill="none" stroke="#2563eb" stroke-width="2.3" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="340.0" y1="152.0" x2="520.0" y2="152.0" stroke="#111827" stroke-width="1.8"/>
<line x1="340.0" y1="152.0" x2="340.0" y2="36.0" stroke="#111827" stroke-width="1.8"/>
<line x1="336.0" y1="152.0" x2="340.0" y2="152.0" stroke="#111827" stroke-width="1.5"/>
<text x="333.0" y="156.0" font-size="12" text-anchor="end" fill="#111827">0.0</text>
<line x1="336.0" y1="119.1" x2="340.0" y2="119.1" stroke="#111827" stroke-width="1.5"/>
<text x="333.0" y="123.1" font-size="12" text-anchor="end" fill="#111827">0.5</text>
<line x1="336.0" y1="86.1" x2="340.0" y2="86.1" stroke="#111827" stroke-width="1.5"/>
<text x="333.0" y="90.1" font-size="12" text-anchor="end" fill="#111827">1.0</text>
<line x1="336.0" y1="53.2" x2="340.0" y2="53.2" stroke="#111827" stroke-width="1.5"/>
<text x="333.0" y="57.2" font-size="12" text-anchor="end" fill="#111827">1.5</text>
<text x="430.0" y="168.0" font-size="12" text-anchor="middle" fill="#111827">Time</text>
<text x="306.0" y="96.0" font-size="12" text-anchor="middle" fill="#111827" transform="rotate(-90 306.0 96.0)">Conc. (M)</text>
<text x="430.0" y="28.0" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">II</text>
<text x="349.0" y="79.1" font-size="12" text-anchor="start" fill="#111827" font-weight="bold">[A]</text>
<text x="382.0" y="146.0" font-size="12" text-anchor="start" fill="#2563eb" font-weight="bold">[B]</text>
<text x="524.0" y="123.1" font-size="12" text-anchor="start" fill="#111827">0.50</text>
<text x="524.0" y="90.1" font-size="12" text-anchor="start" fill="#2563eb">1.00</text>
<line x1="62.0" y1="289.1" x2="242.0" y2="289.1" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62.0" y1="256.1" x2="242.0" y2="256.1" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62.0" y1="223.2" x2="242.0" y2="223.2" stroke="#e5e7eb" stroke-width="1"/>
<polyline points="62.0,256.1 64.2,261.9 66.5,267.0 68.8,271.6 71.0,275.6 73.2,279.1 75.5,282.2 77.8,284.9 80.0,287.4 82.2,289.5 84.5,291.4 86.8,293.0 89.0,294.5 91.2,295.8 93.5,296.9 95.8,298.0 98.0,298.8 100.2,299.6 102.5,300.3 104.8,300.9 107.0,301.5 109.2,302.0 111.5,302.4 113.8,302.7 116.0,303.1 118.2,303.4 120.5,303.6 122.8,303.8 125.0,304.0 127.2,304.2 129.5,304.4 131.8,304.5 134.0,304.6 136.2,304.7 138.5,304.8 140.8,304.9 143.0,305.0 145.2,305.0 147.5,305.1 149.8,305.2 152.0,305.2 154.2,305.2 156.5,305.3 158.8,305.3 161.0,305.3 163.2,305.4 165.5,305.4 167.8,305.4 170.0,305.4 172.2,305.4 174.5,305.4 176.8,305.4 179.0,305.5 181.2,305.5 183.5,305.5 185.8,305.5 188.0,305.5 190.2,305.5 192.5,305.5 194.8,305.5 197.0,305.5 199.2,305.5 201.5,305.5 203.8,305.5 206.0,305.5 208.2,305.5 210.5,305.5 212.8,305.5 215.0,305.5 217.2,305.5 219.5,305.5 221.8,305.5 224.0,305.5 226.2,305.5 228.5,305.5 230.8,305.5 233.0,305.5 235.2,305.5 237.5,305.5 239.8,305.5 242.0,305.5" fill="none" stroke="#111827" stroke-width="2.3" stroke-linejoin="round" stroke-linecap="round"/>
<polyline points="62.0,322.0 64.2,310.4 66.5,300.1 68.8,291.1 71.0,283.1 73.2,276.1 75.5,269.9 77.8,264.4 80.0,259.5 82.2,255.3 84.5,251.5 86.8,248.2 89.0,245.2 91.2,242.6 93.5,240.3 95.8,238.3 98.0,236.6 100.2,235.0 102.5,233.6 104.8,232.4 107.0,231.3 109.2,230.3 111.5,229.5 113.8,228.8 116.0,228.1 118.2,227.5 120.5,227.0 122.8,226.6 125.0,226.2 127.2,225.8 129.5,225.5 131.8,225.2 134.0,225.0 136.2,224.8 138.5,224.6 140.8,224.4 143.0,224.3 145.2,224.1 147.5,224.0 149.8,223.9 152.0,223.8 154.2,223.8 156.5,223.7 158.8,223.6 161.0,223.6 163.2,223.5 165.5,223.5 167.8,223.5 170.0,223.4 172.2,223.4 174.5,223.4 176.8,223.3 179.0,223.3 181.2,223.3 183.5,223.3 185.8,223.3 188.0,223.3 190.2,223.3 192.5,223.2 194.8,223.2 197.0,223.2 199.2,223.2 201.5,223.2 203.8,223.2 206.0,223.2 208.2,223.2 210.5,223.2 212.8,223.2 215.0,223.2 217.2,223.2 219.5,223.2 221.8,223.2 224.0,223.2 226.2,223.2 228.5,223.2 230.8,223.2 233.0,223.2 235.2,223.2 237.5,223.2 239.8,223.2 242.0,223.2" fill="none" stroke="#2563eb" stroke-width="2.3" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="62.0" y1="322.0" x2="242.0" y2="322.0" stroke="#111827" stroke-width="1.8"/>
<line x1="62.0" y1="322.0" x2="62.0" y2="206.0" stroke="#111827" stroke-width="1.8"/>
<line x1="58.0" y1="322.0" x2="62.0" y2="322.0" stroke="#111827" stroke-width="1.5"/>
<text x="55.0" y="326.0" font-size="12" text-anchor="end" fill="#111827">0.0</text>
<line x1="58.0" y1="289.1" x2="62.0" y2="289.1" stroke="#111827" stroke-width="1.5"/>
<text x="55.0" y="293.1" font-size="12" text-anchor="end" fill="#111827">0.5</text>
<line x1="58.0" y1="256.1" x2="62.0" y2="256.1" stroke="#111827" stroke-width="1.5"/>
<text x="55.0" y="260.1" font-size="12" text-anchor="end" fill="#111827">1.0</text>
<line x1="58.0" y1="223.2" x2="62.0" y2="223.2" stroke="#111827" stroke-width="1.5"/>
<text x="55.0" y="227.2" font-size="12" text-anchor="end" fill="#111827">1.5</text>
<text x="152.0" y="338.0" font-size="12" text-anchor="middle" fill="#111827">Time</text>
<text x="28.0" y="266.0" font-size="12" text-anchor="middle" fill="#111827" transform="rotate(-90 28.0 266.0)">Conc. (M)</text>
<text x="152.0" y="198.0" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">III</text>
<text x="71.0" y="249.1" font-size="12" text-anchor="start" fill="#111827" font-weight="bold">[A]</text>
<text x="104.0" y="316.0" font-size="12" text-anchor="start" fill="#2563eb" font-weight="bold">[B]</text>
<text x="246.0" y="309.5" font-size="12" text-anchor="start" fill="#111827">0.25</text>
<text x="246.0" y="227.2" font-size="12" text-anchor="start" fill="#2563eb">1.50</text>
<line x1="340.0" y1="289.1" x2="520.0" y2="289.1" stroke="#e5e7eb" stroke-width="1"/>
<line x1="340.0" y1="256.1" x2="520.0" y2="256.1" stroke="#e5e7eb" stroke-width="1"/>
<line x1="340.0" y1="223.2" x2="520.0" y2="223.2" stroke="#e5e7eb" stroke-width="1"/>
<polyline points="340.0,256.1 342.2,262.8 344.5,268.1 346.8,272.4 349.0,275.8 351.2,278.5 353.5,280.6 355.8,282.3 358.0,283.7 360.2,284.8 362.5,285.7 364.8,286.4 367.0,286.9 369.2,287.3 371.5,287.7 373.8,288.0 376.0,288.2 378.2,288.4 380.5,288.5 382.8,288.6 385.0,288.7 387.2,288.8 389.5,288.8 391.8,288.9 394.0,288.9 396.2,288.9 398.5,289.0 400.8,289.0 403.0,289.0 405.2,289.0 407.5,289.0 409.8,289.0 412.0,289.0 414.2,289.0 416.5,289.0 418.8,289.0 421.0,289.0 423.2,289.1 425.5,289.1 427.8,289.1 430.0,289.1 432.2,289.1 434.5,289.1 436.8,289.1 439.0,289.1 441.2,289.1 443.5,289.1 445.8,289.1 448.0,289.1 450.2,289.1 452.5,289.1 454.8,289.1 457.0,289.1 459.2,289.1 461.5,289.1 463.8,289.1 466.0,289.1 468.2,289.1 470.5,289.1 472.8,289.1 475.0,289.1 477.2,289.1 479.5,289.1 481.8,289.1 484.0,289.1 486.2,289.1 488.5,289.1 490.8,289.1 493.0,289.1 495.2,289.1 497.5,289.1 499.8,289.1 502.0,289.1 504.2,289.1 506.5,289.1 508.8,289.1 511.0,289.1 513.2,289.1 515.5,289.1 517.8,289.1 520.0,289.1" fill="none" stroke="#111827" stroke-width="2.3" stroke-linejoin="round" stroke-linecap="round"/>
<polyline points="340.0,322.0 342.2,318.0 344.5,314.3 346.8,310.7 349.0,307.4 351.2,304.3 353.5,301.4 355.8,298.7 358.0,296.1 360.2,293.7 362.5,291.4 364.8,289.2 367.0,287.2 369.2,285.4 371.5,283.6 373.8,281.9 376.0,280.4 378.2,278.9 380.5,277.5 382.8,276.2 385.0,275.0 387.2,273.8 389.5,272.8 391.8,271.8 394.0,270.8 396.2,269.9 398.5,269.1 400.8,268.3 403.0,267.6 405.2,266.9 407.5,266.2 409.8,265.6 412.0,265.0 414.2,264.5 416.5,264.0 418.8,263.5 421.0,263.1 423.2,262.6 425.5,262.2 427.8,261.9 430.0,261.5 432.2,261.2 434.5,260.9 436.8,260.6 439.0,260.3 441.2,260.1 443.5,259.8 445.8,259.6 448.0,259.4 450.2,259.2 452.5,259.0 454.8,258.8 457.0,258.7 459.2,258.5 461.5,258.4 463.8,258.2 466.0,258.1 468.2,258.0 470.5,257.9 472.8,257.8 475.0,257.7 477.2,257.6 479.5,257.5 481.8,257.4 484.0,257.3 486.2,257.3 488.5,257.2 490.8,257.1 493.0,257.1 495.2,257.0 497.5,256.9 499.8,256.9 502.0,256.8 504.2,256.8 506.5,256.8 508.8,256.7 511.0,256.7 513.2,256.7 515.5,256.6 517.8,256.6 520.0,256.6" fill="none" stroke="#2563eb" stroke-width="2.3" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="340.0" y1="322.0" x2="520.0" y2="322.0" stroke="#111827" stroke-width="1.8"/>
<line x1="340.0" y1="322.0" x2="340.0" y2="206.0" stroke="#111827" stroke-width="1.8"/>
<line x1="336.0" y1="322.0" x2="340.0" y2="322.0" stroke="#111827" stroke-width="1.5"/>
<text x="333.0" y="326.0" font-size="12" text-anchor="end" fill="#111827">0.0</text>
<line x1="336.0" y1="289.1" x2="340.0" y2="289.1" stroke="#111827" stroke-width="1.5"/>
<text x="333.0" y="293.1" font-size="12" text-anchor="end" fill="#111827">0.5</text>
<line x1="336.0" y1="256.1" x2="340.0" y2="256.1" stroke="#111827" stroke-width="1.5"/>
<text x="333.0" y="260.1" font-size="12" text-anchor="end" fill="#111827">1.0</text>
<line x1="336.0" y1="223.2" x2="340.0" y2="223.2" stroke="#111827" stroke-width="1.5"/>
<text x="333.0" y="227.2" font-size="12" text-anchor="end" fill="#111827">1.5</text>
<text x="430.0" y="338.0" font-size="12" text-anchor="middle" fill="#111827">Time</text>
<text x="306.0" y="266.0" font-size="12" text-anchor="middle" fill="#111827" transform="rotate(-90 306.0 266.0)">Conc. (M)</text>
<text x="430.0" y="198.0" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">IV</text>
<text x="349.0" y="249.1" font-size="12" text-anchor="start" fill="#111827" font-weight="bold">[A]</text>
<text x="382.0" y="316.0" font-size="12" text-anchor="start" fill="#2563eb" font-weight="bold">[B]</text>
<text x="524.0" y="293.1" font-size="12" text-anchor="start" fill="#111827">0.50</text>
<text x="524.0" y="260.1" font-size="12" text-anchor="start" fill="#2563eb">1.00</text>
</svg>
<figcaption>Figure: [A] (black) and [B] (blue) versus time</figcaption>
</figure>""",
        "question": (
            r"Pure $\text{A}(g)$ is placed in a rigid container at an initial concentration of $1.00\text{ "
            r"M}$ and reacts according to the equation $\text{A}(g) \rightleftharpoons 2\,\text{B}(g)$, for "
            r"which $K_c = 2.0$ at the temperature of the experiment. Which of the graphs above correctly "
            r"shows $[\text{A}]$ and $[\text{B}]$ as functions of time as the system approaches equilibrium?"
        ),
        "options": [
            r"Graph I",
            r"Graph II",
            r"Graph III",
            r"Graph IV",
        ],
        "correct_index": 1,
        "explanation": (
            r"From the stoichiometry, $[\text{A}] = 1.00 - x$ and $[\text{B}] = 2x$ at every moment, so "
            r"$[\text{B}]$ must rise twice as fast as $[\text{A}]$ falls, and both must stop changing at the "
            r"same time. At equilibrium, $K_c = \frac{(2x)^2}{1.00 - x} = 2.0$, which gives $2x^2 + x - 1 = "
            r"0$ and $x = 0.50$. Thus $[\text{A}] = 0.50\text{ M}$ and $[\text{B}] = 1.00\text{ M}$ (check: "
            r"$\frac{(1.00)^2}{0.50} = 2.0$), as shown in Graph II. Graph I shows a 1 : 1 change and gives "
            r"$\frac{(0.50)^2}{0.50} = 0.50$; Graph III has the correct 1 : 2 ratio but gives "
            r"$\frac{(1.50)^2}{0.25} = 9.0$; Graph IV has the correct final values, but $[\text{B}]$ keeps "
            r"changing after $[\text{A}]$ has leveled off, which the 1 : 2 stoichiometry does not allow."
        ),
    },
    {
        "unit_q_num": 51,
        "topic_code": "7.8",
        "topic_title": "Representations of Equilibrium",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 540 250" role="img" aria-label="Three identical boxes of gas molecules with a key: A2 is two dark atoms, B2 is two white atoms, and AB is one dark and one white atom. Box 1 contains 3 A2, 3 B2, and 2 AB. Box 2 contains 1 A2, 2 B2, and 4 AB. Box 3 contains 2 A2, 2 B2, and 4 AB." font-family="sans-serif" font-size="13">
<circle cx="113.0" cy="22.0" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="127.0" cy="22.0" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<text x="140.0" y="27.0" font-size="13" text-anchor="start" fill="#111827">A₂</text>
<circle cx="223.0" cy="22.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="237.0" cy="22.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<text x="250.0" y="27.0" font-size="13" text-anchor="start" fill="#111827">B₂</text>
<circle cx="333.0" cy="22.0" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="347.0" cy="22.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<text x="360.0" y="27.0" font-size="13" text-anchor="start" fill="#111827">AB</text>
<rect x="20.0" y="50.0" width="150.0" height="150.0" fill="#ffffff" stroke="#111827" stroke-width="2"/>
<circle cx="33.4" cy="76.6" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="46.6" cy="81.4" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="95.3" cy="76.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="106.7" cy="68.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="143.0" cy="62.0" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="143.0" cy="76.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="42.0" cy="131.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="56.0" cy="131.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="85.5" cy="116.9" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="92.5" cy="129.1" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="45.1" cy="165.1" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="54.9" cy="174.9" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="88.6" cy="186.6" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="93.4" cy="173.4" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="140.1" cy="171.8" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="153.9" cy="174.2" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<text x="95.0" y="222.0" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">Box 1</text>
<rect x="195.0" y="50.0" width="150.0" height="150.0" fill="#ffffff" stroke="#111827" stroke-width="2"/>
<circle cx="212.3" cy="73.0" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="223.7" cy="65.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="274.0" cy="74.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="274.0" cy="88.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="219.5" cy="121.9" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="226.5" cy="134.1" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="268.2" cy="121.8" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="281.8" cy="118.2" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="311.1" cy="125.1" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="320.9" cy="134.9" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="258.1" cy="177.8" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="271.9" cy="180.2" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="319.4" cy="169.6" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="332.6" cy="174.4" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<text x="270.0" y="222.0" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">Box 2</text>
<rect x="370.0" y="50.0" width="150.0" height="150.0" fill="#ffffff" stroke="#111827" stroke-width="2"/>
<circle cx="389.0" cy="66.0" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="389.0" cy="80.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="441.0" cy="78.0" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="455.0" cy="78.0" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="496.5" cy="63.9" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="503.5" cy="76.1" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="442.1" cy="118.1" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="451.9" cy="127.9" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="487.6" cy="135.6" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="492.4" cy="122.4" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="394.1" cy="170.8" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="407.9" cy="173.2" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="436.4" cy="166.6" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="449.6" cy="171.4" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="493.3" cy="185.0" r="8" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="504.7" cy="177.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<text x="445.0" y="222.0" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">Box 3</text>
</svg>
<figcaption>Figure: Three mixtures in identical containers at the same temperature</figcaption>
</figure>""",
        "question": (
            r"The diagrams above represent three mixtures of $\text{A}_2(g)$, $\text{B}_2(g)$, and "
            r"$\text{AB}(g)$ in identical rigid containers at the same temperature. For the reaction "
            r"$\text{A}_2(g) + \text{B}_2(g) \rightleftharpoons 2\,\text{AB}(g)$, $K_c = 4.0$ at this "
            r"temperature. Which of the following correctly predicts the net reaction, if any, that occurs in "
            r"each container as the mixture approaches equilibrium?"
        ),
        "options": [
            r"Box 1: net forward reaction; Box 2: no net change; Box 3: net forward reaction",
            r"Box 1: net forward reaction; Box 2: net forward reaction; Box 3: net forward reaction",
            r"Box 1: net reverse reaction; Box 2: net forward reaction; Box 3: no net change",
            r"Box 1: net forward reaction; Box 2: net reverse reaction; Box 3: no net change",
        ],
        "correct_index": 3,
        "explanation": (
            r"Because there are equal numbers of gas molecules on the two sides of the equation, the volume "
            r"cancels and $Q_c$ can be calculated directly from the particle counts: $Q_c = "
            r"\frac{(n_{\text{AB}})^2}{(n_{\text{A}_2})(n_{\text{B}_2})}$. Box 1: $\frac{2^2}{(3)(3)} = 0.44 "
            r"< 4.0$, so there is a net forward reaction. Box 2: $\frac{4^2}{(1)(2)} = 8.0 > 4.0$, so there "
            r"is a net reverse reaction. Box 3: $\frac{4^2}{(2)(2)} = 4.0 = K_c$, so the mixture is already "
            r"at equilibrium and no net change occurs. Forgetting to square $n_{\text{AB}}$ makes every box "
            r"appear to react in the forward direction, multiplying by the coefficient 2 instead of squaring "
            r"makes Box 2 appear to be at equilibrium, and reversing the meaning of $Q_c < K_c$ swaps the "
            r"directions for Boxes 1 and 2."
        ),
    },
    {
        "unit_q_num": 52,
        "topic_code": "7.8",
        "topic_title": "Representations of Equilibrium",
        "difficulty": "Challenging",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 500 270" role="img" aria-label="Two particulate diagrams of a 1.0 liter container with a key: a bent molecule of one dark N atom and two white O atoms is NO2; two joined N atoms each bonded to two O atoms is N2O4. Before reaction the container holds 10 NO2 molecules. At equilibrium it holds 4 NO2 molecules and 3 N2O4 molecules." font-family="sans-serif" font-size="13">
<g transform="translate(130.0 24.0) rotate(0)"><circle cx="-10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="0.0" cy="-1.5" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<text x="148.0" y="29.0" font-size="13" text-anchor="start" fill="#111827">= NO₂</text>
<g transform="translate(250.0 24.0) rotate(0)"><circle cx="-13.0" cy="-10.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="-13.0" cy="10.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="13.0" cy="-10.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="13.0" cy="10.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="-6.5" cy="0.0" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="6.5" cy="0.0" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<text x="276.0" y="29.0" font-size="13" text-anchor="start" fill="#111827">= N₂O₄</text>
<circle cx="372.0" cy="24.0" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<text x="383.0" y="29.0" font-size="13" text-anchor="start" fill="#111827">N</text>
<circle cx="412.0" cy="24.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<text x="423.0" y="29.0" font-size="13" text-anchor="start" fill="#111827">O</text>
<rect x="30.0" y="55.0" width="180.0" height="180.0" fill="#ffffff" stroke="#111827" stroke-width="2"/>
<rect x="290.0" y="55.0" width="180.0" height="180.0" fill="#ffffff" stroke="#111827" stroke-width="2"/>
<g transform="translate(55.5 81.0) rotate(0)"><circle cx="-10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="0.0" cy="-1.5" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<g transform="translate(93.5 88.0) rotate(40)"><circle cx="-10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="0.0" cy="-1.5" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<g transform="translate(144.5 90.0) rotate(-30)"><circle cx="-10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="0.0" cy="-1.5" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<g transform="translate(184.5 83.0) rotate(75)"><circle cx="-10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="0.0" cy="-1.5" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<g transform="translate(56.5 147.0) rotate(15)"><circle cx="-10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="0.0" cy="-1.5" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<g transform="translate(140.5 140.0) rotate(100)"><circle cx="-10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="0.0" cy="-1.5" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<g transform="translate(190.5 149.0) rotate(20)"><circle cx="-10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="0.0" cy="-1.5" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<g transform="translate(48.5 206.0) rotate(-15)"><circle cx="-10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="0.0" cy="-1.5" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<g transform="translate(99.5 202.0) rotate(55)"><circle cx="-10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="0.0" cy="-1.5" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<g transform="translate(184.5 209.0) rotate(-40)"><circle cx="-10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="0.0" cy="-1.5" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<g transform="translate(316.0 87.0) rotate(20)"><circle cx="-13.0" cy="-10.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="-13.0" cy="10.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="13.0" cy="-10.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="13.0" cy="10.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="-6.5" cy="0.0" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="6.5" cy="0.0" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<g transform="translate(385.0 81.0) rotate(-20)"><circle cx="-10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="0.0" cy="-1.5" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<g transform="translate(323.0 150.0) rotate(70)"><circle cx="-10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="0.0" cy="-1.5" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<g transform="translate(378.0 142.0) rotate(-35)"><circle cx="-13.0" cy="-10.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="-13.0" cy="10.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="13.0" cy="-10.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="13.0" cy="10.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="-6.5" cy="0.0" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="6.5" cy="0.0" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<g transform="translate(444.0 148.0) rotate(10)"><circle cx="-10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="0.0" cy="-1.5" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<g transform="translate(375.0 203.0) rotate(120)"><circle cx="-10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="10.4" cy="5.2" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="0.0" cy="-1.5" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<g transform="translate(443.0 207.0) rotate(50)"><circle cx="-13.0" cy="-10.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="-13.0" cy="10.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="13.0" cy="-10.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="13.0" cy="10.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><circle cx="-6.5" cy="0.0" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="6.5" cy="0.0" r="6.5" fill="#374151" stroke="#111827" stroke-width="1.5"/></g>
<line x1="222.0" y1="145.0" x2="270.0" y2="145.0" stroke="#111827" stroke-width="2"/>
<polygon points="278,145 266,139 266,151" fill="#111827"/>
<text x="120.0" y="258.0" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">Before reaction</text>
<text x="380.0" y="258.0" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">At equilibrium</text>
</svg>
<figcaption>Figure: Container contents before reaction and at equilibrium</figcaption>
</figure>""",
        "question": (
            r"The diagrams above represent the contents of a rigid $1.0\text{ L}$ container before reaction, "
            r"when it holds only $\text{NO}_2(g)$, and after the system $2\,\text{NO}_2(g) \rightleftharpoons "
            r"\text{N}_2\text{O}_4(g)$ has reached equilibrium at constant temperature. Each molecule shown "
            r"represents $0.10\text{ mol}$. What is the value of $K_c$ for the reaction at this temperature?"
        ),
        "options": [
            r"$1.9$",
            r"$0.75$",
            r"$0.53$",
            r"$0.19$",
        ],
        "correct_index": 0,
        "explanation": (
            r"Convert the particle counts to concentrations. At equilibrium there are 4 $\text{NO}_2$ "
            r"molecules ($0.40\text{ mol}$) and 3 $\text{N}_2\text{O}_4$ molecules ($0.30\text{ mol}$) in "
            r"$1.0\text{ L}$, so $[\text{NO}_2] = 0.40\text{ M}$ and $[\text{N}_2\text{O}_4] = 0.30\text{ "
            r"M}$. (Check: forming 3 $\text{N}_2\text{O}_4$ uses 6 of the original 10 $\text{NO}_2$, leaving "
            r"4.) Then $K_c = \frac{[\text{N}_2\text{O}_4]}{[\text{NO}_2]^2} = \frac{0.30}{(0.40)^2} = 1.9$. "
            r"Using the raw particle counts, $\frac{3}{4^2} = 0.19$, is not valid here: because the number of "
            r"gas molecules changes in the reaction, the factor of $0.10\text{ mol}$ per particle does not "
            r"cancel. The value $0.75$ results from not squaring $[\text{NO}_2]$, and $0.53$ is $K_c$ for the "
            r"reverse reaction."
        ),
    },
    {
        "unit_q_num": 53,
        "topic_code": "7.9",
        "topic_title": "Introduction to Le Châtelier's Principle",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": (
            r"An orange solution contains the equilibrium $\text{Cr}_2\text{O}_7^{2-}(aq) + "
            r"\text{H}_2\text{O}(l) \rightleftharpoons 2\,\text{CrO}_4^{2-}(aq) + 2\,\text{H}^+(aq)$, in "
            r"which $\text{Cr}_2\text{O}_7^{2-}$ is orange and $\text{CrO}_4^{2-}$ is yellow. A small amount "
            r"of solid $\text{Ba(NO}_3)_2$ is dissolved in the solution, and a yellow precipitate of "
            r"$\text{BaCrO}_4(s)$ forms. Which of the following correctly predicts how the solution above the "
            r"precipitate changes as equilibrium is re-established?"
        ),
        "options": [
            r"The orange color becomes less intense, and the pH decreases.",
            r"The orange color becomes less intense, and the pH increases.",
            r"The orange color becomes more intense, and the pH decreases.",
            r"The orange color becomes more intense, and the pH increases.",
        ],
        "correct_index": 0,
        "explanation": (
            r"Barium ions remove $\text{CrO}_4^{2-}$ from solution as $\text{BaCrO}_4(s)$. Lowering "
            r"$[\text{CrO}_4^{2-}]$ makes $Q = "
            r"\frac{[\text{CrO}_4^{2-}]^2[\text{H}^+]^2}{[\text{Cr}_2\text{O}_7^{2-}]}$ smaller than $K$ "
            r"(water is omitted as a pure liquid), so the system shifts in the forward direction to partially "
            r"replace the chromate. The forward reaction consumes orange $\text{Cr}_2\text{O}_7^{2-}$, so the "
            r"orange color fades, and it produces $\text{H}^+$, so $[\text{H}^+]$ increases and the pH "
            r"decreases. Predicting a pH increase confuses $[\text{H}^+]$ with pH: a higher $[\text{H}^+]$ "
            r"means a lower pH. Predicting a more intense orange color reverses the direction of the shift; "
            r"the stress is the removal of a product, which drives the forward reaction."
        ),
    },
    {
        "unit_q_num": 54,
        "topic_code": "7.10",
        "topic_title": "Reaction Quotient and Le Châtelier's Principle",
        "difficulty": "Challenging",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 580 330" role="img" aria-label="Particulate diagrams in piston-cylinders with a key: dark atom A, white atom B, and joined dark-white molecule AB. The initial equilibrium mixture at volume V contains 5 A, 6 B, and 3 AB. Four cylinders at volume V/2: I contains 5 A, 6 B, 3 AB; II contains 6 A, 7 B, 2 AB; III contains 3 A, 4 B, 5 AB; IV contains 4 A, 5 B, 4 AB." font-family="sans-serif" font-size="13">
<circle cx="30.0" cy="22.0" r="6" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<text x="41.0" y="27.0" font-size="13" text-anchor="start" fill="#111827">A</text>
<circle cx="72.0" cy="22.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<text x="83.0" y="27.0" font-size="13" text-anchor="start" fill="#111827">B</text>
<circle cx="118.0" cy="22.0" r="6" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="126.0" cy="22.0" r="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<text x="138.0" y="27.0" font-size="13" text-anchor="start" fill="#111827">AB</text>
<text x="398.0" y="22.0" font-size="13" text-anchor="middle" fill="#111827">Diagrams I–IV: volume = V/2</text>
<line x1="20.0" y1="92.0" x2="20.0" y2="300.0" stroke="#111827" stroke-width="2.2"/>
<line x1="180.0" y1="92.0" x2="180.0" y2="300.0" stroke="#111827" stroke-width="2.2"/>
<line x1="20.0" y1="300.0" x2="180.0" y2="300.0" stroke="#111827" stroke-width="2.2"/>
<rect x="21.5" y="129.0" width="157.0" height="11.0" fill="#9ca3af" stroke="#111827" stroke-width="1.6"/>
<rect x="95.0" y="78.0" width="10.0" height="51.0" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
<circle cx="144.0" cy="176.2" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="80.7" cy="155.3" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="87.6" cy="159.3" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="56.3" cy="283.8" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="32.9" cy="202.7" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="63.7" cy="179.8" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="58.1" cy="185.5" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="29.9" cy="176.7" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="62.7" cy="254.5" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="58.7" cy="261.4" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="85.6" cy="286.3" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="37.0" cy="233.2" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="87.3" cy="236.3" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="57.5" cy="150.6" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="36.6" cy="262.5" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="111.3" cy="257.5" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="141.9" cy="236.9" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<text x="100.0" y="72.0" font-size="13" text-anchor="middle" fill="#111827" font-weight="bold">Initial equilibrium</text>
<text x="100.0" y="318.0" font-size="13" text-anchor="middle" fill="#111827">Volume = V</text>
<line x1="230.0" y1="46.0" x2="230.0" y2="152.0" stroke="#111827" stroke-width="2.2"/>
<line x1="390.0" y1="46.0" x2="390.0" y2="152.0" stroke="#111827" stroke-width="2.2"/>
<line x1="230.0" y1="152.0" x2="390.0" y2="152.0" stroke="#111827" stroke-width="2.2"/>
<rect x="231.5" y="61.0" width="157.0" height="11.0" fill="#9ca3af" stroke="#111827" stroke-width="1.6"/>
<rect x="305.0" y="32.0" width="10.0" height="29.0" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
<circle cx="324.9" cy="139.9" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="273.5" cy="81.5" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="298.6" cy="135.4" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="325.8" cy="108.2" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="374.0" cy="140.5" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="242.5" cy="82.5" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="244.7" cy="111.8" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="379.2" cy="108.6" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="294.2" cy="86.7" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="295.6" cy="111.3" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="302.6" cy="115.3" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="240.3" cy="138.5" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="325.9" cy="82.9" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="276.2" cy="112.3" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="270.6" cy="117.9" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="351.2" cy="86.1" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="345.5" cy="91.8" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<text x="310.0" y="169.0" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">I</text>
<line x1="405.0" y1="46.0" x2="405.0" y2="152.0" stroke="#111827" stroke-width="2.2"/>
<line x1="565.0" y1="46.0" x2="565.0" y2="152.0" stroke="#111827" stroke-width="2.2"/>
<line x1="405.0" y1="152.0" x2="565.0" y2="152.0" stroke="#111827" stroke-width="2.2"/>
<rect x="406.5" y="61.0" width="157.0" height="11.0" fill="#9ca3af" stroke="#111827" stroke-width="1.6"/>
<rect x="480.0" y="32.0" width="10.0" height="29.0" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
<circle cx="442.5" cy="142.0" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="419.1" cy="86.9" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="495.1" cy="84.5" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="528.3" cy="86.5" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="448.9" cy="82.9" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="448.1" cy="112.4" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="441.2" cy="116.4" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="524.2" cy="135.1" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="473.4" cy="136.8" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="528.0" cy="113.1" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="475.4" cy="109.6" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="549.0" cy="89.3" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="415.5" cy="108.5" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="552.6" cy="112.1" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="478.0" cy="87.2" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="471.1" cy="91.2" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="552.8" cy="135.0" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<text x="485.0" y="169.0" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">II</text>
<line x1="230.0" y1="196.0" x2="230.0" y2="302.0" stroke="#111827" stroke-width="2.2"/>
<line x1="390.0" y1="196.0" x2="390.0" y2="302.0" stroke="#111827" stroke-width="2.2"/>
<line x1="230.0" y1="302.0" x2="390.0" y2="302.0" stroke="#111827" stroke-width="2.2"/>
<rect x="231.5" y="211.0" width="157.0" height="11.0" fill="#9ca3af" stroke="#111827" stroke-width="1.6"/>
<rect x="305.0" y="182.0" width="10.0" height="29.0" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
<circle cx="246.1" cy="237.8" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="266.5" cy="288.7" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="292.4" cy="283.8" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="299.4" cy="287.8" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="379.2" cy="233.9" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="379.2" cy="241.9" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="378.8" cy="288.7" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="325.3" cy="287.9" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="324.0" cy="257.0" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="328.0" cy="263.9" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="294.8" cy="238.3" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="345.3" cy="286.3" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="352.2" cy="290.3" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="293.4" cy="258.5" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="300.3" cy="262.5" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="267.7" cy="238.9" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="349.6" cy="259.9" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<text x="310.0" y="319.0" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">III</text>
<line x1="405.0" y1="196.0" x2="405.0" y2="302.0" stroke="#111827" stroke-width="2.2"/>
<line x1="565.0" y1="196.0" x2="565.0" y2="302.0" stroke="#111827" stroke-width="2.2"/>
<line x1="405.0" y1="302.0" x2="565.0" y2="302.0" stroke="#111827" stroke-width="2.2"/>
<rect x="406.5" y="211.0" width="157.0" height="11.0" fill="#9ca3af" stroke="#111827" stroke-width="1.6"/>
<rect x="480.0" y="182.0" width="10.0" height="29.0" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
<circle cx="519.5" cy="286.3" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="526.4" cy="290.3" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="554.5" cy="284.6" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="550.5" cy="291.5" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="414.8" cy="233.4" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="419.2" cy="259.5" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="444.9" cy="234.1" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="551.4" cy="261.9" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="469.9" cy="263.0" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="448.5" cy="262.9" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="503.9" cy="231.9" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="499.9" cy="238.8" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="550.7" cy="234.8" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="524.8" cy="239.3" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="414.8" cy="288.0" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/><circle cx="421.7" cy="292.0" r="6.0" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="496.7" cy="265.0" r="6.0" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<text x="485.0" y="319.0" font-size="14" text-anchor="middle" fill="#111827" font-weight="bold">IV</text>
</svg>
</figure>""",
        "question": (
            r"The diagram labeled Initial equilibrium represents an equilibrium mixture for the reaction "
            r"$\text{A}(g) + \text{B}(g) \rightleftharpoons \text{AB}(g)$ in a cylinder with a movable piston "
            r"at volume $V$. At constant temperature, the piston is pushed down until the volume is $V/2$, "
            r"and the system is allowed to reach a new equilibrium. Which of the diagrams I–IV best "
            r"represents the contents of the cylinder at the new equilibrium?"
        ),
        "options": [
            r"Diagram I",
            r"Diagram II",
            r"Diagram III",
            r"Diagram IV",
        ],
        "correct_index": 3,
        "explanation": (
            r"In terms of particle counts, $K_c = \frac{[\text{AB}]}{[\text{A}][\text{B}]} = "
            r"\frac{n_{\text{AB}}V}{n_{\text{A}}\,n_{\text{B}}}$. For the initial mixture, $K_c = "
            r"\frac{3V}{(5)(6)} = \frac{V}{10}$. Halving the volume increases every concentration, and "
            r"immediately $Q_c = \frac{3(V/2)}{(5)(6)} = \frac{V}{20} < K_c$, so there is a net forward "
            r"reaction, toward fewer gas particles. If $x$ pairs of A and B combine, $\frac{(3 + x)(V/2)}{(5 "
            r"- x)(6 - x)} = \frac{V}{10}$, which is satisfied by $x = 1$: $\frac{4(V/2)}{(4)(5)} = "
            r"\frac{V}{10}$. Diagram IV (4 A, 5 B, 4 AB) is correct. Diagram I shows no shift, Diagram II "
            r"shows a shift in the wrong direction, and Diagram III shifts too far: $\frac{5(V/2)}{(3)(4)} = "
            r"\frac{5V}{24} > \frac{V}{10}$."
        ),
    },
    {
        "unit_q_num": 55,
        "topic_code": "7.10",
        "topic_title": "Reaction Quotient and Le Châtelier's Principle",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 285" role="img" aria-label="Graph of concentration in molar versus time. Before t1, [N2O4] is constant at 0.50 M and [NO2] is constant at 0.20 M. After t1, with no sudden jumps, [N2O4] gradually decreases to 0.45 M and [NO2] gradually increases to 0.30 M, and both then remain constant." font-family="sans-serif" font-size="13">
<line x1="72.0" y1="232.5" x2="490.0" y2="232.5" stroke="#e5e7eb" stroke-width="1"/>
<line x1="72.0" y1="215.0" x2="490.0" y2="215.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="72.0" y1="197.5" x2="490.0" y2="197.5" stroke="#e5e7eb" stroke-width="1"/>
<line x1="72.0" y1="180.0" x2="490.0" y2="180.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="72.0" y1="162.5" x2="490.0" y2="162.5" stroke="#e5e7eb" stroke-width="1"/>
<line x1="72.0" y1="145.0" x2="490.0" y2="145.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="72.0" y1="127.5" x2="490.0" y2="127.5" stroke="#e5e7eb" stroke-width="1"/>
<line x1="72.0" y1="110.0" x2="490.0" y2="110.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="72.0" y1="92.5" x2="490.0" y2="92.5" stroke="#e5e7eb" stroke-width="1"/>
<line x1="72.0" y1="75.0" x2="490.0" y2="75.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="72.0" y1="57.5" x2="490.0" y2="57.5" stroke="#e5e7eb" stroke-width="1"/>
<line x1="72.0" y1="40.0" x2="490.0" y2="40.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="197.4" y1="250.0" x2="197.4" y2="34.0" stroke="#374151" stroke-width="1.5" stroke-dasharray="5 4"/>
<polyline points="72.0,75.0 74.1,75.0 76.2,75.0 78.3,75.0 80.4,75.0 82.5,75.0 84.5,75.0 86.6,75.0 88.7,75.0 90.8,75.0 92.9,75.0 95.0,75.0 97.1,75.0 99.2,75.0 101.3,75.0 103.3,75.0 105.4,75.0 107.5,75.0 109.6,75.0 111.7,75.0 113.8,75.0 115.9,75.0 118.0,75.0 120.1,75.0 122.2,75.0 124.2,75.0 126.3,75.0 128.4,75.0 130.5,75.0 132.6,75.0 134.7,75.0 136.8,75.0 138.9,75.0 141.0,75.0 143.1,75.0 145.2,75.0 147.2,75.0 149.3,75.0 151.4,75.0 153.5,75.0 155.6,75.0 157.7,75.0 159.8,75.0 161.9,75.0 164.0,75.0 166.1,75.0 168.1,75.0 170.2,75.0 172.3,75.0 174.4,75.0 176.5,75.0 178.6,75.0 180.7,75.0 182.8,75.0 184.9,75.0 186.9,75.0 189.0,75.0 191.1,75.0 193.2,75.0 195.3,75.0 197.4,75.0 199.5,75.9 201.6,76.7 203.7,77.4 205.8,78.2 207.8,78.9 209.9,79.5 212.0,80.2 214.1,80.8 216.2,81.3 218.3,81.9 220.4,82.4 222.5,82.9 224.6,83.4 226.7,83.8 228.8,84.2 230.8,84.6 232.9,85.0 235.0,85.4 237.1,85.7 239.2,86.1 241.3,86.4 243.4,86.7 245.5,87.0 247.6,87.2 249.7,87.5 251.7,87.7 253.8,88.0 255.9,88.2 258.0,88.4 260.1,88.6 262.2,88.8 264.3,89.0 266.4,89.1 268.5,89.3 270.6,89.5 272.6,89.6 274.7,89.7 276.8,89.9 278.9,90.0 281.0,90.1 283.1,90.2 285.2,90.4 287.3,90.5 289.4,90.6 291.4,90.7 293.5,90.7 295.6,90.8 297.7,90.9 299.8,91.0 301.9,91.1 304.0,91.1 306.1,91.2 308.2,91.3 310.3,91.3 312.4,91.4 314.4,91.4 316.5,91.5 318.6,91.5 320.7,91.6 322.8,91.6 324.9,91.7 327.0,91.7 329.1,91.8 331.2,91.8 333.2,91.8 335.3,91.9 337.4,91.9 339.5,91.9 341.6,91.9 343.7,92.0 345.8,92.0 347.9,92.0 350.0,92.0 352.1,92.1 354.1,92.1 356.2,92.1 358.3,92.1 360.4,92.1 362.5,92.2 364.6,92.2 366.7,92.2 368.8,92.2 370.9,92.2 373.0,92.2 375.1,92.3 377.1,92.3 379.2,92.3 381.3,92.3 383.4,92.3 385.5,92.3 387.6,92.3 389.7,92.3 391.8,92.3 393.9,92.3 395.9,92.3 398.0,92.4 400.1,92.4 402.2,92.4 404.3,92.4 406.4,92.4 408.5,92.4 410.6,92.4 412.7,92.4 414.8,92.4 416.9,92.4 418.9,92.4 421.0,92.4 423.1,92.4 425.2,92.4 427.3,92.4 429.4,92.4 431.5,92.4 433.6,92.4 435.7,92.4 437.8,92.4 439.8,92.4 441.9,92.4 444.0,92.5 446.1,92.5 448.2,92.5 450.3,92.5 452.4,92.5 454.5,92.5 456.6,92.5 458.6,92.5 460.7,92.5 462.8,92.5 464.9,92.5 467.0,92.5 469.1,92.5 471.2,92.5 473.3,92.5 475.4,92.5 477.5,92.5 479.6,92.5 481.6,92.5 483.7,92.5 485.8,92.5 487.9,92.5 490.0,92.5" fill="none" stroke="#111827" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>
<polyline points="72.0,180.0 74.1,180.0 76.2,180.0 78.3,180.0 80.4,180.0 82.5,180.0 84.5,180.0 86.6,180.0 88.7,180.0 90.8,180.0 92.9,180.0 95.0,180.0 97.1,180.0 99.2,180.0 101.3,180.0 103.3,180.0 105.4,180.0 107.5,180.0 109.6,180.0 111.7,180.0 113.8,180.0 115.9,180.0 118.0,180.0 120.1,180.0 122.2,180.0 124.2,180.0 126.3,180.0 128.4,180.0 130.5,180.0 132.6,180.0 134.7,180.0 136.8,180.0 138.9,180.0 141.0,180.0 143.1,180.0 145.2,180.0 147.2,180.0 149.3,180.0 151.4,180.0 153.5,180.0 155.6,180.0 157.7,180.0 159.8,180.0 161.9,180.0 164.0,180.0 166.1,180.0 168.1,180.0 170.2,180.0 172.3,180.0 174.4,180.0 176.5,180.0 178.6,180.0 180.7,180.0 182.8,180.0 184.9,180.0 186.9,180.0 189.0,180.0 191.1,180.0 193.2,180.0 195.3,180.0 197.4,180.0 199.5,178.3 201.6,176.7 203.7,175.1 205.8,173.7 207.8,172.3 209.9,170.9 212.0,169.7 214.1,168.5 216.2,167.3 218.3,166.2 220.4,165.2 222.5,164.2 224.6,163.3 226.7,162.4 228.8,161.5 230.8,160.7 232.9,160.0 235.0,159.2 237.1,158.5 239.2,157.9 241.3,157.2 243.4,156.7 245.5,156.1 247.6,155.5 249.7,155.0 251.7,154.5 253.8,154.1 255.9,153.6 258.0,153.2 260.1,152.8 262.2,152.4 264.3,152.1 266.4,151.7 268.5,151.4 270.6,151.1 272.6,150.8 274.7,150.5 276.8,150.2 278.9,150.0 281.0,149.7 283.1,149.5 285.2,149.3 287.3,149.1 289.4,148.9 291.4,148.7 293.5,148.5 295.6,148.3 297.7,148.2 299.8,148.0 301.9,147.9 304.0,147.7 306.1,147.6 308.2,147.5 310.3,147.4 312.4,147.2 314.4,147.1 316.5,147.0 318.6,146.9 320.7,146.8 322.8,146.7 324.9,146.7 327.0,146.6 329.1,146.5 331.2,146.4 333.2,146.4 335.3,146.3 337.4,146.2 339.5,146.2 341.6,146.1 343.7,146.1 345.8,146.0 347.9,146.0 350.0,145.9 352.1,145.9 354.1,145.8 356.2,145.8 358.3,145.7 360.4,145.7 362.5,145.7 364.6,145.6 366.7,145.6 368.8,145.6 370.9,145.6 373.0,145.5 375.1,145.5 377.1,145.5 379.2,145.5 381.3,145.4 383.4,145.4 385.5,145.4 387.6,145.4 389.7,145.4 391.8,145.3 393.9,145.3 395.9,145.3 398.0,145.3 400.1,145.3 402.2,145.3 404.3,145.2 406.4,145.2 408.5,145.2 410.6,145.2 412.7,145.2 414.8,145.2 416.9,145.2 418.9,145.2 421.0,145.2 423.1,145.2 425.2,145.2 427.3,145.1 429.4,145.1 431.5,145.1 433.6,145.1 435.7,145.1 437.8,145.1 439.8,145.1 441.9,145.1 444.0,145.1 446.1,145.1 448.2,145.1 450.3,145.1 452.4,145.1 454.5,145.1 456.6,145.1 458.6,145.1 460.7,145.1 462.8,145.1 464.9,145.1 467.0,145.1 469.1,145.1 471.2,145.1 473.3,145.0 475.4,145.0 477.5,145.0 479.6,145.0 481.6,145.0 483.7,145.0 485.8,145.0 487.9,145.0 490.0,145.0" fill="none" stroke="#2563eb" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="72.0" y1="250.0" x2="490.0" y2="250.0" stroke="#111827" stroke-width="1.8"/>
<line x1="72.0" y1="250.0" x2="72.0" y2="34.0" stroke="#111827" stroke-width="1.8"/>
<line x1="67.0" y1="250.0" x2="72.0" y2="250.0" stroke="#111827" stroke-width="1.5"/>
<text x="63.0" y="254.0" font-size="12" text-anchor="end" fill="#111827">0.00</text>
<line x1="67.0" y1="215.0" x2="72.0" y2="215.0" stroke="#111827" stroke-width="1.5"/>
<text x="63.0" y="219.0" font-size="12" text-anchor="end" fill="#111827">0.10</text>
<line x1="67.0" y1="180.0" x2="72.0" y2="180.0" stroke="#111827" stroke-width="1.5"/>
<text x="63.0" y="184.0" font-size="12" text-anchor="end" fill="#111827">0.20</text>
<line x1="67.0" y1="145.0" x2="72.0" y2="145.0" stroke="#111827" stroke-width="1.5"/>
<text x="63.0" y="149.0" font-size="12" text-anchor="end" fill="#111827">0.30</text>
<line x1="67.0" y1="110.0" x2="72.0" y2="110.0" stroke="#111827" stroke-width="1.5"/>
<text x="63.0" y="114.0" font-size="12" text-anchor="end" fill="#111827">0.40</text>
<line x1="67.0" y1="75.0" x2="72.0" y2="75.0" stroke="#111827" stroke-width="1.5"/>
<text x="63.0" y="79.0" font-size="12" text-anchor="end" fill="#111827">0.50</text>
<line x1="67.0" y1="40.0" x2="72.0" y2="40.0" stroke="#111827" stroke-width="1.5"/>
<text x="63.0" y="44.0" font-size="12" text-anchor="end" fill="#111827">0.60</text>
<text x="197.4" y="28.0" font-size="14" text-anchor="middle" fill="#111827" font-style="italic">t₁</text>
<text x="281.0" y="272.0" font-size="13" text-anchor="middle" fill="#111827">Time</text>
<text x="26.0" y="145.0" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 26.0 145.0)">Concentration (M)</text>
<text x="84.5" y="67.0" font-size="13" text-anchor="start" fill="#111827" font-weight="bold">[N₂O₄]</text>
<text x="84.5" y="172.0" font-size="13" text-anchor="start" fill="#2563eb" font-weight="bold">[NO₂]</text>
</svg>
<figcaption>Figure: Concentrations in a rigid vessel before and after a change at time t₁</figcaption>
</figure>""",
        "question": (
            r"The graph above shows the concentrations of $\text{N}_2\text{O}_4(g)$ and $\text{NO}_2(g)$ in a "
            r"rigid, sealed vessel for the reaction $\text{N}_2\text{O}_4(g) \rightleftharpoons "
            r"2\,\text{NO}_2(g)$, for which $\Delta H^\circ = +57\text{ kJ/mol}_{rxn}$. A single change was "
            r"made to the system at time $t_1$. Which of the following changes is most consistent with the "
            r"data?"
        ),
        "options": [
            r"Some $\text{N}_2\text{O}_4(g)$ was injected into the vessel.",
            r"Some $\text{NO}_2(g)$ was removed from the vessel.",
            r"The temperature of the vessel was increased.",
            r"The temperature of the vessel was decreased.",
        ],
        "correct_index": 2,
        "explanation": (
            r"Adding or removing a gas would cause a sudden jump or drop in that gas's concentration at "
            r"$t_1$, and the volume of a rigid vessel cannot change. The graph shows no sudden change, only "
            r"gradual ones, which is the signature of a temperature change: temperature changes the value of "
            r"$K$ itself, and the concentrations then redistribute. Before $t_1$, $K_c = "
            r"\frac{(0.20)^2}{0.50} = 0.080$; afterward, $K_c = \frac{(0.30)^2}{0.45} = 0.20$. (The 1 : 2 "
            r"stoichiometry checks: $[\text{N}_2\text{O}_4]$ fell by $0.05\text{ M}$ while $[\text{NO}_2]$ "
            r"rose by $0.10\text{ M}$.) Because $K_c$ increased and the reaction is endothermic, the "
            r"temperature was raised. Lowering the temperature would decrease $K_c$ and shift the system "
            r"toward $\text{N}_2\text{O}_4$."
        ),
    },
    {
        "unit_q_num": 56,
        "topic_code": "7.11",
        "topic_title": "Introduction to Solubility Equilibria",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"At $25^\circ\text{C}$, a saturated solution of sodium chloride contains $5.4\text{ mol}$ of "
            r"dissolved $\text{NaCl}$ per liter of solution. Which of the following gives the approximate "
            r"value of $K_{\text{sp}}$ for $\text{NaCl}$ at $25^\circ\text{C}$ and correctly interprets it?"
        ),
        "options": [
            r"$K_{\text{sp}} \approx 5.4$; a $K_{\text{sp}}$ value greater than 1 corresponds to a soluble salt.",
            r"$K_{\text{sp}} \approx 29$; a $K_{\text{sp}}$ value greater than 1 corresponds to a soluble salt.",
            r"$K_{\text{sp}} \approx 29$; such a large $K_{\text{sp}}$ means that the dissolution equilibrium favors $\text{NaCl}(s)$, so the salt is only slightly soluble.",
            r"No $K_{\text{sp}}$ can be written for $\text{NaCl}$, because it is a strong electrolyte that dissociates completely and does not establish an equilibrium with its solid.",
        ],
        "correct_index": 1,
        "explanation": (
            r"For $\text{NaCl}(s) \rightleftharpoons \text{Na}^+(aq) + \text{Cl}^-(aq)$, the saturated "
            r"solution has $[\text{Na}^+] = [\text{Cl}^-] = 5.4\text{ M}$, so $K_{\text{sp}} = "
            r"[\text{Na}^+][\text{Cl}^-] = (5.4)^2 \approx 29$. Because $K_{\text{sp}}$ describes the "
            r"dissolution reaction, a value greater than 1 means that the equilibrium favors the dissolved "
            r"ions; salts with $K_{\text{sp}} > 1$ are the soluble salts of the solubility rules (all sodium "
            r"salts are soluble), whereas sparingly soluble salts such as $\text{AgCl}$ have $K_{\text{sp}}$ "
            r"values far less than 1 ($1.8 \times 10^{-10}$). Writing $K_{\text{sp}} = 5.4$ omits the product "
            r"of the two ion concentrations. Although $\text{NaCl}$ dissociates completely, a saturated "
            r"solution in contact with excess solid is still a dynamic equilibrium between dissolution and "
            r"precipitation. (In such a concentrated solution, the value 29 is only approximate.)"
        ),
    },
    {
        "unit_q_num": 57,
        "topic_code": "7.11",
        "topic_title": "Introduction to Solubility Equilibria",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": (
            r"To determine $K_{\text{sp}}$ for $\text{PbCl}_2$, a student stirs excess solid $\text{PbCl}_2$ "
            r"in distilled water at $25^\circ\text{C}$ until the solution is saturated. The student then "
            r"pipets a $50.00\text{ mL}$ sample of the mixture into a weighed evaporating dish, evaporates "
            r"the water completely, and weighs the dry residue. The student uses the mass of the residue to "
            r"calculate the molar solubility, $s$, of $\text{PbCl}_2$ and then calculates $K_{\text{sp}} = "
            r"4s^3$. The student forgot to filter the mixture, so the pipetted sample contained some "
            r"suspended particles of undissolved $\text{PbCl}_2(s)$. How does this error affect the "
            r"calculated value of $K_{\text{sp}}$?"
        ),
        "options": [
            r"The calculated $K_{\text{sp}}$ is too high, because the mass of the residue, and therefore the calculated value of $s$, is too high.",
            r"The calculated $K_{\text{sp}}$ is too low, because the suspended solid removes $\text{Pb}^{2+}$ and $\text{Cl}^-$ ions from the solution.",
            r"The calculated $K_{\text{sp}}$ is unaffected, because pure solids are not included in the $K_{\text{sp}}$ expression.",
            r"The calculated $K_{\text{sp}}$ is unaffected, because the solution was saturated, so the concentrations of the dissolved ions were correct.",
        ],
        "correct_index": 0,
        "explanation": (
            r"The method assumes that all of the residue came from dissolved $\text{PbCl}_2$. The suspended "
            r"particles of undissolved solid also remain in the dish after the water evaporates, so the "
            r"measured mass of residue is too large. The calculated moles of $\text{PbCl}_2$ per liter, $s$, "
            r"is therefore too high, and because $K_{\text{sp}} = [\text{Pb}^{2+}][\text{Cl}^-]^2 = (s)(2s)^2 "
            r"= 4s^3$, the calculated $K_{\text{sp}}$ is too high; the error is magnified by the cube. The "
            r"suspended solid does not change the actual equilibrium concentrations of the dissolved ions, "
            r"which is why solids are omitted from the $K_{\text{sp}}$ expression, but the experiment does "
            r"not measure ion concentrations directly. It measures the total mass of $\text{PbCl}_2$ in the "
            r"sample, which includes the undissolved solid."
        ),
    },
    {
        "unit_q_num": 58,
        "topic_code": "7.11",
        "topic_title": "Introduction to Solubility Equilibria",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 420 280" role="img" aria-label="Diagram of a beaker containing a saturated solution with excess solid MX2 at the bottom. Dissolved in the solution are 3 M2+ ions, drawn as larger gray circles, and 6 X- ions, drawn as smaller white circles. Water molecules are not shown." font-family="sans-serif" font-size="13">
<rect x="70" y="72" width="240" height="190" fill="#e5e7eb" stroke="none"/>
<line x1="70.0" y1="72.0" x2="310.0" y2="72.0" stroke="#374151" stroke-width="1.5" stroke-dasharray="6 4"/>
<path d="M 62 38 L 70 46 L 70 262 L 310 262 L 310 46 L 318 38" fill="none" stroke="#111827" stroke-width="2.4" stroke-linejoin="round"/>
<circle cx="88.0" cy="252.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="99.5" cy="252.0" r="5.5" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
<circle cx="111.0" cy="252.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="122.5" cy="252.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="134.0" cy="252.0" r="5.5" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
<circle cx="145.5" cy="252.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="157.0" cy="252.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="168.5" cy="252.0" r="5.5" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
<circle cx="180.0" cy="252.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="191.5" cy="252.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="203.0" cy="252.0" r="5.5" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
<circle cx="214.5" cy="252.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="226.0" cy="252.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="237.5" cy="252.0" r="5.5" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
<circle cx="249.0" cy="252.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="260.5" cy="252.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="272.0" cy="252.0" r="5.5" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
<circle cx="283.5" cy="252.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="295.0" cy="252.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="94.0" cy="241.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="105.5" cy="241.0" r="5.5" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
<circle cx="117.0" cy="241.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="128.5" cy="241.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="140.0" cy="241.0" r="5.5" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
<circle cx="151.5" cy="241.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="163.0" cy="241.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="174.5" cy="241.0" r="5.5" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
<circle cx="186.0" cy="241.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="197.5" cy="241.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="209.0" cy="241.0" r="5.5" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
<circle cx="220.5" cy="241.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="232.0" cy="241.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="243.5" cy="241.0" r="5.5" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
<circle cx="255.0" cy="241.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="266.5" cy="241.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<circle cx="278.0" cy="241.0" r="5.5" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/>
<circle cx="289.5" cy="241.0" r="4.2" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
<text x="324.0" y="250.0" font-size="13" text-anchor="start" fill="#111827">MX₂(s)</text>
<circle cx="112.0" cy="112.0" r="11.5" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/><text x="112.0" y="116.0" font-size="12" text-anchor="middle" fill="#111827" font-weight="bold">2+</text>
<circle cx="168.0" cy="98.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><text x="168.0" y="102.0" font-size="12" text-anchor="middle" fill="#111827" font-weight="bold">−</text>
<circle cx="248.0" cy="104.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><text x="248.0" y="108.0" font-size="12" text-anchor="middle" fill="#111827" font-weight="bold">−</text>
<circle cx="210.0" cy="150.0" r="11.5" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/><text x="210.0" y="154.0" font-size="12" text-anchor="middle" fill="#111827" font-weight="bold">2+</text>
<circle cx="128.0" cy="168.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><text x="128.0" y="172.0" font-size="12" text-anchor="middle" fill="#111827" font-weight="bold">−</text>
<circle cx="278.0" cy="160.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><text x="278.0" y="164.0" font-size="12" text-anchor="middle" fill="#111827" font-weight="bold">−</text>
<circle cx="150.0" cy="210.0" r="11.5" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/><text x="150.0" y="214.0" font-size="12" text-anchor="middle" fill="#111827" font-weight="bold">2+</text>
<circle cx="236.0" cy="206.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><text x="236.0" y="210.0" font-size="12" text-anchor="middle" fill="#111827" font-weight="bold">−</text>
<circle cx="96.0" cy="222.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><text x="96.0" y="226.0" font-size="12" text-anchor="middle" fill="#111827" font-weight="bold">−</text>
<circle cx="350.0" cy="104.0" r="11.5" fill="#9ca3af" stroke="#111827" stroke-width="1.5"/><text x="350.0" y="108.0" font-size="12" text-anchor="middle" fill="#111827" font-weight="bold">2+</text>
<text x="368.0" y="109.0" font-size="13" text-anchor="start" fill="#111827">M²⁺</text>
<circle cx="350.0" cy="140.0" r="8" fill="#ffffff" stroke="#111827" stroke-width="1.5"/><text x="350.0" y="144.0" font-size="12" text-anchor="middle" fill="#111827" font-weight="bold">−</text>
<text x="368.0" y="145.0" font-size="13" text-anchor="start" fill="#111827">X⁻</text>
</svg>
<figcaption>Figure: Dissolved ions in a saturated solution of MX₂ (water not shown)</figcaption>
</figure>""",
        "question": (
            r"The diagram above represents a saturated solution of the ionic compound $\text{MX}_2$ in "
            r"contact with excess $\text{MX}_2(s)$ at $25^\circ\text{C}$. Assume that the diagram represents "
            r"$1.0\text{ L}$ of solution and that each dissolved ion shown represents $1.0 \times "
            r"10^{-3}\text{ mol}$ of that ion. Based on the diagram, what is the value of $K_{\text{sp}}$ for "
            r"$\text{MX}_2$ at $25^\circ\text{C}$?"
        ),
        "options": [
            r"$1.8 \times 10^{-5}$",
            r"$4.3 \times 10^{-7}$",
            r"$1.1 \times 10^{-7}$",
            r"$2.7 \times 10^{-8}$",
        ],
        "correct_index": 2,
        "explanation": (
            r"In a saturated solution the dissolved ions are in equilibrium with the solid: $\text{MX}_2(s) "
            r"\rightleftharpoons \text{M}^{2+}(aq) + 2\,\text{X}^-(aq)$. The diagram shows 3 $\text{M}^{2+}$ "
            r"ions and 6 $\text{X}^-$ ions (a 1 : 2 ratio, as the formula requires), so $[\text{M}^{2+}] = "
            r"3.0 \times 10^{-3}\text{ M}$ and $[\text{X}^-] = 6.0 \times 10^{-3}\text{ M}$. Then "
            r"$K_{\text{sp}} = [\text{M}^{2+}][\text{X}^-]^2 = (3.0 \times 10^{-3})(6.0 \times 10^{-3})^2 = "
            r"1.1 \times 10^{-7}$; the solid does not appear in the expression. Omitting the square gives "
            r"$1.8 \times 10^{-5}$. Doubling $[\text{X}^-]$ again before squaring gives $4.3 \times 10^{-7}$, "
            r"but the 6 ions already represent $2s$. Calculating $(3.0 \times 10^{-3})^3 = 2.7 \times "
            r"10^{-8}$ omits the factor of 4 in $K_{\text{sp}} = (s)(2s)^2 = 4s^3$."
        ),
    },
    {
        "unit_q_num": 59,
        "topic_code": "7.12",
        "topic_title": "Common-Ion Effect",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": (
            r"A student determines the solubility of $\text{Ca(OH)}_2$ by titrating $25.00\text{ mL}$ samples "
            r"of filtered, saturated $\text{Ca(OH)}_2$ solutions with standardized $\text{HCl}(aq)$. In Trial "
            r"1, the $\text{Ca(OH)}_2$ solution was saturated in distilled water. In Trial 2, it was prepared "
            r"by saturating $0.050\text{ M}$ $\text{CaCl}_2(aq)$ with $\text{Ca(OH)}_2$ at the same "
            r"temperature. Which of the following correctly compares the volume of $\text{HCl}(aq)$ needed to "
            r"reach the equivalence point in Trial 2 with the volume needed in Trial 1?"
        ),
        "options": [
            r"More $\text{HCl}$ is needed in Trial 2, because the additional $\text{Ca}^{2+}$ ions from the $\text{CaCl}_2$ also react with the $\text{HCl}$.",
            r"Less $\text{HCl}$ is needed in Trial 2, because the $\text{Ca}^{2+}$ already present shifts the dissolution equilibrium of $\text{Ca(OH)}_2$ toward the solid, so the sample contains less $\text{OH}^-$.",
            r"Less $\text{HCl}$ is needed in Trial 2, because the dissolved $\text{CaCl}_2$ decreases the value of $K_{\text{sp}}$ for $\text{Ca(OH)}_2$.",
            r"The same volume of $\text{HCl}$ is needed in both trials, because both solutions are saturated with $\text{Ca(OH)}_2$.",
        ],
        "correct_index": 1,
        "explanation": (
            r"For $\text{Ca(OH)}_2(s) \rightleftharpoons \text{Ca}^{2+}(aq) + 2\,\text{OH}^-(aq)$, "
            r"$K_{\text{sp}} = [\text{Ca}^{2+}][\text{OH}^-]^2$. In $0.050\text{ M}$ $\text{CaCl}_2$, "
            r"$\text{Ca}^{2+}$ is already present, so $Q$ reaches $K_{\text{sp}}$ after less "
            r"$\text{Ca(OH)}_2$ has dissolved (the common-ion effect). The saturated solution therefore has a "
            r"lower $[\text{OH}^-]$, and fewer moles of $\text{HCl}$ are needed to neutralize the "
            r"$\text{OH}^-$ in a $25.00\text{ mL}$ sample. For example, with $K_{\text{sp}} \approx 5 \times "
            r"10^{-6}$, $[\text{OH}^-] \approx 0.022\text{ M}$ in water but only about $0.0096\text{ M}$ in "
            r"$0.050\text{ M}$ $\text{CaCl}_2$. $K_{\text{sp}}$ depends only on temperature, so it is the "
            r"same in both trials. Neither $\text{Ca}^{2+}$ nor $\text{Cl}^-$ reacts with $\text{HCl}$; only "
            r"$\text{OH}^-$ is titrated. Both solutions are saturated, but the amount that dissolves depends "
            r"on the ions already present."
        ),
    },
    {
        "unit_q_num": 60,
        "topic_code": "7.12",
        "topic_title": "Common-Ion Effect",
        "difficulty": "Challenging",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 340" role="img" aria-label="Graph of [M+] versus [X-], both in units of 10 to the minus 3 molar, from 0 to 8. A curve shows [M+][X-] = 4.0 times 10 to the minus 6 for saturated solutions. Point P is on the curve at (2.0, 2.0). Point 1 is above the curve at (5.0, 2.0). Point 2 is on the curve at (1.0, 4.0). Point 3 is on the curve at (5.0, 0.8). Point 4 is on the curve at (4.0, 1.0)." font-family="sans-serif" font-size="13">
<line x1="130.0" y1="285.0" x2="130.0" y2="45.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="80.0" y1="255.0" x2="480.0" y2="255.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="180.0" y1="285.0" x2="180.0" y2="45.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="80.0" y1="225.0" x2="480.0" y2="225.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="230.0" y1="285.0" x2="230.0" y2="45.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="80.0" y1="195.0" x2="480.0" y2="195.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="280.0" y1="285.0" x2="280.0" y2="45.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="80.0" y1="165.0" x2="480.0" y2="165.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="330.0" y1="285.0" x2="330.0" y2="45.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="80.0" y1="135.0" x2="480.0" y2="135.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="380.0" y1="285.0" x2="380.0" y2="45.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="80.0" y1="105.0" x2="480.0" y2="105.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="430.0" y1="285.0" x2="430.0" y2="45.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="80.0" y1="75.0" x2="480.0" y2="75.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="480.0" y1="285.0" x2="480.0" y2="45.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="80.0" y1="45.0" x2="480.0" y2="45.0" stroke="#e5e7eb" stroke-width="1"/>
<polyline points="105.0,45.0 107.5,66.8 110.0,85.0 112.5,100.4 115.0,113.6 117.5,125.0 120.0,135.0 122.5,143.8 125.0,151.7 127.5,158.7 130.0,165.0 132.5,170.7 135.0,175.9 137.5,180.7 140.0,185.0 142.5,189.0 145.0,192.7 147.5,196.1 150.0,199.3 152.5,202.2 155.0,205.0 157.5,207.6 160.0,210.0 162.5,212.3 165.0,214.4 167.5,216.4 170.0,218.3 172.5,220.1 175.0,221.8 177.5,223.5 180.0,225.0 182.5,226.5 185.0,227.9 187.5,229.2 190.0,230.5 192.5,231.7 195.0,232.8 197.5,233.9 200.0,235.0 202.5,236.0 205.0,237.0 207.5,237.9 210.0,238.8 212.5,239.7 215.0,240.6 217.5,241.4 220.0,242.1 222.5,242.9 225.0,243.6 227.5,244.3 230.0,245.0 232.5,245.7 235.0,246.3 237.5,246.9 240.0,247.5 242.5,248.1 245.0,248.6 247.5,249.2 250.0,249.7 252.5,250.2 255.0,250.7 257.5,251.2 260.0,251.7 262.5,252.1 265.0,252.6 267.5,253.0 270.0,253.4 272.5,253.8 275.0,254.2 277.5,254.6 280.0,255.0 282.5,255.4 285.0,255.7 287.5,256.1 290.0,256.4 292.5,256.8 295.0,257.1 297.5,257.4 300.0,257.7 302.5,258.0 305.0,258.3 307.5,258.6 310.0,258.9 312.5,259.2 315.0,259.5 317.5,259.7 320.0,260.0 322.5,260.3 325.0,260.5 327.5,260.8 330.0,261.0 332.5,261.2 335.0,261.5 337.5,261.7 340.0,261.9 342.5,262.1 345.0,262.4 347.5,262.6 350.0,262.8 352.5,263.0 355.0,263.2 357.5,263.4 360.0,263.6 362.5,263.8 365.0,263.9 367.5,264.1 370.0,264.3 372.5,264.5 375.0,264.7 377.5,264.8 380.0,265.0 382.5,265.2 385.0,265.3 387.5,265.5 390.0,265.6 392.5,265.8 395.0,266.0 397.5,266.1 400.0,266.2 402.5,266.4 405.0,266.5 407.5,266.7 410.0,266.8 412.5,267.0 415.0,267.1 417.5,267.2 420.0,267.4 422.5,267.5 425.0,267.6 427.5,267.7 430.0,267.9 432.5,268.0 435.0,268.1 437.5,268.2 440.0,268.3 442.5,268.4 445.0,268.6 447.5,268.7 450.0,268.8 452.5,268.9 455.0,269.0 457.5,269.1 460.0,269.2 462.5,269.3 465.0,269.4 467.5,269.5 470.0,269.6 472.5,269.7 475.0,269.8 477.5,269.9 480.0,270.0" fill="none" stroke="#111827" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="80.0" y1="285.0" x2="480.0" y2="285.0" stroke="#111827" stroke-width="1.8"/>
<line x1="80.0" y1="285.0" x2="80.0" y2="41.0" stroke="#111827" stroke-width="1.8"/>
<line x1="80.0" y1="285.0" x2="80.0" y2="290.0" stroke="#111827" stroke-width="1.5"/>
<text x="80.0" y="304.0" font-size="12" text-anchor="middle" fill="#111827">0</text>
<line x1="75.0" y1="285.0" x2="80.0" y2="285.0" stroke="#111827" stroke-width="1.5"/>
<text x="71.0" y="289.0" font-size="12" text-anchor="end" fill="#111827">0</text>
<line x1="130.0" y1="285.0" x2="130.0" y2="290.0" stroke="#111827" stroke-width="1.5"/>
<text x="130.0" y="304.0" font-size="12" text-anchor="middle" fill="#111827">1</text>
<line x1="75.0" y1="255.0" x2="80.0" y2="255.0" stroke="#111827" stroke-width="1.5"/>
<text x="71.0" y="259.0" font-size="12" text-anchor="end" fill="#111827">1</text>
<line x1="180.0" y1="285.0" x2="180.0" y2="290.0" stroke="#111827" stroke-width="1.5"/>
<text x="180.0" y="304.0" font-size="12" text-anchor="middle" fill="#111827">2</text>
<line x1="75.0" y1="225.0" x2="80.0" y2="225.0" stroke="#111827" stroke-width="1.5"/>
<text x="71.0" y="229.0" font-size="12" text-anchor="end" fill="#111827">2</text>
<line x1="230.0" y1="285.0" x2="230.0" y2="290.0" stroke="#111827" stroke-width="1.5"/>
<text x="230.0" y="304.0" font-size="12" text-anchor="middle" fill="#111827">3</text>
<line x1="75.0" y1="195.0" x2="80.0" y2="195.0" stroke="#111827" stroke-width="1.5"/>
<text x="71.0" y="199.0" font-size="12" text-anchor="end" fill="#111827">3</text>
<line x1="280.0" y1="285.0" x2="280.0" y2="290.0" stroke="#111827" stroke-width="1.5"/>
<text x="280.0" y="304.0" font-size="12" text-anchor="middle" fill="#111827">4</text>
<line x1="75.0" y1="165.0" x2="80.0" y2="165.0" stroke="#111827" stroke-width="1.5"/>
<text x="71.0" y="169.0" font-size="12" text-anchor="end" fill="#111827">4</text>
<line x1="330.0" y1="285.0" x2="330.0" y2="290.0" stroke="#111827" stroke-width="1.5"/>
<text x="330.0" y="304.0" font-size="12" text-anchor="middle" fill="#111827">5</text>
<line x1="75.0" y1="135.0" x2="80.0" y2="135.0" stroke="#111827" stroke-width="1.5"/>
<text x="71.0" y="139.0" font-size="12" text-anchor="end" fill="#111827">5</text>
<line x1="380.0" y1="285.0" x2="380.0" y2="290.0" stroke="#111827" stroke-width="1.5"/>
<text x="380.0" y="304.0" font-size="12" text-anchor="middle" fill="#111827">6</text>
<line x1="75.0" y1="105.0" x2="80.0" y2="105.0" stroke="#111827" stroke-width="1.5"/>
<text x="71.0" y="109.0" font-size="12" text-anchor="end" fill="#111827">6</text>
<line x1="430.0" y1="285.0" x2="430.0" y2="290.0" stroke="#111827" stroke-width="1.5"/>
<text x="430.0" y="304.0" font-size="12" text-anchor="middle" fill="#111827">7</text>
<line x1="75.0" y1="75.0" x2="80.0" y2="75.0" stroke="#111827" stroke-width="1.5"/>
<text x="71.0" y="79.0" font-size="12" text-anchor="end" fill="#111827">7</text>
<line x1="480.0" y1="285.0" x2="480.0" y2="290.0" stroke="#111827" stroke-width="1.5"/>
<text x="480.0" y="304.0" font-size="12" text-anchor="middle" fill="#111827">8</text>
<line x1="75.0" y1="45.0" x2="80.0" y2="45.0" stroke="#111827" stroke-width="1.5"/>
<text x="71.0" y="49.0" font-size="12" text-anchor="end" fill="#111827">8</text>
<text x="280.0" y="325.0" font-size="13" text-anchor="middle" fill="#111827">[X⁻] (×10⁻³ M)</text>
<text x="46.0" y="165.0" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 46.0 165.0)">[M⁺] (×10⁻³ M)</text>
<circle cx="180.0" cy="225.0" r="5" fill="#ffffff" stroke="#111827" stroke-width="1.8"/>
<text x="189.0" y="217.0" font-size="14" text-anchor="start" fill="#111827" font-weight="bold">P</text>
<circle cx="330.0" cy="225.0" r="5" fill="#111827" stroke="#111827" stroke-width="1.8"/>
<text x="339.0" y="217.0" font-size="14" text-anchor="start" fill="#111827" font-weight="bold">1</text>
<circle cx="130.0" cy="165.0" r="5" fill="#111827" stroke="#111827" stroke-width="1.8"/>
<text x="139.0" y="159.0" font-size="14" text-anchor="start" fill="#111827" font-weight="bold">2</text>
<circle cx="330.0" cy="261.0" r="5" fill="#111827" stroke="#111827" stroke-width="1.8"/>
<text x="338.0" y="277.0" font-size="14" text-anchor="start" fill="#111827" font-weight="bold">3</text>
<circle cx="280.0" cy="255.0" r="5" fill="#111827" stroke="#111827" stroke-width="1.8"/>
<text x="276.0" y="244.0" font-size="14" text-anchor="end" fill="#111827" font-weight="bold">4</text>
<text x="360.0" y="249.6" font-size="12" text-anchor="start" fill="#374151" font-style="italic">saturated</text>
</svg>
<figcaption>Figure: Concentrations of M⁺ and X⁻ in saturated solutions of MX at 25 °C</figcaption>
</figure>""",
        "question": (
            r"The curve in the graph above shows the combinations of $[\text{M}^+]$ and $[\text{X}^-]$ in "
            r"saturated solutions of the salt $\text{MX}$ at $25^\circ\text{C}$, for which $K_{\text{sp}} = "
            r"4.0 \times 10^{-6}$. Point P represents a saturated solution of $\text{MX}$ in pure water in "
            r"contact with excess $\text{MX}(s)$. Enough solid $\text{NaX}$ is dissolved in this mixture to "
            r"add $3.0 \times 10^{-3}\text{ mol}$ of $\text{X}^-$ per liter of solution (assume no change in "
            r"volume), and the system returns to equilibrium. Which numbered point represents the solution at "
            r"the new equilibrium?"
        ),
        "options": [
            r"Point 1",
            r"Point 2",
            r"Point 3",
            r"Point 4",
        ],
        "correct_index": 3,
        "explanation": (
            r"Immediately after the $\text{NaX}$ dissolves, $[\text{X}^-] = 2.0 \times 10^{-3} + 3.0 \times "
            r"10^{-3} = 5.0 \times 10^{-3}\text{ M}$ while $[\text{M}^+] = 2.0 \times 10^{-3}\text{ M}$ "
            r"(point 1). There $Q = (2.0 \times 10^{-3})(5.0 \times 10^{-3}) = 1.0 \times 10^{-5} > "
            r"K_{\text{sp}}$, so $\text{MX}(s)$ precipitates, removing $\text{M}^+$ and $\text{X}^-$ in a 1 : "
            r"1 ratio. If $z \times 10^{-3}\text{ M}$ of each ion precipitates, $(2.0 - z)(5.0 - z) = 4.0$, "
            r"so $z^2 - 7z + 6 = 0$ and $z = 1.0$ (the root $z = 6$ is impossible). The new equilibrium has "
            r"$[\text{M}^+] = 1.0 \times 10^{-3}\text{ M}$ and $[\text{X}^-] = 4.0 \times 10^{-3}\text{ M}$: "
            r"point 4. Point 1 is supersaturated and not at equilibrium; point 3 lies on the curve but would "
            r"require removing only $\text{M}^+$; point 2 has a higher $[\text{M}^+]$, the opposite of the "
            r"common-ion effect."
        ),
    },
]
