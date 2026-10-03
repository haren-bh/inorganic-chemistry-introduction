UNIT_META = {
    "id": 8,
    "title": "Unit 8: Acids and Bases",
    "short_title": "Acids, Bases & Buffers",
    "exam_weight": "11–15%",
    "color": "#e11d48",
    "description": "Autoionization of water (Kw) and temperature dependence of neutral pH, pH and pOH of strong monoprotic/diprotic acids and bases, weak acid/base equilibria (Ka, Kb, percent ionization), acid-base reactions and buffers, titration curves (half-equivalence point pH = pKa, equivalence point pH, indicator selection), molecular structure and inductive effects on acid strength, Henderson-Hasselbalch equation, buffer capacity, and the effect of pH on the solubility of salts with basic anions (Topic 8.11).",
    "topics": [
        {"code": "8.1", "title": "Introduction to Acids and Bases"},
        {"code": "8.2", "title": "pH and pOH of Strong Acids and Bases"},
        {"code": "8.3", "title": "Weak Acid and Base Equilibria"},
        {"code": "8.4", "title": "Acid-Base Reactions and Buffers"},
        {"code": "8.5", "title": "Acid-Base Titrations"},
        {"code": "8.6", "title": "Molecular Structure of Acids and Bases"},
        {"code": "8.7", "title": "pH and pKa"},
        {"code": "8.8", "title": "Properties of Buffers"},
        {"code": "8.9", "title": "Henderson-Hasselbalch Equation"},
        {"code": "8.10", "title": "Buffer Capacity"},
        {"code": "8.11", "title": "pH and Solubility"},
    ],
}

