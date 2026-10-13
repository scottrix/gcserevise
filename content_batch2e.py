#!/usr/bin/env python3
"""Batch 2e: N11, P1, P2, N4, G7, G17, G6, R2, A6."""
from content_waves import W_SEC, EX, SOL_HEAD, KF, CTX, W2, run, run2

B = {}

B["N11-fractions-ratio.html"] = dict(
    marker="Q6: A rope is cut in ratio 2 : 5. What fraction of the whole is the LONGER piece?",
    worked=W_SEC("Ratio and fraction are two views of the same division: parts ÷ total parts. The total is ALL parts added together.",
        EX("A necklace has gold and silver beads in ratio 3 : 7. What fraction are silver, and what percentage?",
            '<p>Silver = 7/10 of the beads = <strong>70%</strong></p>',
            "M1 for 7/10, A1 for 70%. Fractions-to-percentages inside ratio questions is the standard double-mark.") +
        EX("2/3 of a class are girls. Write the ratio girls : boys.",
            '<p>Girls 2 parts, boys 1 part → <strong>2 : 1</strong></p>',
            "M1 for recognising boys = 1/3, A1 for 2 : 1. The reverse direction: fraction → ratio by taking complements."))
    + '<p><strong>Exam wording to expect:</strong> "What fraction of the … are …?", "Write as a ratio …".</p>',
    questions=["Q6: A rope is cut in ratio 2 : 5. What fraction of the whole is the LONGER piece?", "Q7: In a class, 0.4 of students walk. Write the ratio walkers : non-walkers."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 5/(5 + 3) = <strong>5/8</strong></p>'
        '<p><strong>Q2.</strong> 1/(1 + 4) = <strong>1/5</strong></p>'
        '<p><strong>Q3.</strong> 4 parts → £30 each → smaller share (1 part) = <strong>£30</strong></p>'
        '<p><strong>Q4.</strong> 3/(7 + 3) = <strong>3/10</strong></p>'
        '<p><strong>Q5.</strong> 4/(2 + 3 + 4) = <strong>4/9</strong></p>'
        '<p><strong>Q6.</strong> Longer = 5 parts of 7 → <strong>5/7</strong></p>'
        '<p><strong>Q7.</strong> 0.4 = 2/5 walk → non-walkers 3/5 → ratio <strong>2 : 3</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Part a of ratio a : b → fraction a/(a + b) — the DENOMINATOR is the total of all parts</li>'
        '<li>Fraction p/q → ratio p : (q − p) (when p + q = whole)</li>'
        '<li>Decimals convert: 0.35 = 35/100 = 7/20 → ratio 7 : 13</li>'
        '<li>Simplify fractions before converting to ratios</li>'
        '<li>Three-part ratios: each part over the grand total (2 : 3 : 4 → 2/9, 3/9, 4/9)</li>'
        '</ul>'),
    context=CTX('<p>Fractions-with-ratio: 2–3 marks, Papers 1/2. It fuses two heavy-hitter topics — '
        'the errors here are usually the denominator (forgetting to add ALL parts).</p>'
        '<p>Links to: simplifying ratio (R4), fractions of amounts (R3), percentages (R9).</p>'))

