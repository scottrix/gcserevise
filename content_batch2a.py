#!/usr/bin/env python3
"""Batch 2a: A4, G18, A1, N15 (full), G14, N2, N13, A14, N14, A8, R9."""
from content_waves import W_SEC, EX, SOL_HEAD, KF, CTX, W2, run

B = {}

B["A4-simplifying-expressions.html"] = dict(
    marker="Q7: Expand and simplify: 3(2x − 1) − 2(x + 4)",
    worked=W_SEC("Simplifying expressions is the grammar of algebra — every later topic assumes it. Two skills: collecting like terms (only identical letter parts combine) and expanding brackets (everything inside is multiplied).",
        EX("Expand and simplify: 3(2x + 5) − 2(x − 4)",
            '<p>Expand each bracket: 6x + 15 − 2x + 8</p>'
            '<p>Careful with the second: −2 × (−4) = +8</p>'
            '<p>Collect: (6x − 2x) + (15 + 8) = <strong>4x + 23</strong></p>',
            "M1 for both expansions, A1 for 4x + 23. The minus-before-bracket case is the single most examined slip.") +
        EX("Factorise fully: 6x² + 9x",
            '<p>Highest common factor of 6x² and 9x is 3x.</p>'
            '<p>6x² ÷ 3x = 2x &nbsp;and&nbsp; 9x ÷ 3x = 3</p>'
            '<p><strong>Answer: 3x(2x + 3)</strong></p>',
            "M1 for 3x, A1 for 3x(2x + 3). 'Fully' means take out ALL common factors — 3(2x² + 3x) loses the mark."))
    + '<p><strong>Exam wording to expect:</strong> "Simplify", "Expand and simplify", "Factorise fully".</p>',
    questions=["Q7: Expand and simplify: 3(2x − 1) − 2(x + 4)", "Q8: Factorise fully: 10x² − 5x"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> All three terms are a-terms: 5 + 3 − 2 = 6 → <strong>6a</strong></p>'
        '<p><strong>Q2.</strong> x-terms: 4 − 2 = 2x; y-terms: 3 + 5 = 8y → <strong>2x + 8y</strong>. '
        'Unlike terms never combine — 2x + 8y is finished.</p>'
        '<p><strong>Q3.</strong> 4 × x and 4 × (−3): <strong>4x − 12</strong></p>'
        '<p><strong>Q4.</strong> FOIL: x² + 5x + 2x + 10 = <strong>x² + 7x + 10</strong></p>'
        '<p><strong>Q5.</strong> HCF of 8 and 12 is 4 → <strong>4(2x + 3)</strong></p>'
        '<p><strong>Q6.</strong> HCF is 5x: 5x² ÷ 5x = x, 15x ÷ 5x = 3 → <strong>5x(x − 3)</strong></p>'
        '<p><strong>Q7.</strong> 6x − 3 − 2x − 8 = <strong>4x − 11</strong> (the −2 multiplies BOTH terms: −2 × +4 = −8)</p>'
        '<p><strong>Q8.</strong> HCF 5x → <strong>5x(2x − 1)</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Like terms: same letter AND same power — 3a² and 3a are NOT like terms</li>'
        '<li>Expand: every term inside the bracket is multiplied: a(b + c) = ab + ac</li>'
        '<li>Minus before a bracket flips EVERY sign inside: −(x − 5) = −x + 5</li>'
        '<li>Factorise = expand in reverse: take out the HCF of coefficients and letters</li>'
        '<li>Double brackets: (x + a)(x + b) = x² + (a + b)x + ab</li>'
        '</ul>'),
    context=CTX('<p>Simplifying sits inside almost every algebra question as a first step: solving '
        'equations, expanding for quadratics, substitution. Standalone questions are 1–3 marks '
        'on Paper 1 (non-calculator).</p>'
        '<p>Links to: solving equations (A17), quadratic graphs (A11), factorising quadratics (A18).</p>'),
    worked2=W2("Expand and simplify: (2x + 3)(x − 4)",
        '<p>Multiply every term in the first bracket by every term in the second:</p>'
        '<p>2x × x = 2x² &nbsp;·&nbsp; 2x × (−4) = −8x &nbsp;·&nbsp; 3 × x = 3x &nbsp;·&nbsp; 3 × (−4) = −12</p>'
        '<p>Combine: 2x² − 8x + 3x − 12 = <strong>2x² − 5x − 12</strong></p>',
        "M1 for three correct products, A1 for 2x² − 5x − 12. "
        "Check with x = 1: LHS (5)(−3) = −15; RHS 2 − 5 − 12 = −15 ✓"))

