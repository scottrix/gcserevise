#!/usr/bin/env python3
"""History options: American West (A40-42), Russia (R40-43), Cold War (C40-43).
Compact depth — 12 topics covering the core narrative of each option."""
from build_medicine_a import build, H, END, TBL, Q

def topic(key_concepts, worked, practice, answers, keyfacts, exam, errors, tips):
    return (
        H('📋 Key Concepts', key_concepts + END) +
        H('🧮 Worked Examples — Exam Style', worked + END) +
        H('❓ Practice Questions', '<div class="practice-questions">' +
          ''.join(Q(i + 1, t) for i, t in enumerate(practice)) + '</div>' + END) +
        H('✅ Answers', '<ol>' + ''.join(f'<li>{a}</li>' for a in answers) + '</ol>' + END) +
        H('📌 Key Facts to Memorise', '<ul>' + ''.join(f'<li>{k}</li>' for k in keyfacts) + '</ul>' + END) +
        H('🗺️ In the Exam', f'<p>{exam}</p>' + END) +
        H('⚠️ Common Errors', '<ul>' + ''.join(
            f'<li><span class="wrong">Wrong: {w}</span> <span class="right">Correct: {r}</span></li>'
            for w, r in errors) + '</ul>' + END) +
        H('🎯 Exam Tips', '<ul>' + ''.join(f'<li>{t}</li>' for t in tips) + '</ul>' + END)
    )

PAGES = []

# ============================== AMERICAN WEST (aqa, edexcel) ==============================
PAGES.append(("A40-plains-indians-way-of-life",
 "The Plains Indians' Way of Life",
 "Lakota bands and tribes, the buffalo economy, counting coup and beliefs, the horse — with structure vocabulary for way-of-life questions.",
 topic(
  '<p><strong>Structure:</strong> <strong>bands</strong> (extended family, ~10–30 tipis) formed <strong>tribes</strong> '
  '(Lakota, Cheyenne) only for summer hunts; chiefs led by consent; women owned the tipi and processed buffalo; '
  'old age = wisdom. <strong>Beliefs:</strong> Wakan Tanka (Great Spirit), the sacred circle, land held in common '
  '(never owned), visions and the Sun Dance. <strong>Buffalo = life</strong>: food, tipi, clothing, tools, fuel, '
  'ceremony. <strong>Warfare:</strong> small-scale and ritual — <strong>counting coup</strong> (touching an enemy) '
  'outranked killing. <strong>Horses (1600s+):</strong> transformed hunting, warfare and wealth.</p>',
  "<div class='example'><p><strong>Describe two features of Plains Indian beliefs (4).</strong></p>"
  "<p>« They believed in Wakan Tanka, the Great Spirit present in all things. The circle was sacred — tipis, camps "
  "and the Sun Dance were circular because life had no end. »</p></div>",
  ["Name two roles of women in Plains bands.",
   "Describe two features of the Sun Dance.",
   "What was counting coup, and why did it matter?",
   "Describe two uses of the buffalo.",
   "'The horse was the most important change in Plains life.' How far do you agree? (16 + 4)"],
  ["<strong>Women</strong>: owned the tipi, butchered and processed buffalo, influenced band decisions.",
   "<strong>Sun Dance</strong>: summer renewal ceremony — later banned by the US government.",
   "<strong>Counting coup</strong>: touching an enemy with a coup stick earned the highest honour.",
   "Buffalo: food, tipi covering, clothing, shields, fuel (dung), ceremony.",
   "Land: held in common and sacred — US ownership law violated the Plains way."],
  "Use band/tribe vocabulary precisely — examiners reward the distinction. Way-of-life questions contrast "
  "naturally with white settlers: land, warfare, family, law.",
  ["Homestead Act 1862: 160 acres, 5 years; railroad 1869; barbed wire 1874.",
   "Band (10-30 tipis) -> tribe; chiefs by consent; women owned the tipi.",
   "Counting coup outranked killing; buffalo = economy + religion; land held in common."],
  [("Plains people were 'primitive'", "Their society solved survival on the Plains elegantly — mobility, consent "
    "and ecology in balance"),
   ("Chiefs ordered everyone about", "Leadership was by consent; war chiefs led only raids")],
  ["Learn band → tribe structure with ONE example (Lakota).",
   "Buffalo + horse = your two evidence anchors for any way-of-life question."])))