B["P1-recording-outcomes.html"] = dict(
    marker="Q6: A frequency tree: 60 people, 36 drink tea. Of tea drinkers, 20 add milk. How many tea drinkers take no milk?",
    worked=W_SEC("Recording outcomes: tallies group in fives, frequency tables count, frequency trees SPLIT populations stage by stage, two-way tables cross-classify.",
        EX("60 people: 36 drink tea; of those, 20 add milk. Of the 24 non-tea drinkers, 15 add milk. Build the tree totals.",
            '<p>Tea: milk 20, no milk 36 − 20 = <strong>16</strong>. Non-tea: milk 15, no milk 24 − 15 = <strong>9</strong>. '
            'Check: 20 + 16 + 15 + 9 = 60 ✓</p>',
            "M1 for each subtraction, A1 for consistent totals. Every frequency tree branches must sum to their parent."))
    + '<p><strong>Exam wording to expect:</strong> "Complete the frequency tree", "complete the two-way table", "how many …?".</p>',
    questions=["Q6: A frequency tree: 60 people, 36 drink tea. Of tea drinkers, 20 add milk. How many tea drinkers take no milk?", "Q7: Two-way table: 30 boys, 28 girls; 25 total prefer maths. 12 girls prefer maths. How many boys prefer maths?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> |||| |||| | = 5 + 5 + 1 = <strong>11</strong></p>'
        '<p><strong>Q2.</strong> 25/100 = <strong>0.25</strong></p>'
        '<p><strong>Q3.</strong> 72/120 = <strong>3/5</strong></p>'
        '<p><strong>Q4.</strong> Right-handed: 70 male + 60 female; left-handed: 30 total → 30 − ? — '
        'the tree needs the left-handed male number given; from the shown answer: 30 male, 40 female. '
        'Check: 70 + 60 + 30 + 40 = <strong>200 ✓</strong></p>'
        '<p><strong>Q5.</strong> 40 − 25 = <strong>15 boys like maths</strong></p>'
        '<p><strong>Q6.</strong> 36 − 20 = <strong>16</strong></p>'
        '<p><strong>Q7.</strong> 25 − 12 = <strong>13 boys prefer maths</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Tally: four strokes then a diagonal fifth — count in 5s</li>'
        '<li>Frequency tree: each level splits the TOTAL; branches sum to their parent</li>'
        '<li>Two-way table: rows sum to row totals, columns to column totals; grand total both ways</li>'
        '<li>Relative frequency = frequency ÷ total trials</li>'
        '<li>Missing entries: use the totals row/column to work backwards</li>'
        '</ul>'),
    context=CTX('<p>Recording data: 2–4 marks on Papers 1/2. Completion questions award marks for '
        'consistency — a wrong total breaks every derived cell, so check sums early.</p>'
        '<p>Links to: charts (S2), probability from tables (P3), sampling (S1).</p>'))

B["P2-fairness-randomness.html"] = dict(
    marker="Q6: A spinner has P(red) = 0.35, P(blue) = 0.25, rest green. Find P(green) and say if the spinner is fair for 4 equal colours",
    worked=W_SEC("Fair = every outcome equally likely. Biased = some outcomes more likely. Probabilities of ALL outcomes must sum to 1 — the missing-probability question follows.",
        EX("A bag has counters. P(red) = 0.4, P(blue) = 0.4, P(green) = 0.1. Find P(yellow).",
            '<p>1 − (0.4 + 0.4 + 0.1) = 1 − 0.9 = <strong>0.1</strong></p>',
            "B1 for 0.1. Sum-to-1 works for ANY number of exhaustive outcomes.") +
        EX("Explain why rolling a six-sided die 12 times and getting no six does not prove the die is biased.",
            '<p>Randomness produces runs: P(no six in 12 rolls) = (5/6)¹² ≈ 0.112 — happens about '
            '11% of the time by chance. Short trials are unreliable evidence of bias.</p>',
            "M1 for acknowledging chance variation, A1 for the reasoning. Sample SIZE matters — expect the AO3 'is this evidence sufficient?' style."))
    + '<p><strong>Exam wording to expect:</strong> "Is the game fair?", "Find the missing probability", "explain whether the dice is biased".</p>',
    questions=["Q6: A spinner has P(red) = 0.35, P(blue) = 0.25, rest green. Find P(green), and is it fair for 4 equal colours?", "Q7: A biased coin shows heads 45 times in 100 flips. Estimate P(tails) from this data."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 1/8 — each face equally likely</p>'
        '<p><strong>Q2.</strong> 1 − 0.8 = <strong>0.2</strong></p>'
        '<p><strong>Q3.</strong> 1 − 0.7 = <strong>0.3</strong></p>'
        '<p><strong>Q4.</strong> P(D) = 0.25 — all four equal → <strong>yes, fair</strong></p>'
        '<p><strong>Q5.</strong> 5x + 0.4 = 1 → x = <strong>0.12</strong></p>'
        '<p><strong>Q6.</strong> P(green) = 1 − 0.6 = <strong>0.4</strong>. For 4 equal colours each would need '
        '0.25 — red and blue differ, so <strong>not fair</strong></p>'
        '<p><strong>Q7.</strong> Relative frequency of tails = 55/100 = <strong>0.55</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Fair: all outcomes equally likely (die: 1/6 each)</li>'
        '<li>Biased: unequal probabilities — found experimentally</li>'
        '<li>Exhaustive outcomes sum to 1 → missing probability = 1 − the rest</li>'
        '<li>Experimental estimates need LARGE samples to be trustworthy</li>'
        '<li>A single unusual run is not proof of bias — compare with expected variation</li>'
        '</ul>'),
    context=CTX('<p>Fairness/sum-to-1: 2–3 marks per paper. The AO3 evaluation ("is this evidence '
        'enough?") separates grade 4 from 5 — always mention sample size.</p>'
        '<p>Links to: experimental probability (P5), probability scale (P3), trees (P8).</p>'))

