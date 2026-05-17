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
var bcLinks = document.querySelectorAll('.breadcrumb a');
for (var i = 0; i < bcLinks.length; i++) {
var href = bcLinks[i].getAttribute('href') || '';
if (href.indexOf('index.html') === -1 && href.indexOf('#') === -1) {
subjectSlug = href.replace(/^..\/..\/?/, '').replace(/\.html$/, '');
break;
}
}
// Fallback: extract subject slug from the nav link in the header
if (!subjectSlug) {
var navLinks = document.querySelectorAll('header .nav a');
for (var j = 0; j < navLinks.length; j++) {
var nhref = navLinks[j].getAttribute('href') || '';
if (nhref.indexOf('../../') === 0 && nhref.indexOf('index') === -1) {
subjectSlug = nhref.replace(/^..\/..\/?/, '').replace(/\.html$/, '');
break;
}
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

// Right-side ad rail
var adRail = document.createElement('aside');
adRail.className = 'ad-right';
adRail.id = 'ad-rail-right';
adRail.innerHTML = '<div class="ad-unit" id="ad-right-top"><ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-5741314833802600" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins></div><div class="ad-unit" id="ad-right-mid"></div>';
document.body.appendChild(adRail);

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

// Push AdSense ads into right rail
try {
var adIns = document.querySelector('#ad-right-top ins.adsbygoogle');
if (adIns && window.adsbygoogle) {
(adsbygoogle = window.adsbygoogle || []).push({});
}
} catch(e) {}
})();
