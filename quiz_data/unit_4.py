UNIT_META = {
    "id": 4,
    "title": "Unit 4: Chemical Reactions",
    "short_title": "Chemical Reactions & Stoichiometry",
    "exam_weight": "7–9%",
    "color": "#059669",
    "description": "Physical vs. chemical changes, balanced molecular and net ionic equations, particulate representations, limiting reactants, percent yield, gravimetric & volumetric stoichiometry, acid-base and redox titrations, Brønsted-Lowry conjugate acid-base pairs, oxidation numbers, and balancing redox half-reactions.",
    "topics": [
        {"code": "4.1", "title": "Introduction for Reactions"},
        {"code": "4.2", "title": "Net Ionic Equations"},
        {"code": "4.3", "title": "Representations of Reactions"},
        {"code": "4.4", "title": "Physical and Chemical Changes"},
        {"code": "4.5", "title": "Stoichiometry"},
        {"code": "4.6", "title": "Introduction to Titration"},
        {"code": "4.7", "title": "Types of Chemical Reactions"},
        {"code": "4.8", "title": "Introduction to Acid-Base Reactions"},
        {"code": "4.9", "title": "Oxidation-Reduction (Redox) Reactions"},
    ],
}

QUESTIONS = [
    # -------------------------------------------------------------------------
    # 4.1 Introduction for Reactions (Q1 - Q5)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 1,
        "topic_code": "4.1",
        "topic_title": "Introduction for Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Experiment</th><th>Procedure</th><th>Macroscopic Observation</th></tr></thead>"
            "<tbody>"
            "<tr><td>1</td><td>Solid $\\text{NH}_4\\text{NO}_3$ is stirred into distilled water at $25^\\circ\\text{C}$.</td><td>The solid disappears and the temperature of the solution drops to $18^\\circ\\text{C}$.</td></tr>"
            "<tr><td>2</td><td>Clear, colorless solutions of $\\text{Pb(NO}_3)_2(aq)$ and $\\text{KI}(aq)$ are mixed.</td><td>A bright yellow solid forms and settles to the bottom of the beaker.</td></tr>"
            "<tr><td>3</td><td>Solid $\\text{I}_2$ crystals are gently warmed in an evaporating dish covered with a watch glass containing ice.</td><td>Purple vapor fills the dish and dark crystals form on the underside of the watch glass.</td></tr>"
            "<tr><td>4</td><td>Aqueous $\\text{NaCl}$ is heated on a hot plate until the liquid volume decreases by half.</td><td>Steam rises from the beaker; the remaining solution stays clear and colorless.</td></tr>"
            "</tbody></table>"
        ),
        "question": r"Based on the experimental observations in the table above, which experiment provides the strongest macroscopic evidence that a chemical reaction has occurred?",
        "options": [
            r"Experiment 1, because a temperature change always indicates covalent bond breaking",
            r"Experiment 2, because the formation of an insoluble precipitate from two aqueous solutions indicates the formation of a new substance",
            r"Experiment 3, because the color change from solid crystals to purple vapor proves a new compound was synthesized",
            r"Experiment 4, because gas evolution during heating proves decomposition of the solute",
        ],
        "correct_index": 1,
        "explanation": r"In Experiment 2, mixing $\text{Pb(NO}_3)_2(aq)$ and $\text{KI}(aq)$ produces a yellow precipitate of $\text{PbI}_2(s)$, which is definitive macroscopic evidence of a chemical change (new substance formed). Experiment 1 is the endothermic dissolution of an ionic salt, Experiment 3 is the sublimation and deposition of $\text{I}_2$, and Experiment 4 is the vaporization (boiling) of water.",
    },
    {
        "unit_q_num": 2,
        "topic_code": "4.1",
        "topic_title": "Introduction for Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"When $50.0\text{ mL}$ of $0.20\text{ M }\text{Na}_2\text{CO}_3(aq)$ is added to $50.0\text{ mL}$ of $0.50\text{ M }\text{HCl}(aq)$ (an excess of acid) in an open beaker on an analytical balance, effervescence is observed and the total mass recorded by the balance decreases slightly over two minutes. Which of the following best explains why this observation does not violate the law of conservation of mass?",
        "options": [
            r"Mass is converted into thermal energy during the exothermic neutralization reaction.",
            r"Hydronium ions and hydroxide ions combine to form liquid water, which has a lower density than the ionic reactants.",
            r"Carbonate ions have a larger molar mass in the aqueous phase than in the gaseous phase.",
            r"The gaseous product, $\text{CO}_2(g)$, escapes from the open beaker into the surroundings and is no longer weighed by the balance.",
        ],
        "correct_index": 3,
        "explanation": r"The acid is in excess ($0.025\text{ mol H}^+$, while $0.010\text{ mol CO}_3^{2-}$ requires only $0.020\text{ mol H}^+$), so the reaction $\text{CO}_3^{2-}(aq) + 2\text{H}^+(aq) \rightarrow \text{H}_2\text{O}(l) + \text{CO}_2(g)$ goes to completion and produces carbon dioxide gas. In an open container, $\text{CO}_2(g)$ escapes into the atmosphere, decreasing the mass remaining on the balance while total mass of reactants and products (including the escaped gas) remains strictly conserved. Mass is not converted into energy in a chemical reaction, and changes in density or phase of species that stay in the beaker cannot change the mass being weighed.",
    },
    {
        "unit_q_num": 3,
        "topic_code": "4.1",
        "topic_title": "Introduction for Reactions",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"A student adds a strip of shiny zinc metal, $\text{Zn}(s)$, to $1.0\text{ M }\text{CuSO}_4(aq)$ in a test tube. Over $15\text{ minutes}$, the blue color of the solution fades, a reddish-brown solid coats the metal strip, and the temperature of the mixture increases. Which of the following statements correctly links a macroscopic observation to the particulate process occurring?",
        "options": [
            r"The blue color fades because $\text{SO}_4^{2-}(aq)$ ions are reduced to $\text{SO}_2(g)$ at the metal surface.",
            r"The temperature increases because breaking metallic bonds in $\text{Zn}(s)$ releases heat to the solvent.",
            r"The blue color fades and a reddish-brown solid forms because hydrated $\text{Cu}^{2+}(aq)$ ions gain electrons to form $\text{Cu}(s)$ as $\text{Zn}(s)$ is oxidized to colorless $\text{Zn}^{2+}(aq)$.",
            r"The reddish-brown solid is copper(II) oxide formed by the reaction of $\text{Cu}^{2+}(aq)$ with dissolved oxygen.",
        ],
        "correct_index": 2,
        "explanation": r"Aqueous $\text{Cu}^{2+}(aq)$ ions are responsible for the characteristic blue color of $\text{CuSO}_4(aq)$. As $\text{Zn}(s)$ reduces $\text{Cu}^{2+}(aq)$ to reddish-brown metallic $\text{Cu}(s)$ ($\text{Zn}(s) + \text{Cu}^{2+}(aq) \rightarrow \text{Zn}^{2+}(aq) + \text{Cu}(s)$), the concentration of $\text{Cu}^{2+}(aq)$ decreases and colorless $\text{Zn}^{2+}(aq)$ enters solution.",
    },
    {
        "unit_q_num": 4,
        "topic_code": "4.1",
        "topic_title": "Introduction for Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"Equal volumes of two clear, colorless aqueous solutions are mixed in a calorimeter, and the temperature of the mixture rises by $6.4^\circ\text{C}$, while no precipitate or gas forms. Which of the following conclusions is best supported by this information?",
        "options": [
            r"A physical dilution must have occurred because no phase change or color change was observed.",
            r"A redox reaction occurred in which water was oxidized to hydrogen peroxide.",
            r"No net ionic reaction occurred because all ions remained dissolved in the aqueous phase.",
            r"A chemical reaction such as strong acid–strong base neutralization ($\text{H}^+(aq) + \text{OH}^-(aq) \rightarrow \text{H}_2\text{O}(l)$) likely occurred, indicated by the significant release of heat upon mixing two dilute aqueous solutions.",
        ],
        "correct_index": 3,
        "explanation": r"While many chemical reactions produce precipitates, gases, or color changes, acid-base neutralization between colorless strong acids and bases (e.g., $\text{HCl}(aq)$ and $\text{NaOH}(aq)$) forms soluble salt ions and $\text{H}_2\text{O}(l)$ with no visible change other than a substantial exothermic temperature increase.",
    },
    {
        "unit_q_num": 5,
        "topic_code": "4.1",
        "topic_title": "Introduction for Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"When aqueous solutions of $\text{NH}_4\text{Cl}(aq)$ and $\text{NaOH}(aq)$ are mixed in a test tube, no precipitate forms and the solution remains colorless, yet a pungent odor is detected above the test tube and moist red litmus paper held over the mouth of the tube turns blue. Which statement best accounts for these observations?",
        "options": [
            r"A chemical reaction transferred a proton from $\text{NH}_4^+(aq)$ to $\text{OH}^-(aq)$, producing volatile basic $\text{NH}_3(g)$ and $\text{H}_2\text{O}(l)$.",
            r"Chloride ions were oxidized by hydroxide ions to produce pungent $\text{Cl}_2(g)$.",
            r"Sodium hydroxide evaporated from the warm solution and condensed on the litmus paper.",
            r"Ammonium chloride sublimed directly from the aqueous solution without undergoing a chemical change.",
        ],
        "correct_index": 0,
        "explanation": r"Mixing $\text{NH}_4^+(aq)$ and $\text{OH}^-(aq)$ results in a Brønsted-Lowry acid-base reaction: $\text{NH}_4^+(aq) + \text{OH}^-(aq) \rightarrow \text{NH}_3(g) + \text{H}_2\text{O}(l)$. The evolved $\text{NH}_3(g)$ has a characteristic pungent odor and dissolves in the moisture on the red litmus paper to form $\text{OH}^-$, turning it blue.",
    },

    # -------------------------------------------------------------------------
    # 4.2 Net Ionic Equations (Q6 - Q11)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 6,
        "topic_code": "4.2",
        "topic_title": "Net Ionic Equations",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"When aqueous solutions of lead(II) nitrate, $\text{Pb(NO}_3)_2(aq)$, and sodium sulfate, $\text{Na}_2\text{SO}_4(aq)$, are mixed, a white precipitate forms. Which of the following is the balanced net ionic equation for the reaction?",
        "options": [
            r"$\text{Pb(NO}_3)_2(aq) + \text{Na}_2\text{SO}_4(aq) \rightarrow \text{PbSO}_4(s) + 2\text{NaNO}_3(aq)$",
            r"$\text{Pb}^{2+}(aq) + 2\text{NO}_3^-(aq) + 2\text{Na}^+(aq) + \text{SO}_4^{2-}(aq) \rightarrow \text{PbSO}_4(s) + 2\text{NaNO}_3(s)$",
            r"$\text{Na}^+(aq) + \text{NO}_3^-(aq) \rightarrow \text{NaNO}_3(s)$",
            r"$\text{Pb}^{2+}(aq) + \text{SO}_4^{2-}(aq) \rightarrow \text{PbSO}_4(s)$",
        ],
        "correct_index": 3,
        "explanation": r"All sodium and nitrate salts are soluble in water, so $\text{Na}^+(aq)$ and $\text{NO}_3^-(aq)$ are spectator ions, so the white precipitate must be lead(II) sulfate, $\text{PbSO}_4(s)$. Eliminating the spectator ions leaves the net ionic equation $\text{Pb}^{2+}(aq) + \text{SO}_4^{2-}(aq) \rightarrow \text{PbSO}_4(s)$.",
    },
    {
        "unit_q_num": 7,
        "topic_code": "4.2",
        "topic_title": "Net Ionic Equations",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"Aqueous hydrofluoric acid, $\text{HF}(aq)$ ($K_a = 6.8 \times 10^{-4}$), is neutralized by addition of aqueous potassium hydroxide, $\text{KOH}(aq)$. Which of the following is the correct net ionic equation for this reaction?",
        "options": [
            r"$\text{HF}(aq) + \text{OH}^-(aq) \rightarrow \text{F}^-(aq) + \text{H}_2\text{O}(l)$",
            r"$\text{H}^+(aq) + \text{OH}^-(aq) \rightarrow \text{H}_2\text{O}(l)$",
            r"$\text{HF}(aq) + \text{KOH}(aq) \rightarrow \text{KF}(s) + \text{H}_2\text{O}(l)$",
            r"$\text{H}^+(aq) + \text{F}^-(aq) + \text{K}^+(aq) + \text{OH}^-(aq) \rightarrow \text{KF}(aq) + \text{H}_2\text{O}(l)$",
        ],
        "correct_index": 0,
        "explanation": r"Because $\text{HF}$ is a weak acid ($K_a \ll 1$), it exists predominantly as unionized $\text{HF}(aq)$ molecules in aqueous solution and is written in molecular form in ionic equations. $\text{KOH}$ is a strong base that dissociates completely into $\text{K}^+(aq)$ and $\text{OH}^-(aq)$, and $\text{KF}$ is a soluble salt ($\text{K}^+(aq) + \text{F}^-(aq)$). Eliminating the spectator ion $\text{K}^+(aq)$ gives $\text{HF}(aq) + \text{OH}^-(aq) \rightarrow \text{F}^-(aq) + \text{H}_2\text{O}(l)$.",
    },
    {
        "unit_q_num": 8,
        "topic_code": "4.2",
        "topic_title": "Net Ionic Equations",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"When stoichiometric amounts of $0.10\text{ M }\text{Ba(OH)}_2(aq)$ and $0.10\text{ M }\text{H}_2\text{SO}_4(aq)$ are mixed, a white precipitate forms and the electrical conductivity of the resulting mixture drops to nearly zero. Which of the following balanced net ionic equations best explains this observation?",
        "options": [
            r"$\text{Ba}^{2+}(aq) + \text{SO}_4^{2-}(aq) \rightarrow \text{BaSO}_4(s)$",
            r"$\text{H}^+(aq) + \text{OH}^-(aq) \rightarrow \text{H}_2\text{O}(l)$",
            r"$\text{Ba}^{2+}(aq) + 2\text{OH}^-(aq) + 2\text{H}^+(aq) + \text{SO}_4^{2-}(aq) \rightarrow \text{BaSO}_4(s) + 2\text{H}_2\text{O}(l)$",
            r"$\text{Ba(OH)}_2(s) + 2\text{H}^+(aq) \rightarrow \text{Ba}^{2+}(aq) + 2\text{H}_2\text{O}(l)$",
        ],
        "correct_index": 2,
        "explanation": r"Both products—insoluble $\text{BaSO}_4(s)$ and weakly ionizing $\text{H}_2\text{O}(l)$—remove mobile ions from solution. Because neither $\text{Ba}^{2+}(aq)$, $\text{OH}^-(aq)$, $\text{H}^+(aq)$, nor $\text{SO}_4^{2-}(aq)$ remains in solution as a spectator ion, all four ions appear in the complete and net ionic equation: $\text{Ba}^{2+}(aq) + 2\text{OH}^-(aq) + 2\text{H}^+(aq) + \text{SO}_4^{2-}(aq) \rightarrow \text{BaSO}_4(s) + 2\text{H}_2\text{O}(l)$.",
    },
    {
        "unit_q_num": 9,
        "topic_code": "4.2",
        "topic_title": "Net Ionic Equations",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"Excess dilute nitric acid, $\text{HNO}_3(aq)$, is poured onto solid calcium carbonate, $\text{CaCO}_3(s)$, causing vigorous bubbling as the solid dissolves. What is the balanced net ionic equation for this reaction?",
        "options": [
            r"$\text{CO}_3^{2-}(aq) + 2\text{H}^+(aq) \rightarrow \text{H}_2\text{O}(l) + \text{CO}_2(g)$",
            r"$\text{Ca}^{2+}(aq) + 2\text{NO}_3^-(aq) \rightarrow \text{Ca(NO}_3)_2(s)$",
            r"$\text{CaCO}_3(s) + 2\text{HNO}_3(aq) \rightarrow \text{Ca(NO}_3)_2(s) + \text{H}_2\text{O}(l) + \text{CO}_2(g)$",
            r"$\text{CaCO}_3(s) + 2\text{H}^+(aq) \rightarrow \text{Ca}^{2+}(aq) + \text{H}_2\text{O}(l) + \text{CO}_2(g)$",
        ],
        "correct_index": 3,
        "explanation": r"Calcium carbonate is an insoluble solid and must be written intact as $\text{CaCO}_3(s)$ on the reactant side. Nitric acid is a strong acid ($\text{H}^+(aq) + \text{NO}_3^-(aq)$) and calcium nitrate is soluble ($\text{Ca}^{2+}(aq) + 2\text{NO}_3^-(aq)$). Canceling the spectator ion $\text{NO}_3^-(aq)$ gives $\text{CaCO}_3(s) + 2\text{H}^+(aq) \rightarrow \text{Ca}^{2+}(aq) + \text{H}_2\text{O}(l) + \text{CO}_2(g)$.",
    },
    {
        "unit_q_num": 10,
        "topic_code": "4.2",
        "topic_title": "Net Ionic Equations",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="equation-block">'
            r"$$2\text{Al}(s) + 3\text{CuCl}_2(aq) \rightarrow 2\text{AlCl}_3(aq) + 3\text{Cu}(s)$$"
            "</div>"
        ),
        "question": r"For the single-replacement reaction represented by the molecular equation above, what is the sum of the stoichiometric coefficients of all species in the properly balanced net ionic equation (written with lowest whole-number coefficients)?",
        "options": [
            r"$4$",
            r"$6$",
            r"$10$",
            r"$22$",
        ],
        "correct_index": 2,
        "explanation": r"In aqueous solution, $\text{CuCl}_2(aq)$ and $\text{AlCl}_3(aq)$ are soluble strong electrolytes, so $\text{Cl}^-(aq)$ is a spectator ion. The balanced net ionic equation is $2\text{Al}(s) + 3\text{Cu}^{2+}(aq) \rightarrow 2\text{Al}^{3+}(aq) + 3\text{Cu}(s)$. Summing the lowest whole-number coefficients gives $2 + 3 + 2 + 3 = 10$. Keeping the spectator ions, as in the complete ionic equation $2\text{Al}(s) + 3\text{Cu}^{2+}(aq) + 6\text{Cl}^-(aq) \rightarrow 2\text{Al}^{3+}(aq) + 6\text{Cl}^-(aq) + 3\text{Cu}(s)$, would give $22$; ignoring charge balance ($\text{Al} + \text{Cu}^{2+} \rightarrow \text{Al}^{3+} + \text{Cu}$) would give $4$.",
    },
    {
        "unit_q_num": 11,
        "topic_code": "4.2",
        "topic_title": "Net Ionic Equations",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"An aqueous solution of ammonium phosphate, $(\text{NH}_4)_3\text{PO}_4(aq)$, is mixed with an aqueous solution of calcium chloride, $\text{CaCl}_2(aq)$, producing a precipitate of calcium phosphate. Which ions are the spectator ions in this reaction?",
        "options": [
            r"$\text{Ca}^{2+}(aq)$ and $\text{PO}_4^{3-}(aq)$",
            r"$\text{NH}_4^+(aq)$ and $\text{PO}_4^{3-}(aq)$",
            r"$\text{Ca}^{2+}(aq)$ and $\text{Cl}^-(aq)$",
            r"$\text{NH}_4^+(aq)$ and $\text{Cl}^-(aq)$",
        ],
        "correct_index": 3,
        "explanation": r"All ammonium ($\text{NH}_4^+$) salts are soluble, and chloride ($\text{Cl}^-$) salts with $\text{Ca}^{2+}$ and $\text{NH}_4^+$ are soluble. Calcium phosphate, $\text{Ca}_3(\text{PO}_4)_2(s)$, precipitates via $3\text{Ca}^{2+}(aq) + 2\text{PO}_4^{3-}(aq) \rightarrow \text{Ca}_3(\text{PO}_4)_2(s)$, leaving $\text{NH}_4^+(aq)$ and $\text{Cl}^-(aq)$ unchanged in solution as spectator ions.",
    },

    # -------------------------------------------------------------------------
    # 4.3 Representations of Reactions (Q12 - Q17)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 12,
        "topic_code": "4.3",
        "topic_title": "Representations of Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Container State</th><th>Particulate Inventory</th></tr></thead>"
            "<tbody>"
            "<tr><td>Initial (Before Spark)</td><td>$6\\text{ molecules of }\\text{H}_2(g)$ and $4\\text{ molecules of }\\text{O}_2(g)$</td></tr>"
            "<tr><td>Final (After Complete Reaction)</td><td>$?$</td></tr>"
            "</tbody></table>"
        ),
        "question": r"A rigid reaction vessel initially contains the particulate inventory shown in the table above. After a spark initiates the reaction $2\text{H}_2(g) + \text{O}_2(g) \rightarrow 2\text{H}_2\text{O}(g)$ and the reaction goes to completion, which of the following accurately describes the particulate inventory in the vessel?",
        "options": [
            r"$6\text{ molecules of }\text{H}_2\text{O}(g)$ and $1\text{ molecule of }\text{O}_2(g)$",
            r"$6\text{ molecules of }\text{H}_2\text{O}(g)$ and $2\text{ molecules of }\text{O}_2(g)$",
            r"$8\text{ molecules of }\text{H}_2\text{O}(g)$ and $0\text{ molecules of }\text{H}_2(g)$",
            r"$4\text{ molecules of }\text{H}_2\text{O}(g)$ and $2\text{ molecules of }\text{H}_2(g)$",
        ],
        "correct_index": 0,
        "explanation": r"According to $2\text{H}_2(g) + \text{O}_2(g) \rightarrow 2\text{H}_2\text{O}(g)$, every $2\text{ molecules of }\text{H}_2$ react with $1\text{ molecule of }\text{O}_2$ to form $2\text{ molecules of }\text{H}_2\text{O}$. Therefore, $6\text{ molecules of }\text{H}_2$ (the limiting reactant) consume $3\text{ molecules of }\text{O}_2$ to produce $6\text{ molecules of }\text{H}_2\text{O}$, leaving $4 - 3 = 1\text{ molecule of }\text{O}_2$ in excess.",
    },
    {
        "unit_q_num": 13,
        "topic_code": "4.3",
        "topic_title": "Representations of Reactions",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Beaker</th><th>Initial Ions Represented in Particulate Diagram</th></tr></thead>"
            "<tbody>"
            "<tr><td>Beaker X ($\\text{AgNO}_3(aq)$)</td><td>$4\\text{ Ag}^+$ ions and $4\\text{ NO}_3^-$ ions</td></tr>"
            "<tr><td>Beaker Y ($\\text{CaCl}_2(aq)$)</td><td>$3\\text{ Ca}^{2+}$ ions and $6\\text{ Cl}^-$ ions</td></tr>"
            "</tbody></table>"
        ),
        "question": r"A student combines the contents of Beaker X and Beaker Y shown in the table above. Assuming $\text{AgCl}(s)$ is completely insoluble, which of the following correctly lists the species that should appear in the particulate diagram of the final mixture?",
        "options": [
            r"$2\text{ formula units of }\text{Ag}_2\text{Cl}_2(s)$ at the bottom, and $3\text{ Ca}^{2+}$ and $4\text{ NO}_3^-$ ions dissolved in solution",
            r"$6\text{ formula units of }\text{AgCl}(s)$ at the bottom, and $3\text{ Ca}^{2+}$ and $4\text{ NO}_3^-$ ions dissolved in solution",
            r"$4\text{ formula units of }\text{AgCl}(s)$ at the bottom, and $1\text{ Ca}^{2+}$ and $4\text{ NO}_3^-$ ions dissolved in solution",
            r"$4\text{ formula units of }\text{AgCl}(s)$ at the bottom, and $3\text{ Ca}^{2+}$, $4\text{ NO}_3^-$, and $2\text{ Cl}^-$ ions dissolved in solution",
        ],
        "correct_index": 3,
        "explanation": r"The net ionic reaction is $\text{Ag}^+(aq) + \text{Cl}^-(aq) \rightarrow \text{AgCl}(s)$. The $4\text{ Ag}^+$ ions are limiting and react with $4$ of the $6\text{ Cl}^-$ ions to form $4\text{ formula units of }\text{AgCl}(s)$ at the bottom of the beaker. In the supernatant solution, $6 - 4 = 2\text{ Cl}^-$ ions remain along with all $3\text{ Ca}^{2+}$ and $4\text{ NO}_3^-$ spectator ions (total positive charge $= 3(+2) = +6$; total negative charge $= 4(-1) + 2(-1) = -6$, preserving electroneutrality).",
    },
    {
        "unit_q_num": 14,
        "topic_code": "4.3",
        "topic_title": "Representations of Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"In a particulate representation of a sealed container before a reaction, there are $4\text{ molecules of }\text{N}_2(g)$ and $9\text{ molecules of }\text{H}_2(g)$. After the synthesis reaction $\text{N}_2(g) + 3\text{H}_2(g) \rightarrow 2\text{NH}_3(g)$ proceeds as far as possible toward completion, what is the ratio of $\text{NH}_3$ molecules to unreacted $\text{N}_2$ molecules in the container?",
        "options": [
            r"$2:1$",
            r"$3:1$",
            r"$6:1$",
            r"$8:1$",
        ],
        "correct_index": 2,
        "explanation": r"Since $1\text{ molecule of }\text{N}_2$ requires $3\text{ molecules of }\text{H}_2$, the $9\text{ molecules of }\text{H}_2$ are the limiting reactant and react completely with $3\text{ molecules of }\text{N}_2$ to form $3 \times 2 = 6\text{ molecules of }\text{NH}_3$. This leaves $4 - 3 = 1\text{ molecule of }\text{N}_2$ unreacted. The ratio of $\text{NH}_3$ molecules to unreacted $\text{N}_2$ molecules is $6:1$.",
    },
    {
        "unit_q_num": 15,
        "topic_code": "4.3",
        "topic_title": "Representations of Reactions",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"A student draws a particulate diagram representing the reaction between solid magnesium and aqueous hydrochloric acid: $\text{Mg}(s) + 2\text{HCl}(aq) \rightarrow \text{MgCl}_2(aq) + \text{H}_2(g)$. In the 'before reaction' diagram, the student draws $2\text{ Mg}$ atoms in a solid lattice and $4\text{ H}^+(aq)$ ions plus $4\text{ Cl}^-(aq)$ ions in solution. Which of the following features in the 'after reaction' diagram would represent a conceptual error?",
        "options": [
            r"Drawing $2\text{ H}_2(g)$ diatomic molecules escaping as gas bubbles above the solution",
            r"Drawing $2\text{ Mg}^{2+}(aq)$ ions and $4\text{ Cl}^-(aq)$ ions dispersed as separated, hydrated ions in the solution",
            r"Drawing $2\text{ discrete }\text{MgCl}_2$ neutral triatomic molecules bonded together and floating in the aqueous phase",
            r"Omitting the solid $\text{Mg}$ lattice because all $2\text{ Mg}$ atoms reacted completely with the $4\text{ H}^+(aq)$ ions",
        ],
        "correct_index": 2,
        "explanation": r"Magnesium chloride, $\text{MgCl}_2(aq)$, is a soluble strong electrolyte that exists in aqueous solution as separated, hydrated $\text{Mg}^{2+}(aq)$ and $\text{Cl}^-(aq)$ ions, not as discrete neutral covalent $\text{MgCl}_2$ molecules.",
    },
    {
        "unit_q_num": 16,
        "topic_code": "4.3",
        "topic_title": "Representations of Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Time</th><th>Molecules of $\\text{X}_2$</th><th>Molecules of $\\text{Y}_2$</th><th>Molecules of $\\text{X}_2\\text{Y}$</th></tr></thead>"
            "<tbody>"
            "<tr><td>$t = 0\\text{ s}$</td><td>$10$</td><td>$6$</td><td>$0$</td></tr>"
            "<tr><td>$t = t_{\\text{final}}$</td><td>$2$</td><td>$2$</td><td>$8$</td></tr>"
            "</tbody></table>"
        ),
        "question": r"The table above shows the number of molecules in a closed reaction vessel before and after a reaction between diatomic gases $\text{X}_2$ and $\text{Y}_2$. Does the final state at $t = t_{\text{final}}$ represent a reaction that has gone to completion, or a system where both reactants remain even though more product could stoichiometrically form?",
        "options": [
            r"The reaction has gone to completion because $\text{X}_2$ and $\text{Y}_2$ are left in a $1:1$ ratio.",
            r"The reaction did not go to completion; the balanced equation is $2\text{X}_2 + \text{Y}_2 \rightarrow 2\text{X}_2\text{Y}$, so the remaining $2\text{ molecules of }\text{X}_2$ could react with $1\text{ molecule of }\text{Y}_2$ to form $2\text{ more molecules of }\text{X}_2\text{Y}$.",
            r"The table violates conservation of atoms because $16\text{ reactant molecules}$ produced only $12\text{ total molecules}$.",
            r"The balanced equation is $\text{X}_2 + \text{Y}_2 \rightarrow \text{X}_2\text{Y}$, which violates conservation of mass.",
        ],
        "correct_index": 1,
        "explanation": r"Between $t = 0$ and $t_{\text{final}}$, $\Delta N(\text{X}_2) = -8$, $\Delta N(\text{Y}_2) = -4$, and $\Delta N(\text{X}_2\text{Y}) = +8$, which corresponds to the balanced equation $2\text{X}_2 + \text{Y}_2 \rightarrow 2\text{X}_2\text{Y}$ (conserving $16\text{ X}$ atoms and $8\text{ Y}$ atoms). Because both $2\text{ X}_2$ and $2\text{ Y}_2$ remain, the reaction stopped prior to completion (e.g., reached equilibrium); complete reaction of the limiting reactant $\text{X}_2$ would leave $0\text{ X}_2$, $1\text{ Y}_2$, and $10\text{ X}_2\text{Y}$.",
    },
    {
        "unit_q_num": 17,
        "topic_code": "4.3",
        "topic_title": "Representations of Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A particulate diagram shows $3\text{ molecules of }\text{CH}_4(g)$ and $8\text{ molecules of }\text{O}_2(g)$ before combustion. Which of the following particulate counts accurately represents the system after complete combustion to $\text{CO}_2(g)$ and $\text{H}_2\text{O}(g)$?",
        "options": [
            r"$3\text{ CO}_2$, $6\text{ H}_2\text{O}$, and $2\text{ O}_2$",
            r"$3\text{ CO}_2$, $3\text{ H}_2\text{O}$, and $3.5\text{ O}_2$",
            r"$4\text{ CO}_2$, $8\text{ H}_2\text{O}$, and $0\text{ O}_2$",
            r"$3\text{ CO}_2$, $6\text{ H}_2\text{O}$, and $5\text{ O}_2$",
        ],
        "correct_index": 0,
        "explanation": r"The balanced combustion equation is $\text{CH}_4(g) + 2\text{O}_2(g) \rightarrow \text{CO}_2(g) + 2\text{H}_2\text{O}(g)$. Three molecules of $\text{CH}_4$ require $3 \times 2 = 6\text{ molecules of }\text{O}_2$, producing $3\text{ molecules of }\text{CO}_2$ and $3 \times 2 = 6\text{ molecules of }\text{H}_2\text{O}$, with $8 - 6 = 2\text{ molecules of }\text{O}_2$ left over.",
    },

    # -------------------------------------------------------------------------
    # 4.4 Physical and Chemical Changes (Q18 - Q22)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 18,
        "topic_code": "4.4",
        "topic_title": "Physical and Chemical Changes",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"Which of the following processes involves breaking only intermolecular attractions (London dispersion forces, dipole-dipole interactions, or hydrogen bonds) without breaking any covalent or ionic bonds?",
        "options": [
            r"Electrolysis of liquid water, $\text{H}_2\text{O}(l)$, into $\text{H}_2(g)$ and $\text{O}_2(g)$",
            r"Sublimation of solid carbon dioxide, $\text{CO}_2(s)$, into gaseous carbon dioxide, $\text{CO}_2(g)$",
            r"Dissolution of solid sodium chloride, $\text{NaCl}(s)$, into $\text{Na}^+(aq)$ and $\text{Cl}^-(aq)$ in water",
            r"Thermal decomposition of solid potassium chlorate, $\text{KClO}_3(s)$, into $\text{KCl}(s)$ and $\text{O}_2(g)$",
        ],
        "correct_index": 1,
        "explanation": r"Sublimation of dry ice ($\text{CO}_2(s) \rightarrow \text{CO}_2(g)$) overcomes only the weak London dispersion forces between discrete $\text{CO}_2$ molecules while leaving the intramolecular $\text{C}=\text{O}$ double bonds completely intact. Electrolysis and thermal decomposition break covalent bonds, and dissolving $\text{NaCl}(s)$ breaks ionic bonds in the crystal lattice.",
    },
    {
        "unit_q_num": 19,
        "topic_code": "4.4",
        "topic_title": "Physical and Chemical Changes",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"Dissolving solid ammonium chloride, $\text{NH}_4\text{Cl}(s)$, in water is sometimes classified as a physical change because evaporation of the water recovers $\text{NH}_4\text{Cl}(s)$, yet it also exhibits characteristics of a chemical process. Which of the following best justifies why the dissolution of $\text{NH}_4\text{Cl}(s)$ has both physical and chemical aspects at the particulate level?",
        "options": [
            r"Covalent $\text{N}-\text{H}$ bonds within the $\text{NH}_4^+$ ion are completely broken to form $\text{N}_2(g)$ and $\text{H}_2(g)$ upon dissolution.",
            r"Water molecules undergo oxidation by $\text{Cl}^-$ ions to form hypochlorous acid.",
            r"Only weak London dispersion forces between $\text{NH}_4\text{Cl}$ molecules are disrupted during dissolution.",
            r"Strong ionic attractions between $\text{NH}_4^+$ and $\text{Cl}^-$ in the crystal lattice are broken and replaced by ion-dipole attractions with water molecules, even though the identities of the polyatomic and monatomic ions are preserved upon recrystallization.",
        ],
        "correct_index": 3,
        "explanation": r"AP Chemistry emphasizes that the dissolution of a salt involves breaking strong electrostatic (ionic) bonds in the lattice and forming new ion-dipole interactions (hydration shells)—a bond-breaking/interaction-forming aspect similar to chemical changes—even though evaporating the solvent regenerates the original ionic solid.",
    },
    {
        "unit_q_num": 20,
        "topic_code": "4.4",
        "topic_title": "Physical and Chemical Changes",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Process</th><th>Equation</th><th>$\\Delta H^\\circ\\text{ (kJ/mol)}_{\\text{rxn}}$</th></tr></thead>"
            "<tbody>"
            "<tr><td>Process I</td><td>$\\text{H}_2\\text{O}(l) \\rightarrow \\text{H}_2\\text{O}(g)$</td><td>$+44.0$</td></tr>"
            "<tr><td>Process II</td><td>$\\text{H}_2\\text{O}(l) \\rightarrow \\text{H}_2(g) + \\frac{1}{2}\\text{O}_2(g)$</td><td>$+285.8$</td></tr>"
            "</tbody></table>"
        ),
        "question": r"The table above compares two endothermic processes involving liquid water. Why is the enthalpy change for Process II more than six times greater than the enthalpy change for Process I?",
        "options": [
            r"Process I breaks covalent $\text{O}-\text{H}$ bonds, whereas Process II breaks both covalent $\text{O}-\text{H}$ bonds and hydrogen bonds.",
            r"Process I overcomes intermolecular hydrogen bonds between $\text{H}_2\text{O}$ molecules, whereas Process II breaks much stronger intramolecular polar covalent $\text{O}-\text{H}$ bonds to form new substances.",
            r"Process II produces gases with higher molar masses than $\text{H}_2\text{O}(g)$.",
            r"Process I occurs only at $100^\circ\text{C}$, whereas Process II occurs only at absolute zero.",
        ],
        "correct_index": 1,
        "explanation": r"Process I is vaporization (a physical phase change), which only requires enough energy ($44.0\text{ kJ/mol}$) to overcome intermolecular hydrogen bonding and dipole-dipole/dispersion forces between intact $\text{H}_2\text{O}$ molecules. Process II is chemical decomposition, which requires breaking strong intramolecular $\text{O}-\text{H}$ covalent bonds ($\sim 463\text{ kJ/mol}$ per bond, partially offset by forming $\text{H}-\text{H}$ and $\text{O}=\text{O}$ bonds).",
    },
    {
        "unit_q_num": 21,
        "topic_code": "4.4",
        "topic_title": "Physical and Chemical Changes",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"When anhydrous copper(II) sulfate, a white crystalline solid with formula $\text{CuSO}_4(s)$, is exposed to water vapor, it turns bright blue and forms copper(II) sulfate pentahydrate, $\text{CuSO}_4\cdot 5\text{H}_2\text{O}(s)$. Why is this transformation classified as a chemical change rather than merely a physical wetting of the solid?",
        "options": [
            r"Water molecules become bonded to the ions within a new crystal structure, forming a new substance with a fixed composition ($5\text{ mol H}_2\text{O}$ per mol of $\text{CuSO}_4$) and different properties, such as its blue color.",
            r"The sulfate ion $\text{SO}_4^{2-}$ is reduced to elemental sulfur $\text{S}_8(s)$.",
            r"The copper(II) ion $\text{Cu}^{2+}$ is reduced to metallic $\text{Cu}(s)$ by water.",
            r"Liquid water condenses physically on the surface without interacting with the ions in the lattice.",
        ],
        "correct_index": 0,
        "explanation": r"In the pentahydrate, water molecules are bonded to the $\text{Cu}^{2+}$ ions within a new crystal structure, in a fixed $5:1$ mole ratio of $\text{H}_2\text{O}$ to $\text{CuSO}_4$. The formation of new bonds and of a new substance with a definite composition and different properties, signaled by the color change from white to blue, is evidence of a chemical change. Water merely condensing on the surface without interacting with the ions would not change the composition or the color of the solid. Neither $\text{Cu}$ nor $\text{S}$ changes oxidation number, so no reduction to $\text{Cu}(s)$ or $\text{S}_8(s)$ occurs.",
    },
    {
        "unit_q_num": 22,
        "topic_code": "4.4",
        "topic_title": "Physical and Chemical Changes",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A student passes an electric current through molten magnesium chloride, $\text{MgCl}_2(l)$, using inert graphite electrodes. Silvery liquid metal forms at the cathode and a greenish-yellow gas bubbles off at the anode. Which statement accurately describes this process?",
        "options": [
            r"It is a physical separation because heating melted the $\text{MgCl}_2$ prior to electrolysis.",
            r"It is a chemical change in which water is decomposed into $\text{H}_2(g)$ and $\text{O}_2(g)$.",
            r"It is a physical phase change in which $\text{MgCl}_2(l)$ boils into $\text{MgCl}_2(g)$.",
            r"It is a chemical change in which ionic bonds are broken and electron transfer produces elemental $\text{Mg}(l)$ and covalent $\text{Cl}_2(g)$ molecules.",
        ],
        "correct_index": 3,
        "explanation": r"Electrolysis of molten $\text{MgCl}_2(l)$ transfers electrons from $\text{Cl}^-$ to $\text{Mg}^{2+}$ ($\text{MgCl}_2(l) \rightarrow \text{Mg}(l) + \text{Cl}_2(g)$), transforming an ionic compound into two distinct elements with metallic and covalent bonding—a quintessential chemical change.",
    },

    # -------------------------------------------------------------------------
    # 4.5 Stoichiometry (Q23 - Q28)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 23,
        "topic_code": "4.5",
        "topic_title": "Stoichiometry",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="equation-block">'
            r"$$\text{Fe}_2\text{O}_3(s) + 2\text{Al}(s) \rightarrow \text{Al}_2\text{O}_3(s) + 2\text{Fe}(l)$$"
            "</div>"
        ),
        "question": r"In the thermite reaction shown above, $32.0\text{ g}$ of $\text{Fe}_2\text{O}_3$ ($\text{molar mass } 159.7\text{ g/mol}$) is mixed with $13.5\text{ g}$ of $\text{Al}$ ($\text{molar mass } 27.0\text{ g/mol}$) and ignited. What is the maximum mass of molten $\text{Fe}$ ($\text{molar mass } 55.85\text{ g/mol}$) that can be produced, and which reactant is in excess?",
        "options": [
            r"$22.4\text{ g of Fe}$; $\text{Al}$ is in excess by $2.7\text{ g}$",
            r"$27.9\text{ g of Fe}$; $\text{Fe}_2\text{O}_3$ is in excess by $8.0\text{ g}$",
            r"$11.2\text{ g of Fe}$; $\text{Al}$ is in excess by $8.1\text{ g}$",
            r"$22.4\text{ g of Fe}$; $\text{Fe}_2\text{O}_3$ is in excess by $5.4\text{ g}$",
        ],
        "correct_index": 0,
        "explanation": r"Moles of $\text{Fe}_2\text{O}_3 = \frac{32.0\text{ g}}{159.7\text{ g/mol}} = 0.2004\text{ mol}$. Moles of $\text{Al} = \frac{13.5\text{ g}}{27.0\text{ g/mol}} = 0.500\text{ mol}$. Since $1\text{ mol }\text{Fe}_2\text{O}_3$ requires $2\text{ mol }\text{Al}$, $0.2004\text{ mol }\text{Fe}_2\text{O}_3$ requires $0.4008\text{ mol }\text{Al}$, which is less than the $0.500\text{ mol}$ available. Thus $\text{Fe}_2\text{O}_3$ is the limiting reactant, producing $2 \times 0.2004 = 0.4008\text{ mol Fe}$, and $0.4008\text{ mol} \times 55.85\text{ g/mol} = 22.4\text{ g Fe}$. Excess $\text{Al} = (0.500 - 0.4008)\text{ mol} \times 27.0\text{ g/mol} = 2.68\text{ g} \approx 2.7\text{ g}$.",
    },
    {
        "unit_q_num": 24,
        "topic_code": "4.5",
        "topic_title": "Stoichiometry",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Measurement</th><th>Mass (g)</th></tr></thead>"
            "<tbody>"
            "<tr><td>Mass of impure $\\text{NaCl}$ + $\\text{KNO}_3$ mixture dissolved in water</td><td>$2.500\\text{ g}$</td></tr>"
            "<tr><td>Mass of clean, dry filter paper</td><td>$0.812\\text{ g}$</td></tr>"
            "<tr><td>Mass of filter paper + dried $\\text{AgCl}(s)$ precipitate (after washing)</td><td>$3.680\\text{ g}$</td></tr>"
            "</tbody></table>"
        ),
        "question": r"A student performs a gravimetric analysis to determine the mass percent of $\text{NaCl}$ ($\text{molar mass } 58.44\text{ g/mol}$) in an impure mixture containing only $\text{NaCl}$ and $\text{KNO}_3$. The student dissolves $2.500\text{ g}$ of the mixture in water and adds excess $\text{AgNO}_3(aq)$ to precipitate all chloride ions as $\text{AgCl}(s)$ ($\text{molar mass } 143.32\text{ g/mol}$). Based on the data table above, what is the mass percent of $\text{NaCl}$ in the original mixture?",
        "options": [
            r"$23.4\%$",
            r"$46.8\%$",
            r"$57.3\%$",
            r"$93.5\%$",
        ],
        "correct_index": 1,
        "explanation": r"Mass of $\text{AgCl}(s) = 3.680\text{ g} - 0.812\text{ g} = 2.868\text{ g}$. Moles of $\text{AgCl} = \frac{2.868\text{ g}}{143.32\text{ g/mol}} = 0.02001\text{ mol}$. By $1:1$ stoichiometry of $\text{Cl}^-$, moles of $\text{NaCl} = 0.02001\text{ mol}$. Mass of $\text{NaCl} = 0.02001\text{ mol} \times 58.44\text{ g/mol} = 1.169\text{ g}$. Mass percent of $\text{NaCl} = \frac{1.169\text{ g}}{2.500\text{ g}} \times 100\% = 46.8\%$.",
    },
    {
        "unit_q_num": 25,
        "topic_code": "4.5",
        "topic_title": "Stoichiometry",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"In the gravimetric analysis of chloride by precipitation of $\text{AgCl}(s)$, a student forgets to rinse the collected precipitate on the filter paper with distilled water before drying and weighing it, and also removes the precipitate from the oven before it is completely dry. How would these procedural errors affect the calculated mass percent of $\text{Cl}^-$ in the unknown sample?",
        "options": [
            r"It would be artificially high because both residual mother liquor salts and trapped water increase the apparent mass of $\text{AgCl}(s)$.",
            r"It would be artificially low because residual $\text{AgNO}_3$ reacts with $\text{AgCl}(s)$ to form a volatile gas.",
            r"The two errors would cancel out because unwashed ions decrease the mass while residual water increases the mass.",
            r"It would be unaffected because only $\text{AgCl}(s)$ contributes to the molar mass used in the stoichiometric calculation.",
        ],
        "correct_index": 0,
        "explanation": r"Both failing to wash away soluble spectator ions/excess $\text{AgNO}_3$ and failing to dry the precipitate completely leave extra mass on the filter paper. The student attributes this inflated mass entirely to $\text{AgCl}(s)$, calculating too many moles of $\text{Cl}^-$ and an artificially high mass percent.",
    },
    {
        "unit_q_num": 26,
        "topic_code": "4.5",
        "topic_title": "Stoichiometry",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="equation-block">'
            r"$$2\text{KClO}_3(s) \xrightarrow{\Delta, \text{ MnO}_2} 2\text{KCl}(s) + 3\text{O}_2(g)$$"
            "</div>"
        ),
        "question": r"When $12.25\text{ g}$ of solid potassium chlorate, $\text{KClO}_3$ ($\text{molar mass } 122.55\text{ g/mol}$), is heated in the presence of a $\text{MnO}_2$ catalyst, the oxygen gas produced is collected at $273\text{ K}$ and $1.00\text{ atm}$ (where the molar volume of an ideal gas is $22.4\text{ L/mol}$). If $2.69\text{ L}$ of $\text{O}_2(g)$ is actually collected, what is the percent yield of the reaction?",
        "options": [
            r"$60.0\%$",
            r"$75.0\%$",
            r"$80.1\%$",
            r"$90.0\%$",
        ],
        "correct_index": 2,
        "explanation": r"Moles of $\text{KClO}_3 = \frac{12.25\text{ g}}{122.55\text{ g/mol}} = 0.1000\text{ mol}$. By the $2:3$ stoichiometric ratio, theoretical moles of $\text{O}_2(g) = 0.1000\text{ mol} \times \frac{3}{2} = 0.1500\text{ mol}$. At STP ($22.4\text{ L/mol}$), theoretical volume of $\text{O}_2 = 0.1500\text{ mol} \times 22.4\text{ L/mol} = 3.36\text{ L}$. Percent yield $= \frac{2.69\text{ L}}{3.36\text{ L}} \times 100\% = 80.1\%$.",
    },
    {
        "unit_q_num": 27,
        "topic_code": "4.5",
        "topic_title": "Stoichiometry",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"Exactly $40.0\text{ mL}$ of $0.300\text{ M }\text{Pb(NO}_3)_2(aq)$ is mixed with $60.0\text{ mL}$ of $0.300\text{ M }\text{NaCl}(aq)$, precipitating $\text{PbCl}_2(s)$ according to $\text{Pb}^{2+}(aq) + 2\text{Cl}^-(aq) \rightarrow \text{PbCl}_2(s)$. Assuming the volumes are additive and $\text{PbCl}_2(s)$ has negligible solubility, what are the final concentrations of $\text{Pb}^{2+}(aq)$ and $\text{NO}_3^-(aq)$ in the $100.0\text{ mL}$ solution after precipitation is complete?",
        "options": [
            r"$[\text{Pb}^{2+}] = 0.0300\text{ M}$ and $[\text{NO}_3^-] = 0.240\text{ M}$",
            r"$[\text{Pb}^{2+}] = 0.000\text{ M}$ and $[\text{NO}_3^-] = 0.120\text{ M}$",
            r"$[\text{Pb}^{2+}] = 0.0600\text{ M}$ and $[\text{NO}_3^-] = 0.240\text{ M}$",
            r"$[\text{Pb}^{2+}] = 0.0300\text{ M}$ and $[\text{NO}_3^-] = 0.120\text{ M}$",
        ],
        "correct_index": 0,
        "explanation": r"Initial moles: $n(\text{Pb}^{2+}) = 0.0400\text{ L} \times 0.300\text{ M} = 0.0120\text{ mol}$; $n(\text{NO}_3^-) = 2 \times 0.0120 = 0.0240\text{ mol}$; $n(\text{Cl}^-) = 0.0600\text{ L} \times 0.300\text{ M} = 0.0180\text{ mol}$. Since $1\text{ mol }\text{Pb}^{2+}$ requires $2\text{ mol }\text{Cl}^-$, $\text{Cl}^-$ is limiting and consumes $\frac{0.0180}{2} = 0.0090\text{ mol }\text{Pb}^{2+}$. Remaining $n(\text{Pb}^{2+}) = 0.0120 - 0.0090 = 0.0030\text{ mol}$ in $0.1000\text{ L}$, so $[\text{Pb}^{2+}] = 0.0300\text{ M}$. Nitrate is a spectator ion: $[\text{NO}_3^-] = \frac{0.0240\text{ mol}}{0.1000\text{ L}} = 0.240\text{ M}$.",
    },
    {
        "unit_q_num": 28,
        "topic_code": "4.5",
        "topic_title": "Stoichiometry",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Stage of Heating</th><th>Mass of Crucible + Contents (g)</th></tr></thead>"
            "<tbody>"
            "<tr><td>Empty crucible</td><td>$15.000\\text{ g}$</td></tr>"
            "<tr><td>Crucible + pure $\\text{CaCO}_3(s)$ before heating</td><td>$20.005\\text{ g}$</td></tr>"
            "<tr><td>Crucible + solid residue after $10\\text{ min}$ of heating</td><td>$18.525\\text{ g}$</td></tr>"
            "</tbody></table>"
        ),
        "question": r"A student heats $5.005\text{ g}$ of pure $\text{CaCO}_3(s)$ ($\text{molar mass } 100.1\text{ g/mol}$) in an open crucible to decompose it according to $\text{CaCO}_3(s) \rightarrow \text{CaO}(s) + \text{CO}_2(g)$. Using the data in the table above ($\text{molar mass of }\text{CO}_2 = 44.01\text{ g/mol}$), what percentage of the initial $\text{CaCO}_3(s)$ has decomposed after $10\text{ minutes}$ of heating?",
        "options": [
            r"$29.6\%$",
            r"$67.3\%$",
            r"$70.4\%$",
            r"$100\%$",
        ],
        "correct_index": 1,
        "explanation": r"The mass lost from the open crucible is entirely escaped $\text{CO}_2(g)$: $m(\text{CO}_2) = 20.005\text{ g} - 18.525\text{ g} = 1.480\text{ g}$. Moles of $\text{CO}_2$ evolved $= \frac{1.480\text{ g}}{44.01\text{ g/mol}} = 0.03363\text{ mol}$, which equals the moles of $\text{CaCO}_3$ decomposed. Initial moles of $\text{CaCO}_3 = \frac{5.005\text{ g}}{100.1\text{ g/mol}} = 0.05000\text{ mol}$. Percent decomposed $= \frac{0.03363\text{ mol}}{0.05000\text{ mol}} \times 100\% = 67.3\%$.",
    },

    # -------------------------------------------------------------------------
    # 4.6 Introduction to Titration (Q29 - Q34)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 29,
        "topic_code": "4.6",
        "topic_title": "Introduction to Titration",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Measurement</th><th>Value</th></tr></thead>"
            "<tbody>"
            "<tr><td>Volume of diprotic acid $\\text{H}_2\\text{A}(aq)$ pipetted into flask</td><td>$25.00\\text{ mL}$</td></tr>"
            "<tr><td>Concentration of standardized $\\text{NaOH}(aq)$ titrant</td><td>$0.150\\text{ M}$</td></tr>"
            "<tr><td>Initial buret reading of $\\text{NaOH}(aq)$</td><td>$1.20\\text{ mL}$</td></tr>"
            "<tr><td>Final buret reading at second equivalence point</td><td>$34.53\\text{ mL}$</td></tr>"
            "</tbody></table>"
        ),
        "question": r"A student titrates a $25.00\text{ mL}$ aliquot of an unknown diprotic acid, $\text{H}_2\text{A}(aq)$, with standardized $0.150\text{ M }\text{NaOH}(aq)$ according to the reaction $\text{H}_2\text{A}(aq) + 2\text{NaOH}(aq) \rightarrow \text{Na}_2\text{A}(aq) + 2\text{H}_2\text{O}(l)$. Based on the titration data above, what is the molar concentration of the $\text{H}_2\text{A}(aq)$ solution?",
        "options": [
            r"$0.100\text{ M}$",
            r"$0.200\text{ M}$",
            r"$0.300\text{ M}$",
            r"$0.400\text{ M}$",
        ],
        "correct_index": 0,
        "explanation": r"Volume of $\text{NaOH}$ delivered $= 34.53\text{ mL} - 1.20\text{ mL} = 33.33\text{ mL} = 0.03333\text{ L}$. Moles of $\text{NaOH} = 0.03333\text{ L} \times 0.150\text{ M} = 0.00500\text{ mol}$. Since $1\text{ mol }\text{H}_2\text{A}$ reacts with $2\text{ mol }\text{NaOH}$, moles of $\text{H}_2\text{A} = \frac{0.00500\text{ mol}}{2} = 0.00250\text{ mol}$. Concentration $[\text{H}_2\text{A}] = \frac{0.00250\text{ mol}}{0.02500\text{ L}} = 0.100\text{ M}$.",
    },
    {
        "unit_q_num": 30,
        "topic_code": "4.6",
        "topic_title": "Introduction to Titration",
        "difficulty": "Challenging",
        "stimulus": (
            '<div class="equation-block">'
            r"$$\text{MnO}_4^-(aq) + 5\text{Fe}^{2+}(aq) + 8\text{H}^+(aq) \rightarrow \text{Mn}^{2+}(aq) + 5\text{Fe}^{3+}(aq) + 4\text{H}_2\text{O}(l)$$"
            "</div>"
        ),
        "question": r"An acidified solution containing $\text{Fe}^{2+}(aq)$ is titrated with standardized $0.0200\text{ M }\text{KMnO}_4(aq)$ according to the balanced net ionic equation above. If $20.00\text{ mL}$ of the $\text{Fe}^{2+}(aq)$ solution requires $16.00\text{ mL}$ of $0.0200\text{ M }\text{KMnO}_4(aq)$ to reach the persistent faint pink endpoint, what is the molarity of $\text{Fe}^{2+}(aq)$ in the original $20.00\text{ mL}$ sample?",
        "options": [
            r"$0.00320\text{ M}$",
            r"$0.0160\text{ M}$",
            r"$0.0800\text{ M}$",
            r"$0.125\text{ M}$",
        ],
        "correct_index": 2,
        "explanation": r"Moles of $\text{MnO}_4^-$ added $= 0.01600\text{ L} \times 0.0200\text{ M} = 3.20 \times 10^{-4}\text{ mol}$. From the $1:5$ mole ratio, moles of $\text{Fe}^{2+} = 5 \times (3.20 \times 10^{-4}\text{ mol}) = 1.60 \times 10^{-3}\text{ mol}$. Molarity of $\text{Fe}^{2+} = \frac{1.60 \times 10^{-3}\text{ mol}}{0.02000\text{ L}} = 0.0800\text{ M}$.",
    },
    {
        "unit_q_num": 31,
        "topic_code": "4.6",
        "topic_title": "Introduction to Titration",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"Which of the following best distinguishes the equivalence point of a titration from the endpoint of a titration?",
        "options": [
            r"The equivalence point occurs when the pH of the solution equals $7.00$, whereas the endpoint occurs when all indicator molecules have precipitated.",
            r"The equivalence point is the theoretical point at which stoichiometric quantities of titrant and analyte have reacted completely, whereas the endpoint is the experimental point at which an indicator or sensor shows a detectable physical change.",
            r"The endpoint always occurs at half the volume of titrant required to reach the equivalence point.",
            r"The equivalence point depends on the choice of acid-base indicator, whereas the endpoint is independent of the indicator used.",
        ],
        "correct_index": 1,
        "explanation": r"The equivalence point is defined strictly by reaction stoichiometry (when moles of titrant added are stoichiometrically equivalent to moles of analyte initially present), whereas the endpoint is the experimentally observed signal (such as an indicator color change) used to estimate the equivalence point.",
    },
    {
        "unit_q_num": 32,
        "topic_code": "4.6",
        "topic_title": "Introduction to Titration",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"Before filling a buret with standardized $0.100\text{ M }\text{NaOH}(aq)$ to titrate a $25.00\text{ mL}$ sample of unknown $\text{HCl}(aq)$ in an Erlenmeyer flask, a student rinses the buret with distilled water but forgets to condition (rinse) the buret with the $0.100\text{ M }\text{NaOH}(aq)$ titrant. Additionally, the student rinses the Erlenmeyer flask with distilled water right before pipetting the $25.00\text{ mL}$ of $\text{HCl}(aq)$ into it. How do these two actions affect the calculated concentration of $\text{HCl}(aq)$?",
        "options": [
            r"Both actions cause the calculated $[\text{HCl}]$ to be artificially low.",
            r"Both actions cause the calculated $[\text{HCl}]$ to be artificially high.",
            r"Failing to rinse the buret with $\text{NaOH}(aq)$ dilutes the titrant and makes the calculated $[\text{HCl}]$ artificially high, whereas residual distilled water in the Erlenmeyer flask does not change the moles of $\text{HCl}$ and has no effect on the calculated $[\text{HCl}]$.",
            r"Failing to rinse the buret with $\text{NaOH}(aq)$ has no effect, whereas residual water in the Erlenmeyer flask dilutes the $\text{HCl}$ and makes the calculated $[\text{HCl}]$ artificially low.",
        ],
        "correct_index": 2,
        "explanation": r"Water left in the buret dilutes the $\text{NaOH}(aq)$ titrant, so a larger volume of titrant is needed to deliver the required moles of $\text{OH}^-$, leading to an overestimated mole count and artificially high calculated $[\text{HCl}]$. Conversely, distilled water in the receiving Erlenmeyer flask does not alter the exact moles of $\text{HCl}$ delivered by the $25.00\text{ mL}$ pipet, so it does not affect the equivalence volume.",
    },
    {
        "unit_q_num": 33,
        "topic_code": "4.6",
        "topic_title": "Introduction to Titration",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"A $0.510\text{ g}$ sample of a pure solid monoprotic acid, $\text{HA}$, is dissolved in distilled water and titrated to the phenolphthalein endpoint with $25.0\text{ mL}$ of $0.100\text{ M }\text{NaOH}(aq)$. What is the molar mass of the monoprotic acid $\text{HA}$?",
        "options": [
            r"$102\text{ g/mol}$",
            r"$128\text{ g/mol}$",
            r"$204\text{ g/mol}$",
            r"$408\text{ g/mol}$",
        ],
        "correct_index": 2,
        "explanation": r"At the equivalence point for a monoprotic acid ($\text{HA} + \text{OH}^- \rightarrow \text{A}^- + \text{H}_2\text{O}$), $n(\text{HA}) = n(\text{NaOH}) = 0.0250\text{ L} \times 0.100\text{ M} = 0.00250\text{ mol}$. Therefore, the molar mass is $\mathcal{M} = \frac{0.510\text{ g}}{0.00250\text{ mol}} = 204\text{ g/mol}$ (which corresponds to potassium hydrogen phthalate, KHP).",
    },
    {
        "unit_q_num": 34,
        "topic_code": "4.6",
        "topic_title": "Introduction to Titration",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Volume of $0.10\\text{ M }\\text{AgNO}_3(aq)$ Added (mL)</th><th>Conductivity of Mixture (Relative Units)</th></tr></thead>"
            "<tbody>"
            "<tr><td>$0.0$</td><td>$120$</td></tr>"
            "<tr><td>$10.0$</td><td>$89$</td></tr>"
            "<tr><td>$20.0$</td><td>$70$</td></tr>"
            "<tr><td>$30.0$</td><td>$58$</td></tr>"
            "<tr><td>$40.0$</td><td>$68$</td></tr>"
            "<tr><td>$50.0$</td><td>$75$</td></tr>"
            "</tbody></table>"
        ),
        "question": r"A $30.0\text{ mL}$ sample of $\text{NaCl}(aq)$ of unknown concentration is titrated with $0.10\text{ M }\text{AgNO}_3(aq)$ while monitoring the electrical conductivity of the solution, as shown in the table above ($\text{Ag}^+(aq) + \text{Cl}^-(aq) \rightarrow \text{AgCl}(s)$). Based on the conductivity data, what is the approximate concentration of the original $30.0\text{ mL }\text{NaCl}(aq)$ solution?",
        "options": [
            r"$0.050\text{ M}$",
            r"$0.10\text{ M}$",
            r"$0.20\text{ M}$",
            r"$0.30\text{ M}$",
        ],
        "correct_index": 1,
        "explanation": r"Before the equivalence point, each $\text{Cl}^-(aq)$ ion removed as $\text{AgCl}(s)$ is replaced by an $\text{NO}_3^-(aq)$ ion, so the number of ions in solution stays constant while the added titrant dilutes the mixture; the conductivity falls. After the equivalence point, the added $\text{Ag}^+(aq)$ and $\text{NO}_3^-(aq)$ ions are no longer removed, so the number of ions increases and the conductivity rises. The minimum, where the two trends meet, is at $30.0\text{ mL}$: $n(\text{Cl}^-) = n(\text{Ag}^+) = 0.0300\text{ L} \times 0.10\text{ M} = 3.0 \times 10^{-3}\text{ mol}$, so $[\text{NaCl}] = \frac{3.0 \times 10^{-3}\text{ mol}}{0.0300\text{ L}} = 0.10\text{ M}$.",
    },

    # -------------------------------------------------------------------------
    # 4.7 Types of Chemical Reactions (Q35 - Q39)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 35,
        "topic_code": "4.7",
        "topic_title": "Types of Chemical Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Reaction</th><th>Balanced Equation</th></tr></thead>"
            "<tbody>"
            "<tr><td>I</td><td>$\\text{AgNO}_3(aq) + \\text{NaCl}(aq) \\rightarrow \\text{AgCl}(s) + \\text{NaNO}_3(aq)$</td></tr>"
            "<tr><td>II</td><td>$\\text{CH}_3\\text{COOH}(aq) + \\text{NH}_3(aq) \\rightarrow \\text{NH}_4^+(aq) + \\text{CH}_3\\text{COO}^-(aq)$</td></tr>"
            "<tr><td>III</td><td>$\\text{Zn}(s) + 2\\text{HCl}(aq) \\rightarrow \\text{ZnCl}_2(aq) + \\text{H}_2(g)$</td></tr>"
            "</tbody></table>"
        ),
        "question": r"Which of the following correctly classifies Reactions I, II, and III shown in the table above?",
        "options": [
            r"I: Acid-Base; II: Precipitation; III: Oxidation-Reduction",
            r"I: Precipitation; II: Acid-Base; III: Oxidation-Reduction",
            r"I: Oxidation-Reduction; II: Acid-Base; III: Precipitation",
            r"I: Precipitation; II: Oxidation-Reduction; III: Acid-Base",
        ],
        "correct_index": 1,
        "explanation": r"Reaction I forms an insoluble solid ($\text{AgCl}(s)$) from soluble ions with no change in oxidation state or proton transfer (precipitation). Reaction II transfers an $\text{H}^+$ ion from $\text{CH}_3\text{COOH}$ to $\text{NH}_3$ (Brønsted-Lowry acid-base). Reaction III involves electron transfer where $\text{Zn}$ is oxidized from $0$ to $+2$ and $\text{H}$ is reduced from $+1$ to $0$ (redox).",
    },
    {
        "unit_q_num": 36,
        "topic_code": "4.7",
        "topic_title": "Types of Chemical Reactions",
        "difficulty": "Challenging",
        "stimulus": (
            '<div class="equation-block">'
            r"$$\text{Cl}_2(aq) + 2\text{OH}^-(aq) \rightarrow \text{Cl}^-(aq) + \text{ClO}^-(aq) + \text{H}_2\text{O}(l)$$"
            "</div>"
        ),
        "question": r"How is the reaction between aqueous chlorine and hydroxide ions shown above best classified?",
        "options": [
            r"A Brønsted-Lowry acid-base reaction only, because $\text{H}_2\text{O}(l)$ is formed from $\text{OH}^-(aq)$",
            r"A precipitation reaction, because $\text{ClO}^-(aq)$ forms an insoluble salt",
            r"An oxidation-reduction (disproportionation) reaction, because chlorine changes oxidation state from $0$ in $\text{Cl}_2$ to $-1$ in $\text{Cl}^-$ and $+1$ in $\text{ClO}^-$",
            r"A physical dissolution, because no covalent bonds are broken or formed",
        ],
        "correct_index": 2,
        "explanation": r"In $\text{Cl}_2$, the oxidation state of $\text{Cl}$ is $0$. In $\text{Cl}^-$, the oxidation state is $-1$ (reduction), and in $\text{ClO}^-$, the oxidation state of $\text{Cl}$ is $+1$ (oxidation, since $\text{O}$ is $-2$). Because electrons are transferred and $\text{Cl}_2$ is simultaneously oxidized and reduced, it is an oxidation-reduction (disproportionation) reaction.",
    },
    {
        "unit_q_num": 37,
        "topic_code": "4.7",
        "topic_title": "Types of Chemical Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"Which of the following reactions is BOTH a synthesis (combination) reaction and an oxidation-reduction reaction?",
        "options": [
            r"$\text{CaO}(s) + \text{CO}_2(g) \rightarrow \text{CaCO}_3(s)$",
            r"$\text{SO}_3(g) + \text{H}_2\text{O}(l) \rightarrow \text{H}_2\text{SO}_4(aq)$",
            r"$2\text{Mg}(s) + \text{O}_2(g) \rightarrow 2\text{MgO}(s)$",
            r"$\text{NH}_3(g) + \text{HCl}(g) \rightarrow \text{NH}_4\text{Cl}(s)$",
        ],
        "correct_index": 2,
        "explanation": r"While all four equations combine two reactants into a single product, only $2\text{Mg}(s) + \text{O}_2(g) \rightarrow 2\text{MgO}(s)$ involves changes in oxidation numbers ($\text{Mg}: 0 \rightarrow +2$; $\text{O}: 0 \rightarrow -2$). In the other three reactions, oxidation numbers remain completely unchanged.",
    },
    {
        "unit_q_num": 38,
        "topic_code": "4.7",
        "topic_title": "Types of Chemical Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A student adds $0.10\text{ M }\text{K}_2\text{SO}_4(aq)$ to three separate test tubes containing $0.10\text{ M }\text{Ba(NO}_3)_2(aq)$, $0.10\text{ M }\text{Cu(NO}_3)_2(aq)$, and $0.10\text{ M }\text{NH}_4\text{NO}_3(aq)$, respectively. A white precipitate forms only in the test tube containing $\text{Ba(NO}_3)_2(aq)$. Which of the following correctly identifies the precipitate and gives the best justification?",
        "options": [
            r"$\text{KNO}_3$, because $\text{K}^+$ and $\text{NO}_3^-$ ions are present together in the test tube after mixing",
            r"$\text{Ba(NO}_3)_2$, because adding $\text{K}_2\text{SO}_4$ causes the dissolved barium nitrate to come out of solution",
            r"$\text{BaSO}_4$, because all sulfate salts are insoluble in water",
            r"$\text{BaSO}_4$, because all potassium and nitrate salts are soluble, so the solid must contain $\text{Ba}^{2+}$ and $\text{SO}_4^{2-}$ ions",
        ],
        "correct_index": 3,
        "explanation": r"In the first test tube the possible new combinations of ions are $\text{K}^+$ with $\text{NO}_3^-$ and $\text{Ba}^{2+}$ with $\text{SO}_4^{2-}$. All potassium and nitrate salts are soluble, so the solid cannot be $\text{KNO}_3$ or $\text{Ba(NO}_3)_2$ (and a $\text{KNO}_3$ precipitate would have appeared in all three tubes, which each contain $\text{K}^+$ and $\text{NO}_3^-$). Therefore the precipitate is $\text{BaSO}_4(s)$: $\text{Ba}^{2+}(aq) + \text{SO}_4^{2-}(aq) \rightarrow \text{BaSO}_4(s)$. The claim that all sulfates are insoluble is contradicted by the evidence: $\text{SO}_4^{2-}$ was also mixed with $\text{Cu}^{2+}$ and $\text{NH}_4^+$, and no solid formed, so $\text{CuSO}_4$ and $(\text{NH}_4)_2\text{SO}_4$ are soluble.",
    },
    {
        "unit_q_num": 39,
        "topic_code": "4.7",
        "topic_title": "Types of Chemical Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"Why is the complete combustion of liquid ethanol, $\text{C}_2\text{H}_5\text{OH}(l) + 3\text{O}_2(g) \rightarrow 2\text{CO}_2(g) + 3\text{H}_2\text{O}(g)$, classified as an oxidation-reduction reaction?",
        "options": [
            r"Protons ($\text{H}^+$) are transferred from $\text{C}_2\text{H}_5\text{OH}$ to $\text{O}_2$ molecules.",
            r"The oxidation state of hydrogen changes from $+1$ in $\text{C}_2\text{H}_5\text{OH}$ to $0$ in $\text{H}_2\text{O}$.",
            r"Insoluble $\text{CO}_2(g)$ precipitates out of the liquid ethanol phase.",
            r"The average oxidation state of carbon increases from $-2$ in $\text{C}_2\text{H}_5\text{OH}$ to $+4$ in $\text{CO}_2$, while the oxidation state of oxygen decreases from $0$ in $\text{O}_2$ to $-2$ in $\text{CO}_2$ and $\text{H}_2\text{O}$.",
        ],
        "correct_index": 3,
        "explanation": r"In $\text{C}_2\text{H}_6\text{O}$, assigning $\text{H} = +1$ and $\text{O} = -2$ gives $2x + 6(+1) + (-2) = 0 \Rightarrow x = -2$ as the average oxidation state of carbon. In $\text{CO}_2$, carbon has an oxidation state of $+4$ (oxidized), while elemental oxygen in $\text{O}_2$ ($0$) is reduced to $-2$ in $\text{CO}_2$ and $\text{H}_2\text{O}$.",
    },

    # -------------------------------------------------------------------------
    # 4.8 Introduction to Acid-Base Reactions (Q40 - Q44)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 40,
        "topic_code": "4.8",
        "topic_title": "Introduction to Acid-Base Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<div class="equation-block">'
            r"$$\text{HSO}_3^-(aq) + \text{HPO}_4^{2-}(aq) \rightleftharpoons \text{SO}_3^{2-}(aq) + \text{H}_2\text{PO}_4^-(aq)$$"
            "</div>"
        ),
        "question": r"In the reversible Brønsted-Lowry acid-base reaction represented above, which of the following correctly identifies a conjugate acid-base pair?",
        "options": [
            r"$\text{HSO}_3^-$ and $\text{HPO}_4^{2-}$",
            r"$\text{HSO}_3^-$ and $\text{H}_2\text{PO}_4^-$",
            r"$\text{HPO}_4^{2-}$ and $\text{H}_2\text{PO}_4^-$",
            r"$\text{SO}_3^{2-}$ and $\text{H}_2\text{PO}_4^-$",
        ],
        "correct_index": 2,
        "explanation": r"A conjugate acid-base pair differs by exactly one proton ($\text{H}^+$). Here, $\text{HPO}_4^{2-}$ acts as a Brønsted-Lowry base by accepting an $\text{H}^+$ from $\text{HSO}_3^-$ to form its conjugate acid, $\text{H}_2\text{PO}_4^-$ (and $\text{HSO}_3^-$ / $\text{SO}_3^{2-}$ is the other conjugate pair).",
    },
    {
        "unit_q_num": 41,
        "topic_code": "4.8",
        "topic_title": "Introduction to Acid-Base Reactions",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Reaction</th><th>Equilibrium Equation</th></tr></thead>"
            "<tbody>"
            "<tr><td>1</td><td>$\\text{HCO}_3^-(aq) + \\text{OH}^-(aq) \\rightleftharpoons \\text{CO}_3^{2-}(aq) + \\text{H}_2\\text{O}(l)$</td></tr>"
            "<tr><td>2</td><td>$\\text{HCO}_3^-(aq) + \\text{H}_3\\text{O}^+(aq) \\rightleftharpoons \\text{H}_2\\text{CO}_3(aq) + \\text{H}_2\\text{O}(l)$</td></tr>"
            "</tbody></table>"
        ),
        "question": r"The hydrogen carbonate ion, $\text{HCO}_3^-(aq)$, is amphiprotic (amphoteric), as illustrated by the two reactions in the table above. What is the role of $\text{HCO}_3^-(aq)$ in Reaction 1 and in Reaction 2, respectively?",
        "options": [
            r"Brønsted-Lowry acid in Reaction 1; Brønsted-Lowry base in Reaction 2",
            r"Brønsted-Lowry base in Reaction 1; Brønsted-Lowry acid in Reaction 2",
            r"Brønsted-Lowry acid in both Reaction 1 and Reaction 2",
            r"Brønsted-Lowry base in both Reaction 1 and Reaction 2",
        ],
        "correct_index": 0,
        "explanation": r"In Reaction 1, $\text{HCO}_3^-$ donates a proton ($\text{H}^+$) to $\text{OH}^-$ to become $\text{CO}_3^{2-}$, acting as a Brønsted-Lowry acid. In Reaction 2, $\text{HCO}_3^-$ accepts a proton ($\text{H}^+$) from $\text{H}_3\text{O}^+$ to become $\text{H}_2\text{CO}_3$, acting as a Brønsted-Lowry base.",
    },
    {
        "unit_q_num": 42,
        "topic_code": "4.8",
        "topic_title": "Introduction to Acid-Base Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"When hydroxylamine, $\text{NH}_2\text{OH}$, dissolves in water, a weakly basic solution is formed according to the equilibrium $\text{NH}_2\text{OH}(aq) + \text{H}_2\text{O}(l) \rightleftharpoons \text{NH}_3\text{OH}^+(aq) + \text{OH}^-(aq)$. In this reaction, water acts as which of the following?",
        "options": [
            r"A Brønsted-Lowry base, because it produces $\text{OH}^-(aq)$ ions",
            r"A Brønsted-Lowry acid, because it donates a proton ($\text{H}^+$) to $\text{NH}_2\text{OH}$",
            r"A species that is reduced, because it gains electrons from $\text{NH}_2\text{OH}$",
            r"A spectator species, because it is the solvent",
        ],
        "correct_index": 1,
        "explanation": r"In the forward reaction, $\text{H}_2\text{O}$ transfers a proton ($\text{H}^+$) to the nitrogen lone pair of $\text{NH}_2\text{OH}$, forming $\text{NH}_3\text{OH}^+$ and leaving behind its conjugate base, $\text{OH}^-$. By definition, a proton donor is a Brønsted-Lowry acid. No oxidation numbers change, so nothing is reduced, and water is a reactant that loses a proton rather than a spectator.",
    },
    {
        "unit_q_num": 43,
        "topic_code": "4.8",
        "topic_title": "Introduction to Acid-Base Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"Which of the following species CANNOT function as a Brønsted-Lowry acid in an aqueous chemical reaction?",
        "options": [
            r"$\text{H}_2\text{PO}_4^-(aq)$",
            r"$\text{NH}_4^+(aq)$",
            r"$\text{CO}_3^{2-}(aq)$",
            r"$\text{HSO}_4^-(aq)$",
        ],
        "correct_index": 2,
        "explanation": r"A Brønsted-Lowry acid must contain at least one ionizable hydrogen atom ($\text{H}^+$) to donate. Because $\text{CO}_3^{2-}$ contains no hydrogen atoms, it can only act as a Brønsted-Lowry base (proton acceptor), never as a Brønsted-Lowry acid.",
    },
    {
        "unit_q_num": 44,
        "topic_code": "4.8",
        "topic_title": "Introduction to Acid-Base Reactions",
        "difficulty": "Challenging",
        "stimulus": (
            '<div class="equation-block">'
            r"$$\text{N}_2\text{H}_4(aq) + \text{HSO}_4^-(aq) \rightleftharpoons \text{N}_2\text{H}_5^+(aq) + \text{SO}_4^{2-}(aq)$$"
            "</div>"
        ),
        "question": r"For the reaction represented above, which species act as Brønsted-Lowry bases in the forward and reverse reactions?",
        "options": [
            r"$\text{N}_2\text{H}_4(aq)$ and $\text{SO}_4^{2-}(aq)$",
            r"$\text{HSO}_4^-(aq)$ and $\text{N}_2\text{H}_5^+(aq)$",
            r"$\text{N}_2\text{H}_4(aq)$ and $\text{N}_2\text{H}_5^+(aq)$",
            r"$\text{HSO}_4^-(aq)$ and $\text{SO}_4^{2-}(aq)$",
        ],
        "correct_index": 0,
        "explanation": r"In the forward direction, $\text{N}_2\text{H}_4$ accepts a proton ($\text{H}^+$) from $\text{HSO}_4^-$ to form $\text{N}_2\text{H}_5^+$, so $\text{N}_2\text{H}_4$ is the Brønsted-Lowry base. In the reverse direction, $\text{SO}_4^{2-}$ accepts a proton ($\text{H}^+$) from $\text{N}_2\text{H}_5^+$ to form $\text{HSO}_4^-$, so $\text{SO}_4^{2-}$ is the conjugate Brønsted-Lowry base.",
    },

    # -------------------------------------------------------------------------
    # 4.9 Oxidation-Reduction (Redox) Reactions (Q45 - Q50)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 45,
        "topic_code": "4.9",
        "topic_title": "Oxidation-Reduction (Redox) Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"In which of the following nitrogen-containing species does nitrogen have the highest (most positive) oxidation number?",
        "options": [
            r"$\text{NH}_2\text{OH}$",
            r"$\text{N}_2\text{O}_4$",
            r"$\text{NO}_2^-$",
            r"$\text{N}_2\text{H}_4$",
        ],
        "correct_index": 1,
        "explanation": r"Assigning $\text{O} = -2$ and $\text{H} = +1$: in $\text{NH}_2\text{OH}$, $x + 3(+1) + (-2) = 0 \Rightarrow x = -1$; in $\text{N}_2\text{O}_4$, $2x + 4(-2) = 0 \Rightarrow x = +4$; in $\text{NO}_2^-$, $x + 2(-2) = -1 \Rightarrow x = +3$; in $\text{N}_2\text{H}_4$, $2x + 4(+1) = 0 \Rightarrow x = -2$. Thus nitrogen has the highest oxidation number ($+4$) in $\text{N}_2\text{O}_4$.",
    },
    {
        "unit_q_num": 46,
        "topic_code": "4.9",
        "topic_title": "Oxidation-Reduction (Redox) Reactions",
        "difficulty": "Challenging",
        "stimulus": (
            '<div class="equation-block">'
            r"$$\text{Cr}_2\text{O}_7^{2-}(aq) + \text{C}_2\text{O}_4^{2-}(aq) + \text{H}^+(aq) \rightarrow \text{Cr}^{3+}(aq) + \text{CO}_2(g) + \text{H}_2\text{O}(l)\quad\text{(unbalanced)}$$"
            "</div>"
        ),
        "question": r"When the oxidation-reduction reaction in acidic solution shown above is balanced using the lowest whole-number coefficients, what are the coefficients of $\text{C}_2\text{O}_4^{2-}(aq)$ and $\text{H}^+(aq)$, respectively?",
        "options": [
            r"$3\text{ and }7$",
            r"$3\text{ and }14$",
            r"$6\text{ and }14$",
            r"$2\text{ and }8$",
        ],
        "correct_index": 1,
        "explanation": r"Reduction half-reaction: $\text{Cr}_2\text{O}_7^{2-} + 14\text{H}^+ + 6e^- \rightarrow 2\text{Cr}^{3+} + 7\text{H}_2\text{O}$. Oxidation half-reaction: $\text{C}_2\text{O}_4^{2-} \rightarrow 2\text{CO}_2 + 2e^-$. Multiplying the oxidation half-reaction by $3$ to balance the $6e^-$ transferred gives the overall balanced equation: $\text{Cr}_2\text{O}_7^{2-} + 3\text{C}_2\text{O}_4^{2-} + 14\text{H}^+ \rightarrow 2\text{Cr}^{3+} + 6\text{CO}_2 + 7\text{H}_2\text{O}$. The coefficients of $\text{C}_2\text{O}_4^{2-}$ and $\text{H}^+$ are $3$ and $14$.",
    },
    {
        "unit_q_num": 47,
        "topic_code": "4.9",
        "topic_title": "Oxidation-Reduction (Redox) Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Half-Reaction</th><th>Balanced Equation</th></tr></thead>"
            "<tbody>"
            "<tr><td>Oxidation</td><td>$\\text{Cu}(s) \\rightarrow \\text{Cu}^{2+}(aq) + 2e^-$</td></tr>"
            "<tr><td>Reduction</td><td>$\\text{NO}_3^-(aq) + 4\\text{H}^+(aq) + 3e^- \\rightarrow \\text{NO}(g) + 2\\text{H}_2\\text{O}(l)$</td></tr>"
            "</tbody></table>"
        ),
        "question": r"Based on the two half-reactions in the table above, how many moles of electrons are transferred per mole of $\text{NO}_3^-(aq)$ reduced, and what is the stoichiometric ratio of $\text{Cu}(s)$ oxidized to $\text{NO}(g)$ produced in the overall balanced redox equation?",
        "options": [
            r"$3\text{ moles of }e^-$ per mole of $\text{NO}_3^-$; mole ratio of $\text{Cu} : \text{NO}$ is $3:2$",
            r"$2\text{ moles of }e^-$ per mole of $\text{NO}_3^-$; mole ratio of $\text{Cu} : \text{NO}$ is $2:3$",
            r"$6\text{ moles of }e^-$ per mole of $\text{NO}_3^-$; mole ratio of $\text{Cu} : \text{NO}$ is $1:1$",
            r"$3\text{ moles of }e^-$ per mole of $\text{NO}_3^-$; mole ratio of $\text{Cu} : \text{NO}$ is $2:3$",
        ],
        "correct_index": 0,
        "explanation": r"The reduction half-reaction shows $3e^-$ gained per $1\text{ NO}_3^-$ ion reduced ($\text{N}$ changes from $+5$ to $+2$). To equalize electrons ($6e^-$ least common multiple), multiply the $\text{Cu}$ half-reaction by $3$ and the $\text{NO}_3^-$ half-reaction by $2$: $3\text{Cu}(s) + 2\text{NO}_3^-(aq) + 8\text{H}^+(aq) \rightarrow 3\text{Cu}^{2+}(aq) + 2\text{NO}(g) + 4\text{H}_2\text{O}(l)$. Thus the $\text{Cu}:\text{NO}$ mole ratio is $3:2$.",
    },
    {
        "unit_q_num": 48,
        "topic_code": "4.9",
        "topic_title": "Oxidation-Reduction (Redox) Reactions",
        "difficulty": "Challenging",
        "stimulus": (
            '<table class="quiz-data-table">'
            "<thead><tr><th>Experiment</th><th>Metal Strip Added</th><th>Solution</th><th>Observation</th></tr></thead>"
            "<tbody>"
            "<tr><td>1</td><td>$\\text{X}(s)$</td><td>$1.0\\text{ M }\\text{Y(NO}_3)_2(aq)$</td><td>Solid $\\text{Y}$ plates out on strip $\\text{X}$</td></tr>"
            "<tr><td>2</td><td>$\\text{Y}(s)$</td><td>$1.0\\text{ M }\\text{Z(NO}_3)_2(aq)$</td><td>No reaction observed</td></tr>"
            "<tr><td>3</td><td>$\\text{X}(s)$</td><td>$1.0\\text{ M }\\text{Z(NO}_3)_2(aq)$</td><td>Solid $\\text{Z}$ plates out on strip $\\text{X}$</td></tr>"
            "<tr><td>4</td><td>$\\text{Z}(s)$</td><td>$1.0\\text{ M }\\text{Y(NO}_3)_2(aq)$</td><td>Solid $\\text{Y}$ plates out on strip $\\text{Z}$</td></tr>"
            "</tbody></table>"
        ),
        "question": r"A student tests the relative ease of oxidation of three unknown metals ($\text{X}$, $\text{Y}$, and $\text{Z}$) using the four experiments summarized in the table above. Which of the following lists the metals in order from least easily oxidized to most easily oxidized?",
        "options": [
            r"$\text{X} < \text{Z} < \text{Y}$",
            r"$\text{Y} < \text{Z} < \text{X}$",
            r"$\text{Z} < \text{Y} < \text{X}$",
            r"$\text{Y} < \text{X} < \text{Z}$",
        ],
        "correct_index": 1,
        "explanation": r"In Experiments 1 and 3, metal $\text{X}(s)$ loses electrons to both $\text{Y}^{2+}$ and $\text{Z}^{2+}$, so $\text{X}$ is the most easily oxidized. In Experiment 4, $\text{Z}(s)$ loses electrons to $\text{Y}^{2+}$, consistent with Experiment 2, in which $\text{Y}(s)$ does not transfer electrons to $\text{Z}^{2+}$. Thus ease of oxidation increases in the order $\text{Y} < \text{Z} < \text{X}$.",
    },
    {
        "unit_q_num": 49,
        "topic_code": "4.9",
        "topic_title": "Oxidation-Reduction (Redox) Reactions",
        "difficulty": "Challenging",
        "stimulus": (
            '<div class="equation-block">'
            r"$$2\text{MnO}_4^-(aq) + 5\text{H}_2\text{O}_2(aq) + 6\text{H}^+(aq) \rightarrow 2\text{Mn}^{2+}(aq) + 5\text{O}_2(g) + 8\text{H}_2\text{O}(l)$$"
            "</div>"
        ),
        "question": r"A $10.00\text{ mL}$ sample of aqueous hydrogen peroxide, $\text{H}_2\text{O}_2(aq)$, is acidified and titrated with $0.0400\text{ M }\text{KMnO}_4(aq)$ according to the balanced equation above. If $25.00\text{ mL}$ of $\text{KMnO}_4(aq)$ is required to reach the equivalence point, what is the concentration of $\text{H}_2\text{O}_2(aq)$ in the original sample, and what is the change in oxidation number of oxygen in $\text{H}_2\text{O}_2$?",
        "options": [
            r"$0.100\text{ M}$; oxygen changes from $-2$ to $0$",
            r"$0.250\text{ M}$; oxygen changes from $-1$ to $0$",
            r"$0.250\text{ M}$; oxygen changes from $-2$ to $0$",
            r"$0.0400\text{ M}$; oxygen changes from $-1$ to $-2$",
        ],
        "correct_index": 1,
        "explanation": r"Moles of $\text{MnO}_4^-$ added $= 0.02500\text{ L} \times 0.0400\text{ M} = 0.00100\text{ mol}$. By the $2:5$ mole ratio, moles of $\text{H}_2\text{O}_2 = 0.00100\text{ mol} \times \frac{5}{2} = 0.00250\text{ mol}$. In the $10.00\text{ mL}$ ($0.01000\text{ L}$) sample, $[\text{H}_2\text{O}_2] = \frac{0.00250\text{ mol}}{0.01000\text{ L}} = 0.250\text{ M}$. In $\text{H}_2\text{O}_2$ (a peroxide), oxygen has an oxidation state of $-1$ and is oxidized to $0$ in $\text{O}_2(g)$.",
    },
    {
        "unit_q_num": 50,
        "topic_code": "4.9",
        "topic_title": "Oxidation-Reduction (Redox) Reactions",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"A $25.0\text{ mL}$ solution containing $0.0030\text{ mol}$ of an ion $\text{XO}_3^-(aq)$ (in which element $\text{X}$ has an oxidation state of $+5$) reacts completely with $0.0090\text{ mol}$ of $\text{Fe}^{2+}(aq)$ in acidic solution, oxidizing all of the $\text{Fe}^{2+}(aq)$ to $\text{Fe}^{3+}(aq)$. What is the final oxidation state of element $\text{X}$ in the product?",
        "options": [
            r"$-1$",
            r"$0$",
            r"$+2$",
            r"$+4$",
        ],
        "correct_index": 2,
        "explanation": r"Each mole of $\text{Fe}^{2+}$ oxidized to $\text{Fe}^{3+}$ loses $1\text{ mol of }e^-$, so $0.0090\text{ mol }\text{Fe}^{2+}$ transfers $0.0090\text{ mol of }e^-$ to $0.0030\text{ mol of }\text{XO}_3^-$. This is $\frac{0.0090\text{ mol }e^-}{0.0030\text{ mol }\text{X}} = 3\text{ mol of }e^-$ gained per mole of $\text{X}$. Reducing $\text{X}$ from an initial oxidation state of $+5$ by $3$ units yields a final oxidation state of $+5 - 3 = +2$.",
    },

    # -------------------------------------------------------------------------
    # Added 2026-10-03 — Blind-spot coverage (Fall 2024 CED): topics 4.1–4.9
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 51,
        "topic_code": "4.1",
        "topic_title": "Introduction for Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A student stirs a white crystalline solid into distilled water. The solid disappears completely, and the temperature of the mixture decreases from $22.0^\circ\text{C}$ to $19.5^\circ\text{C}$. The student claims that a chemical reaction occurred because the temperature changed. Which of the following additional results would provide the strongest evidence that only a physical change occurred?",
        "options": [
            r"The resulting solution conducts electricity.",
            r"The solid dissolves more quickly when the mixture is stirred faster.",
            r"After all of the water is evaporated, a white solid is recovered that has the same mass and the same melting point as the original sample.",
            r"The temperature of the mixture slowly returns to $22.0^\circ\text{C}$ after an hour.",
        ],
        "correct_index": 2,
        "explanation": r"Dissolving forms a mixture, and forming or separating a mixture is a physical change because the substances keep their identities. Recovering a solid with the original mass and the same characteristic property (melting point) shows that the solute was only dispersed in the water and then separated again, so no new substance formed. A temperature change alone is not conclusive, because physical processes such as dissolving also absorb or release energy. Electrical conductivity shows only that ions are present, which is also true when an ionic solid simply dissolves. The rate of dissolving and the later return to room temperature (heat exchange with the surroundings) give no information about whether the composition changed.",
    },
    {
        "unit_q_num": 52,
        "topic_code": "4.2",
        "topic_title": "Net Ionic Equations",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap"><svg class="quiz-figure" viewBox="0 0 580 315" role="img" aria-label="Particulate diagram in two panels. Left panel, solid calcium chloride: an ordered array of 4 calcium ions (small dark spheres labeled 2+) and 8 chloride ions (larger light spheres labeled minus) packed together. Right panel, after the solid is stirred into water: the same 4 calcium ions and 8 chloride ions are separated from one another and spread through the water; three water molecules surround one calcium ion with their oxygen atoms pointing toward it, and two water molecules surround one chloride ion with a hydrogen atom pointing toward it."><rect x="15" y="40" width="240" height="212" rx="6" fill="white" stroke="#374151" stroke-width="2"/><rect x="325" y="40" width="240" height="212" rx="6" fill="white" stroke="#374151" stroke-width="2"/><text x="135.0" y="28.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">Before: solid CaCl₂</text><text x="445.0" y="28.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">After: stirred into water</text><line x1="262" y1="146" x2="309" y2="146" stroke="#374151" stroke-width="2.5"/><polygon points="318,146 306,140 306,152" fill="#374151"/><circle cx="85.5" cy="113.0" r="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/><text x="85.5" y="118.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="151.5" cy="113.0" r="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/><text x="151.5" y="118.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="184.5" cy="113.0" r="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/><text x="184.5" y="118.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="118.5" cy="146.0" r="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/><text x="118.5" y="151.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="151.5" cy="146.0" r="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/><text x="151.5" y="151.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="85.5" cy="179.0" r="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/><text x="85.5" y="184.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="118.5" cy="179.0" r="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/><text x="118.5" y="184.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="184.5" cy="179.0" r="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/><text x="184.5" y="184.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="118.5" cy="113.0" r="11" fill="#4b5563" stroke="#111827" stroke-width="1.5"/><text x="118.5" y="117.0" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="white">2+</text><circle cx="85.5" cy="146.0" r="11" fill="#4b5563" stroke="#111827" stroke-width="1.5"/><text x="85.5" y="150.0" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="white">2+</text><circle cx="184.5" cy="146.0" r="11" fill="#4b5563" stroke="#111827" stroke-width="1.5"/><text x="184.5" y="150.0" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="white">2+</text><circle cx="151.5" cy="179.0" r="11" fill="#4b5563" stroke="#111827" stroke-width="1.5"/><text x="151.5" y="183.0" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="white">2+</text><circle cx="448.0" cy="70.0" r="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/><text x="448.0" y="75.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="540.0" cy="118.0" r="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/><text x="540.0" y="123.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="468.0" cy="122.0" r="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/><text x="468.0" y="127.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="352.0" cy="162.0" r="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/><text x="352.0" y="167.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="420.0" cy="228.0" r="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/><text x="420.0" y="233.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="538.0" cy="232.0" r="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/><text x="538.0" y="237.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="350.0" cy="60.0" r="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/><text x="350.0" y="65.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="492.0" cy="196.0" r="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/><text x="492.0" y="201.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="505.0" cy="70.0" r="11" fill="#4b5563" stroke="#111827" stroke-width="1.5"/><text x="505.0" y="74.0" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="white">2+</text><circle cx="425.0" cy="172.0" r="11" fill="#4b5563" stroke="#111827" stroke-width="1.5"/><text x="425.0" y="176.0" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="white">2+</text><circle cx="365.0" cy="222.0" r="11" fill="#4b5563" stroke="#111827" stroke-width="1.5"/><text x="365.0" y="226.0" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="white">2+</text><circle cx="382.0" cy="100.0" r="11" fill="#4b5563" stroke="#111827" stroke-width="1.5"/><text x="382.0" y="104.0" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="white">2+</text><circle cx="359.9" cy="85.7" r="3.6" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="355.9" cy="96.8" r="3.6" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="362.3" cy="92.8" r="6" fill="#dc2626" stroke="#111827" stroke-width="1.0"/><circle cx="407.1" cy="92.3" r="3.6" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="401.2" cy="82.1" r="3.6" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="400.2" cy="89.5" r="6" fill="#dc2626" stroke="#111827" stroke-width="1.0"/><circle cx="378.3" cy="126.0" r="3.6" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="390.1" cy="125.0" r="3.6" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="383.8" cy="120.9" r="6" fill="#dc2626" stroke="#111827" stroke-width="1.0"/><circle cx="474.2" cy="206.2" r="3.6" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="469.8" cy="217.2" r="3.6" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="467.8" cy="210.0" r="6" fill="#dc2626" stroke="#111827" stroke-width="1.0"/><circle cx="490.2" cy="175.6" r="3.6" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="482.2" cy="166.9" r="3.6" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="489.6" cy="168.1" r="6" fill="#dc2626" stroke="#111827" stroke-width="1.0"/><circle cx="40.0" cy="284.0" r="11" fill="#4b5563" stroke="#111827" stroke-width="1.5"/><text x="40.0" y="288.0" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="white">2+</text><text x="58.0" y="289.0" text-anchor="start" font-family="sans-serif" font-size="13" fill="#111827">Ca²⁺</text><circle cx="122.0" cy="284.0" r="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/><text x="122.0" y="289.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><text x="144.0" y="289.0" text-anchor="start" font-family="sans-serif" font-size="13" fill="#111827">Cl⁻</text><circle cx="218.9" cy="279.4" r="3.6" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="207.1" cy="279.4" r="3.6" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="213.0" cy="284.0" r="6" fill="#dc2626" stroke="#111827" stroke-width="1.0"/><text x="230.0" y="289.0" text-anchor="start" font-family="sans-serif" font-size="13" fill="#111827">H₂O molecule (only a few are shown)</text></svg><figcaption>Figure: Particulate views of solid calcium chloride before and after it is stirred into water.</figcaption></figure>""",
        "question": r"The diagram above represents a sample of solid calcium chloride before and after it is stirred into water (only a few water molecules are shown). Which of the following equations best represents the process shown in the diagram?",
        "options": [
            r"$\text{CaCl}_2(s) \rightarrow \text{Ca}^{2+}(aq) + \text{Cl}_2^{\,2-}(aq)$",
            r"$\text{CaCl}_2(s) \rightarrow \text{Ca}^{2+}(aq) + 2\text{Cl}^-(aq)$",
            r"$\text{CaCl}_2(s) + 2\text{H}_2\text{O}(l) \rightarrow \text{Ca(OH)}_2(aq) + 2\text{HCl}(aq)$",
            r"$\text{Ca}^{2+}(aq) + 2\text{Cl}^-(aq) \rightarrow \text{CaCl}_2(s)$",
        ],
        "correct_index": 1,
        "explanation": r"In the 'after' panel, the same $4\text{ Ca}^{2+}$ and $8\text{ Cl}^-$ ions that made up the solid are separated from one another and surrounded by water molecules (O atoms oriented toward $\text{Ca}^{2+}$, an H atom toward $\text{Cl}^-$), with two separate $\text{Cl}^-$ ions for every $\text{Ca}^{2+}$ ion. This physical change (dissolution) is represented by $\text{CaCl}_2(s) \rightarrow \text{Ca}^{2+}(aq) + 2\text{Cl}^-(aq)$, which conserves both atoms and charge. The chloride ions are not bonded to each other, so $\text{Cl}_2^{\,2-}$ misrepresents them. No $\text{OH}^-$ or $\text{H}^+$ species appear in the diagram, so the ions did not react with water to form $\text{Ca(OH)}_2$ and $\text{HCl}$. The equation with aqueous ions as reactants describes the reverse process, formation of the solid.",
    },
    {
        "unit_q_num": 53,
        "topic_code": "4.3",
        "topic_title": "Representations of Reactions",
        "difficulty": "Challenging",
        "stimulus": r"""<figure class="quiz-figure-wrap"><svg class="quiz-figure" viewBox="0 0 560 300" role="img" aria-label="Particulate diagram of a beaker after the reaction is complete, water molecules not shown. At the bottom are 2 formula units of solid lead(II) iodide, each drawn as one Pb2+ ion between two I- ions. Dissolved in the solution are 1 Pb2+ ion, 4 K+ ions, and 6 nitrate ions; there are no free iodide ions. A legend identifies the symbols for Pb2+, I-, K+, and NO3-."><path d="M22,28 L22,272 Q22,282 32,282 L368,282 Q378,282 378,272 L378,28" fill="white" stroke="#374151" stroke-width="2.5"/><line x1="22" y1="44" x2="378" y2="44" stroke="#9ca3af" stroke-width="1.5" stroke-dasharray="6 4"/><circle cx="140.0" cy="265.0" r="15" fill="#d1d5db" stroke="#374151" stroke-width="1.5"/><text x="140.0" y="270.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="166.0" cy="265.0" r="11" fill="#111827" stroke="#111827" stroke-width="1.5"/><text x="166.0" y="269.0" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="white">2+</text><circle cx="192.0" cy="265.0" r="15" fill="#d1d5db" stroke="#374151" stroke-width="1.5"/><text x="192.0" y="270.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="236.0" cy="265.0" r="15" fill="#d1d5db" stroke="#374151" stroke-width="1.5"/><text x="236.0" y="270.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="262.0" cy="265.0" r="11" fill="#111827" stroke="#111827" stroke-width="1.5"/><text x="262.0" y="269.0" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="white">2+</text><circle cx="288.0" cy="265.0" r="15" fill="#d1d5db" stroke="#374151" stroke-width="1.5"/><text x="288.0" y="270.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="150.0" cy="57.0" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="157.8" cy="70.5" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="142.2" cy="70.5" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="150.0" cy="66.0" r="4.5" fill="#2563eb" stroke="#111827" stroke-width="1.0"/><text x="165.0" y="61.0" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">−</text><circle cx="268.0" cy="57.0" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="275.8" cy="70.5" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="260.2" cy="70.5" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="268.0" cy="66.0" r="4.5" fill="#2563eb" stroke="#111827" stroke-width="1.0"/><text x="283.0" y="61.0" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">−</text><circle cx="58.0" cy="125.0" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="65.8" cy="138.5" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="50.2" cy="138.5" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="58.0" cy="134.0" r="4.5" fill="#2563eb" stroke="#111827" stroke-width="1.0"/><text x="73.0" y="129.0" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">−</text><circle cx="204.0" cy="137.0" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="211.8" cy="150.5" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="196.2" cy="150.5" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="204.0" cy="146.0" r="4.5" fill="#2563eb" stroke="#111827" stroke-width="1.0"/><text x="219.0" y="141.0" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">−</text><circle cx="344.0" cy="85.0" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="351.8" cy="98.5" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="336.2" cy="98.5" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="344.0" cy="94.0" r="4.5" fill="#2563eb" stroke="#111827" stroke-width="1.0"/><text x="359.0" y="89.0" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">−</text><circle cx="72.0" cy="213.0" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="79.8" cy="226.5" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="64.2" cy="226.5" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="72.0" cy="222.0" r="4.5" fill="#2563eb" stroke="#111827" stroke-width="1.0"/><text x="87.0" y="217.0" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">−</text><circle cx="92.0" cy="74.0" r="9" fill="white" stroke="#374151" stroke-width="1.5"/><text x="92.0" y="78.5" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">+</text><circle cx="215.0" cy="92.0" r="9" fill="white" stroke="#374151" stroke-width="1.5"/><text x="215.0" y="96.5" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">+</text><circle cx="130.0" cy="178.0" r="9" fill="white" stroke="#374151" stroke-width="1.5"/><text x="130.0" y="182.5" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">+</text><circle cx="334.0" cy="206.0" r="9" fill="white" stroke="#374151" stroke-width="1.5"/><text x="334.0" y="210.5" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">+</text><circle cx="300.0" cy="120.0" r="11" fill="#111827" stroke="#111827" stroke-width="1.5"/><text x="300.0" y="124.0" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="white">2+</text><text x="400.0" y="52.0" text-anchor="start" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">Key</text><circle cx="414.0" cy="82.0" r="11" fill="#111827" stroke="#111827" stroke-width="1.5"/><text x="414.0" y="86.0" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="white">2+</text><text x="436.0" y="87.0" text-anchor="start" font-family="sans-serif" font-size="13" fill="#111827">Pb²⁺</text><circle cx="414.0" cy="122.0" r="15" fill="#d1d5db" stroke="#374151" stroke-width="1.5"/><text x="414.0" y="127.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><text x="436.0" y="127.0" text-anchor="start" font-family="sans-serif" font-size="13" fill="#111827">I⁻</text><circle cx="414.0" cy="160.0" r="9" fill="white" stroke="#374151" stroke-width="1.5"/><text x="414.0" y="164.5" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">+</text><text x="436.0" y="165.0" text-anchor="start" font-family="sans-serif" font-size="13" fill="#111827">K⁺</text><circle cx="414.0" cy="189.0" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="421.8" cy="202.5" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="406.2" cy="202.5" r="5.5" fill="#9ca3af" stroke="#374151" stroke-width="1.2"/><circle cx="414.0" cy="198.0" r="4.5" fill="#2563eb" stroke="#111827" stroke-width="1.0"/><text x="436.0" y="203.0" text-anchor="start" font-family="sans-serif" font-size="13" fill="#111827">NO₃⁻</text><text x="400.0" y="240.0" text-anchor="start" font-family="sans-serif" font-size="12" fill="#374151">Water molecules</text><text x="400.0" y="256.0" text-anchor="start" font-family="sans-serif" font-size="12" fill="#374151">are not shown.</text></svg><figcaption>Figure: Contents of the beaker after the reaction is complete.</figcaption></figure>""",
        "question": r"Aqueous solutions of lead(II) nitrate, $\text{Pb(NO}_3)_2$, and potassium iodide, $\text{KI}$, are mixed, and a yellow precipitate forms. The diagram above represents the contents of the beaker after the reaction is complete (water molecules are not shown). Which of the following best represents the ions in the two solutions before they were mixed?",
        "options": [
            r"$1\text{ Pb}^{2+}$ and $2\text{ NO}_3^-$ ions mixed with $4\text{ K}^+$ and $4\text{ I}^-$ ions",
            r"$2\text{ Pb}^{2+}$ and $4\text{ NO}_3^-$ ions mixed with $4\text{ K}^+$ and $4\text{ I}^-$ ions",
            r"$3\text{ Pb}^{2+}$ and $6\text{ NO}_3^-$ ions mixed with $6\text{ K}^+$ and $6\text{ I}^-$ ions",
            r"$3\text{ Pb}^{2+}$ and $6\text{ NO}_3^-$ ions mixed with $4\text{ K}^+$ and $4\text{ I}^-$ ions",
        ],
        "correct_index": 3,
        "explanation": r"Atoms and charge are conserved, and spectator ions are unchanged by the reaction. The diagram shows $2$ formula units of $\text{PbI}_2(s)$ (containing $2\text{ Pb}^{2+}$ and $4\text{ I}^-$) plus $1\text{ Pb}^{2+}$, $4\text{ K}^+$, and $6\text{ NO}_3^-$ ions in solution. The original solutions therefore contained $2 + 1 = 3\text{ Pb}^{2+}$ with $6\text{ NO}_3^-$, and $4\text{ I}^-$ with $4\text{ K}^+$. Because $\text{I}^-$ was limiting in $\text{Pb}^{2+}(aq) + 2\text{I}^-(aq) \rightarrow \text{PbI}_2(s)$, one $\text{Pb}^{2+}$ remains. Starting with only $1$ or $2\text{ Pb}^{2+}$ cannot account for all of the lead shown or for the $6$ spectator $\text{NO}_3^-$ ions, and $6\text{ I}^-$ would have precipitated all $3\text{ Pb}^{2+}$ and left $6\text{ K}^+$, not $4$, in solution.",
    },
    {
        "unit_q_num": 54,
        "topic_code": "4.4",
        "topic_title": "Physical and Chemical Changes",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table"><thead><tr><th>Substance</th><th>Melting Point</th><th>Electrical Conductivity of the Liquid</th></tr></thead><tbody><tr><td>$\text{H}_2\text{O}$</td><td>$0^\circ\text{C}$</td><td>Very low</td></tr><tr><td>$\text{NaCl}$</td><td>$801^\circ\text{C}$</td><td>High</td></tr></tbody></table>""",
        "question": r"The table above gives the melting points of ice and of sodium chloride and the electrical conductivity of each substance in the liquid state. Which of the following best explains these data?",
        "options": [
            r"Melting $\text{NaCl}$ is a chemical change in which electrons are transferred to form $\text{Na}(l)$ and $\text{Cl}_2(l)$; the liquid conducts because it contains metallic sodium.",
            r"Melting ice breaks covalent $\text{O}-\text{H}$ bonds within $\text{H}_2\text{O}$ molecules, whereas melting $\text{NaCl}$ overcomes only London dispersion forces between $\text{NaCl}$ molecules.",
            r"Both substances melt by overcoming only intermolecular forces between molecules; $\text{NaCl}$ melts at a higher temperature because it has a greater molar mass.",
            r"Melting $\text{NaCl}$ disrupts strong ionic bonds and frees the ions to move, whereas melting ice overcomes only hydrogen bonds between intact $\text{H}_2\text{O}$ molecules; both are physical changes because no new substances form.",
        ],
        "correct_index": 3,
        "explanation": r"Solid $\text{NaCl}$ is a lattice of $\text{Na}^+$ and $\text{Cl}^-$ ions held together by strong ionic bonds, so melting it requires a high temperature and produces mobile ions; hence the molten salt conducts. Ice consists of discrete $\text{H}_2\text{O}$ molecules, and melting overcomes only intermolecular hydrogen bonds, so it occurs at a low temperature and the liquid contains very few ions. Cooling molten $\text{NaCl}$ regenerates the same solid, so no new substance forms: melting $\text{NaCl}$ is a physical process that nevertheless involves breaking chemical (ionic) bonds. Forming $\text{Na}$ and $\text{Cl}_2$ requires electron transfer (electrolysis), not melting. $\text{NaCl}$ is not molecular, so dispersion forces between 'NaCl molecules' and molar-mass arguments do not apply, and melting ice leaves the covalent $\text{O}-\text{H}$ bonds intact.",
    },
    {
        "unit_q_num": 55,
        "topic_code": "4.5",
        "topic_title": "Stoichiometry",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"A $0.486\text{ g}$ sample of magnesium metal ($\text{molar mass } 24.31\text{ g/mol}$) is added to $15.0\text{ mL}$ of $1.00\text{ M }\text{HCl}(aq)$. The reaction $\text{Mg}(s) + 2\text{HCl}(aq) \rightarrow \text{MgCl}_2(aq) + \text{H}_2(g)$ proceeds until one reactant is completely consumed. What volume of dry $\text{H}_2(g)$, measured at $1.00\text{ atm}$ and $300\text{ K}$, is produced?",
        "options": [
            r"$0.168\text{ L}$",
            r"$0.185\text{ L}$",
            r"$0.369\text{ L}$",
            r"$0.492\text{ L}$",
        ],
        "correct_index": 1,
        "explanation": r"$n(\text{Mg}) = \frac{0.486\text{ g}}{24.31\text{ g/mol}} = 0.0200\text{ mol}$ and $n(\text{HCl}) = 0.0150\text{ L} \times 1.00\text{ M} = 0.0150\text{ mol}$. Consuming all of the Mg would require $2 \times 0.0200 = 0.0400\text{ mol HCl}$, so $\text{HCl}$ is the limiting reactant and $n(\text{H}_2) = \frac{0.0150\text{ mol}}{2} = 0.00750\text{ mol}$. Then $V = \frac{nRT}{P} = \frac{(0.00750\text{ mol})(0.08206\text{ L atm mol}^{-1}\text{ K}^{-1})(300\text{ K})}{1.00\text{ atm}} = 0.185\text{ L}$. Treating Mg as limiting gives $0.492\text{ L}$; ignoring the $2:1$ mole ratio of $\text{HCl}$ to $\text{H}_2$ gives $0.369\text{ L}$; using $22.4\text{ L/mol}$, which applies only at $273\text{ K}$ and $1\text{ atm}$, gives $0.168\text{ L}$.",
    },
    {
        "unit_q_num": 56,
        "topic_code": "4.5",
        "topic_title": "Stoichiometry",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A student determines the mass percent of sulfate in a soluble solid by dissolving a weighed sample in water and adding $\text{BaCl}_2(aq)$ to precipitate the sulfate as $\text{BaSO}_4(s)$, which is insoluble in water. The precipitate will then be filtered, dried, and weighed. Before filtering, which of the following procedures would best confirm that all of the sulfate ions have been precipitated?",
        "options": [
            r"Add a few more drops of $\text{BaCl}_2(aq)$ to the clear liquid above the settled precipitate and check whether any additional precipitate forms.",
            r"Add a few drops of $\text{Na}_2\text{SO}_4(aq)$ to the clear liquid above the settled precipitate; if no precipitate forms, all of the sulfate has been precipitated.",
            r"Dry and weigh the precipitate repeatedly until two consecutive masses agree.",
            r"Weigh the beaker and its contents before and after adding the $\text{BaCl}_2(aq)$ to confirm that mass is conserved.",
        ],
        "correct_index": 0,
        "explanation": r"All of the sulfate has been precipitated only if $\text{Ba}^{2+}$ is present in excess. If adding more $\text{BaCl}_2(aq)$ to the clear liquid produces no new cloudiness, no $\text{SO}_4^{2-}$ remains in solution. Adding $\text{Na}_2\text{SO}_4$ tests for excess $\text{Ba}^{2+}$, but the stated conclusion is reversed: no precipitate would mean that $\text{Ba}^{2+}$ is not in excess, so some sulfate could still be dissolved. Drying and weighing to constant mass confirms that the solid is dry, not that precipitation is complete. Mass is conserved whether or not precipitation is complete, so weighing the beaker cannot detect sulfate that remains in solution.",
    },
    {
        "unit_q_num": 57,
        "topic_code": "4.6",
        "topic_title": "Introduction to Titration",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap"><svg class="quiz-figure" viewBox="0 0 520 330" role="img" aria-label="Titration curve of pH versus volume of 0.100 M NaOH added, from 0 to 50 mL. The pH starts near 0.8, rises slowly to about 2.4 at 28 mL, then rises almost vertically at 30.0 mL, passing pH 7, and levels off near pH 12 to 12.5 after 35 mL."><line x1="70.0" y1="30.0" x2="70.0" y2="282.0" stroke="#e5e7eb" stroke-width="1"/><line x1="112.0" y1="30.0" x2="112.0" y2="282.0" stroke="#e5e7eb" stroke-width="1"/><line x1="154.0" y1="30.0" x2="154.0" y2="282.0" stroke="#e5e7eb" stroke-width="1"/><line x1="196.0" y1="30.0" x2="196.0" y2="282.0" stroke="#e5e7eb" stroke-width="1"/><line x1="238.0" y1="30.0" x2="238.0" y2="282.0" stroke="#e5e7eb" stroke-width="1"/><line x1="280.0" y1="30.0" x2="280.0" y2="282.0" stroke="#e5e7eb" stroke-width="1"/><line x1="322.0" y1="30.0" x2="322.0" y2="282.0" stroke="#e5e7eb" stroke-width="1"/><line x1="364.0" y1="30.0" x2="364.0" y2="282.0" stroke="#e5e7eb" stroke-width="1"/><line x1="406.0" y1="30.0" x2="406.0" y2="282.0" stroke="#e5e7eb" stroke-width="1"/><line x1="448.0" y1="30.0" x2="448.0" y2="282.0" stroke="#e5e7eb" stroke-width="1"/><line x1="490.0" y1="30.0" x2="490.0" y2="282.0" stroke="#e5e7eb" stroke-width="1"/><line x1="70.0" y1="282.0" x2="490.0" y2="282.0" stroke="#e5e7eb" stroke-width="1"/><line x1="70.0" y1="246.0" x2="490.0" y2="246.0" stroke="#e5e7eb" stroke-width="1"/><line x1="70.0" y1="210.0" x2="490.0" y2="210.0" stroke="#e5e7eb" stroke-width="1"/><line x1="70.0" y1="174.0" x2="490.0" y2="174.0" stroke="#e5e7eb" stroke-width="1"/><line x1="70.0" y1="138.0" x2="490.0" y2="138.0" stroke="#e5e7eb" stroke-width="1"/><line x1="70.0" y1="102.0" x2="490.0" y2="102.0" stroke="#e5e7eb" stroke-width="1"/><line x1="70.0" y1="66.0" x2="490.0" y2="66.0" stroke="#e5e7eb" stroke-width="1"/><line x1="70.0" y1="30.0" x2="490.0" y2="30.0" stroke="#e5e7eb" stroke-width="1"/><line x1="70.0" y1="282.0" x2="490.0" y2="282.0" stroke="#111827" stroke-width="2"/><line x1="70.0" y1="282.0" x2="70.0" y2="30.0" stroke="#111827" stroke-width="2"/><line x1="70.0" y1="282.0" x2="70.0" y2="288.0" stroke="#111827" stroke-width="1.5"/><text x="70.0" y="303.0" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#111827">0</text><line x1="154.0" y1="282.0" x2="154.0" y2="288.0" stroke="#111827" stroke-width="1.5"/><text x="154.0" y="303.0" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#111827">10</text><line x1="238.0" y1="282.0" x2="238.0" y2="288.0" stroke="#111827" stroke-width="1.5"/><text x="238.0" y="303.0" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#111827">20</text><line x1="322.0" y1="282.0" x2="322.0" y2="288.0" stroke="#111827" stroke-width="1.5"/><text x="322.0" y="303.0" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#111827">30</text><line x1="406.0" y1="282.0" x2="406.0" y2="288.0" stroke="#111827" stroke-width="1.5"/><text x="406.0" y="303.0" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#111827">40</text><line x1="490.0" y1="282.0" x2="490.0" y2="288.0" stroke="#111827" stroke-width="1.5"/><text x="490.0" y="303.0" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#111827">50</text><line x1="112.0" y1="282.0" x2="112.0" y2="286.0" stroke="#111827" stroke-width="1.2"/><line x1="196.0" y1="282.0" x2="196.0" y2="286.0" stroke="#111827" stroke-width="1.2"/><line x1="280.0" y1="282.0" x2="280.0" y2="286.0" stroke="#111827" stroke-width="1.2"/><line x1="364.0" y1="282.0" x2="364.0" y2="286.0" stroke="#111827" stroke-width="1.2"/><line x1="448.0" y1="282.0" x2="448.0" y2="286.0" stroke="#111827" stroke-width="1.2"/><line x1="64.0" y1="282.0" x2="70.0" y2="282.0" stroke="#111827" stroke-width="1.5"/><text x="60.0" y="286.5" text-anchor="end" font-family="sans-serif" font-size="13" fill="#111827">0</text><line x1="64.0" y1="246.0" x2="70.0" y2="246.0" stroke="#111827" stroke-width="1.5"/><text x="60.0" y="250.5" text-anchor="end" font-family="sans-serif" font-size="13" fill="#111827">2</text><line x1="64.0" y1="210.0" x2="70.0" y2="210.0" stroke="#111827" stroke-width="1.5"/><text x="60.0" y="214.5" text-anchor="end" font-family="sans-serif" font-size="13" fill="#111827">4</text><line x1="64.0" y1="174.0" x2="70.0" y2="174.0" stroke="#111827" stroke-width="1.5"/><text x="60.0" y="178.5" text-anchor="end" font-family="sans-serif" font-size="13" fill="#111827">6</text><line x1="64.0" y1="138.0" x2="70.0" y2="138.0" stroke="#111827" stroke-width="1.5"/><text x="60.0" y="142.5" text-anchor="end" font-family="sans-serif" font-size="13" fill="#111827">8</text><line x1="64.0" y1="102.0" x2="70.0" y2="102.0" stroke="#111827" stroke-width="1.5"/><text x="60.0" y="106.5" text-anchor="end" font-family="sans-serif" font-size="13" fill="#111827">10</text><line x1="64.0" y1="66.0" x2="70.0" y2="66.0" stroke="#111827" stroke-width="1.5"/><text x="60.0" y="70.5" text-anchor="end" font-family="sans-serif" font-size="13" fill="#111827">12</text><line x1="64.0" y1="30.0" x2="70.0" y2="30.0" stroke="#111827" stroke-width="1.5"/><text x="60.0" y="34.5" text-anchor="end" font-family="sans-serif" font-size="13" fill="#111827">14</text><text x="280.0" y="324.0" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#111827">Volume of 0.100 M NaOH added (mL)</text><text x="24.0" y="156.0" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#111827" transform="rotate(-90 24 156.0)">pH</text><polyline points="70.0,267.2 74.2,266.8 78.4,266.5 82.6,266.2 86.8,265.9 91.0,265.6 95.2,265.3 99.4,264.9 103.6,264.6 107.8,264.3 112.0,264.0 116.2,263.7 120.4,263.4 124.6,263.1 128.8,262.7 133.0,262.4 137.2,262.1 141.4,261.8 145.6,261.5 149.8,261.2 154.0,260.8 158.2,260.5 162.4,260.2 166.6,259.8 170.8,259.5 175.0,259.2 179.2,258.8 183.4,258.5 187.6,258.1 191.8,257.7 196.0,257.4 200.2,257.0 204.4,256.6 208.6,256.2 212.8,255.8 217.0,255.4 221.2,255.0 225.4,254.6 229.6,254.1 233.8,253.6 238.0,253.2 242.2,252.7 246.4,252.1 250.6,251.6 254.8,251.0 259.0,250.4 263.2,249.8 267.4,249.1 271.6,248.4 275.8,247.7 280.0,246.8 284.2,245.9 288.4,244.9 292.6,243.8 296.8,242.5 301.0,241.0 305.2,239.2 306.0,238.7 306.9,238.3 307.7,237.8 308.6,237.3 309.4,236.8 310.2,236.3 311.1,235.7 311.9,235.0 312.8,234.3 313.6,233.6 314.4,232.7 315.3,231.8 316.1,230.7 317.0,229.5 317.8,228.1 318.6,226.3 319.5,224.1 320.3,220.9 320.5,220.0 320.7,219.1 320.8,218.1 321.0,216.9 321.2,215.4 321.3,213.7 321.5,211.4 321.7,208.3 321.8,202.8 322.0,156.0 322.2,109.2 322.3,103.8 322.5,100.6 322.7,98.3 322.8,96.6 323.0,95.2 323.2,94.0 323.3,92.9 323.5,92.0 323.7,91.2 324.5,88.0 325.4,85.8 326.2,84.1 327.0,82.7 327.9,81.5 328.7,80.4 329.6,79.5 330.4,78.7 331.2,78.0 332.1,77.3 332.9,76.7 333.8,76.2 334.6,75.6 335.4,75.2 336.3,74.7 337.1,74.3 338.0,73.9 338.8,73.5 343.0,71.8 347.2,70.4 351.4,69.3 355.6,68.3 359.8,67.5 364.0,66.7 368.2,66.1 372.4,65.5 376.6,64.9 380.8,64.4 385.0,63.9 389.2,63.5 393.4,63.1 397.6,62.7 401.8,62.3 406.0,62.0 410.2,61.7 414.4,61.4 418.6,61.1 422.8,60.8 427.0,60.6 431.2,60.3 435.4,60.1 439.6,59.9 443.8,59.7 448.0,59.5 452.2,59.3 456.4,59.1 460.6,58.9 464.8,58.7 469.0,58.6 473.2,58.4 477.4,58.2 481.6,58.1 485.8,57.9 490.0,57.8" fill="none" stroke="#111827" stroke-width="2.5" stroke-linejoin="round"/></svg><figcaption>Figure: pH of the solution as 0.100 M NaOH is added to 20.0 mL of HCl.</figcaption></figure>""",
        "question": r"A $20.0\text{ mL}$ sample of $\text{HCl}(aq)$ of unknown concentration is titrated with $0.100\text{ M }\text{NaOH}(aq)$, and the pH is recorded as the titrant is added, giving the titration curve shown above. What was the concentration of the $\text{HCl}(aq)$?",
        "options": [
            r"$0.0667\text{ M}$",
            r"$0.0750\text{ M}$",
            r"$0.150\text{ M}$",
            r"$0.300\text{ M}$",
        ],
        "correct_index": 2,
        "explanation": r"The equivalence point is at the middle of the nearly vertical rise in pH, at $30.0\text{ mL}$ of titrant (pH $7$ for a strong acid–strong base titration). There, $n(\text{HCl}) = n(\text{NaOH}) = 0.0300\text{ L} \times 0.100\text{ M} = 3.00 \times 10^{-3}\text{ mol}$, because $\text{H}^+(aq) + \text{OH}^-(aq) \rightarrow \text{H}_2\text{O}(l)$ has a $1:1$ ratio. So $[\text{HCl}] = \frac{3.00 \times 10^{-3}\text{ mol}}{0.0200\text{ L}} = 0.150\text{ M}$. Inverting the volume ratio gives $0.0667\text{ M}$; using half of the equivalence volume ($15.0\text{ mL}$) gives $0.0750\text{ M}$; assuming that $2\text{ mol HCl}$ react per mole of $\text{NaOH}$ gives $0.300\text{ M}$.",
    },
    {
        "unit_q_num": 58,
        "topic_code": "4.6",
        "topic_title": "Introduction to Titration",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"A student determines the concentration of an $\text{HCl}(aq)$ solution by titrating a $25.00\text{ mL}$ aliquot with standardized $\text{NaOH}(aq)$, using phenolphthalein as the indicator. Which of the following errors would cause the calculated concentration of $\text{HCl}$ to be lower than the actual concentration?",
        "options": [
            r"An air bubble trapped in the tip of the buret at the start of the titration is expelled during the titration.",
            r"The student adds $\text{NaOH}(aq)$ past the endpoint, until the solution is dark pink, before recording the final buret reading.",
            r"During the titration, the student uses distilled water from a wash bottle to rinse droplets on the inner walls of the flask into the solution.",
            r"Some of the $\text{HCl}$ solution splashes out of the flask while it is being swirled, before the endpoint is reached.",
        ],
        "correct_index": 3,
        "explanation": r"The calculated concentration is $[\text{HCl}] = \frac{M_{\text{NaOH}} V_{\text{NaOH}}}{25.00\text{ mL}}$, so any error that lowers the recorded volume of $\text{NaOH}$ lowers the result. If acid splashes out, fewer moles of $\text{HCl}$ remain in the flask, less $\text{NaOH}$ is needed to reach the endpoint, and the calculated concentration is too low. An expelled air bubble makes the recorded volume larger than the volume actually delivered, and overshooting the endpoint adds extra titrant; both make the calculated concentration too high. Rinsing the walls with distilled water changes only the total volume in the flask, not the moles of $\text{HCl}$, so it does not change the volume of titrant needed.",
    },
    {
        "unit_q_num": 59,
        "topic_code": "4.8",
        "topic_title": "Introduction to Acid-Base Reactions",
        "difficulty": "Challenging",
        "stimulus": r"""<figure class="quiz-figure-wrap"><svg class="quiz-figure" viewBox="0 0 560 300" role="img" aria-label="Two particulate diagrams of equal volumes of 0.10 molar acid solutions, water molecules not shown. Left box, HX solution: five hydronium ions and five X- ions, and no intact HX molecules. Right box, HY solution: four intact HY molecules, one hydronium ion, and one Y- ion. A legend shows the symbols for a hydronium ion, an anion (X- or Y-), and an acid molecule (HX or HY)."><rect x="20" y="40" width="240" height="190" rx="6" fill="white" stroke="#374151" stroke-width="2"/><rect x="300" y="40" width="240" height="190" rx="6" fill="white" stroke="#374151" stroke-width="2"/><text x="140.0" y="28.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">0.10 M HX</text><text x="420.0" y="28.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">0.10 M HY</text><circle cx="112.0" cy="112.0" r="12" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="112.0" y="117.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="210.0" cy="80.0" r="12" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="210.0" y="85.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="56.0" cy="196.0" r="12" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="56.0" y="201.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="156.0" cy="150.0" r="12" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="156.0" y="155.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="140.0" cy="205.0" r="12" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="140.0" y="210.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="62.0" cy="72.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="70.7" cy="87.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="53.3" cy="87.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="62.0" cy="82.0" r="8" fill="#4b5563" stroke="#111827" stroke-width="1.2"/><text x="77.0" y="74.0" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">+</text><circle cx="160.0" cy="62.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="168.7" cy="77.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="151.3" cy="77.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="160.0" cy="72.0" r="8" fill="#4b5563" stroke="#111827" stroke-width="1.2"/><text x="175.0" y="64.0" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">+</text><circle cx="222.0" cy="118.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="230.7" cy="133.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="213.3" cy="133.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="222.0" cy="128.0" r="8" fill="#4b5563" stroke="#111827" stroke-width="1.2"/><text x="237.0" y="120.0" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">+</text><circle cx="100.0" cy="158.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="108.7" cy="173.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="91.3" cy="173.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="100.0" cy="168.0" r="8" fill="#4b5563" stroke="#111827" stroke-width="1.2"/><text x="115.0" y="160.0" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">+</text><circle cx="196.0" cy="186.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="204.7" cy="201.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="187.3" cy="201.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="196.0" cy="196.0" r="8" fill="#4b5563" stroke="#111827" stroke-width="1.2"/><text x="211.0" y="188.0" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">+</text><circle cx="358.2" cy="86.8" r="5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="345.0" cy="82.0" r="12" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="436.8" cy="80.8" r="5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="450.0" cy="76.0" r="12" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="495.2" cy="146.8" r="5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="500.0" cy="160.0" r="12" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="382.1" cy="175.0" r="5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="370.0" cy="182.0" r="12" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><circle cx="500.0" cy="104.0" r="12" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="500.0" y="109.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><circle cx="440.0" cy="140.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="448.7" cy="155.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="431.3" cy="155.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="440.0" cy="150.0" r="8" fill="#4b5563" stroke="#111827" stroke-width="1.2"/><text x="455.0" y="142.0" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">+</text><circle cx="40.0" cy="260.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="48.7" cy="275.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="31.3" cy="275.0" r="4.5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="40.0" cy="270.0" r="8" fill="#4b5563" stroke="#111827" stroke-width="1.2"/><text x="55.0" y="262.0" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#111827">+</text><text x="62.0" y="275.0" text-anchor="start" font-family="sans-serif" font-size="13" fill="#111827">H₃O⁺</text><circle cx="170.0" cy="268.0" r="12" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="170.0" y="273.0" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#111827">−</text><text x="188.0" y="273.0" text-anchor="start" font-family="sans-serif" font-size="13" fill="#111827">X⁻ or Y⁻</text><circle cx="286.0" cy="268.0" r="5" fill="white" stroke="#374151" stroke-width="1.2"/><circle cx="300.0" cy="268.0" r="12" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/><text x="318.0" y="273.0" text-anchor="start" font-family="sans-serif" font-size="13" fill="#111827">HX or HY molecule</text></svg><figcaption>Figure: Equal volumes of 0.10 M HX and 0.10 M HY (water molecules not shown).</figcaption></figure>""",
        "question": r"The particulate diagrams above represent equal volumes of $0.10\text{ M}$ solutions of two monoprotic acids, $\text{HX}$ and $\text{HY}$ (water molecules are not shown). Which of the following statements is best supported by the diagrams?",
        "options": [
            r"$\text{HX}$ is the stronger acid; essentially every $\text{HX}$ molecule has transferred a proton to $\text{H}_2\text{O}$, so $\text{X}^-$ is a weaker base than $\text{Y}^-$.",
            r"$\text{HX}$ is the stronger acid, so its conjugate base, $\text{X}^-$, is a stronger base than $\text{Y}^-$.",
            r"$\text{HY}$ is the stronger acid, because more of its molecules remain intact and available to donate protons.",
            r"In both solutions, $\text{H}_2\text{O}$ acts as a Brønsted-Lowry acid by donating protons to $\text{HX}$ and $\text{HY}$.",
        ],
        "correct_index": 0,
        "explanation": r"In the $\text{HX}$ diagram every acid molecule has ionized, $\text{HX}(aq) + \text{H}_2\text{O}(l) \rightarrow \text{H}_3\text{O}^+(aq) + \text{X}^-(aq)$, whereas in the $\text{HY}$ diagram four of the five molecules remain intact and only one $\text{H}_3\text{O}^+$ ion and one $\text{Y}^-$ ion are present. Thus $\text{HX}$ is the stronger acid. In each ionization, water accepts a proton, acting as a Brønsted-Lowry base (not an acid) to form $\text{H}_3\text{O}^+$. Because $\text{X}^-$ shows essentially no tendency to take a proton back from $\text{H}_3\text{O}^+$, while $\text{Y}^-$ readily recombines to form $\text{HY}$, the conjugate base of the stronger acid is the weaker base. Intact molecules indicate a weaker acid, not a greater supply of donatable protons.",
    },
    {
        "unit_q_num": 60,
        "topic_code": "4.9",
        "topic_title": "Oxidation-Reduction (Redox) Reactions",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"In acidic solution, iodate ions, $\text{IO}_3^-(aq)$, are reduced to solid iodine, $\text{I}_2(s)$. Which of the following is the correctly balanced reduction half-reaction?",
        "options": [
            r"$2\text{IO}_3^-(aq) + 12\text{H}^+(aq) + 10e^- \rightarrow \text{I}_2(s) + 6\text{H}_2\text{O}(l)$",
            r"$2\text{IO}_3^-(aq) + 12\text{H}^+(aq) + 5e^- \rightarrow \text{I}_2(s) + 6\text{H}_2\text{O}(l)$",
            r"$2\text{IO}_3^-(aq) + 12\text{H}^+(aq) \rightarrow \text{I}_2(s) + 6\text{H}_2\text{O}(l) + 10e^-$",
            r"$2\text{IO}_3^-(aq) + 6\text{H}^+(aq) + 10e^- \rightarrow \text{I}_2(s) + 3\text{H}_2\text{O}(l)$",
        ],
        "correct_index": 0,
        "explanation": r"Balance I first ($2\text{IO}_3^-$ forms one $\text{I}_2$), then O by adding $6\text{H}_2\text{O}$ to the product side, then H by adding $12\text{H}^+$ to the reactant side. The reactant side now has a charge of $2(-1) + 12(+1) = +10$ and the product side has a charge of $0$, so $10e^-$ must be added to the reactant side. This agrees with oxidation numbers: each I atom changes from $+5$ to $0$, gaining $5e^-$, and there are two I atoms. Using $5e^-$ accounts for only one I atom and leaves the charge unbalanced; electrons written as a product describe an oxidation and give charges of $+10$ and $-10$; with $6\text{H}^+$ and $3\text{H}_2\text{O}$, neither the O atoms nor the charges balance.",
    },
]