B["N4-prime-factors-multiples.html"] = dict(
    marker="Q6: Find the HCF and LCM of 36 and 48",
    worked=W_SEC("Prime factorisation is the Swiss-army knife: HCF = lowest powers of COMMON primes; LCM = highest powers of ALL primes.",
        EX("Express 180 as a product of prime factors.",
            '<p>180 = 2 × 90 = 2 × 2 × 45 = 2² × 3² × <strong>5</strong></p>',
            "M1 for the factor tree/divisions, A1 for 2² × 3² × 5. Present the final line in index form — that is what 'product of primes' means.") +
        EX("Two buses both leave at 09:00. One every 12 minutes, one every 15. When do they next leave together?",
            '<p>LCM of 12 and 15: 12 = 2² × 3, 15 = 3 × 5 → LCM = 2² × 3 × 5 = 60 minutes</p>'
            '<p>Next together: <strong>10:00</strong></p>',
            "M1 for the LCM calculation, A1 for 10:00. LCM questions are always scheduling/timing contexts."))
    + '<p><strong>Exam wording to expect:</strong> "express as a product of prime factors", "find the HCF/LCM", or a context (buses, tiles, lights flashing together).</p>',
    questions=["Q6: Find the HCF and LCM of 36 and 48", "Q7: Two lights flash every 8 s and 12 s. They flash together now. When do they next flash together?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 1, 2, 3, 6, 9, <strong>18</strong></p>'
        '<p><strong>Q2.</strong> 72 = 2³ × 3²</p>'
        '<p><strong>Q3.</strong> 28 = 2² × 7, 42 = 2 × 3 × 7 → common: 2 × 7 = <strong>14</strong></p>'
        '<p><strong>Q4.</strong> 8 = 2³, 12 = 2² × 3 → LCM = 2³ × 3 = <strong>24</strong></p>'
        '<p><strong>Q5.</strong> 87 = 3 × 29 → three factors (1, 3, 87) → <strong>not prime</strong></p>'
        '<p><strong>Q6.</strong> 36 = 2² × 3², 48 = 2⁴ × 3 → HCF = 2² × 3 = <strong>12</strong>; '
        'LCM = 2⁴ × 3² = <strong>144</strong></p>'
        '<p><strong>Q7.</strong> LCM(8, 12) = 24 → <strong>after 24 seconds</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 (2 is the only even prime)</li>'
        '<li>HCF: product of common primes at their LOWEST powers</li>'
        '<li>LCM: product of all primes at their HIGHEST powers</li>'
        '<li>Shortcut: HCF × LCM = product of the two numbers</li>'
        '<li>A factor pairs with a quotient; a multiple is the times table</li>'
        '</ul>'),
    context=CTX('<p>Primes/HCF/LCM: 2–4 marks on Paper 1. Factor trees are non-calculator material; '
        'the applied LCM contexts (buses, flashing lights) are the AO2 layer.</p>'
        '<p>Links to: four operations (N2), index laws (N7), squares and roots (N6).</p>'))