PAGES.append(("A41-homesteaders-and-the-railroads",
 "Westward Expansion: Homesteaders and the Railroads",
 "Manifest Destiny, the Homestead Act 1862, the transcontinental railroad, sod-house problems and their solutions — with mechanism chains for essay questions.",
 topic(
  '<p><strong>Manifest Destiny</strong>: God intended settlement west to the Pacific — justifying expansion and '
  'ignoring Native rights. <strong>Homestead Act 1862</strong>: 160 acres free for 5 years\u2019 work. '
  '<strong>Transcontinental railroad (1869)</strong> + land grants opened markets. <strong>Problems:</strong> sod '
  'houses, blizzards, drought, locusts (1874–75), isolation; <strong>160 acres too little in dry lands</strong>. '
  '<strong>Solutions:</strong> barbed wire (1874), windmills, dry farming, Turkey Red wheat, Exodusters (1879).</p>',
  "<div class='example'><p><strong>'The railroads were the most important reason for settlement of the Plains.' "
  "How far do you agree? (16 + 4)</strong></p>"
  "<p>YES: the 1869 line brought settlers, goods and markets; land grants funded it; railhead towns boomed. NO: "
  "the Homestead Act gave the LEGAL right; barbed wire and windmills made 160 acres workable; Manifest Destiny "
  "supplied the motive. Verdict: railroads DELIVERED settlement — law and technology made it survive.</p></div>",
  ["Describe two features of the Homestead Act.",
   "Give two problems homesteaders faced on the Plains.",
   "Describe two features of Manifest Destiny.",
   "Explain why 160 acres was often not enough (two reasons, 4 marks).",
   "'Barbed wire changed the West more than the railroad.' How far do you agree? (16 + 4)"],
  ["Homestead Act 1862: 160 acres, 5 years, small fee (21+ or head of household).",
   "Transcontinental railroad completed 1869 (Promontory Point).",
   "Barbed wire 1874 (Glidden); windmills pumped deep water.",
   "Exodusters 1879: ex-slaves moving to Kansas.",
   "Locust plagues 1874–75; Panic of 1873 slowed settlement."],
   [    "Key facts: revise the dates and figures named above."],
  "Economic questions need MECHANISMS: land grant → railroad → settler → market → more settlers. The 1862/1869/1874 "
  "sequence anchors any answer.",
  [("The government gave land away for nothing", "It was a deliberate policy to settle the Plains — and railroad "
    "companies profited hugely"),
   ("Homesteaders were all white-born Americans", "Immigrants and Exodusters (black Americans) settled too")],
  ["Sequence 1862 → 1869 → 1874 as your essay spine.",
   "Pair each problem with its solution (sod → lumber rails; drought → windmills)."])))

PAGES.append(("A42-cattle-industry-and-open-range",
 "The Cattle Industry and the Open Range",
 "Longhorn drives from Texas, Abilene and the Chisholm Trail, cowboys' real lives, the Big Die-Up of 1886–87 and barbed wire's end of the open range.",
 topic(
  '<p><strong>Origins:</strong> longhorns worth $4 in Texas, $40 in the North; <strong>Joseph McCoy\u2019s Abilene '
  '(1867)</strong> = railhead + stockyards; the <strong>Chisholm Trail</strong> (1,500–3,000 head, 8–12 cowboys, '
  '~15 miles/day). <strong>Cowboys:</strong> ~25% black or Mexican; ~$25–30/month; romanticised by dime novels. '
  '<strong>End:</strong> overstocking, the <strong>Terrible Winter 1886–87</strong> (Big Die-Up), barbed wire '
  'closing trails, railroads reaching Texas — open range dead by 1890 (Johnson County War 1892 as the violent '
  'aftermath).</p>',
  "<div class='example'><p><strong>'The railroads made and killed the cattle industry.' How far do you agree? "
  "(16 + 4)</strong></p>"
  "<p>MADE: railheads (Abilene 1867) connected herds to eastern prices. KILLED: rails reached Texas directly "
  "(1880s), ending the drives; barbed wire cut trails. Verdict: the industry\u2019s rise AND fall were rail-driven "
  "— with overstocking and the 1886–87 winter as the immediate killers.</p></div>",
  ["Describe two features of a cattle drive.",
   "Give two reasons the open range ended.",
   "Why was Abilene significant?",
   "Describe two features of a cowboy's real life.",
   "'The winter of 1886–87 mattered more than barbed wire in ending the open range.' How far do you agree? (16 + 4)"],
  ["McCoy\u2019s Abilene 1867 · Chisholm Trail · drives 1866–85.",
   "Cowboys: 8–12 per drive, ~$25–30/month, ~25% black or Mexican.",
   "Big Die-Up: winter 1886–87 (up to 90% losses on some ranges).",
   "Barbed wire 1874 → fenced ranges → fence-cutting wars (Johnson County War 1892)."],
   [    "Homestead Act 1862: 160 acres, 5 years; railroad 1869; barbed wire 1874.",
    "Exodusters 1879; locust plagues 1874-75; Panic of 1873.",
    "Solutions: windmills, dry farming, Turkey Red wheat, sod houses."],
  "Cowboy questions: contrast MYTH (dime novels, independence) with REALITY (wage labour, bilingual crews, short "
  "careers). The 1886–87 winter is your natural factor — most candidates forget non-human causes.",
  [("All cowboys were white and heroic", "~25% were black or Mexican; the work was dirty, seasonal wage labour"),
   ("Barbed wire was invented for ranchers", "It was a farm tool ranchers adopted — then fought trail drivers "
    "over")],
  ["Abilene 1867 + Big Die-Up 1886–87 = the industry\u2019s bookends.",
   "Use 'open range' vs 'fenced ranch' as your change-over-time frame."])))

