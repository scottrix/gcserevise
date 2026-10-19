#!/usr/bin/env python3
"""De-couple the two sites: no page may reference the other domain.

- strips the canonical-host-redirect script
- converts absolute www.scottrix.co.uk / scottrix.github.io URLs in canonical,
  og:url, share buttons and data-url attributes to ORIGIN-RELATIVE paths
- inserts a runtime absolutiser so each site self-references its own host
Idempotent.
"""
import glob
import os
import re
import sys

ABS = re.compile(r'https://(?:www\.scottrix\.co\.uk|scottrix\.github\.io)(?=/)')
REDIRECT_RE = re.compile(r'\n?<script>/\* canonical-host-redirect \*/.*?</script>', re.DOTALL)
ORIGIN_JS = ('<script>/* site-origin */(function(){var o=location.origin;'
             'var c=document.querySelector(\'link[rel="canonical"]\');'
             'if(c&&c.getAttribute("href").charAt(0)==="/")c.href=o+c.getAttribute("href");'
             'var g=document.querySelector(\'meta[property="og:url"]\');'
             'if(g&&g.getAttribute("content").charAt(0)==="/")g.content=o+g.getAttribute("content");'
             'document.querySelectorAll(\'a[href^="/"],[data-url^="/"]\').forEach(function(el){'
             'var k=el.hasAttribute("data-url")?"data-url":"href";'
             'var v=el.getAttribute(k);'
             'if(v.charAt(0)==="/"&&v.charAt(1)!=="/")el.setAttribute(k,o+v);});})();</script>')


def transform(h):
    orig = h
    h = REDIRECT_RE.sub('', h)
    h = re.sub(r'\n{3,}', '\n\n', h)
    if '/* site-origin */' not in h:
        m = re.search(r'<link rel="canonical" href="[^"]*">', h)
        if not m:
            m = re.search(r'</title>', h)
        if m:
            h = h[:m.end()] + '\n' + ORIGIN_JS + h[m.end():]
    h = ABS.sub('', h)
    return h


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    n = 0
    for f in glob.glob(os.path.join(root, '*.html')) + glob.glob(os.path.join(root, 'topics', '**', '*.html'), recursive=True):
        h = open(f, encoding='utf-8', errors='replace').read()
        if 'http-equiv="refresh"' in h[:600]:
            continue
        h2 = transform(h)
        if h2 != h:
            open(f, 'w', encoding='utf-8').write(h2)
            n += 1
    print(f'de-coupled: {n} pages')


if __name__ == '__main__':
    main()