B["G18-arcs-sectors.html"] = dict(
    marker="Q6: Find the perimeter of a semicircle with diameter 14 cm",
    worked=W_SEC("Arcs and sectors are fractions of a circle. Every question reduces to one idea: the fraction is angle ÷ 360.",
        EX("Find the area of a sector with radius 10 cm and angle 72°.",
            '<p>Fraction of circle: 72 ÷ 360 = 1/5</p>'
            '<p>Full circle area: π × 10² = 100π</p>'
            '<p>Sector: 1/5 × 100π = <strong>20π cm²</strong> (≈ 62.8 cm²)</p>',
            "M1 for 72/360, M1 for π × 10², A1 for 20π. Leaving π in the answer is usually required unless the question says otherwise.") +
        EX("An arc has length 5π cm in a circle of radius 6 cm. Find the sector angle.",
            '<p>Arc = (θ/360) × 2πr → 5π = (θ/360) × 12π</p>'
            '<p>Divide both sides by π: 5 = 12θ/360 → θ = 5 × 30 = <strong>150°</strong></p>',
            "M1 for setting up the arc formula, A1 for 150°. Reverse questions are just solving the same formula."))
    + '<p><strong>Exam wording to expect:</strong> "Give your answer in terms of π" or "to 1 decimal place" — read which one is asked.</p>',
    questions=["Q6: Find the perimeter of a semicircle with diameter 14 cm", "Q7: A sector of angle 40° has area 8π cm². Find its radius."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> Fraction 135/360 = 3/8. Arc = 3/8 × 2π × 8 = 3/8 × 16π = <strong>6π cm</strong></p>'
        '<p><strong>Q2.</strong> Fraction 45/360 = 1/8. Area = 1/8 × π × 14² = 196π/8 = <strong>24.5π cm²</strong></p>'
        '<p><strong>Q3.</strong> 4π = (θ/360) × 12π → 4 = 12θ/360 → θ = 4 × 30 = <strong>120°</strong></p>'
        '<p><strong>Q4.</strong> 15π = (60/360) × πr² = πr²/6 → r² = 90 → r = √90 = <strong>3√10 cm</strong> (≈ 9.49 cm)</p>'
        '<p><strong>Q5.</strong> Arc = (120/360) × 2π × 5 = 10π/3. Perimeter = arc + 2 radii = '
        '<strong>10π/3 + 10 cm</strong>. The two straight radii are the part students forget.</p>'
        '<p><strong>Q6.</strong> Semicircle perimeter = arc + diameter = (π × 14 ÷ 2) + 14 = '
        '<strong>7π + 14 cm</strong> (≈ 36.0 cm)</p>'
        '<p><strong>Q7.</strong> 8π = (40/360) × πr² = πr²/9 → r² = 72 → r = <strong>6√2 cm</strong> (≈ 8.49 cm)</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Arc length = (θ/360) × 2πr &nbsp;·&nbsp; Sector area = (θ/360) × πr²</li>'
        '<li>Both are "fraction × whole circle" — find the fraction first</li>'
        '<li>Sector perimeter = arc + 2 radii</li>'
        '<li>Semicircle perimeter = πr + 2r (arc plus diameter)</li>'
        '<li>π ≈ 3.14159; calculator papers expect the π button, not 3.14</li>'
        '</ul>'),
    context=CTX('<p>Arcs and sectors: 3–4 marks on Papers 2/3 (calculator). "Reverse" questions '
        '(find the angle or radius) earn the extra method marks. Answers in terms of π are exact — '
        'a decimal where π was required scores 0 for accuracy.</p>'
        '<p>Links to: circles (G17), area and volume (G16), fractions of amounts (R3).</p>'),
    worked2=W2("A park is a sector of a circle, radius 50 m, angle 54°. Fencing costs £12 per metre and covers only the curved edge. Find the cost, to the nearest pound.",
        '<p>Arc = (54/360) × 2π × 50 = 0.15 × 100π = 15π m</p>'
        '<p>Length = 15π ≈ 47.12 m</p>'
        '<p>Cost = 47.12 × 12 = £565.49 → <strong>£565</strong></p>',
        "M1 for the arc calculation, M1 for the multiplication, A1 for £565. "
        "Applied sector questions always need the rounding stated in the question — 'nearest pound' here."))

