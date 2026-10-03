UNIT_META = {
    "id": 1,
    "title": "Unit 1: Atomic Structure and Properties",
    "short_title": "Atomic Structure & Properties",
    "exam_weight": "7–9%",
    "color": "#2563eb",
    "description": "Moles and molar mass, mass spectroscopy of elements, elemental composition of pure substances, composition of mixtures, atomic structure and electron configuration, photoelectron spectroscopy (PES), periodic trends, and valence electrons in ionic compounds.",
    "topics": [
        {"code": "1.1", "title": "Moles and Molar Mass"},
        {"code": "1.2", "title": "Mass Spectra of Elements"},
        {"code": "1.3", "title": "Elemental Composition of Pure Substances"},
        {"code": "1.4", "title": "Composition of Mixtures"},
        {"code": "1.5", "title": "Atomic Structure and Electron Configuration"},
        {"code": "1.6", "title": "Photoelectron Spectroscopy (PES)"},
        {"code": "1.7", "title": "Periodic Trends"},
        {"code": "1.8", "title": "Valence Electrons and Ionic Compounds"},
    ],
}

QUESTIONS = [
    # -------------------------------------------------------------------------
    # Topic 1.1: Moles and Molar Mass (Q1 - Q7)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 1,
        "topic_code": "1.1",
        "topic_title": "Moles and Molar Mass",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A chemist weighs out a $17.1\text{ g}$ sample of anhydrous aluminum sulfate, $\text{Al}_2(\text{SO}_4)_3$ (molar mass $342.15\text{ g/mol}$). How many total oxygen atoms are present in this sample?",
        "options": [
            r"$3.01 \times 10^{22}$ atoms",
            r"$9.03 \times 10^{22}$ atoms",
            r"$3.61 \times 10^{23}$ atoms",
            r"$7.22 \times 10^{24}$ atoms",
        ],
        "correct_index": 2,
        "explanation": r"First calculate the moles of $\text{Al}_2(\text{SO}_4)_3$: $\text{mol Al}_2(\text{SO}_4)_3 = \frac{17.1\text{ g}}{342.15\text{ g/mol}} = 0.0500\text{ mol}$. Each formula unit of $\text{Al}_2(\text{SO}_4)_3$ contains $3 \times 4 = 12$ oxygen atoms, so $\text{mol O} = 0.0500\text{ mol} \times 12 = 0.600\text{ mol O}$. Multiplying by Avogadro's number gives $0.600\text{ mol} \times 6.022 \times 10^{23}\text{ atoms/mol} = 3.61 \times 10^{23}$ oxygen atoms.",
    },
    {
        "unit_q_num": 2,
        "topic_code": "1.1",
        "topic_title": "Moles and Molar Mass",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Sample</th><th>Gas</th><th>Molar Mass ($\text{g/mol}$)</th><th>Sample Mass ($\text{g}$)</th></tr>
</thead>
<tbody>
<tr><td>1</td><td>$\text{He}$</td><td>$4.00$</td><td>$4.0$</td></tr>
<tr><td>2</td><td>$\text{CH}_4$</td><td>$16.04$</td><td>$8.0$</td></tr>
<tr><td>3</td><td>$\text{O}_2$</td><td>$32.00$</td><td>$32.0$</td></tr>
<tr><td>4</td><td>$\text{SO}_2$</td><td>$64.06$</td><td>$32.0$</td></tr>
</tbody>
</table>""",
        "question": r"Four sealed containers hold the gas samples listed in the table above. Which sample contains the greatest total number of atoms?",
        "options": [
            r"Sample 1 ($\text{He}$)",
            r"Sample 2 ($\text{CH}_4$)",
            r"Sample 3 ($\text{O}_2$)",
            r"Sample 4 ($\text{SO}_2$)",
        ],
        "correct_index": 1,
        "explanation": r"Calculate the total moles of atoms in each sample by multiplying the moles of molecules by the number of atoms per molecule: Sample 1 ($\text{He}$): $\frac{4.0}{4.00} \times 1 = 1.0\text{ mol atoms}$; Sample 2 ($\text{CH}_4$): $\frac{8.0}{16.04} \times 5 = 0.50 \times 5 = 2.5\text{ mol atoms}$; Sample 3 ($\text{O}_2$): $\frac{32.0}{32.00} \times 2 = 2.0\text{ mol atoms}$; Sample 4 ($\text{SO}_2$): $\frac{32.0}{64.06} \times 3 = 0.50 \times 3 = 1.5\text{ mol atoms}$. Sample 2 contains the greatest total number of atoms.",
    },
    {
        "unit_q_num": 3,
        "topic_code": "1.1",
        "topic_title": "Moles and Molar Mass",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"A pure sample of a metal oxide with the formula $\text{M}_2\text{O}_3$ has a mass of $3.99\text{ g}$ and contains $0.0750\text{ mol}$ of $\text{O}^{2-}$ ions. What is the identity of the metal $\text{M}$?",
        "options": [
            r"$\text{Al}$",
            r"$\text{Cr}$",
            r"$\text{Fe}$",
            r"$\text{Ga}$",
        ],
        "correct_index": 2,
        "explanation": r"Since there are $3\text{ mol}$ of $\text{O}^{2-}$ ions per $1\text{ mol}$ of $\text{M}_2\text{O}_3$, the sample contains $\frac{0.0750\text{ mol O}^{2-}}{3} = 0.0250\text{ mol M}_2\text{O}_3$. The molar mass of $\text{M}_2\text{O}_3$ is $\frac{3.99\text{ g}}{0.0250\text{ mol}} = 159.6\text{ g/mol}$. Subtracting the mass of $3\text{ mol}$ of $\text{O}$ ($3 \times 16.00 = 48.00\text{ g/mol}$) gives $111.6\text{ g/mol}$ for $2\text{ mol}$ of $\text{M}$, or $55.8\text{ g/mol}$ per mole of $\text{M}$, which corresponds to iron ($\text{Fe}$, $55.85\text{ g/mol}$).",
    },
    {
        "unit_q_num": 4,
        "topic_code": "1.1",
        "topic_title": "Moles and Molar Mass",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A biological amino acid contains exactly one nitrogen atom per molecule. If a $2.25\text{ g}$ pure sample of this amino acid contains $1.806 \times 10^{22}$ nitrogen atoms, what is the molar mass of the amino acid?",
        "options": [
            r"$37.5\text{ g/mol}$",
            r"$75.0\text{ g/mol}$",
            r"$89.1\text{ g/mol}$",
            r"$150.\text{ g/mol}$",
        ],
        "correct_index": 1,
        "explanation": r"Convert the number of nitrogen atoms to moles: $\text{mol N} = \frac{1.806 \times 10^{22}}{6.022 \times 10^{23}\text{ mol}^{-1}} = 0.02999\text{ mol N} \approx 0.0300\text{ mol N}$. Because each amino acid molecule contains exactly one nitrogen atom, the sample contains $0.0300\text{ mol}$ of the amino acid. Thus, $\text{Molar Mass} = \frac{2.25\text{ g}}{0.0300\text{ mol}} = 75.0\text{ g/mol}$ (glycine).",
    },
    {
        "unit_q_num": 5,
        "topic_code": "1.1",
        "topic_title": "Moles and Molar Mass",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"Vessel A contains $10.0\text{ g}$ of ethene ($\text{C}_2\text{H}_4$, molar mass $28.05\text{ g/mol}$) and Vessel B contains $10.0\text{ g}$ of propene ($\text{C}_3\text{H}_6$, molar mass $42.08\text{ g/mol}$). Which of the following statements accurately compares the contents of the two vessels?",
        "options": [
            r"Vessel A and Vessel B contain the same number of molecules and the same number of carbon atoms.",
            r"Vessel A contains both more molecules and more total hydrogen atoms than Vessel B.",
            r"Vessel B contains more carbon atoms than Vessel A because each $\text{C}_3\text{H}_6$ molecule has three carbon atoms.",
            r"Vessel A contains more molecules than Vessel B, but both vessels contain the same total number of carbon atoms.",
        ],
        "correct_index": 3,
        "explanation": r"Both $\text{C}_2\text{H}_4$ and $\text{C}_3\text{H}_6$ share the same empirical formula ($\text{CH}_2$, empirical mass $14.03\text{ g/mol}$), meaning both compounds have the exact same mass percent of carbon ($85.6\%$) and hydrogen ($14.4\%$). Therefore, $10.0\text{ g}$ of either substance contains the exact same total moles of $\text{C}$ atoms and $\text{H}$ atoms. However, because $\text{C}_2\text{H}_4$ has a smaller molar mass than $\text{C}_3\text{H}_6$, $10.0\text{ g}$ of $\text{C}_2\text{H}_4$ represents more moles of molecules ($\frac{10.0}{28.05} = 0.357\text{ mol}$) than $10.0\text{ g}$ of $\text{C}_3\text{H}_6$ ($\frac{10.0}{42.08} = 0.238\text{ mol}$).",
    },
    {
        "unit_q_num": 6,
        "topic_code": "1.1",
        "topic_title": "Moles and Molar Mass",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"How many moles of chloride ions ($\text{Cl}^-$) are present in an aqueous solution prepared by completely dissolving $11.1\text{ g}$ of calcium chloride, $\text{CaCl}_2$ (molar mass $110.98\text{ g/mol}$), in $250.\text{ mL}$ of distilled water?",
        "options": [
            r"$0.0500\text{ mol}$",
            r"$0.100\text{ mol}$",
            r"$0.200\text{ mol}$",
            r"$0.400\text{ mol}$",
        ],
        "correct_index": 2,
        "explanation": r"First find the moles of $\text{CaCl}_2$: $\frac{11.1\text{ g}}{110.98\text{ g/mol}} = 0.100\text{ mol CaCl}_2$. Upon dissolution, $\text{CaCl}_2(s) \rightarrow \text{Ca}^{2+}(aq) + 2\text{Cl}^-(aq)$, producing $2\text{ mol Cl}^-$ per mole of $\text{CaCl}_2$. Therefore, $\text{mol Cl}^- = 2 \times 0.100\text{ mol} = 0.200\text{ mol}$. (The volume of water is not needed to find moles; $0.400$ would be the approximate molarity of $\text{CaCl}_2$ ($0.100\text{ mol}/0.250\text{ L}$), and the molarity of $\text{Cl}^-$ would be about $0.800\text{ M}$.)",
    },
    {
        "unit_q_num": 7,
        "topic_code": "1.1",
        "topic_title": "Moles and Molar Mass",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Property</th><th>Measured Value</th></tr>
</thead>
<tbody>
<tr><td>Mass of anhydrous metal chloride ($\text{XCl}_2$)</td><td>$4.76\text{ g}$</td></tr>
<tr><td>Moles of $\text{Cl}^-$ ions in sample</td><td>$0.100\text{ mol}$</td></tr>
</tbody>
</table>""",
        "question": r"A student analyzes a pure sample of an unknown alkaline earth metal chloride, $\text{XCl}_2$, and obtains the data in the table above. Based on these data, what is the identity of element $\text{X}$?",
        "options": [
            r"$\text{Be}$",
            r"$\text{Mg}$",
            r"$\text{Ca}$",
            r"$\text{Sr}$",
        ],
        "correct_index": 1,
        "explanation": r"Since the formula is $\text{XCl}_2$, $0.100\text{ mol}$ of $\text{Cl}^-$ corresponds to $0.0500\text{ mol}$ of $\text{XCl}_2$. The molar mass of $\text{XCl}_2$ is $\frac{4.76\text{ g}}{0.0500\text{ mol}} = 95.2\text{ g/mol}$. Subtracting the molar mass of two chlorine atoms ($2 \times 35.45 = 70.90\text{ g/mol}$) gives $M_{\text{X}} = 95.2 - 70.90 = 24.3\text{ g/mol}$, which matches magnesium ($\text{Mg}$, $24.31\text{ g/mol}$).",
    },

    # -------------------------------------------------------------------------
    # Topic 1.2: Mass Spectra of Elements (Q8 - Q13)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 8,
        "topic_code": "1.2",
        "topic_title": "Mass Spectra of Elements",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Mass-to-Charge Ratio ($m/z$)</th><th>Relative Abundance ($\text{\%}$)</th></tr>
