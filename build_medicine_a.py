#!/usr/bin/env python3
"""Medicine through time — history option set, pages 1-3 (H40-H42).
Clones the history topic template; strips the cloned Board Focus (per-board boxes
are re-injected afterwards). Published to aqa/edexcel/ocr/eduqas."""
import re
import sys

TPL = 'topics/history/aqa/H1-kaiser-wilhelm-germany.html'
H = lambda t, b: (f'<section class="section">\n<h2>{t}</h2>\n' + b + ('\n</section>' if not b.rstrip().endswith('</section>') else ''))
END = '</section>'
TBL = lambda rows: '<table>' + ''.join(
    '<tr>' + ''.join(f'<th>{c}</th>' if i == 0 else f'<td>{c}</td>' for i, c in enumerate(r)) + '</tr>'
    for r in rows) + '</table>'
Q = lambda n, t: f'<div class="question">\n<p><strong>Q{n}:</strong> {t}</p>\n</div>'


def build(slug, title, desc, sections):
    h = open(TPL, encoding='utf-8').read()
    h = h.replace('H1-kaiser-wilhelm-germany', slug)
    h = re.sub(r'<title>[^<]*</title>', f'<title>{title} - GCSE History</title>', h, count=1)
    h = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + desc + m.group(2), h, count=1)
    h = re.sub(r'(<meta name="keywords" content=")[^"]*(")',
               lambda m: m.group(1) + f'GCSE History, medicine through time, health and the people, {title.lower()}, GCSE revision' + m.group(2), h, count=1)
    h = re.sub(r'(<meta property="og:title" content=")[^"]*(")', lambda m: m.group(1) + title + ' - GCSE History' + m.group(2), h, count=1)
    h = re.sub(r'(<meta property="og:description" content=")[^"]*(")', lambda m: m.group(1) + desc + m.group(2), h, count=1)
    h = re.sub(r'(<meta name="twitter:title" content=")[^"]*(")', lambda m: m.group(1) + title + m.group(2), h, count=1)
    h = re.sub(r'(<meta name="twitter:description" content=")[^"]*(")', lambda m: m.group(1) + desc + m.group(2), h, count=1)
    h = re.sub(r'(<p class="topic-desc">)[^<]*(</p>)', lambda m: m.group(1) + desc + m.group(2), h, count=1)
    h = h.replace('>H1<', '>' + slug.split('-')[0] + '<')
    h = re.sub(r'<span class="topic-name">[^<]*</span>', f'<span class="topic-name">{title}</span>', h, count=1)
    # strip cloned per-board box; replace all content sections up to Share
    h = re.sub(r'<section class="section"><h2>🧭 Board Focus.*?</section>', '', h, flags=re.DOTALL, count=1)
    m1 = re.search(r'<section class="section">', h)
    share = re.search(r'<section class="section[^"]*">\s*<h2>Share this page</h2>', h)
    h = h[:m1.start()] + sections + '\n\n' + h[share.start():]
    return h


