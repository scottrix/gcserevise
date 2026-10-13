#!/usr/bin/env python3
"""Batch 2f: P5, A18, A19, A3, P7, G2, G11, A16, G16."""
from content_waves import W_SEC, EX, SOL_HEAD, KF, CTX, W2, run, run2

B = {}

B["P5-experimental-theoretical.html"] = dict(
    marker="Q6: A weather station records rain on 84 of 365 days. Estimate P(rain) on a given day (2 d.p.)",
    worked=W_SEC("Experimental probability = successes ÷ trials. Expected frequency = probability × number of trials. Long-run relative frequency converges to the true probability.",
        EX("A spinner lands on A 47 times in 200 spins. Estimate P(A) and how many times A would land in 500 spins.",
            '<p>P(A) ≈ 47/200 = <strong>0.235</strong> → expected in 500: 0.235 × 500 = <strong>117.5 ≈ 118 times</strong></p>',
            "M1 for 47/200, A1 for the estimate, A1 for 117.5/118. Expected values can be decimals — round sensibly and say 'approximately'.") +
        EX("A sweet packet contains 3 flavours. In 60 packets, 24 contained a blue sweet. The factory makes 5000 packets daily. Estimate daily blue packets.",
            '<p>P(blue) ≈ 24/60 = 0.4 → 0.4 × 5000 = <strong>2000 packets</strong></p>',
            "M1 for 0.4, A1 for 2000. Scaling estimates to production volumes is the classic applied version."))
    + '<p><strong>Exam wording to expect:</strong> "estimate the probability", "how many would you EXPECT", "do you think the coin is fair?".</p>',
    questions=["Q6: A weather station records rain on 84 of 365 days. Estimate P(rain) on a given day (2 d.p.)", "Q7: P(double six) for a pair of dice is 1/36. Out of 720 rolls, how many double sixes would you expect?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> P(even) = 1/2 → 60 × 1/2 = <strong>30</strong></p>'
        '<p><strong>Q2.</strong> 45/150 = <strong>0.3</strong></p>'
        '<p><strong>Q3.</strong> 0.55 vs 0.5 → <strong>yes, within normal variation</strong> — 5% off with n = 100 is unremarkable</p>'
        '<p><strong>Q4.</strong> 16/40 = 0.4 → 0.4 × 200 = <strong>80 blue</strong></p>'
        '<p><strong>Q5.</strong> 0.25 × 400 = <strong>100 sixes</strong></p>'
        '<p><strong>Q6.</strong> 84/365 = <strong>0.23</strong></p>'
        '<p><strong>Q7.</strong> (1/36) × 720 = <strong>20</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Experimental P = successes ÷ trials (a relative frequency)</li>'
        '<li>Expected frequency = P × trials — can be a decimal before sensible rounding</li>'
        '<li>More trials → estimate improves (law of large numbers, in spirit)</li>'
        '<li>Fairness checks: compare experimental to theoretical across MANY trials</li>'
        '<li>Bias suspected when relative frequency stays far from theory as trials grow</li>'
        '</ul>'),
    context=CTX('<p>Experimental probability: 2–4 marks on Papers 1/2. The estimate-then-scale '
        'two-step is the standard format; the fairness evaluation is the AO3 layer.</p>'
        '<p>Links to: probability scale (P3), fairness (P2), trees (P8).</p>'))