</thead>
<tbody>
<tr><td>$69$</td><td>$60.1$</td></tr>
<tr><td>$71$</td><td>$39.9$</td></tr>
</tbody>
</table>""",
        "question": r"The mass spectrum of a pure element is summarized in the table above. Based on these data, what is the average atomic mass and identity of the element?",
        "options": [
            r"$69.8\text{ amu}$, Gallium ($\text{Ga}$)",
            r"$70.0\text{ amu}$, Zinc ($\text{Zn}$)",
            r"$70.2\text{ amu}$, Germanium ($\text{Ge}$)",
            r"$69.8\text{ amu}$, Germanium ($\text{Ge}$)",
        ],
        "correct_index": 0,
        "explanation": r"Calculate the weighted average atomic mass: $(0.601 \times 69\text{ amu}) + (0.399 \times 71\text{ amu}) = 41.47 + 28.33 = 69.80\text{ amu}$. On the periodic table, the element with an average atomic mass of $69.72\text{ amu}$ is Gallium ($\text{Ga}$).",
    },
    {
        "unit_q_num": 9,
        "topic_code": "1.2",
        "topic_title": "Mass Spectra of Elements",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"Naturally occurring rubidium consists of two isotopes, $^{85}\text{Rb}$ (isotopic mass $84.91\text{ amu}$) and $^{87}\text{Rb}$ (isotopic mass $86.91\text{ amu}$), and its average atomic mass is $85.47\text{ amu}$. In the mass spectrum of a pure sample of rubidium, what is the ratio of the height of the peak at $m/z = 85$ to the height of the peak at $m/z = 87$?",
        "options": [
            r"$0.389$",
            r"$1.00$",
            r"$1.13$",
            r"$2.57$",
        ],
        "correct_index": 3,
        "explanation": r"Let $x$ be the fractional abundance of $^{85}\text{Rb}$, so the fractional abundance of $^{87}\text{Rb}$ is $1 - x$. Then $84.91x + 86.91(1 - x) = 85.47$, which gives $86.91 - 2.00x = 85.47$ and $x = 0.720$. Thus $72.0\%$ of the atoms are $^{85}\text{Rb}$ and $28.0\%$ are $^{87}\text{Rb}$. Because the height of each peak in the mass spectrum of an element is proportional to the relative abundance of that isotope, the ratio of peak heights is $\frac{72.0}{28.0} = 2.57$, consistent with the average atomic mass lying closer to $85$ than to $87$. The ratio $0.389$ inverts the abundances, $1.00$ assumes that the two isotopes are equally abundant, and $1.13$ ($53:47$) comes from treating the decimal part of $85.47$ as the fraction of the heavier isotope, a shortcut that does not work when the isotopic masses differ by $2\text{ amu}$.",
    },
    {
        "unit_q_num": 10,
        "topic_code": "1.2",
        "topic_title": "Mass Spectra of Elements",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Isotope</th><th>Isotopic Mass ($\text{amu}$)</th><th>Natural Abundance ($\text{\%}$)</th></tr>
</thead>
<tbody>
<tr><td>$^{24}\text{Mg}$</td><td>$23.99$</td><td>$78.99$</td></tr>
<tr><td>$^{25}\text{Mg}$</td><td>$24.99$</td><td>$10.00$</td></tr>
<tr><td>$^{26}\text{Mg}$</td><td>$25.98$</td><td>$11.01$</td></tr>
</tbody>
</table>""",
        "question": r"The natural isotopic abundances of magnesium are given in the table above. If a purified sample of magnesium is artificially enriched in $^{26}\text{Mg}$ so that its $^{26}\text{Mg}$ abundance increases to $40.0\%$, which of the following will change for the enriched sample compared to a natural sample?",
        "options": [
            r"The atomic number of the magnesium atoms in the sample",
            r"The number of valence electrons per magnesium atom",
            r"The mass of $1.00\text{ mol}$ of magnesium atoms in the sample",
            r"The $m/z$ positions of the three peaks in the mass spectrum",
        ],
        "correct_index": 2,
        "explanation": r"Enriching the sample in the heavier isotope $^{26}\text{Mg}$ increases the weighted average atomic mass (and therefore the molar mass, or mass of $1.00\text{ mol}$ of atoms) of the sample. The atomic number ($12$), number of valence electrons ($2$), and the $m/z$ positions of the individual isotopic peaks ($24, 25, 26$) remain unchanged; only the relative peak heights change.",
    },
    {
        "unit_q_num": 11,
        "topic_code": "1.2",
        "topic_title": "Mass Spectra of Elements",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"Silver ($\text{Ag}$) has an average atomic mass of $107.87\text{ amu}$ and consists of two naturally occurring isotopes, $^{107}\text{Ag}$ ($106.91\text{ amu}$) and $^{109}\text{Ag}$ ($108.90\text{ amu}$). Which statement correctly describes the mass spectrum of naturally occurring silver?",
        "options": [
            r"There is a single peak at $m/z = 107.87$.",
            r"There are three peaks at $m/z = 107$, $108$, and $109$, with the tallest peak at $m/z = 108$.",
            r"There are two peaks at $m/z = 107$ and $109$, with the peak at $m/z = 109$ approximately twice as tall as the peak at $m/z = 107$.",
            r"There are two peaks at $m/z = 107$ and $109$, with the peak at $m/z = 107$ slightly taller than the peak at $m/z = 109$.",
        ],
        "correct_index": 3,
        "explanation": r"The midpoint between the two isotopic masses ($106.91\text{ amu}$ and $108.90\text{ amu}$) is $107.905\text{ amu}$. Since the actual average atomic mass ($107.87\text{ amu}$) is just slightly below this midpoint, the lighter isotope $^{107}\text{Ag}$ has an abundance slightly greater than $50\%$ ($\approx 51.8\%$) and $^{109}\text{Ag}$ has an abundance slightly less than $50\%$ ($\approx 48.2\%$).",
    },
    {
        "unit_q_num": 12,
        "topic_code": "1.2",
        "topic_title": "Mass Spectra of Elements",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Mass Number</th><th>Relative Number of Atoms</th></tr>
</thead>
<tbody>
<tr><td>$50$</td><td>$4.3$</td></tr>
<tr><td>$52$</td><td>$83.8$</td></tr>
<tr><td>$53$</td><td>$9.5$</td></tr>
<tr><td>$54$</td><td>$2.4$</td></tr>
</tbody>
</table>""",
        "question": r"The mass spectrum of a pure transition metal is represented in the table above. How many protons and neutrons are present in a nucleus of the most abundant isotope of this element?",
        "options": [
            r"$24$ protons and $28$ neutrons",
            r"$28$ protons and $24$ neutrons",
            r"$24$ protons and $52$ neutrons",
            r"$25$ protons and $27$ neutrons",
        ],
        "correct_index": 0,
        "explanation": r"The weighted average mass is $(0.043 \times 50) + (0.838 \times 52) + (0.095 \times 53) + (0.024 \times 54) = 2.15 + 43.58 + 5.04 + 1.30 = 52.07\text{ amu}$, which identifies the element as chromium ($\text{Cr}$, atomic number $24$, molar mass $52.00\text{ g/mol}$). Every chromium nucleus has $24$ protons, and the most abundant isotope ($^{52}\text{Cr}$) has $52 - 24 = 28$ neutrons.",
    },
    {
        "unit_q_num": 13,
        "topic_code": "1.2",
        "topic_title": "Mass Spectra of Elements",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"The periodic table lists the atomic mass of copper ($\text{Cu}$) as $63.55\text{ amu}$. However, when a pure sample of copper is analyzed by mass spectrometry, no signal is detected at $m/z = 63.55$. Which statement best explains this observation?",
        "options": [
            r"Copper atoms with a mass of $63.55\text{ amu}$ are uncharged and therefore cannot be deflected by the magnetic field.",
            r"Mass spectrometers only have integer resolution and round $63.55\text{ amu}$ to $63\text{ amu}$ and $65\text{ amu}$.",
            r"Copper atoms fragment into smaller subatomic particles inside the ionization chamber of the mass spectrometer.",
            r"The value $63.55\text{ amu}$ is a weighted average of $^{63}\text{Cu}$ and $^{65}\text{Cu}$; no single copper atom has a mass of $63.55\text{ amu}$.",
        ],
        "correct_index": 3,
        "explanation": r"Mass spectrometry measures the mass-to-charge ratio of individual ions. Naturally occurring copper consists of two stable isotopes, $^{63}\text{Cu}$ ($\approx 69.2\%$) and $^{65}\text{Cu}$ ($\approx 30.8\%$). The value $63.55\text{ amu}$ is the weighted average of these two isotopes, so no individual copper atom has a mass of $63.55\text{ amu}$.",
    },

    # -------------------------------------------------------------------------
    # Topic 1.3: Elemental Composition of Pure Substances (Q14 - Q19)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 14,
        "topic_code": "1.3",
        "topic_title": "Elemental Composition of Pure Substances",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Measurement</th><th>Mass ($\text{g}$)</th></tr>
</thead>
<tbody>
<tr><td>Empty crucible and cover</td><td>$15.00$</td></tr>
<tr><td>Crucible, cover, and hydrated $\text{MgSO}_4 \cdot n\text{H}_2\text{O}$ before heating</td><td>$17.46$</td></tr>
<tr><td>Crucible, cover, and anhydrous $\text{MgSO}_4$ after 1st heating</td><td>$16.35$</td></tr>
<tr><td>Crucible, cover, and anhydrous $\text{MgSO}_4$ after 2nd heating</td><td>$16.20$</td></tr>
<tr><td>Crucible, cover, and anhydrous $\text{MgSO}_4$ after 3rd heating</td><td>$16.20$</td></tr>
</tbody>
</table>""",
        "question": r"A student heats a sample of hydrated magnesium sulfate, $\text{MgSO}_4 \cdot n\text{H}_2\text{O}$, to constant mass to determine the value of $n$. Using the data above (molar masses: $\text{MgSO}_4 = 120.37\text{ g/mol}$, $\text{H}_2\text{O} = 18.02\text{ g/mol}$), what is the integer value of $n$?",
        "options": [
            r"$2$",
            r"$5$",
            r"$6$",
            r"$7$",
        ],
        "correct_index": 3,
        "explanation": r"The mass of anhydrous $\text{MgSO}_4$ remaining after heating to constant mass is $16.20\text{ g} - 15.00\text{ g} = 1.20\text{ g}$, which corresponds to $\frac{1.20\text{ g}}{120.37\text{ g/mol}} = 0.0100\text{ mol MgSO}_4$. The mass of $\text{H}_2\text{O}$ driven off is $17.46\text{ g} - 16.20\text{ g} = 1.26\text{ g}$, which corresponds to $\frac{1.26\text{ g}}{18.02\text{ g/mol}} = 0.0700\text{ mol H}_2\text{O}$. The mole ratio is $n = \frac{0.0700\text{ mol H}_2\text{O}}{0.0100\text{ mol MgSO}_4} = 7$.",
    },
    {
        "unit_q_num": 15,
        "topic_code": "1.3",
        "topic_title": "Elemental Composition of Pure Substances",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"Complete combustion of a $1.50\text{ g}$ sample of an organic compound containing only carbon, hydrogen, and oxygen produces $2.20\text{ g}$ of $\text{CO}_2$ (molar mass $44.01\text{ g/mol}$) and $0.900\text{ g}$ of $\text{H}_2\text{O}$ (molar mass $18.02\text{ g/mol}$). What is the empirical formula of the compound?",
        "options": [
            r"$\text{CH}_2\text{O}$",
            r"$\text{C}_2\text{H}_4\text{O}$",
            r"$\text{C}_3\text{H}_6\text{O}$",
            r"$\text{CHO}_2$",
        ],
        "correct_index": 0,
        "explanation": r"Find the moles and mass of $\text{C}$ and $\text{H}$ from the combustion products: $\text{mol C} = \frac{2.20\text{ g CO}_2}{44.01\text{ g/mol}} = 0.0500\text{ mol C}$ ($\text{mass C} = 0.0500 \times 12.01 = 0.600\text{ g}$). $\text{mol H} = 2 \times \frac{0.900\text{ g H}_2\text{O}}{18.02\text{ g/mol}} = 0.100\text{ mol H}$ ($\text{mass H} = 0.100 \times 1.008 = 0.101\text{ g}$). Subtracting $\text{C}$ and $\text{H}$ from the initial sample mass gives the mass of $\text{O}$: $1.50\text{ g} - (0.600\text{ g} + 0.101\text{ g}) = 0.80\text{ g O}$, which is $\frac{0.80\text{ g}}{16.00\text{ g/mol}} = 0.050\text{ mol O}$. Dividing by $0.050\text{ mol}$ yields a $1:2:1$ ratio, so the empirical formula is $\text{CH}_2\text{O}$.",
    },
    {
        "unit_q_num": 16,
        "topic_code": "1.3",
        "topic_title": "Elemental Composition of Pure Substances",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Compound</th><th>Chemical Formula</th><th>Molar Mass ($\text{g/mol}$)</th></tr>
</thead>
<tbody>
<tr><td>Ammonia</td><td>$\text{NH}_3$</td><td>$17.03$</td></tr>
<tr><td>Urea</td><td>$\text{CO(NH}_2)_2$</td><td>$60.06$</td></tr>
<tr><td>Ammonium nitrate</td><td>$\text{NH}_4\text{NO}_3$</td><td>$80.04$</td></tr>
<tr><td>Ammonium sulfate</td><td>$(\text{NH}_4)_2\text{SO}_4$</td><td>$132.14$</td></tr>
</tbody>
</table>""",
        "question": r"Of the three solid nitrogen fertilizers listed in the table above (excluding gaseous $\text{NH}_3$), which has the highest mass percent of nitrogen?",
        "options": [
            r"Urea, $\text{CO(NH}_2)_2$, because $28.0\text{ g}$ of $\text{N}$ is divided by the smallest solid molar mass ($60.06\text{ g/mol}$)",
            r"Ammonium nitrate, $\text{NH}_4\text{NO}_3$, because nitrogen is present in both the cation and the anion",
            r"Ammonium sulfate, $(\text{NH}_4)_2\text{SO}_4$, because it has the largest molar mass",
            r"All three solids have the exact same mass percent of nitrogen because each formula unit contains two nitrogen atoms",
        ],
        "correct_index": 0,
        "explanation": r"Each of the three solid compounds contains $2\text{ mol}$ of $\text{N}$ ($2 \times 14.01 = 28.02\text{ g N}$) per mole of compound. Since mass percent of $\text{N} = \frac{28.02\text{ g}}{\text{Molar Mass}} \times 100\%$, the solid with the smallest molar mass—urea ($\frac{28.02}{60.06} \times 100\% = 46.7\%$)—has the highest mass percent of nitrogen compared to $\text{NH}_4\text{NO}_3$ ($35.0\%$) and $(\text{NH}_4)_2\text{SO}_4$ ($21.2\%$).",
    },
    {
        "unit_q_num": 17,
        "topic_code": "1.3",
        "topic_title": "Elemental Composition of Pure Substances",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A binary oxide of vanadium contains $56.0\%$ vanadium ($\text{V}$, molar mass $50.94\text{ g/mol}$) and $44.0\%$ oxygen ($\text{O}$, molar mass $16.00\text{ g/mol}$) by mass. What is the empirical formula of this oxide?",
        "options": [
            r"$\text{VO}$",
            r"$\text{V}_2\text{O}_3$",
            r"$\text{VO}_2$",
            r"$\text{V}_2\text{O}_5$",
        ],
        "correct_index": 3,
        "explanation": r"Assuming a $100.0\text{ g}$ sample: $\text{mol V} = \frac{56.0\text{ g}}{50.94\text{ g/mol}} = 1.10\text{ mol V}$ and $\text{mol O} = \frac{44.0\text{ g}}{16.00\text{ g/mol}} = 2.75\text{ mol O}$. Dividing both by $1.10\text{ mol}$ gives a ratio of $1.00\text{ V} : 2.50\text{ O}$. Multiplying by $2$ to obtain whole numbers yields $\text{V}_2\text{O}_5$.",
    },
    {
        "unit_q_num": 18,
        "topic_code": "1.3",
        "topic_title": "Elemental Composition of Pure Substances",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A gaseous hydrocarbon consists of $85.6\%$ carbon and $14.4\%$ hydrogen by mass. If the molar mass of the gas is determined to be $56.1\text{ g/mol}$, what is the molecular formula of the hydrocarbon?",
        "options": [
            r"$\text{CH}_2$",
            r"$\text{C}_2\text{H}_4$",
            r"$\text{C}_4\text{H}_8$",
            r"$\text{C}_4\text{H}_{10}$",
        ],
        "correct_index": 2,
        "explanation": r"In a $100.0\text{ g}$ sample, $\text{mol C} = \frac{85.6\text{ g}}{12.01\text{ g/mol}} = 7.13\text{ mol}$ and $\text{mol H} = \frac{14.4\text{ g}}{1.008\text{ g/mol}} = 14.3\text{ mol}$, giving an empirical formula of $\text{CH}_2$ with an empirical formula mass of $14.03\text{ g/mol}$. Dividing the molar mass by the empirical mass gives $\frac{56.1\text{ g/mol}}{14.03\text{ g/mol}} = 4$, so the molecular formula is $\text{C}_4\text{H}_8$.",
    },
    {
        "unit_q_num": 19,
        "topic_code": "1.3",
        "topic_title": "Elemental Composition of Pure Substances",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"A student determines the formula of hydrated copper(II) sulfate, $\text{CuSO}_4 \cdot x\text{H}_2\text{O}$, by heating a weighed sample in a crucible. If the student stops heating too early so that the solid residue still retains a pale blue tint from unremoved water of hydration, how will this procedural error affect the calculated mass of water lost and the experimentally determined value of $x$?",
        "options": [
            r"Calculated mass of water lost is too low; experimental value of $x$ is too low.",
            r"Calculated mass of water lost is too low; experimental value of $x$ is too high.",
            r"Calculated mass of water lost is too high; experimental value of $x$ is too high.",
            r"Calculated mass of water lost is too high; experimental value of $x$ is too low.",
        ],
        "correct_index": 0,
        "explanation": r"Because not all water was driven off, the final measured mass of the solid residue is too high. Consequently, the calculated mass of water lost ($\text{initial mass} - \text{final mass}$) is too low, and the apparent mass (and moles) of anhydrous $\text{CuSO}_4$ is too high. Since $x = \frac{\text{mol H}_2\text{O lost}}{\text{mol CuSO}_4}$, having a smaller numerator and a larger denominator causes the calculated value of $x$ to be artificially low.",
    },

    # -------------------------------------------------------------------------
    # Topic 1.4: Composition of Mixtures (Q20 - Q25)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 20,
        "topic_code": "1.4",
        "topic_title": "Composition of Mixtures",
        "difficulty": "AP Exam Level",
        "stimulus": r"""$$\text{Ag}^+(aq) + \text{Cl}^-(aq) \rightarrow \text{AgCl}(s)$$""",
        "question": r"A $2.00\text{ g}$ solid mixture consisting only of $\text{NaCl}$ (molar mass $58.44\text{ g/mol}$) and $\text{NaNO}_3$ (molar mass $85.00\text{ g/mol}$) is dissolved in distilled water. Excess $\text{AgNO}_3(aq)$ is added to precipitate all chloride ions as $\text{AgCl}(s)$ (molar mass $143.32\text{ g/mol}$). After filtering, washing, and drying to constant mass, $2.87\text{ g}$ of $\text{AgCl}(s)$ is recovered. What was the mass percent of $\text{NaCl}$ in the original mixture?",
        "options": [
            r"$29.2\%$",
            r"$41.5\%$",
            r"$58.5\%$",
            r"$69.6\%$",
        ],
        "correct_index": 2,
        "explanation": r"Calculate the moles of $\text{AgCl}(s)$ precipitated: $\text{mol AgCl} = \frac{2.87\text{ g}}{143.32\text{ g/mol}} = 0.0200\text{ mol}$. By $1:1$ stoichiometry of $\text{Cl}^-$, the mixture contained $0.0200\text{ mol NaCl}$. The mass of $\text{NaCl}$ is $0.0200\text{ mol} \times 58.44\text{ g/mol} = 1.17\text{ g}$. Thus, the mass percent of $\text{NaCl}$ in the $2.00\text{ g}$ mixture is $\frac{1.17\text{ g}}{2.00\text{ g}} \times 100\% = 58.5\%$.",
    },
    {
        "unit_q_num": 21,
        "topic_code": "1.4",
        "topic_title": "Composition of Mixtures",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Compound</th><th>Molar Mass ($\text{g/mol}$)</th><th>Mass Percent of $\text{Ca}$ ($\text{\%}$)</th></tr>
</thead>
<tbody>
<tr><td>$\text{CaCO}_3$</td><td>$100.09$</td><td>$40.0\%$</td></tr>
<tr><td>$\text{CaSO}_4$</td><td>$136.14$</td><td>$29.4\%$</td></tr>
<tr><td>$\text{CaCl}_2$</td><td>$110.98$</td><td>$36.1\%$</td></tr>
<tr><td>$\text{CaO}$</td><td>$56.08$</td><td>$71.5\%$</td></tr>
<tr><td>$\text{SiO}_2$</td><td>$60.08$</td><td>$0.0\%$</td></tr>
</tbody>
</table>""",
        "question": r"A geological sample labeled as calcium carbonate ($\text{CaCO}_3$) is known to be contaminated with a single impurity from the table above. Elemental analysis reveals that the sample contains $44.8\%$ calcium by mass. Which compound is the impurity?",
        "options": [
            r"$\text{CaSO}_4$",
            r"$\text{CaCl}_2$",
            r"$\text{CaO}$",
            r"$\text{SiO}_2$",
        ],
        "correct_index": 2,
        "explanation": r"Pure $\text{CaCO}_3$ is $40.0\%$ $\text{Ca}$ by mass. Because the contaminated sample has a higher mass percent of calcium ($44.8\%$) than pure $\text{CaCO}_3$, the impurity must have a mass percent of $\text{Ca}$ greater than $44.8\%$. Of the compounds listed, only $\text{CaO}$ ($71.5\%$ $\text{Ca}$) can raise the overall mass percent of calcium above $40.0\%$.",
    },
    {
        "unit_q_num": 22,
        "topic_code": "1.4",
        "topic_title": "Composition of Mixtures",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"In a gravimetric analysis to determine the mass percent of sulfate ($\text{SO}_4^{2-}$) in an impure fertilizer sample, a student precipitates $\text{BaSO}_4(s)$ by adding excess $\text{Ba(NO}_3)_2(aq)$, filters the precipitate, and dries it in an oven. If the student forgets to rinse the precipitate on the filter paper with distilled water before drying, how will the calculated mass percent of $\text{SO}_4^{2-}$ in the fertilizer be affected?",
        "options": [
            r"It will be artificially high because soluble spectator ions and excess $\text{Ba(NO}_3)_2$ remain trapped in the dried precipitate.",
            r"It will be artificially low because unwashed $\text{BaSO}_4(s)$ partially decomposes during oven drying.",
            r"It will be artificially low because failing to rinse prevents complete precipitation of $\text{BaSO}_4(s)$.",
            r"It will be unaffected because the oven evaporates any residual solution completely.",
        ],
        "correct_index": 0,
        "explanation": r"When the mother liquor is not rinsed from the wet precipitate with distilled water, the water evaporates in the oven but leaves behind nonvolatile dissolved solids (such as excess $\text{Ba(NO}_3)_2$ and spectator counter-ions) adhering to the $\text{BaSO}_4(s)$. This increases the measured mass of the dried solid, leading to an artificially high calculated moles and mass percent of $\text{SO}_4^{2-}$.",
    },
    {
        "unit_q_num": 23,
        "topic_code": "1.4",
        "topic_title": "Composition of Mixtures",
        "difficulty": "Challenging",
        "stimulus": r"""$$\text{Zn}(s) + 2\text{HCl}(aq) \rightarrow \text{ZnCl}_2(aq) + \text{H}_2(g)$$""",
        "question": r"A $5.00\text{ g}$ sample of brass (an alloy composed solely of copper, $\text{Cu}$, and zinc, $\text{Zn}$) is treated with excess $\text{HCl}(aq)$. Zinc reacts completely according to the equation above, while copper does not react. If $0.0250\text{ mol}$ of $\text{H}_2(g)$ is evolved, what is the mass percent of copper in the brass sample? (Molar masses: $\text{Cu} = 63.55\text{ g/mol}$, $\text{Zn} = 65.38\text{ g/mol}$)",
        "options": [
            r"$32.7\%$",
            r"$50.0\%$",
            r"$67.3\%$",
            r"$74.6\%$",
        ],
        "correct_index": 2,
        "explanation": r"From the $1:1$ stoichiometry between $\text{Zn}(s)$ and $\text{H}_2(g)$, $0.0250\text{ mol H}_2$ indicates $0.0250\text{ mol Zn}$ in the alloy. The mass of $\text{Zn}$ is $0.0250\text{ mol} \times 65.38\text{ g/mol} = 1.63\text{ g}$. Subtracting from the total alloy mass gives the mass of $\text{Cu}$: $5.00\text{ g} - 1.63\text{ g} = 3.37\text{ g}$. The mass percent of $\text{Cu}$ is $\frac{3.37\text{ g}}{5.00\text{ g}} \times 100\% = 67.3\%$.",
    },
    {
        "unit_q_num": 24,
        "topic_code": "1.4",
        "topic_title": "Composition of Mixtures",
        "difficulty": "Challenging",
        "stimulus": r"""$$\text{CaCO}_3(s) \xrightarrow{\Delta} \text{CaO}(s) + \text{CO}_2(g)$$""",
        "question": r"A $3.00\text{ g}$ mixture of $\text{CaCO}_3(s)$ (molar mass $100.09\text{ g/mol}$) and thermally inert sand, $\text{SiO}_2(s)$, is heated strongly in an open crucible until all the $\text{CaCO}_3$ decomposes according to the equation above. After cooling, the solid residue ($\text{CaO} + \text{SiO}_2$) has a total mass of $2.12\text{ g}$. What was the mass percent of $\text{CaCO}_3$ in the original mixture? (Molar mass of $\text{CO}_2 = 44.01\text{ g/mol}$)",
        "options": [
            r"$29.3\%$",
            r"$56.0\%$",
            r"$66.7\%$",
            r"$70.7\%$",
        ],
        "correct_index": 2,
        "explanation": r"The mass lost during heating is exclusively the mass of $\text{CO}_2(g)$ that escaped: $\text{mass CO}_2 = 3.00\text{ g} - 2.12\text{ g} = 0.88\text{ g}$. Convert this to moles of $\text{CO}_2$: $\frac{0.88\text{ g}}{44.01\text{ g/mol}} = 0.020\text{ mol CO}_2$. By $1:1$ stoichiometry, the original mixture contained $0.020\text{ mol CaCO}_3$, which has a mass of $0.020\text{ mol} \times 100.09\text{ g/mol} = 2.00\text{ g}$. Thus, the mass percent of $\text{CaCO}_3$ was $\frac{2.00\text{ g}}{3.00\text{ g}} \times 100\% = 66.7\%$.",
    },
    {
        "unit_q_num": 25,
        "topic_code": "1.4",
        "topic_title": "Composition of Mixtures",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A bottle labeled as pure potassium iodide ($\text{KI}$, molar mass $166.0\text{ g/mol}$, $76.45\%$ $\text{I}$ by mass) is suspected of being contaminated with another alkali halide. Chemical analysis shows that a sample from the bottle contains $80.2\%$ iodine by mass. Which of the following compounds could be the contaminant?",
        "options": [
            r"$\text{CsI}$ (molar mass $259.8\text{ g/mol}$)",
            r"$\text{RbI}$ (molar mass $212.4\text{ g/mol}$)",
            r"$\text{KCl}$ (molar mass $74.55\text{ g/mol}$)",
            r"$\text{NaI}$ (molar mass $149.9\text{ g/mol}$)",
        ],
        "correct_index": 3,
        "explanation": r"For the mixture to have a higher mass percent of iodine ($80.2\%$) than pure $\text{KI}$ ($76.45\%$), the contaminant must have a mass percent of iodine greater than $80.2\%$. Since all alkali iodides contain one $\text{I}$ atom ($126.9\text{ g/mol}$) per formula unit, only an iodide salt with a smaller molar mass than $\text{KI}$—namely $\text{NaI}$ ($\frac{126.9}{149.9} \times 100\% = 84.7\%$ $\text{I}$)—has a higher mass percent of iodine.",
    },

    # -------------------------------------------------------------------------
    # Topic 1.5: Atomic Structure and Electron Configuration (Q26 - Q31)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 26,
        "topic_code": "1.5",
        "topic_title": "Atomic Structure and Electron Configuration",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"What is the ground-state electron configuration of the iron(III) ion, $\text{Fe}^{3+}$ ($Z = 26$)?",
        "options": [
            r"$[\text{Ar}]\,3d^5$",
            r"$[\text{Ar}]\,4s^2 3d^3$",
            r"$[\text{Ar}]\,4s^1 3d^4$",
            r"$[\text{Ar}]\,3d^6$",
        ],
        "correct_index": 0,
        "explanation": r"Neutral iron ($\text{Fe}$, $Z = 26$) has the ground-state configuration $[\text{Ar}]\,4s^2 3d^6$. When a transition metal atom loses electrons to form a cation, electrons are always removed first from the subshell with the highest principal quantum number ($n$), which is the $4s$ subshell. Removing two $4s$ electrons and one $3d$ electron yields $[\text{Ar}]\,3d^5$ for $\text{Fe}^{3+}$.",
    },
    {
        "unit_q_num": 27,
        "topic_code": "1.5",
        "topic_title": "Atomic Structure and Electron Configuration",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"According to Coulomb's law, why does a $2p$ valence electron in a fluorine atom ($\text{F}$, $Z = 9$) experience a stronger attractive force to the nucleus than a $2p$ valence electron in a nitrogen atom ($\text{N}$, $Z = 7$)?",
        "options": [
            r"Fluorine has more core electrons than nitrogen, which pushes the $2p$ electrons closer to the nucleus.",
            r"The $2p$ electrons in fluorine occupy a lower principal energy level ($n$) than the $2p$ electrons in nitrogen.",
            r"Fluorine has fewer paired $2p$ electrons than nitrogen, reducing electron-electron repulsion.",
            r"Both atoms have the same number of shielding core electrons ($1s^2$), but fluorine has a larger nuclear charge ($+9$ vs. $+7$) and a slightly smaller atomic radius.",
        ],
        "correct_index": 3,
        "explanation": r"By Coulomb's law ($F \propto \frac{q_1 q_2}{r^2}$), the electrostatic attraction depends on the effective nuclear charge ($Z_{\text{eff}}$) and the distance from the nucleus ($r$). Both $\text{N}$ and $\text{F}$ have their valence electrons in the $n = 2$ shell shielded by $2$ core electrons ($1s^2$), but $\text{F}$ has $9$ protons compared to $7$ protons in $\text{N}$, giving $\text{F}$ a larger $Z_{\text{eff}}$ ($\approx +7$ vs. $\approx +5$) and a smaller radius.",
    },
    {
        "unit_q_num": 28,
        "topic_code": "1.5",
        "topic_title": "Atomic Structure and Electron Configuration",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Configuration</th><th>Electron Configuration</th></tr>
</thead>
<tbody>
<tr><td>I</td><td>$1s^2 2s^2 2p^4$</td></tr>
<tr><td>II</td><td>$1s^2 2s^2 2p^3 3s^1$</td></tr>
<tr><td>III</td><td>$1s^2 2s^3 2p^3$</td></tr>
<tr><td>IV</td><td>$1s^2 2s^2 2p^5$</td></tr>
</tbody>
</table>""",
        "question": r"Four electron configurations are shown in the table above. Which configuration represents a neutral oxygen atom ($Z = 8$) in an electronically excited state?",
        "options": [
            r"Configuration I",
            r"Configuration II",
            r"Configuration III",
            r"Configuration IV",
        ],
        "correct_index": 1,
        "explanation": r"A neutral oxygen atom ($Z = 8$) must have $8$ electrons. Configuration I ($1s^2 2s^2 2p^4$) is the ground state of oxygen. Configuration II ($1s^2 2s^2 2p^3 3s^1$) has $8$ electrons with one $2p$ electron promoted to the higher-energy $3s$ orbital, representing a valid excited state. Configuration III violates the Pauli exclusion principle ($2s^3$), and Configuration IV has $9$ electrons ($\text{F}$ or $\text{O}^-$).",
    },
    {
        "unit_q_num": 29,
        "topic_code": "1.5",
        "topic_title": "Atomic Structure and Electron Configuration",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"Paramagnetism arises from the presence of unpaired electrons in an atom or ion. Which of the following transition metal ions in its ground state has the greatest number of unpaired electrons?",
        "options": [
            r"$\text{Ti}^{2+}$",
            r"$\text{Cr}^{3+}$",
            r"$\text{Mn}^{2+}$",
            r"$\text{Zn}^{2+}$",
        ],
        "correct_index": 2,
        "explanation": r"Determine the $3d$ electron count and apply Hund's rule to the five $3d$ orbitals: $\text{Ti}^{2+}$ ($[\text{Ar}]\,3d^2$) has $2$ unpaired electrons; $\text{Cr}^{3+}$ ($[\text{Ar}]\,3d^3$) has $3$ unpaired electrons; $\text{Mn}^{2+}$ ($[\text{Ar}]\,3d^5$) has $5$ unpaired electrons (one in each of the five $3d$ orbitals); and $\text{Zn}^{2+}$ ($[\text{Ar}]\,3d^{10}$) has $0$ unpaired electrons.",
    },
    {
        "unit_q_num": 30,
        "topic_code": "1.5",
        "topic_title": "Atomic Structure and Electron Configuration",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"Which of the following species is isoelectronic with a neutral argon atom ($\text{Ar}$, $Z = 18$) in the ground state?",
        "options": [
            r"$\text{Ga}^{3+}$",
            r"$\text{Ti}^{2+}$",
            r"$\text{Sc}^{3+}$",
            r"$\text{Fe}^{2+}$",
        ],
        "correct_index": 2,
        "explanation": r"Argon has $18$ electrons ($1s^2 2s^2 2p^6 3s^2 3p^6$). Scandium ($\text{Sc}$, $Z = 21$) has $21$ electrons in the neutral atom ($[\text{Ar}]\,4s^2 3d^1$); losing all $3$ valence electrons forms $\text{Sc}^{3+}$ with $18$ electrons, which is isoelectronic with $\text{Ar}$. By contrast, $\text{Ti}^{2+}$ has $20$ electrons ($[\text{Ar}]\,3d^2$), $\text{Fe}^{2+}$ has $24$ electrons ($[\text{Ar}]\,3d^6$), and $\text{Ga}^{3+}$ has $28$ electrons ($[\text{Ar}]\,3d^{10}$).",
    },
    {
        "unit_q_num": 31,
        "topic_code": "1.5",
        "topic_title": "Atomic Structure and Electron Configuration",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"A sodium atom ($\text{Na}$, $Z = 11$) has a larger nuclear charge than a neon atom ($\text{Ne}$, $Z = 10$), yet the energy required to remove an outermost electron from $\text{Na}$ ($496\text{ kJ/mol}$) is less than one-fourth the energy required to remove an outermost electron from $\text{Ne}$ ($2081\text{ kJ/mol}$). Which statement best accounts for this difference?",
        "options": [
            r"The outermost electron in $\text{Na}$ is in the $3s$ subshell, which is at a greater average distance from the nucleus and shielded by $10$ core electrons, whereas the outermost electron in $\text{Ne}$ is in the $2p$ subshell shielded by only $2$ core electrons.",
            r"Neon has a completely filled $2p$ subshell that creates a magnetic field attracting its valence electrons more strongly than Coulombic forces predict.",
            r"Sodium has an odd number of protons in its nucleus, which lowers its nuclear binding energy and weakens electron attraction.",
            r"Electron-electron repulsion in the $3s$ orbital of $\text{Na}$ is much greater than in the $2p$ orbitals of $\text{Ne}$.",
        ],
        "correct_index": 0,
        "explanation": r"In $\text{Na}$ ($1s^2 2s^2 2p^6 3s^1$), the valence electron occupies the $n = 3$ shell at a much larger average distance $r$ from the nucleus and is shielded by $10$ inner-shell ($n = 1$ and $n = 2$) core electrons ($Z_{\text{eff}} \approx 11 - 10 = +1$). In $\text{Ne}$ ($1s^2 2s^2 2p^6$), the outermost $2p$ electrons are in the closer $n = 2$ shell shielded by only $2$ core electrons ($1s^2$), experiencing a much higher $Z_{\text{eff}}$ ($\approx 10 - 2 = +8$) and stronger Coulombic attraction.",
    },

    # -------------------------------------------------------------------------
    # Topic 1.6: Photoelectron Spectroscopy (PES) (Q32 - Q37)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 32,
        "topic_code": "1.6",
        "topic_title": "Photoelectron Spectroscopy (PES)",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Peak</th><th>Binding Energy ($\text{MJ/mol}$)</th><th>Relative Number of Electrons</th></tr>
</thead>
<tbody>
<tr><td>A</td><td>$151$</td><td>$2$</td></tr>
<tr><td>B</td><td>$11.8$</td><td>$2$</td></tr>
<tr><td>C</td><td>$7.31$</td><td>$6$</td></tr>
<tr><td>D</td><td>$1.09$</td><td>$2$</td></tr>
<tr><td>E</td><td>$0.58$</td><td>$1$</td></tr>
</tbody>
</table>""",
        "question": r"The complete photoelectron spectrum of a pure element is summarized in the table above. Which element is represented, and which subshell corresponds to Peak C?",
        "options": [
            r"Boron ($\text{B}$); Peak C represents the $2p$ subshell",
            r"Aluminum ($\text{Al}$); Peak C represents the $2p$ subshell",
            r"Aluminum ($\text{Al}$); Peak C represents the $3p$ subshell",
            r"Silicon ($\text{Si}$); Peak C represents the $2p$ subshell",
        ],
        "correct_index": 1,
        "explanation": r"Ordering the peaks from highest binding energy (closest to the nucleus) to lowest binding energy gives the electron configuration: Peak A ($151\text{ MJ/mol}$, $2\text{ e}^-$) $= 1s^2$; Peak B ($11.8\text{ MJ/mol}$, $2\text{ e}^-$) $= 2s^2$; Peak C ($7.31\text{ MJ/mol}$, $6\text{ e}^-$) $= 2p^6$; Peak D ($1.09\text{ MJ/mol}$, $2\text{ e}^-$) $= 3s^2$; Peak E ($0.58\text{ MJ/mol}$, $1\text{ e}^-$) $= 3p^1$. The total of $13$ electrons identifies aluminum ($\text{Al}$), and Peak C corresponds to the $2p$ subshell.",
    },
    {
        "unit_q_num": 33,
        "topic_code": "1.6",
        "topic_title": "Photoelectron Spectroscopy (PES)",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"When comparing the photoelectron spectra of neutral nitrogen ($\text{N}$, $Z = 7$) and neutral oxygen ($\text{O}$, $Z = 8$), how does the $1s$ peak of oxygen compare to the $1s$ peak of nitrogen?",
        "options": [
            r"The $1s$ peak of oxygen is at a higher binding energy and has the same height as the $1s$ peak of nitrogen.",
            r"The $1s$ peak of oxygen is at a higher binding energy and is taller than the $1s$ peak of nitrogen.",
            r"The $1s$ peak of oxygen is at a lower binding energy and has the same height as the $1s$ peak of nitrogen.",
            r"The $1s$ peak of oxygen is at the same binding energy as the $1s$ peak of nitrogen because both subshells contain $2$ electrons.",
        ],
        "correct_index": 0,
        "explanation": r"In both $\text{N}$ and $\text{O}$, the $1s$ subshell holds exactly $2$ electrons, so the relative heights of their $1s$ peaks are identical. However, oxygen has $8$ protons in its nucleus compared to $7$ protons in nitrogen, exerting a stronger Coulombic attraction on its $1s$ electrons and resulting in a higher binding energy ($52.6\text{ MJ/mol}$ for $\text{O}$ vs. $39.6\text{ MJ/mol}$ for $\text{N}$).",
    },
    {
        "unit_q_num": 34,
        "topic_code": "1.6",
        "topic_title": "Photoelectron Spectroscopy (PES)",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Valence Peak</th><th>Binding Energy ($\text{MJ/mol}$)</th><th>Relative Peak Height</th></tr>
</thead>
<tbody>
<tr><td>Peak X</td><td>$0.77$</td><td>$1$</td></tr>
<tr><td>Peak Y</td><td>$0.63$</td><td>$2$</td></tr>
</tbody>
</table>""",
        "question": r"The two lowest-binding-energy peaks in the photoelectron spectrum of scandium ($\text{Sc}$, $Z = 21$, $[\text{Ar}]\,4s^2 3d^1$) are given in the table above. Which of the following conclusions is directly supported by these data?",
        "options": [
            r"Peak X corresponds to the $4s$ subshell and Peak Y corresponds to the $3d$ subshell.",
            r"Scandium only forms $+1$ cations because Peak X contains a single electron.",
            r"The $3d$ electron is located at a greater average distance from the nucleus than the $4s$ electrons.",
            r"In neutral scandium, the $4s$ electrons have a lower binding energy ($0.63\text{ MJ/mol}$) than the $3d$ electron ($0.77\text{ MJ/mol}$), explaining why $4s$ electrons are removed first during ionization.",
        ],
        "correct_index": 3,
        "explanation": r"Since scandium has the valence configuration $4s^2 3d^1$, the peak of relative height $2$ (Peak Y, $0.63\text{ MJ/mol}$) corresponds to the two $4s$ electrons, and the peak of relative height $1$ (Peak X, $0.77\text{ MJ/mol}$) corresponds to the single $3d$ electron. Because the $4s$ electrons have the lower binding energy, they are easier to remove than the $3d$ electron when $\text{Sc}$ forms cations.",
    },
    {
        "unit_q_num": 35,
        "topic_code": "1.6",
        "topic_title": "Photoelectron Spectroscopy (PES)",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Peak in the Spectrum of $\text{Ne}$</th><th>Binding Energy ($\text{MJ/mol}$)</th><th>Relative Number of Electrons</th></tr>
</thead>
<tbody>
<tr><td>1</td><td>$84.0$</td><td>$2$</td></tr>
<tr><td>2</td><td>$4.68$</td><td>$2$</td></tr>
<tr><td>3</td><td>$2.08$</td><td>$6$</td></tr>
</tbody>
</table>""",
        "question": r"The complete photoelectron spectrum of a neon atom, $\text{Ne}$, is summarized in the table above. Which of the following correctly predicts how the photoelectron spectrum of a sodium ion, $\text{Na}^+$, compares with that of $\text{Ne}$?",
        "options": [
            r"The $\text{Na}^+$ spectrum has three peaks with relative heights of $2:2:6$, and each peak is at a higher binding energy than the corresponding peak of $\text{Ne}$.",
            r"The $\text{Na}^+$ spectrum is identical to the $\text{Ne}$ spectrum, with the same three peaks at the same binding energies, because the two species are isoelectronic.",
            r"The $\text{Na}^+$ spectrum has a fourth peak, of relative height $1$, at a binding energy lower than $2.08\text{ MJ/mol}$, corresponding to a $3s$ electron.",
            r"The $\text{Na}^+$ spectrum has three peaks with relative heights of $2:2:6$, but each peak is at a lower binding energy than the corresponding peak of $\text{Ne}$, because sodium has more occupied electron shells than neon.",
        ],
        "correct_index": 0,
        "explanation": r"$\text{Na}^+$ and $\text{Ne}$ are isoelectronic: both have $10$ electrons in the configuration $1s^2 2s^2 2p^6$. Their spectra therefore have the same number of peaks ($3$) with the same relative heights ($2:2:6$), because peak height reflects the number of electrons in each subshell. However, the $\text{Na}^+$ nucleus contains $11$ protons rather than $10$, so each electron, in the same subshell and with the same shielding, experiences a greater Coulombic attraction, and every peak shifts to a higher binding energy (for example, removing a $2p$ electron from $\text{Na}^+$ requires $4.56\text{ MJ/mol}$, compared with $2.08\text{ MJ/mol}$ for $\text{Ne}$). Identical spectra would ignore the difference in nuclear charge; a $3s$ peak would require the valence electron that sodium loses when it forms $\text{Na}^+$; and predicting lower binding energies confuses $\text{Na}^+$ with a neutral sodium atom, whose occupied third shell $\text{Na}^+$ no longer has.",
    },
    {
        "unit_q_num": 36,
        "topic_code": "1.6",
        "topic_title": "Photoelectron Spectroscopy (PES)",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Peak</th><th>Binding Energy ($\text{MJ/mol}$)</th><th>Relative Number of Electrons</th></tr>
</thead>
<tbody>
<tr><td>1</td><td>$126$</td><td>$2$</td></tr>
<tr><td>2</td><td>$9.07$</td><td>$2$</td></tr>
<tr><td>3</td><td>$5.31$</td><td>$6$</td></tr>
<tr><td>4</td><td>$0.74$</td><td>$2$</td></tr>
</tbody>
</table>""",
        "question": r"An unknown element has the photoelectron spectrum summarized in the table above. When this element reacts with chlorine gas, what is the empirical formula of the resulting compound?",
        "options": [
            r"$\text{XCl}$",
            r"$\text{XCl}_2$",
            r"$\text{XCl}_3$",
            r"$\text{X}_2\text{Cl}$",
        ],
        "correct_index": 1,
        "explanation": r"The relative electron counts ($2, 2, 6, 2$) correspond to the electron configuration $1s^2 2s^2 2p^6 3s^2$, which is magnesium ($\text{Mg}$, Group 2). With two valence electrons in the $3s$ subshell ($0.74\text{ MJ/mol}$), element $\text{X}$ readily loses $2$ electrons to form $\text{X}^{2+}$ ions, combining with $\text{Cl}^-$ ions in a $1:2$ ratio to form $\text{XCl}_2$.",
    },
    {
        "unit_q_num": 37,
        "topic_code": "1.6",
        "topic_title": "Photoelectron Spectroscopy (PES)",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Element</th><th>$1s$ Binding Energy ($\text{MJ/mol}$)</th><th>$2s$ Binding Energy ($\text{MJ/mol}$)</th><th>$2p$ Binding Energy ($\text{MJ/mol}$)</th></tr>
</thead>
<tbody>
<tr><td>Nitrogen ($\text{N}$, $Z = 7$)</td><td>$39.6$</td><td>$2.45$</td><td>$1.40$</td></tr>
<tr><td>Oxygen ($\text{O}$, $Z = 8$)</td><td>$52.6$</td><td>$3.12$</td><td>$1.31$</td></tr>
</tbody>
</table>""",
        "question": r"As shown in the table above, the $1s$ and $2s$ peaks of oxygen have higher binding energies than the corresponding peaks of nitrogen, but the $2p$ peak of oxygen has a slightly lower binding energy ($1.31\text{ MJ/mol}$) than the $2p$ peak of nitrogen ($1.40\text{ MJ/mol}$). Which statement best explains why the $2p$ binding energy of oxygen is lower?",
        "options": [
            r"Oxygen has more core electrons in its $1s$ subshell than nitrogen, increasing core shielding of the $2p$ subshell.",
            r"The $2p$ subshell of oxygen is farther from the nucleus than the $2p$ subshell of nitrogen.",
            r"Nitrogen has a completely filled $2p$ subshell, whereas oxygen has a partially filled $2p$ subshell.",
            r"In oxygen ($2p^4$), two electrons must pair in one of the $2p$ orbitals, and the resulting electron-electron repulsion slightly reduces the energy required to remove one of the paired $2p$ electrons.",
        ],
        "correct_index": 3,
        "explanation": r"Nitrogen ($2p^3$) has three unpaired electrons in separate $2p$ orbitals ($\uparrow\ \uparrow\ \uparrow$). Oxygen ($2p^4$) must pair two electrons in one $2p$ orbital ($\uparrow\downarrow\ \uparrow\ \uparrow$). The increased Coulombic electron-electron repulsion between the two electrons sharing the same $2p$ orbital slightly raises the energy of that electron and makes it easier to remove, lowering its binding energy from $1.40\text{ MJ/mol}$ to $1.31\text{ MJ/mol}$.",
    },

    # -------------------------------------------------------------------------
    # Topic 1.7: Periodic Trends (Q38 - Q44)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 38,
        "topic_code": "1.7",
        "topic_title": "Periodic Trends",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Ionization Step</th><th>Ionization Energy ($\text{kJ/mol}$)</th></tr>