B["A1-algebraic-notation.html"] = dict(
    marker="Q7: Write 'subtract x from 5' in symbols",
    worked=W_SEC("Algebraic notation questions are about translation: words ↔ symbols. The order of operations matters — '3 lots of (x + 2)' is 3(x + 2), not 3x + 2.",
        EX("Write 'add 3 to x, then multiply the result by 4' in symbols.",
            '<p>The brackets control the order: <strong>4(x + 3)</strong></p>'
            '<p>4x + 3 would mean &lsquo;multiply x by 4, THEN add 3&rsquo; — different instruction.</p>',
            "B1 for 4(x + 3). Word-order questions test whether you can see which operation happens first.") +
        EX("Mia is n years old. Write an expression for her age in 5 years, and for her brother's age, who is half Mia's age now.",
            '<p>In 5 years: <strong>n + 5</strong></p>'
            '<p>Brother now: <strong>n/2</strong> (or ½n)</p>',
            "B1 each. Context notation questions (ages, money, counters) are the standard Foundation format — define what YOUR letter means."))
    + '<p><strong>Exam wording to expect:</strong> "Write an expression for …", "in terms of n", or forming expressions from a context.</p>',
    questions=["Q7: Write 'subtract x from 5' in symbols", "Q8: Write an expression for the cost of 3 pens at £p each plus a £2 bag"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> x × x = x², so 3 × x² = <strong>3x²</strong></p>'
        '<p><strong>Q2.</strong> 4y means 4 × y = 4 × 7 = <strong>28</strong></p>'
        '<p><strong>Q3.</strong> a² = 5² = <strong>25</strong></p>'
        '<p><strong>Q4.</strong> 2(x + 3) = 2(4 + 3) = 2 × 7 = <strong>14</strong>. Brackets first.</p>'
        '<p><strong>Q5.</strong> <strong>2x + 1</strong> (multiply first, then add — the words give the order)</p>'
        '<p><strong>Q6.</strong> (x + y)/3 means the SUM is divided by 3: (8 + 4) ÷ 3 = <strong>4</strong>. '
        'The fraction line brackets the top.</p>'
        '<p><strong>Q7.</strong> <strong>5 − x</strong> — &lsquo;subtract x FROM 5&rsquo; means x is taken away from 5, so 5 comes first</p>'
        '<p><strong>Q8.</strong> <strong>3p + 2</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>4y means 4 × y; ab means a × b; 3(x + 2) means 3 × (x + 2)</li>'
        '<li>x² means x × x (not 2x)</li>'
        '<li>Writing rules: number before letter (5a), letters alphabetically (3ab), no × or ÷ signs</li>'
        '<li>"Subtract x from 5" = 5 − x; "subtract 5 from x" = x − 5 — order flips!</li>'
        '<li>A fraction bar brackets its whole numerator: (x + y)/3 = (x + y) ÷ 3</li>'
        '</ul>'),
    context=CTX('<p>Notation underpins all of algebra: 1–2 marks directly (translation questions), '
        'and indirectly everywhere else. Paper 1 favourite because it needs no calculator.</p>'
        '<p>Links to: substitution (A2), simplifying (A4), modelling with algebra (A21).</p>'),
    worked2=W2(" Pens cost p pence each. Rulers cost 10p more than pens. Write an expression for the total cost of 4 pens and 2 rulers, and simplify it.",
        '<p>4 pens: 4p. Ruler: p + 10, so 2 rulers: 2p + 20</p>'
        '<p>Total: 4p + 2p + 20 = <strong>6p + 20 pence</strong></p>',
        "M1 for 4p + 2(p + 10), A1 for 6p + 20. "
        "Forming expressions from a context is the opening step of most Foundation algebra word problems."))

B["N15-rounding-error-intervals.html"] = dict(
    marker="Q6: Write the error interval for 260 rounded to 2 significant figures",
    worked=W_SEC("Error intervals answer one question: 'what values would round to this number?' The rule: lower bound included (≤), upper bound NOT included (<).",
        EX("A length is measured as 8.4 cm to 1 decimal place. Write the error interval.",
            '<p>Half of the last placed unit: 0.05</p>'
            '<p>Lower: 8.4 − 0.05 = 8.35 (included — it rounds UP to 8.4)</p>'
            '<p>Upper: 8.4 + 0.05 = 8.45 (NOT included — it would round to 8.5)</p>'
            '<p><strong>8.35 ≤ L < 8.45</strong></p>',
            "M1 for 8.35 and 8.45, A1 for the interval with correct symbols. The < on the upper bound is the examined detail.") +
        EX("A number is truncated to 2.7. Write the error interval.",
            '<p>Truncation chops digits off — no rounding up.</p>'
            '<p><strong>2.7 ≤ T < 2.8</strong></p>',
            "M1 for 2.7 and 2.8, A1 for correct symbols. Truncated values can grow to the next digit but never shrink."))
    + '<p><strong>Exam wording to expect:</strong> "Write the error interval for …", "rounded to …", or "truncated to …".</p>',
    questions=["Q6: Write the error interval for 260 rounded to 2 significant figures", "Q7: A mass is 3.05 kg to 2 d.p. Write the error interval."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> Third decimal is 8 (≥5), round up: <strong>4.73</strong></p>'
        '<p><strong>Q2.</strong> First two significant figures are 8 and 4; next digit 7 rounds: <strong>0.085</strong></p>'
        '<p><strong>Q3.</strong> First two sig figs 4, 7; next digit 2 stays: <strong>4700</strong> — '
        'keep the zeros as placeholders</p>'
        '<p><strong>Q4.</strong> Nearest whole → ±0.5 → <strong>14.5 ≤ n < 15.5</strong></p>'
        '<p><strong>Q5.</strong> 2 d.p. → ±0.005 → <strong>0.715 ≤ x < 0.725</strong></p>'
        '<p><strong>Q6.</strong> 2 s.f. → nearest 10 → <strong>255 ≤ n < 265</strong></p>'
        '<p><strong>Q7.</strong> 2 d.p. → ±0.005 → <strong>3.045 ≤ m < 3.055</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Rounded to the nearest unit U → interval (U − ½unit) ≤ x < (U + ½unit)</li>'
        '<li>Rounded to n decimal places → add/subtract 5 in the (n+1)th place</li>'
        '<li>Lower bound INCLUDED (≤), upper bound EXCLUDED (<)</li>'
        '<li>Truncation: value can only be bigger — U ≤ x < U + 1 unit</li>'
        '<li>Rounding 5s: 4.725 → 4.73 (round half up); significant figures count from the first non-zero digit</li>'
        '</ul>'),
    context=CTX('<p>Rounding: 1 mark almost every Paper 1. Error intervals: 2 marks, increasingly common '
        'on Foundation Papers 2/3. The excluded upper bound is the discriminator between grades 4 and 5.</p>'
        '<p>Links to: estimation (N14), bounds in calculations (N16), units (N13).</p>'),
    worked2=W2("A number x satisfies 40 ≤ x < 50. State the value it could have been rounded to, and the rounding unit.",
        '<p>Any value in [40, 50) rounds to <strong>40 to 1 significant figure</strong> — the rounding '
        'unit is 10, giving 40 − 5 ≤ x < 40 + 5, i.e. 35 ≤ x < 45.</p>'
        '<p>Wait — check: 40 to 1 s.f. gives 35 ≤ x < 45, NOT [40, 50). So [40, 50) cannot come '
        'from 1 s.f. rounding; it could come from <strong>truncation to 1 s.f.</strong> (40 ≤ x < 50).</p>',
        "This distinction — rounding vs truncation — is a genuine AO2 discriminator. "
        "Rounding spreads ±½ unit around the value; truncation only reaches upward."))