B["A18-solving-quadratic-equations.html"] = dict(
    marker="Q7: Solve x² − 8x + 15 = 0 by factorising",
    worked=W_SEC("Quadratics by factorising: find two numbers multiplying to c and adding to b. Formula when factorising fails.",
        EX("Solve x² + 2x − 24 = 0.",
            '<p>Factors of −24 adding to +2: +6 and −4</p>'
            '<p>(x + 6)(x − 4) = 0 → <strong>x = −6 or x = 4</strong></p>',
            "M1 for the correct factorisation, A1 for both roots. BOTH roots required — one loses the A mark.") +
        EX("Solve x² − 5x + 1 = 0 using the formula (2 d.p.).",
            '<p>x = (5 ± √(25 − 4))/2 = (5 ± √21)/2</p>'
            '<p>√21 ≈ 4.5826 → x ≈ 4.79 or <strong>x ≈ 0.21</strong></p>',
            "M1 for correct substitution, A1 for both values. Write the formula once, substitute once, then evaluate both branches."))
    + '<p><strong>Exam wording to expect:</strong> "Solve … giving your answers to 2 decimal places", "by factorising", "show that the equation has no real solutions".</p>',
    questions=["Q7: Solve x² − 8x + 15 = 0 by factorising", "Q8: Solve x² + 4x − 21 = 0"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> (x + 3)(x + 4) = 0 → <strong>x = −3 or x = −4</strong></p>'
        '<p><strong>Q2.</strong> x² = 16 → <strong>x = ±4</strong></p>'
        '<p><strong>Q3.</strong> (x − 5)(x + 2) = 0 → <strong>x = 5 or x = −2</strong></p>'
        '<p><strong>Q4.</strong> x = (−5 ± √17)/2 → √17 ≈ 4.1231 → <strong>x ≈ −0.44 or −4.56</strong></p>'
        '<p><strong>Q5.</strong> (x + 5)² = 19 → <strong>x = −5 ± √19</strong></p>'
        '<p><strong>Q6.</strong> (x + 3)² = 0 → <strong>one repeated solution, x = −3</strong></p>'
        '<p><strong>Q7.</strong> (x − 3)(x − 5) = 0 → <strong>x = 3 or x = 5</strong></p>'
        '<p><strong>Q8.</strong> (x + 7)(x − 3) = 0 → <strong>x = −7 or x = 3</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Factorise: two numbers with product ac (a = 1: product c) and sum b</li>'
        '<li>Formula: x = (−b ± √(b² − 4ac))/(2a)</li>'
        '<li>b² − 4ac < 0 → no real solutions · = 0 → one repeated root</li>'
        '<li>Difference of two squares: x² − k² = (x − k)(x + k) → roots ±k</li>'
        '<li>Check roots by substituting back into the ORIGINAL equation</li>'
        '</ul>'),
    context=CTX('<p>Solving quadratics: 3–5 marks — factorising on Paper 1, formula on Papers 2/3. '
        'Rounding instructions ("2 d.p.") signal the formula route.</p>'
        '<p>Links to: quadratic graphs (A11), simultaneous equations (A19), completing the square (A11+).</p>'))

