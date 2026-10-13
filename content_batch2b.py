#!/usr/bin/env python3
"""Batch 2b: A12, A23, R12, N5, A7, A17, G19, A10, R1, A24."""
from content_waves import W_SEC, EX, SOL_HEAD, KF, CTX, W2, run, run2

B = {}

B["A12-other-graphs.html"] = dict(
    marker="Q7: Sketch y = cos x for 0° ≤ x ≤ 360°. Where does it cross the x-axis?",
    worked=W_SEC("Non-linear graphs are recognised by SHAPE. Learn the five families — cubic, reciprocal, exponential, trigonometric — and 'which graph is which' becomes free marks.",
        EX("Describe the key features of the graph of y = x³.",
            '<p>Passes through the origin, S-shaped (positive cubic): flattens briefly at the '
            'origin, falls to the bottom-left, rises to the top-right.</p>',
            "B1 for S-shape through origin. Negative cubics (−x³) are reflected: top-left to bottom-right.") +
        EX("Sketch y = 2ˣ and label where it crosses the y-axis.",
            '<p>Starts near the x-axis on the left (never touches), rises increasingly steeply.</p>'
            '<p>Crosses the y-axis at (0, 1) because 2⁰ = 1 — every exponential y = aˣ passes through (0, 1).</p>',
            "M1 for increasing-curve shape with asymptote at the x-axis, A1 for (0, 1)."))
    + '<p><strong>Exam wording to expect:</strong> "Sketch", "match the equation to the graph", "write down the coordinates where the graph crosses …".</p>',
    questions=["Q7: Sketch y = cos x for 0° ≤ x ≤ 360°. Where does it cross the x-axis?", "Q8: Which is steepest near x = 0: y = 2ˣ or y = x²?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> <strong>S-shaped cubic curve</strong></p>'
        '<p><strong>Q2.</strong> y = 2/x has asymptotes <strong>x = 0 (the y-axis) and y = 0 (the x-axis)</strong> — '
        'the curve gets arbitrarily close but never touches</p>'
        '<p><strong>Q3.</strong> y = 3ˣ passes through <strong>(0, 1)</strong> since 3⁰ = 1</p>'
        '<p><strong>Q4.</strong> sin x crosses the x-axis at <strong>0°, 180°, 360°</strong>, peaking at 90° (y = 1) and bottoming at 270° (y = −1)</p>'
        '<p><strong>Q5.</strong> <strong>y = 1/x²</strong> — squaring makes both branches positive, so both sit ABOVE the x-axis in quadrants 1 and 2</p>'
        '<p><strong>Q6.</strong> Maximum of cos x is <strong>1</strong> (at x = 0° and 360°)</p>'
        '<p><strong>Q7.</strong> cos x starts at (0°, 1), falls to (180°, −1), returns to (360°, 1); '
        'crosses the x-axis at <strong>90° and 270°</strong></p>'
        '<p><strong>Q8.</strong> <strong>y = 2ˣ</strong> — exponential growth climbs faster than any polynomial near and beyond small x; at x = 0 both equal 1, but 2ˣ pulls away immediately</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Cubic (x³): S-shape through the origin; negative cubic is upside-down</li>'
        '<li>Reciprocal (k/x): two branches; asymptotes are the axes; k/x² has both branches above</li>'
        '<li>Exponential (aˣ): passes (0, 1); horizontal asymptote y = 0; grows fast for a > 1</li>'
        '<li>sin x: 0 → 1 (90°) → 0 (180°) → −1 (270°) → 0 (360°); cos x starts at 1</li>'
        '<li>Trig graphs repeat every 360°; maximum 1, minimum −1</li>'
        '</ul>'),
    context=CTX('<p>Graph recognition: 1–2 marks on Paper 2/3. Trig graphs gate the ' 
        'Higher graph-transformation questions; reciprocals gate asymptote reasoning.</p>'
        '<p>Links to: straight lines (A9), quadratic graphs (A11), transformations (A13).</p>'),
    worked2=W2("Match each equation to its graph shape: (a) y = x³ (b) y = 1/x (c) y = 3ˣ (d) y = sin x — given graphs: S-curve through origin; two branches in opposite quadrants; curve through (0, 1) rising steeply; smooth wave between −1 and 1.",
        '<p>(a) S-curve through the origin → <strong>y = x³</strong></p>'
        '<p>(b) Two branches in opposite quadrants (1 and 3 for positive k) → <strong>y = 1/x</strong></p>'
        '<p>(c) Through (0, 1), rising steeply → <strong>y = 3ˣ</strong></p>'
        '<p>(d) Wave oscillating between −1 and 1 → <strong>y = sin x</strong></p>',
        "B1 each. Elimination makes matching safe: exponential is the only one pinned at (0, 1); "
        "reciprocal is the only one with two separate branches."))