B["G14-units-measure.html"] = dict(
    marker="Q6: Convert 4.5 hours to minutes",
    worked=W_SEC("Unit conversion errors cost marks across the whole paper. Two rules: know the factor, and square it for areas (×100), cube it for volumes (×1000… actually ×10⁶ for m²→cm²).",
        EX("Convert 2.5 m² to cm².",
            '<p>1 m = 100 cm, but area scales by the SQUARE: 1 m² = 100 × 100 = 10,000 cm²</p>'
            '<p>2.5 × 10,000 = <strong>25,000 cm²</strong></p>',
            "M1 for 10,000 (the squared factor), A1 for 25,000. Multiplying by 100 (the length factor) is the classic error.") +
        EX("Convert 90 minutes to hours, giving your answer as a decimal.",
            '<p>90 ÷ 60 = <strong>1.5 hours</strong></p>'
            '<p>Not 1.90 or 1.3 — minutes are sixtieths, not hundredths.</p>',
            "B1 for 1.5. Time-to-decimal conversions feed compound measures (speed questions)."))
    + '<p><strong>Exam wording to expect:</strong> "Convert …", "Give your answer in …" — check the target unit before calculating.</p>',
    questions=["Q6: Convert 4.5 hours to minutes", "Q7: Convert 0.05 kg to grams"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> ÷ 1000: 7500 ÷ 1000 = <strong>7.5 km</strong></p>'
        '<p><strong>Q2.</strong> Area factor 10,000: 0.8 × 10,000 = <strong>8000 cm²</strong></p>'
        '<p><strong>Q3.</strong> 1 litre = 1000 mL: <strong>3000 mL</strong></p>'
        '<p><strong>Q4.</strong> 1 kg = 1000 g: 2.4 × 1000 = <strong>2400 g</strong></p>'
        '<p><strong>Q5.</strong> 135 ÷ 60 = <strong>2.25 hours</strong> (= 2 h 15 min)</p>'
        '<p><strong>Q6.</strong> 4.5 × 60 = <strong>270 minutes</strong></p>'
        '<p><strong>Q7.</strong> 0.05 × 1000 = <strong>50 g</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Length: 1 km = 1000 m · 1 m = 100 cm · 1 cm = 10 mm</li>'
        '<li>Mass: 1 kg = 1000 g · 1 tonne = 1000 kg</li>'
        '<li>Volume: 1 litre = 1000 mL = 1000 cm³ · 1 m³ = 1,000,000 cm³</li>'
        '<li>Area: 1 m² = 10,000 cm² (square the length factor)</li>'
        '<li>Time: 1 h = 60 min · 1 min = 60 s · 1 h = 3600 s</li>'
        '<li>Imperial: 1 inch ≈ 2.5 cm · 1 kg ≈ 2.2 pounds · 1 mile ≈ 1.6 km</li>'
        '</ul>'),
    context=CTX('<p>Conversions appear inside other questions (speed, density, area) more often than '
        'standalone. 1 mark each; the squared/cubed factors are where marks are lost on Papers 2/3.</p>'
        '<p>Links to: compound measures (R1/R11), area and volume (G16), estimation (N14).</p>'),
    worked2=W2("A water tank holds 0.75 m³. How many litres is that?",
        '<p>1 m = 100 cm → 1 m³ = 100³ = 1,000,000 cm³</p>'
        '<p>0.75 m³ = 750,000 cm³</p>'
        '<p>1 litre = 1000 cm³ → 750,000 ÷ 1000 = <strong>750 litres</strong></p>',
        "M1 for the cubed factor, A1 for 750 litres. "
        "The m³-to-litres bridge (× 1000) appears in real-world capacity questions every year."))