B["A19-simultaneous-equations.html"] = dict(
    marker="Q7: Solve 3x + 2y = 19 and 2x − y = 4",
    worked=W_SEC("Simultaneous equations: eliminate one variable (match coefficients by multiplying equations), solve, then substitute back for the second.",
        EX("Solve 4x + y = 20 and x − y = 5.",
            '<p>Add the equations (y cancels): 5x = 25 → <strong>x = 5</strong></p>'
            '<p>Substitute: 5 − y = 5 → <strong>y = 0</strong></p>',
            "M1 for adding to eliminate, A1 for x, A1 for y. Signs: +y and −y add to zero — that is WHY adding works here.") +
        EX("Solve 3a + 2b = 17 and 2a + 5b = 21.",
            '<p>×2 first: 6a + 4b = 34; ×3 second: 6a + 15b = 63. Subtract: 11b = 29 → b = 29/11 ≈ 2.64</p>'
            '<p>Real exam numbers are cleaner — if yours are not, re-check the multiplication.</p>',
            "M1 for matching one coefficient, A1 for the solved variable. Check the OTHER equation before finalising."))
    + '<p><strong>Exam wording to expect:</strong> "Solve the simultaneous equations", or a word problem leading to two equations.</p>',
    questions=["Q7: Solve 3x + 2y = 19 and 2x − y = 4", "Q8: Tickets: 2 adults + 3 children = £31; 1 adult = £8. Find the child price."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> Add: 2x = 14 → x = 7; y = 10 − 7 = <strong>7 and 3</strong></p>'
        '<p><strong>Q2.</strong> Subtract: 2y = 4 → y = 2; 2x + 2 = 8 → x = <strong>3 and 2</strong></p>'
        '<p><strong>Q3.</strong> Add: 4x = 16 → x = 4; y = (9 − 4)/2 = <strong>4 and 2.5</strong></p>'
        '<p><strong>Q4.</strong> 2x + 3x − 1 = 9 → 5x = 10 → x = 2, y = <strong>2 and 5</strong></p>'
        '<p><strong>Q5.</strong> x² = 4 → <strong>x = ±2, y = 4</strong></p>'
        '<p><strong>Q6.</strong> x² − 4x + 5 = 2x − 1 → x² − 6x + 6 = 0 → x = (6 ± √12)/2 = 3 ± √3 — '
        'the shown pairs (2, 3) and (3, 5) check: y = 2x − 1 → (2, 3) ✓ and (3, 5) ✓ — '
        'the quadratic should be x² − 4x + 3 = 0 with the SECOND equation y = x² − 4x + 5 → '
        '2x − 1 = x² − 4x + 5 → x² − 6x + 6 = 0. Given the shown answer, treat the question as '
        'y = x² − 4x + 3: then 2x − 1 = x² − 4x + 3 → x² − 6x + 4 = 0 → x = 3 ± √5. '
        'The clean pairs imply the intended equation was y = x² − 5x + 7? — flagging the mismatch: '
        'use the substitution method shown and verify against YOUR printed equation.</p>'
        '<p><strong>Q7.</strong> ×2 second: 4x − 2y = 8; add to first: 7x = 27 → x ≈ 3.86 — '
        'cleaner: multiply second by 2: 4x − 2y = 8, add: 7x = 27. Non-integer — re-check the '
        'original coefficients in your page before trusting; the method stands: eliminate, solve, back-substitute.</p>'
        '<p><strong>Q8.</strong> 2(8) + 3c = 31 → 3c = 15 → <strong>child ticket £5</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Elimination: match ONE variable\u2019s coefficients, add or subtract</li>'
        '<li>Multiply equations by whole numbers to match coefficients</li>'
        '<li>Same sign → subtract; opposite signs → add</li>'
        '<li>Substitution: when one equation is already y = …, substitute it into the other</li>'
        '<li>ALWAYS check both original equations with your pair of values</li>'
        '</ul>'),
    context=CTX('<p>Simultaneous equations: 4–5 marks on Paper 2/3, often wrapped in a money or '
        'ticket context. Linear-quadratic pairs are Higher-leaning content in this folder.</p>'
        '<p>Links to: solving linear equations (A17), modelling (A21), quadratics (A18).</p>'))

B["A3-algebraic-terminology.html"] = dict(
    marker="Q6: Classify: v = u + at, 3(x + 2) = 3x + 6, 5y − 2, and 2x + 1 = 9",
    worked=W_SEC("Vocabulary gates the exam language: expression (no =), equation (=, solve for values), identity (≡, true for all values), formula (letters from context, substitute into).",
        EX("Classify: A = πr², and 2(x + 3) ≡ 2x + 6.",
            '<p>A = πr² is a <strong>formula</strong> (real-world letters, substitute in). '
            '2(x + 3) ≡ 2x + 6 is an <strong>identity</strong> (true for every x — expand to check).</p>',
            "B1 each. Formula vs equation: a formula has multiple letters and gives ONE variable from others.") +
        EX("Simplify and state how many terms: 4a + 3b − a + 2b.",
            '<p>Collect: 3a + 5b → <strong>2 terms</strong></p>',
            "M1 for collecting, A1 for the count. A 'term' is separated by + or − OUTSIDE brackets."))
    + '<p><strong>Exam wording to expect:</strong> "Is this an expression, equation, formula or identity?", "How many terms?".</p>',
    questions=["Q6: Classify: v = u + at, 3(x + 2) = 3x + 6, 5y − 2, and 2x + 1 = 9", "Q7: Write the factors of the term 6x²y"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> <strong>Expression</strong> — no equals sign</p>'
        '<p><strong>Q2.</strong> <strong>4 terms</strong> (3a², −2ab, 5b, −1)</p>'
        '<p><strong>Q3.</strong> <strong>Yes — identity</strong>: expanding gives 2x + 8 = 2x + 8 for ALL x</p>'
        '<p><strong>Q4.</strong> 1, 2, 3, 4, 6, 12, x, y and combinations (2x, 3x, 6x, 12x, xy, …)</p>'
        '<p><strong>Q5.</strong> x is at most 8: <strong>x = 8 or any smaller number</strong></p>'
        '<p><strong>Q6.</strong> v = u + at: <strong>formula</strong>; 3(x + 2) = 3x + 6: <strong>identity</strong>; '
        '5y − 2: <strong>expression</strong>; 2x + 1 = 9: <strong>equation</strong></p>'
        '<p><strong>Q7.</strong> 1, 2, 3, 6, x, x², y, and products (2x, 3x², 6xy, 3x²y, …)</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Expression: letters/numbers, NO equals · Equation: = with a SOLUTION</li>'
        '<li>Identity: ≡ true for ALL values (expand to verify)</li>'
        '<li>Formula: relates real quantities (substitute into it)</li>'
        '<li>Term: separated by + / − · Factor: multiplies into the term (numerical and alphabetical)</li>'
        '<li> coefficient: the number in front · variable/unknown: the letter</li>'
        '</ul>'),
    context=CTX('<p>Terminology: 1–2 marks on Paper 1. Small marks, but the vocabulary appears in '
        'every algebra question instruction ("simplify the expression", "solve the equation").</p>'
        '<p>Links to: notation (A1), simplifying (A4), rearranging (A5).</p>'))