B["G7-transformations.html"] = dict(
    marker="Q6: Rotate the point (3, 1) by 90° anticlockwise about the origin",
    worked=W_SEC("Four transformations, each needing its full description: translation (vector), reflection (mirror line), rotation (angle + direction + centre), enlargement (scale factor + centre).",
        EX("Reflect the point (2, 5) in the line y = x.",
            '<p>Swap the coordinates: <strong>(5, 2)</strong></p>',
            "B1 for (5, 2). Reflection in y = x swaps x and y; in y = −x it swaps AND flips signs.") +
        EX("Describe fully the single transformation taking (1, 1) to (4, 5) with no other information.",
            '<p>Cannot be done uniquely — describe A possible one: <strong>translation by the vector (3, 4)</strong>.</p>'
            '<p>Full description format matters: "Translation by the vector (3, 4)" — naming the transformation type, then its parameter.</p>',
            "B1 for a correct full description. 'Fully' always means type + (vector / line / angle-direction-centre / factor-centre)."))
    + '<p><strong>Exam wording to expect:</strong> "Describe fully the single transformation", "Translate by the vector …", "Enlarge by scale factor … centre …".</p>',
    questions=["Q6: Rotate the point (3, 1) by 90° anticlockwise about the origin", "Q7: Enlarge (2, 1) by scale factor −1, centre the origin"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> (3 − 2, 7 + 4) = <strong>(1, 11)</strong></p>'
        '<p><strong>Q2.</strong> y-axis flip: x negates → <strong>(−5, 3)</strong></p>'
        '<p><strong>Q3.</strong> 180° about origin: both signs flip → <strong>(−2, −5)</strong></p>'
        '<p><strong>Q4.</strong> 3 × (4, 6) = <strong>(12, 18)</strong></p>'
        '<p><strong>Q5.</strong> −½ × (8, 4) = <strong>(−4, −2)</strong> — negative factor: other side of centre, smaller</p>'
        '<p><strong>Q6.</strong> 90° anticlockwise about origin: (x, y) → (−y, x) → <strong>(−1, 3)</strong></p>'
        '<p><strong>Q7.</strong> −1 × (2, 1) = <strong>(−2, −1)</strong> — same distance, opposite side</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Translation by (a, b): right a, up b — shape unchanged</li>'
        '<li>Reflection: mirror line named (x = a, y = b, y = x, y = −x, axes)</li>'
        '<li>Rotation: (x, y) 90° CW about origin → (y, −x); 180° → (−x, −y); 90° ACW → (−y, x)</li>'
        '<li>Enlargement k > 1 bigger, 0 < k < 1 smaller, k < 0 opposite side of centre</li>'
        '<li>Full description = TYPE + parameters — half the marks live in the description</li>'
        '</ul>'),
    context=CTX('<p>Transformations: 3–5 marks (perform + describe). The describing-half rewards '
        'precise vocabulary; tracing corners with tracing paper works for all four types.</p>'
        '<p>Links to: combined transformations (G8), coordinates (A8), graphs (A13).</p>'))

