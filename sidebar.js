// GCSE Revise - Sidebar Navigation
(function() {
var SUBJ_DATA = [
{id:'mathematics',name:'Maths'},{id:'english-language',name:'English Lang'},
{id:'english-literature',name:'English Lit'},{id:'combined-science',name:'Combined Sci'},
{id:'biology',name:'Biology'},{id:'chemistry',name:'Chemistry'},
{id:'physics',name:'Physics'},{id:'computer-science',name:'Comp Sci'},
{id:'geography',name:'Geography'},{id:'history',name:'History'},
{id:'religious-studies',name:'Rel Studies'},{id:'french',name:'French'},
{id:'german',name:'German'},{id:'spanish',name:'Spanish'},
{id:'art-and-design',name:'Art & Design'},{id:'music',name:'Music'},
{id:'drama',name:'Drama'},{id:'design-and-technology',name:'D&T'},
{id:'pe',name:'PE'},{id:'business',name:'Business'},
{id:'economics',name:'Economics'},{id:'psychology',name:'Psychology'},
{id:'sociology',name:'Sociology'},{id:'citizenship-studies',name:'Citizenship'},
{id:'media-studies',name:'Media'},{id:'food-preparation-nutrition',name:'Food & Nutrition'},
{id:'latin',name:'Latin'},{id:'astronomy',name:'Astronomy'},
{id:'geology',name:'Geology'},{id:'ancient-history',name:'Ancient Hist'},
{id:'classical-civilisation',name:'Class Civ'},{id:'law',name:'Law'},
{id:'dance',name:'Dance'},{id:'film-studies',name:'Film'},
{id:'electronics',name:'Electronics'},{id:'engineering',name:'Engineering'},
{id:'statistics',name:'Statistics'}
];

var path = location.pathname;
var currentPage = path.split('/').pop().replace('.html','');
var isTopicPage = path.indexOf('/topics/') !== -1;
var isLandingPage = !isTopicPage && currentPage !== 'index' && currentPage !== '';
if (currentPage === 'index' || currentPage === '') return;

var nav = document.createElement('nav');
nav.className = 'sidebar';
nav.id = 'sidebar-nav';

if (isLandingPage) {
nav.innerHTML = '<h3>Subjects</h3><ul>' +
SUBJ_DATA.map(function(s) {
var cls = s.id === currentPage ? ' class="active"' : '';
return '<li><a href="' + s.id + '.html"' + cls + '>' + s.name + '</a></li>';
}).join('') + '</ul>';
} else if (isTopicPage) {
var segs = path.split('/');
var subjectSlug = '';
// Extract a subject slug (e.g. 'combined-science') from a link href.
// Strict: only match subject.html links, skipping home links (./ ../../),
// fragment links (#subjects), and index links.
function subjectFromHref(href) {
if (!href) return '';
if (href.indexOf('#') !== -1) return '';
if (href.indexOf('index') !== -1) return '';
if (/(?:^|\/)\.?$/.test(href)) return '';
var m = /([a-z][a-z0-9-]+)\.html$/.exec(href);
return m ? m[1] : '';
}
var bcLinks = document.querySelectorAll('.breadcrumb a');
for (var i = 0; i < bcLinks.length; i++) {
subjectSlug = subjectFromHref(bcLinks[i].getAttribute('href') || '');
if (subjectSlug) break;
}
// Fallback: extract subject slug from the nav link in the header
if (!subjectSlug) {
var navLinks = document.querySelectorAll('header .nav a');
for (var j = 0; j < navLinks.length; j++) {
subjectSlug = subjectFromHref(navLinks[j].getAttribute('href') || '');
if (subjectSlug) break;
}
}
var prefix = '../../';
var landingHref = prefix + subjectSlug + '.html';
var currentTopicFile = segs[segs.length - 1];

if (!subjectSlug) {
nav.innerHTML = '<h3>Subjects</h3><ul>' +
SUBJ_DATA.map(function(s) {
return '<li><a href="' + s.id + '.html">' + s.name + '</a></li>';
}).join('') + '</ul>';
} else {
nav.innerHTML = '<h3>Topics</h3><ul id="sidebar-topics"><li><a href="' + landingHref + '">&larr; ' + (subjectSlug.replace(/-/g,' ')) + '</a></li></ul>';

fetch(landingHref).then(function(r) { return r.text(); }).then(function(html) {
var parser = new DOMParser();
var doc = parser.parseFromString(html, 'text/html');
var cards = doc.querySelectorAll('a.topic-card');
var ul = document.getElementById('sidebar-topics');
if (!ul) return;
var items = '<li><a href="' + landingHref + '">&larr; ' + (subjectSlug.replace(/-/g,' ')) + '</a></li>';
cards.forEach(function(card) {
var href = card.getAttribute('href') || '';
var name = card.querySelector('.topic-name');
var id = card.querySelector('.topic-id');
var label = (id ? id.textContent.trim() + ': ' : '') + (name ? name.textContent.trim() : '');
var fullHref = prefix + href;
var isActive = href.indexOf(currentTopicFile) !== -1;
var cls = isActive ? ' class="active"' : '';
items += '<li><a href="' + fullHref + '"' + cls + '>' + label + '</a></li>';
});
ul.innerHTML = items;
}).catch(function(err) { console.error('Sidebar fetch failed:', landingHref, err); });
}
} else {
nav.innerHTML = '<h3>Subjects</h3><ul>' +
SUBJ_DATA.map(function(s) {
return '<li><a href="' + s.id + '.html">' + s.name + '</a></li>';
}).join('') + '</ul>';
}

// Append sidebar to body (it's position:fixed, so it doesn't need to be inside main)
document.body.appendChild(nav);

// Right-side ad rail: create if missing, fill if empty (generator emits empty asides on subject pages)
var adRail = document.querySelector('aside.ad-right');
if (!adRail) {
adRail = document.createElement('aside');
adRail.className = 'ad-right';
adRail.id = 'ad-rail-right';
document.body.appendChild(adRail);
}
if (!adRail.innerHTML.trim()) {
adRail.innerHTML = '<a href="https://join.fastmail.com/0d63b2d52105" class="affiliate-card" target="_blank" rel="nofollow noopener"><div class="affiliate-card-title">Fastmail — Private Email</div><div class="affiliate-card-desc">Privacy-first email with no ads and no tracking</div><div class="affiliate-card-store">fastmail.com</div></a><a href="https://www.dynadot.com/?ref=scottrix" class="affiliate-card" target="_blank" rel="nofollow noopener"><div class="affiliate-card-title">Dynadot — Domain Registration →</div><div class="affiliate-card-desc">Register or transfer domains with free SSL and affordable pricing</div><div class="affiliate-card-store">dynadot.com</div></a><a href="https://zen.mention-me.com/m/ol/yv3qsjix-scott-harrison" class="affiliate-card" target="_blank" rel="nofollow noopener"><div class="affiliate-card-title">Zen Internet — UK Broadband →</div><div class="affiliate-card-desc">Award-winning UK broadband with no data caps and great customer service</div><div class="affiliate-card-store">zen.co.uk</div></a>';
}

// Mobile toggle
var btn = document.createElement('button');
btn.className = 'sidebar-toggle';
btn.textContent = '\u2630';
btn.id = 'sidebar-toggle-btn';
btn.setAttribute('aria-label', 'Toggle sidebar');
btn.addEventListener('click', function() {
nav.classList.toggle('open');
btn.textContent = nav.classList.contains('open') ? '\u2715' : '\u2630';
});
document.body.appendChild(btn);

document.addEventListener('click', function(e) {
if (nav.classList.contains('open') && !nav.contains(e.target) && e.target !== btn) {
nav.classList.remove('open');
btn.textContent = '\u2630';
}
});

})();
