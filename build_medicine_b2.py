#!/usr/bin/env python3
"""Medicine through time — pages 7-9 (H46 individuals, H47 factors, H48 Western Front)."""
from build_medicine_a import build, H, END, TBL, Q

H46 = (
    H('📋 Key Concepts: Individuals vs Institutions', (
        '<p>Examiners love the individual-versus-others debate. Learn each figure WITH their enabling '
        'context — nobody innovates in a vacuum:</p>' +
        TBL([
            ['Individual','Innovation','What made it possible'],
            ['Vesalius (1543)','Human anatomy corrected','Printing + humanist attitudes + dissection licences'],
            ['Harvey (1628)','Circulation proved','Experiment method; Royal Society channels later'],
            ['Sydenham (1670s)','Bedside classification','Galen\u2019s authority weakened'],
            ['Jenner (1796)','Vaccination','Folk cowpox belief + Royal Society publication'],
            ['Pasteur (1861)','Germ theory','French brewing problem + better microscopes'],
            ['Koch (1870s–80s)','Microbe identification','Petri dish + photographic plate + German labs'],
            ['Ehrlich (1909)','Salvarsan "magic bullet"','Koch\u2019s dye-staining research'],
            ['Fleming/Florey/Chain (1928/39–45)','Penicillin','WWII funding + US industry'],
            ['Watson/Crick/Franklin (1953)','DNA structure','X-ray crystallography + team competition'],
            ['Doll & Hill (1950/54)','Smoking–cancer link','Large-scale statistical method'],
        ]) +
        '<p>The counterweight: <strong>institutions</strong> — universities, the Royal Society, German '
        'laboratories, the NHS, pharmaceutical companies — turn individual insight into medicine. '
        '<strong>Teamwork replaced lone genius after 1900</strong> (penicillin, DNA, COVID vaccines).</p>') + END) +

    H('🧮 Worked Examples — Exam Style', (
        '<div class="example"><p><strong>"Individuals achieved more than institutions in medicine since '
        '1500." How far do you agree? (16 + 4)</strong></p>'
        '<p>YES side: Vesalius, Jenner, Pasteur, Fleming — named leaps, each against inertia. NO side: '
        'printing, the Royal Society, German labs, the NHS, the HGP — institutions created the CONDITIONS '
        'and the DELIVERY. Judgement: individuals for the leap, institutions for the landing — after 1900 '
        'the balance tips to teams. Use the tipping point as your verdict line.</p></div>'
        '<div class="example"><p><strong>Describe two features of Koch\u2019s work (4).</strong></p>'
        '<p>« Koch identified the specific bacteria causing TB (1882) and cholera (1883) using new staining '
        'and culturing techniques — the Petri dish made pure cultures possible. His methods turned germ '
        'theory into a microbe-hunting programme other scientists could copy. »</p></div>') + END) +

    H('❓ Practice Questions', (
        '<div class="practice-questions">' +
        Q(1,'Give two reasons Harvey\u2019s circulation theory was initially rejected.') +
        Q(2,'Describe two features of Pasteur\u2019s germ theory work.') +
        Q(3,'Name the first "magic bullet" and the disease it treated.') +
        Q(4,'Explain why Fleming\u2019s discovery needed Florey and Chain (two reasons, 4 marks).') +
        Q(5,'"The most important medical individual of the period c1250–present was Pasteur." How far do '
           'you agree? (16 + 4 marks)') +
        '</div>') + END) +

    H('✅ Answers', (
        '<ol>'
        '<li>Galen\u2019s authority (teachers ridiculed Harvey); the idea seemed absurd (blood returning via '
        'invisible capillaries — not visible until microscopes improved); (also: no practical benefit at '
        'first).</li>'
        '<li>Disproved <strong>spontaneous generation</strong> (swan-neck flask, 1861); linked SPECIFIC '
        'microbes to SPECIFIC diseases, then delivered vaccines (chicken cholera, anthrax, rabies 1885).</li>'
        '<li><strong>Salvarsan 606</strong> (1909, Ehrlich) — treated syphilis.</li>'
        '<li>Fleming had no chemical-engineering route to mass production and published without developing '
        'it; <strong>Florey and Chain</strong> (Oxford, then US wartime funding) converted it into a stable, '
        'mass-producible drug — science needed industry + war.</li>'
        '<li>Plan: YES — germ theory underpins vaccination, antiseptic logic, Koch, Ehrlich, modern '
        'microbiology. NO — Jenner preceded him (vaccination without germ theory); NHS/delivery matters '
        'more to lives than any single scientist. Verdict: weigh "foundational knowledge" against '
        '"lives saved now" and commit.</li>'
        '</ol>') + END) +

    H('📌 Key Facts to Memorise', (
        '<ul>'
        '<li>Pair every individual with their context factor — the pairing IS the analytical point</li>'
        '<li>After 1900: teams + institutions (Oxford penicillin team, HGP, mRNA collaborations)</li>'
        '<li>Salvarsan 1909 → prontosil 1932 (Domagk) → penicillin 1928/39–45 = the drug pipeline</li>'
        '<li>Nightingale and Garrett Anderson (1865, first woman on the UK medical register) for the '
        'women-in-medicine angle</li>'
        '</ul>') + END) +

    H('🗺️ In the Exam', (
        '<p>"Describe two features of X" questions on individuals need: (1) the innovation, (2) a specific '
        'detail (date, book, method). "How far" questions on individuals vs factors: use TWO individuals '
        'for, TWO factors against, and a judgement that names the tipping point (usually 1850–1900, when '
        'science + state began outpacing lone pioneers).</p>') + END) +

    H('⚠️ Common Errors', (
        '<ul>'
        '<li><span class="wrong">Wrong: "Jenner discovered vaccination using germ theory"</span> '
        '<span class="right">Correct: 1796 — a full 65 years BEFORE germ theory (he built on folk '
        'cowpox belief and experiment)</span></li>'
        '<li><span class="wrong">Wrong: "Pasteur and Koch worked together"</span> '
        '<span class="right">Correct: bitter Franco-German RIVALS — the rivalry sped both up</span></li>'
        '</ul>') + END) +

    H('🎯 Exam Tips', (
        '<ul>'
        '<li>Learn 5 individuals DEEPLY (Vesalius, Jenner, Pasteur, Koch, Fleming) rather than 10 thinly</li>'
        '<li>Always attach the enabling factor: "X made the leap BECAUSE Y existed"</li>'
        '<li>Women-in-medicine facts (Nightingale 1854+, Garrett Anderson 1865, women GPs after the 1877 '
        'Act loophole, WWII women doctors) are increasingly examined — keep two examples ready</li>'
        '</ul>') + END)
)

