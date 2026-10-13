#!/usr/bin/env python3
"""
sitemap_gen.py - Per-repo sitemap.xml generator with per-URL lastmod derived
from each file's last git commit date.

Designed for the 4 scottrix.github.io subsite repos. Auto-detects which repo
it is running in by inspecting the current directory's git remote URL.

Per-repo behaviour:
- scottrix.github.io (root): writes sitemap-1.xml with root URLs; updates
  sitemap.xml (sitemapindex) cross-referencing the 4 child sitemaps with
  today's date as the sitemap-level lastmod.
- devtools/ : writes sitemap.xml with single entry (/devtools/).
- fintools/ : writes sitemap.xml with single entry (/fintools/).
- gcserevise/: writes sitemap.xml with ~1,254 entries (home, subjects,
  topics, privacy) preserving the existing priority scheme (1.0/0.8/0.7/0.3).

Idempotent: if the generated content matches the existing file, the file
is left untouched so `git diff` stays clean.

Usage:
    python3 sitemap_gen.py          # write sitemap(s) for current repo
    python3 sitemap_gen.py --check # exit code 0 if up-to-date, 1 if stale
"""
import argparse
import subprocess
import sys
from pathlib import Path

BASE_URL = 'https://www.scottrix.co.uk'
TODAY = subprocess.check_output(['date', '-u', '+%Y-%m-%d']).decode().strip()


def git_last_date(filepath, repo_root):
    """Return the YYYY-MM-DD of the last commit touching filepath."""
    try:
        out = subprocess.check_output(
            ['git', 'log', '-1', '--format=%ad', '--date=short', '--', filepath],
            cwd=repo_root, stderr=subprocess.DEVNULL,
        )
        return out.decode().strip() or TODAY
    except subprocess.CalledProcessError:
        return TODAY


def is_skippable(p, repo_root):
    """Skip verification files, dotfiles, pycache, redirect stubs."""
    try:
        if 'http-equiv="refresh"' in open(p, encoding="utf-8", errors="replace").read(600):
            return True
    except OSError:
        pass
    name = p.name
    if name.startswith('google') and name.endswith('.html'):
        return True
    if name == 'BingSiteAuth.xml':
        return True
    rel = p.relative_to(repo_root).as_posix()
    if rel.startswith('.') or '/__pycache__/' in rel or rel.endswith('.pyc'):
        return True
    # Skip IndexNow key file and other non-HTML root text files
    return False


def enumerate_html(repo_root):
    """Yield (Path, public_url, priority, changefreq_or_None) per HTML file."""
    # Detect repo kind by directory name
    repo_name = Path(repo_root).resolve().name
    subpath_map = {
        'scottrix.github.io': '',
        'devtools':           '/devtools',
        'fintools':           '/fintools',
        'gcserevise':         '/gcserevise',
    }
    if repo_name not in subpath_map:
        raise SystemExit(f'Unknown repo: {repo_name}')
    subpath = subpath_map[repo_name]
    is_gcserevise = (repo_name == 'gcserevise')
    is_root = (repo_name == 'scottrix.github.io')

    files = sorted(p for p in repo_root.rglob('*.html') if not is_skippable(p, repo_root))
    # Sort by priority (desc) then URL (asc): home first, privacy last.
    prio_order = {'1.0': 0, '0.8': 1, '0.7': 2, '0.3': 3}
    collected = []
    for p in files:
        rel = p.relative_to(repo_root).as_posix()
        # index.html -> directory URL (no /index.html in URL)
        if rel == 'index.html':
            public = f'{BASE_URL}{subpath}/'
        elif rel.endswith('/index.html'):
            public = f'{BASE_URL}{subpath}/{rel[:-len("/index.html")]}/'
        else:
            public = f'{BASE_URL}{subpath}/{rel}'

        # Determine priority
        if is_gcserevise:
            if rel == 'index.html':
                prio = '1.0'
            elif rel == 'privacy.html':
                prio = '0.3'
            elif rel.startswith('topics/'):
                prio = '0.7'
            else:
                prio = '0.8'  # subject pages
            cf = None
        elif is_root:
            if rel == 'index.html':
                prio = '1.0'
            elif rel == 'privacy.html':
                prio = '0.3'
            else:
                prio = '0.8'
            cf = None
        else:
            # devtools / fintools: home page 1.0, privacy 0.3
            if rel == 'index.html':
                prio = '1.0'
            elif rel == 'privacy.html':
                prio = '0.3'
            else:
                prio = '0.8'
            cf = 'weekly'

        collected.append((prio_order.get(prio, 9), public, p, prio, cf))

    # Stable sort: by priority order then URL asc
    collected.sort(key=lambda e: (e[0], e[1]))
    for _, public, p, prio, cf in collected:
        yield p, public, prio, cf


