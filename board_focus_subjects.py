#!/usr/bin/env python3
"""Board-focus data: social sciences, creative, technical, languages."""

SUB = {}

SUB["mathematics"] = __import__('board_focus_sciences').MATHS
_SCI = __import__('board_focus_sciences').SCI
for _s in ("biology", "chemistry", "physics", "combined-science"):
    SUB[_s] = _SCI[_s]

SUB["history"] = __import__('board_focus_english_hum').HIST
SUB["geography"] = __import__('board_focus_english_hum').GEOG
SUB["religious-studies"] = __import__('board_focus_english_hum').RS
SUB["english-language"] = __import__('board_focus_english_hum').ENG_LANG
SUB["english-literature"] = __import__('board_focus_english_hum').ENG_LIT

SUB["french"] = __import__('board_focus_english_hum')._mfl("8652")
SUB["spanish"] = __import__('board_focus_english_hum')._mfl("8692")
SUB["german"] = __import__('board_focus_english_hum')._mfl("8662")

SUB["business"] = {
"aqa": "<p><strong>Spec 8132.</strong> Two 1h45 papers (90 marks each): Paper 1 covers business in the real world and influences on business; Paper 2 covers operations, human resources, finance and the interdependent nature of business. AQA's 9-mark and 12-mark questions demand a justified recommendation — always finish with a decision.</p>",
"edexcel": "<p><strong>Spec 1BS0.</strong> Two papers spanning Themes 1–3 (enterprise, spotting a business opportunity, business growth, making decisions). Edexcel's calculation marks (break-even, cash flow, percentages) are quick wins — show the formula line even on a calculator paper.</p>",
"ocr": "<p><strong>Spec J204.</strong> Paper 1: business activity, marketing and people. Paper 2: operations, finance and the interdependent nature of business. OCR rewards seeing the CONNECTIONS between topics — its later questions deliberately mix marketing with finance, so revise links, not islands.</p>",
"eduqas": "<p><strong>Component-based assessment.</strong> Components split business starters, growth and operations content with data-response questions. Eduqas supplies stimulus material for most questions — read the extract before the question and underline the business's situation.</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland).</strong> Units cover starting a business, growing it and the wider business environment. Check your unit list; CCEA includes local Northern Ireland business contexts in its case material.</p>",
}

SUB["economics"] = {
"aqa": "<p><strong>Spec 8136.</strong> Paper 1: How markets work (micro). Paper 2: How the economy works (macro). AQA's chains of reasoning (a change → effect → further effect → final outcome) are the assessed skill — practise writing 3-link chains, not single-step answers.</p>",
"edexcel": "<p><strong>Spec 1EC0.</strong> Paper 1 focuses on microeconomics (markets and market failure); Paper 2 on macroeconomics and international trade. Edexcel's quantitative skills (percentages, averages, index numbers) appear inside theory questions — practise recomputing figures from data tables.</p>",
"ocr": "<p><strong>OCR economics.</strong> Papers split microeconomic and macroeconomic content with structured data-response questions. OCR expects definitions up front — open every answer with the precise definition, then apply it to the data.</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland).</strong> Units split micro and macro content. Check your unit list; CCEA includes local economic examples in its data responses.</p>",
}

SUB["psychology"] = {
"aqa": "<p><strong>Spec 8182.</strong> Paper 1: Cognition and behaviour (memory, perception, development, research methods). Paper 2: Social context and behaviour (social influence, language, brain, aggression, self). AQA's research-methods marks appear in BOTH papers — the 13-mark 'design a study' question is predictable and drillable.</p>",
"edexcel": "<p><strong>Spec 1PS0.</strong> Two papers covering individual/social/cognitive/biological topics plus studies. Edexcel examines named CLASSIC STUDIES in detail — learn one classic study's aim, method, results and evaluation inside out per topic.</p>",
"ocr": "<p><strong>OCR psychology.</strong> Structured papers covering studies and applications with research-methods questions embedded. OCR rewards evaluating studies with specific criticisms (sample, method, ethics) rather than generic 'it was biased' comments.</p>",
}