B["A23-generating-sequences.html"] = dict(
    marker="Q7: Find the first 5 terms of uₙ = 4n − 3",
    worked=W_SEC("Sequences come in two rule types: term-to-term (use the previous term) and position-to-term (the nth term — substitute n directly).",
        EX("A sequence starts at 3 with term-to-term rule 'add 7'. Write the first four terms.",
            '<p>3, 10, 17, <strong>24</strong> — keep adding 7.</p>',
            "B1 for all four. Term-to-term = repeated application; nth term = formula.") +
        EX("For uₙ = 5n − 2, find the first three terms and the 50th term.",
            '<p>n = 1: 3; n = 2: 8; n = 3: 13. 50th: 5 × 50 − 2 = <strong>248</strong></p>',
            "M1 for substituting, A1 for 248. The nth term makes the 50th term as easy as the 1st — that is its whole point."))
    + '<p><strong>Exam wording to expect:</strong> "Generate the first … terms", "Find the …th term", "Is … a term in the sequence?".</p>',
    questions=["Q7: Find the first 5 terms of uₙ = 4n − 3", "Q8: Which term of uₙ = 9n − 7 equals 101?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 2, 6, 10, 14, <strong>18</strong> (add 4 each time)</p>'
        '<p><strong>Q2.</strong> 1, 2, 4, <strong>8</strong> (double each time)</p>'
        '<p><strong>Q3.</strong> n = 1…5: <strong>2, 5, 8, 11, 14</strong></p>'
        '<p><strong>Q4.</strong> 2(15) + 5 = <strong>35</strong></p>'
        '<p><strong>Q5.</strong> 6n + 2 = 50 → 6n = 48 → <strong>n = 8</strong>, so yes — the 8th term</p>'
        '<p><strong>Q6.</strong> 7n − 4 = 66 → 7n = 70 → <strong>n = 10</strong></p>'
        '<p><strong>Q7.</strong> 1, 5, 9, 13, <strong>17</strong></p>'
        '<p><strong>Q8.</strong> 9n − 7 = 101 → 9n = 108 → <strong>n = 12</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Term-to-term: state the RULE (add 4, double, subtract 3)</li>'
        '<li>nth term: substitute n = 1, 2, 3… directly</li>'
        '<li>"Is k a term?" → solve k = un for n; only WHOLE positive n counts</li>'
        '<li>Linear sequences change by a constant amount; geometric multiply by a constant</li>'
        '<li>uₙ notation: u₅ means the 5th term — substitute n = 5</li>'
        '</ul>'),
    context=CTX('<p>Generating sequences: 2–3 marks on Paper 1. The "is k a term?" version adds '
        'an AO2 layer (solve and interpret a non-integer n as "no").</p>'
        '<p>Links to: nth term (A25), types of sequences (A24), solving equations (A17).</p>'),
    worked2=W2("A sequence has uₙ = n² − 3. Find the first four terms and state whether 46 is a term.",
        '<p>n = 1: 1 − 3 = −2; n = 2: 4 − 3 = 1; n = 3: 9 − 3 = 6; n = 4: 16 − 3 = 13</p>'
        '<p>Terms: <strong>−2, 1, 6, 13</strong></p>'
        '<p>n² − 3 = 46 → n² = 49 → n = 7 (positive root) → <strong>yes, 46 is the 7th term</strong></p>',
        "M1 for substituting, A1 for the terms, A1 for n = 7. "
        "Quadratic nth terms appear at Foundation as pattern tables — square numbers minus/plus a constant."))