def render_urlset(entries, indent='  ', changefreq=False):
    """Render a <urlset> from entries=[(url, lastmod, priority, changefreq_or_None)].

    indent: 2-space (gcserevise/root) or 4-space (devtools/fintools).
    changefreq: if True, include <changefreq> tag (devtools/fintools use this).
    """
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    inner = indent + '  '
    for url, lastmod, prio, cf in entries:
        lines.append(f'{indent}<url>')
        lines.append(f'{inner}<loc>{url}</loc>')
        lines.append(f'{inner}<lastmod>{lastmod}</lastmod>')
        if changefreq and cf:
            lines.append(f'{inner}<changefreq>{cf}</changefreq>')
        lines.append(f'{inner}<priority>{prio}</priority>')
        lines.append(f'{indent}</url>')
    lines.append('</urlset>')
    return '\n'.join(lines) + '\n'


def render_sitemapindex(entries):
    """Render a <sitemapindex> from entries=[(loc, lastmod)]."""
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod in entries:
        lines.append('  <sitemap>')
        lines.append(f'    <loc>{loc}</loc>')
        lines.append(f'    <lastmod>{lastmod}</lastmod>')
        lines.append('  </sitemap>')
    lines.append('</sitemapindex>')
    return '\n'.join(lines) + '\n'


def generate_for_repo(repo_root, check_only=False):
    repo_root = Path(repo_root).resolve()
    repo_name = repo_root.name
    plan = []  # (path, new_content)

    if repo_name == 'scottrix.github.io':
        # Root repo: regenerate sitemap-1.xml + sitemap.xml (sitemapindex)
        entries = []
        for p, public, prio, cf in enumerate_html(repo_root):
            lm = git_last_date(p, repo_root)
            entries.append((public, lm, prio, cf))
        plan.append((repo_root / 'sitemap-1.xml',
                     render_urlset(entries, indent='  ', changefreq=False)))

        # sitemapindex
        sub_lastmod = TODAY
        idx = [
            (f'{BASE_URL}/sitemap-1.xml', sub_lastmod),
            (f'{BASE_URL}/devtools/sitemap.xml', sub_lastmod),
            (f'{BASE_URL}/fintools/sitemap.xml', sub_lastmod),
            (f'{BASE_URL}/gcserevise/sitemap.xml', sub_lastmod),
        ]
        plan.append((repo_root / 'sitemap.xml', render_sitemapindex(idx)))

    elif repo_name in ('devtools', 'fintools'):
        # Single-URL repos with 4-space indentation + changefreq=weekly
        entries = []
        for p, public, prio, cf in enumerate_html(repo_root):
            lm = git_last_date(p, repo_root)
            entries.append((public, lm, prio, cf))
        plan.append((repo_root / 'sitemap.xml',
                     render_urlset(entries, indent='    ', changefreq=True)))

    elif repo_name == 'gcserevise':
        entries = []
        for p, public, prio, cf in enumerate_html(repo_root):
            lm = git_last_date(p, repo_root)
            entries.append((public, lm, prio, cf))
        plan.append((repo_root / 'sitemap.xml',
                     render_urlset(entries, indent='  ', changefreq=False)))

    changed = 0
    for path, content in plan:
        existing = ''
        if path.exists():
            existing = path.read_text(encoding='utf-8')
        if existing == content:
            print(f'  {path.name}: up-to-date')
            continue
        if check_only:
            print(f'  {path.name}: STALE (would update)')
            changed += 1
            continue
        path.write_text(content, encoding='utf-8')
        print(f'  {path.name}: UPDATED ({len(content.splitlines())} lines)')
        changed += 1
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true',
                    help='Exit 0 if all sitemaps are up-to-date, 1 otherwise.')
    ap.add_argument('--repo', default='.',
                    help='Repo root directory (default: current dir).')
    args = ap.parse_args()

    print(f'Today (UTC): {TODAY}')
    print(f'Repo:        {Path(args.repo).resolve().name}')
    print()
    changed = generate_for_repo(args.repo, check_only=args.check)
    if args.check:
        sys.exit(0 if changed == 0 else 1)


if __name__ == '__main__':
    main()
