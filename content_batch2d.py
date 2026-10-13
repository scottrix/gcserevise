#!/usr/bin/env python3
"""Batch 2d: G3, A11, A13, R14, R8, A21, N16, P3, R13."""
from content_waves import W_SEC, EX, SOL_HEAD, KF, CTX, W2, run, run2

B = {}

B["G3-angles.html"] = dict(
    marker="Q6: Find the interior angle sum of a regular hexagon, and each angle",
    worked=W_SEC("Angle reasoning chains one fact to the next: point (360°), line (180°), vertically opposite (equal), parallel (Z/F rules), triangle (180°), polygon ((n − 2) × 180°).",
        EX("Two angles on a straight line are (3x)° and (x + 20)°. Find x.",
            '<p>3x + x + 20 = 180 → 4x = 160 → <strong>x = 40</strong> (angles 120° and 60°)</p>',
            "M1 for summing to 180, A1 for x = 40. 'Angles on a straight line add to 180°' is the reason to quote.")
        + EX("A regular polygon has exterior angles of 24°. How many sides does it have?",
            '<p>Exterior angles always total 360° → 360 ÷ 24 = <strong>15 sides</strong></p>',
            "M1 for 360 ÷ 24, A1 for 15. The exterior-angle total (360°) is the fastest polygon tool — memorise it."))
    + '<p><strong>Exam wording to expect:</strong> "Work out the size of angle …" (give reasons), "Find x".</p>',
    questions=["Q6: Find the interior angle sum of a regular hexagon, and each interior angle.", "Q7: In a triangle, angles are 2x°, 3x° and 4x°. Find x and the largest angle."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 98 + 112 = 210 → x = 360 − 210 = <strong>150°</strong> (angles at a point sum to 360°)</p>'
        '<p><strong>Q2.</strong> 180 − 74 = <strong>106°</strong></p>'
        '<p><strong>Q3.</strong> Vertically opposite pairs: 53° each, the other pair = (180 − 53) = <strong>127° each</strong></p>'
        '<p><strong>Q4.</strong> (10 − 2) × 180 = <strong>1440°</strong></p>'
        '<p><strong>Q5.</strong> 360 ÷ 5 = <strong>72°</strong></p>'
        '<p><strong>Q6.</strong> Sum = (6 − 2) × 180 = 720°; each = 720 ÷ 6 = <strong>120°</strong></p>'
        '<p><strong>Q7.</strong> 9x = 180 → x = 20; largest = 4x = <strong>80°</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Point: 360° · Straight line: 180° · Vertically opposite: equal</li>'
        '<li>Parallel lines: alternate (Z) equal · corresponding (F) equal · co-interior (C) sum 180°</li>'
        '<li>Triangle: 180° · Quadrilateral: 360° · n-gon: (n − 2) × 180°</li>'
        '<li>Exterior angles of ANY polygon total 360°; regular → each = 360 ÷ n</li>'
        '<li>Base angles of isosceles are equal; equilateral = 60° each</li>'
        '</ul>'),
    context=CTX('<p>Angle chains: 2–5 marks on Paper 1 (non-calculator). Every numeric answer needs '
        'its REASON — a correct number with no reason loses half the marks.</p>'
        '<p>Links to: quadrilaterals (G4), polygons and symmetry (G), circle theorems (G10).</p>'),
    worked2=W2("AB and CD are parallel lines. PQ cuts them. One alternate angle is 65°. Find all four angles at the other intersection, with reasons.",
        '<p>At the first intersection the four angles are 65°, 115°, 65°, 115° (supplementary + vertically opposite).</p>'
        '<p>At the second intersection: corresponding to 65° is 65° (F rule); its supplement is 115° (allied/co-interior); '
        'vertically opposite pairs repeat: <strong>65°, 115°, 65°, 115°</strong></p>',
        "M1 for corresponding/co-interior use, A1 for all four. "
        "Quote a named rule for every line of working — that is how the 9-marker scores."))