B["R12-similarity-trigonometry.html"] = dict(
    marker="Q6: y is inversely proportional to x². When x = 2, y = 12. Find y when x = 6.",
    worked=W_SEC("Inverse proportion with powers follows the same recipe as R13: write the model (y = k/xⁿ), find k, then answer.",
        EX("y is inversely proportional to x. When x = 5, y = 12. Find y when x = 2.",
            '<p>y = k/x → 12 = k/5 → k = 60</p>'
            '<p>y = 60/2 = <strong>30</strong></p>',
            "M1 for k = 60, A1 for 30. Halving x doubles y — sanity-check the direction.") +
        EX("d is inversely proportional to s². When s = 2, d = 45. Find d when s = 3.",
            '<p>d = k/s² → 45 = k/4 → k = 180</p>'
            '<p>d = 180/9 = <strong>20</strong></p>',
            "M1 for k = 180, A1 for 20. Squared inverse: tripling s divides d by NINE — the exam's favourite twist."))
    + '<p><strong>Exam wording to expect:</strong> "inversely proportional to the square of …", "P ∝ 1/Q".</p>',
    questions=["Q6: y is inversely proportional to x². When x = 2, y = 12. Find y when x = 6.", "Q7: v is inversely proportional to r. When r = 8, v = 9. Find v when r = 12."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> k = xy = 4 × 15 = 60 → y = 60/10 = <strong>6</strong></p>'
        '<p><strong>Q2.</strong> P = k/Q → 5 = k/6 → <strong>k = 30</strong></p>'
        '<p><strong>Q3.</strong> Total work = 3 × 8 = 24 painter-hours → 24 ÷ 4 = <strong>6 hours</strong></p>'
        '<p><strong>Q4.</strong> k = ab² = 2² × 50 = 200 → a = 200/25 = <strong>8</strong></p>'
        '<p><strong>Q5.</strong> y = k/x → y′ = k/(2x) = (k/x)/2 = y/2 → <strong>halves ✓</strong></p>'
        '<p><strong>Q6.</strong> k = x²y = 4 × 12 = 48 → y = 48/36 = <strong>4/3</strong></p>'
        '<p><strong>Q7.</strong> k = rv = 8 × 9 = 72 → v = 72/12 = <strong>6</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Inverse: y = k/x · inverse square: y = k/x² · find k from ONE data pair</li>'
        '<li>Inverse intuition: as x grows, y SHRINKS proportionally</li>'
        '<li>x doubles → y halves; x triples → y thirds; x doubles in y = k/x² → y quarters</li>'
        '<li>k = the product x × y (for y = k/x)</li>'
        '<li>Graph of y = k/x: hyperbola, two branches, asymptotes on the axes</li>'
        '</ul>'),
    context=CTX('<p>Inverse proportion: 3–5 marks on Papers 2/3. The x² version separates '
        'grade 5 from grade 6 at Foundation/Higher boundary.</p>'
        '<p>Links to: direct proportion (R7/R10), graphs of proportion (R8), substitution (A2).</p>'))

