#!/usr/bin/env python3
"""Convert origin-relative URLs to STATIC absolute URLs for single-domain deployments.
Usage: python3 absolutise.py <root> <domain>"""
import glob
import os
import re
import sys

domain = sys.argv[2]
root = sys.argv[1]
ORIGIN_RE = re.compile(r'<script>/\* site-origin \*/.*?</script>\n?', re.DOTALL)
BASE = 'https://' + domain

n = 0
for f in glob.glob(os.path.join(root, '*.html')) + glob.glob(os.path.join(root, 'topics', '**', '*.html'), recursive=True):
    h = open(f, encoding='utf-8', errors='replace').read()
    if 'http-equiv="refresh"' in h[:600]:
        continue
    if '/* site-origin */' not in h and 'href="/gcserevise' not in h:
        continue
    h2 = ORIGIN_RE.sub('', h)
    h2 = re.sub(r'(rel="canonical" href=")/(gcserevise/)', r'\1' + BASE + r'/\2', h2)
    h2 = re.sub(r'(property="og:url" content=")/(gcserevise/)', r'\1' + BASE + r'/\2', h2)
    h2 = re.sub(r'(sharer\.php\?u=)/(gcserevise/)', r'\1' + BASE + r'/\2', h2)
    h2 = re.sub(r'(intent/tweet\?url=)/(gcserevise/)', r'\1' + BASE + r'/\2', h2)
    h2 = re.sub(r'(wa\.me/\?text=[^"]*%20)/(gcserevise/)', r'\1' + BASE + r'/\2', h2)
    h2 = re.sub(r'(share-offsite/\?url=)/(gcserevise/)', r'\1' + BASE + r'/\2', h2)
    h2 = re.sub(r'(data-url=")/(gcserevise/)', r'\1' + BASE + r'/\2', h2)
    if h2 != h:
        open(f, 'w', encoding='utf-8').write(h2)
        n += 1
print(f'absolutised to {domain}: {n} pages')