QUESTIONS = [
    # -------------------------------------------------------------------------
    # 8.1 Introduction to Acids and Bases (Q1 - Q5)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 1,
        "topic_code": "8.1",
        "topic_title": "Introduction to Acids and Bases",
        "difficulty": "AP Exam Level",
        "stimulus": """<table class="quiz-data-table">
<thead>
<tr><th>Temperature ($^\\circ\\text{C}$)</th><th>$K_w$</th><th>$\\text{p}K_w$</th></tr>
</thead>
<tbody>
<tr><td>$10$</td><td>$2.9 \\times 10^{-15}$</td><td>$14.54$</td></tr>
<tr><td>$25$</td><td>$1.0 \\times 10^{-14}$</td><td>$14.00$</td></tr>
<tr><td>$50$</td><td>$5.5 \\times 10^{-14}$</td><td>$13.26$</td></tr>
</tbody>
</table>""",
        "question": "The autoionization of water is represented by the equilibrium $2\\,\\text{H}_2\\text{O}(l) \\rightleftharpoons \\text{H}_3\\text{O}^+(aq) + \\text{OH}^-(aq)$. Based on the data in the table above, which of the following statements about pure water at $50^\\circ\\text{C}$ is correct?",
        "options": [
            "Pure water is slightly acidic at $50^\\circ\\text{C}$ because $[\\text{H}_3\\text{O}^+] > 1.0 \\times 10^{-7}\\,\\text{M}$.",
            "The autoionization of water is endothermic, and pure water is neutral at $50^\\circ\\text{C}$ with $\\text{pH} = 6.63$.",
            "The autoionization of water is exothermic, and pure water has $\\text{pOH} = 7.37$ at $50^\\circ\\text{C}$.",
            "Pure water is neutral at $50^\\circ\\text{C}$ because $[\\text{H}_3\\text{O}^+] = 1.0 \\times 10^{-7}\\,\\text{M}$ at all temperatures."
        ],
        "correct_index": 1,
        "explanation": "As temperature increases from $10^\\circ\\text{C}$ to $50^\\circ\\text{C}$, $K_w$ increases from $2.9 \\times 10^{-15}$ to $5.5 \\times 10^{-14}$, proving that the forward autoionization reaction is endothermic ($\\Delta H^\\circ > 0$). In pure water at any temperature, stoichiometry requires $[\\text{H}_3\\text{O}^+] = [\\text{OH}^-]$, so pure water is always neutral. At $50^\\circ\\text{C}$, $\\text{pH} = \\text{pOH} = \\frac{1}{2}\\text{p}K_w = \\frac{13.26}{2} = 6.63$."
    },
    {
        "unit_q_num": 2,
        "topic_code": "8.1",
        "topic_title": "Introduction to Acids and Bases",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "At $25^\\circ\\text{C}$, an aqueous solution has a hydronium ion concentration of $[\\text{H}_3\\text{O}^+] = 4.0 \\times 10^{-9}\\,\\text{M}$. Which of the following correctly gives the hydroxide ion concentration $[\\text{OH}^-]$ and classifies the solution?",
        "options": [
            "$[\\text{OH}^-] = 2.5 \\times 10^{-6}\\,\\text{M}$; the solution is basic",
            "$[\\text{OH}^-] = 2.5 \\times 10^{-5}\\,\\text{M}$; the solution is basic",
            "$[\\text{OH}^-] = 4.0 \\times 10^{-5}\\,\\text{M}$; the solution is acidic",
            "$[\\text{OH}^-] = 6.0 \\times 10^{-6}\\,\\text{M}$; the solution is basic"
        ],
        "correct_index": 0,
        "explanation": "At $25^\\circ\\text{C}$, $K_w = [\\text{H}_3\\text{O}^+][\\text{OH}^-] = 1.0 \\times 10^{-14}$. Solving for $[\\text{OH}^-]$ gives $[\\text{OH}^-] = \\frac{1.0 \\times 10^{-14}}{4.0 \\times 10^{-9}} = 0.25 \\times 10^{-5}\\,\\text{M} = 2.5 \\times 10^{-6}\\,\\text{M}$. Because $[\\text{OH}^-] > [\\text{H}_3\\text{O}^+]$ (and $\\text{pH} = 8.40 > 7.00$), the solution is basic."
    },
    {
        "unit_q_num": 3,
        "topic_code": "8.1",
        "topic_title": "Introduction to Acids and Bases",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "Consider the reversible Brønsted-Lowry acid-base reaction below:\n$$\\text{H}_2\\text{PO}_4^-(aq) + \\text{HCO}_3^-(aq) \\rightleftharpoons \\text{HPO}_4^{2-}(aq) + \\text{H}_2\\text{CO}_3(aq)$$\nWhich of the following correctly identifies a conjugate acid-base pair in this reaction?",
        "options": [
            "$\\text{H}_2\\text{PO}_4^-$ and $\\text{HCO}_3^-$",
            "$\\text{HCO}_3^-$ and $\\text{HPO}_4^{2-}$",
            "$\\text{H}_2\\text{CO}_3$ and $\\text{HCO}_3^-$",
            "$\\text{H}_2\\text{PO}_4^-$ and $\\text{H}_3\\text{PO}_4$"
        ],
        "correct_index": 2,
        "explanation": "A conjugate acid-base pair differs by exactly one proton ($\\text{H}^+$). In the forward reaction, $\\text{H}_2\\text{PO}_4^-$ donates a proton to become its conjugate base $\\text{HPO}_4^{2-}$, while $\\text{HCO}_3^-$ accepts a proton to become its conjugate acid $\\text{H}_2\\text{CO}_3$. Thus, $\\text{H}_2\\text{CO}_3$ and $\\text{HCO}_3^-$ form a conjugate acid-base pair present in the reaction."
    },
    {
        "unit_q_num": 4,
        "topic_code": "8.1",
        "topic_title": "Introduction to Acids and Bases",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": "At $37^\\circ\\text{C}$ (normal human body temperature), the autoionization constant of water is $K_w = 2.4 \\times 10^{-14}$. If a sample of blood plasma at $37^\\circ\\text{C}$ has $\\text{pH} = 7.40$, what is the $\\text{pOH}$ of the blood plasma at this temperature? ($\\log(2.4) = 0.38$)",
        "options": [
            "$6.22$",
            "$6.60$",
            "$6.98$",
            "$7.40$"
        ],
        "correct_index": 0,
        "explanation": "First calculate $\\text{p}K_w$ at $37^\\circ\\text{C}$: $\\text{p}K_w = -\\log(2.4 \\times 10^{-14}) = 14 - \\log(2.4) = 14 - 0.38 = 13.62$. Using the relation $\\text{pH} + \\text{pOH} = \\text{p}K_w$, we find $\\text{pOH} = 13.62 - 7.40 = 6.22$."
    },
    {
        "unit_q_num": 5,
        "topic_code": "8.1",
        "topic_title": "Introduction to Acids and Bases",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "Which of the following species can act as an amphoteric (amphiprotic) substance in aqueous solution, capable of both donating and accepting a proton?",
        "options": [
            "$\\text{PO}_4^{3-}(aq)$",
            "$\\text{NH}_4^+(aq)$",
            "$\\text{NO}_3^-(aq)$",
            "$\\text{HSO}_3^-(aq)$"
        ],
        "correct_index": 3,
        "explanation": "An amphiprotic species can both donate an $\\text{H}^+$ ion (acting as a Brønsted-Lowry acid) and accept an $\\text{H}^+$ ion (acting as a Brønsted-Lowry base). $\\text{HSO}_3^-$ can donate a proton to form $\\text{SO}_3^{2-}$ or accept a proton to form $\\text{H}_2\\text{SO}_3$. $\\text{PO}_4^{3-}$ and $\\text{NO}_3^-$ have no ionizable protons, and $\\text{NH}_4^+$ has no lone pair to accept another proton."
    },

    # -------------------------------------------------------------------------
    # 8.2 pH and pOH of Strong Acids and Bases (Q6 - Q10)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 6,
        "topic_code": "8.2",
        "topic_title": "pH and pOH of Strong Acids and Bases",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "What is the $\\text{pH}$ of a $0.025\\,\\text{M}$ aqueous solution of barium hydroxide, $\\text{Ba(OH)}_2(aq)$, at $25^\\circ\\text{C}$? ($\\log(5.0) = 0.70$)",
        "options": [
            "$1.30$",
            "$1.60$",
            "$12.40$",
            "$12.70$"
        ],
        "correct_index": 3,
        "explanation": "$\\text{Ba(OH)}_2$ is a strong soluble Group 2 hydroxide that dissociates completely according to $\\text{Ba(OH)}_2(aq) \\rightarrow \\text{Ba}^{2+}(aq) + 2\\,\\text{OH}^-(aq)$. Therefore, $[\\text{OH}^-] = 2 \\times 0.025\\,\\text{M} = 0.050\\,\\text{M} = 5.0 \\times 10^{-2}\\,\\text{M}$. Then $\\text{pOH} = -\\log(5.0 \\times 10^{-2}) = 2 - 0.70 = 1.30$. At $25^\\circ\\text{C}$, $\\text{pH} = 14.00 - 1.30 = 12.70$."
    },
    {
        "unit_q_num": 7,
        "topic_code": "8.2",
        "topic_title": "pH and pOH of Strong Acids and Bases",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "A student has $10.0\\,\\text{mL}$ of an aqueous $\\text{HCl}$ solution with $\\text{pH} = 2.00$ at $25^\\circ\\text{C}$. How much distilled water must be added to this sample to change the $\\text{pH}$ to $4.00$? (Assume volumes are additive.)",
        "options": [
            "$10.0\\,\\text{mL}$",
            "$90.0\\,\\text{mL}$",
            "$990.\\,\\text{mL}$",
            "$1000.\\,\\text{mL}$"
        ],
        "correct_index": 2,
        "explanation": "Changing the $\\text{pH}$ from $2.00$ to $4.00$ corresponds to decreasing $[\\text{H}_3\\text{O}^+]$ from $1.0 \\times 10^{-2}\\,\\text{M}$ to $1.0 \\times 10^{-4}\\,\\text{M}$, a $100$-fold dilution. Using $M_1V_1 = M_2V_2$, the final volume must be $V_2 = 10.0\\,\\text{mL} \\times \\frac{1.0 \\times 10^{-2}\\,\\text{M}}{1.0 \\times 10^{-4}\\,\\text{M}} = 1000.\\,\\text{mL}$. Therefore, the volume of distilled water that must be added is $1000.\\,\\text{mL} - 10.0\\,\\text{mL} = 990.\\,\\text{mL}$."
    },
    {
        "unit_q_num": 8,
        "topic_code": "8.2",
        "topic_title": "pH and pOH of Strong Acids and Bases",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "At $25^\\circ\\text{C}$, $40.0\\,\\text{mL}$ of $0.100\\,\\text{M}\\,\\text{HNO}_3(aq)$ is mixed with $60.0\\,\\text{mL}$ of $0.100\\,\\text{M}\\,\\text{KOH}(aq)$. What is the $\\text{pH}$ of the resulting $100.0\\,\\text{mL}$ solution? ($\\log(2.0) = 0.30$)",
        "options": [
            "$1.70$",
            "$7.00$",
            "$12.30$",
            "$12.52$"
        ],
        "correct_index": 2,
        "explanation": "Calculate the initial moles of $\\text{H}_3\\text{O}^+$ and $\\text{OH}^-$: $n_{\\text{H}_3\\text{O}^+} = (0.0400\\,\\text{L})(0.100\\,\\text{M}) = 0.00400\\,\\text{mol}$ and $n_{\\text{OH}^-} = (0.0600\\,\\text{L})(0.100\\,\\text{M}) = 0.00600\\,\\text{mol}$. Neutralization leaves $0.00600 - 0.00400 = 0.00200\\,\\text{mol}$ of excess $\\text{OH}^-$ in a total volume of $0.1000\\,\\text{L}$, giving $[\\text{OH}^-] = 0.0200\\,\\text{M} = 2.0 \\times 10^{-2}\\,\\text{M}$. Thus, $\\text{pOH} = -\\log(2.0 \\times 10^{-2}) = 2.00 - 0.30 = 1.70$, and $\\text{pH} = 14.00 - 1.70 = 12.30$."
    },
    {
        "unit_q_num": 9,
        "topic_code": "8.2",
        "topic_title": "pH and pOH of Strong Acids and Bases",
        "difficulty": "AP Exam Level",
        "stimulus": """<table class="quiz-data-table">
<thead>
<tr><th>Solution</th><th>Solute</th><th>Concentration ($\\text{M}$)</th></tr>
</thead>
<tbody>
<tr><td>$\\text{W}$</td><td>$\\text{HClO}_4$</td><td>$0.010$</td></tr>
<tr><td>$\\text{X}$</td><td>$\\text{Sr(OH)}_2$</td><td>$0.010$</td></tr>
<tr><td>$\\text{Y}$</td><td>$\\text{NaOH}$</td><td>$0.010$</td></tr>
<tr><td>$\\text{Z}$</td><td>$\\text{HI}$</td><td>$0.10$</td></tr>
</tbody>
</table>""",
        "question": "Based on the data in the table above, which of the following lists the four aqueous solutions in order of increasing $\\text{pH}$ at $25^\\circ\\text{C}$?",
        "options": [
            "$\\text{Z} < \\text{W} < \\text{Y} < \\text{X}$",
            "$\\text{W} < \\text{Z} < \\text{Y} < \\text{X}$",
            "$\\text{Z} < \\text{W} < \\text{X} < \\text{Y}$",
            "$\\text{X} < \\text{Y} < \\text{W} < \\text{Z}$"
        ],
        "correct_index": 0,
        "explanation": "Solution $\\text{Z}$ ($0.10\\,\\text{M}\\,\\text{HI}$, strong acid) has $[\\text{H}_3\\text{O}^+] = 0.10\\,\\text{M}$ and $\\text{pH} = 1.00$. Solution $\\text{W}$ ($0.010\\,\\text{M}\\,\\text{HClO}_4$, strong acid) has $[\\text{H}_3\\text{O}^+] = 0.010\\,\\text{M}$ and $\\text{pH} = 2.00$. Solution $\\text{Y}$ ($0.010\\,\\text{M}\\,\\text{NaOH}$, a strong base that releases one $\\text{OH}^-$ per formula unit) has $[\\text{OH}^-] = 0.010\\,\\text{M}$ and $\\text{pH} = 12.00$. Solution $\\text{X}$ ($0.010\\,\\text{M}\\,\\text{Sr(OH)}_2$, a strong base that releases two $\\text{OH}^-$ per formula unit) has $[\\text{OH}^-] = 0.020\\,\\text{M}$ and $\\text{pH} = 12.30$. Thus, increasing $\\text{pH}$ is $\\text{Z} < \\text{W} < \\text{Y} < \\text{X}$."
    },
    {
        "unit_q_num": 10,
        "topic_code": "8.2",
        "topic_title": "pH and pOH of Strong Acids and Bases",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": "A chemist prepares an extremely dilute solution of $1.0 \\times 10^{-8}\\,\\text{M}\\,\\text{HCl}(aq)$ at $25^\\circ\\text{C}$. Which of the following best describes the $\\text{pH}$ of this solution?",
        "options": [
            "$\\text{pH} = 8.00$, because $-\\log(1.0 \\times 10^{-8}) = 8.00$.",
            "$\\text{pH} = 7.00$ exactly, because $1.0 \\times 10^{-8}\\,\\text{M}\\,\\text{HCl}$ is too dilute to ionize in water.",
            "$\\text{pH} = 6.00$, because water autoionization doubles the $\\text{HCl}$ concentration.",
            "$\\text{pH}$ is slightly less than $7.00$, because the autoionization of water contributes a significant amount of $\\text{H}_3\\text{O}^+$ in addition to the $\\text{HCl}$."
        ],
        "correct_index": 3,
        "explanation": "Adding an acid to pure water at $25^\\circ\\text{C}$ can never make the solution basic ($\\text{pH} > 7$). When $[\\text{HCl}] = 1.0 \\times 10^{-8}\\,\\text{M}$, the $\\text{H}_3\\text{O}^+$ from the autoionization of water ($\\approx 9.5 \\times 10^{-8}\\,\\text{M}$) cannot be neglected. The total $[\\text{H}_3\\text{O}^+]$ is approximately $1.05 \\times 10^{-7}\\,\\text{M}$, which gives a $\\text{pH}$ of $6.98$ (slightly less than $7.00$)."
    },

    # -------------------------------------------------------------------------
    # 8.3 Weak Acid and Base Equilibria (Q11 - Q15)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 11,
        "topic_code": "8.3",
        "topic_title": "Weak Acid and Base Equilibria",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "Hypochlorous acid, $\\text{HOCl}$, is a weak monoprotic acid with $K_a = 4.0 \\times 10^{-8}$ at $25^\\circ\\text{C}$. What is the $\\text{pH}$ of a $0.10\\,\\text{M}\\,\\text{HOCl}(aq)$ solution at $25^\\circ\\text{C}$? ($\\log(6.3) = 0.80$)",
        "options": [
            "$3.80$",
            "$4.20$",
            "$7.40$",
            "$8.40$"
        ],
        "correct_index": 1,
        "explanation": "Set up the weak acid equilibrium $\\text{HOCl}(aq) + \\text{H}_2\\text{O}(l) \\rightleftharpoons \\text{H}_3\\text{O}^+(aq) + \\text{OCl}^-(aq)$:\n$$K_a = \\frac{x^2}{0.10 - x} \\approx \\frac{x^2}{0.10} = 4.0 \\times 10^{-8}$$\nSolving for $x = [\\text{H}_3\\text{O}^+]$ gives $x^2 = 4.0 \\times 10^{-9} = 40. \\times 10^{-10}$, so $x = 6.3 \\times 10^{-5}\\,\\text{M}$. Thus, $\\text{pH} = -\\log(6.3 \\times 10^{-5}) = 5 - 0.80 = 4.20$."
    },
    {
        "unit_q_num": 12,
        "topic_code": "8.3",
        "topic_title": "Weak Acid and Base Equilibria",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "A $0.20\\,\\text{M}$ aqueous solution of a weak monoprotic acid, $\\text{HX}$, is found to be $1.5\\%$ ionized at $25^\\circ\\text{C}$. What is the acid dissociation constant, $K_a$, for $\\text{HX}$ at this temperature?",
        "options": [
            "$4.5 \\times 10^{-5}$",
            "$3.0 \\times 10^{-3}$",
            "$2.3 \\times 10^{-4}$",
            "$1.5 \\times 10^{-2}$"
        ],
        "correct_index": 0,
        "explanation": "From the percent ionization of $1.5\\%$, the equilibrium concentrations are $[\\text{H}_3\\text{O}^+] = [\\text{X}^-] = 0.015 \\times 0.20\\,\\text{M} = 3.0 \\times 10^{-3}\\,\\text{M}$, and $[\\text{HX}] \\approx 0.20\\,\\text{M}$. Substituting into the $K_a$ expression gives:\n$$K_a = \\frac{[\\text{H}_3\\text{O}^+][\\text{X}^-]}{[\\text{HX}]} = \\frac{(3.0 \\times 10^{-3})^2}{0.20} = \\frac{9.0 \\times 10^{-6}}{0.20} = 4.5 \\times 10^{-5}$$"
    },
    {
        "unit_q_num": 13,
        "topic_code": "8.3",
        "topic_title": "Weak Acid and Base Equilibria",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "At $25^\\circ\\text{C}$, a $1.0\\,\\text{M}$ solution of acetic acid, $\\text{CH}_3\\text{COOH}(aq)$, is diluted with distilled water to a final concentration of $0.010\\,\\text{M}$. How do the percent ionization of $\\text{CH}_3\\text{COOH}$, the equilibrium concentration $[\\text{H}_3\\text{O}^+]$, and the $\\text{pH}$ change as a result of this dilution?",
        "options": [
            "Percent ionization increases, $[\\text{H}_3\\text{O}^+]$ decreases, and $\\text{pH}$ increases.",
            "Percent ionization decreases, $[\\text{H}_3\\text{O}^+]$ decreases, and $\\text{pH}$ increases.",
            "Percent ionization increases, $[\\text{H}_3\\text{O}^+]$ increases, and $\\text{pH}$ decreases.",
            "Percent ionization remains constant, $[\\text{H}_3\\text{O}^+]$ decreases, and $\\text{pH}$ increases."
        ],
        "correct_index": 0,
        "explanation": "For a weak acid with initial concentration $C$, $[\\text{H}_3\\text{O}^+] \\approx \\sqrt{K_a C}$ and percent ionization $\\approx \\sqrt{\\frac{K_a}{C}} \\times 100\\%$. As $C$ decreases upon dilution, the equilibrium shifts toward the side with more solute particles (products), so percent ionization increases. However, because the total volume increases by a factor of $100$, $[\\text{H}_3\\text{O}^+]$ decreases by a factor of $10$, causing the $\\text{pH}$ to increase by $1.0$ unit."
    },
    {
        "unit_q_num": 14,
        "topic_code": "8.3",
        "topic_title": "Weak Acid and Base Equilibria",
        "difficulty": "AP Exam Level",
        "stimulus": """<table class="quiz-data-table">
<thead>
<tr><th>Weak Acid</th><th>Formula</th><th>$K_a$ at $25^\\circ\\text{C}$</th></tr>
</thead>
<tbody>
<tr><td>Hydrofluoric acid</td><td>$\\text{HF}$</td><td>$6.8 \\times 10^{-4}$</td></tr>
<tr><td>Nitrous acid</td><td>$\\text{HNO}_2$</td><td>$4.5 \\times 10^{-4}$</td></tr>
<tr><td>Benzoic acid</td><td>$\\text{C}_6\\text{H}_5\\text{COOH}$</td><td>$6.3 \\times 10^{-5}$</td></tr>
<tr><td>Hydrocyanic acid</td><td>$\\text{HCN}$</td><td>$6.2 \\times 10^{-10}$</td></tr>
</tbody>
</table>""",
        "question": "Four separate $0.10\\,\\text{M}$ aqueous solutions of the sodium salts $\\text{NaF}$, $\\text{NaNO}_2$, $\\text{C}_6\\text{H}_5\\text{COONa}$, and $\\text{NaCN}$ are prepared at $25^\\circ\\text{C}$. Based on the $K_a$ values in the table above, which of the four salt solutions has the highest $\\text{pH}$, and what is the base ionization constant $K_b$ of its anion?",
        "options": [
            "$\\text{NaF}(aq)$, with $K_b = 1.5 \\times 10^{-11}$",
            "$\\text{C}_6\\text{H}_5\\text{COONa}(aq)$, with $K_b = 1.6 \\times 10^{-10}$",
            "$\\text{NaCN}(aq)$, with $K_b = 6.2 \\times 10^{-4}$",
            "$\\text{NaCN}(aq)$, with $K_b = 1.6 \\times 10^{-5}$"
        ],
        "correct_index": 3,
        "explanation": "For a conjugate acid-base pair at $25^\\circ\\text{C}$, $K_a \\times K_b = K_w = 1.0 \\times 10^{-14}$. The weakest acid ($\\text{HCN}$, $K_a = 6.2 \\times 10^{-10}$) has the strongest conjugate base ($\\text{CN}^-$), which undergoes the greatest extent of base hydrolysis ($\\text{CN}^- + \\text{H}_2\\text{O} \\rightleftharpoons \\text{HCN} + \\text{OH}^-$) to produce the highest $\\text{pH}$. Its $K_b$ value is $K_b = \\frac{1.0 \\times 10^{-14}}{6.2 \\times 10^{-10}} = 1.6 \\times 10^{-5}$."
    },
    {
        "unit_q_num": 15,
        "topic_code": "8.3",
        "topic_title": "Weak Acid and Base Equilibria",
        "difficulty": "Challenging",
        "stimulus": r'<table class="quiz-data-table"><thead><tr><th>Base</th><th>Formula</th><th>$\text{p}K_a$ of Conjugate Acid at $25^\circ\text{C}$</th></tr></thead><tbody><tr><td>Ammonia</td><td>$\text{NH}_3$</td><td>$9.25$</td></tr><tr><td>Methylamine</td><td>$\text{CH}_3\text{NH}_2$</td><td>$10.64$</td></tr><tr><td>Trimethylamine</td><td>$(\text{CH}_3)_3\text{N}$</td><td>$9.80$</td></tr><tr><td>Pyridine</td><td>$\text{C}_5\text{H}_5\text{N}$</td><td>$5.23$</td></tr></tbody></table>',
        "question": r"Based on the data in the table above, what is the approximate $\text{pH}$ of a $0.10\,\text{M}$ aqueous solution of trimethylamine, $(\text{CH}_3)_3\text{N}(aq)$, at $25^\circ\text{C}$?",
        "options": [
            r"$2.60$",
            r"$5.40$",
            r"$8.60$",
            r"$11.40$",
        ],
        "correct_index": 3,
        "explanation": r"Trimethylamine is a weak base: $(\text{CH}_3)_3\text{N}(aq) + \text{H}_2\text{O}(l) \rightleftharpoons (\text{CH}_3)_3\text{NH}^+(aq) + \text{OH}^-(aq)$. For a conjugate pair, $\text{p}K_b = \text{p}K_w - \text{p}K_a = 14.00 - 9.80 = 4.20$, so $K_b = 10^{-4.20} = 6.3 \times 10^{-5}$. Because only a small fraction of the base ionizes, $[\text{OH}^-] \approx \sqrt{K_b C} = \sqrt{(6.3 \times 10^{-5})(0.10)} = 2.5 \times 10^{-3}\,\text{M}$, so $\text{pOH} = 2.60$ and $\text{pH} = 14.00 - 2.60 = 11.40$. A value of $2.60$ is the pOH, not the pH. A value of $5.40$ results from treating $9.80$ as the $\text{p}K_a$ of a weak acid dissolved in water ($8.60$ is $14.00 - 5.40$), but a solution of a weak base must be basic.",
    },

    # -------------------------------------------------------------------------
    # 8.4 Acid-Base Reactions and Buffers (Q16 - Q20)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 16,
        "topic_code": "8.4",
        "topic_title": "Acid-Base Reactions and Buffers",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "Which of the following is the correct net ionic equation for the reaction that occurs when equal volumes of $0.10\\,\\text{M}$ nitrous acid, $\\text{HNO}_2(aq)$, and $0.10\\,\\text{M}$ potassium hydroxide, $\\text{KOH}(aq)$, are mixed?",
        "options": [
            "$\\text{H}_3\\text{O}^+(aq) + \\text{OH}^-(aq) \\rightarrow 2\\,\\text{H}_2\\text{O}(l)$",
            "$\\text{HNO}_2(aq) + \\text{KOH}(aq) \\rightarrow \\text{KNO}_2(aq) + \\text{H}_2\\text{O}(l)$",
            "$\\text{H}^+(aq) + \\text{NO}_2^-(aq) + \\text{K}^+(aq) + \\text{OH}^-(aq) \\rightarrow \\text{KNO}_2(aq) + \\text{H}_2\\text{O}(l)$",
            "$\\text{HNO}_2(aq) + \\text{OH}^-(aq) \\rightarrow \\text{NO}_2^-(aq) + \\text{H}_2\\text{O}(l)$"
        ],
        "correct_index": 3,
        "explanation": "Nitrous acid ($\\text{HNO}_2$) is a weak acid that exists predominantly as unionized $\\text{HNO}_2$ molecules in aqueous solution, whereas $\\text{KOH}$ is a strong soluble base that dissociates completely into $\\text{K}^+(aq)$ and $\\text{OH}^-(aq)$. Eliminating the spectator ion $\\text{K}^+$ gives the net ionic equation $\\text{HNO}_2(aq) + \\text{OH}^-(aq) \\rightarrow \\text{NO}_2^-(aq) + \\text{H}_2\\text{O}(l)$."
    },
    {
        "unit_q_num": 17,
        "topic_code": "8.4",
        "topic_title": "Acid-Base Reactions and Buffers",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "Which of the following mixtures, when prepared using the specified volumes and concentrations at $25^\\circ\\text{C}$, will result in an effective buffer solution?",
        "options": [
            "$50.0\\,\\text{mL}$ of $0.10\\,\\text{M}\\,\\text{HCl}(aq)$ and $25.0\\,\\text{mL}$ of $0.10\\,\\text{M}\\,\\text{NaOH}(aq)$",
            "$50.0\\,\\text{mL}$ of $0.10\\,\\text{M}\\,\\text{HF}(aq)$ and $50.0\\,\\text{mL}$ of $0.10\\,\\text{M}\\,\\text{NaOH}(aq)$",
            "$50.0\\,\\text{mL}$ of $0.10\\,\\text{M}\\,\\text{NH}_3(aq)$ and $25.0\\,\\text{mL}$ of $0.10\\,\\text{M}\\,\\text{HCl}(aq)$",
            "$25.0\\,\\text{mL}$ of $0.10\\,\\text{M}\\,\\text{CH}_3\\text{COOH}(aq)$ and $50.0\\,\\text{mL}$ of $0.10\\,\\text{M}\\,\\text{NaOH}(aq)$"
        ],
        "correct_index": 2,
        "explanation": "A buffer requires significant amounts of both a weak acid and its conjugate base after any neutralization reaction goes to completion. When $50.0\\,\\text{mL}$ of $0.10\\,\\text{M}\\,\\text{NH}_3$ ($5.0\\,\\text{mmol}$) reacts with $25.0\\,\\text{mL}$ of $0.10\\,\\text{M}\\,\\text{HCl}$ ($2.5\\,\\text{mmol}$), the reaction $\\text{NH}_3 + \\text{H}_3\\text{O}^+ \\rightarrow \\text{NH}_4^+ + \\text{H}_2\\text{O}$ consumes all $2.5\\,\\text{mmol}$ of $\\text{H}_3\\text{O}^+$, leaving $2.5\\,\\text{mmol}$ of $\\text{NH}_3$ and $2.5\\,\\text{mmol}$ of $\\text{NH}_4^+$ (an ideal buffer at the half-equivalence point)."
    },
    {
        "unit_q_num": 18,
        "topic_code": "8.4",
        "topic_title": "Acid-Base Reactions and Buffers",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "A student mixes $100.0\\,\\text{mL}$ of $0.200\\,\\text{M}$ formic acid, $\\text{HCOOH}(aq)$, with $50.0\\,\\text{mL}$ of $0.200\\,\\text{M}\\,\\text{NaOH}(aq)$. After the reaction goes to completion, what are the concentrations of $\\text{HCOOH}$ and $\\text{HCOO}^-$ in the final $150.0\\,\\text{mL}$ solution?",
        "options": [
            "$[\\text{HCOOH}] = 0.0667\\,\\text{M}$ and $[\\text{HCOO}^-] = 0.0667\\,\\text{M}$",
            "$[\\text{HCOOH}] = 0.100\\,\\text{M}$ and $[\\text{HCOO}^-] = 0.100\\,\\text{M}$",
            "$[\\text{HCOOH}] = 0.133\\,\\text{M}$ and $[\\text{HCOO}^-] = 0.0667\\,\\text{M}$",
            "$[\\text{HCOOH}] = 0.00\\,\\text{M}$ and $[\\text{HCOO}^-] = 0.133\\,\\text{M}$"
        ],
        "correct_index": 0,
        "explanation": "Initially, $n_{\\text{HCOOH}} = (0.1000\\,\\text{L})(0.200\\,\\text{M}) = 0.0200\\,\\text{mol}$ and $n_{\\text{OH}^-} = (0.0500\\,\\text{L})(0.200\\,\\text{M}) = 0.0100\\,\\text{mol}$. The neutralization $\\text{HCOOH} + \\text{OH}^- \\rightarrow \\text{HCOO}^- + \\text{H}_2\\text{O}$ converts $0.0100\\,\\text{mol}$ of $\\text{HCOOH}$ into $0.0100\\,\\text{mol}$ of $\\text{HCOO}^-$, leaving $0.0100\\,\\text{mol}$ of $\\text{HCOOH}$ unreacted. Dividing by the total volume of $0.1500\\,\\text{L}$ gives $[\\text{HCOOH}] = [\\text{HCOO}^-] = \\frac{0.0100\\,\\text{mol}}{0.1500\\,\\text{L}} = 0.0667\\,\\text{M}$."
    },
    {
        "unit_q_num": 19,
        "topic_code": "8.4",
        "topic_title": "Acid-Base Reactions and Buffers",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "When $50.0\\,\\text{mL}$ of $0.20\\,\\text{M}\\,\\text{HBr}(aq)$ is added to $50.0\\,\\text{mL}$ of $0.20\\,\\text{M}$ pyridine, $\\text{C}_5\\text{H}_5\\text{N}(aq)$ ($K_b = 1.7 \\times 10^{-9}$ at $25^\\circ\\text{C}$), which of the following lists the major species (excluding $\\text{H}_2\\text{O}$) present at equilibrium and correctly describes the $\\text{pH}$ of the solution?",
        "options": [
            "$\\text{C}_5\\text{H}_5\\text{N}$ and $\\text{Br}^-$; $\\text{pH} > 7.00$",
            "$\\text{C}_5\\text{H}_5\\text{NH}^+$ and $\\text{Br}^-$; $\\text{pH} < 7.00$",
            "$\\text{C}_5\\text{H}_5\\text{NH}^+$ and $\\text{Br}^-$; $\\text{pH} = 7.00$",
            "$\\text{C}_5\\text{H}_5\\text{N}$, $\\text{C}_5\\text{H}_5\\text{NH}^+$, and $\\text{Br}^-$; $\\text{pH} < 7.00$"
        ],
        "correct_index": 1,
        "explanation": "Equal moles ($0.010\\,\\text{mol}$ each) of strong acid $\\text{HBr}$ and weak base $\\text{C}_5\\text{H}_5\\text{N}$ react stoichiometrically to the equivalence point: $\\text{H}_3\\text{O}^+(aq) + \\text{C}_5\\text{H}_5\\text{N}(aq) \\rightarrow \\text{C}_5\\text{H}_5\\text{NH}^+(aq) + \\text{H}_2\\text{O}(l)$. The major species in the resulting solution are the conjugate acid $\\text{C}_5\\text{H}_5\\text{NH}^+$ and the spectator ion $\\text{Br}^-$. Because $\\text{C}_5\\text{H}_5\\text{NH}^+$ is a weak acid that partially hydrolyzes water to form $\\text{H}_3\\text{O}^+$, the $\\text{pH}$ is less than $7.00$."
    },
    {
        "unit_q_num": 20,
        "topic_code": "8.4",
        "topic_title": "Acid-Base Reactions and Buffers",
        "difficulty": "Challenging",
        "stimulus": """<table class="quiz-data-table">
<thead>
<tr><th>Acid / Ion</th><th>$K_a$ at $25^\\circ\\text{C}$</th><th>$\\text{p}K_a$</th></tr>
</thead>
<tbody>
<tr><td>$\\text{H}_3\\text{PO}_4$</td><td>$7.5 \\times 10^{-3}$</td><td>$2.12$</td></tr>
<tr><td>$\\text{H}_2\\text{PO}_4^-$</td><td>$6.2 \\times 10^{-8}$</td><td>$7.21$</td></tr>
<tr><td>$\\text{HPO}_4^{2-}$</td><td>$4.2 \\times 10^{-13}$</td><td>$12.38$</td></tr>
</tbody>
</table>""",
        "question": "A chemist adds $0.15\\,\\text{mol}$ of solid $\\text{NaOH}$ to $1.00\\,\\text{L}$ of $0.10\\,\\text{M}\\,\\text{H}_3\\text{PO}_4(aq)$ at $25^\\circ\\text{C}$. Based on the data in the table above, what is the $\\text{pH}$ of the resulting solution?",
        "options": [
            "$2.12$",
            "$4.67$",
            "$7.21$",
            "$12.38$"
        ],
        "correct_index": 2,
        "explanation": "Initially there is $0.10\\,\\text{mol}$ of $\\text{H}_3\\text{PO}_4$ and $0.15\\,\\text{mol}$ of $\\text{OH}^-$. The first $0.10\\,\\text{mol}$ of $\\text{OH}^-$ quantitatively converts all $0.10\\,\\text{mol}$ of $\\text{H}_3\\text{PO}_4$ into $0.10\\,\\text{mol}$ of $\\text{H}_2\\text{PO}_4^-$, leaving $0.05\\,\\text{mol}$ of $\\text{OH}^-$. This remaining $0.05\\,\\text{mol}$ of $\\text{OH}^-$ reacts with $0.05\\,\\text{mol}$ of $\\text{H}_2\\text{PO}_4^-$ to form $0.05\\,\\text{mol}$ of $\\text{HPO}_4^{2-}$, leaving $0.05\\,\\text{mol}$ of $\\text{H}_2\\text{PO}_4^-$. Because $[\\text{H}_2\\text{PO}_4^-] = [\\text{HPO}_4^{2-}]$, $\\text{pH} = \\text{p}K_{a2} = 7.21$."
    },

    # -------------------------------------------------------------------------
    # 8.5 Acid-Base Titrations (Q21 - Q25)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 21,
        "topic_code": "8.5",
        "topic_title": "Acid-Base Titrations",
        "difficulty": "AP Exam Level",
        "stimulus": """<table class="quiz-data-table">
<thead>
<tr><th>Volume of $0.100\\,\\text{M}\\,\\text{NaOH}$ Added ($\\text{mL}$)</th><th>$\\text{pH}$ of Solution</th></tr>
</thead>
<tbody>
<tr><td>$0.0$</td><td>$2.84$</td></tr>
<tr><td>$10.0$</td><td>$4.46$</td></tr>
<tr><td>$15.0$</td><td>$4.76$</td></tr>
<tr><td>$20.0$</td><td>$5.06$</td></tr>
<tr><td>$29.9$</td><td>$7.24$</td></tr>
<tr><td>$30.0$</td><td>$8.75$</td></tr>
<tr><td>$30.1$</td><td>$10.26$</td></tr>
<tr><td>$40.0$</td><td>$12.19$</td></tr>
</tbody>
</table>""",
        "question": "A $25.0\\,\\text{mL}$ sample of a monoprotic weak acid, $\\text{HA}(aq)$, is titrated with $0.100\\,\\text{M}\\,\\text{NaOH}(aq)$ at $25^\\circ\\text{C}$, producing the data in the table above. What are the initial concentration of $\\text{HA}(aq)$ and the $\\text{p}K_a$ of $\\text{HA}$?",
        "options": [
            "$[\\text{HA}]_0 = 0.120\\,\\text{M}$ and $\\text{p}K_a = 4.76$",
            "$[\\text{HA}]_0 = 0.100\\,\\text{M}$ and $\\text{p}K_a = 4.46$",
            "$[\\text{HA}]_0 = 0.120\\,\\text{M}$ and $\\text{p}K_a = 8.75$",
            "$[\\text{HA}]_0 = 0.0833\\,\\text{M}$ and $\\text{p}K_a = 4.76$"
        ],
        "correct_index": 0,
        "explanation": "The steepest vertical jump in $\\text{pH}$ occurs at $30.0\\,\\text{mL}$ of $\\text{NaOH}$ added ($\\text{pH} = 8.75$), which is the equivalence point. At the equivalence point, $M_{\\text{HA}}V_{\\text{HA}} = M_{\\text{NaOH}}V_{\\text{NaOH}}$, so $[\\text{HA}]_0 = \\frac{(0.100\\,\\text{M})(30.0\\,\\text{mL})}{25.0\\,\\text{mL}} = 0.120\\,\\text{M}$. The half-equivalence point occurs at $\\frac{30.0\\,\\text{mL}}{2} = 15.0\\,\\text{mL}$ of $\\text{NaOH}$ added, where $[\\text{HA}] = [\\text{A}^-]$ and $\\text{pH} = \\text{p}K_a = 4.76$."
    },
    {
        "unit_q_num": 22,
        "topic_code": "8.5",
        "topic_title": "Acid-Base Titrations",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": "A $50.0\\,\\text{mL}$ sample of $0.200\\,\\text{M}$ lactic acid, $\\text{HC}_3\\text{H}_5\\text{O}_3(aq)$ ($K_a = 1.0 \\times 10^{-4}$ at $25^\\circ\\text{C}$), is titrated to the equivalence point using $50.0\\,\\text{mL}$ of $0.200\\,\\text{M}\\,\\text{NaOH}(aq)$. What is the $\\text{pH}$ of the solution at the equivalence point?",
        "options": [
            "$5.50$",
            "$7.00$",
            "$8.00$",
            "$8.50$"
        ],
        "correct_index": 3,
        "explanation": "At the equivalence point, all $0.0100\\,\\text{mol}$ of lactic acid has been converted to $0.0100\\,\\text{mol}$ of lactate ion ($\\text{C}_3\\text{H}_5\\text{O}_3^-$) in a total volume of $100.0\\,\\text{mL}$ ($0.100\\,\\text{L}$), so $[\\text{C}_3\\text{H}_5\\text{O}_3^-] = 0.100\\,\\text{M}$. For the lactate ion, $K_b = \\frac{K_w}{K_a} = \\frac{1.0 \\times 10^{-14}}{1.0 \\times 10^{-4}} = 1.0 \\times 10^{-10}$. Setting up the base hydrolysis equilibrium gives $[\\text{OH}^-] = \\sqrt{K_b \\times [\\text{A}^-]} = \\sqrt{(1.0 \\times 10^{-10})(0.100)} = \\sqrt{1.0 \\times 10^{-11}} = 3.16 \\times 10^{-6}\\,\\text{M}$ ($\\text{pOH} = 5.50$). Thus, $\\text{pH} = 14.00 - 5.50 = 8.50$."
    },
    {
        "unit_q_num": 23,
        "topic_code": "8.5",
        "topic_title": "Acid-Base Titrations",
        "difficulty": "AP Exam Level",
        "stimulus": """<table class="quiz-data-table">
<thead>
<tr><th>Indicator</th><th>Acid Color</th><th>Base Color</th><th>$\\text{p}K_{\\text{in}}$</th><th>Useful $\\text{pH}$ Transition Range</th></tr>
</thead>
<tbody>
<tr><td>Thymol blue</td><td>Red</td><td>Yellow</td><td>$1.7$</td><td>$1.2 - 2.8$</td></tr>
<tr><td>Bromothymol blue</td><td>Yellow</td><td>Blue</td><td>$7.1$</td><td>$6.0 - 7.6$</td></tr>
<tr><td>Phenolphthalein</td><td>Colorless</td><td>Pink</td><td>$9.4$</td><td>$8.2 - 10.0$</td></tr>
<tr><td>Methyl red</td><td>Red</td><td>Yellow</td><td>$5.0$</td><td>$4.2 - 6.2$</td></tr>
</tbody>
</table>""",
        "question": "A student performs a titration of $25.0\\,\\text{mL}$ of $0.10\\,\\text{M}$ ammonia, $\\text{NH}_3(aq)$ ($K_b = 1.8 \\times 10^{-5}$), with $0.10\\,\\text{M}\\,\\text{HCl}(aq)$ at $25^\\circ\\text{C}$. Based on the table above, which acid-base indicator is best suited to signal the equivalence point of this titration?",
        "options": [
            "Thymol blue",
            "Bromothymol blue",
            "Phenolphthalein",
            "Methyl red"
        ],
        "correct_index": 3,
        "explanation": "In the titration of a weak base ($\\text{NH}_3$) with a strong acid ($\\text{HCl}$), the species present at the equivalence point is the conjugate weak acid $\\text{NH}_4^+$ ($[\\text{NH}_4^+] = 0.050\\,\\text{M}$, $K_a = 5.6 \\times 10^{-10}$). Hydrolysis of $\\text{NH}_4^+$ yields $[\\text{H}_3\\text{O}^+] = \\sqrt{(0.050)(5.6 \\times 10^{-10})} = 5.3 \\times 10^{-6}\\,\\text{M}$, or $\\text{pH} \\approx 5.28$. The best indicator has $\\text{p}K_{\\text{in}}$ close to the equivalence-point $\\text{pH}$ ($5.28$), which is methyl red ($\\text{p}K_{\\text{in}} = 5.0$, range $4.2 - 6.2$)."
    },
    {
        "unit_q_num": 24,
        "topic_code": "8.5",
        "topic_title": "Acid-Base Titrations",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "A $20.0\\,\\text{mL}$ sample of $0.10\\,\\text{M}$ diprotic weak acid $\\text{H}_2\\text{A}(aq)$ ($\\text{p}K_{a1} = 3.00$, $\\text{p}K_{a2} = 8.00$) is titrated with $0.10\\,\\text{M}\\,\\text{NaOH}(aq)$. After $30.0\\,\\text{mL}$ of $0.10\\,\\text{M}\\,\\text{NaOH}(aq)$ has been added, what are the predominant $\\text{A}$-containing species in the solution and the approximate $\\text{pH}$?",
        "options": [
            "$[\\text{H}_2\\text{A}] \\approx [\\text{HA}^-]$ and $\\text{pH} \\approx 3.00$",
            "$\\text{HA}^-$ only and $\\text{pH} \\approx 5.50$",
            "$[\\text{HA}^-] \\approx [\\text{A}^{2-}]$ and $\\text{pH} \\approx 8.00$",
            "$\\text{A}^{2-}$ only and $\\text{pH} > 10.00$"
        ],
        "correct_index": 2,
        "explanation": "The first equivalence point requires $20.0\\,\\text{mL}$ of $0.10\\,\\text{M}\\,\\text{NaOH}$ to convert all $\\text{H}_2\\text{A}$ into $\\text{HA}^-$, and the second equivalence point requires $40.0\\,\\text{mL}$ of $0.10\\,\\text{M}\\,\\text{NaOH}$ to convert all $\\text{HA}^-$ into $\\text{A}^{2-}$. At $30.0\\,\\text{mL}$ of $\\text{NaOH}$ added, the titration is at the second half-equivalence point, where half of the $\\text{HA}^-$ has been converted into $\\text{A}^{2-}$. Therefore, $[\\text{HA}^-] \\approx [\\text{A}^{2-}]$ and $\\text{pH} \\approx \\text{p}K_{a2} = 8.00$."
    },
    {
        "unit_q_num": 25,
        "topic_code": "8.5",
        "topic_title": "Acid-Base Titrations",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "Two separate $25.0\\,\\text{mL}$ samples—one of $0.100\\,\\text{M}\\,\\text{HCl}(aq)$ and one of $0.100\\,\\text{M}\\,\\text{CH}_3\\text{COOH}(aq)$ ($K_a = 1.8 \\times 10^{-5}$)—are each titrated with $0.100\\,\\text{M}\\,\\text{NaOH}(aq)$ at $25^\\circ\\text{C}$. How do the volume of $\\text{NaOH}$ required to reach the equivalence point ($V_{\\text{eq}}$) and the $\\text{pH}$ at the equivalence point ($\\text{pH}_{\\text{eq}}$) compare for the two titrations?",
        "options": [
            "$V_{\\text{eq}}$ is larger for $\\text{HCl}$, and $\\text{pH}_{\\text{eq}}$ is lower for $\\text{HCl}$.",
            "$V_{\\text{eq}}$ is the same ($25.0\\,\\text{mL}$) for both acids, and $\\text{pH}_{\\text{eq}}$ is higher for $\\text{CH}_3\\text{COOH}$.",
            "$V_{\\text{eq}}$ is the same ($25.0\\,\\text{mL}$) for both acids, and $\\text{pH}_{\\text{eq}} = 7.00$ for both acids.",
            "$V_{\\text{eq}}$ is smaller for $\\text{CH}_3\\text{COOH}$ because it is only partially ionized, and $\\text{pH}_{\\text{eq}}$ is higher for $\\text{CH}_3\\text{COOH}$."
        ],
        "correct_index": 1,
        "explanation": "The volume of titrant needed to reach the equivalence point depends only on stoichiometry and total moles of monoprotic acid ($n = MV = 0.00250\\,\\text{mol}$), not acid strength, so both require exactly $25.0\\,\\text{mL}$ of $0.100\\,\\text{M}\\,\\text{NaOH}$. At the equivalence point, the $\\text{HCl}$ titration produces neutral $\\text{NaCl}(aq)$ ($\\text{pH}_{\\text{eq}} = 7.00$), whereas the $\\text{CH}_3\\text{COOH}$ titration produces basic $\\text{CH}_3\\text{COO}^-(aq)$ ($\\text{pH}_{\\text{eq}} \\approx 8.72$)."
    },

    # -------------------------------------------------------------------------
    # 8.6 Molecular Structure of Acids and Bases (Q26 - Q30)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 26,
        "topic_code": "8.6",
        "topic_title": "Molecular Structure of Acids and Bases",
        "difficulty": "AP Exam Level",
        "stimulus": """<table class="quiz-data-table">
<thead>
<tr><th>Binary Acid</th><th>$\\text{H}-\\text{X}$ Bond Length ($\\text{pm}$)</th><th>$\\text{H}-\\text{X}$ Bond Enthalpy ($\\text{kJ/mol}$)</th><th>$\\text{p}K_a$ in Water</th></tr>
</thead>
<tbody>
<tr><td>$\\text{HF}$</td><td>$92$</td><td>$567$</td><td>$+3.17$</td></tr>
<tr><td>$\\text{HCl}$</td><td>$127$</td><td>$431$</td><td>$-7$</td></tr>
<tr><td>$\\text{HBr}$</td><td>$141$</td><td>$366$</td><td>$-9$</td></tr>
<tr><td>$\\text{HI}$</td><td>$161$</td><td>$299$</td><td>$-10$</td></tr>
</tbody>
</table>""",
        "question": "Although fluorine is the most electronegative halogen, $\\text{HF}$ is a weak acid in water whereas $\\text{HCl}$, $\\text{HBr}$, and $\\text{HI}$ are strong acids. Based on the data in the table above, which statement best explains why acid strength increases from $\\text{HF}$ to $\\text{HI}$?",
        "options": [
            "As halogen electronegativity decreases down Group 17, the $\\text{H}-\\text{X}$ bond becomes more polar, making $\\text{H}^+$ easier to remove.",
            "The fluoride ion $\\text{F}^-$ is the largest halide ion and therefore the least stable conjugate base in water.",
            "$\\text{HI}$ forms the strongest intermolecular hydrogen bonds with water molecules.",
            "As atomic radius increases down Group 17, the $\\text{H}-\\text{X}$ bond becomes longer and weaker, requiring much less energy to break during ionization."
        ],
        "correct_index": 3,
        "explanation": "Down a group in the periodic table, the size of the atom bonded to hydrogen increases significantly. Poor orbital overlap with the larger halogen atoms results in a progressively longer and weaker $\\text{H}-\\text{X}$ bond (bond enthalpy drops from $567\\,\\text{kJ/mol}$ in $\\text{HF}$ to $299\\,\\text{kJ/mol}$ in $\\text{HI}$), which dominates over bond polarity and makes proton donation much more favorable."
    },
    {
        "unit_q_num": 27,
        "topic_code": "8.6",
        "topic_title": "Molecular Structure of Acids and Bases",
        "difficulty": "AP Exam Level",
        "stimulus": """<table class="quiz-data-table">
<thead>
<tr><th>Oxoacid</th><th>Lewis / Structural Formula</th><th>$K_a$ at $25^\\circ\\text{C}$</th></tr>
</thead>
<tbody>
<tr><td>Hypochlorous acid</td><td>$\\text{H}-\\text{O}-\\text{Cl}$</td><td>$4.0 \\times 10^{-8}$</td></tr>
<tr><td>Chlorous acid</td><td>$\\text{H}-\\text{O}-\\text{Cl}=\\text{O}$</td><td>$1.1 \\times 10^{-2}$</td></tr>
<tr><td>Chloric acid</td><td>$\\text{H}-\\text{O}-\\text{ClO}_2$</td><td>$\\approx 10^1$</td></tr>
<tr><td>Perchloric acid</td><td>$\\text{H}-\\text{O}-\\text{ClO}_3$</td><td>$\\approx 10^8$</td></tr>
</tbody>
</table>""",
        "question": "Based on the molecular structures in the table above, why does the acid strength of the chlorine oxoacids increase dramatically from $\\text{HOCl}$ to $\\text{HClO}_4$?",
        "options": [
            "The $\\text{H}-\\text{Cl}$ bond becomes shorter and stronger as more oxygen atoms are attached to the hydrogen atom.",
            "Additional electronegative oxygen atoms withdraw electron density from the $\\text{O}-\\text{H}$ bond via the inductive effect and delocalize the negative charge of the conjugate base across more oxygen atoms.",
            "The molar mass of the acid increases, which increases London dispersion forces with water.",
            "Perchloric acid contains four ionizable protons per molecule, whereas hypochlorous acid contains only one."
        ],
        "correct_index": 1,
        "explanation": "In oxoacids of the form $\\text{H}-\\text{O}-\\text{ClO}_n$, adding terminal electronegative oxygen atoms pulls electron density away from the central $\\text{Cl}$ atom and the $\\text{O}-\\text{H}$ bond (inductive effect), making the $\\text{O}-\\text{H}$ bond more polar and weaker. Furthermore, in the conjugate base $\\text{ClO}_4^-$, the $-1$ charge is delocalized by resonance over four equivalent oxygen atoms, greatly stabilizing the conjugate base."
    },
    {
        "unit_q_num": 28,
        "topic_code": "8.6",
        "topic_title": "Molecular Structure of Acids and Bases",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "Which of the following correctly ranks the hypohalous acids $\\text{HOCl}$, $\\text{HOBr}$, and $\\text{HOI}$ in order of increasing acid strength ($K_a$) in aqueous solution, and provides the correct justification?",
        "options": [
            "$\\text{HOI} < \\text{HOBr} < \\text{HOCl}$, because $\\text{Cl}$ is the most electronegative halogen and withdraws the most electron density from the $\\text{O}-\\text{H}$ bond.",
            "$\\text{HOCl} < \\text{HOBr} < \\text{HOI}$, because the $\\text{O}-\\text{I}$ bond is the weakest bond.",
            "$\\text{HOI} < \\text{HOBr} < \\text{HOCl}$, because the $\\text{H}-\\text{Cl}$ bond is longer than the $\\text{H}-\\text{I}$ bond.",
            "$\\text{HOCl} = \\text{HOBr} = \\text{HOI}$, because in all three acids the acidic proton is bonded to an oxygen atom."
        ],
        "correct_index": 0,
        "explanation": "In the series $\\text{H}-\\text{O}-\\text{X}$ ($\\text{X} = \\text{Cl}, \\text{Br}, \\text{I}$), the acidic proton is bonded to oxygen in all three molecules. Because electronegativity increases in the order $\\text{I} < \\text{Br} < \\text{Cl}$, chlorine exerts the strongest inductive electron-withdrawing effect on the $\\text{O}-\\text{H}$ bond and best stabilizes the negative charge on the $\\text{OX}^-$ conjugate base. Thus, acid strength increases as $\\text{HOI} < \\text{HOBr} < \\text{HOCl}$."
    },
    {
        "unit_q_num": 29,
        "topic_code": "8.6",
        "topic_title": "Molecular Structure of Acids and Bases",
        "difficulty": "AP Exam Level",
        "stimulus": """<table class="quiz-data-table">
<thead>
<tr><th>Carboxylic Acid</th><th>Formula</th><th>$\\text{p}K_a$ at $25^\\circ\\text{C}$</th></tr>
</thead>
<tbody>
<tr><td>Acetic acid</td><td>$\\text{CH}_3\\text{COOH}$</td><td>$4.76$</td></tr>
<tr><td>Chloroacetic acid</td><td>$\\text{CH}_2\\text{ClCOOH}$</td><td>$2.87$</td></tr>
<tr><td>Dichloroacetic acid</td><td>$\\text{CHCl}_2\\text{COOH}$</td><td>$1.35$</td></tr>
<tr><td>Trichloroacetic acid</td><td>$\\text{CCl}_3\\text{COOH}$</td><td>$0.66$</td></tr>
</tbody>
</table>""",
        "question": "Based on the trend shown in the table above, which of the following best predicts the $\\text{p}K_a$ of trifluoroacetic acid, $\\text{CF}_3\\text{COOH}$, at $25^\\circ\\text{C}$ and explains why?",
        "options": [
            "$\\text{p}K_a \\approx 0.23$, because fluorine is more electronegative than chlorine and exerts a stronger inductive electron-withdrawing effect that further stabilizes $\\text{CF}_3\\text{COO}^-$.",
            "$\\text{p}K_a \\approx 1.80$, because the $\\text{C}-\\text{F}$ bond is shorter and stronger than the $\\text{C}-\\text{Cl}$ bond, preventing ionization.",
            "$\\text{p}K_a \\approx 5.10$, because fluorine donates electron density into the carboxyl group.",
            "$\\text{p}K_a \\approx 0.66$, because substituting one halogen for another has no effect on the $\\text{O}-\\text{H}$ bond."
        ],
        "correct_index": 0,
        "explanation": "Replacing $\\text{H}$ atoms on the methyl group with electronegative halogen atoms pulls electron density away from the carboxylate group via the inductive effect, polarizing the $\\text{O}-\\text{H}$ bond and stabilizing the conjugate base. Because fluorine is more electronegative than chlorine, $\\text{CF}_3\\text{COOH}$ is an even stronger acid than $\\text{CCl}_3\\text{COOH}$ ($\\text{p}K_a = 0.66$), giving it a lower $\\text{p}K_a$ ($\\approx 0.23$)."
    },
    {
        "unit_q_num": 30,
        "topic_code": "8.6",
        "topic_title": "Molecular Structure of Acids and Bases",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": "Both ethanol ($\\text{CH}_3\\text{CH}_2\\text{OH}$, $\\text{p}K_a \\approx 16$) and acetic acid ($\\text{CH}_3\\text{COOH}$, $\\text{p}K_a = 4.76$) contain an $-\\text{OH}$ group, yet acetic acid has an acid dissociation constant more than $10^{11}$ times larger than that of ethanol. Which of the following best accounts for this difference?",
        "options": [
            "Ethanol has more hydrogen atoms than acetic acid, which suppresses proton donation.",
            "Ethanol cannot form hydrogen bonds with water, whereas acetic acid can.",
            "The $\\text{C}-\\text{C}$ bond in acetic acid breaks during ionization to release $\\text{H}_3\\text{O}^+$.",
            "In the acetate ion ($\\text{CH}_3\\text{COO}^-$), the negative charge is delocalized across two electronegative oxygen atoms via resonance, whereas in the ethoxide ion ($\\text{CH}_3\\text{CH}_2\\text{O}^-$), the negative charge is localized on a single oxygen atom."
        ],
        "correct_index": 3,
        "explanation": "In acetic acid, the carbonyl oxygen ($\\text{C}=\\text{O}$) withdraws electron density from the $-\\text{OH}$ group via induction, and upon deprotonation, the resulting acetate ion ($\\text{CH}_3\\text{COO}^-$) is stabilized by resonance delocalization of the $-1$ charge equally over two oxygen atoms. In ethoxide ($\\text{CH}_3\\text{CH}_2\\text{O}^-$), no resonance stabilization is possible and the negative charge remains localized on one oxygen atom."
    },

    # -------------------------------------------------------------------------
    # 8.7 pH and pKa (Q31 - Q35)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 31,
        "topic_code": "8.7",
        "topic_title": "pH and pKa",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "Propanoic acid, $\\text{CH}_3\\text{CH}_2\\text{COOH}$, is a weak monoprotic acid with $\\text{p}K_a = 4.87$ at $25^\\circ\\text{C}$. If a buffer solution containing propanoic acid and sodium propanoate is adjusted to $\\text{pH} = 5.87$, which of the following correctly compares the concentrations of propanoic acid and propanoate ion in the solution?",
        "options": [
            "$[\\text{CH}_3\\text{CH}_2\\text{COOH}] = 10 \\times [\\text{CH}_3\\text{CH}_2\\text{COO}^-]$",
            "$[\\text{CH}_3\\text{CH}_2\\text{COO}^-] = 10 \\times [\\text{CH}_3\\text{CH}_2\\text{COOH}]$",
            "$[\\text{CH}_3\\text{CH}_2\\text{COO}^-] = [\\text{CH}_3\\text{CH}_2\\text{COOH}]$",
            "$[\\text{CH}_3\\text{CH}_2\\text{COO}^-] = 1.2 \\times [\\text{CH}_3\\text{CH}_2\\text{COOH}]$"
        ],
        "correct_index": 1,
        "explanation": "When $\\text{pH} > \\text{p}K_a$, the deprotonated conjugate base form predominates. Using $\\text{pH} = \\text{p}K_a + \\log\\left(\\frac{[\\text{A}^-]}{[\\text{HA}]}\\right)$, we have $5.87 = 4.87 + \\log\\left(\\frac{[\\text{A}^-]}{[\\text{HA}]}\\right)$, so $\\log\\left(\\frac{[\\text{A}^-]}{[\\text{HA}]}\\right) = 1.00$ and $\\frac{[\\text{CH}_3\\text{CH}_2\\text{COO}^-]}{[\\text{CH}_3\\text{CH}_2\\text{COOH}]} = 10^1 = 10$. A ratio of $1.2$ comes from dividing the pH by the $\\text{p}K_a$ ($\\frac{5.87}{4.87}$), which is not valid: the ratio depends on the difference $\\text{pH} - \\text{p}K_a$, and a pH above the $\\text{p}K_a$ means the base form predominates."
    },
    {
        "unit_q_num": 32,
        "topic_code": "8.7",
        "topic_title": "pH and pKa",
        "difficulty": "AP Exam Level",
        "stimulus": """<table class="quiz-data-table">
<thead>
<tr><th>Citric Acid ($\\text{H}_3\\text{Cit}$) Ionization Step</th><th>$\\text{p}K_a$ at $25^\\circ\\text{C}$</th></tr>
</thead>
<tbody>
<tr><td>$\\text{H}_3\\text{Cit}(aq) + \\text{H}_2\\text{O}(l) \\rightleftharpoons \\text{H}_3\\text{O}^+(aq) + \\text{H}_2\\text{Cit}^-(aq)$</td><td>$\\text{p}K_{a1} = 3.13$</td></tr>
<tr><td>$\\text{H}_2\\text{Cit}^-(aq) + \\text{H}_2\\text{O}(l) \\rightleftharpoons \\text{H}_3\\text{O}^+(aq) + \\text{HCit}^{2-}(aq)$</td><td>$\\text{p}K_{a2} = 4.76$</td></tr>
<tr><td>$\\text{HCit}^{2-}(aq) + \\text{H}_2\\text{O}(l) \\rightleftharpoons \\text{H}_3\\text{O}^+(aq) + \\text{Cit}^{3-}(aq)$</td><td>$\\text{p}K_{a3} = 6.40$</td></tr>
</tbody>
</table>""",
        "question": "Citric acid, $\\text{H}_3\\text{Cit}$, is a triprotic acid with the $\\text{p}K_a$ values shown in the table above. In an aqueous citrate solution buffered at $\\text{pH} = 5.50$, which of the four citrate species is present in the highest concentration?",
        "options": [
            "$\\text{H}_3\\text{Cit}$",
            "$\\text{H}_2\\text{Cit}^-$",
            "$\\text{HCit}^{2-}$",
            "$\\text{Cit}^{3-}$"
        ],
        "correct_index": 2,
        "explanation": "For a polyprotic acid, the predominant species depends on how the solution $\\text{pH}$ compares to each $\\text{p}K_a$: for $\\text{pH} < \\text{p}K_{a1}$ ($3.13$), $\\text{H}_3\\text{Cit}$ predominates; for $\\text{p}K_{a1} < \\text{pH} < \\text{p}K_{a2}$ ($3.13 < \\text{pH} < 4.76$), $\\text{H}_2\\text{Cit}^-$ predominates; for $\\text{p}K_{a2} < \\text{pH} < \\text{p}K_{a3}$ ($4.76 < \\text{pH} < 6.40$), $\\text{HCit}^{2-}$ predominates; and for $\\text{pH} > \\text{p}K_{a3}$ ($6.40$), $\\text{Cit}^{3-}$ predominates. Because $\\text{pH} = 5.50$ lies between $\\text{p}K_{a2}$ and $\\text{p}K_{a3}$, $\\text{HCit}^{2-}$ has the highest concentration."
    },
    {
        "unit_q_num": 33,
        "topic_code": "8.7",
        "topic_title": "pH and pKa",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "Bromocresol green is a weak monoprotic acid indicator ($\\text{HIn}$) with $K_{\\text{in}} = 2.0 \\times 10^{-5}$ ($\\text{p}K_{\\text{in}} = 4.70$). The protonated form $\\text{HIn}(aq)$ is yellow, and the deprotonated form $\\text{In}^-(aq)$ is blue. A few drops of bromocresol green are added to a colorless buffer solution, and the solution turns green (containing approximately equal concentrations of yellow $\\text{HIn}$ and blue $\\text{In}^-$). What is the approximate $\\text{pH}$ of the buffer solution?",
        "options": [
            "$2.00$",
            "$7.00$",
            "$9.30$",
            "$4.70$"
        ],
        "correct_index": 3,
        "explanation": "For an acid-base indicator $\\text{HIn}(aq) + \\text{H}_2\\text{O}(l) \\rightleftharpoons \\text{H}_3\\text{O}^+(aq) + \\text{In}^-(aq)$, the Henderson-Hasselbalch relationship gives $\\text{pH} = \\text{p}K_{\\text{in}} + \\log\\left(\\frac{[\\text{In}^-]}{[\\text{HIn}]}\\right)$. When the indicator appears intermediate in color (green), $[\\text{HIn}] \\approx [\\text{In}^-]$, so $\\text{pH} \\approx \\text{p}K_{\\text{in}} = 4.70$."
    },
    {
        "unit_q_num": 34,
        "topic_code": "8.7",
        "topic_title": "pH and pKa",
        "difficulty": "AP Exam Level",
        "stimulus": """<table class="quiz-data-table">
<thead>
<tr><th>Ionizable Group of Glycine</th><th>Equilibrium</th><th>$\\text{p}K_a$ at $25^\\circ\\text{C}$</th></tr>
</thead>
<tbody>
<tr><td>Carboxylic acid group</td><td>$-\\text{COOH} \\rightleftharpoons -\\text{COO}^- + \\text{H}^+$</td><td>$2.34$</td></tr>
<tr><td>Protonated amino group</td><td>$-\\text{NH}_3^+ \\rightleftharpoons -\\text{NH}_2 + \\text{H}^+$</td><td>$9.60$</td></tr>
</tbody>
</table>""",
        "question": "Glycine ($\\text{H}_2\\text{N}-\\text{CH}_2-\\text{COOH}$) has the two ionizable groups listed in the table above. In an aqueous solution buffered at physiological $\\text{pH} = 7.40$, which of the following structures represents the predominant form of glycine?",
        "options": [
            "$\\text{H}_3\\text{N}^+-\\text{CH}_2-\\text{COOH}$",
            "$\\text{H}_3\\text{N}^+-\\text{CH}_2-\\text{COO}^-$",
            "$\\text{H}_2\\text{N}-\\text{CH}_2-\\text{COOH}$",
            "$\\text{H}_2\\text{N}-\\text{CH}_2-\\text{COO}^-$"
        ],
        "correct_index": 1,
        "explanation": "At $\\text{pH} = 7.40$, the $\\text{pH}$ is well above the $\\text{p}K_a$ of the carboxylic acid group ($7.40 > 2.34$), so the carboxyl group is predominantly deprotonated ($-\\text{COO}^-$). At the same time, the $\\text{pH}$ is well below the $\\text{p}K_a$ of the protonated amino group ($7.40 < 9.60$), so the amino group remains predominantly protonated ($-\\text{NH}_3^+$). Therefore, the zwitterion $\\text{H}_3\\text{N}^+-\\text{CH}_2-\\text{COO}^-$ is the predominant species."
    },
    {
        "unit_q_num": 35,
        "topic_code": "8.7",
        "topic_title": "pH and pKa",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": "A weak monoprotic acid, $\\text{HA}$, has $\\text{p}K_a = 5.00$. At what $\\text{pH}$ is the acid exactly $90.\\%$ in its deprotonated conjugate base form, $\\text{A}^-$, and $10.\\%$ in its protonated form, $\\text{HA}$? ($\\log(9.0) = 0.95$)",
        "options": [
            "$4.05$",
            "$5.00$",
            "$5.95$",
            "$6.00$"
        ],
        "correct_index": 2,
        "explanation": "When $90.\\%$ of the acid is in the $\\text{A}^-$ form and $10.\\%$ is in the $\\text{HA}$ form, the concentration ratio is $\\frac{[\\text{A}^-]}{[\\text{HA}]} = \\frac{0.90}{0.10} = 9.0$. Substituting into the Henderson-Hasselbalch equation gives $\\text{pH} = \\text{p}K_a + \\log\\left(\\frac{[\\text{A}^-]}{[\\text{HA}]}\\right) = 5.00 + \\log(9.0) = 5.00 + 0.95 = 5.95$."
    },

    # -------------------------------------------------------------------------
    # 8.8 Properties of Buffers (Q36 - Q40)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 36,
        "topic_code": "8.8",
        "topic_title": "Properties of Buffers",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "An aqueous buffer solution is prepared with $0.50\\,\\text{M}\\,\\text{HF}(aq)$ and $0.50\\,\\text{M}\\,\\text{NaF}(aq)$. When a small amount of concentrated $\\text{HNO}_3(aq)$ is added to this buffer, which of the following net ionic equations represents the reaction that prevents a large decrease in $\\text{pH}$?",
        "options": [
            "$\\text{HF}(aq) + \\text{H}_3\\text{O}^+(aq) \\rightarrow \\text{H}_2\\text{F}^+(aq) + \\text{H}_2\\text{O}(l)$",
            "$\\text{F}^-(aq) + \\text{H}_3\\text{O}^+(aq) \\rightarrow \\text{HF}(aq) + \\text{H}_2\\text{O}(l)$",
            "$\\text{HF}(aq) + \\text{NO}_3^-(aq) \\rightarrow \\text{HNO}_3(aq) + \\text{F}^-(aq)$",
            "$\\text{Na}^+(aq) + \\text{NO}_3^-(aq) \\rightarrow \\text{NaNO}_3(s)$"
        ],
        "correct_index": 1,
        "explanation": "When a strong acid ($\\text{HNO}_3$, source of $\\text{H}_3\\text{O}^+$) is added to an $\\text{HF}/\\text{F}^-$ buffer, the conjugate base component of the buffer ($\\text{F}^-$) reacts nearly quantitatively with the added $\\text{H}_3\\text{O}^+$ to form weak acid $\\text{HF}$ and water: $\\text{F}^-(aq) + \\text{H}_3\\text{O}^+(aq) \\rightarrow \\text{HF}(aq) + \\text{H}_2\\text{O}(l)$. This consumes the added $\\text{H}_3\\text{O}^+$ and prevents a large drop in $\\text{pH}$."
    },
    {
        "unit_q_num": 37,
        "topic_code": "8.8",
        "topic_title": "Properties of Buffers",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "A $100.\\,\\text{mL}$ buffer solution contains $0.20\\,\\text{M}\\,\\text{NH}_3(aq)$ and $0.20\\,\\text{M}\\,\\text{NH}_4\\text{Cl}(aq)$ at $25^\\circ\\text{C}$ ($\\text{pH} = 9.25$). If $100.\\,\\text{mL}$ of pure distilled water is added to this buffer at $25^\\circ\\text{C}$, how are the $\\text{pH}$ of the buffer and the number of moles of $\\text{HCl}$ the total solution can neutralize before losing its buffer action affected?",
        "options": [
            "Both the $\\text{pH}$ and the total moles of $\\text{HCl}$ that can be neutralized decrease.",
            "The $\\text{pH}$ decreases by $0.30$ units, while the total moles of $\\text{HCl}$ that can be neutralized remains unchanged.",
            "Neither the $\\text{pH}$ nor the total moles of $\\text{HCl}$ that can be neutralized by the entire solution changes.",
            "The $\\text{pH}$ increases, while the total moles of $\\text{HCl}$ that can be neutralized decreases."
        ],
        "correct_index": 2,
        "explanation": "In the Henderson-Hasselbalch equation, $\\text{pH} = \\text{p}K_a + \\log\\left(\\frac{[\\text{NH}_3]}{[\\text{NH}_4^+]}\\right) = \\text{p}K_a + \\log\\left(\\frac{n_{\\text{NH}_3}/V}{n_{\\text{NH}_4^+}/V}\\right)$. Diluting the buffer with pure water changes the volume $V$ equally for both species, so the mole ratio $\\frac{n_{\\text{NH}_3}}{n_{\\text{NH}_4^+}}$ and the $\\text{pH}$ remain unchanged. Furthermore, because the total moles of $\\text{NH}_3$ in the entire container ($0.020\\,\\text{mol}$) did not change, the total moles of $\\text{HCl}$ the entire solution can neutralize also remains unchanged."
    },
    {
        "unit_q_num": 38,
        "topic_code": "8.8",
        "topic_title": "Properties of Buffers",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "Which of the following pairs of substances, when dissolved in $1.0\\,\\text{L}$ of water in equimolar ($0.20\\,\\text{mol}$ each) amounts, will NOT form a buffer solution?",
        "options": [
            "$\\text{NaH}_2\\text{PO}_4$ and $\\text{Na}_2\\text{HPO}_4$",
            "$\\text{HNO}_3$ and $\\text{NaNO}_3$",
            "$\\text{CH}_3\\text{NH}_2$ and $\\text{CH}_3\\text{NH}_3\\text{Cl}$",
            "$\\text{HCOOH}$ and $\\text{HCOONa}$"
        ],
        "correct_index": 1,
        "explanation": "A buffer requires a weak acid and its conjugate base (or a weak base and its conjugate acid). $\\text{HNO}_3$ is a strong acid that dissociates completely in water, and $\\text{NO}_3^-$ has negligible basicity in water (it cannot accept $\\text{H}_3\\text{O}^+$ to reform $\\text{HNO}_3$). Therefore, a mixture of $\\text{HNO}_3$ and $\\text{NaNO}_3$ is simply a strong acid solution and cannot act as a buffer."
    },
    {
        "unit_q_num": 39,
        "topic_code": "8.8",
        "topic_title": "Properties of Buffers",
        "difficulty": "AP Exam Level",
        "stimulus": """<table class="quiz-data-table">
<thead>
<tr><th>Beaker</th><th>Particle Count of $\\text{HA}$</th><th>Particle Count of $\\text{A}^-$ (with $\\text{Na}^+$)</th></tr>
</thead>
<tbody>
<tr><td>Initial Buffer</td><td>$6$ molecules of $\\text{HA}$</td><td>$6$ ions of $\\text{A}^-$</td></tr>
</tbody>
</table>""",
        "question": "A particulate representation of a buffer solution initially shows $6$ molecules of a weak acid $\\text{HA}$ and $6$ ions of its conjugate base $\\text{A}^-$ (spectator $\\text{Na}^+$ ions and water molecules are omitted for clarity). If a quantity of $\\text{NaOH}$ equivalent to $2$ $\\text{OH}^-$ ions is added to this sample, how many $\\text{HA}$ molecules and $\\text{A}^-$ ions will be present after the reaction goes to completion?",
        "options": [
            "$6$ $\\text{HA}$ molecules and $8$ $\\text{A}^-$ ions",
            "$4$ $\\text{HA}$ molecules and $6$ $\\text{A}^-$ ions",
            "$4$ $\\text{HA}$ molecules and $8$ $\\text{A}^-$ ions",
            "$8$ $\\text{HA}$ molecules and $4$ $\\text{A}^-$ ions"
        ],
        "correct_index": 2,
        "explanation": "Added $\\text{OH}^-$ ions react stoichiometrically with the weak acid $\\text{HA}$ according to $\\text{HA}(aq) + \\text{OH}^-(aq) \\rightarrow \\text{A}^-(aq) + \\text{H}_2\\text{O}(l)$. Adding $2$ $\\text{OH}^-$ ions consumes $2$ $\\text{HA}$ molecules (reducing $\\text{HA}$ from $6$ to $4$) and produces $2$ additional $\\text{A}^-$ ions (increasing $\\text{A}^-$ from $6$ to $8$)."
    },
    {
        "unit_q_num": 40,
        "topic_code": "8.8",
        "topic_title": "Properties of Buffers",
        "difficulty": "Challenging",
        "stimulus": r'<table class="quiz-data-table"><thead><tr><th>Solution</th><th>Composition</th><th>Initial $\text{pH}$</th><th>$\text{pH}$ After Adding $1.0\,\text{mL}$ of $1.0\,\text{M}\,\text{NaOH}$</th></tr></thead><tbody><tr><td>Solution $1$</td><td>$100.\,\text{mL}$ of $1.0 \times 10^{-5}\,\text{M}\,\text{HCl}(aq)$</td><td>$5.00$</td><td>$12.00$</td></tr><tr><td>Solution $2$</td><td>$100.\,\text{mL}$ of $0.50\,\text{M}\,\text{HA}$ and $0.50\,\text{M}\,\text{NaA}$ ($\text{p}K_a = 5.00$)</td><td>$5.00$</td><td>$5.02$</td></tr></tbody></table>',
        "question": r"Both solutions in the table above have an initial $\text{pH}$ of $5.00$ at $25^\circ\text{C}$. A student adds $1.0\,\text{mL}$ of $1.0\,\text{M}\,\text{NaOH}(aq)$ ($1.0\,\text{mmol}$ of $\text{OH}^-$) to each solution and records the $\text{pH}$ values shown. Which of the following best explains the difference between the two results?",
        "options": [
            r"Solution $2$ contains $50.\,\text{mmol}$ of $\text{HA}$, which reacts with the added $\text{OH}^-$ to form $\text{A}^-$ and $\text{H}_2\text{O}$ and changes the ratio $[\text{A}^-]/[\text{HA}]$ only slightly; Solution $1$ contains only $0.0010\,\text{mmol}$ of $\text{H}_3\text{O}^+$, so nearly all of the added $\text{OH}^-$ remains in solution.",
            r"In Solution $2$, the $\text{A}^-$ ions react with the added $\text{OH}^-$ to form $\text{HA}$, which removes the $\text{OH}^-$ from solution.",
            r"In Solution $2$, the $\text{Na}^+$ ions combine with the added $\text{OH}^-$ to form $\text{NaOH}$ molecules, which do not affect the $\text{pH}$.",
            r"Solution $2$ has a much higher initial $[\text{H}_3\text{O}^+]$ than Solution $1$, so more $\text{H}_3\text{O}^+$ is available to neutralize the added $\text{OH}^-$.",
        ],
        "correct_index": 0,
        "explanation": r"Both solutions start with $[\text{H}_3\text{O}^+] = 1.0 \times 10^{-5}\,\text{M}$, so the difference must come from the other species present. Solution $1$ contains only $(0.100\,\text{L})(1.0 \times 10^{-5}\,\text{M}) = 1.0 \times 10^{-6}\,\text{mol}$ ($0.0010\,\text{mmol}$) of $\text{H}_3\text{O}^+$, far less than the $1.0\,\text{mmol}$ of $\text{OH}^-$ added, so almost all of the $\text{OH}^-$ remains and the pH rises to about $12$. Solution $2$ is a buffer: its $50.\,\text{mmol}$ of $\text{HA}$ consumes the added base, $\text{HA}(aq) + \text{OH}^-(aq) \rightarrow \text{A}^-(aq) + \text{H}_2\text{O}(l)$, converting only a small fraction of the $\text{HA}$ into $\text{A}^-$. Because $[\text{A}^-]/[\text{HA}]$ stays close to $1$, the pH stays close to the $\text{p}K_a$. The conjugate base $\text{A}^-$ neutralizes added acid, not added base, and $\text{Na}^+$ is a spectator ion.",
    },

    # -------------------------------------------------------------------------
    # 8.9 Henderson-Hasselbalch Equation (Q41 - Q45)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 41,
        "topic_code": "8.9",
        "topic_title": "Henderson-Hasselbalch Equation",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "What is the $\\text{pH}$ at $25^\\circ\\text{C}$ of a buffer solution that is $0.20\\,\\text{M}$ in acetic acid, $\\text{CH}_3\\text{COOH}$ ($\\text{p}K_a = 4.76$), and $0.60\\,\\text{M}$ in sodium acetate, $\\text{CH}_3\\text{COONa}$? ($\\log(3.0) = 0.48$)",
        "options": [
            "$4.28$",
            "$4.76$",
            "$5.24$",
            "$5.36$"
        ],
        "correct_index": 2,
        "explanation": "Using the Henderson-Hasselbalch equation:\n$$\\text{pH} = \\text{p}K_a + \\log\\left(\\frac{[\\text{A}^-]}{[\\text{HA}]}\\right) = 4.76 + \\log\\left(\\frac{0.60}{0.20}\\right) = 4.76 + \\log(3.0) = 4.76 + 0.48 = 5.24$$"
    },
    {
        "unit_q_num": 42,
        "topic_code": "8.9",
        "topic_title": "Henderson-Hasselbalch Equation",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "A biochemist wants to prepare $500.\\,\\text{mL}$ of a formate buffer with $\\text{pH} = 4.05$ using $0.10\\,\\text{M}$ formic acid, $\\text{HCOOH}$ ($\\text{p}K_a = 3.75$), and solid sodium formate, $\\text{HCOONa}$ ($\\text{molar mass} = 68.0\\,\\text{g/mol}$). Assuming no volume change upon dissolving the solid, what mass of $\\text{HCOONa}$ must be added to the $500.\\,\\text{mL}$ of $0.10\\,\\text{M}\\,\\text{HCOOH}$? ($10^{0.30} = 2.0$)",
        "options": [
            "$1.7\\,\\text{g}$",
            "$3.4\\,\\text{g}$",
            "$13.6\\,\\text{g}$",
            "$6.8\\,\\text{g}$"
        ],
        "correct_index": 3,
        "explanation": "Using the Henderson-Hasselbalch equation, $4.05 = 3.75 + \\log\\left(\\frac{[\\text{HCOO}^-]}{0.10\\,\\text{M}}\\right)$, so $\\log\\left(\\frac{[\\text{HCOO}^-]}{0.10\\,\\text{M}}\\right) = 0.30$ and $\\frac{[\\text{HCOO}^-]}{0.10\\,\\text{M}} = 10^{0.30} = 2.0$. Thus, the required concentration of $\\text{HCOO}^-$ is $0.20\\,\\text{M}$. In $0.500\\,\\text{L}$ of solution, the required moles of $\\text{HCOONa}$ are $(0.500\\,\\text{L})(0.20\\,\\text{M}) = 0.10\\,\\text{mol}$, which corresponds to a mass of $(0.10\\,\\text{mol})(68.0\\,\\text{g/mol}) = 6.8\\,\\text{g}$."
    },
    {
        "unit_q_num": 43,
        "topic_code": "8.9",
        "topic_title": "Henderson-Hasselbalch Equation",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"A buffer is prepared at $25^\circ\text{C}$ by mixing $50.0\,\text{mL}$ of $0.40\,\text{M}\,\text{HNO}_2(aq)$ ($\text{p}K_a = 3.35$) with $100.0\,\text{mL}$ of $0.10\,\text{M}\,\text{NaNO}_2(aq)$. What is the $\text{pH}$ of the buffer? ($\log(2.0) = 0.30$)",
        "options": [
            r"$2.75$",
            r"$3.05$",
            r"$3.35$",
            r"$3.65$",
        ],
        "correct_index": 1,
        "explanation": r"Mixing changes the volume of both buffer components equally, so the Henderson-Hasselbalch ratio can be written in moles. $n_{\text{HNO}_2} = (0.0500\,\text{L})(0.40\,\text{M}) = 0.020\,\text{mol}$ and $n_{\text{NO}_2^-} = (0.1000\,\text{L})(0.10\,\text{M}) = 0.010\,\text{mol}$. Then $\text{pH} = \text{p}K_a + \log\left(\frac{n_{\text{NO}_2^-}}{n_{\text{HNO}_2}}\right) = 3.35 + \log(0.50) = 3.35 - 0.30 = 3.05$. Using the stock concentrations ($\frac{0.10}{0.40}$) ignores the different volumes that were mixed and gives $2.75$; inverting the ratio gives $3.65$; and a pH of $3.35$ would require equal amounts of $\text{HNO}_2$ and $\text{NO}_2^-$.",
    },
    {
        "unit_q_num": 44,
        "topic_code": "8.9",
        "topic_title": "Henderson-Hasselbalch Equation",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "At $25^\\circ\\text{C}$, ammonia ($\\text{NH}_3$) has $K_b = 1.8 \\times 10^{-5}$ ($\\text{p}K_b = 4.74$, so $\\text{p}K_a$ of $\\text{NH}_4^+ = 9.26$). What is the $\\text{pH}$ of a buffer solution containing $0.40\\,\\text{M}\\,\\text{NH}_3(aq)$ and $0.10\\,\\text{M}\\,\\text{NH}_4\\text{Cl}(aq)$ at $25^\\circ\\text{C}$? ($\\log(4.0) = 0.60$)",
        "options": [
            "$4.14$",
            "$8.66$",
            "$9.26$",
            "$9.86$"
        ],
        "correct_index": 3,
        "explanation": "In an $\\text{NH}_3/\\text{NH}_4^+$ buffer, $\\text{NH}_4^+$ is the weak acid ($\\text{HA}$, $\\text{p}K_a = 9.26$) and $\\text{NH}_3$ is its conjugate base ($\\text{A}^-$). Using the Henderson-Hasselbalch equation:\n$$\\text{pH} = \\text{p}K_a + \\log\\left(\\frac{[\\text{NH}_3]}{[\\text{NH}_4^+]}\\right) = 9.26 + \\log\\left(\\frac{0.40}{0.10}\\right) = 9.26 + \\log(4.0) = 9.26 + 0.60 = 9.86$$"
    },
    {
        "unit_q_num": 45,
        "topic_code": "8.9",
        "topic_title": "Henderson-Hasselbalch Equation",
        "difficulty": "Challenging",
        "stimulus": r'<table class="quiz-data-table"><thead><tr><th>Solution</th><th>Composition</th><th>$\text{p}K_a$ of Weak Acid</th></tr></thead><tbody><tr><td>Acetic acid solution</td><td>$100.\,\text{mL}$ of $0.50\,\text{M}\,\text{CH}_3\text{COOH}(aq)$</td><td>$4.76$</td></tr></tbody></table>',
        "question": r"A student wants to convert the acetic acid solution described in the table above into a buffer with $\text{pH} = 5.24$ by adding $1.00\,\text{M}\,\text{NaOH}(aq)$ at $25^\circ\text{C}$. What volume of the $\text{NaOH}$ solution should be added? ($10^{0.48} = 3.0$)",
        "options": [
            r"$12.5\,\text{mL}$",
            r"$25.0\,\text{mL}$",
            r"$37.5\,\text{mL}$",
            r"$50.0\,\text{mL}$",
        ],
        "correct_index": 2,
        "explanation": r"The added $\text{OH}^-$ reacts completely with the weak acid: $\text{CH}_3\text{COOH}(aq) + \text{OH}^-(aq) \rightarrow \text{CH}_3\text{COO}^-(aq) + \text{H}_2\text{O}(l)$. The solution initially contains $(0.100\,\text{L})(0.50\,\text{M}) = 50.\,\text{mmol}$ of $\text{CH}_3\text{COOH}$. If $x$ mmol of $\text{OH}^-$ is added, $x$ mmol of $\text{CH}_3\text{COO}^-$ forms and $(50. - x)$ mmol of $\text{CH}_3\text{COOH}$ remains. For $\text{pH} = 5.24$: $\log\left(\frac{x}{50. - x}\right) = 5.24 - 4.76 = 0.48$, so $\frac{x}{50. - x} = 3.0$ and $x = 37.5\,\text{mmol}$, which is $37.5\,\text{mL}$ of $1.00\,\text{M}\,\text{NaOH}$. Adding $25.0\,\text{mL}$ only reaches the half-equivalence point ($\text{pH} = \text{p}K_a = 4.76$), $12.5\,\text{mL}$ gives the inverted ratio ($\text{pH} = 4.28$), and $50.0\,\text{mL}$ consumes all of the acid, leaving no buffer.",
    },

    # -------------------------------------------------------------------------
    # 8.10 Buffer Capacity (Q46 - Q50)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 46,
        "topic_code": "8.10",
        "topic_title": "Buffer Capacity",
        "difficulty": "AP Exam Level",
        "stimulus": """<table class="quiz-data-table">
<thead>
<tr><th>Buffer</th><th>$[\\text{CH}_3\\text{COOH}]$ ($\\text{M}$)</th><th>$[\\text{CH}_3\\text{COO}^-]$ ($\\text{M}$)</th></tr>
</thead>
<tbody>
<tr><td>Buffer $1$</td><td>$1.00$</td><td>$1.00$</td></tr>
<tr><td>Buffer $2$</td><td>$0.50$</td><td>$0.50$</td></tr>
<tr><td>Buffer $3$</td><td>$0.10$</td><td>$0.10$</td></tr>
<tr><td>Buffer $4$</td><td>$0.010$</td><td>$0.010$</td></tr>
</tbody>
</table>""",
        "question": "Equal $100.\\,\\text{mL}$ volumes of the four acetate buffers listed in the table above ($\\text{p}K_a = 4.76$) are prepared at $25^\\circ\\text{C}$. Which statement correctly compares their initial $\\text{pH}$ values and their buffer capacities when $5.0\\,\\text{mL}$ of $1.0\\,\\text{M}\\,\\text{HCl}(aq)$ is added to each?",
        "options": [
            "Buffer $1$ has the lowest initial $\\text{pH}$ and the highest buffer capacity.",
            "All four buffers have the same initial $\\text{pH}$ ($4.76$), and Buffer $1$ exhibits the smallest change in $\\text{pH}$ because it has the highest buffer capacity.",
            "All four buffers have the same initial $\\text{pH}$ ($4.76$) and undergo the exact same change in $\\text{pH}$ upon adding the $\\text{HCl}$.",
            "Buffer $4$ has the highest initial $\\text{pH}$ and the highest buffer capacity."
        ],
        "correct_index": 1,
        "explanation": "Because the ratio $\\frac{[\\text{CH}_3\\text{COO}^-]}{[\\text{CH}_3\\text{COOH}]} = 1.0$ in all four solutions, all four have the exact same initial $\\text{pH} = \\text{p}K_a = 4.76$. However, buffer capacity increases with the absolute concentrations of the weak acid and conjugate base. Buffer $1$ ($1.00\\,\\text{M}$ of each component, $100\\,\\text{mmol}$) has the highest buffer capacity and shows the smallest $\\text{pH}$ change when $5.0\\,\\text{mmol}$ of $\\text{HCl}$ is added (in fact, Buffer $4$'s capacity of $1.0\\,\\text{mmol}$ is completely exceeded)."
    },
    {
        "unit_q_num": 47,
        "topic_code": "8.10",
        "topic_title": "Buffer Capacity",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": "A buffer solution is prepared with $[\\text{HA}] = 0.20\\,\\text{M}$ and $[\\text{A}^-] = 0.80\\,\\text{M}$ ($\\text{p}K_a = 5.00$). Which of the following statements correctly describes the directional buffer capacity of this solution?",
        "options": [
            "The buffer has a greater capacity to neutralize added strong base ($\\text{OH}^-$) than added strong acid ($\\text{H}_3\\text{O}^+$).",
            "The buffer has a greater capacity to neutralize added strong acid ($\\text{H}_3\\text{O}^+$) than added strong base ($\\text{OH}^-$).",
            "The buffer has equal capacity to neutralize added strong acid and added strong base because it is a buffer.",
            "The buffer cannot neutralize any added strong acid because $\\text{pH} > \\text{p}K_a$."
        ],
        "correct_index": 1,
        "explanation": "In a buffer, the conjugate base $\\text{A}^-$ reacts with added strong acid ($\\text{H}_3\\text{O}^+$), whereas the weak acid $\\text{HA}$ reacts with added strong base ($\\text{OH}^-$). Because $[\\text{A}^-] = 0.80\\,\\text{M}$ is four times larger than $[\\text{HA}] = 0.20\\,\\text{M}$, the solution contains four times as many moles of $\\text{A}^-$ as $\\text{HA}$ and therefore has a much greater capacity to neutralize added strong acid than added strong base."
    },
    {
        "unit_q_num": 48,
        "topic_code": "8.10",
        "topic_title": "Buffer Capacity",
        "difficulty": "AP Exam Level",
        "stimulus": """<table class="quiz-data-table">
<thead>
<tr><th>Conjugate Acid-Base Pair</th><th>$K_a$ of Weak Acid</th><th>$\\text{p}K_a$</th></tr>
</thead>
<tbody>
<tr><td>$\\text{H}_2\\text{C}_2\\text{O}_4 / \\text{HC}_2\\text{O}_4^-$</td><td>$5.6 \\times 10^{-2}$</td><td>$1.25$</td></tr>
<tr><td>$\\text{HC}_2\\text{H}_3\\text{O}_2 / \\text{C}_2\\text{H}_3\\text{O}_2^-$</td><td>$1.8 \\times 10^{-5}$</td><td>$4.74$</td></tr>
<tr><td>$\\text{H}_2\\text{PO}_4^- / \\text{HPO}_4^{2-}$</td><td>$6.2 \\times 10^{-8}$</td><td>$7.21$</td></tr>
<tr><td>$\\text{HCO}_3^- / \\text{CO}_3^{2-}$</td><td>$4.7 \\times 10^{-11}$</td><td>$10.33$</td></tr>
</tbody>
</table>""",
        "question": "A chemist needs to prepare an aqueous buffer solution at $\\text{pH} = 7.30$ that has a high capacity against both added strong acid and added strong base. Based on the table above, which of the following $1.0\\,\\text{L}$ mixtures is the best choice?",
        "options": [
            "$0.010\\,\\text{M}\\,\\text{NaH}_2\\text{PO}_4$ and $0.012\\,\\text{M}\\,\\text{Na}_2\\text{HPO}_4$",
            "$0.50\\,\\text{M}\\,\\text{NaH}_2\\text{PO}_4$ and $0.62\\,\\text{M}\\,\\text{Na}_2\\text{HPO}_4$",
            "$0.50\\,\\text{M}\\,\\text{HC}_2\\text{H}_3\\text{O}_2$ and $0.50\\,\\text{M}\\,\\text{NaC}_2\\text{H}_3\\text{O}_2$",
            "$0.50\\,\\text{M}\\,\\text{NaHCO}_3$ and $0.50\\,\\text{M}\\,\\text{Na}_2\\text{CO}_3$"
        ],
        "correct_index": 1,
        "explanation": "An optimal buffer against both acid and base has a $\\text{p}K_a$ as close as possible to the target $\\text{pH}$ (so that $[\\text{A}^-] \\approx [\\text{HA}]$) and high concentrations of both components for high buffer capacity. The $\\text{H}_2\\text{PO}_4^-/\\text{HPO}_4^{2-}$ system has $\\text{p}K_a = 7.21$, which is very close to $7.30$. With $0.50\\,\\text{M}\\,\\text{H}_2\\text{PO}_4^-$ and $0.62\\,\\text{M}\\,\\text{HPO}_4^{2-}$, $\\text{pH} = 7.21 + \\log\\left(\\frac{0.62}{0.50}\\right) = 7.21 + 0.09 = 7.30$, and the high concentrations ($\\sim 0.5\\,\\text{M}$) provide much higher buffer capacity than the $0.01\\,\\text{M}$ mixture."
    },
    {
        "unit_q_num": 49,
        "topic_code": "8.10",
        "topic_title": "Buffer Capacity",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": "A $100.0\\,\\text{mL}$ buffer solution is $0.100\\,\\text{M}$ in $\\text{HF}$ ($\\text{p}K_a = 3.17$) and $0.100\\,\\text{M}$ in $\\text{NaF}$. Which of the following additions will completely exceed the buffer capacity of this solution?",
        "options": [
            "Adding $5.0\\,\\text{mL}$ of $1.00\\,\\text{M}\\,\\text{HCl}(aq)$",
            "Adding $8.0\\,\\text{mL}$ of $1.00\\,\\text{M}\\,\\text{NaOH}(aq)$",
            "Adding $12.0\\,\\text{mL}$ of $1.00\\,\\text{M}\\,\\text{HNO}_3(aq)$",
            "Adding $100.0\\,\\text{mL}$ of pure distilled water"
        ],
        "correct_index": 2,
        "explanation": "The $100.0\\,\\text{mL}$ buffer contains $(0.1000\\,\\text{L})(0.100\\,\\text{M}) = 0.0100\\,\\text{mol}$ ($10.0\\,\\text{mmol}$) of $\\text{HF}$ and $10.0\\,\\text{mmol}$ of $\\text{F}^-$. Therefore, its maximum capacity before one buffer component is completely consumed is $10.0\\,\\text{mmol}$ of strong acid or $10.0\\,\\text{mmol}$ of strong base. Adding $12.0\\,\\text{mL}$ of $1.00\\,\\text{M}\\,\\text{HNO}_3$ introduces $12.0\\,\\text{mmol}$ of $\\text{H}_3\\text{O}^+$, which consumes all $10.0\\,\\text{mmol}$ of $\\text{F}^-$ and leaves $2.0\\,\\text{mmol}$ of excess strong acid, completely exceeding the buffer capacity."
    },
    {
        "unit_q_num": 50,
        "topic_code": "8.10",
        "topic_title": "Buffer Capacity",
        "difficulty": "Challenging",
        "stimulus": """<table class="quiz-data-table">
<thead>
<tr><th>Beaker</th><th>Volume of $0.40\\,\\text{M}\\,\\text{NH}_3$</th><th>Volume of $0.40\\,\\text{M}\\,\\text{HCl}$</th></tr>
</thead>
<tbody>
<tr><td>Beaker $\\text{A}$</td><td>$50.0\\,\\text{mL}$</td><td>$25.0\\,\\text{mL}$</td></tr>
<tr><td>Beaker $\\text{B}$</td><td>$100.0\\,\\text{mL}$</td><td>$50.0\\,\\text{mL}$</td></tr>
</tbody>
</table>""",
        "question": "Two buffer solutions are prepared by mixing $0.40\\,\\text{M}\\,\\text{NH}_3(aq)$ and $0.40\\,\\text{M}\\,\\text{HCl}(aq)$ in the volumes shown in the table above. If $5.0\\,\\text{mL}$ of $1.0\\,\\text{M}\\,\\text{HCl}(aq)$ is subsequently added to Beaker $\\text{A}$ and $5.0\\,\\text{mL}$ of $1.0\\,\\text{M}\\,\\text{HCl}(aq)$ is added to Beaker $\\text{B}$, how do the initial $\\text{pH}$ (before the $5.0\\,\\text{mL}$ addition) and the final $\\text{pH}$ (after the $5.0\\,\\text{mL}$ addition) compare between Beaker $\\text{A}$ and Beaker $\\text{B}$?",
        "options": [
            "Both beakers have the same initial $\\text{pH}$, and Beaker $\\text{B}$ has a higher final $\\text{pH}$ than Beaker $\\text{A}$ because Beaker $\\text{B}$ contains twice as many moles of $\\text{NH}_3$ and $\\text{NH}_4^+$.",
            "Both beakers have the same initial $\\text{pH}$ and the same final $\\text{pH}$ because the molar concentrations of $\\text{NH}_3$ and $\\text{NH}_4^+$ are identical in both beakers.",
            "Beaker $\\text{B}$ has a higher initial $\\text{pH}$ than Beaker $\\text{A}$, and both have the same final $\\text{pH}$.",
            "Both beakers have the same initial $\\text{pH}$, and Beaker $\\text{A}$ has a higher final $\\text{pH}$ than Beaker $\\text{B}$."
        ],
        "correct_index": 0,
        "explanation": r"Before the $5.0\,\text{mL}$ of $1.0\,\text{M}\,\text{HCl}$ is added, Beaker $\text{A}$ contains $10.\,\text{mmol}$ each of $\text{NH}_3$ and $\text{NH}_4^+$, and Beaker $\text{B}$ contains $20.\,\text{mmol}$ of each. Because $\text{NH}_3$ and $\text{NH}_4^+$ are present in equal amounts in both beakers, the initial pH values are identical ($\text{pH} = \text{p}K_a$ of $\text{NH}_4^+$). The added $5.0\,\text{mmol}$ of $\text{H}_3\text{O}^+$ converts $5.0\,\text{mmol}$ of $\text{NH}_3$ into $\text{NH}_4^+$ in each beaker. In Beaker $\text{A}$ this uses up half of the $\text{NH}_3$ ($5.0\,\text{mmol}$ $\text{NH}_3$ and $15.0\,\text{mmol}$ $\text{NH}_4^+$ remain), whereas in Beaker $\text{B}$ it uses up only one-fourth ($15.0\,\text{mmol}$ $\text{NH}_3$ and $25.0\,\text{mmol}$ $\text{NH}_4^+$ remain). The ratio $[\text{NH}_3]/[\text{NH}_4^+]$ falls further below $1$ in Beaker $\text{A}$, so its pH drops more. Although the two beakers have identical concentrations, Beaker $\text{B}$ contains twice as many moles of buffer components, so it has the greater buffer capacity and the higher final pH.",
    },

    # -------------------------------------------------------------------------
    # Topic 8.11: pH and Solubility (Q51–Q54)
    # Moved from former Unit 7 topic 7.13 (re-aligned with the Fall 2024 CED).
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 51,
        "topic_code": "8.11",
        "topic_title": "pH and Solubility",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Salt</th><th>Dissolution Equilibrium</th><th>Conjugate Acid of Anion</th></tr></thead>"
            "<tbody>"
            "<tr><td>$\\text{AgBr}(s)$</td><td>$\\text{AgBr}(s) \\rightleftharpoons \\text{Ag}^+(aq) + \\text{Br}^-(aq)$</td><td>$\\text{HBr}$ (strong acid)</td></tr>"
            "<tr><td>$\\text{BaSO}_4(s)$</td><td>$\\text{BaSO}_4(s) \\rightleftharpoons \\text{Ba}^{2+}(aq) + \\text{SO}_4^{2-}(aq)$</td><td>$\\text{HSO}_4^-$ ($K_a = 1.2 \\times 10^{-2}$)</td></tr>"
            "<tr><td>$\\text{CaCO}_3(s)$</td><td>$\\text{CaCO}_3(s) \\rightleftharpoons \\text{Ca}^{2+}(aq) + \\text{CO}_3^{2-}(aq)$</td><td>$\\text{HCO}_3^-$ ($K_a = 4.7 \\times 10^{-11}$)</td></tr>"
            "<tr><td>$\\text{PbCl}_2(s)$</td><td>$\\text{PbCl}_2(s) \\rightleftharpoons \\text{Pb}^{2+}(aq) + 2\\,\\text{Cl}^-(aq)$</td><td>$\\text{HCl}$ (strong acid)</td></tr>"
            "</tbody></table>"
        ),
        "question": (
            "Based on the data in the table above, which of the four sparingly soluble salts will exhibit the GREATEST "
            "increase in molar solubility when strong acid ($\\text{HNO}_3$) is added to lower the pH of the solution?"
        ),
        "options": [
            "$\\text{AgBr}(s)$",
            "$\\text{BaSO}_4(s)$",
            "$\\text{CaCO}_3(s)$",
            "$\\text{PbCl}_2(s)$",
        ],
        "correct_index": 2,
        "explanation": (
            "The carbonate ion $\\text{CO}_3^{2-}$ is a relatively strong weak base (conjugate base of the very weak acid "
            "$\\text{HCO}_3^-$, $K_a = 4.7 \\times 10^{-11}$). Adding $\\text{H}^+$ reacts extensively with $\\text{CO}_3^{2-}(aq)$ "
            "to form $\\text{HCO}_3^-(aq)$ and $\\text{H}_2\\text{CO}_3(aq) / \\text{CO}_2(g)$, drastically decreasing $[\\text{CO}_3^{2-}]$ "
            "so $Q_{\\text{sp}} < K_{\\text{sp}}$ and shifting the dissolution equilibrium of $\\text{CaCO}_3(s)$ strongly to the right."
        ),
    },
    {
        "unit_q_num": 52,
        "topic_code": "8.11",
        "topic_title": "pH and Solubility",
        "difficulty": "AP Exam Level",
        "stimulus": r'<div class="quiz-equation">$\text{Mg(OH)}_2(s) \rightleftharpoons \text{Mg}^{2+}(aq) + 2\,\text{OH}^-(aq)$</div>',
        "question": r"Excess solid $\text{Mg(OH)}_2$ is added to each of three buffer solutions at $25^\circ\text{C}$: Solution X ($\text{pH} = 10.0$), Solution Y ($\text{pH} = 11.0$), and Solution Z ($\text{pH} = 12.0$). After equilibrium is established, which of the following correctly ranks the molar solubility of $\text{Mg(OH)}_2$ in the three solutions and gives the correct reason?",
        "options": [
            r"$\text{X} < \text{Y} < \text{Z}$, because a solution with a higher $\text{pH}$ contains more $\text{OH}^-$ available to dissolve the solid.",
            r"$\text{Z} < \text{Y} < \text{X}$, because a lower $[\text{OH}^-]$ makes $Q_{\text{sp}} < K_{\text{sp}}$, so more solid dissolves before equilibrium is reached.",
            r"$\text{X} = \text{Y} = \text{Z}$, because $K_{\text{sp}}$ of $\text{Mg(OH)}_2$ has the same value in all three solutions at $25^\circ\text{C}$.",
            r"$\text{Z} < \text{Y} < \text{X}$, because the value of $K_{\text{sp}}$ of $\text{Mg(OH)}_2$ is largest in the solution with the lowest $\text{pH}$.",
        ],
        "correct_index": 1,
        "explanation": r"For $\text{Mg(OH)}_2(s) \rightleftharpoons \text{Mg}^{2+}(aq) + 2\,\text{OH}^-(aq)$, $K_{\text{sp}} = [\text{Mg}^{2+}][\text{OH}^-]^2$ depends only on temperature, so it has the same value in all three solutions. A lower $\text{pH}$ means the buffer holds $[\text{OH}^-]$ at a lower value, so $Q_{\text{sp}} < K_{\text{sp}}$ until more solid dissolves and $[\text{Mg}^{2+}]$ becomes larger (Le Châtelier's principle). The molar solubility is therefore greatest in Solution X ($\text{pH} = 10.0$) and smallest in Solution Z ($\text{pH} = 12.0$). Because $\text{OH}^-$ is a product of the dissolution, a higher $[\text{OH}^-]$ suppresses solubility (common-ion effect) rather than increasing it. A constant $K_{\text{sp}}$ does not mean a constant solubility when the concentration of one ion is held at different values.",
    },
    {
        "unit_q_num": 53,
        "topic_code": "8.11",
        "topic_title": "pH and Solubility",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="quiz-equation">'
            "$\\text{Ca}_3(\\text{PO}_4)_2(s) \\rightleftharpoons 3\\,\\text{Ca}^{2+}(aq) + 2\\,\\text{PO}_4^{3-}(aq)$"
            "</div>"
        ),
        "question": r"Tooth enamel is composed mainly of hydroxyapatite, a calcium phosphate mineral; for simplicity, model the enamel as $\text{Ca}_3(\text{PO}_4)_2(s)$, which dissolves as shown above. Oral bacteria metabolize sugars to produce lactic acid, lowering the pH of saliva in contact with teeth. Which of the following best explains why acidic foods and bacterial lactic acid promote tooth decay?",
        "options": [
            "$\\text{Ca}^{2+}(aq) + 2\\,\\text{OH}^-(aq) \\rightarrow \\text{Ca(OH)}_2(s)$, which precipitates on tooth surfaces.",
            "Lowering the pH increases the value of $K_{\\text{sp}}$ for $\\text{Ca}_3(\\text{PO}_4)_2$, so more of the solid dissolves.",
            "Lowering the pH increases $[\\text{PO}_4^{3-}]$ by the common-ion effect, causing $Q_{\\text{sp}} > K_{\\text{sp}}$.",
            "$\\text{H}^+(aq) + \\text{PO}_4^{3-}(aq) \\rightleftharpoons \\text{HPO}_4^{2-}(aq)$, which lowers $[\\text{PO}_4^{3-}]$ so $Q_{\\text{sp}} < K_{\\text{sp}}$ and causes $\\text{Ca}_3(\\text{PO}_4)_2(s)$ to dissolve.",
        ],
        "correct_index": 3,
        "explanation": r"The phosphate ion $\text{PO}_4^{3-}$ is the conjugate base of a weak acid ($\text{HPO}_4^{2-}$). When $\text{H}^+(aq)$ is added, it protonates $\text{PO}_4^{3-}(aq)$ to form $\text{HPO}_4^{2-}(aq)$ (and $\text{H}_2\text{PO}_4^-$), decreasing $[\text{PO}_4^{3-}]$. This makes $Q_{\text{sp}} < K_{\text{sp}}$ and drives further dissolution of the enamel (Le Châtelier's principle). The value of $K_{\text{sp}}$ depends only on temperature, and lowering the pH decreases, rather than increases, $[\text{PO}_4^{3-}]$.",
    },
    {
        "unit_q_num": 54,
        "topic_code": "8.11",
        "topic_title": "pH and Solubility",
        "difficulty": "Challenging",
        "stimulus": r'<table class="quiz-data-table"><thead><tr><th>Test Tube</th><th>Solid in Contact with Its Saturated Solution</th><th>Anion of the Salt</th></tr></thead><tbody><tr><td>$1$</td><td>$\text{CaCO}_3(s)$</td><td>$\text{CO}_3^{2-}$</td></tr><tr><td>$2$</td><td>$\text{Mg(OH)}_2(s)$</td><td>$\text{OH}^-$</td></tr><tr><td>$3$</td><td>$\text{AgCl}(s)$</td><td>$\text{Cl}^-$</td></tr></tbody></table>',
        "question": r"A student prepares the three test tubes described in the table above. Each contains a saturated solution in contact with excess undissolved solid at $25^\circ\text{C}$. The student then adds $1.0\,\text{M}\,\text{HNO}_3(aq)$ dropwise to each tube while stirring. Which of the following best predicts and explains the observations?",
        "options": [
            r"Only the $\text{CaCO}_3$ dissolves, because carbonate is the only anion that can be converted into a gas.",
            r"All three solids dissolve, because adding a strong acid increases the solubility of every sparingly soluble salt.",
            r"The $\text{CaCO}_3$ and the $\text{Mg(OH)}_2$ dissolve, but the amount of $\text{AgCl}$ does not change noticeably, because $\text{CO}_3^{2-}$ and $\text{OH}^-$ react with $\text{H}_3\text{O}^+$, whereas $\text{Cl}^-$ has negligible basicity.",
            r"None of the solids dissolve, because adding an acid does not change the value of $K_{\text{sp}}$ for any of the salts.",
        ],
        "correct_index": 2,
        "explanation": r"Adding $\text{H}_3\text{O}^+$ changes the solubility of a salt only if one of its ions is basic. $\text{CO}_3^{2-}$ is protonated to $\text{HCO}_3^-$ and then $\text{H}_2\text{CO}_3$ (which releases $\text{CO}_2$ gas), and $\text{OH}^-$ is neutralized to $\text{H}_2\text{O}$. Each reaction lowers the concentration of the anion, so $Q_{\text{sp}} < K_{\text{sp}}$ and more $\text{CaCO}_3$ and $\text{Mg(OH)}_2$ dissolve (Le Châtelier's principle). $\text{Cl}^-$ is the conjugate base of the strong acid $\text{HCl}$, so it does not react with $\text{H}_3\text{O}^+$, and the solubility of $\text{AgCl}$ is essentially unchanged. The $K_{\text{sp}}$ values stay the same, but the ion concentrations do not; hydroxide is removed by acid just as carbonate is.",
    },

    # -------------------------------------------------------------------------
    # Added 2026-10-03 — Blind-spot coverage (Fall 2024 CED): topics 8.2–8.11
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 55,
        "topic_code": "8.2",
        "topic_title": "pH and pOH of Strong Acids and Bases",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"Excess magnesium ribbon is added to each of two flasks at $25^\circ\text{C}$. One flask contains $50.0\,\text{mL}$ of $0.10\,\text{M}\,\text{HCl}(aq)$, and the other contains $50.0\,\text{mL}$ of $0.10\,\text{M}\,\text{CH}_3\text{COOH}(aq)$ ($K_a = 1.8 \times 10^{-5}$). In both flasks the acid reacts as represented by $\text{Mg}(s) + 2\,\text{H}_3\text{O}^+(aq) \rightarrow \text{Mg}^{2+}(aq) + \text{H}_2(g) + 2\,\text{H}_2\text{O}(l)$. Which of the following best describes the results?",
        "options": [
            r"$\text{H}_2(g)$ is produced at the same initial rate in both flasks, because both solutions contain $0.0050\,\text{mol}$ of acid.",
            r"$\text{H}_2(g)$ is produced faster in the $\text{HCl}$ flask, and the $\text{HCl}$ flask produces about $75$ times as much $\text{H}_2(g)$, because only about $1.3\%$ of the $\text{CH}_3\text{COOH}$ molecules are ionized.",
            r"$\text{H}_2(g)$ is produced faster in the $\text{HCl}$ flask, but both flasks eventually produce the same amount of $\text{H}_2(g)$, because $\text{CH}_3\text{COOH}$ continues to ionize as $\text{H}_3\text{O}^+$ is consumed.",
            r"$\text{H}_2(g)$ is produced faster in the $\text{CH}_3\text{COOH}$ flask, because each $\text{CH}_3\text{COOH}$ molecule contains four hydrogen atoms.",
        ],
        "correct_index": 2,
        "explanation": r"$\text{HCl}$ is a strong acid, so $[\text{H}_3\text{O}^+] = 0.10\,\text{M}$. $\text{CH}_3\text{COOH}$ is a weak acid, so $[\text{H}_3\text{O}^+] \approx \sqrt{K_aC} = \sqrt{(1.8 \times 10^{-5})(0.10)} = 1.3 \times 10^{-3}\,\text{M}$ (about $1.3\%$ ionized). The much higher $[\text{H}_3\text{O}^+]$ makes the reaction with $\text{Mg}$ faster in the $\text{HCl}$ flask. However, both flasks contain $0.0050\,\text{mol}$ of acid. As $\text{Mg}$ consumes $\text{H}_3\text{O}^+$ in the acetic acid flask, the equilibrium $\text{CH}_3\text{COOH} + \text{H}_2\text{O} \rightleftharpoons \text{H}_3\text{O}^+ + \text{CH}_3\text{COO}^-$ shifts to the right (Le Châtelier), so eventually all of the acid reacts and each flask produces $0.0025\,\text{mol}$ of $\text{H}_2$. The amount of $\text{H}_2$ depends on the total moles of acid, not on the initial fraction ionized; equal acid concentrations do not mean equal $[\text{H}_3\text{O}^+]$; and only the one $\text{O}-\text{H}$ hydrogen of acetic acid is acidic.",
    },
    {
        "unit_q_num": 56,
        "topic_code": "8.3",
        "topic_title": "Weak Acid and Base Equilibria",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 260" role="img" aria-label="Particulate diagram of a portion of an aqueous solution of the acid HA at equilibrium: 8 un-ionized HA molecules, 2 A minus ions, and 2 hydronium ions. Water molecules are not shown." font-family="sans-serif">
<rect x="20" y="20" width="330" height="220" rx="10" fill="#ffffff" stroke="#374151" stroke-width="2"/>
<circle cx="62" cy="60" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="72" cy="51" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="140" cy="68" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="140" y="73" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<circle cx="222" cy="58" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="232" cy="49" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="300" cy="66" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="310" cy="57" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="78" cy="132" r="10" fill="#374151" stroke="#111827" stroke-width="1.5"/><text x="78" y="137" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">+</text>
<circle cx="158" cy="126" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="168" cy="117" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="238" cy="136" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="248" cy="127" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="312" cy="128" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="312" y="133" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<circle cx="60" cy="196" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="70" cy="187" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="138" cy="204" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="148" cy="195" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="220" cy="194" r="10" fill="#374151" stroke="#111827" stroke-width="1.5"/><text x="220" y="199" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">+</text>
<circle cx="298" cy="202" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="308" cy="193" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<text x="384" y="52" font-size="13" font-weight="bold" fill="#111827">Key</text>
<circle cx="398" cy="92" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="408" cy="83" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<text x="428" y="97" font-size="14" fill="#111827">HA</text>
<circle cx="398" cy="142" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="398" y="147" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<text x="428" y="147" font-size="14" fill="#111827">A⁻</text>
<circle cx="398" cy="192" r="10" fill="#374151" stroke="#111827" stroke-width="1.5"/><text x="398" y="197" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">+</text>
<text x="428" y="197" font-size="14" fill="#111827">H₃O⁺</text>
</svg>
<figcaption>Water molecules are not shown.</figcaption>
</figure>""",
        "question": r"The particulate diagram above represents a small portion of an aqueous solution of a monoprotic acid, $\text{HA}$, at equilibrium. Which of the following is best supported by the diagram?",
        "options": [
            r"$\text{HA}$ is a weak acid, and its percent ionization is $20\%$.",
            r"$\text{HA}$ is a weak acid, and its percent ionization is $25\%$.",
            r"$\text{HA}$ is a weak acid, and its percent ionization is $40\%$.",
            r"$\text{HA}$ is a strong acid, because $\text{H}_3\text{O}^+$ ions are present in the solution.",
        ],
        "correct_index": 0,
        "explanation": r"Percent ionization compares the acid that has ionized with the total acid originally present. The diagram shows $8$ un-ionized $\text{HA}$ molecules and $2$ $\text{A}^-$ ions (each formed together with one $\text{H}_3\text{O}^+$ ion), so $10$ acid molecules were originally present: percent ionization $= \frac{2}{8 + 2} \times 100\% = 20\%$. Because most of the $\text{HA}$ remains un-ionized, $\text{HA}$ is a weak acid; a strong acid would show only $\text{H}_3\text{O}^+$ and $\text{A}^-$, so the mere presence of $\text{H}_3\text{O}^+$ does not indicate a strong acid. Dividing by only the $8$ remaining $\text{HA}$ molecules ($25\%$) or counting both ions as ionized acid ($40\%$) are common errors.",
    },
    {
        "unit_q_num": 57,
        "topic_code": "8.3",
        "topic_title": "Weak Acid and Base Equilibria",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A student uses a calibrated pH meter to measure the $\text{pH}$ of a $0.050\,\text{M}$ aqueous solution of a weak base, $\text{B}$, at $25^\circ\text{C}$ and obtains $\text{pH} = 10.50$. Which of the following is closest to the value of $K_b$ for $\text{B}$?",
        "options": [
            r"$2.0 \times 10^{-20}$",
            r"$5.0 \times 10^{-9}$",
            r"$2.0 \times 10^{-6}$",
            r"$6.3 \times 10^{-3}$",
        ],
        "correct_index": 2,
        "explanation": r"For $\text{B}(aq) + \text{H}_2\text{O}(l) \rightleftharpoons \text{HB}^+(aq) + \text{OH}^-(aq)$, first convert the measured $\text{pH}$ to $[\text{OH}^-]$: $\text{pOH} = 14.00 - 10.50 = 3.50$, so $[\text{OH}^-] = [\text{HB}^+] = 10^{-3.50} = 3.16 \times 10^{-4}\,\text{M}$. Then $K_b = \frac{[\text{HB}^+][\text{OH}^-]}{[\text{B}]} = \frac{(3.16 \times 10^{-4})^2}{0.050 - 0.0003} \approx \frac{1.0 \times 10^{-7}}{0.050} = 2.0 \times 10^{-6}$. Using $[\text{H}_3\text{O}^+] = 10^{-10.50}\,\text{M}$ in place of $[\text{OH}^-]$ gives $2.0 \times 10^{-20}$; $5.0 \times 10^{-9}$ is $K_a$ of the conjugate acid $\text{HB}^+$ ($K_w/K_b$); and $6.3 \times 10^{-3}$ is the fraction of $\text{B}$ that is ionized ($[\text{OH}^-]/[\text{B}]_0$), not $K_b$.",
    },
    {
        "unit_q_num": 58,
        "topic_code": "8.4",
        "topic_title": "Acid-Base Reactions and Buffers",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Acid</th><th>$K_a$ at $25^\circ\text{C}$</th></tr></thead><tbody><tr><td>Nitrous acid, $\text{HNO}_2$</td><td>$4.5 \times 10^{-4}$</td></tr><tr><td>Acetic acid, $\text{CH}_3\text{COOH}$</td><td>$1.8 \times 10^{-5}$</td></tr></tbody></table>""",
        "question": r"Equal volumes of $0.10\,\text{M}\,\text{HNO}_2(aq)$ and $0.10\,\text{M}\,\text{NaCH}_3\text{COO}(aq)$ are mixed at $25^\circ\text{C}$, and the reaction represented below reaches equilibrium. $$\text{HNO}_2(aq) + \text{CH}_3\text{COO}^-(aq) \rightleftharpoons \text{NO}_2^-(aq) + \text{CH}_3\text{COOH}(aq)$$ Based on the data in the table above, what is the value of the equilibrium constant, $K$, for this reaction, and which side of the reaction is favored at equilibrium?",
        "options": [
            r"$K = 4.5 \times 10^{10}$; products are favored.",
            r"$K = 25$; products are favored.",
            r"$K = 0.040$; reactants are favored.",
            r"$K = 8.1 \times 10^{-9}$; reactants are favored.",
        ],
        "correct_index": 1,
        "explanation": r"The reaction is the sum of $\text{HNO}_2 + \text{H}_2\text{O} \rightleftharpoons \text{H}_3\text{O}^+ + \text{NO}_2^-$ ($K_a = 4.5 \times 10^{-4}$) and $\text{H}_3\text{O}^+ + \text{CH}_3\text{COO}^- \rightleftharpoons \text{CH}_3\text{COOH} + \text{H}_2\text{O}$ ($K = 1/K_a$ of acetic acid). Adding reactions multiplies their constants: $K = \frac{4.5 \times 10^{-4}}{1.8 \times 10^{-5}} = 25$. Because $K > 1$, products are favored: the proton moves from the stronger acid ($\text{HNO}_2$) to the stronger base ($\text{CH}_3\text{COO}^-$), forming the weaker acid and the weaker base. Inverting the ratio gives $0.040$, multiplying the two $K_a$ values gives $8.1 \times 10^{-9}$, and $4.5 \times 10^{10}$ ($K_a/K_w$) is the constant for the reaction of $\text{HNO}_2$ with the strong base $\text{OH}^-$, not with acetate.",
    },
    {
        "unit_q_num": 59,
        "topic_code": "8.4",
        "topic_title": "Acid-Base Reactions and Buffers",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Solution</th><th>Solutions mixed at $25^\circ\text{C}$</th></tr></thead><tbody><tr><td>1</td><td>$30.0\,\text{mL}$ of $0.100\,\text{M}\,\text{HCl}$ and $20.0\,\text{mL}$ of $0.100\,\text{M}\,\text{NaOH}$</td></tr><tr><td>2</td><td>$30.0\,\text{mL}$ of $0.100\,\text{M}\,\text{HCl}$ and $20.0\,\text{mL}$ of $0.100\,\text{M}\,\text{NH}_3$ ($K_b = 1.8 \times 10^{-5}$)</td></tr></tbody></table>""",
        "question": r"Two solutions are prepared as described in the table above. Which of the following correctly compares the $\text{pH}$ values of Solution 1 and Solution 2? ($\log 2.0 = 0.30$)",
        "options": [
            r"Both solutions have $\text{pH} \approx 1.70$, because in each solution the $\text{pH}$ is determined by the $1.00\,\text{mmol}$ of $\text{H}_3\text{O}^+$ that remains after all of the base has reacted.",
            r"Solution 1 has $\text{pH} \approx 1.70$, but Solution 2 has $\text{pH} \approx 5.3$, because the $\text{pH}$ of Solution 2 is determined by the reaction of $\text{NH}_4^+$ with water.",
            r"Solution 2 has a lower $\text{pH}$ than Solution 1, because $\text{NH}_4^+$ is a weak acid that adds a significant amount of $\text{H}_3\text{O}^+$ to the excess $\text{HCl}$.",
            r"Solution 2 has a higher $\text{pH}$ than Solution 1, because $\text{NH}_3$ and $\text{NH}_4^+$ form a buffer that resists the decrease in $\text{pH}$.",
        ],
        "correct_index": 0,
        "explanation": r"Each solution contains $(0.0300\,\text{L})(0.100\,\text{M}) = 3.00\,\text{mmol}$ of $\text{H}_3\text{O}^+$ and $2.00\,\text{mmol}$ of base. Both $\text{OH}^-$ and $\text{NH}_3$ react essentially completely with a strong acid ($\text{NH}_3 + \text{H}_3\text{O}^+ \rightarrow \text{NH}_4^+ + \text{H}_2\text{O}$), leaving $1.00\,\text{mmol}$ of excess $\text{H}_3\text{O}^+$ in $50.0\,\text{mL}$: $[\text{H}_3\text{O}^+] = 0.0200\,\text{M}$ and $\text{pH} = 2.00 - 0.30 = 1.70$. In Solution 2, $\text{NH}_4^+$ ($K_a = K_w/K_b = 5.6 \times 10^{-10}$) is far too weak an acid to add a significant amount of $\text{H}_3\text{O}^+$ to $0.0200\,\text{M}$, so both solutions have $\text{pH} \approx 1.70$. No $\text{NH}_3$ remains, so there is no buffer, and the reaction of $\text{NH}_4^+$ with water controls the $\text{pH}$ only when no strong acid is in excess (as at the equivalence point).",
    },
    {
        "unit_q_num": 60,
        "topic_code": "8.5",
        "topic_title": "Acid-Base Titrations",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 320" role="img" aria-label="Titration curve of pH versus volume of 0.100 M NaOH added, from 0 to 35 mL. The pH starts near 2.6, rises gradually through a buffer region and passes pH 4.0 at 10.0 mL, rises steeply at 20.0 mL where the pH is about 8.3, and levels off near pH 12.4." font-family="sans-serif">
<line x1="62" y1="262.0" x2="496" y2="262.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="244.6" x2="496" y2="244.6" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="227.1" x2="496" y2="227.1" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="209.7" x2="496" y2="209.7" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="192.3" x2="496" y2="192.3" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="174.9" x2="496" y2="174.9" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="157.4" x2="496" y2="157.4" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="140.0" x2="496" y2="140.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="122.6" x2="496" y2="122.6" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="105.1" x2="496" y2="105.1" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="87.7" x2="496" y2="87.7" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="70.3" x2="496" y2="70.3" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="52.9" x2="496" y2="52.9" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="35.4" x2="496" y2="35.4" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="18.0" x2="496" y2="18.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62.0" y1="18" x2="62.0" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="124.0" y1="18" x2="124.0" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="186.0" y1="18" x2="186.0" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="248.0" y1="18" x2="248.0" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="310.0" y1="18" x2="310.0" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="372.0" y1="18" x2="372.0" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="434.0" y1="18" x2="434.0" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="496.0" y1="18" x2="496.0" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="262" x2="496" y2="262" stroke="#374151" stroke-width="1.8"/>
<line x1="62" y1="18" x2="62" y2="262" stroke="#374151" stroke-width="1.8"/>
<line x1="57" y1="262.0" x2="62" y2="262.0" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="266.0" text-anchor="end" font-size="12" fill="#374151">0</text>
<line x1="57" y1="227.1" x2="62" y2="227.1" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="231.1" text-anchor="end" font-size="12" fill="#374151">2</text>
<line x1="57" y1="192.3" x2="62" y2="192.3" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="196.3" text-anchor="end" font-size="12" fill="#374151">4</text>
<line x1="57" y1="157.4" x2="62" y2="157.4" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="161.4" text-anchor="end" font-size="12" fill="#374151">6</text>
<line x1="57" y1="122.6" x2="62" y2="122.6" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="126.6" text-anchor="end" font-size="12" fill="#374151">8</text>
<line x1="57" y1="87.7" x2="62" y2="87.7" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="91.7" text-anchor="end" font-size="12" fill="#374151">10</text>
<line x1="57" y1="52.9" x2="62" y2="52.9" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="56.9" text-anchor="end" font-size="12" fill="#374151">12</text>
<line x1="57" y1="18.0" x2="62" y2="18.0" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="22.0" text-anchor="end" font-size="12" fill="#374151">14</text>
<line x1="62.0" y1="262" x2="62.0" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="62.0" y="281" text-anchor="middle" font-size="12" fill="#374151">0</text>
<line x1="124.0" y1="262" x2="124.0" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="124.0" y="281" text-anchor="middle" font-size="12" fill="#374151">5</text>
<line x1="186.0" y1="262" x2="186.0" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="186.0" y="281" text-anchor="middle" font-size="12" fill="#374151">10</text>
<line x1="248.0" y1="262" x2="248.0" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="248.0" y="281" text-anchor="middle" font-size="12" fill="#374151">15</text>
<line x1="310.0" y1="262" x2="310.0" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="310.0" y="281" text-anchor="middle" font-size="12" fill="#374151">20</text>
<line x1="372.0" y1="262" x2="372.0" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="372.0" y="281" text-anchor="middle" font-size="12" fill="#374151">25</text>
<line x1="434.0" y1="262" x2="434.0" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="434.0" y="281" text-anchor="middle" font-size="12" fill="#374151">30</text>
<line x1="496.0" y1="262" x2="496.0" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="496.0" y="281" text-anchor="middle" font-size="12" fill="#374151">35</text>
<text x="279" y="306" text-anchor="middle" font-size="13" fill="#111827">Volume of 0.100 M NaOH added (mL)</text>
<text x="20" y="140" text-anchor="middle" font-size="13" fill="#111827" transform="rotate(-90 20 140)">pH</text>
<polyline points="62.0,217.5 72.5,212.8 81.8,209.5 92.4,206.6 104.8,203.8 138.9,198.2 221.3,187.8 253.0,183.1 267.8,180.3 279.6,177.4 288.9,174.3 296.4,170.7 301.3,167.2 304.8,163.2 307.2,158.5 308.7,152.5 309.8,138.3 310.3,91.3 311.0,83.2 312.2,77.3 314.3,72.3 317.4,68.2 322.4,64.4 328.6,61.4 337.9,58.5 349.7,56.0 364.6,53.7 382.5,51.8 430.3,48.5 496.0,45.9" fill="none" stroke="#111827" stroke-width="2.2" stroke-linejoin="round"/>
</svg>
<figcaption>Titration of 25.0 mL of HA(aq) with 0.100 M NaOH(aq) at 25 °C</figcaption>
</figure>""",
        "question": r"A $25.0\,\text{mL}$ sample of a weak monoprotic acid, $\text{HA}(aq)$, is titrated with $0.100\,\text{M}\,\text{NaOH}(aq)$, producing the titration curve shown above. Based on the curve, which of the following is closest to the value of $K_a$ for $\text{HA}$?",
        "options": [
            r"$3 \times 10^{-3}$",
            r"$1 \times 10^{-4}$",
            r"$5 \times 10^{-9}$",
            r"$1 \times 10^{-10}$",
        ],
        "correct_index": 1,
        "explanation": r"The steep rise shows that the equivalence point is at $20.0\,\text{mL}$ of $\text{NaOH}$, so the half-equivalence point is at $10.0\,\text{mL}$. There, half of the $\text{HA}$ has been converted to $\text{A}^-$, so $[\text{HA}] = [\text{A}^-]$ and $\text{pH} = \text{p}K_a$. The curve shows $\text{pH} = 4.0$ at $10.0\,\text{mL}$, so $K_a = 10^{-4.0} = 1 \times 10^{-4}$. Using the initial $\text{pH}$ ($2.6$) gives $3 \times 10^{-3}$, which is $[\text{H}_3\text{O}^+]$ of the original acid solution, not $K_a$; using the equivalence-point $\text{pH}$ ($8.3$) gives $5 \times 10^{-9}$; and $1 \times 10^{-10}$ is $K_b$ of $\text{A}^-$ ($K_w/K_a$).",
    },
    {
        "unit_q_num": 61,
        "topic_code": "8.5",
        "topic_title": "Acid-Base Titrations",
        "difficulty": "Challenging",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 320" role="img" aria-label="Titration curve of pH versus volume of 0.100 M HCl added, from 0 to 40 mL. The pH starts at 11.0, decreases gradually and passes pH 9.0 at 12.5 mL, drops steeply at 25.0 mL where the pH is about 5.2, and levels off near pH 1.6." font-family="sans-serif">
<line x1="62" y1="262.0" x2="496" y2="262.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="244.6" x2="496" y2="244.6" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="227.1" x2="496" y2="227.1" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="209.7" x2="496" y2="209.7" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="192.3" x2="496" y2="192.3" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="174.9" x2="496" y2="174.9" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="157.4" x2="496" y2="157.4" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="140.0" x2="496" y2="140.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="122.6" x2="496" y2="122.6" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="105.1" x2="496" y2="105.1" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="87.7" x2="496" y2="87.7" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="70.3" x2="496" y2="70.3" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="52.9" x2="496" y2="52.9" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="35.4" x2="496" y2="35.4" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="18.0" x2="496" y2="18.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62.0" y1="18" x2="62.0" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="116.2" y1="18" x2="116.2" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="170.5" y1="18" x2="170.5" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="224.8" y1="18" x2="224.8" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="279.0" y1="18" x2="279.0" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="333.2" y1="18" x2="333.2" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="387.5" y1="18" x2="387.5" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="441.8" y1="18" x2="441.8" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="496.0" y1="18" x2="496.0" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="262" x2="496" y2="262" stroke="#374151" stroke-width="1.8"/>
<line x1="62" y1="18" x2="62" y2="262" stroke="#374151" stroke-width="1.8"/>
<line x1="57" y1="262.0" x2="62" y2="262.0" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="266.0" text-anchor="end" font-size="12" fill="#374151">0</text>
<line x1="57" y1="227.1" x2="62" y2="227.1" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="231.1" text-anchor="end" font-size="12" fill="#374151">2</text>
<line x1="57" y1="192.3" x2="62" y2="192.3" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="196.3" text-anchor="end" font-size="12" fill="#374151">4</text>
<line x1="57" y1="157.4" x2="62" y2="157.4" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="161.4" text-anchor="end" font-size="12" fill="#374151">6</text>
<line x1="57" y1="122.6" x2="62" y2="122.6" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="126.6" text-anchor="end" font-size="12" fill="#374151">8</text>
<line x1="57" y1="87.7" x2="62" y2="87.7" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="91.7" text-anchor="end" font-size="12" fill="#374151">10</text>
<line x1="57" y1="52.9" x2="62" y2="52.9" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="56.9" text-anchor="end" font-size="12" fill="#374151">12</text>
<line x1="57" y1="18.0" x2="62" y2="18.0" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="22.0" text-anchor="end" font-size="12" fill="#374151">14</text>
<line x1="62.0" y1="262" x2="62.0" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="62.0" y="281" text-anchor="middle" font-size="12" fill="#374151">0</text>
<line x1="116.2" y1="262" x2="116.2" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="116.2" y="281" text-anchor="middle" font-size="12" fill="#374151">5</text>
<line x1="170.5" y1="262" x2="170.5" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="170.5" y="281" text-anchor="middle" font-size="12" fill="#374151">10</text>
<line x1="224.8" y1="262" x2="224.8" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="224.8" y="281" text-anchor="middle" font-size="12" fill="#374151">15</text>
<line x1="279.0" y1="262" x2="279.0" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="279.0" y="281" text-anchor="middle" font-size="12" fill="#374151">20</text>
<line x1="333.2" y1="262" x2="333.2" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="333.2" y="281" text-anchor="middle" font-size="12" fill="#374151">25</text>
<line x1="387.5" y1="262" x2="387.5" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="387.5" y="281" text-anchor="middle" font-size="12" fill="#374151">30</text>
<line x1="441.8" y1="262" x2="441.8" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="441.8" y="281" text-anchor="middle" font-size="12" fill="#374151">35</text>
<line x1="496.0" y1="262" x2="496.0" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="496.0" y="281" text-anchor="middle" font-size="12" fill="#374151">40</text>
<text x="279" y="306" text-anchor="middle" font-size="13" fill="#111827">Volume of 0.100 M HCl added (mL)</text>
<text x="20" y="140" text-anchor="middle" font-size="13" fill="#111827" transform="rotate(-90 20 140)">pH</text>
<polyline points="62.0,70.3 65.3,74.7 68.5,78.2 71.8,80.8 76.1,83.4 81.5,85.9 87.5,88.1 103.8,92.3 121.7,95.6 145.0,99.0 235.1,109.4 267.1,113.7 293.6,118.5 303.4,121.0 311.6,123.6 318.6,126.8 324.0,130.5 327.8,134.6 330.4,139.6 331.9,145.0 332.7,152.1 333.6,188.5 334.8,200.1 336.2,205.2 338.5,209.3 341.4,212.7 345.7,215.8 353.3,219.3 363.1,222.2 375.6,224.7 391.3,226.9 410.8,228.8 434.7,230.6 496.0,233.5" fill="none" stroke="#111827" stroke-width="2.2" stroke-linejoin="round"/>
</svg>
<figcaption>Titration of 25.0 mL of 0.100 M B(aq) with 0.100 M HCl(aq) at 25 °C</figcaption>
</figure>""",
        "question": r"A $25.0\,\text{mL}$ sample of $0.100\,\text{M}$ aqueous weak base, $\text{B}$, is titrated with $0.100\,\text{M}\,\text{HCl}(aq)$ at $25^\circ\text{C}$, producing the titration curve shown above. Which of the following gives the value of $K_b$ for $\text{B}$ and correctly explains the $\text{pH}$ at the equivalence point?",
        "options": [
            r"$K_b = 1 \times 10^{-9}$; the $\text{pH}$ at the equivalence point is below $7$ because excess $\text{H}_3\text{O}^+$ from the $\text{HCl}$ is present at the equivalence point.",
            r"$K_b = 1 \times 10^{-9}$; the $\text{pH}$ at the equivalence point is below $7$ because $\text{HB}^+$ reacts with water to produce $\text{H}_3\text{O}^+$.",
            r"$K_b = 1 \times 10^{-5}$; the $\text{pH}$ at the equivalence point is below $7$ because excess $\text{H}_3\text{O}^+$ from the $\text{HCl}$ is present at the equivalence point.",
            r"$K_b = 1 \times 10^{-5}$; the $\text{pH}$ at the equivalence point is below $7$ because $\text{HB}^+$ reacts with water to produce $\text{H}_3\text{O}^+$.",
        ],
        "correct_index": 3,
        "explanation": r"The sharp drop shows the equivalence point at $25.0\,\text{mL}$, so the half-equivalence point is at $12.5\,\text{mL}$, where $[\text{B}] = [\text{HB}^+]$ and $\text{pH} = \text{p}K_a$ of $\text{HB}^+$. The curve gives $\text{pH} = 9.0$ there, so $\text{p}K_a = 9.0$, $\text{p}K_b = 14.0 - 9.0 = 5.0$, and $K_b = 1 \times 10^{-5}$; reading $9.0$ directly as $\text{p}K_b$ gives the incorrect $1 \times 10^{-9}$. At the equivalence point, the moles of $\text{H}_3\text{O}^+$ added equal the moles of $\text{B}$ originally present, so no excess strong acid remains. The solution contains $\text{HB}^+$ and the spectator ion $\text{Cl}^-$, and the weak acid $\text{HB}^+$ reacts with water ($\text{HB}^+ + \text{H}_2\text{O} \rightleftharpoons \text{B} + \text{H}_3\text{O}^+$), giving an acidic $\text{pH}$ of about $5.2$.",
    },
    {
        "unit_q_num": 62,
        "topic_code": "8.5",
        "topic_title": "Acid-Base Titrations",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 320" role="img" aria-label="Titration curve of a diprotic acid with 0.100 M NaOH from 0 to 50 mL. The pH starts near 2.0 and shows two steep rises, at 20.0 mL (pH about 5.3) and at 40.0 mL (pH about 10.0). Point W is at 10.0 mL (pH 3.0), point X at 20.0 mL (pH 5.3), point Y at 30.0 mL (pH 7.5), and point Z at 40.0 mL (pH 10.0)." font-family="sans-serif">
<line x1="62" y1="262.0" x2="496" y2="262.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="244.6" x2="496" y2="244.6" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="227.1" x2="496" y2="227.1" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="209.7" x2="496" y2="209.7" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="192.3" x2="496" y2="192.3" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="174.9" x2="496" y2="174.9" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="157.4" x2="496" y2="157.4" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="140.0" x2="496" y2="140.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="122.6" x2="496" y2="122.6" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="105.1" x2="496" y2="105.1" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="87.7" x2="496" y2="87.7" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="70.3" x2="496" y2="70.3" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="52.9" x2="496" y2="52.9" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="35.4" x2="496" y2="35.4" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="18.0" x2="496" y2="18.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62.0" y1="18" x2="62.0" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="105.4" y1="18" x2="105.4" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="148.8" y1="18" x2="148.8" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="192.2" y1="18" x2="192.2" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="235.6" y1="18" x2="235.6" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="279.0" y1="18" x2="279.0" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="322.4" y1="18" x2="322.4" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="365.8" y1="18" x2="365.8" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="409.2" y1="18" x2="409.2" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="452.6" y1="18" x2="452.6" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="496.0" y1="18" x2="496.0" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="262" x2="496" y2="262" stroke="#374151" stroke-width="1.8"/>
<line x1="62" y1="18" x2="62" y2="262" stroke="#374151" stroke-width="1.8"/>
<line x1="57" y1="262.0" x2="62" y2="262.0" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="266.0" text-anchor="end" font-size="12" fill="#374151">0</text>
<line x1="57" y1="227.1" x2="62" y2="227.1" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="231.1" text-anchor="end" font-size="12" fill="#374151">2</text>
<line x1="57" y1="192.3" x2="62" y2="192.3" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="196.3" text-anchor="end" font-size="12" fill="#374151">4</text>
<line x1="57" y1="157.4" x2="62" y2="157.4" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="161.4" text-anchor="end" font-size="12" fill="#374151">6</text>
<line x1="57" y1="122.6" x2="62" y2="122.6" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="126.6" text-anchor="end" font-size="12" fill="#374151">8</text>
<line x1="57" y1="87.7" x2="62" y2="87.7" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="91.7" text-anchor="end" font-size="12" fill="#374151">10</text>
<line x1="57" y1="52.9" x2="62" y2="52.9" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="56.9" text-anchor="end" font-size="12" fill="#374151">12</text>
<line x1="57" y1="18.0" x2="62" y2="18.0" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="22.0" text-anchor="end" font-size="12" fill="#374151">14</text>
<line x1="62.0" y1="262" x2="62.0" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="62.0" y="281" text-anchor="middle" font-size="12" fill="#374151">0</text>
<line x1="105.4" y1="262" x2="105.4" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="105.4" y="281" text-anchor="middle" font-size="12" fill="#374151">5</text>
<line x1="148.8" y1="262" x2="148.8" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="148.8" y="281" text-anchor="middle" font-size="12" fill="#374151">10</text>
<line x1="192.2" y1="262" x2="192.2" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="192.2" y="281" text-anchor="middle" font-size="12" fill="#374151">15</text>
<line x1="235.6" y1="262" x2="235.6" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="235.6" y="281" text-anchor="middle" font-size="12" fill="#374151">20</text>
<line x1="279.0" y1="262" x2="279.0" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="279.0" y="281" text-anchor="middle" font-size="12" fill="#374151">25</text>
<line x1="322.4" y1="262" x2="322.4" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="322.4" y="281" text-anchor="middle" font-size="12" fill="#374151">30</text>
<line x1="365.8" y1="262" x2="365.8" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="365.8" y="281" text-anchor="middle" font-size="12" fill="#374151">35</text>
<line x1="409.2" y1="262" x2="409.2" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="409.2" y="281" text-anchor="middle" font-size="12" fill="#374151">40</text>
<line x1="452.6" y1="262" x2="452.6" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="452.6" y="281" text-anchor="middle" font-size="12" fill="#374151">45</text>
<line x1="496.0" y1="262" x2="496.0" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="496.0" y="281" text-anchor="middle" font-size="12" fill="#374151">50</text>
<text x="279" y="306" text-anchor="middle" font-size="13" fill="#111827">Volume of 0.100 M NaOH added (mL)</text>
<text x="20" y="140" text-anchor="middle" font-size="13" fill="#111827" transform="rotate(-90 20 140)">pH</text>
<polyline points="62.0,226.8 82.8,221.5 102.4,217.4 167.0,206.2 186.6,202.4 202.6,198.5 214.8,194.5 223.4,190.0 226.9,187.4 229.5,184.6 231.6,181.7 233.2,178.2 237.4,164.3 239.9,158.7 242.1,155.7 244.7,153.1 251.7,148.5 262.5,144.1 278.1,139.8 297.7,135.7 359.3,124.4 375.8,120.4 387.9,116.4 393.6,113.8 397.9,111.1 401.4,108.2 404.3,104.5 406.2,101.0 407.5,96.9 410.3,80.6 412.2,74.3 413.7,71.3 415.7,68.6 418.3,66.2 421.4,64.0 426.1,61.6 431.8,59.5 447.0,55.8 468.2,52.7 496.0,50.2" fill="none" stroke="#111827" stroke-width="2.2" stroke-linejoin="round"/>
<circle cx="148.8" cy="209.3" r="4.5" fill="#2563eb" stroke="#ffffff" stroke-width="1.2"/>
<text x="144.8" y="198.3" text-anchor="end" font-size="14" font-weight="bold" fill="#2563eb">W</text>
<circle cx="235.6" cy="170.4" r="4.5" fill="#2563eb" stroke="#ffffff" stroke-width="1.2"/>
<text x="245.6" y="184.4" text-anchor="start" font-size="14" font-weight="bold" fill="#2563eb">X</text>
<circle cx="322.4" cy="131.3" r="4.5" fill="#2563eb" stroke="#ffffff" stroke-width="1.2"/>
<text x="318.4" y="120.3" text-anchor="end" font-size="14" font-weight="bold" fill="#2563eb">Y</text>
<circle cx="409.2" cy="87.5" r="4.5" fill="#2563eb" stroke="#ffffff" stroke-width="1.2"/>
<text x="419.2" y="101.5" text-anchor="start" font-size="14" font-weight="bold" fill="#2563eb">Z</text>
</svg>
<figcaption>Titration of H₂A(aq) with 0.100 M NaOH(aq) at 25 °C</figcaption>
</figure>""",
        "question": r"A sample of a weak diprotic acid, $\text{H}_2\text{A}$, is titrated with $0.100\,\text{M}\,\text{NaOH}(aq)$, producing the titration curve shown above. At which labeled point is $\text{HA}^-$ the predominant $\text{A}$-containing species, with $[\text{H}_2\text{A}]$ and $[\text{A}^{2-}]$ both much smaller than $[\text{HA}^-]$?",
        "options": [
            r"Point W",
            r"Point X",
            r"Point Y",
            r"Point Z",
        ],
        "correct_index": 1,
        "explanation": r"The curve has two steep rises, at $20.0\,\text{mL}$ and $40.0\,\text{mL}$, showing two acidic protons. At point X ($20.0\,\text{mL}$, the first equivalence point), the moles of $\text{OH}^-$ added equal the moles of $\text{H}_2\text{A}$, so essentially every $\text{H}_2\text{A}$ has lost one proton; $\text{HA}^-$ predominates, with only small amounts of $\text{H}_2\text{A}$ and $\text{A}^{2-}$. At point W (first half-equivalence point), $[\text{H}_2\text{A}] = [\text{HA}^-]$ and $\text{pH} = \text{p}K_{a1} \approx 3.0$. At point Y (second half-equivalence point), $[\text{HA}^-] = [\text{A}^{2-}]$ and $\text{pH} = \text{p}K_{a2} \approx 7.5$. At point Z (second equivalence point), $\text{A}^{2-}$ is the predominant species.",
    },
    {
        "unit_q_num": 63,
        "topic_code": "8.5",
        "topic_title": "Acid-Base Titrations",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A student determines the concentration of acetic acid in vinegar by titrating a $10.00\,\text{mL}$ sample of vinegar, delivered with a volumetric pipet, with standardized $0.1000\,\text{M}\,\text{NaOH}(aq)$, using phenolphthalein as the indicator. Which of the following errors would cause the calculated concentration of acetic acid to be LOWER than the actual concentration?",
        "options": [
            r"The buret was rinsed with distilled water but not with the $\text{NaOH}$ solution before it was filled.",
            r"The titration was stopped when the solution turned dark pink instead of at the first permanent faint pink color.",
            r"Distilled water was used to rinse the inner walls of the Erlenmeyer flask during the titration.",
            r"The volumetric pipet was rinsed with distilled water but not with vinegar before the sample was measured.",
        ],
        "correct_index": 3,
        "explanation": r"The acid concentration is calculated from $M_{\text{acid}} = \frac{M_{\text{NaOH}}V_{\text{NaOH}}}{V_{\text{acid}}}$, because at the equivalence point the moles of $\text{OH}^-$ added equal the moles of $\text{CH}_3\text{COOH}$ in the sample. Water left inside the pipet dilutes the vinegar, so the $10.00\,\text{mL}$ sample contains fewer moles of acid than assumed; less $\text{NaOH}$ is needed, and the calculated concentration is too low. Water left in the buret dilutes the $\text{NaOH}$, so a larger volume is needed and the result is too high. Overshooting the end point (dark pink) also records too much $\text{NaOH}$, giving a result that is too high. Rinsing the flask walls with water changes the volume but not the moles of acid, so it has no effect.",
    },
    {
        "unit_q_num": 64,
        "topic_code": "8.6",
        "topic_title": "Molecular Structure of Acids and Bases",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 230" role="img" aria-label="Structural formula of lactic acid, CH3-CH(OH)-COOH. Hydrogen 1 is one of the three hydrogen atoms on the CH3 carbon; hydrogen 2 is bonded to the central carbon; hydrogen 3 is bonded to the oxygen of the OH group on the central carbon; hydrogen 4 is bonded to the single-bonded oxygen of the carboxyl group, COOH." font-family="sans-serif">
<line x1="150" y1="130" x2="240" y2="130" stroke="#111827" stroke-width="2.2"/>
<line x1="240" y1="130" x2="330" y2="130" stroke="#111827" stroke-width="2.2"/>
<line x1="150" y1="130" x2="150" y2="78" stroke="#111827" stroke-width="2.2"/>
<line x1="150" y1="130" x2="150" y2="182" stroke="#111827" stroke-width="2.2"/>
<line x1="150" y1="130" x2="98" y2="130" stroke="#111827" stroke-width="2.2"/>
<line x1="240" y1="130" x2="240" y2="78" stroke="#111827" stroke-width="2.2"/>
<line x1="240" y1="78" x2="240" y2="28" stroke="#111827" stroke-width="2.2"/>
<line x1="240" y1="130" x2="240" y2="182" stroke="#111827" stroke-width="2.2"/>
<line x1="330" y1="130" x2="400" y2="130" stroke="#111827" stroke-width="2.2"/>
<line x1="400" y1="130" x2="452" y2="130" stroke="#111827" stroke-width="2.2"/>
<line x1="325.5" y1="130" x2="325.5" y2="78" stroke="#111827" stroke-width="2.2"/>
<line x1="334.5" y1="130" x2="334.5" y2="78" stroke="#111827" stroke-width="2.2"/>
<circle cx="150" cy="130" r="12" fill="#ffffff"/>
<text x="150" y="136.5" text-anchor="middle" font-size="19" fill="#111827">C</text>
<circle cx="150" cy="78" r="12" fill="#ffffff"/>
<text x="150" y="84.5" text-anchor="middle" font-size="19" fill="#111827">H</text>
<circle cx="150" cy="182" r="12" fill="#ffffff"/>
<text x="150" y="188.5" text-anchor="middle" font-size="19" fill="#111827">H</text>
<circle cx="98" cy="130" r="12" fill="#ffffff"/>
<text x="98" y="136.5" text-anchor="middle" font-size="19" fill="#111827">H</text>
<circle cx="240" cy="130" r="12" fill="#ffffff"/>
<text x="240" y="136.5" text-anchor="middle" font-size="19" fill="#111827">C</text>
<circle cx="240" cy="78" r="12" fill="#ffffff"/>
<text x="240" y="84.5" text-anchor="middle" font-size="19" fill="#111827">O</text>
<circle cx="240" cy="28" r="12" fill="#ffffff"/>
<text x="240" y="34.5" text-anchor="middle" font-size="19" fill="#111827">H</text>
<circle cx="240" cy="182" r="12" fill="#ffffff"/>
<text x="240" y="188.5" text-anchor="middle" font-size="19" fill="#111827">H</text>
<circle cx="330" cy="130" r="12" fill="#ffffff"/>
<text x="330" y="136.5" text-anchor="middle" font-size="19" fill="#111827">C</text>
<circle cx="330" cy="78" r="12" fill="#ffffff"/>
<text x="330" y="84.5" text-anchor="middle" font-size="19" fill="#111827">O</text>
<circle cx="400" cy="130" r="12" fill="#ffffff"/>
<text x="400" y="136.5" text-anchor="middle" font-size="19" fill="#111827">O</text>
<circle cx="452" cy="130" r="12" fill="#ffffff"/>
<text x="452" y="136.5" text-anchor="middle" font-size="19" fill="#111827">H</text>
<circle cx="76" cy="112" r="10" fill="#2563eb"/>
<text x="76" y="116.5" text-anchor="middle" font-size="13" font-weight="bold" fill="#ffffff">1</text>
<circle cx="262" cy="198" r="10" fill="#2563eb"/>
<text x="262" y="202.5" text-anchor="middle" font-size="13" font-weight="bold" fill="#ffffff">2</text>
<circle cx="262" cy="18" r="10" fill="#2563eb"/>
<text x="262" y="22.5" text-anchor="middle" font-size="13" font-weight="bold" fill="#ffffff">3</text>
<circle cx="474" cy="112" r="10" fill="#2563eb"/>
<text x="474" y="116.5" text-anchor="middle" font-size="13" font-weight="bold" fill="#ffffff">4</text>
</svg>
<figcaption>Lactic acid, CH₃CH(OH)COOH (lone pairs not shown)</figcaption>
</figure>""",
        "question": r"The structural formula of lactic acid is shown above, with four of its hydrogen atoms labeled $1$ through $4$. Which labeled hydrogen atom is most readily donated to water when lactic acid acts as a Brønsted–Lowry acid, and why?",
        "options": [
            r"Hydrogen $1$, because the $\text{CH}_3$ group has three equivalent hydrogen atoms that can be donated.",
            r"Hydrogen $2$, because it is bonded to a carbon atom that is attached to two oxygen-containing groups.",
            r"Hydrogen $3$, because it is bonded to an electronegative oxygen atom, and the anion formed when it is removed is stabilized by resonance.",
            r"Hydrogen $4$, because the negative charge of the carboxylate ion formed when it is removed is delocalized by resonance over two oxygen atoms.",
        ],
        "correct_index": 3,
        "explanation": r"Lactic acid is a carboxylic acid, a common class of weak acids. Removing hydrogen 4 (the $-\text{COOH}$ hydrogen) produces a carboxylate ion, $-\text{COO}^-$, whose negative charge is shared by resonance between two electronegative oxygen atoms; this stabilized conjugate base makes the carboxyl $\text{O}-\text{H}$ by far the most acidic proton. Hydrogen 3 is also bonded to oxygen, but removing it gives an alkoxide ion with the charge localized on a single oxygen atom (no resonance), so that $\text{O}-\text{H}$ is about as weakly acidic as the $\text{O}-\text{H}$ in ethanol. Hydrogens 1 and 2 are bonded to carbon; $\text{C}-\text{H}$ bonds are nearly nonpolar, and the resulting anions are not stabilized, so these hydrogens are not acidic in water.",
    },
    {
        "unit_q_num": 65,
        "topic_code": "8.7",
        "topic_title": "pH and pKa",
        "difficulty": "Challenging",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 320" role="img" aria-label="Titration curve of 25.0 mL of 0.100 M acetic acid with 0.100 M NaOH from 0 to 40 mL. The pH starts near 2.9, rises gradually through a buffer region, rises steeply at 25.0 mL where the pH is about 8.7, and levels off near 12.4. A shaded band from pH 4.2 to 6.2 is labeled methyl red; the curve passes through it between about 6 mL and 24 mL. A shaded band from pH 8.2 to 10.0 is labeled phenolphthalein; the curve passes through it in the steep rise at 25.0 mL." font-family="sans-serif">
<rect x="62" y="87.7" width="434" height="31.4" fill="#d1d5db" fill-opacity="0.55"/>
<rect x="62" y="153.9" width="434" height="34.9" fill="#d1d5db" fill-opacity="0.55"/>
<line x1="62" y1="262.0" x2="496" y2="262.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="244.6" x2="496" y2="244.6" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="227.1" x2="496" y2="227.1" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="209.7" x2="496" y2="209.7" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="192.3" x2="496" y2="192.3" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="174.9" x2="496" y2="174.9" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="157.4" x2="496" y2="157.4" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="140.0" x2="496" y2="140.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="122.6" x2="496" y2="122.6" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="105.1" x2="496" y2="105.1" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="87.7" x2="496" y2="87.7" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="70.3" x2="496" y2="70.3" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="52.9" x2="496" y2="52.9" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="35.4" x2="496" y2="35.4" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="18.0" x2="496" y2="18.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62.0" y1="18" x2="62.0" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="116.2" y1="18" x2="116.2" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="170.5" y1="18" x2="170.5" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="224.8" y1="18" x2="224.8" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="279.0" y1="18" x2="279.0" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="333.2" y1="18" x2="333.2" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="387.5" y1="18" x2="387.5" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="441.8" y1="18" x2="441.8" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="496.0" y1="18" x2="496.0" y2="262" stroke="#e5e7eb" stroke-width="1"/>
<line x1="62" y1="262" x2="496" y2="262" stroke="#374151" stroke-width="1.8"/>
<line x1="62" y1="18" x2="62" y2="262" stroke="#374151" stroke-width="1.8"/>
<line x1="57" y1="262.0" x2="62" y2="262.0" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="266.0" text-anchor="end" font-size="12" fill="#374151">0</text>
<line x1="57" y1="227.1" x2="62" y2="227.1" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="231.1" text-anchor="end" font-size="12" fill="#374151">2</text>
<line x1="57" y1="192.3" x2="62" y2="192.3" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="196.3" text-anchor="end" font-size="12" fill="#374151">4</text>
<line x1="57" y1="157.4" x2="62" y2="157.4" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="161.4" text-anchor="end" font-size="12" fill="#374151">6</text>
<line x1="57" y1="122.6" x2="62" y2="122.6" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="126.6" text-anchor="end" font-size="12" fill="#374151">8</text>
<line x1="57" y1="87.7" x2="62" y2="87.7" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="91.7" text-anchor="end" font-size="12" fill="#374151">10</text>
<line x1="57" y1="52.9" x2="62" y2="52.9" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="56.9" text-anchor="end" font-size="12" fill="#374151">12</text>
<line x1="57" y1="18.0" x2="62" y2="18.0" stroke="#374151" stroke-width="1.5"/>
<text x="53" y="22.0" text-anchor="end" font-size="12" fill="#374151">14</text>
<line x1="62.0" y1="262" x2="62.0" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="62.0" y="281" text-anchor="middle" font-size="12" fill="#374151">0</text>
<line x1="116.2" y1="262" x2="116.2" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="116.2" y="281" text-anchor="middle" font-size="12" fill="#374151">5</text>
<line x1="170.5" y1="262" x2="170.5" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="170.5" y="281" text-anchor="middle" font-size="12" fill="#374151">10</text>
<line x1="224.8" y1="262" x2="224.8" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="224.8" y="281" text-anchor="middle" font-size="12" fill="#374151">15</text>
<line x1="279.0" y1="262" x2="279.0" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="279.0" y="281" text-anchor="middle" font-size="12" fill="#374151">20</text>
<line x1="333.2" y1="262" x2="333.2" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="333.2" y="281" text-anchor="middle" font-size="12" fill="#374151">25</text>
<line x1="387.5" y1="262" x2="387.5" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="387.5" y="281" text-anchor="middle" font-size="12" fill="#374151">30</text>
<line x1="441.8" y1="262" x2="441.8" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="441.8" y="281" text-anchor="middle" font-size="12" fill="#374151">35</text>
<line x1="496.0" y1="262" x2="496.0" y2="267" stroke="#374151" stroke-width="1.5"/>
<text x="496.0" y="281" text-anchor="middle" font-size="12" fill="#374151">40</text>
<text x="279" y="306" text-anchor="middle" font-size="13" fill="#111827">Volume of 0.100 M NaOH added (mL)</text>
<text x="20" y="140" text-anchor="middle" font-size="13" fill="#111827" transform="rotate(-90 20 140)">pH</text>
<polyline points="62.0,211.9 69.6,204.8 77.7,200.0 89.7,195.6 105.4,191.8 123.3,188.6 146.1,185.3 234.5,175.1 266.5,170.8 293.1,166.1 303.4,163.5 311.6,160.8 318.6,157.6 324.0,154.0 328.0,149.7 330.6,144.4 332.0,138.8 332.8,131.3 333.5,92.6 334.6,80.6 336.0,75.4 338.2,71.1 341.4,67.3 345.2,64.5 352.2,61.1 362.0,58.1 374.5,55.5 390.8,53.2 410.3,51.2 434.2,49.5 496.0,46.5" fill="none" stroke="#111827" stroke-width="2.2" stroke-linejoin="round"/>
<text x="70" y="107.4" font-size="12" fill="#111827">phenolphthalein (pH 8.2–10.0)</text>
<text x="488" y="175.4" text-anchor="end" font-size="12" fill="#111827">methyl red (pH 4.2–6.2)</text>
</svg>
<figcaption>Titration of 25.0 mL of 0.100 M CH₃COOH(aq) with 0.100 M NaOH(aq); shaded bands show indicator color-change ranges</figcaption>
</figure>""",
        "question": r"The titration curve above is for $25.0\,\text{mL}$ of $0.100\,\text{M}\,\text{CH}_3\text{COOH}(aq)$ titrated with $0.100\,\text{M}\,\text{NaOH}(aq)$. The shaded bands show the $\text{pH}$ ranges over which two indicators change color. A student uses methyl red instead of phenolphthalein and records the volume of $\text{NaOH}$ at which the color change of methyl red is complete. How will the student's calculated concentration of $\text{CH}_3\text{COOH}$ compare with the actual concentration, and why?",
        "options": [
            r"It will be lower than the actual value, because methyl red completes its color change at a $\text{pH}$ that is reached before the equivalence point, so too little $\text{NaOH}$ is recorded.",
            r"It will be higher than the actual value, because methyl red changes color after the equivalence point, so too much $\text{NaOH}$ is recorded.",
            r"It will be equal to the actual value, because the volume of $\text{NaOH}$ required to reach the equivalence point does not depend on the indicator used.",
            r"It will be higher than the actual value, because methyl red is a weak acid that consumes a significant amount of the $\text{NaOH}$.",
        ],
        "correct_index": 0,
        "explanation": r"An indicator gives accurate results only if its color change occurs at (or very near) the $\text{pH}$ of the equivalence point, that is, if its $\text{p}K_a$ is close to that $\text{pH}$. Here the equivalence point is at $25.0\,\text{mL}$ with $\text{pH} \approx 8.7$ (basic, because $\text{CH}_3\text{COO}^-$ is present), which lies in the phenolphthalein band. The methyl red band ($\text{pH}$ 4.2 to 6.2) is crossed in the buffer region: the curve reaches $\text{pH}\ 6.2$ at about $24\,\text{mL}$, before the equivalence point. The recorded volume of $\text{NaOH}$ is therefore too small, and $M_{\text{acid}} = M_{\text{NaOH}}V_{\text{NaOH}}/V_{\text{acid}}$ is too low. The equivalence-point volume does not depend on the indicator, but the observed end point does, and the few drops of indicator consume a negligible amount of base.",
    },
    {
        "unit_q_num": 66,
        "topic_code": "8.7",
        "topic_title": "pH and pKa",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Indicator</th><th>Color of $\text{HIn}$ (acid form)</th><th>Color of $\text{In}^-$ (base form)</th><th>$\text{pH}$ range of color change</th><th>Color observed in solution X</th></tr></thead><tbody><tr><td>Methyl orange</td><td>Red</td><td>Yellow</td><td>$3.1$ to $4.4$</td><td>Yellow</td></tr><tr><td>Bromothymol blue</td><td>Yellow</td><td>Blue</td><td>$6.0$ to $7.6$</td><td>Yellow</td></tr></tbody></table>""",
        "question": r"A few drops of each indicator listed in the table above are added to separate samples of solution X at $25^\circ\text{C}$, and the colors in the last column are observed. Which of the following could be solution X? ($K_a$ for $\text{CH}_3\text{COOH}$ and $K_b$ for $\text{NH}_3$ are both $1.8 \times 10^{-5}$.)",
        "options": [
            r"$0.10\,\text{M}\,\text{CH}_3\text{COOH}(aq)$",
            r"$0.10\,\text{M}\,\text{NH}_4\text{Cl}(aq)$",
            r"$0.10\,\text{M}\,\text{NaCl}(aq)$",
            r"$0.10\,\text{M}\,\text{NaCH}_3\text{COO}(aq)$",
        ],
        "correct_index": 1,
        "explanation": r"An indicator shows its base-form color when the $\text{pH}$ is above its transition range and its acid-form color when the $\text{pH}$ is below that range. Yellow methyl orange (base form) means $\text{pH} > 4.4$, and yellow bromothymol blue (acid form) means $\text{pH} < 6.0$, so $4.4 < \text{pH} < 6.0$. $\text{NH}_4^+$ is a weak acid with $K_a = K_w/K_b = 5.6 \times 10^{-10}$, so $[\text{H}_3\text{O}^+] = \sqrt{(5.6 \times 10^{-10})(0.10)} = 7.5 \times 10^{-6}\,\text{M}$ and $\text{pH} = 5.13$, which fits. $0.10\,\text{M}\,\text{CH}_3\text{COOH}$ has $\text{pH} = 2.87$ (methyl orange would be red), $\text{NaCl}$ is neutral ($\text{pH} = 7.00$; bromothymol blue would be green), and $\text{CH}_3\text{COO}^-$ is a weak base ($\text{pH} = 8.87$; bromothymol blue would be blue).",
    },
    {
        "unit_q_num": 67,
        "topic_code": "8.9",
        "topic_title": "Henderson-Hasselbalch Equation",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 260" role="img" aria-label="Particulate diagram of a portion of a buffer solution: 3 HA molecules, 6 A minus ions, and 6 sodium ions. Water molecules are not shown." font-family="sans-serif">
<rect x="20" y="20" width="330" height="220" rx="10" fill="#ffffff" stroke="#374151" stroke-width="2"/>
<circle cx="56" cy="60" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/><text x="56" y="64.5" text-anchor="middle" font-size="13" font-weight="bold" fill="#111827">+</text>
<circle cx="124" cy="66" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="124" y="71" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<circle cx="190" cy="58" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="200" cy="49" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="252" cy="68" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="252" y="73" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<circle cx="318" cy="60" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/><text x="318" y="64.5" text-anchor="middle" font-size="13" font-weight="bold" fill="#111827">+</text>
<circle cx="60" cy="132" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="60" y="137" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<circle cx="126" cy="126" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/><text x="126" y="130.5" text-anchor="middle" font-size="13" font-weight="bold" fill="#111827">+</text>
<circle cx="186" cy="136" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="186" y="141" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<circle cx="256" cy="128" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="266" cy="119" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="320" cy="134" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/><text x="320" y="138.5" text-anchor="middle" font-size="13" font-weight="bold" fill="#111827">+</text>
<circle cx="54" cy="198" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/><text x="54" y="202.5" text-anchor="middle" font-size="13" font-weight="bold" fill="#111827">+</text>
<circle cx="122" cy="204" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="132" cy="195" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="190" cy="196" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="190" y="201" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<circle cx="258" cy="202" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/><text x="258" y="206.5" text-anchor="middle" font-size="13" font-weight="bold" fill="#111827">+</text>
<circle cx="316" cy="198" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="316" y="203" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<text x="384" y="52" font-size="13" font-weight="bold" fill="#111827">Key</text>
<circle cx="398" cy="92" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="408" cy="83" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<text x="428" y="97" font-size="14" fill="#111827">HA</text>
<circle cx="398" cy="142" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="398" y="147" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<text x="428" y="147" font-size="14" fill="#111827">A⁻</text>
<circle cx="398" cy="192" r="8" fill="#ffffff" stroke="#374151" stroke-width="1.5"/><text x="398" y="196.5" text-anchor="middle" font-size="13" font-weight="bold" fill="#111827">+</text>
<text x="428" y="197" font-size="14" fill="#111827">Na⁺</text>
</svg>
<figcaption>Water molecules are not shown.</figcaption>
</figure>""",
        "question": r"The particulate diagram above represents a small portion of a buffer solution prepared from a weak acid, $\text{HA}$ ($\text{p}K_a = 4.74$), and its sodium salt, $\text{NaA}$. Based on the diagram, what is the $\text{pH}$ of the buffer? ($\log 2.0 = 0.30$)",
        "options": [
            r"$4.44$",
            r"$4.74$",
            r"$5.04$",
            r"$5.34$",
        ],
        "correct_index": 2,
        "explanation": r"By the Henderson–Hasselbalch equation, $\text{pH} = \text{p}K_a + \log\frac{[\text{A}^-]}{[\text{HA}]}$; because all of the particles are in the same volume, the concentration ratio equals the particle ratio. The diagram shows $6$ $\text{A}^-$ ions and $3$ $\text{HA}$ molecules ($\text{Na}^+$ is a spectator ion and is not part of the conjugate acid-base pair), so $\text{pH} = 4.74 + \log\frac{6}{3} = 4.74 + 0.30 = 5.04$. Inverting the ratio gives $4.44$; counting the $\text{Na}^+$ ions as base ($\frac{12}{3} = 4$) gives $5.34$; and $\text{pH} = 4.74$ would require equal numbers of $\text{HA}$ and $\text{A}^-$.",
    },
    {
        "unit_q_num": 68,
        "topic_code": "8.10",
        "topic_title": "Buffer Capacity",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 540 265" role="img" aria-label="Three particulate diagrams of equal-volume buffer solutions. Buffer X contains 6 HA molecules and 2 A minus ions; Buffer Y contains 4 HA molecules and 4 A minus ions; Buffer Z contains 2 HA molecules and 6 A minus ions. Sodium ions and water molecules are not shown." font-family="sans-serif">
<rect x="20" y="20" width="150" height="175" rx="10" fill="#ffffff" stroke="#374151" stroke-width="2"/>
<circle cx="60" cy="54" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="70" cy="45" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="128" cy="60" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="138" cy="51" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="66" cy="96" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="66" y="101" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<circle cx="124" cy="92" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="134" cy="83" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="58" cy="136" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="68" cy="127" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="130" cy="132" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="140" cy="123" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="64" cy="174" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="64" y="179" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<circle cx="126" cy="170" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="136" cy="161" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<text x="95" y="216" text-anchor="middle" font-size="14" font-weight="bold" fill="#111827">Buffer X</text>
<rect x="195" y="20" width="150" height="175" rx="10" fill="#ffffff" stroke="#374151" stroke-width="2"/>
<circle cx="235" cy="54" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="245" cy="45" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="303" cy="60" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="303" y="65" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<circle cx="241" cy="96" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="241" y="101" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<circle cx="299" cy="92" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="309" cy="83" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="233" cy="136" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="243" cy="127" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="305" cy="132" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="305" y="137" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<circle cx="239" cy="174" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="239" y="179" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<circle cx="301" cy="170" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="311" cy="161" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<text x="270" y="216" text-anchor="middle" font-size="14" font-weight="bold" fill="#111827">Buffer Y</text>
<rect x="370" y="20" width="150" height="175" rx="10" fill="#ffffff" stroke="#374151" stroke-width="2"/>
<circle cx="410" cy="54" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="410" y="59" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<circle cx="478" cy="60" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="478" y="65" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<circle cx="416" cy="96" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="426" cy="87" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="474" cy="92" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="474" y="97" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<circle cx="408" cy="136" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="408" y="141" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<circle cx="480" cy="132" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="480" y="137" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<circle cx="414" cy="174" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="424" cy="165" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<circle cx="476" cy="170" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="476" y="175" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<text x="445" y="216" text-anchor="middle" font-size="14" font-weight="bold" fill="#111827">Buffer Z</text>
<circle cx="205" cy="246" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="215" cy="237" r="6" fill="#ffffff" stroke="#374151" stroke-width="1.5"/>
<text x="226" y="251" font-size="14" fill="#111827">= HA</text>
<circle cx="305" cy="246" r="11" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="305" y="251" text-anchor="middle" font-size="17" font-weight="bold" fill="#111827">−</text>
<text x="324" y="251" font-size="14" fill="#111827">= A⁻</text>
</svg>
<figcaption>Na⁺ ions and water molecules are not shown; all three samples have the same volume.</figcaption>
</figure>""",
        "question": r"The particulate diagrams above represent equal volumes of three buffer solutions, each made from the same weak acid, $\text{HA}$, and its conjugate base, $\text{A}^-$. Which buffer can neutralize the greatest amount of added strong base, $\text{OH}^-$, before its buffer capacity is exceeded, and how does its $\text{pH}$ compare with the $\text{p}K_a$ of $\text{HA}$?",
        "options": [
            r"Buffer X; its $\text{pH}$ is less than the $\text{p}K_a$ of $\text{HA}$.",
            r"Buffer X; its $\text{pH}$ is greater than the $\text{p}K_a$ of $\text{HA}$.",
            r"Buffer Y; its $\text{pH}$ is equal to the $\text{p}K_a$ of $\text{HA}$.",
            r"Buffer Z; its $\text{pH}$ is greater than the $\text{p}K_a$ of $\text{HA}$.",
        ],
        "correct_index": 0,
        "explanation": r"Added $\text{OH}^-$ is neutralized by the weak-acid component of a buffer: $\text{HA} + \text{OH}^- \rightarrow \text{A}^- + \text{H}_2\text{O}$. Buffer X contains the most $\text{HA}$ ($6$ particles), so it can neutralize the most $\text{OH}^-$ before its $\text{HA}$ is used up. Because $[\text{HA}] > [\text{A}^-]$ in Buffer X, $\log\frac{[\text{A}^-]}{[\text{HA}]}$ is negative and $\text{pH} < \text{p}K_a$. Buffer Z, with the most $\text{A}^-$, has the greatest capacity for added acid, not added base. Buffer Y has $\text{pH} = \text{p}K_a$ and equal capacity for added acid and added base, but it contains less $\text{HA}$ than Buffer X.",
    },
    {
        "unit_q_num": 69,
        "topic_code": "8.10",
        "topic_title": "Buffer Capacity",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"A student intends to prepare a buffer that is $0.20\,\text{M}$ in $\text{CH}_3\text{COOH}$ and $0.20\,\text{M}$ in $\text{CH}_3\text{COONa}$ ($\text{p}K_a$ of $\text{CH}_3\text{COOH} = 4.76$). The student weighs out the calculated mass of solid $\text{CH}_3\text{COONa}$, but the solid had absorbed water from the air, so only part of the weighed mass was $\text{CH}_3\text{COONa}$. All other steps are performed correctly. Compared with the intended buffer, how do the $\text{pH}$ and the buffer capacity of the prepared buffer differ?",
        "options": [
            r"The $\text{pH}$ is higher, and the buffer can neutralize less added strong acid.",
            r"The $\text{pH}$ is the same, because $\text{pH} = \text{p}K_a$ for any acetate buffer, but the buffer can neutralize less added strong acid and less added strong base.",
            r"The $\text{pH}$ is lower, and the buffer can neutralize less added strong acid.",
            r"The $\text{pH}$ is lower, and the buffer can neutralize less added strong base.",
        ],
        "correct_index": 2,
        "explanation": r"Because part of the weighed mass was water, the prepared buffer contains less $\text{CH}_3\text{COO}^-$ than intended, while $[\text{CH}_3\text{COOH}]$ is still $0.20\,\text{M}$. With $[\text{CH}_3\text{COO}^-] < [\text{CH}_3\text{COOH}]$, $\log\frac{[\text{CH}_3\text{COO}^-]}{[\text{CH}_3\text{COOH}]}$ is negative, so the $\text{pH}$ is below the intended value of $4.76$. Added strong acid is neutralized by the conjugate base ($\text{CH}_3\text{COO}^- + \text{H}_3\text{O}^+ \rightarrow \text{CH}_3\text{COOH} + \text{H}_2\text{O}$), so the capacity for added acid decreases. The capacity for added base depends on the amount of $\text{CH}_3\text{COOH}$, which is unchanged. $\text{pH} = \text{p}K_a$ only when the two components are present in equal amounts.",
    },
    {
        "unit_q_num": 70,
        "topic_code": "8.11",
        "topic_title": "pH and Solubility",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 300" role="img" aria-label="Graph of the molar solubility of calcium fluoride, on a logarithmic axis from 1 times 10 to the minus 4 to 1 times 10 to the minus 2 molar, versus pH from 1 to 8. The curve is flat at about 2 times 10 to the minus 4 molar from pH 8 down to about pH 5, then rises increasingly steeply as the pH decreases, reaching about 6 times 10 to the minus 3 molar at pH 1." font-family="sans-serif">
<line x1="92.0" y1="18" x2="92.0" y2="236" stroke="#e5e7eb" stroke-width="1"/>
<line x1="149.7" y1="18" x2="149.7" y2="236" stroke="#e5e7eb" stroke-width="1"/>
<line x1="207.4" y1="18" x2="207.4" y2="236" stroke="#e5e7eb" stroke-width="1"/>
<line x1="265.1" y1="18" x2="265.1" y2="236" stroke="#e5e7eb" stroke-width="1"/>
<line x1="322.9" y1="18" x2="322.9" y2="236" stroke="#e5e7eb" stroke-width="1"/>
<line x1="380.6" y1="18" x2="380.6" y2="236" stroke="#e5e7eb" stroke-width="1"/>
<line x1="438.3" y1="18" x2="438.3" y2="236" stroke="#e5e7eb" stroke-width="1"/>
<line x1="496.0" y1="18" x2="496.0" y2="236" stroke="#e5e7eb" stroke-width="1"/>
<line x1="92" y1="236.0" x2="496" y2="236.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="92" y1="181.5" x2="496" y2="181.5" stroke="#e5e7eb" stroke-width="1"/>
<line x1="92" y1="127.0" x2="496" y2="127.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="92" y1="72.5" x2="496" y2="72.5" stroke="#e5e7eb" stroke-width="1"/>
<line x1="92" y1="18.0" x2="496" y2="18.0" stroke="#e5e7eb" stroke-width="1"/>
<line x1="92" y1="236" x2="496" y2="236" stroke="#374151" stroke-width="1.8"/>
<line x1="92" y1="18" x2="92" y2="236" stroke="#374151" stroke-width="1.8"/>
<line x1="92.0" y1="236" x2="92.0" y2="241" stroke="#374151" stroke-width="1.5"/>
<text x="92.0" y="255" text-anchor="middle" font-size="12" fill="#374151">1</text>
<line x1="149.7" y1="236" x2="149.7" y2="241" stroke="#374151" stroke-width="1.5"/>
<text x="149.7" y="255" text-anchor="middle" font-size="12" fill="#374151">2</text>
<line x1="207.4" y1="236" x2="207.4" y2="241" stroke="#374151" stroke-width="1.5"/>
<text x="207.4" y="255" text-anchor="middle" font-size="12" fill="#374151">3</text>
<line x1="265.1" y1="236" x2="265.1" y2="241" stroke="#374151" stroke-width="1.5"/>
<text x="265.1" y="255" text-anchor="middle" font-size="12" fill="#374151">4</text>
<line x1="322.9" y1="236" x2="322.9" y2="241" stroke="#374151" stroke-width="1.5"/>
<text x="322.9" y="255" text-anchor="middle" font-size="12" fill="#374151">5</text>
<line x1="380.6" y1="236" x2="380.6" y2="241" stroke="#374151" stroke-width="1.5"/>
<text x="380.6" y="255" text-anchor="middle" font-size="12" fill="#374151">6</text>
<line x1="438.3" y1="236" x2="438.3" y2="241" stroke="#374151" stroke-width="1.5"/>
<text x="438.3" y="255" text-anchor="middle" font-size="12" fill="#374151">7</text>
<line x1="496.0" y1="236" x2="496.0" y2="241" stroke="#374151" stroke-width="1.5"/>
<text x="496.0" y="255" text-anchor="middle" font-size="12" fill="#374151">8</text>
<line x1="87" y1="236.0" x2="92" y2="236.0" stroke="#374151" stroke-width="1.5"/>
<text x="84" y="240.0" text-anchor="end" font-size="12" fill="#374151">1×10⁻⁴</text>
<line x1="87" y1="127.0" x2="92" y2="127.0" stroke="#374151" stroke-width="1.5"/>
<text x="84" y="131.0" text-anchor="end" font-size="12" fill="#374151">1×10⁻³</text>
<line x1="87" y1="18.0" x2="92" y2="18.0" stroke="#374151" stroke-width="1.5"/>
<text x="84" y="22.0" text-anchor="end" font-size="12" fill="#374151">1×10⁻²</text>
<text x="294" y="280" text-anchor="middle" font-size="13" fill="#111827">pH of buffered solution</text>
<text x="18" y="127" text-anchor="middle" font-size="13" fill="#111827" transform="rotate(-90 18 127)">Molar solubility of CaF₂ (M), log scale</text>
<polyline points="92.0,42.3 125.5,83.9 148.6,111.8 167.0,133.0 183.2,150.1 197.0,163.1 204.0,168.9 210.9,174.0 216.7,177.9 223.6,182.0 230.5,185.5 237.4,188.5 250.1,192.6 264.0,195.5 280.1,197.6 299.8,198.9 321.7,199.6 351.7,199.9 496.0,200.1" fill="none" stroke="#111827" stroke-width="2.2" stroke-linejoin="round"/>
</svg>
<figcaption>Molar solubility of CaF₂(s) in buffered solutions at 25 °C</figcaption>
</figure>""",
        "question": r"The graph above shows the measured molar solubility of $\text{CaF}_2(s)$ in buffered aqueous solutions at $25^\circ\text{C}$ as a function of $\text{pH}$. Which of the following best explains the shape of the curve?",
        "options": [
            r"The value of $K_{sp}$ for $\text{CaF}_2$ increases as the $\text{pH}$ decreases, because $\text{H}_3\text{O}^+$ ions weaken the attractions between the $\text{Ca}^{2+}$ and $\text{F}^-$ ions.",
            r"Below about $\text{pH}\ 4$, $\text{H}_3\text{O}^+$ reacts with $\text{Ca}^{2+}$, which lowers $[\text{Ca}^{2+}]$ so that more $\text{CaF}_2$ dissolves.",
            r"Above about $\text{pH}\ 5$, the solubility is constant because $\text{F}^-$ is the conjugate base of a strong acid and does not react with $\text{H}_3\text{O}^+$.",
            r"Below about $\text{pH}\ 4$, $\text{H}_3\text{O}^+$ converts $\text{F}^-$ to $\text{HF}$, which lowers $[\text{F}^-]$ so that more $\text{CaF}_2$ dissolves; above about $\text{pH}\ 5$, $[\text{H}_3\text{O}^+]$ is too low to convert a significant amount of $\text{F}^-$ to $\text{HF}$.",
        ],
        "correct_index": 3,
        "explanation": r"For $\text{CaF}_2(s) \rightleftharpoons \text{Ca}^{2+}(aq) + 2\,\text{F}^-(aq)$, the anion $\text{F}^-$ is the conjugate base of the weak acid $\text{HF}$ ($\text{p}K_a \approx 3.2$). When the $\text{pH}$ is near or below the $\text{p}K_a$, much of the fluoride is converted to $\text{HF}$ ($\text{F}^- + \text{H}_3\text{O}^+ \rightarrow \text{HF} + \text{H}_2\text{O}$); the lower $[\text{F}^-]$ makes $Q < K_{sp}$, so more solid dissolves (Le Châtelier), and the solubility rises as the $\text{pH}$ falls. When the $\text{pH}$ is well above the $\text{p}K_a$, nearly all of the fluoride remains as $\text{F}^-$, so the solubility does not depend on $\text{pH}$. $K_{sp}$ depends only on temperature, $\text{Ca}^{2+}$ is not a base, and $\text{HF}$ is a weak acid, not a strong one.",
    },
]