PAGES.append(("A43-conflict-reservations-and-wounded-knee",
 "Conflict, Reservations and Wounded Knee",
 "Sand Creek 1864, Red Cloud's War, the 1868 treaty, Little Bighorn 1876, the buffalo's destruction, the Dawes Act 1887 and Wounded Knee 1890.",
 topic(
  '<p><strong>Sand Creek Massacre (1864)</strong>: Chivington\u2019s militia killed a Cheyenne village camped under '
  'the US flag. <strong>Red Cloud\u2019s War (1866–68)</strong>: Fetterman ambush; the <strong>1868 Treaty</strong> '
  'guaranteed the Black Hills — until gold (1874) → <strong>Little Bighorn (1876)</strong> → revenge and forced '
  'surrenders. <strong>Buffalo destroyed</strong> (millions to near-extinction by 1885: railroads, hide hunters, '
  'army policy). <strong>Dawes Act 1887</strong>: allotment broke tribal land; <strong>Ghost Dance (1890)</strong> → '
  'fear → <strong>Wounded Knee Massacre (1890, ~250 dead)</strong> — the Plains wars end.</p>',
  "<div class='example'><p><strong>'The destruction of the buffalo was the most important reason Plains Indian "
  "life collapsed.' How far do you agree? (16 + 4)</strong></p>"
  "<p>YES: buffalo = food, shelter, religion — its loss destroyed economy AND culture; railroads and hide hunters "
  "did it in a decade. NO: reservations confined people; the Dawes Act legally dismantled tribal land; defeats "
  "after 1876 destroyed independence. Verdict: the buffalo killed the body of the way of life; the Dawes Act "
  "killed it in law.</p></div>",
  ["Describe two features of the Fort Laramie Treaty (1868).",
   "What happened at Sand Creek (1864)?",
   "Describe two features of Little Bighorn (1876).",
   "Explain why the buffalo was destroyed (two reasons, 4 marks).",
   "'Government policy, not the army, destroyed Plains Indian life.' How far do you agree? (16 + 4)"],
  ["Sand Creek 1864 · Fetterman 1866 · Treaty 1868 · Little Bighorn 1876 · Wounded Knee 1890.",
   "Dawes Act 1887: 160-acre allotments, 'surplus' sold, tribal structures broken.",
   "Buffalo: ~30 million → near-extinction by 1885.",
   "Ghost Dance: pan-Indian revival; Wounded Knee ~250 dead."],
   [    "McCoy's Abilene 1867; Chisholm Trail; drives 1866-85.",
    "Cowboys: 8-12 per drive, ~$25-30/month, ~25% black or Mexican.",
    "Big Die-Up winter 1886-87; barbed wire 1874; Johnson County War 1892."],
  "Chronology chains win here: treaty → gold → war → defeat → reservation → allotment → Ghost Dance → Wounded "
  "Knee. Name treaties and years — vague answers score low.",
  [("Little Bighorn was the last Indian victory", "It was the last major US defeat — resistance continued to "
    "Wounded Knee 1890"),
   ("Reservations were voluntary", "Treaties were forced and then broken whenever gold or land was found")],
  ["1868 treaty → 1874 gold → 1876 Custer — the Black Hills chain is exam gold.",
   "Dawes Act 1887 = the legal end; Wounded Knee 1890 = the military end."])))

