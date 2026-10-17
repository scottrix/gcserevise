#!/usr/bin/env python3
"""Medicine through time — pages 4-6 (H43 modern, H44 surgery, H45 public health)."""
from build_medicine_a import build, H, END, TBL, Q

H43 = (
    H('📋 Key Concepts: Modern Medicine (1900–present)', (
        '<p>After 1900 medicine accelerated: germ theory was <strong>applied</strong> (vaccines, '
        'antibiotics, "magic bullets"), the <strong>NHS (1948)</strong> universalised access, and DNA '
        '(structure 1953, Human Genome Project 2000–03) opened predictive medicine. Two world wars '
        'forced speed: blood transfusion, X-rays in the field, plastic surgery, penicillin mass-production.</p>' +
        TBL([
            ['Year','Development','Why it matters'],
            ['1900s','Blood groups (Karl Landsteiner, 1901)','Transfusion became safe (cross-matching)'],
            ['1928','Penicillin discovered (Alexander Fleming)','First antibiotic — but left unexploited until 1939–45'],
            ['1940s','Florey & Heatley mass-produce penicillin (US funding, WWII)','By D-Day, enough for all casualties'],
            ['1942','Beveridge Report; 1948 NHS (Aneurin Bevan)','Free care at the point of use'],
            ['1953','DNA structure (Watson, Crick, Franklin\u2019s X-ray work)','Molecular basis of heredity'],
            ['1978','First IVF baby (Louise Brown)','Fertility treatment era'],
            ['1990s–2000s','Keyhole surgery, MRI/CT scanning, HGP','Precision diagnosis; genetic medicine'],
            ['2020','COVID-19 vaccines in under a year','mRNA technology; global collaboration'],
        ]) + END) +

    H('📝 The British Government After 1900', (
        '<p><strong>Liberal reforms 1906–11:</strong> school meals (1906), medical inspections (1907), '
        'National Insurance (1911) — the state accepted that poverty (including illness) needed intervention, '
        'partly from Boer War recruitment failures. <strong>1948 NHS:</strong> free at the point of use, '
        'funded by taxation; the piecemeal panel system replaced. Debate ever since: cost, "health tourism", '
        'privatisation — but the principle has held for 75+ years.</p>' +
        '<p><strong>Examiner\u2019s pointer:</strong> the government factor returns in force after 1900 — '
        'wars (Boer, WWI, WWII) repeatedly exposed ill health and accelerated state action. Use that chain: '
        '<em>war → evidence → reform</em>.</p>') + END) +

    H('🧮 Worked Examples — Exam Style', (
        '<div class="example"><p><strong>"War has been the most important factor in medical progress since '
        '1900." How far do you agree? (16 + 4)</strong></p>'
        '<p>YES: WWI — blood depots (first at Cambrai, 1917), X-rays, Thomas splint (fracture deaths fell), '
        'plastic surgery (Gillies); WWII — penicillin mass-produced (US government funding), blood '
        'transfusion services (National Blood Service founded 1946 from wartime service). NO: peacetime '
        'science — DNA (1953), HGP, IVF, mRNA vaccines (2020) came from laboratory collaboration, not '
        'battlefields; the NHS came from politics, not war. JUDGEMENT: war accelerated APPLYING known '
        'science; peace-time science produced the fundamental breakthroughs — agree "partly".</p></div>'
        '<div class="example"><p><strong>Describe two features of the NHS when it opened in 1948 (4).</strong></p>'
        '<p>« It provided care free at the point of use for everyone, funded from taxation. It was built on '
        'the 1942 Beveridge Report\u2019s plan to attack the five giants, uniting hospitals, GPs and public '
        'health under one system. »</p></div>') + END) +

    H('❓ Practice Questions', (
        '<div class="practice-questions">' +
        Q(1,'Name the scientist who discovered penicillin in 1928 and the pair who mass-produced it.') +
        Q(2,'Describe two features of the NHS established in 1948.') +
        Q(3,'Give two ways WWI improved surgery and treatment.') +
        Q(4,'What did the Human Genome Project achieve, and when?') +
        Q(5,'Explain why the government created the NHS in 1948 (two reasons, 4 marks).') +
        Q(6,'"Penicillin changed medicine more than the NHS." How far do you agree? (16 + 4 marks)') +
        '</div>') + END) +

    H('✅ Answers', (
        '<ol>'
        '<li><strong>Alexander Fleming</strong> (1928, mould killing staphylococci); '
        '<strong>Howard Florey and Ernst Chain</strong> (with Norman Heatley\u2019s engineering) '
        'mass-produced it 1939–45.</li>'
        '<li>Free at the point of use, tax-funded; brought hospitals, GPs and public health into one '
        'national service (Beveridge Report 1942 backdrop).</li>'
        '<li><strong>Blood transfusion</strong> (Ramsgate depot 1917, cross-matching after Landsteiner '
        '1901) and the <strong>Thomas splint</strong> (fracture mortality from ~80% to ~20%); also X-ray '
        'units at casualty clearing stations, Gillies\u2019 plastic surgery at Sidcup.</li>'
        '<li>Sequenced all human genes (2000–03) — enabling genetic testing, targeted drugs and the '
        'understanding of inherited disease.</li>'
        '<li>Beveridge identified disease as one of the "five giants"; wartime experience of a coordinated '
        'Emergency Hospital Service proved national provision worked and was popular.</li>'
        '<li>Plan: penicillin = global lives saved (infections that killed for millennia); NHS = access for '
        'everyone (delivery). Argue: discovery vs delivery; the strongest answers note both needed the '
        'other — antibiotics without the NHS reach fewer patients; the NHS without antibiotics treats '
        'little. Commit to a weighted verdict.</li>'
        '</ol>') + END) +

    H('📌 Key Facts to Memorise', (
        '<ul>'
        '<li>Landsteiner blood groups 1901 · Fleming penicillin 1928 · Florey/Chain 1939–45</li>'
        '<li>Beveridge 1942 → NHS 5 July 1948 (Bevan)</li>'
        '<li>DNA double helix 1953 (Watson, Crick, Franklin, Wilkins) · HGP 1990–2003</li>'
        '<li>IVF: Louise Brown 1978 (Steptoe & Edwards)</li>'
        '<li>Liberal reforms: 1906 meals, 1907 inspections, 1911 National Insurance</li>'
        '<li>mRNA COVID vaccines 2020 — fastest vaccine development ever</li>'
        '</ul>') + END) +

    H('🗺️ In the Exam', (
        '<p>Modern questions reward <strong>judgement about ACCELERATION</strong>: change is fast, '
        'multi-factor and government-driven. For "greatest impact" questions, weigh scale (NHS), '
        'science (penicillin/DNA) and prevention (vaccination, smoking policy 1950s–2000s). Keep one '
        'eye on CONTINUITY: inequalities persisted (2020 COVID mortality gaps echo 1842 Chadwick) — '
        'top-band answers notice that.</p>') + END) +

    H('⚠️ Common Errors', (
        '<ul>'
        '<li><span class="wrong">Wrong: "Fleming mass-produced penicillin"</span> '
        '<span class="right">Correct: Fleming DISCOVERED it (1928); Florey, Chain and Heatley '
        'mass-produced it (1939–45, with US funding)</span></li>'
        '<li><span class="wrong">Wrong: "the NHS began in 1942"</span> '
        '<span class="right">Correct: Beveridge REPORT 1942; NHS opened 5 July 1948</span></li>'
        '<li><span class="wrong">Wrong: "Watson and Crick discovered DNA alone"</span> '
        '<span class="right">Correct: built on Rosalind Franklin\u2019s X-ray crystallography (Photo 51)</span></li>'
        '</ul>') + END) +

    H('🎯 Exam Tips', (
        '<ul>'
        '<li>Chain the 20th century: war → science → state: Boer War → Liberal reforms; WWI → '
        'transfusion/surgery; WWII → penicillin + NHS momentum</li>'
        '<li>Use scale numbers sparingly but well: NHS covers ~67 million people today</li>'
        '<li>For factor essays, "science and technology" (microscope → DNA sequencer) is the backbone '
        'factor of this period</li>'
        '</ul>') + END)
)

)
H44 = (
    H('📋 Key Concepts: The Three Problems of Surgery', (
        '<p>All surgery before 1850 faced three killers: <strong>pain</strong> (patients died of shock), '
        '<strong>infection</strong> (gangrene; "hospitalism"), and <strong>blood loss</strong>. Each was '
        'solved in sequence — and each solution created the next problem.</p>' +
        TBL([
            ['Problem','Breakthrough','Key figure(s)','Remaining limit'],
            ['Pain','Nitrous oxide (1844, Wells), ether (1846, Morton), chloroform (1847, Simpson)','Simpson popularised chloroform','Opposition; dosage deaths until John Snow\u2019s dosages (1858)'],
            ['Infection','Antiseptics (Lister, carbolic, 1867) → aseptic surgery (1900)','Lister; Halsted gloves','Needed germ theory (1861) to make sense'],
            ['Blood loss','Blood groups (Landsteiner, 1901), cross-match; storage + citrate+dextrose (WWI depots, 1917)','Landsteiner; Robertson; WWI teams','Plasma + freeze-drying (WWII) solved transport'],
        ]) +
        '<p><strong>The interlock:</strong> anaesthetics allowed LONG operations → infection deaths rose → '
        'germ theory explained why → antiseptics/asepsis attacked it → deeper surgery needed transfusion → '
        'blood science followed. Exam essays should TELL THAT STORY.</p>') + END) +

    H('📝 Opposition and Its Overcoming', (
        '<p><strong>Chloroform:</strong> religious objection ("pain in childbirth is God\u2019s curse"), '
        'fears of deaths on the table (Hannah Greener, 1848) — overcome by Queen Victoria\u2019s use (1853, '
        '"Anaesthetic Birth of Prince Leopold") and Snow\u2019s precise dosimeter work.</p>'
        '<p><strong>Lister:</strong> initially attacked (his results seemed too good; carbolic irritated '
        'skin); older surgeons called it ",Listerism" nonsense; won through data (mortality falls), '
        'his students spreading the method, and <strong>germ theory</strong> giving a reason why it worked. '
        '<strong>Blood:</strong> early transfusions killed randomly until Landsteiner explained incompatibility; '
        'WWI created the organisational breakthrough (depots, citrate storage) — again, war as accelerator.</p>') + END) +

    H('🧮 Worked Examples — Exam Style', (
        '<div class="example"><p><strong>"Germ theory was the most important development in 19th-century '
        'surgery." How far do you agree? (16 + 4)</strong></p>'
        '<p>YES: without Pasteur (1861), Lister\u2019s carbolic (1867) is a lucky trick; germ theory '
        'explains infection and leads to asepsis. NO: anaesthetics (1847) came FIRST and independently — '
        'without pain relief there is no long surgery for infection to matter; blood loss (1901+) also '
        'independent. JUDGEMENT: germ theory was the most important for SOLVING the deadliest problem '
        '(infection), but the surgical revolution needed all three — a "necessary but not sufficient" '
        'verdict scores top band.</p></div>'
        '<div class="example"><p><strong>Describe two features of surgical progress before 1875 (4).</strong></p>'
        '<p>« Chloroform (Simpson, 1847) removed pain during operations, enabling longer, more ambitious '
        'surgery. Lister applied carbolic acid spray and dressings (from 1867), cutting gangrene deaths in '
        'his Glasgow wards. »</p></div>') + END) +

    H('❓ Practice Questions', (
        '<div class="practice-questions">' +
        Q(1,'Name the anaesthetic Simpson championed in 1847 and the operation context that popularised it.') +
        Q(2,'Describe two features of Lister\u2019s antiseptic surgery.') +
        Q(3,'What did Landsteiner discover in 1901, and what did it make safe?') +
        Q(4,'Give two reasons chloroform faced opposition.') +
        Q(5,'Explain how WWI improved blood transfusion (two ways, 4 marks).') +
        Q(6,'"Surgery advanced most when science, not individual surgeons, drove change." How far do you '
           'agree? (16 + 4 marks)') +
        '</div>') + END) +

    H('✅ Answers', (
        '<ol>'
        '<li><strong>Chloroform</strong> — popularised after Queen Victoria used it at the birth of Prince '
        'Leopold (1853).</li>'
        '<li>Carbolic acid (phenol) spray + dressings in the operating theatre, based on carbolic\u2019s use '
        'on sewage; published mortality falls (e.g. from ~45% to ~15% in his wards); insisted on '
        'mechanical cleanliness ("scrubbing").</li>'
        '<li><strong>Blood groups (A, B, AB, O)</strong> — cross-matching made transfusion safe instead of '
        'a lethal lottery.</li>'
        '<li>Religious objections (pain, especially childbirth pain, seen as divinely intended); safety '
        'fears after anaesthetic deaths (Hannah Greener, 1848); some doctors mistrusted dosing.</li>'
        '<li><strong>Storage</strong>: citrate-dextrose stopped clotting → blood could be kept, not '
        'donated on the spot; <strong>organisation</strong>: Ramsgate depot (1917) and delivery to '
        'casualty clearing stations — transfusion became a SYSTEM, not an event.</li>'
        '<li>Plan: individuals (Simpson, Lister, Landsteiner) made the leaps; science (germ theory, '
        'immunology) EXPLAINED and generalised them; war industrialised delivery. Verdict: science set '
        'the direction, individuals leapt, institutions scaled — argue "science + individuals are '
        'inseparable" if you can defend it.</li>'
        '</ol>') + END) +

    H('📌 Key Facts to Memorise', (
        '<ul>'
        '<li>1844 nitrous oxide (Wells) · 1846 ether (Morton) · 1847 chloroform (Simpson)</li>'
        '<li>1853 Queen Victoria under chloroform · 1858 Snow on chloroform dosages</li>'
        '<li>1861 germ theory → 1867 Lister carbolic → 1890s gloves (Halsted) → 1900 asepsis</li>'
        '<li>1901 Landsteiner blood groups · 1917 Ramsgate blood depot (WWI)</li>'
        '<li>Three problems in order solved: pain → infection → blood loss</li>'
        '</ul>') + END) +

    H('🗺️ In the Exam', (
        '<p>Surgery questions are almost always CHRONOLOGICAL-STORY questions: the three-problem structure '
        '(pain → infection → blood loss) organises any answer. "How far" questions on individuals vs '
        'science: remember Lister BEFORE understanding (he acted on Pasteur\u2019s theory within 6 years — '
        'fast for the time) and Simpson WITHOUT theory (empirical). Use that contrast as your judgement '
        'spine. Source questions about operations: look for the absence of masks/gloves (pre-1900 asepsis) '
        'in illustrations — dating evidence.</p>') + END) +

    H('⚠️ Common Errors', (
        '<ul>'
        '<li><span class="wrong">Wrong: "Lister discovered chloroform"</span> '
        '<span class="right">Correct: Simpson (1847); Lister = carbolic antiseptic (1867)</span></li>'
        '<li><span class="wrong">Wrong: "anaesthetics came after antiseptics"</span> '
        '<span class="right">Correct: pain was solved FIRST (1840s), infection second (1860s–90s)</span></li>'
        '<li><span class="wrong">Wrong: "blood transfusion began in WWII"</span> '
        '<span class="right">Correct: WWI depots (1917); WWII added plasma and freeze-drying at scale</span></li>'
        '</ul>') + END) +

    H('🎯 Exam Tips', (
        '<ul>'
        '<li>Open surgery essays with the three problems — it frames everything and examiners reward the '
        'framework</li>'
        '<li>Pair each breakthrough with its OPPOSITION: Simpson vs religion, Lister vs sceptics, '
        'transfusion vs incompatibility</li>'
        '<li>Use the interlock sentence: "each solution created the next problem" — instant analytical '
        'depth</li>'
        '</ul>') + END)
)