B["N5-systematic-listing.html"] = dict(
    marker="Q6: How many ways can 4 friends arrange themselves in a row for a photo?",
    worked=W_SEC("Counting questions reward SYSTEMATIC listing (so nothing is missed or doubled) or the product rule (multiply choices at each stage).",
        EX("A menu has 4 starters and 6 mains. How many different two-course meals?",
            '<p>Product rule: 4 × 6 = <strong>24 meals</strong></p>',
            "B1 for 24. Each starter pairs with each main — that is WHY you multiply.") +
        EX("List systematically all the ways to choose 2 letters from A, B, C (order doesn't matter).",
            '<p>AB, AC, <strong>BC</strong> — fix the first letter and pair it with each later one.</p>'
            '<p>Listing AB, BA, AC, CA… would double-count: order doesn\'t matter here.</p>',
            "M1 for a systematic list, A1 for exactly 3. 'Order doesn't matter' halves the count versus arrangements."))
    + '<p><strong>Exam wording to expect:</strong> "How many different ways …", "List all the possible …", "How many combinations …".</p>',
    questions=["Q6: How many ways can 4 friends arrange themselves in a row for a photo?", "Q7: A passcode uses 2 letters (A–D, no repeats) then 1 digit (0–9). How many codes?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 2 × 6 = <strong>12 outcomes</strong></p>'
        '<p><strong>Q2.</strong> 3! = 3 × 2 × 1 = <strong>6 ways</strong></p>'
        '<p><strong>Q3.</strong> 5 × 3 × 2 = <strong>30 combinations</strong></p>'
        '<p><strong>Q4.</strong> Fix spinner 1 and vary spinner 2: (1,1), (1,2), (1,3), (2,1)… — '
        '<strong>9 outcomes</strong> (3 × 3)</p>'
        '<p><strong>Q5.</strong> 4 choices for the first digit × 3 remaining = <strong>12 numbers</strong></p>'
        '<p><strong>Q6.</strong> 4 × 3 × 2 × 1 = <strong>24 ways</strong></p>'
        '<p><strong>Q7.</strong> 4 × 3 × 10 = <strong>120 codes</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Product rule: multiply the number of choices at each independent stage</li>'
        '<li>Arrangements (order matters): n × (n−1) × … down to the slots filled</li>'
        '<li>Selections (order irrelevant): count pairs/groups once — AB and BA are the SAME</li>'
        '<li>Systematic listing: fix the first item, run through the rest, then move on</li>'
        '<li>With repetition allowed: the same number of choices at every stage</li>'
        '</ul>'),
    context=CTX('<p>Listing/counting: 1–3 marks on every paper, often as the setup for a probability '
        'question (count outcomes to get denominators).</p>'
        '<p>Links to: possibility spaces (P7), tree diagrams (P8), probability (P3).</p>'))

B["A7-functions.html"] = dict(
    marker="Q7: Given f(x) = 3x − 1 and g(x) = x², find fg(3)",
    worked=W_SEC("Function machines: f(x) is the rule. Composite fg(x) means 'g FIRST, then f' — work from the inside out.",
        EX("Given f(x) = 2x + 1, find f(−3).",
            '<p>f(−3) = 2(−3) + 1 = −6 + 1 = <strong>−5</strong></p>',
            "B1 for −5. Substitution with brackets — the (−3) gets multiplied by 2, not the 3.") +
        EX("Find the inverse of f(x) = 3x + 6.",
            '<p>Rearrange: y = 3x + 6 → x = (y − 6)/3</p>'
            '<p><strong>f⁻¹(x) = (x − 6)/3</strong></p>',
            "M1 for swapping/rearranging, A1 for (x − 6)/3. Check with a value: f(2) = 12 and f⁻¹(12) = 2 ✓"))
    + '<p><strong>Exam wording to expect:</strong> "Find f(…)", "Find the inverse function", "Find fg(…)".</p>',
    questions=["Q7: Given f(x) = 3x − 1 and g(x) = x², find fg(3)", "Q8: Find the inverse of h(x) = (x + 2)/5"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> f(5) = 20 − 3 = <strong>17</strong>; f(−2) = −8 − 3 = <strong>−11</strong></p>'
        '<p><strong>Q2.</strong> g(3) = 9 − 1 = <strong>8</strong>; g(x + 1) = (x + 1)² − 1 = x² + 2x + 1 − 1 = <strong>x² + 2x</strong></p>'
        '<p><strong>Q3.</strong> y = 2x − 7 → x = (y + 7)/2 → <strong>f⁻¹(x) = (x + 7)/2</strong></p>'
        '<p><strong>Q4.</strong> y = x/4 + 1 → x = 4(y − 1) → <strong>g⁻¹(x) = 4x − 4</strong></p>'
        '<p><strong>Q5.</strong> fg(x) = f(2x) = 2(2x) + 3 = <strong>4x + 3</strong>; '
        'gf(x) = g(x + 3) = 2(x + 3) = <strong>2x + 6</strong></p>'
        '<p><strong>Q6.</strong> fg(2) = f(3) = <strong>9</strong>; gf(2) = g(4) = <strong>5</strong> — order matters!</p>'
        '<p><strong>Q7.</strong> g(3) = 9, then f(9) = 27 − 1 = <strong>26</strong></p>'
        '<p><strong>Q8.</strong> y = (x + 2)/5 → x = 5y − 2 → <strong>h⁻¹(x) = 5x − 2</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>f(x) = the rule; f(3) = substitute 3 for x</li>'
        '<li>fg(x) = f(g(x)): g runs FIRST, f second (read right to left)</li>'
        '<li>Inverse: swap x and y, then rearrange — undoes the original</li>'
        '<li>f(f⁻¹(x)) = x — use as a check</li>'
        '<li>Two-step functions invert in reverse order: ×2 then +1 inverts as −1 then ÷2</li>'
        '</ul>'),
    context=CTX('<p>Functions: 2–4 marks. Inverses appear on Paper 1; composites on Paper 2/3. '
        'The "which order?" trap in composites is the discriminator.</p>'
        '<p>Links to: substitution (A2), rearranging (A5), solving equations (A17).</p>'))