B["N2-four-operations.html"] = dict(
    marker="Q6: Calculate: 2¾ + 1½",
    worked=W_SEC("Four operations with mixed number types — integers, decimals, fractions. Each has one hazard: subtracting negatives, decimal alignment, common denominators, flip-and-multiply.",
        EX("Calculate: −7 − (−12)",
            '<p>Subtracting a negative ADDS: −7 + 12 = <strong>5</strong></p>'
            '<p>Number line: start at −7, move 12 right.</p>',
            "B1 for 5. 'Two minuses make a plus' — but only for subtraction of a negative and multiplication of two negatives.") +
        EX("Calculate: 2/3 × 3/4",
            '<p>Multiply straight across: (2 × 3)/(3 × 4) = 6/12</p>'
            '<p>Simplify: ÷ 6 → <strong>1/2</strong></p>',
            "B1 for 1/2. Multiplication needs NO common denominator — that's only for + and −."))
    + '<p><strong>Exam wording to expect:</strong> "Work out …", "Give your answer as a fraction in its simplest form".</p>',
    questions=["Q6: Calculate: 2¾ + 1½", "Q7: Calculate: −3 × (−4) + 2 × (−5)"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> −8 + 15 − (−3) = −8 + 15 + 3 = <strong>10</strong></p>'
        '<p><strong>Q2.</strong> Line up decimal points: 4.56 + 2.80 = <strong>7.36</strong></p>'
        '<p><strong>Q3.</strong> 6 × 24 = 144, then place TWO decimal places: <strong>1.44</strong></p>'
        '<p><strong>Q4.</strong> Common denominator 24: 9/24 + 4/24 = <strong>13/24</strong> (already simplest)</p>'
        '<p><strong>Q5.</strong> Flip and multiply: 5/6 × 3/2 = 15/12 = <strong>5/4 = 1¼</strong></p>'
        '<p><strong>Q6.</strong> 2¾ + 1½ = 2¾ + 1¾ (½ = 2/4) = 3 + 5/4 = <strong>4¼</strong></p>'
        '<p><strong>Q7.</strong> (−3)(−4) = +12 and (2)(−5) = −10 → 12 − 10 = <strong>2</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Minus × minus = plus; minus ÷ minus = plus; subtracting a negative adds</li>'
        '<li>Decimal + / −: line up the points; ×: count total decimal places; ÷: make the divisor a whole number</li>'
        '<li>Fractions + / −: common denominator first; ×: straight across; ÷: flip the second, then ×</li>'
        '<li>Mixed numbers: convert to improper fractions before multiplying/dividing</li>'
        '<li>Financial terms: profit, loss, deposit, balance, discount</li>'
        '</ul>'),
    context=CTX('<p>Non-calculator arithmetic is the backbone of Paper 1: nearly every question starts '
        'here. Decimal × decimal and fraction ÷ fraction are the two discriminating skills.</p>'
        '<p>Links to: order of operations (N3), fractions of amounts (R3), money problems (N12).</p>'),
    worked2=W2("Work out 3½ × 2⅔, giving your answer as a mixed number.",
        '<p>Convert to improper fractions: 3½ = 7/2 and 2⅔ = 8/3</p>'
        '<p>Multiply: (7 × 8)/(2 × 3) = 56/6</p>'
        '<p>Simplify: ÷ 2 → 28/3 = <strong>9⅓</strong></p>',
        "M1 for converting both, M1 for 56/6, A1 for 9⅓. "
        "Mixed-number multiplication REQUIRES improper conversion — multiplying the whole parts separately is the error."))