H45 = (
    H('📋 Key Concepts: Public Health Through Time', (
        '<p>Public health = organised community action on health (water, sewers, housing, food, vaccines). '
        'The long arc: medieval towns did <strong>quarantine and street-cleaning by-laws</strong> (miasma '
        'logic) but no systematic provision; 1348/1665 plagues produced temporary action; industrial cities '
        'created the crisis; <strong>1842 → 1848 → 1866 → 1875 → 1948</strong> is the government story.</p>' +
        TBL([
            ['Period','Provision','Limit'],
            ['c1250–1500','By-laws on filth, quarantine (lepers), church-run care','Local, temporary, religious — no sanitation systems'],
            ['1500–1750','Same + plague orders (1665: searchers, burial rules)','Ends when the plague threat fades'],
            ['1750–1850','Cholera panics; 1842 Chadwick; 1848 Act (optional boards)','Laissez-faire; most towns ignore it'],
            ['1850–1900','Snow 1854; 1866 last cholera; 1875 Act compulsory; officers of health','Slums persist; implementation slow'],
            ['1900–1948','Liberal reforms; council housing begins; panel system','Patchy until the NHS'],
            ['1948–now','NHS; clean-air acts; vaccination programmes; smoking bans (2007); sugar tax (2018)','Persistent inequality (Chadwick\u2019s ghost)'],
        ]) + END) +

    H('📝 The Government Story in Five Steps', (
        '<p><strong>1) 1842:</strong> Chadwick\u2019s <em>Report on the Sanitary Condition of the Labouring '
        'Population</em> — filth causes disease, disease causes poverty (poor relief costs!). '
        '<strong>2) 1848:</strong> first Public Health Act — councils MAY act (only ~180 did). '
        '<strong>3) 1854:</strong> Snow\u2019s Broad Street + the Board of Health abolished the next year '
        '(opinion still miasma/laissez-faire). <strong>4) 1866:</strong> last cholera epidemic hits the '
        'water companies\u2019 customers — the political dam breaks. <strong>5) 1875:</strong> Public '
        'Health Act — clean water, sewers, inspectors, housing standards COMPULSORY everywhere. From '
        '<strong>1948</strong>, health care itself joins public health; from the 1950s, prevention shifts '
        'to lifestyle (smoking: Doll & Hill\u2019s 1950/54 studies → health warnings → 2007 indoor ban).</p>') + END) +

    H('🧮 Worked Examples — Exam Style', (
        '<div class="example"><p><strong>"The 1875 Public Health Act mattered more than any individual." '
        'How far do you agree? (16 + 4)</strong></p>'
        '<p>YES: compulsion reached millions; Snow/Pasteur proved points but laws delivered pipes. NO: '
        'without Chadwick\u2019s report (1842) there is no 1848 Act; without Snow/Pasteur/Koch, no evidence '
        'base; without cholera epidemics, no pressure. JUDGEMENT: the Act was the DELIVERY mechanism; '
        'individuals + epidemics were the engine. Best answers weigh mechanism vs engine.</p></div>'
        '<div class="example"><p><strong>Compare responses to the Black Death (1348) and the Great Plague '
        '(1665). (8 marks)</strong></p>'
        '<p>Similarities: prayer/penance, miasma-avoidance (herbs, smoke), quarantine attempts. Differences: '
        '1665 had state organisation (searchers of the dead, weekly bills of mortality, shuttering infected '
        'houses, plague doctors), plus European quarantine learning. Both periods still blamed God/planets '
        'and had no effective cure.</p></div>') + END) +

    H('❓ Practice Questions', (
        '<div class="practice-questions">' +
        Q(1,'What did Chadwick argue in his 1842 report, and what did it lead to?') +
        Q(2,'Give two differences between the 1848 and 1875 Public Health Acts.') +
        Q(3,'Describe two features of government action during the 1665 plague.') +
        Q(4,'What did Doll and Hill establish in the 1950s?') +
        Q(5,'Explain why the 1875 Act happened when it did (two reasons, 4 marks).') +
        Q(6,'"Public health improved when government stopped believing in laissez-faire." How far do you '
           'agree? (16 + 4 marks)') +
        '</div>') + END) +

    H('✅ Answers', (
        '<ol>'
        '<li>That <strong>filth caused disease and disease caused poverty</strong> (costly poor relief); '
        'it led to the <strong>1848 Public Health Act</strong> (optional boards of health).</li>'
        '<li>1848: <strong>optional</strong> (councils could adopt boards; ~180 did); 1875: '
        '<strong>compulsory</strong> everywhere — water, sewers, health officers required. (Also: 1875 '
        'came after germ theory; 1848 before.)</li>'
        '<li><strong>Searchers of the dead</strong> kept weekly bills of mortality; infected households '
        'were <strong>shut up</strong> (red cross, 40 days); (also: burial rules, cat/dog culls, public '
        'prayer days).</li>'
        '<li>The <strong>link between smoking and lung cancer</strong> (doctors\u2019 study, 1950/54) — '
        'beginning evidence-based lifestyle policy.</li>'
        '<li>The <strong>1866 cholera epidemic</strong> killed middle-class water-company customers — '
        'pressure became irresistible; <strong>Pasteur/Koch\u2019s germ theory</strong> gave the scientific '
        'case for sanitation. (Also: 1867 Reform Act — urban voters now mattered.)</li>'
        '<li>Plan: attitudes (laissez-faire) blocked action 1842–66; epidemics forced exceptions; 1867 '
        'democracy + germ theory removed the excuses. Judgement: attitude change was necessary but came '
        'FROM epidemics + evidence — argue the circular relationship and commit.</li>'
        '</ol>') + END) +

    H('📌 Key Facts to Memorise', (
        '<ul>'
        '<li>Medieval: by-laws + quarantine only; church care</li>'
        '<li>1842 Chadwick · 1848 permissive · 1854 Snow · 1866 last cholera · 1875 compulsory</li>'
        '<li>Laissez-faire = the barrier; epidemics + reports + voters = the push</li>'
        '<li>1948 NHS; 1956 Clean Air Act (smog); 2007 smoking ban; 2018 sugar tax</li>'
        '<li>Continuity: inequality in health outcomes from Chadwick (1842) to COVID (2020)</li>'
        '</ul>') + END) +

    H('🗺️ In the Exam', (
        '<p>Public health is the THEME — it can be asked about ANY period ("how far did the government "'
        'improve public health 1800–1900?" is a classic). The 5-step government story (1842→1848→1854→'
        '1866→1875) is your skeleton; flesh it with ONE detail per step. For long-period comparisons, '
        'judge by PROVIDER (who acts: church → town → state) and MECHANISM (by-law → optional → '
        'compulsory → universal service).</p>') + END) +

    H('⚠️ Common Errors', (
        '<ul>'
        '<li><span class="wrong">Wrong: "Chadwick was a doctor"</span> '
        '<span class="right">Correct: a poor-law reformer (bureaucrat) — his argument was ECONOMIC '
        '(sick workers cost money)</span></li>'
        '<li><span class="wrong">Wrong: "the 1875 Act built hospitals"</span> '
        '<span class="right">Correct: it mandated water, sewers, inspection — hospital care came with '
        'the NHS (1948)</span></li>'
        '<li><span class="wrong">Wrong: "medieval towns had no public health at all"</span> '
        '<span class="right">Correct: quarantine, by-laws and street-cleaning existed — they were '
        'local, temporary and theory-driven (miasma)</span></li>'
        '</ul>') + END) +

    H('🎯 Exam Tips', (
        '<ul>'
        '<li>Memorise the five-step government story as a chain — each step CAUSES the next</li>'
        '<li>Provider-mechanism grid (church → town → state; by-law → optional → compulsory) answers any '
        'long-period comparison</li>'
        '<li>End factor essays with the "who delivers?" question — knowledge vs delivery is the '
        'examiners\u2019 favourite tension</li>'
        '</ul>') + END)
)

)
PAGES = [
    ("H43-modern-medicine-1900-present",
     "Modern Medicine 1900–present",
     "Penicillin and the antibiotics revolution, blood transfusion, the NHS 1948, DNA and the Human Genome Project, IVF, keyhole surgery and mRNA vaccines — with the government factor after 1900.",
     H43),
    ("H44-surgery-pain-infection-blood-loss",
     "Surgery: Pain, Infection and Blood Loss",
     "The three problems of surgery solved in sequence: anaesthetics (Wells, Morton, Simpson), antiseptic and aseptic surgery (Lister), and blood transfusion (Landsteiner, WWI depots) — with opposition to each.",
     H44),
    ("H45-public-health-through-time",
     "Public Health Through Time",
     "From medieval by-laws and quarantine to Chadwick, the Public Health Acts of 1848 and 1875, the NHS and lifestyle policy — the five-step government story and the battle against laissez-faire.",
     H45),
]

if __name__ == "__main__":
    out = __import__('sys').argv[1] if len(__import__('sys').argv) > 1 else 'topics/history/aqa'
    for slug, title, desc, body in PAGES:
        html = build(slug, title, desc, body)
        open(f'{out}/{slug}.html', 'w', encoding='utf-8').write(html)
        print('wrote', f'{out}/{slug}.html', len(html), 'bytes')