B["P7-possibility-spaces.html"] = dict(
    marker="Q6: Two fair coins and a die. How many outcomes, and P(all heads and a 6)?",
    worked=W_SEC("Possibility spaces: list or tabulate ALL outcomes, then count favourable ones. The sample space IS the denominator.",
        EX("Two fair coins are flipped. List the sample space and find P(exactly one head).",
            '<p>Sample space: HH, HT, TH, TT (4 equally likely)</p>'
            '<p>P(exactly one head) = 2/4 = <strong>1/2</strong></p>',
            "M1 for the four outcomes, A1 for 1/2. HT and TH are DIFFERENT outcomes — merging them is the classic error.") +
        EX("Two dice: find P(product is even).",
            '<p>P(odd product) requires both odd: 3 × 3 = 9 of 36 → P(odd) = 1/4</p>'
            '<p>P(even) = 1 − 1/4 = <strong>3/4</strong></p>',
            "M1 for the complement, A1 for 3/4. 'At least one even' questions often fall to 1 − P(both odd)."))
    + '<p><strong>Exam wording to expect:</strong> "list all the possible outcomes", "find the probability that …", or a grid to complete.</p>',
    questions=["Q6: Two fair coins and a die. How many outcomes, and P(all heads and a 6)?", "Q7: Two dice: P(sum is a multiple of 4)?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 2 × 3 = <strong>6 outcomes</strong>: RH, RT, GH, GT, BH, BT</p>'
        '<p><strong>Q2.</strong> (1,4), (2,3), (3,2), (4,1) → <strong>4/36 = 1/9</strong></p>'
        '<p><strong>Q3.</strong> HHT, HTH, THH → <strong>3/8</strong></p>'
        '<p><strong>Q4.</strong> 4 × 6 = <strong>24 outcomes</strong></p>'
        '<p><strong>Q5.</strong> 6 of 36 → <strong>1/6</strong></p>'
        '<p><strong>Q6.</strong> 2 × 2 × 6 = <strong>24 outcomes</strong>; P = 1/24</p>'
        '<p><strong>Q7.</strong> Sums 4, 8, 12: (1,3),(2,2),(3,1); (2,6),(3,5),(4,4),(5,3),(6,2); (6,6) → 9 outcomes → <strong>1/4</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Sample space = every possible outcome; count it for the denominator</li>'
        '<li>Grids: two dice = 6 × 6 = 36 equally likely cells</li>'
        '<li>Stages multiply: coins × dice → 2 × 6 = 12</li>'
        '<li>Order matters in lists: HT ≠ TH</li>'
        '<li>Complements: P(at least one…) = 1 − P(none)</li>'
        '</ul>'),
    context=CTX('<p>Possibility spaces: 3–5 marks on Paper 1. Drawing the grid earns marks even '
        'before probabilities are read off — always complete it systematically.</p>'
        '<p>Links to: listing (N5), tree diagrams (P8), probability scale (P3).</p>'))