B["N13-units-conversions.html"] = dict(
    marker="Q6: Convert 2.5 gallons to litres (1 gallon = 4.5 litres)",
    worked=W_SEC("Metric conversions are powers of ten. Imperial conversions (miles, pounds, gallons, stones) are GIVEN in the question — the skill is choosing multiply or divide.",
        EX("Convert 55 miles to km (1 mile = 1.6 km).",
            '<p>Km per mile, so MULTIPLY: 55 × 1.6 = <strong>88 km</strong></p>'
            '<p>Reasoning check: a mile is LONGER than a km, so the km number must be bigger.</p>',
            "M1 for × 1.6, A1 for 88. The 'bigger unit → bigger number' check catches most direction errors.") +
        EX("Convert 250 g to ounces (1 ounce = 28 g). Give your answer to 1 decimal place.",
            '<p>Grams per ounce given, so DIVIDE: 250 ÷ 28 = 8.928…</p>'
            '<p><strong>≈ 8.9 ounces</strong></p>',
            "M1 for ÷ 28, A1 for 8.9. When the conversion says '1 ounce = 28 g', ounces → divide."))
    + '<p><strong>Exam wording to expect:</strong> the conversion factor is always given for imperial units — look for "use 1 mile = …".</p>',
    questions=["Q6: Convert 2.5 gallons to litres (1 gallon = 4.5 litres)", "Q7: Convert 36.6°C… no — convert 5 stones to kg (1 stone = 6.35 kg)"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> g → kg: ÷ 1000 → <strong>4.5 kg</strong></p>'
        '<p><strong>Q2.</strong> km → m: × 1000 → <strong>3200 m</strong></p>'
        '<p><strong>Q3.</strong> 90 ÷ 60 = <strong>1.5 hours</strong></p>'
        '<p><strong>Q4.</strong> 10 × 1.6 = <strong>16 km</strong></p>'
        '<p><strong>Q5.</strong> Speed = 48 ÷ 2 = <strong>24 km/h</strong></p>'
        '<p><strong>Q6.</strong> 2.5 × 4.5 = <strong>11.25 litres</strong></p>'
        '<p><strong>Q7.</strong> 5 × 6.35 = <strong>31.75 kg</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Metric: km-m (×1000), m-cm (×100), kg-g (×1000), litre-mL (×1000)</li>'
        '<li>Imperial facts given in questions: 1 mile ≈ 1.6 km · 1 kg ≈ 2.2 lb · 1 inch ≈ 2.5 cm · 1 gallon ≈ 4.5 litres · 1 stone = 14 lb</li>'
        '<li>Bigger unit → SMALLER number when converting up (88 km is 55 miles)</li>'
        '<li>Area: square the factor; Volume: cube it</li>'
        '<li>Speed units: km/h ÷ 3.6 = m/s</li>'
        '</ul>'),
    context=CTX('<p>Conversion questions: 1–2 marks, and embedded in speed/density/recipe questions. '
        'The given-factor imperial conversions are Foundation staples on Papers 2/3.</p>'
        '<p>Links to: units and measure (G14), compound measures (R1), scale drawings (R2).</p>'))

B["A14-real-life-graphs.html"] = dict(
    marker="Q7: A distance-time graph is a straight line from (0, 0) to (4, 260)",
    worked=W_SEC("Real-life graphs test reading, not calculating: gradient = rate, area = total, shape = story.",
        EX("A distance-time graph rises steeply, then flattens to horizontal, then rises gently. Describe the journey.",
            '<p>Steep rise: fast constant speed. Horizontal: stationary (a stop). '
            'Gentle rise: slower constant speed.</p>',
            "B1 for describing all three stages with directions of speed. Horizontal NEVER means 'stopped suddenly' — it means stationary for that time.") +
        EX("A conversion graph shows £1 = $1.25. Draw how you would find the cost of £40, and state it.",
            '<p>Read across from 40 on the £ axis to the line, then down to the $ axis.</p>'
            '<p>Cost = 40 × 1.25 = <strong>$50</strong></p>',
            "M1 for using the graph (or multiplying), A1 for $50. Conversion graph questions allow either method — the graph is the point of the topic."))
    + '<p><strong>Exam wording to expect:</strong> "Describe the journey", "What does the gradient represent?", "Use the graph to convert …".</p>',
    questions=["Q7: A distance-time graph is a straight line from (0, 0) to (4, 260). What speed does it show?", "Q8: On a filling-container graph, the gradient decreases over time. What does that tell you about the container?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> Horizontal line = <strong>stationary</strong> (zero speed)</p>'
        '<p><strong>Q2.</strong> Speed = 120 ÷ 3 = <strong>40 mph</strong></p>'
        '<p><strong>Q3.</strong> Area under a speed-time graph = <strong>distance travelled</strong></p>'
        '<p><strong>Q4.</strong> 5 × 2.2 = <strong>11 pounds</strong></p>'
        '<p><strong>Q5.</strong> Narrow bottom fills fast (steep), wide top fills slowly (shallow) → '
        '<strong>gradient decreases</strong> (starts steep, becomes shallower)</p>'
        '<p><strong>Q6.</strong> Steeper = faster (more distance per hour)</p>'
        '<p><strong>Q7.</strong> Speed = 260 ÷ 4 = <strong>65 units per hour</strong></p>'
        '<p><strong>Q8.</strong> The container <strong>widens</strong> — the same inflow raises the level more slowly as the cross-section grows</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Distance-time: gradient = speed; horizontal = stationary; steeper = faster; line sloping DOWN = returning to start</li>'
        '<li>Speed-time: gradient = acceleration; area = distance; below zero = moving backwards</li>'
        '<li>Conversion graphs: read across then up/down; only valid within the drawn range</li>'
        '<li>Container graphs: gradient = rate of height increase; shape of container explains gradient changes</li>'
        '<li>Curve on distance-time = changing speed (accelerating or decelerating)</li>'
        '</ul>'),
    context=CTX('<p>Real-life graphs: 2–4 marks, usually Paper 2 (calculator allowed but rarely needed). '
        'Describing journeys in words is the AO2 skill — practise converting graph shapes into sentences.</p>'
        '<p>Links to: gradients (A10), rates of change (R14), compound measures (R1).</p>'))