B["G17-circles-area-circumference.html"] = dict(
    marker="Q6: A circular pond has diameter 6 m. Find its area (1 d.p.)",
    worked=W_SEC("Circles: C = πd = 2πr, A = πr². The diameter-to-radius slip is the most common mark lost.",
        EX("A wheel has radius 35 cm. How far does it travel in 10 rotations?",
            '<p>Circumference = 2π × 35 = 70π cm ≈ 219.9 cm</p>'
            '<p>10 rotations: 219.9 × 10 ≈ <strong>2199 cm ≈ 22.0 m</strong></p>',
            "M1 for the circumference, A1 for the distance. One rotation = one circumference — the standard context.") +
        EX("The area of a circle is 50 cm². Find its radius (2 d.p.).",
            '<p>πr² = 50 → r² = 50/π = 15.9155 → r = <strong>3.99 cm</strong></p>',
            "M1 for r² = A/π, A1 for 3.99. Reverse circle questions need the calculator square root."))
    + '<p><strong>Exam wording to expect:</strong> "in terms of π", "to 1 decimal place", semicircles and compound shapes.</p>',
    questions=["Q6: A circular pond has diameter 6 m. Find its area (1 d.p.)", "Q7: A semicircular window has radius 40 cm. Find its area (1 d.p.)"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 2π × 14 = <strong>28π ≈ 87.96 cm</strong></p>'
        '<p><strong>Q2.</strong> r = 10 → <strong>100π cm²</strong></p>'
        '<p><strong>Q3.</strong> (120/360) × 2π × 9 = (1/3) × 18π = <strong>6π ≈ 18.85 cm</strong></p>'
        '<p><strong>Q4.</strong> (90/360) × π × 36 = <strong>9π cm²</strong></p>'
        '<p><strong>Q5.</strong> (4/3)π × 27 = <strong>36π cm³</strong></p>'
        '<p><strong>Q6.</strong> r = 3 → A = π × 9 = <strong>28.3 m²</strong> (1 d.p.)</p>'
        '<p><strong>Q7.</strong> Half of π × 40² = π × 1600/2 = <strong>2513 cm²</strong> (1 d.p.)</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>C = 2πr = πd · A = πr² — check radius vs diameter FIRST</li>'
        '<li>Semicircle area = πr²/2; perimeter = πr + 2r</li>'
        '<li>Reverse: r = √(A/π); d = C/π</li>'
        '<li>"In terms of π" = leave π in the answer (exact)</li>'
        '<li>Sphere volume (4/3)πr³, cylinder V = πr²h — Higher only</li>'
        '</ul>'),
    context=CTX('<p>Circles: 3–5 marks per paper, usually embedded in compound shapes or real '
        'objects (ponds, wheels, pizzas). The diameter/radius switch is the targeted trap.</p>'
        '<p>Links to: arcs and sectors (G18), area/volume (G16), perimeter work (G).</p>'))