H47 = (
    H('📋 Key Concepts: The Factor Toolkit', (
        '<p>Every medicine essay is a FACTOR essay. Six factors cover the whole c1250–present sweep — learn '
        'an example for each in EACH period block:</p>' +
        TBL([
            ['Factor','Medieval/Renaissance','Industrial','Modern'],
            ['Religion','Church defends Galen; hospitals as care','Opposition to vaccination/chloroform','Fewer clashes; ethics debates (IVF, transplant)'],
            ['Individuals','Vesalius, Harvey, Paré','Jenner, Snow, Pasteur, Koch, Lister','Fleming, Florey, Crick team, Doll & Hill'],
            ['Science & technology','Printing; microscope late 1500s','Microscope + staining; steam printing','X-ray, DNA sequencing, MRI, mRNA platforms'],
            ['Attitudes','Trust in ancient texts; superstition','Laissez-faire; later faith in progress','Expectation of free care; prevention mindset'],
            ['Government','By-laws only','1848/1875 Acts','1906–11 reforms; 1948 NHS; smoking/sugar policy'],
            ['War','Hundred Years\u2019 War little effect','Crimea → Nightingale','WWI blood/X-ray; WWII penicillin; Boer War → reforms'],
        ]) +
        '<p><strong>Interplay beats listing:</strong> top answers show factors COMBINING — e.g. germ theory '
        '(science) + epidemics (pressure) + voters (government) = the 1875 Act. The mark scheme calls this '
        '"analytical understanding of the interplay".</p>') + END) +

    H('📝 Which Factor "Wins"? Patterns to Argue', (
        '<p><strong>Before 1750:</strong> religion + attitudes dominate — individuals fight uphill. '
        '<strong>1750–1900:</strong> science + individuals lead, government follows epidemics. '
        '<strong>After 1900:</strong> government + science-industry teams dominate; individuals work INSIDE '
        'institutions. That arc is your default thesis for any "most important factor" question — adapt it '
        'to the period named and defend it with the table\u2019s examples.</p>') + END) +

    H('🧮 Worked Examples — Exam Style', (
        '<div class="example"><p><strong>"Science and technology have been the most important factor in '
        'medical progress c1250–present." How far do you agree? (16 + 4)</strong></p>'
        '<p>P1 (science): germ theory 1861 → everything after; DNA 1953 → genetic medicine. '
        'P2 (technology): printing spread challenge; microscope made microbes visible; HGP platforms. '
        'P3 (counter-factor): government delivered 1875/1948 regardless of technology; attitudes blocked '
        'or enabled. P4: religion/attitudes dominated the FIRST 500 years — science only became king when '
        'institutions let it. JUDGEMENT: science is the engine SINCE 1860; before that, attitudes and '
        'religion throttled even good science — so "most important overall" is false; "most important '
        'since 1860" is true.</p></div>'
        '<div class="example"><p><strong>Explain why the role of government changed after 1866 (two '
        'reasons, 4 marks).</strong></p>'
        '<p>« The 1866 cholera epidemic finally hit middle-class consumers of water-company supplies, '
        'creating political pressure. The 1867 Reform Act enfranchised urban workers, so urban health '
        'became an electoral issue. »</p></div>') + END) +

    H('❓ Practice Questions', (
        '<div class="practice-questions">' +
        Q(1,'Name one example of WAR accelerating medicine in each of two different periods.') +
        Q(2,'Give two examples of ATTITUDES delaying medical progress.') +
        Q(3,'Which factor dominated 1250–1500, and why?') +
        Q(4,'Explain why "science and technology" became dominant after 1860 (two reasons, 4 marks).') +
        Q(5,'"Religion did more harm than good to medicine c1250–present." How far do you agree? '
           '(16 + 4 marks)') +
        '</div>') + END) +

    H('✅ Answers', (
        '<ol>'
        '<li><strong>Crimea (1853–56)</strong> → Nightingale\u2019s sanitation revolution; '
        '<strong>WWI (1914–18)</strong> → blood depots, X-rays, Thomas splint. (Also: WWII → penicillin; '
        'Boer War → 1906–11 reforms.)</li>'
        '<li><strong>Laissez-faire</strong> blocked the 1848 Act\u2019s enforcement; <strong>religious '
        'objection</strong> delayed chloroform and Jenner; (also: trust in Galen delaying dissection).</li>'
        '<li><strong>Religion</strong> — the Church controlled universities, preserved Galen and shaped '
        'hospitals; alternative voices lacked platforms (no printing).</li>'
        '<li><strong>Germ theory (1861)</strong> gave science authority over tradition; '
        '<strong>new instruments</strong> (staining, Petri dishes, X-rays) produced results sceptics could '
        'see — technology made science provable.</li>'
        '<li>Plan: HARM — Galen preserved and enforced; dissection discouraged; vaccination/chloroform '
        'opposed. GOOD — hospitals founded and run; learning preserved; religious charity built care '
        'networks. Verdict: harm to PROGRESS, good to CARE — split the question.</li>'
        '</ol>') + END) +

    H('📌 Key Facts to Memorise', (
        '<ul>'
        '<li>Six factors with 1 example per period block (18 pairs total — build the grid as revision)</li>'
        '<li>The arc: religion/attitudes → individuals+science → government+teams</li>'
        '<li>Interplay sentences beat factor lists: "X created the knowledge, Y created the pressure, '
        'Z delivered it"</li>'
        '</ul>') + END) +

    H('🗺️ In the Exam', (
        '<p>Any 16-marker is a factor question in disguise. Recipe: P1+P2 = the two STRONGEST factors for '
        'the named change; P3 = the strongest COUNTER-factor; P4 = judgement that ranks and explains WHY '
        'that factor dominated THAT period. Quote one exact fact per factor — no factor without evidence.</p>') + END) +

    H('🎯 Exam Tips', (
        '<ul>'
        '<li>Build the 6×3 factor grid as one revision sheet — it IS the whole thematic paper</li>'
        '<li>In judgements, name the PERIOD limit: a factor can be "most important then, not overall"</li>'
        '<li>Underused factors (attitudes, war) differentiate grade 8 from grade 6 — deploy them</li>'
        '</ul>') + END)
)