</thead>
<tbody>
<tr><td>$I_1$</td><td>$578$</td></tr>
<tr><td>$I_2$</td><td>$1,817$</td></tr>
<tr><td>$I_3$</td><td>$2,745$</td></tr>
<tr><td>$I_4$</td><td>$11,577$</td></tr>
<tr><td>$I_5$</td><td>$14,842$</td></tr>
</tbody>
</table>""",
        "question": r"The first five successive ionization energies for a Period 3 element are shown in the table above. Which of the following is the most likely identity of this element?",
        "options": [
            r"$\text{Mg}$",
            r"$\text{Al}$",
            r"$\text{Si}$",
            r"$\text{P}$",
        ],
        "correct_index": 1,
        "explanation": r"There is an enormous jump between $I_3$ ($2,745\text{ kJ/mol}$) and $I_4$ ($11,577\text{ kJ/mol}$), indicating that the fourth electron is removed from an inner core shell ($n = 2$) after three valence electrons ($n = 3$) have been removed. A Period 3 element with $3$ valence electrons is aluminum ($\text{Al}$).",
    },
    {
        "unit_q_num": 39,
        "topic_code": "1.7",
        "topic_title": "Periodic Trends",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"Which of the following correctly lists the isoelectronic ions $\text{S}^{2-}$, $\text{Cl}^-$, $\text{K}^+$, and $\text{Ca}^{2+}$ in order of increasing ionic radius (from smallest to largest)?",
        "options": [
            r"$\text{Ca}^{2+} < \text{K}^+ < \text{Cl}^- < \text{S}^{2-}$",
            r"$\text{S}^{2-} < \text{Cl}^- < \text{K}^+ < \text{Ca}^{2+}$",
            r"$\text{K}^+ < \text{Ca}^{2+} < \text{S}^{2-} < \text{Cl}^-$",
            r"$\text{Cl}^- < \text{S}^{2-} < \text{Ca}^{2+} < \text{K}^+$",
        ],
        "correct_index": 0,
        "explanation": r"All four ions are isoelectronic with $18$ electrons ($1s^2 2s^2 2p^6 3s^2 3p^6$). Because the electron configuration and core shielding are identical, ionic radius is governed by the nuclear charge ($Z$): $\text{Ca}^{2+}$ ($Z = 20$) pulls the $18$-electron cloud tightest, followed by $\text{K}^+$ ($Z = 19$), $\text{Cl}^-$ ($Z = 17$), and $\text{S}^{2-}$ ($Z = 16$). Thus, $\text{Ca}^{2+} < \text{K}^+ < \text{Cl}^- < \text{S}^{2-}$.",
    },
    {
        "unit_q_num": 40,
        "topic_code": "1.7",
        "topic_title": "Periodic Trends",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"Although first ionization energy generally increases across Period 3 from left to right, the first ionization energy of aluminum ($\text{Al}$, $578\text{ kJ/mol}$) is lower than that of magnesium ($\text{Mg}$, $738\text{ kJ/mol}$). Which of the following best explains this anomaly?",
        "options": [
            r"Magnesium has paired electrons in its $3s$ orbital, which increases the attraction between the nucleus and the $3s$ electrons.",
            r"Aluminum has a larger atomic radius than magnesium, weakening the Coulombic attraction to its valence electrons.",
            r"Aluminum loses three electrons simultaneously during its first ionization step, whereas magnesium loses only one.",
            r"The outermost electron in aluminum occupies a $3p$ orbital, which is higher in energy, slightly farther from the nucleus on average, and partially shielded by the $3s^2$ electrons compared to a $3s$ electron in magnesium.",
        ],
        "correct_index": 3,
        "explanation": r"In $\text{Mg}$ ($[\text{Ne}]\,3s^2$), the ionized electron is removed from the $3s$ subshell. In $\text{Al}$ ($[\text{Ne}]\,3s^2 3p^1$), the ionized electron is removed from the $3p$ subshell, which penetrates the core less effectively than the $3s$ subshell, sits at a slightly larger average distance from the nucleus, and experiences additional shielding from the $3s^2$ electrons.",
    },
    {
        "unit_q_num": 41,
        "topic_code": "1.7",
        "topic_title": "Periodic Trends",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"Fluorine ($\text{F}$) is the most electronegative element on the periodic table, yet chlorine ($\text{Cl}$) has a slightly more exothermic electron affinity ($\Delta H_{\text{EA}} = -349\text{ kJ/mol}$) than fluorine ($\Delta H_{\text{EA}} = -328\text{ kJ/mol}$). What is the primary reason that adding an electron to a neutral $\text{F}(g)$ atom is slightly less exothermic than adding an electron to a neutral $\text{Cl}(g)$ atom?",
        "options": [
            r"Chlorine has a higher effective nuclear charge ($Z_{\text{eff}}$) than fluorine.",
            r"Because the $2p$ valence shell of fluorine is extremely small and compact, adding an extra electron introduces significant electron-electron repulsion.",
            r"Chlorine places the incoming electron into an empty $3d$ orbital where there is no electron-electron repulsion.",
            r"Fluorine has more core shells shielding the nucleus than chlorine.",
        ],
        "correct_index": 1,
        "explanation": r"While an incoming electron is closer to the nucleus in $\text{F}$ ($n = 2$) than in $\text{Cl}$ ($n = 3$), the $2p$ subshell of $\text{F}$ occupies a very small volume already crowded with $5$ valence electrons. The strong interelectronic repulsion experienced by an incoming electron entering the compact $n = 2$ shell partially offsets the nuclear attraction, making $\text{F}$'s electron affinity slightly less exothermic than $\text{Cl}$'s.",
    },
    {
        "unit_q_num": 42,
        "topic_code": "1.7",
        "topic_title": "Periodic Trends",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Alkali Metal</th><th>Atomic Radius ($\text{pm}$)</th><th>First Ionization Energy ($\text{kJ/mol}$)</th></tr>
</thead>
<tbody>
<tr><td>$\text{Li}$</td><td>$152$</td><td>$520$</td></tr>
<tr><td>$\text{Na}$</td><td>$186$</td><td>$496$</td></tr>
<tr><td>$\text{K}$</td><td>$227$</td><td>$419$</td></tr>
<tr><td>$\text{Rb}$</td><td>$248$</td><td>$403$</td></tr>
</tbody>
</table>""",
        "question": r"The atomic radii and first ionization energies of the first four Group 1 alkali metals are shown in the table above. Which statement best explains why the first ionization energy decreases down the group?",
        "options": [
            r"The effective nuclear charge ($Z_{\text{eff}}$) decreases significantly from $\text{Li}$ to $\text{Rb}$.",
            r"Protons in heavier nuclei are shielded by a larger number of neutrons, reducing nuclear attraction.",
            r"As principal quantum number $n$ increases down the group, the valence electron is at a greater average distance from the nucleus, weakening Coulombic attraction.",
            r"Heavier alkali metals have paired valence electrons that repel one another.",
        ],
        "correct_index": 2,
        "explanation": r"Moving down Group 1 from $\text{Li}$ ($2s^1$) to $\text{Rb}$ ($5s^1$), the valence electron occupies progressively higher principal energy levels ($n$) and is shielded by additional inner shells of core electrons. Because the average distance $r$ between the nucleus and the valence electron increases, Coulomb's law ($F \propto \frac{q_1 q_2}{r^2}$) dictates that the attractive force decreases, requiring less energy to remove the electron.",
    },
    {
        "unit_q_num": 43,
        "topic_code": "1.7",
        "topic_title": "Periodic Trends",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"Which of the Period 3 elements—$\text{Na}$, $\text{Mg}$, $\text{Al}$, or $\text{Si}$—has the largest second ionization energy ($I_2$), and why?",
        "options": [
            r"$\text{Si}$, because it has the largest nuclear charge ($Z = 14$) of the four elements.",
            r"$\text{Mg}$, because its second ionization removes the last electron from the $3s$ subshell.",
            r"$\text{Na}$, because removing a second electron from $\text{Na}^+$ requires removing a core $2p$ electron from the $n = 2$ shell.",
            r"$\text{Al}$, because removing a second electron disrupts a completely filled $3s^2$ subshell.",
        ],
        "correct_index": 2,
        "explanation": r"After losing its single $3s^1$ valence electron, $\text{Na}^+$ has the noble-gas core configuration $1s^2 2s^2 2p^6$. The second ionization ($I_2$) of sodium therefore requires removing an electron from the inner $2p$ core shell, which is much closer to the nucleus and experiences a much greater effective nuclear charge than the $n = 3$ valence electrons removed during $I_2$ of $\text{Mg}$, $\text{Al}$, or $\text{Si}$.",
    },
    {
        "unit_q_num": 44,
        "topic_code": "1.7",
        "topic_title": "Periodic Trends",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"How does the radius of a neutral iron atom ($\text{Fe}$) compare to the radii of its common cations, $\text{Fe}^{2+}$ and $\text{Fe}^{3+}$, and why?",
        "options": [
            r"$\text{Fe}^{3+} < \text{Fe}^{2+} < \text{Fe}$, because removing electrons while keeping the nuclear charge constant (+26) reduces electron-electron repulsion and contracts the electron cloud.",
            r"$\text{Fe} < \text{Fe}^{2+} < \text{Fe}^{3+}$, because losing negatively charged electrons causes the positively charged protons in the nucleus to repel one another and expand the ion.",
            r"$\text{Fe}^{3+} = \text{Fe}^{2+} < \text{Fe}$, because both cations have lost their $4s$ shell and have the same number of occupied principal energy levels.",
            r"$\text{Fe}^{2+} < \text{Fe}^{3+} < \text{Fe}$, because $\text{Fe}^{3+}$ has a half-filled $3d^5$ subshell that expands to minimize repulsion.",
        ],
        "correct_index": 0,
        "explanation": r"All three species have the same nuclear charge ($26$ protons). Removing the $4s^2$ electrons from $\text{Fe}$ to form $\text{Fe}^{2+}$ vacates the $n = 4$ shell and decreases electron-electron repulsion, substantially shrinking the radius. Removing an additional $3d$ electron to form $\text{Fe}^{3+}$ further reduces electron-electron repulsion among the remaining $23$ electrons, pulling the electron cloud even closer to the nucleus ($\text{Fe}^{3+} < \text{Fe}^{2+} < \text{Fe}$).",
    },

    # -------------------------------------------------------------------------
    # Topic 1.8: Valence Electrons and Ionic Compounds (Q45 - Q50)
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 45,
        "topic_code": "1.8",
        "topic_title": "Valence Electrons and Ionic Compounds",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"Calcium ($\text{Ca}$) and phosphorus ($\text{P}$) react with oxygen to form the ionic compound calcium phosphate, $\text{Ca}_3(\text{PO}_4)_2$. Based on periodic group trends in valence electron configuration, what is the expected chemical formula of strontium arsenate, an analogous compound containing strontium ($\text{Sr}$) and arsenic ($\text{As}$)?",
        "options": [
            r"$\text{SrAsO}_4$",
            r"$\text{Sr}_2(\text{AsO}_4)_3$",
            r"$\text{Sr}_3(\text{AsO}_4)_2$",
            r"$\text{Sr}_3\text{As}_2\text{O}_4$",
        ],
        "correct_index": 2,
        "explanation": r"Strontium ($\text{Sr}$) is in Group 2 directly below calcium ($\text{Ca}$), so it has $2$ valence electrons and forms $\text{Sr}^{2+}$ ions. Arsenic ($\text{As}$) is in Group 15 directly below phosphorus ($\text{P}$), so it has $5$ valence electrons and forms the analogous oxoanion arsenate, $\text{AsO}_4^{3-}$. Balancing $+2$ and $-3$ charges gives $\text{Sr}_3(\text{AsO}_4)_2$.",
    },
    {
        "unit_q_num": 46,
        "topic_code": "1.8",
        "topic_title": "Valence Electrons and Ionic Compounds",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Ionic Compound</th><th>Interionic Distance ($\text{pm}$)</th><th>Melting Point ($^\circ\text{C}$)</th><th>Lattice Energy ($\text{kJ/mol}$)</th></tr>
</thead>
<tbody>
<tr><td>$\text{NaF}$</td><td>$231$</td><td>$993$</td><td>$923$</td></tr>
<tr><td>$\text{MgO}$</td><td>$210$</td><td>$2,852$</td><td>$3,791$</td></tr>
</tbody>
</table>""",
        "question": r"Based on the data in the table above, why is the lattice energy of $\text{MgO}$ roughly four times as large as that of $\text{NaF}$ (consistent with the much higher melting point of $\text{MgO}$)?",
        "options": [
            r"$\text{MgO}$ has a slightly larger molar mass than $\text{NaF}$, resulting in stronger London dispersion forces between formula units.",
            r"$\text{Mg}^{2+}$ and $\text{O}^{2-}$ have more occupied electron shells than $\text{Na}^+$ and $\text{F}^-$.",
            r"$\text{MgO}$ forms a covalent network solid, whereas $\text{NaF}$ forms an ionic crystal lattice.",
            r"According to Coulomb's law, $\text{MgO}$ consists of $+2$ and $-2$ ions ($\text{Mg}^{2+}$ and $\text{O}^{2-}$), whereas $\text{NaF}$ consists of $+1$ and $-1$ ions ($\text{Na}^+$ and $\text{F}^-$), quadrupling the numerator $|q_1 q_2|$.",
        ],
        "correct_index": 3,
        "explanation": r"Both $\text{NaF}$ ($\text{Na}^+$ and $\text{F}^-$) and $\text{MgO}$ ($\text{Mg}^{2+}$ and $\text{O}^{2-}$) consist of ions that are isoelectronic with neon ($10\text{ e}^-$) and have very similar interionic distances ($231\text{ pm}$ vs. $210\text{ pm}$). By Coulomb's law ($E \propto \frac{|q_1 q_2|}{r}$), the product of ionic charges in $\text{MgO}$ ($|(+2)(-2)| = 4$) is four times as large as in $\text{NaF}$ ($|(+1)(-1)| = 1$), accounting for the nearly fourfold increase in lattice energy.",
    },
    {
        "unit_q_num": 47,
        "topic_code": "1.8",
        "topic_title": "Valence Electrons and Ionic Compounds",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A main-group metal $\text{M}$ forms an ionic oxide with the empirical formula $\text{M}_2\text{O}$ and an ionic sulfide with the empirical formula $\text{M}_2\text{S}$. Which of the following could be the ground-state valence electron configuration of neutral atom $\text{M}$?",
        "options": [
            r"$4s^1$",
            r"$4s^2$",
            r"$3s^2 3p^1$",
            r"$3s^2 3p^5$",
        ],
        "correct_index": 0,
        "explanation": r"Since oxygen and sulfur (Group 16) form $\text{O}^{2-}$ and $\text{S}^{2-}$ anions in ionic compounds, the empirical formulas $\text{M}_2\text{O}$ and $\text{M}_2\text{S}$ indicate that metal $\text{M}$ forms $\text{M}^+$ cations. A main-group metal that forms a $+1$ ion belongs to Group 1 (alkali metals) and has a $ns^1$ valence electron configuration, such as $4s^1$ ($\text{K}$).",
    },
    {
        "unit_q_num": 48,
        "topic_code": "1.8",
        "topic_title": "Valence Electrons and Ionic Compounds",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"Which of the following alkali halide salts has the smallest magnitude of lattice energy?",
        "options": [
            r"$\text{LiF}$",
            r"$\text{NaCl}$",
            r"$\text{KBr}$",
            r"$\text{CsI}$",
        ],
        "correct_index": 3,
        "explanation": r"All four alkali halides consist of $+1$ cations and $-1$ anions, so the charge product $|q_1 q_2| = 1$ is identical for all of them. According to Coulomb's law ($E \propto \frac{|q_1 q_2|}{r}$), lattice energy is inversely proportional to the interionic distance $r$. Because $\text{Cs}^+$ ($n = 5$ core) and $\text{I}^-$ ($n = 5$ valence) have the largest ionic radii among the ions listed, $\text{CsI}$ has the largest interionic distance and therefore the smallest lattice energy.",
    },
    {
        "unit_q_num": 49,
        "topic_code": "1.8",
        "topic_title": "Valence Electrons and Ionic Compounds",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Element</th><th>Ground-State Electron Configuration</th></tr>
</thead>
<tbody>
<tr><td>Element $\text{X}$</td><td>$1s^2 2s^2 2p^6 3s^2$</td></tr>
<tr><td>Element $\text{Y}$</td><td>$1s^2 2s^2 2p^5$</td></tr>
</tbody>
</table>""",
        "question": r"The ground-state electron configurations of two elements, $\text{X}$ and $\text{Y}$, are given in the table above. When $\text{X}$ and $\text{Y}$ react, what type of compound is formed and what is its empirical formula?",
        "options": [
            r"A molecular compound with formula $\text{XY}_2$",
            r"An ionic compound with formula $\text{XY}_2$",
            r"An ionic compound with formula $\text{X}_2\text{Y}$",
            r"A molecular compound with formula $\text{X}_2\text{Y}_5$",
        ],
        "correct_index": 1,
        "explanation": r"Element $\text{X}$ ($1s^2 2s^2 2p^6 3s^2$, magnesium) is a Group 2 metal with $2$ valence electrons that loses $2$ electrons to form $\text{X}^{2+}$. Element $\text{Y}$ ($1s^2 2s^2 2p^5$, fluorine) is a Group 17 nonmetal with $7$ valence electrons that gains $1$ electron to form $\text{Y}^-$. Combining $\text{X}^{2+}$ and $\text{Y}^-$ in a $1:2$ ratio produces an ionic compound with empirical formula $\text{XY}_2$ ($\text{MgF}_2$).",
    },
    {
        "unit_q_num": 50,
        "topic_code": "1.8",
        "topic_title": "Valence Electrons and Ionic Compounds",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Element</th><th>$I_1$ ($\text{kJ/mol}$)</th><th>$I_2$ ($\text{kJ/mol}$)</th></tr>
</thead>
<tbody>
<tr><td>$\text{Na}$ ($Z = 11$)</td><td>$496$</td><td>$4,562$</td></tr>
<tr><td>$\text{Mg}$ ($Z = 12$)</td><td>$738$</td><td>$1,451$</td></tr>
</tbody>
</table>""",
        "question": r"Although sodium has a lower first ionization energy than magnesium, sodium exclusively forms $+1$ ions ($\text{NaCl}$) when reacting with chlorine, whereas magnesium exclusively forms $+2$ ions ($\text{MgCl}_2$). Based on the ionization energies in the table above, why does sodium not form stable $\text{NaCl}_2(s)$?",
        "options": [
            r"The $\text{Na}^{2+}$ ion is too large to fit into a crystal lattice with two $\text{Cl}^-$ ions.",
            r"Removing a second electron from $\text{Na}$ requires breaking into the $n = 2$ core shell ($I_2 = 4,562\text{ kJ/mol}$), an enormous energy cost that cannot be compensated by the additional lattice energy of forming $\text{NaCl}_2(s)$.",
            r"Chlorine atoms can only accept one electron from Group 1 metals but can accept two electrons from Group 2 metals.",
            r"The first ionization of magnesium is exothermic, whereas the second ionization of sodium is endothermic.",
        ],
        "correct_index": 1,
        "explanation": r"All ionization energies are endothermic. While forming a $+2$ cation doubles the ionic charge and increases lattice energy, forming $\text{Na}^{2+}$ requires removing a $2p$ core electron ($I_2 = 4,562\text{ kJ/mol}$), which costs over $3,100\text{ kJ/mol}$ more than removing the second $3s$ valence electron from $\text{Mg}$ ($I_2 = 1,451\text{ kJ/mol}$). This massive core-ionization energy penalty cannot be recovered by the lattice energy of $\text{NaCl}_2(s)$.",
    },

    # -------------------------------------------------------------------------
    # Added 2026-10-03 — Blind-spot coverage (Fall 2024 CED): topics 1.1–1.8
    # -------------------------------------------------------------------------
    {
        "unit_q_num": 51,
        "topic_code": "1.1",
        "topic_title": "Moles and Molar Mass",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"The average mass of one molecule of sucrose, $\text{C}_{12}\text{H}_{22}\text{O}_{11}$, is $342.3\text{ amu}$. Because molecules are far too small to count individually, a student who needs a sample containing $1.00 \times 10^{22}$ sucrose molecules decides to measure out the sample by mass on a balance. What mass of sucrose should the student measure out?",
        "options": [
            r"$4.85 \times 10^{-5}\text{ g}$",
            r"$1.66 \times 10^{-2}\text{ g}$",
            r"$5.68\text{ g}$",
            r"$3.42 \times 10^{24}\text{ g}$",
        ],
        "correct_index": 2,
        "explanation": r"The average mass of one particle in amu is numerically equal to the molar mass in grams, so sucrose has a molar mass of $342.3\text{ g/mol}$. Convert the number of molecules to moles with Avogadro's number: $\frac{1.00 \times 10^{22}}{6.022 \times 10^{23}\text{ mol}^{-1}} = 0.01661\text{ mol}$. Then $m = nM = 0.01661\text{ mol} \times 342.3\text{ g/mol} = 5.68\text{ g}$. The value $1.66 \times 10^{-2}\text{ g}$ is the number of moles mislabeled as grams, $4.85 \times 10^{-5}\text{ g}$ results from dividing the moles by the molar mass instead of multiplying, and $3.42 \times 10^{24}\text{ g}$ is the total mass in amu ($1.00 \times 10^{22} \times 342.3\text{ amu}$) mistakenly reported in grams.",
    },
    {
        "unit_q_num": 52,
        "topic_code": "1.2",
        "topic_title": "Mass Spectra of Elements",
        "difficulty": "Challenging",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 300" role="img" font-family="sans-serif" aria-label="Mass spectrum of a pure element. The vertical axis is relative intensity from 0 to 100 and the horizontal axis is mass-to-charge ratio from 4 to 9. There are two peaks: a short peak of relative intensity 8.2 at m/z 6 and a tall peak of relative intensity 100 at m/z 7.">
<line x1="70" y1="212" x2="490" y2="212" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="174" x2="490" y2="174" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="136" x2="490" y2="136" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="98" x2="490" y2="98" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="60" x2="490" y2="60" stroke="#e5e7eb" stroke-width="1"/>
<line x1="70" y1="250" x2="490" y2="250" stroke="#111827" stroke-width="2"/>
<line x1="70" y1="250" x2="70" y2="40" stroke="#111827" stroke-width="2"/>
<line x1="64" y1="250" x2="70" y2="250" stroke="#111827" stroke-width="1.5"/>
<text x="59" y="254" font-size="12" text-anchor="end" fill="#111827">0</text>
<line x1="64" y1="212" x2="70" y2="212" stroke="#111827" stroke-width="1.5"/>
<text x="59" y="216" font-size="12" text-anchor="end" fill="#111827">20</text>
<line x1="64" y1="174" x2="70" y2="174" stroke="#111827" stroke-width="1.5"/>
<text x="59" y="178" font-size="12" text-anchor="end" fill="#111827">40</text>
<line x1="64" y1="136" x2="70" y2="136" stroke="#111827" stroke-width="1.5"/>
<text x="59" y="140" font-size="12" text-anchor="end" fill="#111827">60</text>
<line x1="64" y1="98" x2="70" y2="98" stroke="#111827" stroke-width="1.5"/>
<text x="59" y="102" font-size="12" text-anchor="end" fill="#111827">80</text>
<line x1="64" y1="60" x2="70" y2="60" stroke="#111827" stroke-width="1.5"/>
<text x="59" y="64" font-size="12" text-anchor="end" fill="#111827">100</text>
<line x1="90" y1="250" x2="90" y2="256" stroke="#111827" stroke-width="1.5"/>
<text x="90" y="271" font-size="12" text-anchor="middle" fill="#111827">4</text>
<line x1="166" y1="250" x2="166" y2="256" stroke="#111827" stroke-width="1.5"/>
<text x="166" y="271" font-size="12" text-anchor="middle" fill="#111827">5</text>
<line x1="242" y1="250" x2="242" y2="256" stroke="#111827" stroke-width="1.5"/>
<text x="242" y="271" font-size="12" text-anchor="middle" fill="#111827">6</text>
<line x1="318" y1="250" x2="318" y2="256" stroke="#111827" stroke-width="1.5"/>
<text x="318" y="271" font-size="12" text-anchor="middle" fill="#111827">7</text>
<line x1="394" y1="250" x2="394" y2="256" stroke="#111827" stroke-width="1.5"/>
<text x="394" y="271" font-size="12" text-anchor="middle" fill="#111827">8</text>
<line x1="470" y1="250" x2="470" y2="256" stroke="#111827" stroke-width="1.5"/>
<text x="470" y="271" font-size="12" text-anchor="middle" fill="#111827">9</text>
<rect x="235" y="234.4" width="14" height="15.6" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="242" y="227.4" font-size="12" text-anchor="middle" fill="#111827">8.2</text>
<rect x="311" y="60" width="14" height="190" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="318" y="53" font-size="12" text-anchor="middle" fill="#111827">100</text>
<text x="280" y="292" font-size="13" text-anchor="middle" fill="#111827">Mass-to-Charge Ratio (m/z)</text>
<text x="22" y="145" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 22 145)">Relative Intensity</text>
</svg>
<figcaption>Figure: Mass spectrum of a pure element (intensities scaled so that the tallest peak = 100)</figcaption>
</figure>""",
        "question": r"The mass spectrum of a pure sample of an element is shown above. The relative intensities are scaled so that the tallest peak has a value of $100$. The isotope responsible for the peak at $m/z = 6$ has a mass of $6.015\text{ amu}$, and the isotope responsible for the peak at $m/z = 7$ has a mass of $7.016\text{ amu}$. Based on the spectrum, what is the average atomic mass of the element?",
        "options": [
            r"$7.51\text{ amu}$",
            r"$6.94\text{ amu}$",
            r"$6.52\text{ amu}$",
            r"$6.09\text{ amu}$",
        ],
        "correct_index": 1,
        "explanation": r"Because the intensities are scaled to the tallest peak rather than given as percentages, first convert them to fractional abundances by dividing each by the total, $8.2 + 100 = 108.2$: the $m/z = 6$ isotope is $\frac{8.2}{108.2} = 0.0758$ ($7.58\%$) and the $m/z = 7$ isotope is $\frac{100}{108.2} = 0.924$ ($92.4\%$). The weighted average is $(0.0758)(6.015\text{ amu}) + (0.924)(7.016\text{ amu}) = 6.94\text{ amu}$, which identifies the element as lithium. The value $7.51\text{ amu}$ comes from dividing by $100$ instead of $108.2$ (an average larger than the mass of the heaviest isotope is impossible), $6.52\text{ amu}$ is the unweighted mean of the two isotopic masses, and $6.09\text{ amu}$ assigns the larger abundance to the lighter isotope.",
    },
    {
        "unit_q_num": 53,
        "topic_code": "1.3",
        "topic_title": "Elemental Composition of Pure Substances",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th>Trial</th><th>Mass of $\text{Cu}$ Used ($\text{g}$)</th><th>Mass of $\text{S}$ Used ($\text{g}$)</th><th>Mass of Copper Sulfide Formed ($\text{g}$)</th></tr>
</thead>
<tbody>
<tr><td>1</td><td>$0.500$</td><td>$2.00$</td><td>$0.626$</td></tr>
<tr><td>2</td><td>$1.000$</td><td>$2.00$</td><td>$1.252$</td></tr>
<tr><td>3</td><td>$1.500$</td><td>$2.00$</td><td>$1.878$</td></tr>
</tbody>
</table>""",
        "question": r"A student heats different masses of pure copper wire with $2.00\text{ g}$ of sulfur, an excess, in a crucible until the reaction is complete and all of the unreacted sulfur has burned off. The solid copper sulfide that remains is cooled and weighed. The data are shown in the table above. Which of the following scientific questions can be answered using these data?",
        "options": [
            r"Is the ratio of the mass of sulfur to the mass of copper in the product the same regardless of how much copper reacts?",
            r"Does the mass of copper sulfide formed depend on the mass of sulfur used in the reaction?",
            r"Does copper react with sulfur more rapidly when a larger mass of copper is used?",
            r"Does the temperature at which the crucible is heated affect the mass of copper sulfide formed?",
        ],
        "correct_index": 0,
        "explanation": r"Only the mass of copper was varied, and the mass of sulfur that combined with the copper can be calculated from the data: $0.626 - 0.500 = 0.126\text{ g}$, $1.252 - 1.000 = 0.252\text{ g}$, and $1.878 - 1.500 = 0.378\text{ g}$. The mass ratio of sulfur to copper in the product is $0.252$ in every trial, so these data directly test whether the compound has a fixed composition by mass (the law of definite proportions). The mass of sulfur used was the same (and in excess) in every trial, so its effect cannot be determined; no times were recorded, so the reaction rate cannot be evaluated; and the heating temperature was neither varied nor measured.",
    },
    {
        "unit_q_num": 54,
        "topic_code": "1.4",
        "topic_title": "Composition of Mixtures",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 345" role="img" font-family="sans-serif" aria-label="Four particle diagrams. Diagram I: identical diatomic molecules, each made of two light-colored atoms of the same element. Diagram II: a regular checkerboard array of small gray positive ions and larger light negative ions in a 1 to 1 ratio. Diagram III: identical bent molecules, each made of one dark atom bonded to two small light-colored atoms. Diagram IV: a mixture of the diatomic molecules of diagram I and the bent molecules of diagram III.">
<rect x="10" y="28" width="240" height="140" fill="white" stroke="#374151" stroke-width="1.5"/>
<text x="130" y="19" font-size="14" font-weight="bold" text-anchor="middle" fill="#111827">I</text>
<rect x="270" y="28" width="240" height="140" fill="white" stroke="#374151" stroke-width="1.5"/>
<text x="390" y="19" font-size="14" font-weight="bold" text-anchor="middle" fill="#111827">II</text>
<rect x="10" y="200" width="240" height="140" fill="white" stroke="#374151" stroke-width="1.5"/>
<text x="130" y="191" font-size="14" font-weight="bold" text-anchor="middle" fill="#111827">III</text>
<rect x="270" y="200" width="240" height="140" fill="white" stroke="#374151" stroke-width="1.5"/>
<text x="390" y="191" font-size="14" font-weight="bold" text-anchor="middle" fill="#111827">IV</text>
<circle cx="41.2" cy="58.8" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="54.8" cy="65.2" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="111.9" cy="60.3" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="124.1" cy="51.7" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="196.7" cy="54.6" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="199.3" cy="69.4" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="64.8" cy="126.8" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="71.2" cy="113.2" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="132.5" cy="103.3" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="147.5" cy="104.7" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="201.2" cy="135.2" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="214.8" cy="128.8" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="112.3" cy="145.2" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="123.7" cy="154.8" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="315" cy="53" r="13" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<text x="315" y="57.5" font-size="13" text-anchor="middle" fill="#111827">−</text>
<circle cx="345" cy="53" r="8.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="345" y="57" font-size="11" text-anchor="middle" fill="#111827">+</text>
<circle cx="375" cy="53" r="13" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<text x="375" y="57.5" font-size="13" text-anchor="middle" fill="#111827">−</text>
<circle cx="405" cy="53" r="8.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="405" y="57" font-size="11" text-anchor="middle" fill="#111827">+</text>
<circle cx="435" cy="53" r="13" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<text x="435" y="57.5" font-size="13" text-anchor="middle" fill="#111827">−</text>
<circle cx="465" cy="53" r="8.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="465" y="57" font-size="11" text-anchor="middle" fill="#111827">+</text>
<circle cx="315" cy="83" r="8.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="315" y="87" font-size="11" text-anchor="middle" fill="#111827">+</text>
<circle cx="345" cy="83" r="13" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<text x="345" y="87.5" font-size="13" text-anchor="middle" fill="#111827">−</text>
<circle cx="375" cy="83" r="8.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="375" y="87" font-size="11" text-anchor="middle" fill="#111827">+</text>
<circle cx="405" cy="83" r="13" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<text x="405" y="87.5" font-size="13" text-anchor="middle" fill="#111827">−</text>
<circle cx="435" cy="83" r="8.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="435" y="87" font-size="11" text-anchor="middle" fill="#111827">+</text>
<circle cx="465" cy="83" r="13" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<text x="465" y="87.5" font-size="13" text-anchor="middle" fill="#111827">−</text>
<circle cx="315" cy="113" r="13" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<text x="315" y="117.5" font-size="13" text-anchor="middle" fill="#111827">−</text>
<circle cx="345" cy="113" r="8.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="345" y="117" font-size="11" text-anchor="middle" fill="#111827">+</text>
<circle cx="375" cy="113" r="13" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<text x="375" y="117.5" font-size="13" text-anchor="middle" fill="#111827">−</text>
<circle cx="405" cy="113" r="8.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="405" y="117" font-size="11" text-anchor="middle" fill="#111827">+</text>
<circle cx="435" cy="113" r="13" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<text x="435" y="117.5" font-size="13" text-anchor="middle" fill="#111827">−</text>
<circle cx="465" cy="113" r="8.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="465" y="117" font-size="11" text-anchor="middle" fill="#111827">+</text>
<circle cx="315" cy="143" r="8.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="315" y="147" font-size="11" text-anchor="middle" fill="#111827">+</text>
<circle cx="345" cy="143" r="13" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<text x="345" y="147.5" font-size="13" text-anchor="middle" fill="#111827">−</text>
<circle cx="375" cy="143" r="8.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="375" y="147" font-size="11" text-anchor="middle" fill="#111827">+</text>
<circle cx="405" cy="143" r="13" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<text x="405" y="147.5" font-size="13" text-anchor="middle" fill="#111827">−</text>
<circle cx="435" cy="143" r="8.5" fill="#9ca3af" stroke="#374151" stroke-width="1.5"/>
<text x="435" y="147" font-size="11" text-anchor="middle" fill="#111827">+</text>
<circle cx="465" cy="143" r="13" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<text x="465" y="147.5" font-size="13" text-anchor="middle" fill="#111827">−</text>
<circle cx="39.7" cy="226.1" r="6.5" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="60.3" cy="226.1" r="6.5" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="50" cy="234" r="10" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="131.7" cy="217.1" r="6.5" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="142" cy="235" r="6.5" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="130" cy="230" r="10" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="192" cy="242.6" r="6.5" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="207.8" cy="229.3" r="6.5" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="205" cy="242" r="10" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="74.9" cy="301.7" r="6.5" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="57" cy="312" r="6.5" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="62" cy="300" r="10" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="151.6" cy="285.2" r="6.5" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="148" cy="305.5" r="6.5" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="142" cy="294" r="10" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="219" cy="321" r="6.5" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="199.6" cy="313.9" r="6.5" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="212" cy="310" r="10" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="298.5" cy="228.2" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="311.5" cy="235.8" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="420.2" cy="310.7" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="429.8" cy="299.3" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="477.3" cy="230.5" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="478.7" cy="245.5" r="9" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="375" cy="234" r="6.5" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="394.4" cy="241.1" r="6.5" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="382" cy="245" r="10" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="331" cy="304.4" r="6.5" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="315.2" cy="317.7" r="6.5" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="318" cy="305" r="10" fill="#374151" stroke="#111827" stroke-width="1.5"/>
<circle cx="479.1" cy="320.4" r="6.5" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="472" cy="301" r="6.5" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
<circle cx="483" cy="308" r="10" fill="#374151" stroke="#111827" stroke-width="1.5"/>
</svg>
<figcaption>Figure: Particle diagrams I–IV</figcaption>
</figure>""",
        "question": r"In the particle diagrams above, each circle represents an atom or a monatomic ion. Circles of different sizes or shades represent different elements, and the symbols $+$ and $-$ indicate the charges of ions. Which of the diagrams represent pure substances?",
        "options": [
            r"I only",
            r"I and III only",
            r"I, III, and IV",
            r"I, II, and III",
        ],
        "correct_index": 3,
        "explanation": r"A pure substance contains particles of only one type (one kind of atom, molecule, or formula unit), whereas a mixture contains two or more types of particles whose relative proportions can vary. Diagram I contains only identical diatomic molecules of one element, and Diagram III contains only identical molecules of one compound, so both are pure substances. Diagram II contains two kinds of ions, but they occur in a fixed $1:1$ ratio in a repeating array: the sample is a single ionic compound whose formula describes a formula unit rather than a discrete molecule, so it is also a pure substance. Diagram IV contains two different kinds of molecules (those of Diagrams I and III), so it is a mixture. Choosing only Diagram I treats every compound as a mixture of elements; choosing only Diagrams I and III treats the ionic solid as a mixture of two kinds of ions; and including Diagram IV treats any collection of molecules as pure.",
    },
    {
        "unit_q_num": 55,
        "topic_code": "1.4",
        "topic_title": "Composition of Mixtures",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A student is given a white crystalline solid labeled sodium chloride, $\text{NaCl}$, and suspects that it is contaminated with potassium chloride, $\text{KCl}$. Which of the following procedures would provide the best evidence of whether the solid is pure $\text{NaCl}$?",
        "options": [
            r"Precipitate all of the chloride ions in a weighed sample as $\text{AgCl}(s)$, dry and weigh the precipitate, and compare the mass percent of chlorine in the sample with that of pure $\text{NaCl}$.",
            r"Dissolve a weighed sample in distilled water, and conclude that the solid is pure $\text{NaCl}$ if the entire sample dissolves.",
            r"Add excess $\text{AgNO}_3(aq)$ to a dissolved sample, and conclude that the solid is pure $\text{NaCl}$ if a white precipitate forms.",
            r"Measure the pH of a solution of the sample in distilled water, and conclude that the solid is pure $\text{NaCl}$ if the pH is $7$.",
        ],
        "correct_index": 0,
        "explanation": r"Elemental analysis can be used to determine the purity of a substance. Pure $\text{NaCl}$ is $\frac{35.45}{58.44} \times 100\% = 60.7\%$ chlorine by mass, whereas $\text{KCl}$ is only $\frac{35.45}{74.55} \times 100\% = 47.6\%$ chlorine. Any $\text{KCl}$ contamination therefore lowers the mass percent of chlorine below $60.7\%$, which a quantitative (gravimetric) analysis of the $\text{AgCl}(s)$ precipitate can detect. The other procedures cannot distinguish the two salts: both are very soluble in water, both form a white $\text{AgCl}$ precipitate with $\text{AgNO}_3(aq)$, and both produce neutral solutions.",
    },
    {
        "unit_q_num": 56,
        "topic_code": "1.5",
        "topic_title": "Atomic Structure and Electron Configuration",
        "difficulty": "AP Exam Level",
        "stimulus": "",
        "question": r"A hydrogen atom, $\text{H}$, and a helium ion, $\text{He}^+$, each contain a single electron. The average distance between the electron and the nucleus in $\text{He}^+$ is half the average distance in $\text{H}$. Treating each electron as if it were located at its average distance from the nucleus, the Coulombic force of attraction between the nucleus and the electron in $\text{He}^+$ is how many times as large as that in $\text{H}$?",
        "options": [
            r"$2$",
            r"$4$",
            r"$8$",
            r"$16$",
        ],
        "correct_index": 2,
        "explanation": r"Coulomb's law states that $F \propto \frac{q_1 q_2}{r^2}$. The charge of the electron is the same in both species, but the nuclear charge of $\text{He}^+$ ($+2$) is twice that of $\text{H}$ ($+1$), which doubles the force. Because the force depends on $\frac{1}{r^2}$, halving the distance multiplies the force by $\frac{1}{(1/2)^2} = 4$. Overall, $\frac{F_{\text{He}^+}}{F_{\text{H}}} = \frac{(2)(1)/(\frac{1}{2}r)^2}{(1)(1)/r^2} = 2 \times 4 = 8$. A factor of $2$ accounts only for the nuclear charge; a factor of $4$ accounts only for the distance (or treats the force as proportional to $\frac{1}{r}$); and a factor of $16$ incorrectly squares the nuclear charge as well as the distance.",
    },
    {
        "unit_q_num": 57,
        "topic_code": "1.6",
        "topic_title": "Photoelectron Spectroscopy (PES)",
        "difficulty": "AP Exam Level",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 300" role="img" font-family="sans-serif" aria-label="Photoelectron spectrum. The horizontal axis is binding energy in MJ/mol on a logarithmic scale that increases to the left, with labels 1000, 100, 10, 1, and 0.1. The vertical axis is relative number of electrons from 0 to 6. There are four peaks: at 104 MJ/mol with height 2, at 6.84 MJ/mol with height 2, at 3.67 MJ/mol with height 6, and at 0.50 MJ/mol with height 1.">
<line x1="60" y1="222" x2="480" y2="222" stroke="#e5e7eb" stroke-width="1"/>
<line x1="60" y1="194" x2="480" y2="194" stroke="#e5e7eb" stroke-width="1"/>
<line x1="60" y1="166" x2="480" y2="166" stroke="#e5e7eb" stroke-width="1"/>
<line x1="60" y1="138" x2="480" y2="138" stroke="#e5e7eb" stroke-width="1"/>
<line x1="60" y1="110" x2="480" y2="110" stroke="#e5e7eb" stroke-width="1"/>
<line x1="60" y1="82" x2="480" y2="82" stroke="#e5e7eb" stroke-width="1"/>
<line x1="60" y1="250" x2="480" y2="250" stroke="#111827" stroke-width="2"/>
<line x1="60" y1="250" x2="60" y2="62" stroke="#111827" stroke-width="2"/>
<line x1="54" y1="250" x2="60" y2="250" stroke="#111827" stroke-width="1.5"/>
<text x="49" y="254" font-size="12" text-anchor="end" fill="#111827">0</text>
<line x1="54" y1="222" x2="60" y2="222" stroke="#111827" stroke-width="1.5"/>
<text x="49" y="226" font-size="12" text-anchor="end" fill="#111827">1</text>
<line x1="54" y1="194" x2="60" y2="194" stroke="#111827" stroke-width="1.5"/>
<text x="49" y="198" font-size="12" text-anchor="end" fill="#111827">2</text>
<line x1="54" y1="166" x2="60" y2="166" stroke="#111827" stroke-width="1.5"/>
<text x="49" y="170" font-size="12" text-anchor="end" fill="#111827">3</text>
<line x1="54" y1="138" x2="60" y2="138" stroke="#111827" stroke-width="1.5"/>
<text x="49" y="142" font-size="12" text-anchor="end" fill="#111827">4</text>
<line x1="54" y1="110" x2="60" y2="110" stroke="#111827" stroke-width="1.5"/>
<text x="49" y="114" font-size="12" text-anchor="end" fill="#111827">5</text>
<line x1="54" y1="82" x2="60" y2="82" stroke="#111827" stroke-width="1.5"/>
<text x="49" y="86" font-size="12" text-anchor="end" fill="#111827">6</text>
<line x1="70" y1="250" x2="70" y2="256" stroke="#111827" stroke-width="1.5"/>
<text x="70" y="271" font-size="12" text-anchor="middle" fill="#111827">1000</text>
<line x1="170" y1="250" x2="170" y2="256" stroke="#111827" stroke-width="1.5"/>
<text x="170" y="271" font-size="12" text-anchor="middle" fill="#111827">100</text>
<line x1="270" y1="250" x2="270" y2="256" stroke="#111827" stroke-width="1.5"/>
<text x="270" y="271" font-size="12" text-anchor="middle" fill="#111827">10</text>
<line x1="370" y1="250" x2="370" y2="256" stroke="#111827" stroke-width="1.5"/>
<text x="370" y="271" font-size="12" text-anchor="middle" fill="#111827">1</text>
<line x1="470" y1="250" x2="470" y2="256" stroke="#111827" stroke-width="1.5"/>
<text x="470" y="271" font-size="12" text-anchor="middle" fill="#111827">0.1</text>
<path d="M 156.3,250.0 L 157.3,249.9 158.3,249.8 159.3,249.4 160.3,248.4 161.3,246.3 162.3,242.4 163.3,236.0 164.3,227.0 165.3,216.0 166.3,205.2 167.3,197.0 168.3,194.0 169.3,197.0 170.3,205.2 171.3,216.0 172.3,227.0 173.3,236.0 174.3,242.4 175.3,246.3 176.3,248.4 177.3,249.4 178.3,249.8 179.3,249.9 180.3,250.0 Z" fill="#9ca3af" stroke="#111827" stroke-width="1.5" stroke-linejoin="round"/>
<text x="168.3" y="187" font-size="11" text-anchor="middle" fill="#111827">104</text>
<path d="M 274.5,250.0 L 275.5,249.9 276.5,249.8 277.5,249.4 278.5,248.4 279.5,246.3 280.5,242.4 281.5,236.0 282.5,227.0 283.5,216.0 284.5,205.2 285.5,197.0 286.5,194.0 287.5,197.0 288.5,205.2 289.5,216.0 290.5,227.0 291.5,236.0 292.5,242.4 293.5,246.3 294.5,248.4 295.5,249.4 296.5,249.8 297.5,249.9 298.5,250.0 Z" fill="#9ca3af" stroke="#111827" stroke-width="1.5" stroke-linejoin="round"/>
<text x="286.5" y="187" font-size="11" text-anchor="middle" fill="#111827">6.84</text>
<path d="M 301.5,249.9 L 302.5,249.8 303.5,249.4 304.5,248.1 305.5,245.2 306.5,239.0 307.5,227.3 308.5,208.1 309.5,180.9 310.5,148.1 311.5,115.5 312.5,91.1 313.5,82.0 314.5,91.1 315.5,115.5 316.5,148.1 317.5,180.9 318.5,208.1 319.5,227.3 320.5,239.0 321.5,245.2 322.5,248.1 323.5,249.4 324.5,249.8 325.5,249.9 Z" fill="#9ca3af" stroke="#111827" stroke-width="1.5" stroke-linejoin="round"/>
<text x="313.5" y="75" font-size="11" text-anchor="middle" fill="#111827">3.67</text>
<path d="M 388.1,250.0 L 389.1,250.0 390.1,249.9 391.1,249.7 392.1,249.2 393.1,248.2 394.1,246.2 395.1,243.0 396.1,238.5 397.1,233.0 398.1,227.6 399.1,223.5 400.1,222.0 401.1,223.5 402.1,227.6 403.1,233.0 404.1,238.5 405.1,243.0 406.1,246.2 407.1,248.2 408.1,249.2 409.1,249.7 410.1,249.9 411.1,250.0 412.1,250.0 Z" fill="#9ca3af" stroke="#111827" stroke-width="1.5" stroke-linejoin="round"/>
<text x="400.1" y="215" font-size="11" text-anchor="middle" fill="#111827">0.50</text>
<text x="270" y="292" font-size="13" text-anchor="middle" fill="#111827">Binding Energy (MJ/mol)</text>
<text x="18" y="156" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 18 156)">Relative Number of Electrons</text>
</svg>
<figcaption>Figure: Complete photoelectron spectrum of an unknown element (peak positions labeled in MJ/mol)</figcaption>
</figure>""",
        "question": r"The complete photoelectron spectrum of an element is shown above. Which of the following best describes the photoelectron spectrum of the element that has one more proton in its nucleus?",
        "options": [
            r"It has five peaks; the additional peak, with a relative height of $1$, appears at a lower binding energy than any of the peaks shown.",
            r"It has four peaks; every peak is shifted to a lower binding energy, and the peak with the lowest binding energy is twice as tall.",
            r"It has four peaks at the same binding energies as those shown, but the peak with the lowest binding energy is twice as tall.",
            r"It has four peaks; every peak is shifted to a higher binding energy, and the peak with the lowest binding energy is twice as tall.",
        ],
        "correct_index": 3,
        "explanation": r"The relative peak heights ($2, 2, 6, 1$, from highest to lowest binding energy) correspond to $1s^2 2s^2 2p^6 3s^1$, so the element is sodium. The element with one more proton is magnesium, $1s^2 2s^2 2p^6 3s^2$: the additional electron enters the same $3s$ subshell, so there are still four peaks, and the $3s$ peak (lowest binding energy) becomes twice as tall. Because the magnesium nucleus has one more proton, every electron experiences a greater Coulombic attraction, so every peak shifts to a higher binding energy, that is, to the left (for example, the $3s$ peak moves from $0.50$ to $0.74\text{ MJ/mol}$). A fifth peak would require electrons in a new subshell, and keeping the same or lower binding energies ignores the increase in nuclear charge.",
    },
    {
        "unit_q_num": 58,
        "topic_code": "1.7",
        "topic_title": "Periodic Trends",
        "difficulty": "Challenging",
        "stimulus": r"""<figure class="quiz-figure-wrap">