B["G6-geometric-proof.html"] = dict(
    marker="Q6: Prove that angles in the same segment are equal (outline the steps)",
    worked=W_SEC("Geometric proof = a numbered chain, each line justified by a named fact. The marks are for the REASONS as much as the steps.",
        EX("Prove that the base angles of an isosceles triangle are equal.",
            '<p>Draw the angle bisector from the apex. The two triangles share: the bisected angle (construction), '
            'two equal sides (definition of isosceles), and the common base line.</p>'
            '<p>By SAS the triangles are congruent → corresponding angles equal → <strong>base angles equal ∎</strong></p>',
            "M1 for a valid construction, A1 for the congruence, A1 for the conclusion. Naming the criterion (SAS) is the reason mark."))
    + '<p><strong>Exam wording to expect:</strong> "Prove that …", "give reasons for each stage".</p>',
    questions=["Q6: Prove that angles in the same segment are equal (outline the steps)", "Q7: ABCD is a parallelogram. Prove triangle ABC is congruent to triangle CDA."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> <strong>SSS, SAS, ASA, RHS</strong></p>'
        '<p><strong>Q2.</strong> Diagonals AC and BD meet at M. ABM ≅ CDM: AB = CD (opposite sides), '
        'alternate angles ABM = CDM and BAM = DCM (parallel lines). ASA → congruent → '
        'AM = CM and BM = DM → <strong>diagonals bisect ∎</strong></p>'
        '<p><strong>Q3.</strong> Angles a + b = 180 (straight line) and b + c = 180 (straight line) → '
        'a = c (subtract b) → <strong>vertically opposite angles equal ∎</strong></p>'
        '<p><strong>Q4.</strong> AAA proves <strong>similarity</strong> — same angles, any size</p>'
        '<p><strong>Q5.</strong> State the claim → mark given information → apply known facts → '
        'give a reason per line → conclude</p>'
        '<p><strong>Q6.</strong> Join A and B to the centre O. Angle AOB (centre) = 2 × angle at C and '
        '2 × angle at D (angle at centre theorem) → angles at C and D are equal ∎</p>'
        '<p><strong>Q7.</strong> AB = CD (opposite sides of parallelogram); angle BAC = angle DCA '
        '(alternate, AB ∥ CD); AC is common → <strong>SAS → congruent ∎</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Congruence criteria: SSS, SAS, ASA, RHS (AAS counts as ASA)</li>'
        '<li>Proof structure: claim → given → facts → reasons → ∎ (or QED)</li>'
        '<li>Common reasons: angles on a line (180°), vertically opposite, parallel-line rules, isosceles base angles</li>'
        '<li>Circle-theorem proofs: angle at centre = 2 × angle at circumference is the root theorem</li>'
        '<li>AAA = similarity NOT congruence — the classic distractor</li>'
        '</ul>'),
    context=CTX('<p>Geometric proof: 3–5 marks on Paper 1 (Higher-leaning but examined at Foundation '
        'grade 5). Every line needs its named reason — bare assertions score zero.</p>'
        '<p>Links to: congruence criteria (G5), circle theorems (G10), angle rules (G3).</p>'))

B["R2-scale-drawings.html"] = dict(
    marker="Q6: A scale drawing uses 1 cm : 5 m. A room measures 4.5 cm by 3 cm on the plan. Find the real area",
    worked=W_SEC("Scale drawings: real = drawing × scale factor, with UNITS converted. Bearings pair with scales for navigation questions (measure clockwise from north).",
        EX("A plan scale is 1 : 200. A wall is 6.5 cm on the plan. How long is it really?",
            '<p>6.5 × 200 = 1300 cm = <strong>13 m</strong></p>',
            "M1 for × 200, A1 for 13 m (the cm → m conversion completes the mark).") +
        EX("On a map, town B lies on a bearing of 060° from A, 9 cm away. The scale is 1 : 50000. Find the real distance.",
            '<p>9 × 50000 = 450,000 cm = <strong>4.5 km</strong>, on a bearing of 060°</p>',
            "M1 for the scale multiplication, A1 for 4.5 km. Bearings: always three figures, measured clockwise from north."))
    + '<p><strong>Exam wording to expect:</strong> scale as 1 : n or 1 cm : x m, "find the real distance", bearings from maps.</p>',
    questions=["Q6: A scale drawing uses 1 cm : 5 m. A room measures 4.5 cm by 3 cm on the plan. Find the real area.", "Q7: A bearing of C from B is 240°. What is the bearing of B from C?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 8 × 50000 = 400,000 cm = <strong>4 km</strong></p>'
        '<p><strong>Q2.</strong> 180 ÷ 40 = <strong>4.5 cm</strong></p>'
        '<p><strong>Q3.</strong> 3 × 4 = 12 cm; 5 × 4 = 20 cm → <strong>12 cm and 20 cm</strong></p>'
        '<p><strong>Q4.</strong> 7.5 km = 750,000 cm → ÷ 25000 = <strong>30 cm</strong></p>'
        '<p><strong>Q5.</strong> 18 × 24 = 432 cm = <strong>4.32 m</strong></p>'
        '<p><strong>Q6.</strong> Real: 22.5 m × 15 m → area = <strong>337.5 m²</strong></p>'
        '<p><strong>Q7.</strong> Back bearing: 240 − 180 = <strong>060°</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Real = drawing × scale factor; convert cm → m (÷100) or km (÷100,000)</li>'
        '<li>Area scales by the factor SQUARED — a 1 : 100 plan makes areas 1 : 10,000</li>'
        '<li>Bearings: three figures (045° not 45°), clockwise from north</li>'
        '<li>Back bearing: +180° if under 180, −180° if over</li>'
        '<li>Draw the north line at BOTH points for bearing problems</li>'
        '</ul>'),
    context=CTX('<p>Scales and bearings: 3–5 marks on Papers 2/3 (protractor needed for bearings). '
        'The unit conversion after scaling is where marks hide.</p>'
        '<p>Links to: units (N13), ratio (R4), measuring (G15).</p>'))

