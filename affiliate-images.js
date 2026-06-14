(function() {
  var FASTMAIL_RE = /join\.fastmail\.com/;

  function getIconPath() {
    var depth = 0;
    var path = window.location.pathname;
    var parts = path.split('/').filter(Boolean);
    if (parts.length > 2) depth = 2;
    else if (parts.length > 1) depth = 1;
    var prefix = '';
    for (var i = 0; i < depth; i++) prefix += '../';
    return prefix + 'fastmail_icon.svg';
  }

  function addFastmailIcons() {
    var cards = document.querySelectorAll('.affiliate-card');
    var iconPath = getIconPath();
    for (var i = 0; i < cards.length; i++) {
      var card = cards[i];
      if (!FASTMAIL_RE.test(card.href)) continue;
      if (card.querySelector('.affiliate-card-icon')) continue;

      card.setAttribute('data-fastmail', '');

      var icon = document.createElement('img');
      icon.className = 'affiliate-card-icon';
      icon.src = iconPath;
      icon.alt = 'Fastmail';
      icon.style.width = '32px';
      icon.style.height = '32px';
      card.insertBefore(icon, card.firstChild);

      var tm = document.createElement('div');
      tm.className = 'fastmail-trademark';
      tm.textContent = 'Fastmail\u00AE is a trademark of Fastmail Pty Ltd';
      card.appendChild(tm);
    }
  }

  function init() {
    addFastmailIcons();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