B["A17-solving-linear-equations.html"] = dict(
    marker="Q7: Solve: 5(x − 2) = 3x + 4",
    worked=W_SEC("Solving equations = doing the same thing to both sides until x is alone. Expand brackets first; collect variables on one side.",
        EX("Solve: 4(x + 2) = 26",
            '<p>Expand: 4x + 8 = 26 → 4x = 18 → <strong>x = 4.5</strong></p>'
            '<p>(Alternative: ÷2 first: 2(x + 2) = 13 — same destination.)</p>',
            "M1 for expansion or division, A1 for 4.5. Fractional answers are fine — decimals or fractions both accepted.") +
        EX("Solve: 7 − 3x = x + 11",
            '<p>Add 3x: 7 = 4x + 11 → subtract 11: −4 = 4x → <strong>x = −1</strong></p>',
            "M1 for collecting, A1 for −1. Negative solutions are common — do not 'fix' a minus sign away."))
    + '<p><strong>Exam wording to expect:</strong> "Solve …", "Show that x = …", or an equation formed from geometry/word context.</p>',
    questions=["Q7: Solve: 5(x − 2) = 3x + 4", "Q8: Solve: (2x + 1)/3 = 5"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> x = 15 − 9 = <strong>6</strong></p>'
        '<p><strong>Q2.</strong> x = 35 ÷ 5 = <strong>7</strong></p>'
        '<p><strong>Q3.</strong> 3x = 18 → <strong>x = 6</strong></p>'
        '<p><strong>Q4.</strong> 4x − 2x = 13 − 3 → 2x = 10 → <strong>x = 5</strong></p>'
        '<p><strong>Q5.</strong> 2x + 8 = 18 → 2x = 10 → <strong>x = 5</strong></p>'
        '<p><strong>Q6.</strong> x/5 = 6 → <strong>x = 30</strong> (undo −2 first, then × 5)</p>'
        '<p><strong>Q7.</strong> 5x − 10 = 3x + 4 → 2x = 14 → <strong>x = 7</strong></p>'
        '<p><strong>Q8.</strong> 2x + 1 = 15 → 2x = 14 → <strong>x = 7</strong> (× 3 first to clear the fraction)</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Same operation to BOTH sides, in reverse BIDMAS order</li>'
        '<li>Expand brackets before collecting (or divide the whole equation first)</li>'
        '<li>Variables left, numbers right (either way works if consistent)</li>'
        '<li>Check: substitute the answer back — both sides must match</li>'
        '<li>Fractions: multiply both sides by the denominator FIRST</li>'
        '</ul>'),
    context=CTX('<p>Linear equations: 2–4 marks on every paper, plus the final step of geometry and '
        'word problems. The check-back habit converts lost accuracy marks into found ones.</p>'
        '<p>Links to: inequalities (A22), forming equations (A21), substitution (A2).</p>'))