# ============================== RUSSIA (aqa, edexcel, ocr) ==============================
PAGES.append(("R40-tsarist-russia-and-the-1905-revolution",
 "Tsarist Russia and the 1905 Revolution",
 "Nicholas II's autocracy, opposition parties, industrialisation's strains, Bloody Sunday 1905, the October Manifesto and Stolypin's Dumas.",
 topic(
  '<p><strong>Autocracy:</strong> Nicholas II (1894–1917) ruled by divine right; censorship; Okhrana. '
  '<strong>Opposition:</strong> Kadets (liberals), Social Revolutionaries (peasants, terror), Social Democrats '
  '(Marxists — Bolshevik/Menshevik split 1903). <strong>Strains:</strong> Witte\u2019s industrialisation, peasant '
  'land hunger, defeat in the Russo-Japanese War (1904–05). <strong>1905:</strong> <strong>Bloody Sunday (22 '
  'January)</strong> — Gapon\u2019s peaceful march shot down; strikes, Potemkin mutiny, peasant disorders → the '
  '<strong>October Manifesto</strong> (liberties + Duma) split the opposition; the Fundamental Laws (1906) restored '
  'autocracy; Stolypin repressed (the \u201cnecktie\u201d) and reformed (wager on the strong); the 1907 electoral '
  'coup packed the third Duma.</p>',
  "<div class='example'><p><strong>'Bloody Sunday was the main cause of the 1905 Revolution.' How far do you "
  "agree? (16 + 4)</strong></p>"
  "<p>YES: it destroyed the Tsar\u2019s 'Little Father' image and triggered the national strike wave. NO: industrial "
  "misery, land hunger, military defeat and liberal demands predated it. Verdict: Bloody Sunday was the TRIGGER; "
  "structural grievances were the CAUSE — the distinction earns top bands.</p></div>",
  ["Describe two features of Bloody Sunday (1905).",
   "Give two features of the October Manifesto.",
   "Describe two features of opposition to the Tsar before 1905.",
   "Explain why the 1905 Revolution failed (two reasons, 4 marks).",
   "'The October Manifesto saved the Tsar in 1905.' How far do you agree? (16 + 4)"],
  ["Bloody Sunday 22 Jan 1905 (Gapon).",
   "October Manifesto Oct 1905; Fundamental Laws Apr 1906 ('supreme autocratic power').",
   "Stolypin: wager on the strong, hangings, 1907 franchise change.",
   "Dumas 1 and 2 dissolved; third (1907) loyal."],
   [    "Sand Creek 1864; Fetterman 1866; Treaty 1868; Little Bighorn 1876; Wounded Knee 1890.",
    "Dawes Act 1887: 160-acre allotments, 'surplus' sold.",
    "Buffalo ~30 million to near-extinction by 1885."],
  "1905 vs 1917 comparisons: 1905 = spontaneous, loyal, ended by concessions; 1917 = organised, war-worn, "
  "irreversible. Keep the comparison ready.",
  [("The Duma had real power from 1906", "The Fundamental Laws kept autocracy — the Tsar ruled by decree"),
   ("Bloody Sunday was a revolutionary plot", "Gapon\u2019s march was peaceful — the shooting radicalised it")],
  ["Trigger-vs-cause distinction for every revolution question.",
   "1905 = dress rehearsal — use it to explain February 1917\u2019s success."])))

PAGES.append(("R41-1917-february-october-and-dual-power",
 "1917: February and October Revolutions",
 "WWI strains, the February Revolution and abdication, dual power, Lenin's April Theses, the Kornilov affair and the Bolshevik seizure of power.",
 topic(
  '<p><strong>February:</strong> bread shortages + war weariness → strikes and garrison mutiny; Nicholas abdicated '
  '(2 March); <strong>Provisional Government</strong> shared <strong>dual power</strong> with the Petrograd Soviet '
  '(Order No. 1). <strong>Lenin\u2019s April Theses</strong>: \u2018Peace, Bread, Land\u2019, \u2018All power to the '
  'Soviets\u2019, no cooperation with the PG. July Days crushed; <strong>Kornilov affair (August)</strong> — Kerensky '
  'armed the Bolsheviks. <strong>October 24–25</strong>: Red Guards seized bridges, telegraph, Winter Palace; '
  '<strong>Sovnarkom</strong> under Lenin.</p>',
  "<div class='example'><p><strong>'The Kornilov affair was the main reason the Bolsheviks could seize power.' "
  "How far do you agree? (16 + 4)</strong></p>"
  "<p>YES: Kerensky armed the Red Guards, then looked weak when the threat collapsed; the Bolsheviks were armed "
  "and vindicated. NO: war collapse and land seizures made the slogans irresistible; the Soviets gave national "
  "organisation. Verdict: Kornilov handed them weapons and credibility — the slogans handed them the masses.</p></div>",
  ["Describe two features of the February Revolution.",
   "Give two features of dual power.",
   "What were the April Theses?",
   "Explain why the Provisional Government fell (two reasons, 4 marks).",
   "'Lenin was the main reason the Bolsheviks seized power.' How far do you agree? (16 + 4)"],
  ["Abdication 2 March 1917; dual power; Order No. 1.",
   "April Theses Apr 1917; July Days crushed; Kornilov Aug 1917; seizure 24–25 Oct; Sovnarkom.",
   "PG failures: stayed in WWI, delayed land reform, postponed elections."],
   [    "Bloody Sunday 22 Jan 1905 (Gapon).",
    "October Manifesto Oct 1905; Fundamental Laws Apr 1906.",
    "Stolypin: wager on the strong, hangings, 1907 franchise coup; Dumas 1-2 dissolved."],
  "February vs October table: spontaneous vs planned; no leaders vs Lenin; slogans; outcome. The PG\u2019s three "
  "fatal decisions (war, land, elections) explain the fall.",
  [("October was a mass rising", "It was a coup by Red Guards and sailors — mass support came through the Soviets"),
   ("Kerensky had no achievements", "He defeated the Kornilov threat — by arming his own destroyers")],
  ["Memorise the April Theses\u2019 three slogans.",
   "Dual power explains why there were TWO revolutions — always mention it."])))