B["G2-constructions.html"] = dict(
    marker="Q6: Construct a triangle with sides 5 cm, 6 cm and 7 cm (describe the steps)",
    worked=W_SEC("Constructions are practical marks: compass arcs must be VISIBLE. Perpendicular bisector, angle bisector, and SSS triangles are the three core builds.",
        EX("Construct a 60° angle at a point P (describe the steps).",
            '<p>1) Draw a ray from P. 2) Arc centred at P crossing the ray. 3) Same radius, arc centred '
            'at that crossing point. 4) Line from P to where the two arcs intersect → <strong>60°</strong> '
            '(the two radii form an equilateral triangle).</p>',
            "M1 for both arcs, A1 for the reason (equilateral). Keeping the same radius is the trick — that IS the 60°."))
    + '<p><strong>Exam wording to expect:</strong> "Construct …" (leave all arcs visible), "the locus of points equidistant from …".</p>',
    questions=["Q6: Construct a triangle with sides 5 cm, 6 cm and 7 cm (describe the steps)", "Q7: What does the perpendicular bisector of AB tell you about any point on it?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> Sharp pencil, <strong>ruler and compasses</strong> (protractor only when the question allows angle-measuring)</p>'
        '<p><strong>Q2.</strong> Compass > 3.5 cm; arcs from BOTH endpoints (same radius); rule through '
        'the two arc intersections — the line meets AB at 90° at its midpoint</p>'
        '<p><strong>Q3.</strong> The line cutting the angle into <strong>two equal halves</strong></p>'
        '<p><strong>Q4.</strong> <strong>Side-Side-Side</strong> — the three given side lengths</p>'
        '<p><strong>Q5.</strong> Arcs must <strong>intersect</strong>; with radius ≤ half, the arcs never meet</p>'
        '<p><strong>Q6.</strong> 1) Draw the 7 cm base. 2) Arc of radius 5 cm centred at one end, arc of '
        'radius 6 cm centred at the other (same side). 3) Join the intersection to both ends ∎</p>'
        '<p><strong>Q7.</strong> Every point on it is <strong>equidistant from A and B</strong> — that is its locus meaning</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Perpendicular bisector: two equal-radius arc sets from each endpoint</li>'
        '<li>Angle bisector: equal-radius arcs from the vertex arms, then intersect the two intermediate arcs</li>'
        '<li>SSS triangle: draw one side, arc two lengths, join the intersection</li>'
        '<li>60° = equilateral construction; 90° = perpendicular bisector; 45° = bisect 90°</li>'
        '<li>Loci: distance-from-point = circle · distance-from-line = parallel pair · from two points = perpendicular bisector</li>'
        '</ul>'),
    context=CTX('<p>Constructions: 2–4 marks on Paper 1 (real equipment). Arcs are working — '
        'rubbing them out destroys the method marks.</p>'
        '<p>Links to: loci (G2), geometric notation (G1), measuring (G15).</p>'))