B["G19-similar-shapes.html"] = dict(
    marker="Q6: Two similar cylinders have heights 4 cm and 10 cm. The smaller has volume 50 cm³. Find the larger volume.",
    worked=W_SEC("Similar shapes: lengths scale by k, areas by k², volumes by k³. Identify WHICH type of quantity you are scaling before touching a number.",
        EX("Two similar triangles have lengths ratio 2 : 5. The small triangle has area 8 cm². Find the large area.",
            '<p>Length k = 5/2. Area factor k² = 25/4</p>'
            '<p>Area = 8 × 25/4 = <strong>50 cm²</strong></p>',
            "M1 for k² = 25/4, A1 for 50. Squaring the FRACTION (not the decimal) keeps it exact.") +
        EX("Two similar bottles hold 500 ml and 2000 ml. The small one is 15 cm tall. Find the height of the large one.",
            '<p>Volume ratio = 500 : 2000 = 1 : 4 → length k = ∛4 ≈ 1.587</p>'
            '<p>Height = 15 × 1.587 = <strong>23.8 cm</strong> (1 d.p.)</p>',
            "M1 for cube-rooting 4, A1 for 23.8. Cube roots of awkward numbers need the calculator — this is Paper 2/3 material."))
    + '<p><strong>Exam wording to expect:</strong> "The shapes are mathematically similar", "Find the volume/area of …", or reverse (find a length from volumes).</p>',
    questions=["Q6: Two similar cylinders have heights 4 cm and 10 cm. The smaller has volume 50 cm³. Find the larger volume.", "Q7: Similar shapes have area ratio 25 : 49. Write the length ratio."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> Area ratio = k² = 4² : 7² = <strong>16 : 49</strong></p>'
        '<p><strong>Q2.</strong> k = 4 → k² = 16 → 15 × 16 = <strong>240 cm²</strong></p>'
        '<p><strong>Q3.</strong> Length ratio = ∛27 : ∛64 = <strong>3 : 4</strong></p>'
        '<p><strong>Q4.</strong> k² = 144/9 = 16 → k = <strong>4</strong></p>'
        '<p><strong>Q5.</strong> k = 0.5 → k³ = 0.125 → 40 × 0.125 = <strong>5 cm³</strong></p>'
        '<p><strong>Q6.</strong> k = 10/4 = 2.5 → volume factor = 15.625 → 50 × 15.625 = <strong>781.25 cm³</strong></p>'
        '<p><strong>Q7.</strong> Length ratio = √25 : √49 = <strong>5 : 7</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Lengths: × k · Areas: × k² · Volumes: × k³</li>'
        '<li>Going backwards: length ratio = square-root the area ratio, cube-root the volume ratio</li>'
        '<li>k > 1 enlarges; k < 1 shrinks; both preserve shape and angles</li>'
        '<li>Volume ratio (a : b) → length ratio (∛a : ∛b)</li>'
        '<li>Area ratio 1 : 16 → volume ratio 1 : 64 (square then cube the length factor 1 : 4)</li>'
        '</ul>'),
    context=CTX('<p>Similar shapes: 3–5 marks on Papers 2/3 (calculator needed for cube roots). '
        'Choosing k, k² or k³ correctly IS the whole assessment.</p>'
        '<p>Links to: proportion (R7), area and volume (G16), circles (G17).</p>'))