<svg class="quiz-figure" viewBox="0 0 520 310" role="img" font-family="sans-serif" aria-label="Line graph of first ionization energy in kJ/mol (0 to 2500) versus atomic number from 1 to 20. Values: 1312, 2372, 520, 900, 801, 1086, 1402, 1314, 1681, 2081, 496, 738, 578, 787, 1012, 1000, 1251, 1521, 419, 590. Maxima occur at the noble gases helium, neon, and argon, followed by sharp drops to lithium, sodium, and potassium.">
<line x1="64" y1="216" x2="500" y2="216" stroke="#e5e7eb" stroke-width="1"/>
<line x1="64" y1="172" x2="500" y2="172" stroke="#e5e7eb" stroke-width="1"/>
<line x1="64" y1="128" x2="500" y2="128" stroke="#e5e7eb" stroke-width="1"/>
<line x1="64" y1="84" x2="500" y2="84" stroke="#e5e7eb" stroke-width="1"/>
<line x1="64" y1="40" x2="500" y2="40" stroke="#e5e7eb" stroke-width="1"/>
<line x1="64" y1="260" x2="500" y2="260" stroke="#111827" stroke-width="2"/>
<line x1="64" y1="260" x2="64" y2="34" stroke="#111827" stroke-width="2"/>
<line x1="58" y1="260" x2="64" y2="260" stroke="#111827" stroke-width="1.5"/>
<text x="53" y="264" font-size="12" text-anchor="end" fill="#111827">0</text>
<line x1="58" y1="216" x2="64" y2="216" stroke="#111827" stroke-width="1.5"/>
<text x="53" y="220" font-size="12" text-anchor="end" fill="#111827">500</text>
<line x1="58" y1="172" x2="64" y2="172" stroke="#111827" stroke-width="1.5"/>
<text x="53" y="176" font-size="12" text-anchor="end" fill="#111827">1000</text>
<line x1="58" y1="128" x2="64" y2="128" stroke="#111827" stroke-width="1.5"/>
<text x="53" y="132" font-size="12" text-anchor="end" fill="#111827">1500</text>
<line x1="58" y1="84" x2="64" y2="84" stroke="#111827" stroke-width="1.5"/>
<text x="53" y="88" font-size="12" text-anchor="end" fill="#111827">2000</text>
<line x1="58" y1="40" x2="64" y2="40" stroke="#111827" stroke-width="1.5"/>
<text x="53" y="44" font-size="12" text-anchor="end" fill="#111827">2500</text>
<line x1="78" y1="260" x2="78" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="78" y="279" font-size="11" text-anchor="middle" fill="#111827">1</text>
<line x1="99.5" y1="260" x2="99.5" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="99.5" y="279" font-size="11" text-anchor="middle" fill="#111827">2</text>
<line x1="121" y1="260" x2="121" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="121" y="279" font-size="11" text-anchor="middle" fill="#111827">3</text>
<line x1="142.5" y1="260" x2="142.5" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="142.5" y="279" font-size="11" text-anchor="middle" fill="#111827">4</text>
<line x1="164" y1="260" x2="164" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="164" y="279" font-size="11" text-anchor="middle" fill="#111827">5</text>
<line x1="185.5" y1="260" x2="185.5" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="185.5" y="279" font-size="11" text-anchor="middle" fill="#111827">6</text>
<line x1="207" y1="260" x2="207" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="207" y="279" font-size="11" text-anchor="middle" fill="#111827">7</text>
<line x1="228.5" y1="260" x2="228.5" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="228.5" y="279" font-size="11" text-anchor="middle" fill="#111827">8</text>
<line x1="250" y1="260" x2="250" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="250" y="279" font-size="11" text-anchor="middle" fill="#111827">9</text>
<line x1="271.5" y1="260" x2="271.5" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="271.5" y="279" font-size="11" text-anchor="middle" fill="#111827">10</text>
<line x1="293" y1="260" x2="293" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="293" y="279" font-size="11" text-anchor="middle" fill="#111827">11</text>
<line x1="314.5" y1="260" x2="314.5" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="314.5" y="279" font-size="11" text-anchor="middle" fill="#111827">12</text>
<line x1="336" y1="260" x2="336" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="336" y="279" font-size="11" text-anchor="middle" fill="#111827">13</text>
<line x1="357.5" y1="260" x2="357.5" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="357.5" y="279" font-size="11" text-anchor="middle" fill="#111827">14</text>
<line x1="379" y1="260" x2="379" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="379" y="279" font-size="11" text-anchor="middle" fill="#111827">15</text>
<line x1="400.5" y1="260" x2="400.5" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="400.5" y="279" font-size="11" text-anchor="middle" fill="#111827">16</text>
<line x1="422" y1="260" x2="422" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="422" y="279" font-size="11" text-anchor="middle" fill="#111827">17</text>
<line x1="443.5" y1="260" x2="443.5" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="443.5" y="279" font-size="11" text-anchor="middle" fill="#111827">18</text>
<line x1="465" y1="260" x2="465" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="465" y="279" font-size="11" text-anchor="middle" fill="#111827">19</text>
<line x1="486.5" y1="260" x2="486.5" y2="265" stroke="#111827" stroke-width="1.5"/>
<text x="486.5" y="279" font-size="11" text-anchor="middle" fill="#111827">20</text>
<polyline points="78.0,144.5 99.5,51.3 121.0,214.2 142.5,180.8 164.0,189.5 185.5,164.4 207.0,136.6 228.5,144.4 250.0,112.1 271.5,76.9 293.0,216.4 314.5,195.1 336.0,209.1 357.5,190.7 379.0,170.9 400.5,172.0 422.0,149.9 443.5,126.2 465.0,223.1 486.5,208.1" fill="none" stroke="#374151" stroke-width="2" stroke-linejoin="round"/>
<circle cx="78.0" cy="144.5" r="3.2" fill="#111827"/>
<circle cx="99.5" cy="51.3" r="3.2" fill="#111827"/>
<circle cx="121.0" cy="214.2" r="3.2" fill="#111827"/>
<circle cx="142.5" cy="180.8" r="3.2" fill="#111827"/>
<circle cx="164.0" cy="189.5" r="3.2" fill="#111827"/>
<circle cx="185.5" cy="164.4" r="3.2" fill="#111827"/>
<circle cx="207.0" cy="136.6" r="3.2" fill="#111827"/>
<circle cx="228.5" cy="144.4" r="3.2" fill="#111827"/>
<circle cx="250.0" cy="112.1" r="3.2" fill="#111827"/>
<circle cx="271.5" cy="76.9" r="3.2" fill="#111827"/>
<circle cx="293.0" cy="216.4" r="3.2" fill="#111827"/>
<circle cx="314.5" cy="195.1" r="3.2" fill="#111827"/>
<circle cx="336.0" cy="209.1" r="3.2" fill="#111827"/>
<circle cx="357.5" cy="190.7" r="3.2" fill="#111827"/>
<circle cx="379.0" cy="170.9" r="3.2" fill="#111827"/>
<circle cx="400.5" cy="172.0" r="3.2" fill="#111827"/>
<circle cx="422.0" cy="149.9" r="3.2" fill="#111827"/>
<circle cx="443.5" cy="126.2" r="3.2" fill="#111827"/>
<circle cx="465.0" cy="223.1" r="3.2" fill="#111827"/>
<circle cx="486.5" cy="208.1" r="3.2" fill="#111827"/>
<text x="99.5" y="42.3" font-size="12" text-anchor="middle" fill="#111827">He</text>
<text x="271.5" y="67.9" font-size="12" text-anchor="middle" fill="#111827">Ne</text>
<text x="443.5" y="117.2" font-size="12" text-anchor="middle" fill="#111827">Ar</text>
<text x="112.0" y="229.2" font-size="12" text-anchor="middle" fill="#111827">Li</text>
<text x="284.0" y="231.4" font-size="12" text-anchor="middle" fill="#111827">Na</text>
<text x="456.0" y="238.1" font-size="12" text-anchor="middle" fill="#111827">K</text>
<text x="282" y="302" font-size="13" text-anchor="middle" fill="#111827">Atomic Number (Z)</text>
<text x="15" y="147" font-size="13" text-anchor="middle" fill="#111827" transform="rotate(-90 15 147)">First Ionization Energy (kJ/mol)</text>
</svg>
<figcaption>Figure: First ionization energy versus atomic number for elements 1–20</figcaption>
</figure>""",
        "question": r"The graph above shows the first ionization energies of the elements with atomic numbers $1$ through $20$. Which feature of the graph provides the strongest evidence that the electrons in atoms occupy shells and that a new shell begins to fill at $Z = 3$, $11$, and $19$?",
        "options": [
            r"The general increase in first ionization energy from left to right across each period",
            r"The sharp decrease in first ionization energy from each noble gas ($Z = 2$, $10$, and $18$) to the element that follows it",
            r"The small decrease in first ionization energy from $Z = 4$ to $Z = 5$ and from $Z = 12$ to $Z = 13$",
            r"The small decrease in first ionization energy from $Z = 7$ to $Z = 8$ and from $Z = 15$ to $Z = 16$",
        ],
        "correct_index": 1,
        "explanation": r"When a new shell begins to fill, the outermost electron occupies a higher principal energy level: it is, on average, much farther from the nucleus and is shielded by a completely filled inner shell, so its Coulombic attraction to the nucleus drops sharply. This produces the large decreases in ionization energy from $\text{He}$ to $\text{Li}$, from $\text{Ne}$ to $\text{Na}$, and from $\text{Ar}$ to $\text{K}$, and the recurrence of this pattern reflects the periodic filling of shells. The general increase across a period reflects increasing nuclear charge as electrons are added to the same shell. The small drops from $Z = 4$ to $5$ and from $Z = 12$ to $13$ are evidence for subshells ($s$ versus $p$), and the small drops from $Z = 7$ to $8$ and from $Z = 15$ to $16$ arise from repulsion between paired electrons in a $p$ orbital; neither marks the start of a new shell.",
    },
    {
        "unit_q_num": 59,
        "topic_code": "1.7",
        "topic_title": "Periodic Trends",
        "difficulty": "Challenging",
        "stimulus": r"""<table class="quiz-data-table">