SUB["sociology"] = {
"aqa": "<p><strong>Spec 8192.</strong> Paper 1: The sociology of families and education. Paper 2: Crime and deviance, social stratification and sociological approaches. AQA's item-based questions require applying the stimulus material — quote the item, then add sociological knowledge and a named sociologist.</p>",
"eduqas": "<p><strong>Component-based assessment</strong> covering families, education, crime and stratification with sociological theory. Eduqas rewards balanced 'two-sided' answers — present one perspective, challenge it, then conclude.</p>",
"ocr": "<p><strong>OCR sociology.</strong> Structured papers across socialisation, families, education and crime with research-methods questions. OCR's methods-in-context questions ask you to critique a described study — link each criticism to the METHOD described, not to the topic.</p>",
}

SUB["citizenship-studies"] = {
"aqa": "<p><strong>Spec 8100.</strong> Paper 1: active citizenship + politics and participation. Paper 2: life in modern Britain + rights and responsibilities. AQA's active-citizenship questions draw on the ACTION you (or a case study) took — learn the process vocabulary (advocacy, consultation, negotiation).</p>",
"edexcel": "<p><strong>Spec 1CS0.</strong> Two papers covering themes from living together in the UK to democracy, law and active citizenship. Edexcel includes source-based questions using media material — practise spotting viewpoint and bias in newspaper-style extracts.</p>",
"ocr": "<p><strong>Spec J270.</strong> Structured papers across citizenship identities, democracy, law and active participation. OCR rewards precise legal-process knowledge — know the stages of law-making and the roles of parliament vs judiciary.</p>",
}

SUB["latin"] = {
"aqa": "<p><strong>Untiered — all candidates sit the same papers.</strong> A language paper (translation and comprehension) plus literature papers on the set verse and prose texts. Latin grammar is the whole game: drill noun-declension endings and verb principal parts until they are automatic, because every translation question depends on them.</p>",
"edexcel": "<p><strong>Untiered.</strong> Language paper plus literature/verse papers with translation and comprehension elements. Edexcel's unseen translation rewards systematic parsing — identify the verb first, then find its subject and object before translating word-by-word.</p>",
"ocr": "<p><strong>Spec J282, untiered.</strong> Language papers plus a choice of prose or verse literature options — your centre picks the route. OCR's literature papers examine set texts closely: know the context, style and themes of your prescribed passages in detail.</p>",
}

SUB["computer-science"] = {
"aqa": "<p><strong>Spec 8525.</strong> Paper 1: Computational thinking and programming skills — an ON-SCREEN exam (2 hours) where you write and trace code. Paper 2: theory (1h45). AQA's pseudocode and trace-table technique marks are the most drillable marks in the subject — practise tracing daily.</p>",
"ocr": "<p><strong>Spec J277.</strong> Paper 1: Computer systems (1h30). Paper 2: Algorithms and programming (1h30), including SQL and logic. OCR's Paper 2 asks you to design algorithms in pseudocode OR flowcharts — pick one format and practise it consistently.</p>",
"eduqas": "<p><strong>On-screen programming exam plus theory paper.</strong> Eduqas's programming paper is completed on a computer with an IDE — practise typing working programs, not just reading them, under timed conditions.</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland)</strong> with a programming task and theory units. Check your unit list and the language your centre uses for the programming task.</p>",
}

SUB["media-studies"] = {
"aqa": "<p><strong>Spec 8572.</strong> Two written papers plus a media-production NEA (~30%) building media products for a brief. AQA examines the Close Study Products (CSPs) named in the spec — know those exact products' contexts, industries and audiences, not just the framework.</p>",
"edexcel": "<p><strong>Spec 1MS0.</strong> Two papers plus production NEA, covering media language, representation, industries and audiences. Edexcel's industry questions reward precise ownership/regulation facts — learn the conglomerates and regulators by name.</p>",
"ocr": "<p><strong>Spec J200.</strong> Papers span television, film, music, news, advertising, games and magazines with a production NEA. OCR's 'Media One/Media Two' papers mix products across forms — practise switching framework vocabulary between a music video and a newspaper front page quickly.</p>",
"eduqas": "<p><strong>Component-based assessment</strong> with set products named in the specification plus a production NEA. Eduqas examines unscheduled products too — revise the framework so you can analyse ANY product, not only the listed ones.</p>",
}