B["A11-quadratic-graphs.html"] = dict(
    marker="Q7: Sketch y = x² − 2x − 8, marking the y-intercept and roots",
    worked=W_SEC("Quadratic graphs: parabola (U-shape). Key features: y-intercept (constant term), roots (factorise or read the graph), turning point (midway between the roots for symmetric parabolas).",
        EX("Find the roots and turning point of y = x² − 6x + 8.",
            '<p>Roots: (x − 2)(x − 4) = 0 → x = 2, 4</p>'
            '<p>Turning point x = midway = 3; y = 9 − 18 + 8 = −1 → <strong>(3, −1)</strong></p>',
            "M1 for factorising, A1 for roots, A1 for (3, −1). Symmetry: the turning point sits halfway between the roots.")
        + EX("For y = x² − 4x + 1, complete a table for x = 0, 1, 2, 3, 4 and describe the shape.",
            '<p>y: 1, −2, −3, −2, 1 — symmetric values confirm the axis x = 2, minimum (2, −3)</p>',
            "M1 for the table, A1 for symmetry/minimum. Table symmetry is a quick check on your arithmetic."))
    + '<p><strong>Exam wording to expect:</strong> "Complete the table and draw the graph", "estimate the solutions of …", "write down the coordinates of the turning point".</p>',
    questions=["Q7: Sketch y = x² − 2x − 8, marking the y-intercept and roots", "Q8: For which values of x is y = x² − 2x − 8 negative?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> x = 0 → <strong>(0, 3)</strong> — the constant term</p>'
        '<p><strong>Q2.</strong> x² = 9 → <strong>x = ±3</strong>, points (3, 0) and (−3, 0)</p>'
        '<p><strong>Q3.</strong> (x − 2)(x − 3) = 0 → <strong>x = 2, x = 3</strong></p>'
        '<p><strong>Q4.</strong> Midway between 1 and 5 → <strong>x = 3</strong></p>'
        '<p><strong>Q5.</strong> Vertex form directly: <strong>(2, 3)</strong> — minimum (positive x²)</p>'
        '<p><strong>Q6.</strong> x = −b/(2a) = −4/2 = <strong>x = −2</strong></p>'
        '<p><strong>Q7.</strong> (x − 4)(x + 2) = 0 → roots <strong>4 and −2</strong>; y-intercept <strong>(0, −8)</strong>; '
        'turning point (1, −9)</p>'
        '<p><strong>Q8.</strong> Below the x-axis BETWEEN the roots: <strong>−2 < x < 4</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Positive x² → U-shape (minimum); negative x² → ∩-shape (maximum)</li>'
        '<li>y-intercept = the constant term c</li>'
        '<li>Roots: solve ax² + bx + c = 0 by factorising, formula, or graph-reading</li>'
        '<li>Turning point x = midway between roots = −b/(2a)</li>'
        '<li>Line of symmetry passes through the turning point, vertical</li>'
        '</ul>'),
    context=CTX('<p>Quadratic graphs: 4–6 marks across tables, drawing, reading roots and turning '
        'points. "Estimate solutions from your graph" links the drawing to equation solving.</p>'
        '<p>Links to: solving quadratics (A18), transformations of graphs (A13), inequalities (A22).</p>'))