H40 = (
    H('📋 Key Concepts: Medicine in the Middle Ages', (
        '<p>Between <strong>c1250 and 1500</strong> medicine rested on two pillars: <strong>Hippocrates</strong> '
        '(clinical observation, the four humours) and <strong>Galen</strong> (whose theory of opposites and '
        'animal dissection dominated for 1,300 years). The <strong>Christian Church</strong> preserved Galen\u2019s '
        'writings and enforced his authority; <strong>miasma</strong> (bad air) explained most disease; '
        '<strong>supernatural</strong> explanations coexisted with natural ones.</p>' +
        TBL([
            ['Belief','What it meant','Typical treatment'],
            ['Four humours','Illness = imbalance of blood, phlegm, black bile, yellow bile','Bleeding, purging, opposites'],
            ['Miasma','Bad air caused disease','Sweetsmelling herbs, avoiding swamps'],
            ['Supernatural','Sin, planets, witchcraft','Prayer, pilgrimage, charms'],
            ['Galen\u2019s opposites','Treat hot with cold','Cooling foods for fevers'],
        ]) +
        '<p>Who treated you depended on wealth: <strong>physicians</strong> (university-trained, expensive, '
        'urine charts), <strong>apothecaries</strong> (herbal remedies), <strong>barber-surgeons</strong> '
        '(bleeding, amputation, no anatomy training), <strong>wise women</strong> and the household itself. '
        'Hospitals were religious institutions — care, not cure; most were destroyed at the Reformation '
        'or dissolved under Henry VIII.</p>' +
        '<p><strong>Case study — the Black Death (1348–49):</strong> killed perhaps a third of England. '
        'Explanations mixed supernatural (God\u2019s punishment, planetary alignment in 1345), miasma '
        '(corrupt air from earthquakes) and contagion-by-sight. Treatments: prayer, confession, carrying '
        'herbs, avoiding breathing bad air — quarantine attempts appeared in Italian ports. Continuity '
        'outweighed change: responses to plague in 1348 look like responses to later outbreaks in 1563 '
        'and 1665.</p>') + END) +

    H('📝 Progress and Its Limits (c1250–1500)', (
        '<p><strong>Real progress:</strong> <strong>medical training</strong> improved (Renaissance-style '
        'dissection began late in the period: human dissection was legally permitted from the 14th century '
        'in a few universities); <strong>Islamic medicine</strong> — <em>Ibn Sina (Avicenna)</em>\u2019s '
        '<em>Canon of Medicine</em> and <em>Al-Razi</em>\u2019s work — entered Europe via translated texts '
        'and raised clinical standards; <strong>John of Arderne</strong> (surgeon, anal fistula operation, '
        'c1350) showed careful technique and professional pride; <strong>medical regimens</strong> (the '
        'Regimen Sanitatis) promoted diet, exercise and moderation — Hippocratic prevention for the wealthy.</p>' +
        '<p><strong>Why change was slow:</strong> the Church promoted Galen because his ideas fit Christian '
        'teaching (the body as God\u2019s design); dissection was limited; printing had not yet arrived, so '
        'books were copied by hand and error-ridden; war (the Hundred Years\u2019 War) and plague cycles '
        'drained resources; physicians had status invested in NOT challenging Galen.</p>' +
        '<p><strong>Examiner\u2019s pointer:</strong> questions rarely ask "was medieval medicine bad?" — '
        'they ask you to weigh <strong>progress against continuity</strong> with SPECIFIC evidence on both '
        'sides, and to explain <strong>why</strong> (factors: Church, individuals, science and technology, '
        'war, attitudes).</p>') + END) +

    H('🧮 Worked Examples — Exam Style', (
        '<div class="example"><p><strong>Describe two features of medical treatment in the Middle Ages '
        '(4 marks).</strong></p>'
        '<p>Model: « Treatment was dominated by the theory of the four humours: physicians rebalanced the '
        'body by bleeding or purging patients. Second, supernatural explanations mattered: patients might '
        'go on pilgrimage or pray to saints because illness was often seen as God\u2019s punishment. »</p>'
        '<p><em>Two distinct features, each with a specific detail and one sentence of development — that '
        'is the full 4 marks. Vague answers ("treatment was bad") score nothing.</em></p></div>'
        '<div class="example"><p><strong>Interpretation question (8 marks): "Medieval hospitals were more '
        'about care than cure." How far does the source support this?</strong></p>'
        '<p>Method: (1) detail what the source shows (wards, religious staff, prayers for the soul); '
        '(2) link each detail to care vs cure; (3) add context the source CANNOT show — hospitals were '
        'founded as religious houses, physician treatment was separate, leprosy institutions isolated the '
        'sick; (4) judgement: the source supports it but is incomplete. Never spend the marks re-describing '
        'the source alone.</p></div>') + END) +

    H('❓ Practice Questions', (
        '<div class="practice-questions">' +
        Q(1,'Name the two ancient authorities who dominated medieval medicine.') +
        Q(2,'Describe two ways the Christian Church shaped medicine c1250–1500.') +
        Q(3,'Give two treatments a medieval apothecary might sell and the belief behind them.') +
        Q(4,'Describe two features of the Black Death of 1348–49.') +
        Q(5,'Explain why new medical ideas spread slowly in the Middle Ages (two reasons, 4 marks).') +
        Q(6,'“Medieval medicine owed more to religion than to science.” How far do you agree? (16 + 4 marks)') +
        '</div>') + END) +

    H('✅ Answers', (
        '<ol>'
        '<li><strong>Hippocrates</strong> (four humours, clinical observation) and <strong>Galen</strong> '
        '(opposites theory, authority on anatomy).</li>'
        '<li>The Church <strong>preserved and taught Galen</strong> in university curricula, and founded/run '
        '<strong>hospitals as religious care institutions</strong>; it also discouraged dissection and '
        'challenges to Galen.</li>'
        '<li>Herbal laxatives to <strong>purge</strong> excess humours; sweet-smelling posies/w herbs against '
        '<strong>miasma</strong>. (Any two with the belief named.)</li>'
        '<li>Killed roughly a third of England\u2019s population; explained by God\u2019s punishment/planets/'
        'miasma; responses included prayer, confession, quarantine in some ports, herbs against bad air.</li>'
        '<li><strong>Church control</strong> of learning defended Galen; <strong>no printing</strong> — '
        'hand-copied texts spread slowly and inaccurately. (Also accepted: limited dissection, war/plague '
        'disruption, physician status invested in Galen.)</li>'
        '<li>Essay plan — YES side: Galen preserved BY the Church; hospitals = prayers and care; plague '
        'responses religious. NO side: regimens and Arderne = empirical care; Islamic texts entered via '
        'translation (science); urine charts and observation = Hippocratic method alive. Judgement: religion '
        'DOMINATED delivery and explanation, but a genuine scientific strand persisted — answers that hold '
        'both sides and reach a reasoned verdict hit the top band.</li>'
        '</ol>') + END) +

    H('📌 Key Facts to Memorise', (
        '<ul>'
        '<li>Four humours (blood, phlegm, black bile, yellow bile) — Hippocrates; opposites — Galen</li>'
        '<li>Miasma theory; supernatural explanations coexisted with natural ones</li>'
        '<li>Practitioners: physician / apothecary / barber-surgeon / wise woman / home remedies</li>'
        '<li>Hospitals: religious, care-not-cure, ~470 by 1500 in England, lost at the Reformation</li>'
        '<li>Black Death 1348–49: ~⅓ dead; explanations supernatural + miasma + contagion</li>'
        '<li>Progress: Ibn Sina\u2019s Canon, John of Arderne c1350, Regimen Sanitatis, early legal dissection</li>'
        '<li>Continuity reasons: Church authority, no printing, limited dissection, social order</li>'
        '</ul>') + END) +

    H('🗺️ In the Exam', (
        '<p>In the thematic papers this period appears as the START of the narrative — examiners test whether '
        'you can characterise it precisely: <strong>continuity built on Galen + Church + supernatural '
        'beliefs, WITH pockets of progress</strong>. Compare-forward questions ("how similar was treatment '
        'in 1500 to 1700?") need BOTH periods\u2019 specifics: humours still ruled in 1500, but by 1700 '
        'printing, Vesalius and the collapse of Galen\u2019s authority had changed the ground rules. '
        'Name the factor for every point of change or continuity: the factor IS the explanation.</p>') + END) +

    H('⚠️ Common Errors', (
        '<ul>'
        '<li><span class="wrong">Wrong: "people were ignorant and used only prayer"</span> '
        '<span class="right">Correct: natural (humours, miasma) AND supernatural explanations coexisted — '
        'both could be used for the same illness</span></li>'
        '<li><span class="wrong">Wrong: "Galen was forgotten until the Renaissance"</span> '
        '<span class="right">Correct: Galen was taught and used throughout — the question is WHO challenged '
        'him, and when</span></li>'
        '<li><span class="wrong">Wrong: "hospitals cured the sick"</span> '
        '<span class="right">Correct: care, shelter and prayer; cure was not their function</span></li>'
        '<li><span class="wrong">Wrong: "the Church stopped all medicine"</span> '
        '<span class="right">Correct: the Church FUNDED most medicine — it shaped and preserved it, while '
        'also limiting challenges to Galen</span></li>'
        '</ul>') + END) +

    H('🎯 Exam Tips', (
        '<ul>'
        '<li>Anchor every paragraph with a factor word: Church, individuals, science/technology, war, '
        'government, attitudes</li>'
        '<li>Use dates sparingly but exactly: 1348 (Black Death), c1250 start, 1500 end</li>'
        '<li>For interpretation questions: evidence from the source + context BEYOND the source + a judgement</li>'
        '<li>Learn 2 progress examples AND 2 continuity examples — every "how far" question needs both</li>'
        '</ul>') + END)
)

