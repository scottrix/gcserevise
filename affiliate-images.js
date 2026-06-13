(function() {
  var ASIN_RE = /\/dp\/([A-Z0-9]{10})/i;
  var FASTMAIL_RE = /join\.fastmail\.com/;
  var IMG_BASE = 'https://images-eu.ssl-images-amazon.com/images/P/';
  var IMG_SUFFIX = '.02._SL160_.jpg';

  function extractAsin(href) {
    var m = href && href.match(ASIN_RE);
    return m ? m[1] : null;
  }

  function addProductImages() {
    var cards = document.querySelectorAll('.affiliate-card');
    for (var i = 0; i < cards.length; i++) {
      var card = cards[i];
      if (card.querySelector('.affiliate-card-img')) continue;

      var href = card.getAttribute('href') || '';
      var asin = extractAsin(href);
      if (!asin) continue;

      var imgDiv = document.createElement('div');
      imgDiv.className = 'affiliate-card-img';

      var img = document.createElement('img');
      img.alt = 'Product image';
      img.loading = 'lazy';
      img.src = IMG_BASE + asin + IMG_SUFFIX;
      img.onerror = function() {
        this.parentNode.className = 'affiliate-card-img affiliate-card-img-fallback';
        this.removeAttribute('src');
      };

      imgDiv.appendChild(img);
      card.insertBefore(imgDiv, card.firstChild);
    }
  }

  function addFastmailIcons() {
    var cards = document.querySelectorAll('.affiliate-card');
    for (var i = 0; i < cards.length; i++) {
      var card = cards[i];
      if (!FASTMAIL_RE.test(card.href)) continue;
      if (card.querySelector('.affiliate-card-icon')) continue;

      card.setAttribute('data-fastmail', '');

      var icon = document.createElement('div');
      icon.className = 'affiliate-card-icon';
      icon.textContent = '\u2709';
      card.insertBefore(icon, card.firstChild);

      var tm = document.createElement('div');
      tm.className = 'fastmail-trademark';
      tm.textContent = 'Fastmail\u00AE is a trademark of Fastmail Pty Ltd';
      card.appendChild(tm);
    }
  }

  function init() {
    addProductImages();
    addFastmailIcons();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