B["N14-estimation-approximation.html"] = dict(
    marker="Q6: Estimate: (5.8 × 21.7) ÷ 0.48",
    worked=W_SEC("Estimation means rounding EVERY number to 1 significant figure, then computing exactly with the rounded values. State the rounded calculation — the method mark lives there.",
        EX("Estimate: 41.2 × 5.8",
            '<p>Round to 1 s.f.: 40 × 6</p>'
            '<p><strong>Estimate: 240</strong></p>',
            "M1 for 40 × 6, A1 for 240. Writing '≈ 40 × 6 = 240' is the full-mark presentation.") +
        EX("Use estimation to check whether 79 × 21 = 1659 is sensible.",
            '<p>Round: 80 × 20 = 1600. The claimed 1659 is close to 1600 → sensible ✓</p>',
            "M1 for the rounded product, A1 for the verdict. Checking questions expect a verdict sentence, not just the estimate."))
    + '<p><strong>Exam wording to expect:</strong> "Estimate …", "by rounding each number to 1 significant figure", "check whether … is sensible".</p>',
    questions=["Q6: Estimate: (5.8 × 21.7) ÷ 0.48", "Q7: Estimate the cost of 38 items at £4.90 each"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 70 × 50 = <strong>3500</strong></p>'
        '<p><strong>Q2.</strong> 600 ÷ 30 = <strong>20</strong></p>'
        '<p><strong>Q3.</strong> 0.7 × 400 = <strong>280</strong></p>'
        '<p><strong>Q4.</strong> 9 × 3 = <strong>27</strong></p>'
        '<p><strong>Q5.</strong> 60 × 90 = 5400; 5518 ≈ 5400 → <strong>sensible ✓</strong></p>'
        '<p><strong>Q6.</strong> (6 × 20) ÷ 0.5 = 120 ÷ 0.5 = <strong>240</strong> — '
        'dividing by 0.5 doubles: the step students miss</p>'
        '<p><strong>Q7.</strong> 40 × 5 = <strong>£200</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Round EVERY value to 1 significant figure before calculating</li>'
        '<li>÷ by 0.5 doubles; ÷ by 0.25 quadruples</li>'
        '<li>Show the rounded calculation — "≈ 70 × 50 = 3500" — for the method mark</li>'
        '<li>Estimates check sensibility: the real answer should be within ~20% of the estimate</li>'
        '<li>1 s.f. examples: 73 → 70 · 48 → 50 · 592 → 600 · 0.68 → 0.7 · 8.9 → 9</li>'
        '</ul>'),
    context=CTX('<p>Estimation: 2–3 marks on Paper 1 (non-calculator). The check-the-answer version '
        'adds an AO3 mark for the verdict. Rounding to 1 s.f. itself is examined directly in N15.</p>'
        '<p>Links to: significant figures and error intervals (N15), calculator checks (all Papers 2/3).</p>'))