SUB["pe"] = {
"aqa": "<p><strong>Spec 8582.</strong> Two 1h15 written papers (applied anatomy, movement analysis, physical training; then sport psychology, socio-cultural influences, health and fitness) plus non-exam assessment: three practical performances and an analysis-and-evaluation task. AQA's 9-mark 'analyse' questions need a structured plan — practise the pros/cons + justification format.</p>",
"edexcel": "<p><strong>Spec 1PE0.</strong> Two written papers plus practical NEA and a personal exercise programme (PEP). Edexcel's fitness-test and training-zone calculations are quick marks — know the formulas (e.g. 220 − age) cold.</p>",
"ocr": "<p><strong>Spec J587.</strong> Two written papers plus practical performance and an evaluating-and-improving performance NEA. OCR examines applied anatomy with its own muscle/bone naming conventions — learn the OCR names, not a general list.</p>",
"eduqas": "<p><strong>Component-based assessment</strong> with theory components plus practical and a personal-fitness programme. Eduqas's socio-cultural questions reward named campaigns and organisations — learn specific examples, not categories.</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland)</strong> with theory units and practical performance assessment. Check your unit list and the practical activities your centre offers.</p>",
}

SUB["design-and-technology"] = {
"aqa": "<p><strong>Spec 8552.</strong> One written paper (2 hours) plus a design-and-make NEA (~50%) responding to a context released in June of Year 10. AQA's NEA mark scheme rewards iteration — photograph and document EVERY prototype stage, because development evidence scores as much as the final product.</p>",
"edexcel": "<p><strong>Spec 1DT0.</strong> Written paper plus NEA from an Edexcel-set context. Edexcel's exam leans on core technical principles and maths-in-DT (percentages, scale, ratios) — drill the calculations section separately.</p>",
"ocr": "<p><strong>Spec J310.</strong> Written paper plus iterative-design NEA. OCR's NEA explicitly rewards design ITERATION and user feedback loops — structure your folder around 'design → model → test → refine' cycles with dated evidence.</p>",
"eduqas": "<p><strong>Component-based assessment</strong> with a design-and-make task and examinations covering technical principles and designing. Eduqas rewards material and component knowledge in depth — learn properties by category (papers, boards, woods, metals, polymers, textiles).</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland)</strong> with a product design task and technology examinations. Check your unit list; CCEA includes local manufacturing contexts.</p>",
}

SUB["food-preparation-nutrition"] = {
"aqa": "<p><strong>Spec 8585.</strong> Written paper plus TWO NEAs: NEA1 Food investigation (a scientific food experiment report, ~15%) and NEA2 Food preparation task (a 3-hour practical, ~35%). AQA's NEA1 rewards the science — hypothesise, control variables, and link results to food science (gelatinisation, coagulation, denaturation).</p>",
"edexcel": "<p><strong>Spec 1FN0.</strong> Written paper plus food-investigation and practical NEAs. Edexcel's theory paper leans on nutrition calculations (energy from macros, Eatwell Guide proportions) — practise computing and interpreting nutrition data.</p>",
"ocr": "<p><strong>Spec J309.</strong> Written paper plus practical task and food-study NEA. OCR's food-study rewards research-then-experiment structure — show a testable question, trials, and a justified conclusion tied to food science.</p>",
"eduqas": "<p><strong>Component-based assessment</strong> with food-preparation NEA and theory components covering nutrition, food science, provenance and cooking skills. Eduqas's theory includes food SPOILAGE and preservation mechanisms — learn methods (freezing, canning, pickling) with the science behind each.</p>",
}

SUB["music"] = {
"aqa": "<p><strong>Spec 8271.</strong> Listening and appraising exam (~40%) on the Area of Study set works, plus NEA: one performance (~30%) and two compositions (~30%). AQA's dictation and melodic-transcription questions in the listening paper are unique — practise rhythmic and melodic dictation weekly.</p>",
"edexcel": "<p><strong>Spec 1MU0.</strong> Listening paper on set works across four Areas of Study, plus solo/ensemble performance and free/briefed compositions. Edexcel's set-work questions name specific bars and features — annotate your scores thoroughly.</p>",
"ocr": "<p><strong>Spec J536.</strong> Integrated portfolio or separate performance/composition NEA plus a listening exam with unfamiliar-listening questions. OCR's unfamiliar listening rewards rapid dictation and chord identification — train your ear, not just your set works.</p>",
"eduqas": "<p><strong>Component-based assessment:</strong> performing, composing, and a listening exam covering set works and unfamiliar music. Eduqas includes melodic composition to a brief — read the brief's requirements literally and tick them off one by one.</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland)</strong> with performing, composing and listening/appreciating units. Check your unit list and the set pieces for your exam year.</p>",
}