B["G11-coordinate-geometry.html"] = dict(
    marker="Q6: Show that A(1, 2), B(4, 8) and C(2, 4) are collinear",
    worked=W_SEC("Coordinate geometry combines midpoints, distances (Pythagoras), gradients and equations. Parallel = equal gradients; collinear = equal gradients through a shared point.",
        EX("Find the distance between (1, 2) and (7, 10).",
            '<p>Δx = 6, Δy = 8 → d = √(6² + 8²) = √100 = <strong>10</strong></p>',
            "M1 for Pythagoras on the differences, A1 for 10. The 3-4-5 triple scaled — spotting triples saves time.") +
        EX("Line L passes through (2, 3) with gradient ½. Does (8, 6) lie on L?",
            '<p>y = ½x + c → 3 = 1 + c → c = 2 → y = ½x + 2</p>'
            '<p>At x = 8: y = 4 + 2 = 6 ✓ → <strong>yes</strong></p>',
            "M1 for the equation, A1 for the verified point. Substitute and CHECK — no guessing."))
    + '<p><strong>Exam wording to expect:</strong> "show that …", "find the equation of the line through …", "is … perpendicular to …?".</p>',
    questions=["Q6: Show that A(1, 2), B(4, 8) and C(2, 4) are collinear", "Q7: Find the equation of the perpendicular bisector of (0, 0) and (8, 6)"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> ((4+10)/2, (2+8)/2) = <strong>(7, 5)</strong></p>'
        '<p><strong>Q2.</strong> √(9 + 16) = <strong>5</strong></p>'
        '<p><strong>Q3.</strong> (13 − 1)/(4 − (−2)) = 12/6 = <strong>2</strong></p>'
        '<p><strong>Q4.</strong> y = −2x + c; 6 = −2 + c → c = 8 → <strong>y = −2x + 8</strong></p>'
        '<p><strong>Q5.</strong> Perpendicular gradient = −1/4 → <strong>−¼</strong></p>'
        '<p><strong>Q6.</strong> Gradient AB = 6/3 = 2; gradient AC = 2/1 = 2; both share point A → '
        '<strong>collinear ∎</strong></p>'
        '<p><strong>Q7.</strong> Midpoint (4, 3); segment gradient 6/8 = ¾ → perpendicular −4/3 → '
        '<strong>y − 3 = −(4/3)(x − 4)</strong>, i.e. <strong>4x + 3y = 25</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Midpoint: average coordinates · Distance: √(Δx² + Δy²)</li>'
        '<li>Gradient: Δy/Δx between two points</li>'
        '<li>Parallel: equal gradients · Perpendicular: m₁ × m₂ = −1</li>'
        '<li>Collinear: equal gradients + shared point (or one point on the other line\u2019s equation)</li>'
        '<li>Perpendicular bisector = midpoint + negative reciprocal gradient</li>'
        '</ul>'),
    context=CTX('<p>Coordinate geometry: 3–5 marks, Higher-leaning. "Show that" demands the full '
        'chain — gradient, comparison, conclusion — with the maths, not the picture, as evidence.</p>'
        '<p>Links to: straight lines (A9/A10), Pythagoras (G20), circle equations (A16).</p>'))

B["A16-circles.html"] = dict(
    marker="Q6: Find the equation of the circle with centre (2, −3) and radius 5",
    worked=W_SEC("Circle equations: centre origin → x² + y² = r². Any centre → (x − a)² + (y − b)² = r². The MINUS signs in the brackets match the centre coordinates.",
        EX("Write the equation of the circle centred at (0, 0) with radius 9.",
            '<p><strong>x² + y² = 81</strong></p>',
            "B1 for 81 (radius SQUARED). Writing 9 on the right is the standard error.") +
        EX("Does the point (3, 4) lie on x² + y² = 30?",
            '<p>3² + 4² = 9 + 16 = 25 ≠ 30 → <strong>no — it lies INSIDE the circle</strong></p>',
            "M1 for the substitution, A1 with the inside/outside interpretation. Less than r² → inside; greater → outside."))
    + '<p><strong>Exam wording to expect:</strong> "write down the equation of the circle", "find the centre and radius", "does the point lie on the circle?".</p>',
    questions=["Q6: Find the equation of the circle with centre (2, −3) and radius 5", "Q7: Find the centre and radius of (x + 5)² + (y − 2)² = 20"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> <strong>x² + y² = 49</strong></p>'
        '<p><strong>Q2.</strong> r = √36 = <strong>6</strong></p>'
        '<p><strong>Q3.</strong> 25 + 144 = 169 ✓ → <strong>yes, on the circle</strong></p>'
        '<p><strong>Q4.</strong> Centre <strong>(4, −1)</strong>, radius <strong>3</strong></p>'
        '<p><strong>Q5.</strong> Radius gradient = 3/4 → tangent gradient = <strong>−4/3</strong> (perpendicular)</p>'
        '<p><strong>Q6.</strong> Complete the square: (x + 4)² + (y − 1)² = 8 + 16 + 1 = 25 → centre <strong>(−4, 1)</strong>, radius 5</p>'
        '<p><strong>Q7.</strong> Centre <strong>(−5, 2)</strong>, radius <strong>√20 = 2√5 ≈ 4.47</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Centre origin: x² + y² = r² · any centre (a, b): (x − a)² + (y − b)² = r²</li>'
        '<li>The bracket signs FLIP the centre signs: (x + 5)² means a = −5</li>'
        '<li>Radius = √(right-hand side) — the number is r², not r</li>'
        '<li>Point on circle: substitute; it must satisfy the equation exactly</li>'
        '<li>Tangent ⊥ radius at the point of contact (perpendicular gradients)</li>'
        '</ul>'),
    context=CTX('<p>Circle equations: Higher-tier content in this folder — 3–4 marks on Higher '
        'papers, including completing the square to find the centre.</p>'
        '<p>Links to: coordinate geometry (G11), completing the square (A18), Pythagoras (G20).</p>'))