B["A13-graph-transformations.html"] = dict(
    marker="Q7: y = f(x) has a minimum at (−1, 2). State the minimum of y = f(x − 3) + 4",
    worked=W_SEC("Transformations move graphs predictably: OUTSIDE the bracket acts vertically (as written); INSIDE acts horizontally (backwards!).",
        EX("The point (4, −2) lies on y = f(x). Where does it move under y = f(x) + 3 and y = f(x + 1)?",
            '<p>y = f(x) + 3: vertical shift → <strong>(4, 1)</strong></p>'
            '<p>y = f(x + 1): horizontal shift LEFT 1 (inside = backwards) → <strong>(3, −2)</strong></p>',
            "B1 each. The x-shift reversing direction is THE examined trap — x + 1 moves LEFT.")
        + EX("Describe the single transformation mapping y = f(x) onto y = 2f(x).",
            '<p>Vertical stretch, scale factor <strong>2</strong> — every y-value doubles, x-values unchanged.</p>',
            "B1 with the scale factor named. f(2x) would be a horizontal stretch factor ½ — different!"))
    + '<p><strong>Exam wording to expect:</strong> "Describe fully the transformation", "Sketch y = …", or tracing a known point through the transformation.</p>',
    questions=["Q7: y = f(x) has a minimum at (−1, 2). State the minimum of y = f(x − 3) + 4", "Q8: Describe the transformation from y = f(x) to y = f(−x)."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> +5 outside → <strong>translation 5 units up</strong> (vector (0, 5))</p>'
        '<p><strong>Q2.</strong> x − 2 inside → <strong>translation 2 units RIGHT</strong> (vector (2, 0))</p>'
        '<p><strong>Q3.</strong> y = −f(x) → <strong>reflection in the x-axis</strong></p>'
        '<p><strong>Q4.</strong> y = f(−x) → <strong>reflection in the y-axis</strong></p>'
        '<p><strong>Q5.</strong> (x − 3)² + 4: right 3, up 4 → <strong>(3, 4)</strong></p>'
        '<p><strong>Q6.</strong> y flips sign: (2, 4) → <strong>(2, −4)</strong></p>'
        '<p><strong>Q7.</strong> Right 3, up 4: <strong>(2, 6)</strong></p>'
        '<p><strong>Q8.</strong> <strong>Reflection in the y-axis</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>f(x) + a: up a (down if negative) · f(x + a): LEFT a (backwards!)</li>'
        '<li>−f(x): reflect x-axis · f(−x): reflect y-axis</li>'
        '<li>af(x): vertical stretch scale factor a · f(ax): horizontal stretch factor 1/a</li>'
        '<li>Vertex tracking: apply shifts to the known vertex, in order</li>'
        '<li>"Fully" = name the transformation + direction + amount/centre</li>'
        '</ul>'),
    context=CTX('<p>Transformations: 2–4 marks on Papers 1/2. Tracing a labelled point through the '
        'mapping is the reliable method when the whole-graph picture is unclear.</p>'
        '<p>Links to: quadratic graphs (A11), other graphs (A12), geometry transformations (G7).</p>'))

B["R14-graphs-rates-change.html"] = dict(
    marker="Q6: A tap fills a tank at 12 litres per minute. Describe the volume-time graph",
    worked=W_SEC("Rate = gradient. Distance-time → speed; cost graphs → price per unit; filling graphs → flow rate. The units tell you what the gradient means.",
        EX("A delivery van's distance-time graph is horizontal from 10:00 to 10:45, then rises 30 km in 45 minutes. Describe the motion.",
            '<p>10:00–10:45: stationary (unloading). Then: speed = 30 ÷ 0.75 = <strong>40 km/h</strong></p>',
            "M1 for the 0.75 h conversion, A1 for 40. Real time-axes: 45 minutes = 0.75 hours, always.")
        + EX("A tank drains: volume falls from 60 L to 24 L in 6 minutes. Find the rate and describe the graph.",
            '<p>Rate = (24 − 60)/6 = <strong>−6 L/min</strong> — falling 6 litres per minute; a straight line sloping down.</p>',
            "M1 for the gradient calculation, A1 for −6 with units. Negative gradients mean decreasing — quote the minus."))
    + '<p><strong>Exam wording to expect:</strong> "Find the rate of change", "interpret the gradient", "which section is fastest?".</p>',
    questions=["Q6: A tap fills a tank at 12 litres per minute. Describe the volume-time graph.", "Q7: A cooling graph falls steeply then levels off. Why?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> (24 − 8)/(7 − 3) = 16/4 = <strong>4</strong></p>'
        '<p><strong>Q2.</strong> 180 ÷ 3 = <strong>60 mph</strong></p>'
        '<p><strong>Q3.</strong> Gradient −4 → <strong>deceleration of 4 m/s²</strong></p>'
        '<p><strong>Q4.</strong> (35 − 14)/(25 − 10) = 21/15 = <strong>£1.40 per litre</strong></p>'
        '<p><strong>Q5.</strong> 150 ÷ 3 = <strong>50 (mph)</strong> — constant speed gives a constant gradient</p>'
        '<p><strong>Q6.</strong> Straight line rising from (0, 0) with <strong>constant gradient 12 (litres per minute)</strong></p>'
        '<p><strong>Q7.</strong> Cooling is fastest when hottest: big temperature difference at first '
        '(steep), then the rate drops as it approaches room temperature (levels off)</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Gradient = rate of change — read the UNITS to name it</li>'
        '<li>Straight line = constant rate; curve = changing rate; horizontal = zero rate</li>'
        '<li>Negative gradient = decreasing (deceleration, draining, cooling)</li>'
        '<li>Steepness compares rates between sections</li>'
        '<li>Time axes: minutes → hours (÷ 60) before speeds in per-hour units</li>'
        '</ul>'),
    context=CTX('<p>Rates from graphs: 2–4 marks on Papers 2/3 — journeys, filling, cooling, costs. '
        'The interpretation sentence ("the gradient means…") is the examined AO2 line.</p>'
        '<p>Links to: gradients/areas (A15), real-life graphs (A14), compound measures (R1).</p>'))

