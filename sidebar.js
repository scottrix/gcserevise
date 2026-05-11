// GCSE Revise - Sidebar Navigation
(function() {
  const SUBJ_DATA = [
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

  var currentPage = location.pathname.split('/').pop().replace('.html','');
  var isTopicPage = location.pathname.indexOf('/topics/') !== -1;
  var isLandingPage = !isTopicPage && currentPage !== 'index' && currentPage !== '';

  var nav = document.createElement('nav');
  nav.className = 'sidebar';
  nav.id = 'sidebar-nav';

  if (isLandingPage) {
    // Subject list sidebar
    nav.innerHTML = '<h3>Subjects</h3><ul>' +
      SUBJ_DATA.map(function(s) {
        var cls = s.id === currentPage ? ' class="active"' : '';
        return '<li><a href="' + s.id + '.html"' + cls + '>' + s.name + '</a></li>';
      }).join('') + '</ul>';
  } else if (isTopicPage) {
    // Topic list sidebar - extract from landing page topic cards
    var segs = location.pathname.split('/');
    var topicsIdx = segs.indexOf('topics');
    var subjectSlug = '';
    // Find the subject page by looking at breadcrumb
    var bcLinks = document.querySelectorAll('.breadcrumb a');
    for (var i = 0; i < bcLinks.length; i++) {
      var href = bcLinks[i].getAttribute('href') || '';
      if (href.indexOf('index.html') === -1 && href.indexOf('#') === -1) {
        subjectSlug = href.replace(/\.html$/, '').replace(/^..\/..\/?/, '');
        break;
      }
    }

    var topicItems = [];
    var topicCards = document.querySelectorAll('a.topic-card');
    // If we're on a topic page, we need to fetch topic links from the landing page
    // Instead, we'll build from the landing page link in the breadcrumb
    var prefix = isTopicPage ? '../../' : '';
    var landingHref = prefix + subjectSlug + '.html';

    // Build topic list by fetching the landing page
    nav.innerHTML = '<h3>Topics</h3><ul id="sidebar-topics"><li><a href="' + landingHref + '">← Back to ' + (subjectSlug.replace(/-/g,' ')) + '</a></li></ul>';

    // Highlight current topic in sidebar after fetch
    var currentTopicFile = segs[segs.length - 1];

    // Fetch landing page to get topic list
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
        // Adjust href for topic pages (they're in topics/ subdir)
        var fullHref = prefix + href;
        var isActive = href.indexOf(currentTopicFile) !== -1;
        var cls = isActive ? ' class="active"' : '';
        items += '<li><a href="' + fullHref + '"' + cls + '>' + label + '</a></li>';
      });
      ul.innerHTML = items;
    }).catch(function() {});
  } else {
    // Index page - subject list
    nav.innerHTML = '<h3>Subjects</h3><ul>' +
      SUBJ_DATA.map(function(s) {
        return '<li><a href="' + s.id + '.html">' + s.name + '</a></li>';
      }).join('') + '</ul>';
  }

  // Wrap existing main content
  var main = document.querySelector('main.topic-content');
  if (!main) return;

  var wrapper = document.createElement('div');
  wrapper.className = 'content-with-sidebar';
  while (main.firstChild) {
    wrapper.appendChild(main.firstChild);
  }
  main.appendChild(nav);
  main.appendChild(wrapper);

  // Mobile toggle button
  var btn = document.createElement('button');
  btn.className = 'sidebar-toggle';
  btn.textContent = '☰';
  btn.id = 'sidebar-toggle-btn';
  btn.setAttribute('aria-label', 'Toggle sidebar');
  btn.addEventListener('click', function() {
    nav.classList.toggle('open');
    btn.textContent = nav.classList.contains('open') ? '✕' : '☰';
  });
  document.body.appendChild(btn);

  // Close sidebar on overlay click (mobile)
  document.addEventListener('click', function(e) {
    if (nav.classList.contains('open') && !nav.contains(e.target) && e.target !== btn) {
      nav.classList.remove('open');
      btn.textContent = '☰';
    }
  });
})();