PAGES.append(("R42-civil-war-war-communism-and-nep",
 "Civil War, War Communism and the NEP",
 "Reds vs Whites 1918–21, Trotsky's Red Army, War Communism, the Red Terror, Kronstadt 1921, famine, and Lenin's New Economic Policy.",
 topic(
  '<p><strong>Civil War (1918–21):</strong> Reds (centre, railways, industry) vs Whites (divided peripheries, '
  'foreign intervention) vs Greens (peasant armies). <strong>Trotsky\u2019s Red Army</strong>: conscription, '
  'ex-Tsarist officers under commissars, death penalty, armoured trains. <strong>War Communism</strong>: grain '
  'requisitioning, nationalisation, banned trade → <strong>famine 1921–22 (~5m dead)</strong>; <strong>Kronstadt '
  'rising (March 1921)</strong> — \u2018Soviets without Bolsheviks\u2019 — crushed. <strong>NEP (1921)</strong>: '
  'tax in kind, private trade legalised, state kept the \u2018commanding heights\u2019; Scissors Crisis 1923; '
  'Lenin\u2019s strokes 1922–24 → the succession.</p>',
  "<div class='example'><p><strong>'The Reds won the Civil War because of Trotsky's leadership.' How far do you "
  "agree? (16 + 4)</strong></p>"
  "<p>YES: built a ~5-million-man army, used ex-officers with commissars, defended the rail hub triangle. NO: "
  "Whites were geographically split and politically divided; peasants feared landowner restoration; Red Terror "
  "secured the rear; intervention was half-hearted. Verdict: Trotsky organised victory; geography and White "
  "disunity gifted it.</p></div>",
  ["Describe two features of War Communism.",
   "Give two reasons the Whites lost the Civil War.",
   "What happened at Kronstadt (1921)?",
   "Explain why Lenin introduced the NEP (two reasons, 4 marks).",
   "'War Communism was necessary to win the war.' How far do you agree? (16 + 4)"],
  ["Civil War 1918–21; Red Army ~5m; intervention by Britain, France, USA, Japan.",
   "War Communism: requisitioning, nationalisation, banned private trade.",
   "Kronstadt March 1921; NEP: tax in kind, NEPmen, kulaks; Scissors Crisis 1923.",
   "Famine 1921–22 (~5m deaths)."],
   [    "Abdication 2 Mar 1917; dual power; Order No. 1.",
    "April Theses Apr 1917; July Days; Kornilov Aug; seizure 24-25 Oct; Sovnarkom.",
    "PG failures: war, land, postponed elections."],
  "NEP = ideological retreat, economic recovery — the classic two-sided verdict. Reds-vs-Whites needs geography: "
  "the Red industrial centre vs four scattered White fronts.",
  [("The NEP was Stalin's policy", "Lenin\u2019s 1921 retreat — Stalin ended it with collectivisation in 1929"),
   ("The Whites were all Tsarists", "They included SRs and liberals — unity only in anti-Bolshevism")],
  ["Kronstadt = the loyalists\u2019 turn — quote \u2018Soviets without Bolsheviks\u2019.",
   "Civil War map argument: Red centre vs White peripheries."])))

PAGES.append(("R43-stalin-collectivisation-plans-and-terror",
 "Stalin: Collectivisation, Plans and Terror",
 "The succession struggle, collectivisation and the 1932–33 famine, the Five-Year Plans, the Great Purge and the cult of personality.",
 topic(
  '<p><strong>Succession:</strong> Stalin\u2019s party machine beat Trotsky (\u2018socialism in one country\u2019 vs '
  'permanent revolution); Lenin\u2019s Testament suppressed. <strong>Collectivisation (1929–33):</strong> kolkhozes, '
  'de-kulakisation, grain seized → <strong>famine 1932–33 (~5–7m dead)</strong>. <strong>Five-Year Plans:</strong> '
  'Magnitogorsk, Dnieper dam, Stakhanovites; consumer goods sacrificed. <strong>Terror:</strong> Kirov murdered '
  '(1934) → <strong>Great Purge (1936–38)</strong>: show trials (Zinoviev, Kamenev, Bukharin), ~750,000 executed, '
  'gulags, army officer corps beheaded. <strong>Cult of personality</strong>, Socialist Realism, Komsomol.</p>',
  "<div class='example'><p><strong>'Collectivisation failed.' How far do you agree? (16 + 4)</strong></p>"
  "<p>FAILED economically: output fell, famine killed millions, peasants slaughtered livestock. SUCCEEDED "
  "politically: state control of grain (exports funded industrialisation), the Party reached every village, kulaks "
  "eliminated as a class. Verdict: economic failure, political success.</p></div>",
  ["Describe two features of collectivisation.",
   "Give two features of the Five-Year Plans.",
   "What were the show trials?",
   "Explain why Stalin launched the Great Purge (two reasons, 4 marks).",
   "'The Five-Year Plans succeeded.' How far do you agree? (16 + 4)"],
  ["Collectivisation 1929–33; de-kulakisation; famine 1932–33 (Holodomor).",
   "Plans: Magnitogorsk, Dnieper dam, Stakhanovites 1935.",
   "Kirov 1934; show trials 1936–38; ~750,000 executed; gulags.",
   "Cult of personality; Pioneers/Komsomol; Socialist Realism."],
   [    "Civil War 1918-21; Red Army ~5m; foreign intervention.",
    "War Communism: requisitioning, nationalisation, trade banned.",
    "Kronstadt Mar 1921; NEP 1921: tax in kind, NEPmen; famine 1921-22 (~5m)."],
  "Stalin essays hold the \u2018transformation vs terror\u2019 tension: plans succeeded industrially while living "
  "standards fell — top answers keep both facts.",
  [("Collectivisation raised output", "It fell and caused famine — the aim was state control of grain"),
   ("The purges targeted only the Party", "Ordinary people, officers, engineers and minorities were most "
    "victims")],
  ["1934 Kirov → 1936–38 terror: memorise the sequence.",
   "Collectivisation = politics over economics — the ready-made two-sided verdict."])))