H41 = (
    H('📋 Key Concepts: The Medical Renaissance (1500–1700)', (
        '<p>The <strong>printing press (c1440s, reached England 1476)</strong> changed everything: identical, '
        'accurate copies of texts (including Galen in the original Greek) spread fast — and so did '
        '<strong>challenge</strong> to Galen, because scholars could now compare translations and spot errors. '
        'The <strong>Reformation</strong> weakened the Church\u2019s grip on learning (monasteries dissolved '
        '1536–39, their hospitals gone). <strong>Humanism</strong> — "back to the originals" — inspired '
        'anatomists to check Galen against human bodies.</p>' +
        TBL([
            ['Individual','What they did','Why it mattered'],
            ['Andreas Vesalius','De Humani Corporis Fabrica (1543); dissected humans himself; corrected ~300 Galen errors','Proved Galen only dissected animals — licence to question'],
            ['William Harvey','De Motu Cordis (1628): blood CIRCULATES, pumped by the heart','Broke Galen\u2019s blood-flow model; method: observation, dissection, maths'],
            ['Ambroise Paré','Ligatures instead of cauterising wounds; ointments for gunshot','Practical surgery progress from battlefield experience'],
            ['Thomas Sydenham','Observed patients directly; distinguished diseases; "English Hippocrates"','Revived bedside observation over book theory'],
        ]) +
        '<p><strong>Great Plague 1665:</strong> responses still looked medieval (quarantine, red crosses on '
        'doors, killing cats and dogs — which made it worse, prayer, herbs against miasma) but with new '
        'elements: plague doctors, searchers of the dead keeping bills of mortality, government quarantine '
        'orders. Change at the edges, continuity at the core.</p>') + END) +

    H('📝 Continuity: Why Most Treatment Did Not Change', (
        '<p>Vesalius and Harvey changed KNOWLEDGE, not treatment: there was still no germ theory, no '
        'effective drugs, no anaesthetics or antiseptics. Physicians still bled and purged; apothecaries '
        'still sold herbs; the four humours lingered in practice into the 18th century. '
        '<strong>Harvey\u2019s own contemporaries</strong> attacked him (his old teacher ridiculed him); '
        'training lagged behind discovery by decades. <strong>Meetings and institutions</strong> seeded the '
        'future: the Royal Society (1660) published and debated new science (Philosophical Transactions, '
        '1665) — a channel that would later carry Jenner, Pasteur and Koch.</p>' +
        '<p><strong>Examiner\u2019s pointer:</strong> the best answers treat the Renaissance as a change in '
        '<strong>methods and authority</strong> (observation over texts; printing; royal societies) rather '
        'than a change in <strong>care</strong>. Say that explicitly.</p>') + END) +

    H('🧮 Worked Examples — Exam Style', (
        '<div class="example"><p><strong>&ldquo;The printing press was the most important reason for '
        'medical progress in the Renaissance.&rdquo; How far do you agree? (16 + 4 marks)</strong></p>'
        '<p>Plan — P1 printing: identical texts, Galen\u2019s errors visible, Vesalius\u2019s Fabrica '
        'illustrated and copied across Europe. P2 individuals: Vesalius/Harvey made the discoveries — '
        'printing only spread them. P3 attitudes: humanism gave scholars the CONFIDENCE to test authority. '
        'P4 institutions: the Royal Society created a permanent arena. Judgement: printing was the '
        '<em>accelerator</em> — but humanist attitudes and individuals were the engine; without Vesalius '
        'there is nothing to print.</p>'
        '<p><em>Four-paragraph structure, each anchored to a FACTOR, with a weighed judgement — the '
        '16-mark formula on every thematic paper.</em></p></div>') + END) +

    H('❓ Practice Questions', (
        '<div class="practice-questions">' +
        Q(1,'Name Vesalius\u2019s 1543 book and its key claim about Galen.') +
        Q(2,'Describe two features of William Harvey\u2019s work on circulation.') +
        Q(3,'Give two ways Paré improved battlefield surgery.') +
        Q(4,'Describe two features of responses to the Great Plague of 1665.') +
        Q(5,'Explain why the Reformation affected medicine in England (two ways, 4 marks).') +
        Q(6,'"Renaissance doctors cared more about challenging Galen than about treating patients." '
           'How far do you agree? (16 + 4 marks)') +
        '</div>') + END) +

    H('✅ Answers', (
        '<ol>'
        '<li><strong>De Humani Corporis Fabrica</strong> (1543) — dissected humans himself and exposed '
        'hundreds of Galen\u2019s anatomical errors (e.g. the jawbone, the uterus).</li>'
        '<li>Proved blood <strong>circulates</strong> (valves, one-way flow); demonstrated the heart works '
        'as a pump via dissection and calculation — published in <em>De Motu Cordis</em> (1628) using '
        'observation and experiment over textual authority.</li>'
        '<li><strong>Ligatures</strong> to tie arteries instead of burning flesh with hot oil/cautery; '
        '<strong>soothing ointments</strong> for gunshot wounds instead of the accepted (brutal) treatment.</li>'
        '<li>Quarantine and shuttering of infected households (red crosses, 40-day isolation); searchers of '
        'the dead producing weekly <strong>bills of mortality</strong>; (also: killing dogs/cats, prayers, '
        'miasma-defending herbs).</li>'
        '<li>Monasteries dissolved (1536–39) — <strong>hospitals and care networks lost</strong>; Church '
        'authority over learning weakened, so <strong>humanist challenge to Galen became safer</strong>. '
        '(Also: university curricula freed up; printing spread Protestant-backed new learning.)</li>'
        '<li>Plan — YES: Vesalius/Harvey targeted texts, not bedsides; humours still used in treatment; '
        'Sydenham the exception. NO: Paré = bedside surgery; Sydenham\u2019s clinical observation; Harvey\u2019s '
        'work eventually reoriented training. Judgement: challenge led care by decades — the statement is '
        'half-true for the elite, wrong for the bedside.</li>'
        '</ol>') + END) +

    H('📌 Key Facts to Memorise', (
        '<ul>'
        '<li>Printing (c1440s; England 1476) — accurate texts + spread of challenge</li>'
        '<li>Vesalius, Fabrica 1543 — human dissection, corrected Galen</li>'
        '<li>Harvey, De Motu Cordis 1628 — circulation, experiment-based proof</li>'
        '<li>Paré — ligatures, ointments (battlefield, 1530s–60s)</li>'
        '<li>Sydenham — bedside observation, disease distinction ("English Hippocrates")</li>'
        '<li>Royal Society 1660; Philosophical Transactions 1665</li>'
        '<li>Great Plague 1665 — quarantine + bills of mortality; humours/miasma still core beliefs</li>'
        '<li>Reformation 1536–39 — hospitals lost, authority loosened</li>'
        '</ul>') + END) +

    H('🗺️ In the Exam', (
        '<p>The Renaissance rewards <strong>paired comparisons</strong>: knowledge changed (Vesalius, '
        'Harvey) while treatment stayed humoral; authority shifted (text → observation) while the Church '
        'loosened its grip. In "how far" questions, mark the SHIFT explicitly — methods and attitudes '
        'changed faster than care. For interpretation questions on the Great Plague, contrast 1665 with '
        '1348: same beliefs, slightly more organised government — continuity IS the interpretation point.</p>') + END) +

    H('⚠️ Common Errors', (
        '<ul>'
        '<li><span class="wrong">Wrong: "Vesalius discovered circulation"</span> '
        '<span class="right">Correct: Vesalius = anatomy corrections; Harvey = circulation (1628)</span></li>'
        '<li><span class="wrong">Wrong: "the Royal Society invented germ theory"</span> '
        '<span class="right">Correct: the Royal Society was a publishing/debating forum (1660) — germ '
        'theory came in the 1860s–70s</span></li>'
        '<li><span class="wrong">Wrong: "Paré used antiseptic"</span> '
        '<span class="right">Correct: Paré used ligatures and ointments — antisepsis is Lister, 1867</span></li>'
        '<li><span class="wrong">Wrong: "1665 plague responses were scientific"</span> '
        '<span class="right">Correct: quarantine was organisationally new, but prayer and miasma-avoidance '
        'dominated</span></li>'
        '</ul>') + END) +

    H('🎯 Exam Tips', (
        '<ul>'
        '<li>Pair every Renaissance individual with a FACTOR: Vesalius = technology (printing) + attitudes '
        '(humanism); Paré = war; Harvey = method (experiment)</li>'
        '<li>Always separate KNOWLEDGE progress from TREATMENT progress — the paper rewards the distinction</li>'
        '<li>1665 vs 1348 comparisons are high-yield: organisation changed, beliefs did not</li>'
        '<li>Quote book titles with dates: Fabrica (1543), De Motu Cordis (1628)</li>'
        '</ul>') + END)
)