B["A8-coordinates.html"] = dict(
    marker="Q7: Find the midpoint of (−4, 7) and (2, −1)",
    worked=W_SEC("Coordinates: x first (across), y second (up). Midpoint = average the x\u2019s, average the y\u2019s.",
        EX("Find the midpoint of (2, −3) and (8, 5).",
            '<p>x: (2 + 8) ÷ 2 = 5 &nbsp;·&nbsp; y: (−3 + 5) ÷ 2 = 1</p>'
            '<p><strong>Midpoint: (5, 1)</strong></p>',
            "M1 for averaging, A1 for (5, 1). Works with negatives: the average of −3 and 5 is +1.") +
        EX("Write down the coordinates of the point 4 units LEFT and 2 units DOWN from (1, 6).",
            '<p>Left = x decreases: 1 − 4 = −3. Down = y decreases: 6 − 2 = 4</p>'
            '<p><strong>(−3, 4)</strong></p>',
            "B1 for (−3, 4). Left/right change x; up/down change y — never both."))
    + '<p><strong>Exam wording to expect:</strong> "Write down the coordinates of …", "Find the midpoint of A and B", "Plot the point …".</p>',
    questions=["Q7: Find the midpoint of (−4, 7) and (2, −1)", "Q8: A square has vertices (1,1), (5,1) and (5,5). Write the fourth vertex."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> Negative x, positive y → <strong>2nd quadrant</strong></p>'
        '<p><strong>Q2.</strong> 3 right from (−2, 5): −2 + 3 → <strong>(1, 5)</strong></p>'
        '<p><strong>Q3.</strong> x: (4 + 10)/2 = 7; y: (2 + 8)/2 = 5 → <strong>(7, 5)</strong></p>'
        '<p><strong>Q4.</strong> x: (−2 + 6)/2 = 2; y: (3 + (−5))/2 = −1 → <strong>(2, −1)</strong></p>'
        '<p><strong>Q5.</strong> Directly below on the x-axis → same x, y = 0 → <strong>(3, 0)</strong></p>'
        '<p><strong>Q6.</strong> Same x (vertical line): 5 − (−1) = <strong>6 units</strong></p>'
        '<p><strong>Q7.</strong> x: (−4 + 2)/2 = −1; y: (7 + (−1))/2 = 3 → <strong>(−1, 3)</strong></p>'
        '<p><strong>Q8.</strong> Missing corner completes the square: <strong>(1, 5)</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>(x, y): across first, up second · origin (0, 0)</li>'
        '<li>Quadrants: 1 (+,+) · 2 (−,+) · 3 (−,−) · 4 (+,−) — anticlockwise from top-right</li>'
        '<li>Midpoint: ((x₁+x₂)/2, (y₁+y₂)/2)</li>'
        '<li>Same x-coordinate → vertical line; same y → horizontal line</li>'
        '<li>Vertical distance = difference in y; horizontal distance = difference in x</li>'
        '</ul>'),
    context=CTX('<p>Coordinates feed straight-line graphs, transformations and Pythagoras distance: '
        '1–3 marks each time. Midpoint and quadrant recall are Paper 1 regulars.</p>'
        '<p>Links to: straight-line graphs (A9/A10), transformations (G7), Pythagoras (G20).</p>'))

B["R9-percentages.html"] = dict(
    marker="Q6: £2400 is invested at 3% compound interest for 5 years. Find the final amount",
    worked=W_SEC("Percentages of amounts have three moves: multiplier for one-step change, change ÷ original for % change, and divide-back for reverse questions.",
        EX("A population of 12,000 falls by 8%. Find the new population.",
            '<p>Multiplier: 100% − 8% = 92% = 0.92</p>'
            '<p>12,000 × 0.92 = <strong>11,040</strong></p>',
            "M1 for 0.92, A1 for 11,040. One multiplication replaces find-10%-and-subtract, and survives awkward percentages.") +
        EX("A coat costs £96 after a 20% reduction. Find the original price.",
            '<p>£96 = 80% of the original → 1% = 96 ÷ 80 = £1.20 → 100% = <strong>£120</strong></p>',
            "M1 for 96 ÷ 80, A1 for £120. NEVER add 20% back on (96 × 1.2 = £115.20 is wrong — the 20% comes off a bigger base)."))
    + '<p><strong>Exam wording to expect:</strong> "Find …% of …", "Calculate the percentage change", "Find the original price", "compound interest".</p>',
    questions=["Q6: £2400 is invested at 3% compound interest for 5 years. Find the final amount", "Q7: A price rises from £75 to £87. Find the percentage increase."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 0.28 × 350 = <strong>£98</strong></p>'
        '<p><strong>Q2.</strong> 1.35 × 720 = <strong>£972</strong></p>'
        '<p><strong>Q3.</strong> Change 12, original 40: 12 ÷ 40 × 100 = <strong>30%</strong></p>'
        '<p><strong>Q4.</strong> £420 = 75% → 1% = 5.60 → original = <strong>£560</strong>. '
        'Check: 560 × 0.75 = 420 ✓</p>'
        '<p><strong>Q5.</strong> 3000 × 1.05⁴ = 3000 × 1.21550625 = <strong>£3646.52</strong></p>'
        '<p><strong>Q6.</strong> 2400 × 1.03⁵ = 2400 × 1.15927407 = <strong>£2782.26</strong></p>'
        '<p><strong>Q7.</strong> Change 12 ÷ 75 × 100 = <strong>16%</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Multipliers: +15% → 1.15 · −15% → 0.85 · +2.5% → 1.025</li>'
        '<li>% change = change ÷ ORIGINAL × 100</li>'
        '<li>Reverse: given the after-value, divide by the multiplier (never add the % back)</li>'
        '<li>Compound interest: amount × multiplierⁿ (n = years)</li>'
        '<li>Fraction shortcuts: 10% = ÷10 · 1% = ÷100 · 50% = ÷2 · 25% = ÷4</li>'
        '</ul>'),
    context=CTX('<p>Percentages: the highest-frequency money topic — 4–6 marks per paper across '
        'simple, change, reverse and compound. Compound interest is a Paper 2/3 calculator regular.</p>'
        '<p>Links to: fractions and operators (N12), growth and decay (R16), ratio (R4).</p>'))

if __name__ == "__main__":
    run(B)