# ============================== COLD WAR (aqa, edexcel, ocr, eduqas) ==============================
PAGES.append(("C40-origins-of-the-cold-war-1945-49",
 "Origins of the Cold War 1945–49",
 "Yalta and Potsdam, ideological distrust, the Iron Curtain, Truman Doctrine and Marshall Plan, the Berlin blockade and airlift, and NATO.",
 topic(
  '<p><strong>Mistrust:</strong> the Second Front delay, Katyn, capitalism vs communism. <strong>Yalta (Feb 1945)</strong>: '
  'zones, UN, free elections promised for Poland. <strong>Potsdam (Jul–Aug 1945)</strong>: Truman (atomic) + Attlee; '
  'rows over reparations and borders. <strong>Soviet takeover of Eastern Europe 1945–48</strong> (Czechoslovak coup '
  '1948) → <strong>Iron Curtain speech (Fulton, Mar 1946)</strong>. <strong>Containment</strong>: Truman Doctrine '
  '(Mar 1947, Greece/Turkey) + <strong>Marshall Plan ($13bn)</strong> → Cominform (1947)/Comecon (1949). '
  '<strong>Berlin blockade and airlift (Jun 1948–May 1949)</strong>: currency reform, 278,000 flights; NATO (Apr '
  '1949); FRG/GDR founded 1949.</p>',
  "<div class='example'><p><strong>'The Berlin blockade was the first real crisis of the Cold War.' How far do "
  "you agree? (16 + 4)</strong></p>"
  "<p>YES: the first direct military stand-off; NATO followed directly. NO: ideology was already at war by 1947 "
  "(Doctrine, Marshall, Czechoslovak coup). Verdict: the first MILITARY crisis of a war that began politically "
  "in 1947.</p></div>",
  ["Describe two features of Yalta.",
   "Give two features of the Marshall Plan.",
   "Describe two features of the Berlin airlift.",
   "Explain why the USSR blockaded Berlin (two reasons, 4 marks).",
   "'The Truman Doctrine caused the Cold War.' How far do you agree? (16 + 4)"],
  ["Yalta Feb 1945; Potsdam Jul–Aug 1945; Fulton Mar 1946.",
   "Truman Doctrine Mar 1947; Marshall Plan $13bn; Cominform 1947; Comecon 1949.",
   "Blockade Jun 1948–May 1949; 278,000 flights; NATO Apr 1949; FRG/GDR 1949.",
   "Czechoslovak coup Feb 1948."],
   [    "Collectivisation 1929-33; famine 1932-33 (Holodomor).",
    "Plans: Magnitogorsk, Dnieper dam, Stakhanovites 1935.",
    "Kirov 1934; show trials 1936-38; ~750,000 executed; gulags."],
  "Origins essays: who was to blame? Argue actions-and-reactions (the spiral model) along the timeline "
  "Yalta → Potsdam → Fulton → Doctrine → Marshall → blockade.",
  [("The Marshall Plan was charity", "It was economic containment — aid tied to capitalist trade, openly "
    "anti-communist"),
   ("Berlin was deep in the West", "It lay 100 miles inside the Soviet zone — hence the blockade\u2019s leverage")],
  ["1947 = the ideological declaration year (Doctrine + Marshall + Cominform).",
   "Berlin 1948–49 = first stand-off; NATO = the consequence."])))