B["A10-gradients-intercepts.html"] = dict(
    marker="Q7: A line passes through (0, −2) and (6, 10). Write its equation",
    worked=W_SEC("Straight lines: y = mx + c. m = gradient (steepness, rise/run), c = y-intercept (where it crosses the y-axis).",
        EX("Find the gradient of the line through (1, 3) and (5, 15).",
            '<p>m = (15 − 3)/(5 − 1) = 12/4 = <strong>3</strong></p>'
            '<p>Rise over run — y-difference over x-difference, consistently ordered.</p>',
            "M1 for the difference quotient, A1 for 3. Swapping one coordinate's order flips the sign — take both differences the same way round.") +
        EX("A line has gradient 2 and passes through (3, 8). Find its equation.",
            '<p>y = 2x + c → substitute (3, 8): 8 = 6 + c → c = 2</p>'
            '<p><strong>y = 2x + 2</strong></p>',
            "M1 for substituting to find c, A1 for y = 2x + 2. Check with the other given point if there is one."))
    + '<p><strong>Exam wording to expect:</strong> "Find the gradient", "Find the equation of the line", "What does the gradient represent?".</p>',
    questions=["Q7: A line passes through (0, −2) and (6, 10). Write its equation.", "Q8: Line y = −x + 4: write the equation of a parallel line through (0, 9)."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> m = (10 − 2)/(4 − 0) = <strong>2</strong></p>'
        '<p><strong>Q2.</strong> y-intercept = <strong>(0, −8)</strong> — the constant term</p>'
        '<p><strong>Q3.</strong> 0 = 3x + 9 → x = <strong>−3</strong>, point (−3, 0)</p>'
        '<p><strong>Q4.</strong> 5 = −2(1) + c → c = 7 → <strong>(0, 7)</strong></p>'
        '<p><strong>Q5.</strong> The gradient 50 = <strong>speed (50 miles per hour)</strong>; intercept 100 = starting distance</p>'
        '<p><strong>Q6.</strong> <strong>y = 4x − 1</strong></p>'
        '<p><strong>Q7.</strong> m = (10 − (−2))/(6 − 0) = 2, c = −2 → <strong>y = 2x − 2</strong></p>'
        '<p><strong>Q8.</strong> Parallel → same gradient −1, through (0, 9) → <strong>y = −x + 9</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>y = mx + c: m = gradient, c = y-intercept</li>'
        '<li>Gradient = (y₂ − y₁)/(x₂ − x₁) — rise over run</li>'
        '<li>Parallel lines: SAME gradient; perpendicular: gradients multiply to −1</li>'
        '<li>x-intercept: set y = 0 and solve; y-intercept: set x = 0</li>'
        '<li>Context: gradient = rate per unit; intercept = starting value</li>'
        '</ul>'),
    context=CTX('<p>Straight-line graphs: 3–5 marks per paper, from plotting to equations to '
        'interpretation. Real-world gradient reading (cost, speed, filling) is the AO2 layer.</p>'
        '<p>Links to: real-life graphs (A14), coordinate geometry (G11), proportion graphs (R8).</p>'))

B["R1-compound-units.html"] = dict(
    marker="Q6: A car travels 90 km at 60 km/h, then 40 km at 20 km/h. Find the average speed for the whole journey",
    worked=W_SEC("Compound measures bundle two units: speed (km/h), density (g/cm³), pressure (N/m²). The triangle works; showing the rearrangement earns the method mark.",
        EX("A stone has mass 72 g and volume 24 cm³. Calculate its density.",
            '<p>Density = mass ÷ volume = 72 ÷ 24 = <strong>3 g/cm³</strong></p>',
            "M1 for mass ÷ volume, A1 for 3. Water is 1 g/cm³ — a useful anchor: 3 means three times denser than water.") +
        EX("Convert 54 km/h into m/s.",
            '<p>÷ 3.6: 54 ÷ 3.6 = <strong>15 m/s</strong></p>'
            '<p>Why 3.6: 1 km/h = 1000 m per 3600 s = 1/3.6 m/s.</p>',
            "M1 for ÷ 3.6, A1 for 15. Deriving 3.6 from 3600/1000 is worth remembering if the number slips your mind."))
    + '<p><strong>Exam wording to expect:</strong> "Calculate the average speed/density/pressure", "Convert … into …", "Which is better value?".</p>',
    questions=["Q6: A car travels 90 km at 60 km/h, then 40 km at 20 km/h. Find the average speed for the whole journey.", "Q7: A box weighs 120 N and rests on an area of 0.8 m². Calculate the pressure."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 240 ÷ 4 = <strong>60 km/h</strong></p>'
        '<p><strong>Q2.</strong> 450 ÷ 150 = <strong>3 g/cm³</strong></p>'
        '<p><strong>Q3.</strong> 108 ÷ 3.6 = <strong>30 m/s</strong></p>'
        '<p><strong>Q4.</strong> 800 ÷ 40 = <strong>20 N/m²</strong></p>'
        '<p><strong>Q5.</strong> £2.80 ÷ 2 = £1.40/L vs £4.35 ÷ 3 = £1.45/L → <strong>2 litres for £2.80</strong></p>'
        '<p><strong>Q6.</strong> Total 130 km; times: 1.5 h + 2 h = 3.5 h → 130 ÷ 3.5 = <strong>37.1 km/h</strong> (3 s.f.)</p>'
        '<p><strong>Q7.</strong> 120 ÷ 0.8 = <strong>150 N/m²</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Speed = distance ÷ time · Density = mass ÷ volume · Pressure = force ÷ area</li>'
        '<li>Average speed = TOTAL distance ÷ TOTAL time (never average the speeds)</li>'
        '<li>km/h ↔ m/s: ÷ or × 3.6</li>'
        '<li>Best value: price per unit — same unit on both sides before comparing</li>'
        '<li>Triangles hide the algebra; write the rearranged formula for the method mark</li>'
        '</ul>'),
    context=CTX('<p>Compound measures: 3–5 marks, Papers 2/3. The multi-leg journey '
        '(two speeds, one average) is the classic discriminator.</p>'
        '<p>Links to: units (N13/G14), graphs of journeys (A14), proportion (R7).</p>'))