H48 = (
    H('📋 Key Concepts: The Western Front (Edexcel historic environment)', (
        '<p>Edexcel\u2019s Paper 1 historic environment is <strong>British medicine on the Western Front, '
        '1914–18</strong>: how the trench system shaped injuries and treatment. You need the SYSTEM '
        '(chain of evacuation), the INJURIES (new weapons), and the TREATMENTS (blood, infection, X-ray, '
        'brain surgery) — plus SOURCES from the trenches.</p>' +
        TBL([
            ['Stage','What / where','Significance'],
            ['Regimental Aid Post (RAP)','~100m behind the front; basic first aid','Immediate triage; little treatment possible'],
            ['Field Ambulance / Dressing Station','Advanced (ADS) and Main (MDS)','Wound stabilisation; 16 stretcher-bearers per wounded man'],
            ['Casualty Clearing Station (CCS)','~15km back, near rail; surgery','Life-saving operations within the "golden window"'],
            ['Base Hospital','Rail hubs; long-term treatment','Roles of CCS/base blurred as the war went on'],
        ]) +
        '<p><strong>New injuries:</strong> shell fragments carrying infection (gas gangrene), shrapnel '
        'wounds, head injuries, chlorine/mustard gas (1915/1917), <strong>trench fever</strong> (lice) and '
        '<strong>trench foot</strong> (wet conditions — countered by whale-oil rubs and drying rotas).</p>') + END) +

    H('📝 Treatments Born in the Trenches', (
        '<p><strong>Blood transfusion:</strong> cross-matching (Landsteiner 1901) applied; citrate-dextrose '
        'storage; <strong>Geoffrey Keynes</strong>\u2019 portable kits; the first blood depot at the Battle '
        'of Cambrai (1917). <strong>X-rays</strong>: mobile units at CCSs (Marie Curie\u2019s "petites '
        'Curies") locating shrapnel before surgery. <strong>Brain surgery</strong>: Harvey Cushing\u2019s '
        'techniques for head wounds. <strong>Infection:</strong> the Thomas splint (femur fracture mortality '
        '~80% → ~20%); Carrel-Dakin irrigation; amputation as a last resort. '
        '<strong>Plastic surgery:</strong> Harold Gillies\u2019 Sidcup hospital (facial reconstruction).</p>'
        '<p><strong>Context anchors:</strong> the Somme (1916) — 57,000 British casualties on day one '
        'overwhelming the evacuation chain; Arras and Passchendaele (1917) testing it further.</p>') + END) +

    H('🧮 Worked Examples — Exam Style', (
        '<div class="example"><p><strong>"New weapons were the main reason the chain of evacuation '
        'developed." How far do you agree? (16 + 4 — Edexcel style)</strong></p>'
        '<p>YES: artillery caused ~60% of casualties — mass shrapnel wounds demanded organised depth '
        '(RAP → ADS/MDS → CCS → Base); gas created new treatment needs. NO: distance and immobility of '
        'trench warfare made evacuation inherently hard; rail networks dictated CCS placement; medical '
        'invention (splints, depots) responded to the SYSTEM as much as to weapons. JUDGEMENT: weapons set '
        'the INJURY profile; geography and organisation shaped the chain — weigh both.</p></div>'
        '<div class="example"><p><strong>Source utility: "How useful is a soldier\u2019s letter describing '
        'stretcher-bearer delays at the Somme?" (8 marks)</strong></p>'
        '<p>Useful: first-hand detail of delays and wounds. Not enough alone: one man\u2019s sector/day may '
        'not represent the whole front; letters passed censors; compare with official records (war diaries, '
        'bills of mortality) for scale. Utility = content + purpose + MISSING context.</p></div>') + END) +

    H('❓ Practice Questions', (
        '<div class="practice-questions">' +
        Q(1,'Name the four stages of the chain of evacuation in order.') +
        Q(2,'Describe two features of the RAMC\u2019s work at CCSs.') +
        Q(3,'What was the Thomas splint, and what did it change?') +
        Q(4,'Give two features of blood transfusion on the Western Front.') +
        Q(5,'Explain why gas gangrene was such a problem (two reasons, 4 marks).') +
        Q(6,'"The system of care mattered more than medical breakthroughs on the Western Front." How far '
           'do you agree? (16 + 4 marks)') +
        '</div>') + END) +

    H('✅ Answers', (
        '<ol>'
        '<li><strong>Regimental Aid Post → Field Ambulance (ADS/MDS) → Casualty Clearing Station → '
        'Base Hospital</strong>.</li>'
        '<li>Surgery near the front (reducing the delay that killed); motor ambulances and rail links '
        'moving men by triage priority; specialist teams (brain, plastic) by 1917.</li>'
        '<li>A wire splint immobilising the leg WITH traction; femur fracture deaths fell from ~80% to '
        '~20% before men even reached CCSs.</li>'
        '<li>Citrate-dextrose storage allowed pre-stocked blood; <strong>Keynes\u2019 portable transfusion '
        'kits</strong>; the <strong>Cambrai blood depot (1917)</strong> — blood delivered to surgeons '
        'rather than donors to patients.</li>'
        '<li><strong>Shell fragments forced soil and clothing deep into wounds</strong> — anaerobic '
        'bacteria thrived in oxygen-poor tissue; wet, crowded trench conditions and delay before surgery '
        'let infection establish; no antibiotics existed until 1939–45.</li>'
        '<li>Plan: the SYSTEM (triage, CCSs, depots) applied known medicine at scale — deaths fell through '
        'organisation; BREAKTHROUGHS (splint, transfusion practice, Cushing\u2019s surgery) were often '
        'born of the system\u2019s pressure. Verdict: the system delivered; the breakthroughs equipped '
        'it — argue they co-evolved and commit.</li>'
        '</ol>') + END) +

    H('📌 Key Facts to Memorise', (
        '<ul>'
        '<li>Chain: RAP → ADS/MDS → CCS → Base (know distances and roles)</li>'
        '<li>Artillery ≈ 60% of casualties; gas 1915/1917; trench foot/fever causes + counters</li>'
        '<li>Thomas splint (femur deaths 80→20%); Carrel-Dakin irrigation; Keynes kits; Cambrai depot 1917</li>'
        '<li>Gillies Sidcup (facial surgery); Cushing (brain); Curie mobile X-rays</li>'
        '<li>Somme day one 1916: 57,000 casualties — the system under maximum test</li>'
        '</ul>') + END) +

    H('🗺️ In the Exam', (
        '<p>Edexcel asks TWO Western Front questions on Paper 1 (typically "describe two features" and a '
        'source-utility "how useful"). Learn the chain as a DIAGRAM, three treatments with NAMES (Keynes, '
        'Cushing, Gillies), and practise utility questions: content + context + judgement about what the '
        'source cannot show. The historic environment section is the easiest marks on the paper — pure '
        'recall.</p>') + END) +

    H('⚠️ Common Errors', (
        '<ul>'
        '<li><span class="wrong">Wrong: "penicillin treated Western Front wounds"</span> '
        '<span class="right">Correct: antibiotics came in WWII — Western Front infection was fought with '
        'irrigation, splints, amputation and antisepsis</span></li>'
        '<li><span class="wrong">Wrong: "CCSs were at the front line"</span> '
        '<span class="right">Correct: ~15km back near railways — out of shell range but close enough for '
        'surgery within the golden window</span></li>'
        '<li><span class="wrong">Wrong: "trench foot came from standing in cold water alone"</span> '
        '<span class="right">Correct: wet + cold + tight boots; prevention = whale oil, dry socks, '
        'rotas — and officers faced courts of inquiry over it</span></li>'
        '</ul>') + END) +

    H('🎯 Exam Tips', (
        '<ul>'
        '<li>Draw the evacuation chain from memory before every mock — it anchors all other facts</li>'
        '<li>Attach a PERSON to each treatment (Keynes = blood, Cushing = brain, Gillies = plastic, '
        'Curie = X-ray) — named evidence lifts utility answers</li>'
        '<li>For source questions, always state TWO things the source cannot tell you</li>'
        '</ul>') + END)
)

PAGES = [
    ("H46-key-individuals-medicine-through-time",
     "Key Individuals in Medicine Through Time",
     "Vesalius to Fleming: the individuals, the institutions that enabled them, and the individuals-versus-institutions debate — with pairing techniques for factor essays.",
     H46),
    ("H47-factors-in-medical-progress",
     "Factors in Medical Progress",
     "The six-factor toolkit (religion, individuals, science and technology, attitudes, government, war) across every period — with interplay techniques for 16-mark thematic essays.",
     H47),
    ("H48-western-front-medicine-wwi",
     "Medicine on the Western Front, 1914–18",
     "The chain of evacuation, new weapon injuries, and trench-born treatments (blood depots, Thomas splint, X-rays, plastic surgery) — Edexcel's historic environment with source-utility technique.",
     H48),
]

if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else 'topics/history/aqa'
    for slug, title, desc, body in PAGES:
        html = build(slug, title, desc, body)
        open(f'{out}/{slug}.html', 'w', encoding='utf-8').write(html)
        print('wrote', f'{out}/{slug}.html', len(html), 'bytes')