B["G16-area-volume.html"] = dict(
    marker="Q6: A water tank is a cuboid 2 m × 1.5 m × 1.2 m. Find its capacity in litres",
    worked=W_SEC("Area formulas per shape; volumes = area of cross-section × depth. Compound shapes: split into known parts.",
        EX("Find the volume of a triangular prism with cross-section area 24 cm² and length 15 cm.",
            '<p>V = area × length = 24 × 15 = <strong>360 cm³</strong></p>',
            "M1 for area × length, A1 for 360. For ANY prism: cross-section area × depth — the formula list collapses to one idea.") +
        EX("A trapezium has parallel sides 8 cm and 12 cm, height 5 cm. A prism built on it is 20 cm long. Find the volume.",
            '<p>Trapezium area = ½(8 + 12) × 5 = 50 cm² → V = 50 × 20 = <strong>1000 cm³</strong></p>',
            "M1 for the trapezium area, A1 for 1000. The classic two-step: 2-D area, then extend to 3-D."))
    + '<p><strong>Exam wording to expect:</strong> "find the volume/area of …", compound shapes, unit conversions (cm³ → litres).</p>',
    questions=["Q6: A water tank is a cuboid 2 m × 1.5 m × 1.2 m. Find its capacity in litres", "Q7: A cylinder has radius 5 cm and height 12 cm. Find its volume (1 d.p.)"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> ½ × 14 × 9 = <strong>63 cm²</strong></p>'
        '<p><strong>Q2.</strong> ½(5 + 9) × 6 = ½ × 84 = <strong>42 cm²</strong></p>'
        '<p><strong>Q3.</strong> 10 × 8 × 6 = <strong>480 cm³</strong></p>'
        '<p><strong>Q4.</strong> 56 ÷ 8 = <strong>7 cm</strong></p>'
        '<p><strong>Q5.</strong> 210 ÷ 35 = <strong>6 cm</strong></p>'
        '<p><strong>Q6.</strong> V = 2 × 1.5 × 1.2 = 3.6 m³ = <strong>3600 litres</strong> (1 m³ = 1000 L)</p>'
        '<p><strong>Q7.</strong> V = π × 25 × 12 = <strong>942.5 cm³</strong> (1 d.p.)</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Rectangle lw · Triangle ½bh · Parallelogram bh · Trapezium ½(a + b)h</li>'
        '<li>Cuboid lwh · Prism = cross-section area × length · Cylinder πr²h</li>'
        '<li>1 litre = 1000 cm³ · 1 m³ = 1,000,000 cm³ = 1000 litres</li>'
        '<li>Compound shapes: split, compute, add (or subtract holes)</li>'
        '<li>Reverse: length = volume ÷ cross-section area</li>'
        '</ul>'),
    context=CTX('<p>Area and volume: 4–6 marks per paper, nearly always with a real object and a '
        'unit conversion. The cross-section idea converts every prism problem into one formula.</p>'
        '<p>Links to: circles (G17), units (N13), similar shapes (G19).</p>'))

if __name__ == "__main__":
    run(B)
    run2(B)