B["A24-types-of-sequences.html"] = dict(
    marker="Q7: Find the next two terms of the sequence 2, 6, 12, 20, …",
    worked=W_SEC("Sequence identification: check differences first (arithmetic), then ratios (geometric), then the special sets (squares, cubes, triangular, Fibonacci).",
        EX("Identify and continue: 1, 4, 9, 16, 25, …",
            '<p>These are SQUARE numbers (1², 2², 3²…) → next: <strong>36, 49</strong></p>',
            "B1 for identification, B1 for continuation. Difference pattern (3, 5, 7, 9…) confirms it: second difference constant = 2.") +
        EX("Identify and continue: 160, 80, 40, 20, …",
            '<p>Each term is HALVED (geometric, ratio ½) → <strong>10, 5</strong></p>',
            "B1 each. Ratio check: 80/160 = 40/80 = ½ — constant ratio means geometric."))
    + '<p><strong>Exam wording to expect:</strong> "Find the next … terms", "Describe the rule", "Which term is the first above …?".</p>',
    questions=["Q7: Find the next two terms of the sequence 2, 6, 12, 20, …", "Q8: A sequence starts 3, 6, 12, 24. Write the rule and the 7th term."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> Differences constant 5 → arithmetic: <strong>5n − 1</strong></p>'
        '<p><strong>Q2.</strong> ×3 each time → geometric: <strong>2 × 3ⁿ⁻¹</strong></p>'
        '<p><strong>Q3.</strong> Triangular numbers: 1, 3, 6, 10, 15, 21, 28, <strong>36</strong></p>'
        '<p><strong>Q4.</strong> Fibonacci (add previous two): <strong>13, 21, 34</strong></p>'
        '<p><strong>Q5.</strong> Differences 3, 5, 7… → second difference 2 → <strong>n² + 1</strong></p>'
        '<p><strong>Q6.</strong> Multiplied by 0.9 each time → <strong>geometric, ratio 0.9</strong></p>'
        '<p><strong>Q7.</strong> Differences 4, 6, 8 (+2 each time); terms are n² + n → next: '
        '<strong>30, 42</strong></p>'
        '<p><strong>Q8.</strong> Doubling from 3 → rule <strong>×2</strong>; 7th term = 3 × 2⁶ = <strong>192</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Constant difference → arithmetic (linear nth term)</li>'
        '<li>Constant ratio → geometric (nth term a × rⁿ⁻¹)</li>'
        '<li>Squares 1, 4, 9, 16… · Cubes 1, 8, 27… · Triangular 1, 3, 6, 10, 15…</li>'
        '<li>Fibonacci-type: each term = sum of the previous two</li>'
        '<li>Second difference constant (2) → quadratic sequence (n² + adjustment)</li>'
        '</ul>'),
    context=CTX('<p>Sequence types: 2–4 marks on Paper 1. Special sequences (triangular, Fibonacci) '
        'are the recognition marks; geometric decay (×0.9) links to depreciation.</p>'
        '<p>Links to: nth term (A25), generating sequences (A23), growth and decay (R16).</p>'))

if __name__ == "__main__":
    run(B)
    run2(B)