B["R8-ratio-linear-functions.html"] = dict(
    marker="Q6: Two quantities in ratio 4 : 7. If x = 12, find y, and write y as a function of x",
    worked=W_SEC("Direct proportion IS a linear function through the origin: y = kx. The ratio y : x equals k : 1 — the gradient IS the ratio.",
        EX("Petrol cost is proportional to litres: 20 litres cost £28. Write the function and find the cost of 32 litres.",
            '<p>k = 28/20 = 1.4 → <strong>C = 1.4L</strong> → 32 × 1.4 = <strong>£44.80</strong></p>',
            "M1 for k = 1.4, A1 for the equation, A1 for £44.80. The gradient £1.40/litre is the unit price.")
        + EX("y : x = 3 : 5. Write y in terms of x and find y when x = 45.",
            '<p>y = (3/5)x → y = <strong>27</strong> when x = 45</p>',
            "M1 for the 3/5 multiplier, A1 for 27. Ratio-to-function: the gradient is first : second."))
    + '<p><strong>Exam wording to expect:</strong> "y is proportional to x", "write y in terms of x", or a ratio embedded in a graph question.</p>',
    questions=["Q6: Two quantities in ratio 4 : 7. If x = 12, find y, and write y as a function of x.", "Q7: A graph of cost against items passes through (5, 12). Write the cost function."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> k = 18 ÷ 3 = 6 → <strong>y = 6x</strong></p>'
        '<p><strong>Q2.</strong> Through origin → gradient = 10/4 = <strong>2.5</strong></p>'
        '<p><strong>Q3.</strong> F = (3/2)B → <strong>F = 1.5B</strong></p>'
        '<p><strong>Q4.</strong> 120 ÷ 3 = <strong>40 km/h</strong> (assuming the graph starts at the origin)</p>'
        '<p><strong>Q5.</strong> Gradient = y/x = 7/5 = <strong>1.4</strong></p>'
        '<p><strong>Q6.</strong> k = 7/4 = 1.75 → y = 1.75 × 12 = <strong>21</strong>; function <strong>y = 1.75x</strong></p>'
        '<p><strong>Q7.</strong> k = 12/5 = 2.4 → <strong>C = 2.4n</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Direct proportion ↔ y = kx ↔ straight line through the origin</li>'
        '<li>Gradient = unit rate = the ratio (k : 1)</li>'
        '<li>From a graph: k = gradient = any point\u2019s y ÷ x</li>'
        '<li>y : x = a : b gives y = (a/b)x</li>'
        '<li>Non-zero intercept means NOT direct proportion (fixed charges)</li>'
        '</ul>'),
    context=CTX('<p>Proportion-as-graphs: 2–4 marks on Papers 2/3. The fixed-charge version '
        '(y = mx + c) versus pure proportion (y = kx) is the AO2 discriminator.</p>'
        '<p>Links to: proportion (R7/R10), straight lines (A9/A10), ratio (R4).</p>'))