H42 = (
    H('📋 Key Concepts: Industrial Medicine (1700–1900)', (
        '<p>The industrial city broke medieval medicine\u2019s world: overcrowded slums created epidemic '
        'conditions, and <strong>government action</strong> — unthinkable in 1700 — became the decisive '
        'factor by 1900. The period\u2019s arc: spontaneous generation defeated by <strong>germ theory '
        '(1861)</strong>; vaccination generalised; antiseptic and aseptic surgery; and public health '
        'legislation from <strong>1875</strong> that rebuilt urban Britain.</p>' +
        TBL([
            ['Individual / event','Contribution','Effect'],
            ['Edward Jenner (1796)','Vaccination against smallpox (cowpox → immunity)','First vaccination; government funded it 1840; made compulsory 1853'],
            ['Louis Pasteur (1861)','Germ theory: microbes cause decay/disease','Killed spontaneous generation; gave Koch a map'],
            ['Robert Koch (1870s–80s)','Microscope + staining: identified TB (1882), cholera (1883)','Microbe-hunting model; "magic bullets" follow'],
            ['John Snow (1854)','Broad Street pump: cholera mapped to contaminated water','Epidemiology before germ theory; removed the pump handle'],
            ['Florence Nightingale (1854–56+)','Sanitary wards, nursing professionalism','Hospital death rates fell; nursing became trained'],
            ['James Simpson (1847)','Chloroform anaesthesia','Pain-free surgery (opposition: "pain is God-given")'],
            ['Joseph Lister (1867)','Carbolic antiseptic surgery','Surgical deaths fell sharply; asepsis follows by 1900'],
            ['Public Health Acts 1848 & 1875','Local boards of health; 1875: clean water, sewers, inspection COMPULSORY','The state became responsible for health'],
        ]) + END) +

    H('📝 Why It Took So Long: Resistance and the Push', (
        '<p><strong>Resistance:</strong> Jenner\u2019s vaccination was opposed by inoculators (who profited '
        'from the old method) and churches ("injecting cow matter is ungodly"); Snow\u2019s water theory '
        'faced miasma-believers (the government report on his 1848–49 outbreak rejected him); chloroform '
        'faced religious objections until <strong>Queen Victoria took it in childbirth (1853)</strong>; '
        '<strong>laissez-faire</strong> — the doctrine that government should not interfere — blocked public '
        'health spending until cholera epidemics (1848, 1866) and Edwin Chadwick\u2019s report (1842: '
        'disease causes poverty) forced the state\u2019s hand; the 1866 cholera outbreak (the last) finally '
        'made the 1875 Act politically unstoppable.</p>' +
        '<p><strong>Enablers:</strong> the microscope\u2019s improvement; anaesthetics making longer, '
        'deeper surgery possible (which then demanded antisepsis — the two advances interlock); railways '
        'spreading news of discoveries; steam printing + universal education spreading public health '
        'arguments; urban epidemics hitting voters.</p>' +
        '<p><strong>Examiner\u2019s pointer:</strong> the "how far did X help" questions here are usually '
        'about <strong>individuals vs government</strong> — the strongest answers show individuals producing '
        'the knowledge, and government (only after epidemics + reports + press) DELIVERING it.</p>') + END) +

    H('🧮 Worked Examples — Exam Style', (
        '<div class="example"><p><strong>"The most important reason for improved public health after 1750 '
        'was the work of individuals." How far do you agree? (16 + 4)</strong></p>'
        '<p>Plan — YES: Chadwick\u2019s 1842 report, Snow\u2019s pump, Pasteur/Koch\u2019s germ theory gave '
        'government the evidence and the confidence. NO: laissez-faire attitudes and government inaction '
        'delayed everything until epidemics (1848, 1866) made reform unavoidable; the 1875 Act was '
        'compulsory BY LAW, which no individual alone could deliver. Judgement: individuals created the '
        'knowledge; epidemics created the urgency; government created the change — weight your verdict '
        'toward the interplay, not one factor.</p></div>'
        '<div class="example"><p><strong>Describe two features of surgical progress 1847–1900 (4 marks).</strong></p>'
        '<p>Model: « Anaesthetics (chloroform, 1847) removed pain, allowing longer operations. Antiseptic '
        'surgery (Lister\u2019s carbolic acid, 1867) cut post-operative infection deaths, and by 1900 aseptic '
        'theatre routines had followed. »</p>'
        '<p><em>Two features + development each — 4/4. Note the chronology: anaesthetics BEFORE antiseptics, '
        'because pain-free surgery exposed infection as the next killer.</em></p></div>') + END) +

    H('❓ Practice Questions', (
        '<div class="practice-questions">' +
        Q(1,'What did Pasteur publish in 1861, and what did it disprove?') +
        Q(2,'Describe two features of John Snow\u2019s 1854 cholera investigation.') +
        Q(3,'Give two reasons Jenner\u2019s vaccination faced opposition.') +
        Q(4,'Describe two features of the 1875 Public Health Act.') +
        Q(5,'Explain why surgery improved so rapidly after 1847 (two reasons, 4 marks).') +
        Q(6,'"Germ theory changed medicine more than the 1875 Public Health Act." How far do you agree? '
           '(16 + 4 marks)') +
        '</div>') + END) +

    H('✅ Answers', (
        '<ol>'
        '<li><strong>Germ theory</strong> — microbes cause decay and disease — disproving '
        '<strong>spontaneous generation</strong> (that life arises from rotting matter).</li>'
        '<li>Mapped cholera deaths around the <strong>Broad Street pump</strong> (SoHo); removed the pump '
        'handle and deaths stopped; proved water-borne spread BEFORE germ theory existed.</li>'
        '<li><strong>Inoculators lost income</strong> (the old smallpox-infection business); some churchmen '
        'called vaccination <strong>ungodly</strong> (injecting animal disease). (Also: initial safety '
        'fears; no germ theory to explain why it worked.)</li>'
        '<li>Made <strong>clean water, sewers and public health officers COMPULSORY</strong> for every '
        'town council; consolidated earlier permissive acts (1848) into enforceable law — the state '
        'accepted responsibility for urban health.</li>'
        '<li><strong>Anaesthetics (1847)</strong> removed pain → longer, more complex operations possible; '
        '<strong>antisepsis (1867)</strong> then asepsis attacked surgical infection, the main cause of '
        'post-operative death. (Also accepted: Nightingale\u2019s sanitary wards; Koch\u2019s microbe '
        'identification.)</li>'
        '<li>Plan — Germ theory: the knowledge revolution; guided Koch, vaccines, antiseptics. 1875 Act: '
        'delivered clean water/sewers to EVERYONE (bigger lives-saved effect; knowledge without delivery '
        'saves nobody). Judgement: germ theory transformed medicine\u2019s DIRECTION; the 1875 Act '
        'transformed the nation\u2019s HEALTH — argue which kind of "changed" the question means, then '
        'commit.</li>'
        '</ol>') + END) +

    H('📌 Key Facts to Memorise', (
        '<ul>'
        '<li>Jenner 1796 vaccination; funded 1840; compulsory 1853</li>'
        '<li>Chadwick report 1842; Public Health Acts 1848 (permissive) and 1875 (compulsory)</li>'
        '<li>Cholera epidemics 1848, 1854 (Snow), 1866 (the last)</li>'
        '<li>Pasteur germ theory 1861 · Koch TB 1882, cholera 1883 · Pasteurisation, rabies vaccine 1885</li>'
        '<li>Simpson chloroform 1847 · Nightingale 1854–56 · Lister carbolic 1867 · asepsis by 1900</li>'
        '<li>Laissez-faire attitudes as the barrier; epidemics + press + voters as the push</li>'
        '</ul>') + END) +

    H('🗺️ In the Exam', (
        '<p>Industrial medicine is the EXAMINERS\u2019 FAVOURITE period for "how far" questions because the '
        'factors collide: science (germ theory), individuals (Snow, Pasteur, Nightingale), government (1875), '
        'war (Crimea → Nightingale), technology (microscope), attitudes (laissez-faire breaking down). '
        'Build every answer as a FACTOR-LED narrative, not a list of names. Chronology checkpoints: 1796 → '
        '1842 → 1847 → 1848 → 1854 → 1861 → 1866 → 1867 → 1875 → 1882 → 1900. If your essay cannot '
        'place each factor on that line, it will drift.</p>') + END) +

    H('⚠️ Common Errors', (
        '<ul>'
        '<li><span class="wrong">Wrong: "Pasteur discovered germ theory in 1885"</span> '
        '<span class="right">Correct: 1861 (decay/microbes); 1885 = rabies vaccine</span></li>'
        '<li><span class="wrong">Wrong: "Lister invented anaesthetics"</span> '
        '<span class="right">Correct: Simpson/chloroform 1847; Lister = antiseptics 1867</span></li>'
        '<li><span class="wrong">Wrong: "the 1848 Act made public health compulsory"</span> '
        '<span class="right">Correct: 1848 permissive; 1875 compulsory</span></li>'
        '<li><span class="wrong">Wrong: "Snow used germ theory to find the pump"</span> '
        '<span class="right">Correct: Snow worked by mapping deaths — BEFORE germ theory (he suspected '
        'a "poison" in the water, not specific microbes)</span></li>'
        '</ul>') + END) +

    H('🎯 Exam Tips', (
        '<ul>'
        '<li>Interlock the pairs: anaesthetics → longer surgery → infection deaths visible → antiseptics; '
        'germ theory → Koch → vaccines and "magic bullets"</li>'
        '<li>Government questions: 1842 report → 1848 permissive → 1866 epidemic → 1875 compulsory. '
        'Sequence = explanation</li>'
        '<li>Name the ATTITUDE factor (laissez-faire, religious objection) — attitude factors are '
        'underused and examiners reward them</li>'
        '<li>Nightingale = Crimea war factor + sanitation factor + women-in-medicine factor; deploy her '
        'wherever the question mentions war or nursing</li>'
        '</ul>') + END)
))

PAGES = [
    ("H40-medieval-medicine-c1250-1500",
     "Medieval Medicine c1250–1500",
     "Hippocrates, Galen and the four humours; miasma and supernatural beliefs; physicians, apothecaries and barber-surgeons; the Black Death of 1348–49; progress and continuity in medieval medicine.",
     H40),
    ("H41-renaissance-medicine-1500-1700",
     "Renaissance Medicine 1500–1700",
     "Vesalius, Harvey and Paré; the printing press and humanist challenge to Galen; Sydenham's bedside observation; the Royal Society; continuity in treatment and the Great Plague of 1665.",
     H41),
    ("H42-industrial-medicine-1700-1900",
     "Industrial Medicine 1700–1900",
     "Jenner's vaccination, Pasteur's germ theory, Koch's microbes, Snow's cholera map, Nightingale's sanitary wards, anaesthetics and antiseptics, and the Public Health Acts of 1848 and 1875.",
     H42),
]

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else 'topics/history/aqa'
    for slug, title, desc, body in PAGES:
        html = build(slug, title, desc, body)
        open(f'{out}/{slug}.html', 'w', encoding='utf-8').write(html)
        print('wrote', f'{out}/{slug}.html', len(html), 'bytes')