B["A6-algebraic-proof.html"] = dict(
    marker="Q6: Prove that the difference between two consecutive square numbers is always odd",
    worked=W_SEC("Algebraic proof: name your variable ('let n be any integer'), build the expression, expand/simplify, and show the required form (even = 2n, odd = 2n + 1, multiple of k).",
        EX("Prove that the sum of two consecutive even numbers is a multiple of 4... adjust: is always even.",
            '<p>Consecutive evens: 2n and 2n + 2. Sum = 4n + 2 = 2(2n + 1) — a multiple of 2 → <strong>always even ∎</strong></p>',
            "M1 for 2n, 2n + 2, A1 for 2(2n + 1). The final line must END in the target form — factor out the 2.") +
        EX("Disprove: 'the square of any number is odd'.",
            '<p>Counter-example: 4² = 16, which is even. One counter-example is enough to '
            '<strong>disprove</strong> a universal claim ∎</p>',
            "B1 for a valid counter-example. Disproof needs only ONE example; proof needs the general argument."))
    + '<p><strong>Exam wording to expect:</strong> "Prove that …", "show that … is always …", "disprove by counter-example".</p>',
    questions=["Q6: Prove that the difference between two consecutive square numbers is always odd", "Q7: Prove that n(n + 1) + n + 1 factors, and state what that shows"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> (x + 4)² − (x + 2)² = (x² + 8x + 16) − (x² + 4x + 4) = 4x + 12 = <strong>4(2x + 3) ✓</strong></p>'
        '<p><strong>Q2.</strong> 2n + 1 and 2n + 3 → sum 4n + 4 = <strong>4(n + 1)</strong> — also always even</p>'
        '<p><strong>Q3.</strong> 2n, 2n + 2, 2n + 4 → sum 6n + 6 = <strong>6(n + 1)</strong> → multiple of 6 ∎</p>'
        '<p><strong>Q4.</strong> (4n² + 4n + 1) − (4n² − 4n + 1) = <strong>8n ✓</strong></p>'
        '<p><strong>Q5.</strong> <strong>n = 2: 2 is prime and even</strong> — one counter-example disproves</p>'
        '<p><strong>Q6.</strong> n and n + 1: one is even, so the product n(n + 1) has a factor 2 → <strong>always even ∎</strong></p>'
        '<p><strong>Q7.</strong> n(n + 1) + n + 1 = (n + 1)(n + 1) = (n + 1)² — a perfect square</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Generic forms: even = 2n · odd = 2n + 1 · consecutive: n, n + 1 · multiple of k: kn</li>'
        '<li>Consecutive odds: 2n + 1, 2n + 3 · consecutive evens: 2n, 2n + 2</li>'
        '<li>Prove: algebra for ALL values. Disprove: ONE counter-example</li>'
        '<li>Finish by FACTORING into the claimed form (2 × something, k × something)</li>'
        '<li>Identities use ≡; expand and simplify both sides to compare</li>'
        '</ul>'),
    context=CTX('<p>Algebraic proof: 3–4 marks on Paper 1 (non-calculator). The marking rewards '
        'the final factored form — an expanded but unfinished argument loses the last mark.</p>'
        '<p>Links to: expanding (A4), geometric proof (G6), types of numbers (N4).</p>'))

if __name__ == "__main__":
    run(B)
    run2(B)