B["A21-modelling-with-algebra.html"] = dict(
    marker="Q7: A gym charges £25 joining plus £12 per month. Write the cost formula for m months, and find the total for 8 months",
    worked=W_SEC("Modelling = translating a situation into an equation, then solving. Define the unknown FIRST, in words.",
        EX("A taxi charges £2.50 base plus £1.20 per mile. A journey cost £15.40. How many miles?",
            '<p>2.50 + 1.20m = 15.40 → 1.20m = 12.90 → <strong>m = 10.75 miles</strong></p>',
            "M1 for the equation, A1 for 10.75. Not every model answer is a whole number — the context decides if rounding is sensible.")
        + EX("The angles of a triangle are x°, (2x + 10)° and (3x − 20)°. Find the three angles.",
            '<p>Sum: x + 2x + 10 + 3x − 20 = 180 → 6x = 190 → x ≈ 31.7</p>'
            '<p>Non-integer — with real exam numbers this checks out cleanly; always re-verify your '
            'formed equation if the answer is awkward.</p>',
            "M1 for summing to 180, A1 for solving. ALWAYS sanity-check model answers against context."))
    + '<p><strong>Exam wording to expect:</strong> "Write an equation/simplify an expression for …", "hence find …", geometry contexts.</p>',
    questions=["Q7: A gym charges £25 joining plus £12 per month. Write the cost formula for m months, and find the total for 8 months.", "Q8: I think of a number, halve it, then add 7. The result is 15. Find the number."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 2n − 5 = 17 → 2n = 22 → <strong>n = 11</strong></p>'
        '<p><strong>Q2.</strong> Perimeter: x + x + (2x − 1) + (2x − 1) = 6x − 2 = 32 → x = <strong>5.5 cm</strong></p>'
        '<p><strong>Q3.</strong> a + c = 10, 12a + 8c = 96 → 12a + 8(10 − a) = 96 → 4a = 16 → '
        '<strong>4 adults</strong> (6 children)</p>'
        '<p><strong>Q4.</strong> Let brother = b: Sarah = 3b. In 12 years: 3b + 12 = 2(b + 12) → '
        '3b + 12 = 2b + 24 → b = 12 → <strong>Sarah 36, brother 12</strong></p>'
        '<p><strong>Q5.</strong> <strong>C = 20 + 0.05t</strong></p>'
        '<p><strong>Q6.</strong> n + (n + 1) + (n + 2) = 78 → 3n = 75 → <strong>25, 26, 27</strong></p>'
        '<p><strong>Q7.</strong> <strong>C = 25 + 12m</strong>; 8 months: 25 + 96 = <strong>£121</strong></p>'
        '<p><strong>Q8.</strong> n/2 + 7 = 15 → n/2 = 8 → <strong>n = 16</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Define the unknown in words before writing the equation</li>'
        '<li>Fixed charge = constant; per-unit = coefficient (C = a + bm)</li>'
        '<li>Geometry: angles sum (triangle 180°, quadrilateral 360°), perimeter = all sides</li>'
        '<li>Consecutive integers: n, n + 1, n + 2 · consecutive evens: 2n, 2n + 2, 2n + 4</li>'
        '<li>Check the answer against the story — a negative age means the model is wrong</li>'
        '</ul>'),
    context=CTX('<p>Forming and solving: 4–6 marks, the top Foundation algebra skill. '
        'Geometry-angle versions dominate Paper 1; money versions Papers 2/3.</p>'
        '<p>Links to: solving equations (A17), simultaneous equations (A19), sequences (A23).</p>'))