<thead>
<tr><th></th><th>Group 15</th><th>Group 16</th><th>Group 17</th></tr>
</thead>
<tbody>
<tr><td>Period 3</td><td></td><td>$\text{S}$: $2.58$</td><td></td></tr>
<tr><td>Period 4</td><td>$\text{As}$: $2.18$</td><td>$\text{Se}$: ?</td><td>$\text{Br}$: $2.96$</td></tr>
<tr><td>Period 5</td><td></td><td>$\text{Te}$: $2.10$</td><td></td></tr>
</tbody>
</table>""",
        "question": r"The table above gives the electronegativity values of the four elements that surround selenium, $\text{Se}$, in the periodic table. Based on periodic trends, which of the following is the most reasonable estimate of the electronegativity of $\text{Se}$?",
        "options": [
            r"$1.9$",
            r"$2.4$",
            r"$2.8$",
            r"$3.2$",
        ],
        "correct_index": 1,
        "explanation": r"Electronegativity increases from left to right across a period (greater effective nuclear charge acting on valence electrons in the same shell) and decreases down a group (valence electrons in a higher shell are farther from the nucleus and more shielded). Therefore the value for $\text{Se}$ must be greater than those of $\text{As}$ ($2.18$, to its left) and $\text{Te}$ ($2.10$, below it) but less than those of $\text{Br}$ ($2.96$, to its right) and $\text{S}$ ($2.58$, above it). Only $2.4$ lies between $2.18$ and $2.58$ (the measured value is $2.55$). The value $2.8$ lies between the values of $\text{As}$ and $\text{Br}$ but exceeds the value of $\text{S}$ directly above $\text{Se}$, $1.9$ is lower than the values of both $\text{As}$ and $\text{Te}$, and $3.2$ is higher than the value of every neighbor.",
    },
    {
        "unit_q_num": 60,
        "topic_code": "1.8",
        "topic_title": "Valence Electrons and Ionic Compounds",
        "difficulty": "Challenging",
        "stimulus": "",
        "question": r"The reactivity of the Group 1 metals increases down the group ($\text{Li} < \text{Na} < \text{K}$ in their reactions with water), whereas the reactivity of the Group 17 elements decreases down the group ($\text{F}_2 > \text{Cl}_2 > \text{Br}_2 > \text{I}_2$ in their reactions with hydrogen). Which of the following best explains both trends?",
        "options": [
            r"The nuclear charge increases down both groups, so the attraction between the nucleus and the valence electrons becomes stronger down both groups.",
            r"Atomic mass increases down both groups, so heavier atoms collide with the other reactant more forcefully.",
            r"Down Group 1 the valence electron becomes closer to the nucleus, whereas down Group 17 the valence electrons become farther from the nucleus.",
            r"Down both groups the valence electrons occupy a higher shell that is farther from the nucleus and more shielded, so alkali metal atoms lose their valence electron more easily, while halogen atoms attract electrons from other atoms less strongly.",
        ],
        "correct_index": 3,
        "explanation": r"The likelihood that an element forms a bond depends on the interactions between its valence electrons and its nucleus. Moving down any group, the valence electrons are in a higher principal energy level, farther from the nucleus and shielded by more core electrons, so by Coulomb's law the attraction between the nucleus and valence-shell electrons weakens. The Group 1 metals react by losing their single valence electron, so a weaker attraction (lower ionization energy) makes them more reactive down the group. The Group 17 elements react by gaining or sharing electrons, so a weaker attraction for electrons from other atoms (lower electronegativity) makes them less reactive down the group. The increase in nuclear charge is offset by added shielding (and, if it dominated, would predict the opposite of both observed trends), atomic mass does not govern reactivity, and the valence electrons move farther from the nucleus down both groups.",
    },
]