SUB["drama"] = {
"aqa": "<p><strong>Spec 8261.</strong> Written exam (set play + live theatre review) plus NEA: devising (~40%) and text-based performance (~20%). AQA's live-theatre review rewards SPECIFIC performance moments — take notes on lighting, sound and acting choices at the production you see, and quote them as 'evidence'.</p>",
"edexcel": "<p><strong>Spec 1DR0.</strong> Written paper on a set text (from the performer's/designer's perspective) and live evaluation, plus devising and performance NEAs. Edexcel's set-text questions can ask from a DESIGNER's viewpoint — learn lighting/sound/set terminology even if you perform.</p>",
"ocr": "<p><strong>Spec J316.</strong> Devising portfolio + performance, text performance, and a written paper exploring set texts and live theatre. OCR's devising portfolio rewards the PROCESS story — log rehearsals, decisions and changes with reasons.</p>",
"eduqas": "<p><strong>Component-based assessment:</strong> devising theatre, performing from a text, and interpreting theatre (written exam including a set text and live review). Eduqas's interpreting paper mixes 'as an actor' and 'as a designer' questions — prepare both lenses for your set play.</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland)</strong> with supported performance and written units. Check your unit list and set-play options.</p>",
}

SUB["art-and-design"] = {
"aqa": "<p><strong>Spec 8201–8206 by endorsement</strong> (Art & Design, Fine Art, Graphic Communication, Photography, Textiles, 3D). Portfolio (~60%) plus an externally set assignment (~40%) with preparatory work and a 10-hour supervised time. AQA's assessment objectives reward a JOURNEY: record, explore, refine, present — annotate every page.</p>",
"edexcel": "<p><strong>Spec 1AD0 family.</strong> Personal portfolio plus externally set assignment on the same broad 60/40-style split. Edexcel rewards contextual sources — reference artists, designers and photographers BY NAME and link their influence to your own experiments.</p>",
"ocr": "<p><strong>Spec J170 family.</strong> Portfolio plus externally set task. OCR's assessment grid is public — self-assess each page against the four objectives (develop, refine, record, present) before submission and fill the gaps.</p>",
"eduqas": "<p><strong>Portfolio plus externally set assignment.</strong> Eduqas rewards breadth of media exploration — show the SAME idea attempted in different materials/techniques, then justify your chosen route.</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland):</strong> a controlled-assessment portfolio and an externally set assignment. Check your endorsement and the support-studies expectations; CCEA values written annotations linked to artists.</p>",
}

SUB["statistics"] = {
"aqa": "<p><strong>Spec 8382.</strong> Two written papers (one non-calculator, one calculator in the current structure — confirm for your exam year), untiered? no — Foundation/Higher tiers exist. AQA statistics rewards the statistical-enquiry cycle: plan, collect, process, discuss — its long questions walk that cycle and award a mark per stage.</p>",
"edexcel": "<p><strong>Spec 1ST0.</strong> Two calculator papers at Foundation/Higher tiers. Edexcel's papers lean on data-handling techniques (Petersen capture-recapture, standard deviation at Higher) — learn each technique's formula AND its assumptions.</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland).</strong> Check your unit structure; CCEA includes coursework-style data-handling elements in some routes.</p>",
}

SUB["engineering"] = {
"aqa": "<p><strong>Spec 8852.</strong> Written exam plus a design-engineering NEA (~50%) from an AQA-set context. AQA's exam includes maths-for-engineering (percentages, areas, forces) — drill the applied calculations, they are free marks with practice.</p>",
"edexcel": "<p><strong>Spec 1EG0.</strong> Written paper plus NEA from an Edexcel-set brief. Edexcel rewards materials and manufacturing-process knowledge — learn processes by category (casting, forming, joining, CAD/CAM) with one worked example each.</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland)</strong> with a product-development task and technology examinations. Check your unit list for the current NEA weighting.</p>",
}

if __name__ == "__main__":
    print(len(SUB), "subjects with board-focus data")