PAGES.append(("C41-hungary-1956-and-the-berlin-wall-1961",
 "Hungary 1956 and the Berlin Wall 1961",
 "De-Stalinisation, Nagy's reforms and the Soviet invasion, the West's inaction, Khrushchev's Berlin ultimatum and the Wall.",
 topic(
  '<p><strong>Hungary:</strong> Stalin died 1953; <strong>Khrushchev\u2019s Secret Speech (Feb 1956)</strong>; '
  '<strong>Nagy</strong> reformed, then announced leaving the Warsaw Pact (1 Nov) → <strong>Soviet invasion (4 Nov, '
  '~3,000 Hungarians + ~7,000 Soviet dead)</strong>; <strong>Nagy executed (1958)</strong>; the West did nothing '
  '(Suez distracted; Hungary was inside the Soviet sphere). <strong>Berlin:</strong> ultimatums (1958, 1961) failed; '
  '~3m East Germans fled west by 1961 → <strong>the Wall (13 Aug 1961)</strong> — barbed wire → concrete; escapers '
  'shot; Kennedy\u2019s \u2018Ich bin ein Berliner\u2019 (Jun 1963). The Wall ended the refugee crisis — '
  'propaganda disaster, practical victory.</p>',
  "<div class='example'><p><strong>'The West's response to Hungary 1956 proved the Cold War respected spheres of "
  "influence.' How far do you agree? (16 + 4)</strong></p>"
  "<p>YES: no military aid despite Radio Free Europe\u2019s encouragement; Suez overlap; Eastern Europe accepted "
  "as Soviet. NO: outrage, UN debates, refugee support. Verdict: spheres won — the test case for Czechoslovakia "
  "1968 and Poland 1980.</p></div>",
  ["Describe two features of the Hungarian uprising.",
   "Give two reasons the West did not help Hungary.",
   "Describe two features of the Berlin Wall.",
   "Explain why Khrushchev built the Wall (two reasons, 4 marks).",
   "'The Wall was a Soviet defeat.' How far do you agree? (16 + 4)"],
  ["Secret Speech Feb 1956; Nagy PM Oct 1956; invasion 4 Nov 1956; Nagy executed Jun 1958.",
   "~200,000 Hungarian refugees; ~3m East Germans fled by 1961.",
   "Wall 13 Aug 1961; ~140km; at least ~140 killed escaping.",
   "Kennedy Berlin speech Jun 1963."],
   [    "Yalta Feb 1945; Potsdam Jul-Aug 1945; Fulton Mar 1946.",
    "Truman Doctrine Mar 1947; Marshall Plan $13bn; Cominform 1947; Comecon 1949.",
    "Blockade Jun 1948-May 1949 (278,000 flights); NATO Apr 1949; FRG/GDR 1949."],
  "Both crises teach the same lesson: each superpower kept to its sphere. Contrast the Wall (practical fix) with "
  "the 1958 ultimatum (failed bluff): won the point, lost the propaganda.",
  [("The West sent troops to Hungary", "Only radio encouragement and refugee aid — deliberately no intervention"),
   ("The Wall stopped Western spies", "Its purpose was stopping East German EMIGRATION")],
  ["Hungary = the sphere-of-influence test case.",
   "The Wall = crisis ENDER, not starter — say why that mattered."])))

PAGES.append(("C42-cuban-missile-crisis-1962",
 "The Cuban Missile Crisis 1962",
 "Castro's revolution, the Bay of Pigs, Soviet missiles, the thirteen days, the naval quarantine, the secret Jupiter deal, and the hotline and Test Ban Treaty.",
 topic(
  '<p><strong>Cuba:</strong> Castro 1959 → nationalisations → embargo → Soviet alliance. <strong>Bay of Pigs (Apr '
  '1961)</strong>: CIA-backed invasion fiasco → full Soviet tilt. Khrushchev stationed <strong>R-12 missiles</strong> '
  'in Cuba (deterrence + bargaining + US Jupiters in Turkey). <strong>U-2 photos 14 Oct 1962</strong> → ExComm → '
  '<strong>naval quarantine (22 Oct)</strong>; <strong>Black Saturday (27 Oct)</strong>: U-2 shot down, submarine '
  'depth charges; <strong>secret deal</strong>: missiles out ↔ no invasion + Jupiters quietly removed from Turkey. '
  '<strong>Consequences:</strong> hotline (1963), Partial Test Ban Treaty (Aug 1963); Khrushchev ousted (1964); '
  'both sides learned brinkmanship\u2019s danger.</p>',
  "<div class='example'><p><strong>'Kennedy won the Cuban Missile Crisis.' How far do you agree? (16 + 4)</strong></p>"
  "<p>PUBLIC win: Soviet missiles left; quarantine held. PRIVATE Khrushchev win: no-invasion pledge + Jupiter "
  "removal (secret for decades). Verdict: settled, not won — that lesson produced the hotline and détente.</p></div>",
  ["Describe two features of the Bay of Pigs.",
   "Give two reasons Khrushchev placed missiles in Cuba.",
   "Describe two features of the naval quarantine.",
   "Explain why the crisis ended (two reasons, 4 marks).",
   "'The Cuban Missile Crisis made the Cold War safer.' How far do you agree? (16 + 4)"],
  ["Castro 1959; Bay of Pigs Apr 1961; U-2 photos 14 Oct 1962; quarantine 22 Oct 1962.",
   "Black Saturday 27 Oct 1962.",
   "Secret deal: Jupiters removed within months; no-invasion pledge.",
   "Hotline 1963; Test Ban Aug 1963; Khrushchev ousted Oct 1964."],
   [    "Secret Speech Feb 1956; invasion 4 Nov 1956; Nagy executed Jun 1958.",
    "~200,000 Hungarian refugees; ~3m East Germans fled by 1961.",
    "Wall 13 Aug 1961; ~140km; ~140+ killed escaping; Kennedy speech Jun 1963."],
  "ExComm structure: options (air strike vs blockade), the quarantine\u2019s legal cleverness, the secret trade. "
  "'Settled, not won' is the verdict line.",
  [("Kennedy's advisers all wanted war", "ExComm split — the blockade was the middle option over the Joint "
    "Chiefs\u2019 air strike"),
   ("Khrushchev backed down for nothing", "He got the Jupiter removal and a no-invasion pledge — secret but real")],
  ["Black Saturday detail shows how close it came — one well-told anecdote lifts a 16-marker.",
   "Consequences ARE the evaluation: hotline, test ban, détente logic."])))