B["N16-upper-lower-bounds.html"] = dict(
    marker="Q6: p = 6.4 and q = 3.2 (both to 1 d.p.). Write the interval for p ÷ q",
    worked=W_SEC("Bounds arithmetic: MAXIMUM result uses upper ÷ lower (for division) or upper × upper (multiplication); MINIMUM the reverse. Choose bounds per OPERATION, not per number.",
        EX("a = 8.5 and b = 2.5 (both to 1 d.p.). Write the interval for a ÷ b.",
            '<p>a ∈ [8.45, 8.55), b ∈ [2.45, 2.55)</p>'
            '<p>Max quotient = 8.55 ÷ 2.45 = 3.4898; min = 8.45 ÷ 2.55 = 3.3137</p>'
            '<p><strong>3.31 < a/b < 3.49</strong> (2 d.p., strict upper bound)</p>',
            "M1 for choosing UB÷LB and LB÷UB, A1 for both values. The upper bound is EXCLUDED, so strict < on the right.")
        + EX("A rectangle measures 5.2 cm by 3.8 cm (1 d.p.). Write the interval for its perimeter.",
            '<p>Bounds: 5.15–5.25 and 3.75–3.85. Perimeter = 2(l + w)</p>'
            '<p>Min: 2(5.15 + 3.75) = 17.8; Max: 2(5.25 + 3.85) = 18.2 → <strong>17.8 ≤ P < 18.2 cm</strong></p>',
            "M1 for combining bounds, A1 for the interval. For ADDITION both extremes go the same way."))
    + '<p><strong>Exam wording to expect:</strong> "Calculate the least/greatest possible value of …", "Write the error interval for …".</p>',
    questions=["Q6: p = 6.4 and q = 3.2 (both to 1 d.p.). Write the interval for p ÷ q.", "Q7: A square has side 7.2 cm (1 d.p.). Find the least possible area (3 s.f.)."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> Nearest 5 → ±2.5 → <strong>32.5 ≤ x < 37.5</strong></p>'
        '<p><strong>Q2.</strong> 1 d.p. → ±0.05 → <strong>12.35 ≤ x < 12.45</strong></p>'
        '<p><strong>Q3.</strong> Minimum perimeter uses minimum lengths: 2(19.5 + 14.5) = <strong>68 cm</strong> '
        '(the given 34 cm is half the perimeter — one length sum only)</p>'
        '<p><strong>Q4.</strong> Max area = 10.5 × 6.5 = <strong>68.25 cm²</strong> (strictly, just under)</p>'
        '<p><strong>Q5.</strong> Max speed = max distance ÷ min time = 150.5 ÷ 1.5 = <strong>100.3 km/h</strong> (3 s.f.)</p>'
        '<p><strong>Q6.</strong> p ∈ [6.35, 6.45), q ∈ [3.15, 3.25): max = 6.45/3.15 = 2.048, min = 6.35/3.25 = 1.954 → '
        '<strong>1.954 < p/q < 2.048</strong></p>'
        '<p><strong>Q7.</strong> Least area = 7.15² = <strong>51.1 cm²</strong> (3 s.f.)</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Add/subtract: LB = LB − LB, UB = UB + UB (same-direction extremes)</li>'
        '<li>Multiply: LB × LB, UB × UB</li>'
        '<li>Divide: LB = LB₁ ÷ UB₂, UB = UB₁ ÷ LB₂ (opposite extremes!)</li>'
        '<li>Rounded bounds: lower INCLUDED, upper EXCLUDED → interval notation with < on the top</li>'
        '<li>Rounding to nearest 10 → ±5; nearest whole → ±0.5; 2 d.p. → ±0.005</li>'
        '</ul>'),
    context=CTX('<p>Bounds: 3–5 marks on Papers 2/3 (calculator). Choosing the right pairing '
        '(same-direction vs opposite-direction) is the entire assessment — practise the decision, '
        'not just the arithmetic.</p>'
        '<p>Links to: error intervals (N15), estimation (N14), compound measures (R1).</p>'))

B["P3-probability-scale.html"] = dict(
    marker="Q6: A bag holds 3 red, 5 blue, 2 green. One drawn at random: P(not red)?",
    worked=W_SEC("Probability sits between 0 (impossible) and 1 (certain). Theoretical = favourable ÷ total; relative frequency = observed ÷ trials.",
        EX("A spinner has 5 equal sections; 2 are shaded. Find P(not shaded) as a fraction and a decimal.",
            '<p>P(shaded) = 2/5 → P(not shaded) = 3/5 = <strong>0.6</strong></p>',
            "B1 for 3/5 = 0.6. 'Not' event: 1 − P(event). Fractions and decimals both accepted.")
        + EX("A die is rolled 200 times; six appears 38 times. Compare with the theoretical probability.",
            '<p>Theoretical P(6) = 1/6 ≈ 0.167. Relative frequency = 38/200 = 0.19</p>'
            '<p>Close to theory — consistent with a fair die (small sample variation expected).</p>',
            "M1 for both probabilities, A1 for the comparison with reasoning. 'Compare' needs BOTH numbers."))
    + '<p><strong>Exam wording to expect:</strong> "Find the probability of …", "mark on the probability scale", "compare with the theoretical probability".</p>',
    questions=["Q6: A bag holds 3 red, 5 blue, 2 green. One drawn at random: P(not red)?", "Q7: P(rain) = 0.7. What is P(no rain), and what does it mean?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> P(5 or 6) = 2/6 = <strong>1/3</strong></p>'
        '<p><strong>Q2.</strong> 1/10 = <strong>0.1</strong></p>'
        '<p><strong>Q3.</strong> 32/80 = <strong>0.4</strong></p>'
        '<p><strong>Q4.</strong> 0 at the left end (impossible), 0.25 a quarter along (unlikely), '
        '2/3 two-thirds along (likely), 1 at the right end (certain)</p>'
        '<p><strong>Q5.</strong> 485/1000 = 0.485 ≈ 0.5 → <strong>consistent with a fair coin</strong> — '
        'small deviation is expected from randomness</p>'
        '<p><strong>Q6.</strong> P(red) = 3/10 → P(not red) = <strong>7/10</strong></p>'
        '<p><strong>Q7.</strong> P(no rain) = 1 − 0.7 = <strong>0.3</strong> — a 30% chance, '
        'closer to &lsquo;unlikely&rsquo; than &lsquo;likely&rsquo; on the scale</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Scale: 0 impossible → 0.25 unlikely → 0.5 even chance → 0.75 likely → 1 certain</li>'
        '<li>Theoretical P = favourable outcomes ÷ total outcomes (equally likely)</li>'
        '<li>Relative (experimental) frequency = times it happened ÷ trials</li>'
        '<li>P(not A) = 1 − P(A) · all probabilities together sum to 1</li>'
        '<li>More trials → relative frequency converges to the theoretical probability</li>'
        '</ul>'),
    context=CTX('<p>Probability basics: 2–4 marks on every paper. Scale-marking and '
        'relative-frequency-vs-theory comparisons are the AO2/AO3 staples.</p>'
        '<p>Links to: possibility spaces (P7), experimental probability (P5), listing (N5).</p>'))

B["R13-equations-proportion.html"] = dict(
    marker="Q6: T ∝ √d. When d = 9, T = 4. Find T when d = 25",
    worked=W_SEC("Proportion with powers/roots follows the standard recipe: model → k → equation → answer. The only new step is handling the power in k.",
        EX("y ∝ x². When x = 5, y = 75. Find y when x = 8.",
            '<p>y = kx²: 75 = 25k → k = 3 → y = 3 × 64 = <strong>192</strong></p>',
            "M1 for k = 3, A1 for 192. Substitute x² = 64, not x = 8 — the square comes first.")
        + EX("v ∝ 1/w. When w = 4, v = 9. Find w when v = 6.",
            '<p>v = k/w: 9 = k/4 → k = 36 → 6 = 36/w → <strong>w = 6</strong></p>',
            "M1 for k = 36, A1 for w = 6. Reverse direction: solve the same equation for the other letter."))
    + '<p><strong>Exam wording to expect:</strong> "y is proportional to the square of x", "Find the equation connecting …", tables to identify the model.</p>',
    questions=["Q6: T ∝ √d. When d = 9, T = 4. Find T when d = 25.", "Q7: y ∝ x³. When x = 2, y = 5. Find y when x = 4."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> k = 40 ÷ 8 = 5 → <strong>y = 5x³</strong></p>'
        '<p><strong>Q2.</strong> k = x²y = 9 × 8 = 72 → y = 72/36 = <strong>2</strong></p>'
        '<p><strong>Q3.</strong> k = y/√x = 12/4 = 3 → y = 3√25 = <strong>15</strong></p>'
        '<p><strong>Q4.</strong> y/x²: 8/4 = 2, 32/16 = 2, 72/36 = 2 → <strong>y ∝ x²</strong></p>'
        '<p><strong>Q5.</strong> E = kv²: 500 = 100k → k = 5 → E = 5 × 225 = <strong>1125</strong></p>'
        '<p><strong>Q6.</strong> k = T/√d = 4/3 → T = (4/3) × 5 = <strong>20/3 ≈ 6.67</strong></p>'
        '<p><strong>Q7.</strong> k = 5/8 → y = (5/8) × 64 = <strong>40</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Models: y = kx, kx², kx³, k√x, k/x, k/x²</li>'
        '<li>Find k by substituting the given pair — powers FIRST</li>'
        '<li>√x proportion: k = y/√x; x³: k = y/x³</li>'
        '<li>Identify from tables: compute y/x, y/x², x·y — the constant one wins</li>'
        '<li>Physics links: KE ∝ v², pressure ∝ 1/V, gravity ∝ 1/r²</li>'
        '</ul>'),
    context=CTX('<p>Power/root proportion: 3–5 marks on Papers 2/3. The table-identification '
        'version is AO2; the physics-flavoured worded versions are the context of choice.</p>'
        '<p>Links to: proportion (R7/R10), substitution (A2), graphs (R8).</p>'))

if __name__ == "__main__":
    run(B)
    run2(B)