PAGES.append(("C43-vietnam-detente-and-the-collapse",
 "Vietnam, Détente and the Collapse of the USSR",
 "Vietnam's cost to US credibility, SALT and Helsinki, the Afghan invasion, Reagan and SDI, Gorbachev's choices, the fall of the Wall and the USSR's dissolution.",
 topic(
  '<p><strong>Vietnam (1954–75):</strong> domino theory; Gulf of Tonkin (1964) → ~540,000 troops (1969); '
  '<strong>Tet (1968)</strong> turned opinion; withdrawal (1973), Saigon fell (1975). <strong>Détente:</strong> '
  '<strong>SALT I (1972)</strong>, <strong>Helsinki (1975)</strong>; ended by the <strong>Afghan invasion (Dec '
  '1979)</strong> → SALT II shelved, boycotts (1980/84), Reagan\u2019s build-up (\u2018evil empire\u2019, SDI 1983). '
  '<strong>Gorbachev:</strong> glasnost, perestroika, <strong>INF Treaty (Dec 1987)</strong> — first to DELETE a '
  'warhead class; unilateral cuts; <strong>1989</strong>: Poland June, Wall 9 Nov; <strong>1991</strong>: Warsaw '
  'Pact dissolved, failed coup, USSR dissolved (25 December).</p>',
  "Pact dissolved, failed coup, USSR dissolved (25 December).</p>",
  "<div class='example'><p><strong>'Gorbachev, not Reagan, ended the Cold War.' How far do you agree? (16 + 4)"
  "</strong></p>"
  "<p>REAGAN: the build-up strained the Soviet economy; SDI raised stakes. GORBACHEV: chose reform over "
  "repression — left Afghanistan, accepted the Wall\u2019s fall, refused to shoot. Verdict: Reagan raised the "
  "price; Gorbachev paid it willingly — \u2018he ended the Cold War by refusing to keep it\u2019.</p></div>",
  ["Describe two features of the Tet Offensive.",
   "Give two features of détente (SALT I or Helsinki).",
   "Describe two features of the Soviet-Afghan war.",
   "Explain why the Berlin Wall fell in 1989 (two reasons, 4 marks).",
   "'Reagan's SDI won the Cold War.' How far do you agree? (16 + 4)"],
  ["Gulf of Tonkin 1964; Tet 1968; Paris Accords 1973; Saigon 1975.",
   "SALT I 1972; Helsinki 1975; Afghanistan Dec 1979; SDI 1983; INF Dec 1987.",
   "1989: Poland June, Wall 9 Nov; 1991: coup Aug, dissolution 25 Dec.",
   "Gorbachev: glasnost (openness), perestroika (restructuring)."],
  "End-of-Cold-War essays layer causes: long (economy), short (Gorbachev\u2019s choices), immediate (1989 "
  "revolutions). Afghanistan = \u2018Soviet Vietnam\u2019 — the analogy writes itself.",
  [("The USSR collapsed militarily", "The army was intact — the economy and legitimacy collapsed"),
   ("Reagan forced every concession", "Gorbachev outbid his own generals; many cuts were unilateral")],
  ["The 1961 Wall vs the 1989 Wall speech = a ready-made change-over-time pair.",
   "INF 1987 = first DELETED class — contrast with SALT\u2019s limits."])))

if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else 'topics/history/aqa'
    only = None
    if len(sys.argv) > 2:
        only = set(sys.argv[2].split(','))
    for slug, title, desc, body in PAGES:
        if only and slug.split('-')[0] not in only:
            continue
        html = build(slug, title, desc, body)
        open(f'{out}/{slug}.html', 'w', encoding='utf-8').write(html)
        print('wrote', f'{out}/{slug}.html', len(html), 'bytes')
