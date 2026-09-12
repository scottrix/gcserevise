#!/usr/bin/env python3
"""Generate GCSE subject landing pages with board/tier selectors for board-specific architecture"""

import json
import re
from pathlib import Path

BASE = Path('/home/scott/src')
TOPICS_BASE = BASE / 'gcserevise' / 'topics'

# Load GCSE subjects
with open(BASE / 'gcserevise' / 'subjects.json', 'r') as f:
    data = json.load(f)

subjects = data['subjects']

# Subject -> category mapping (from subjects.json)
CATEGORIES = {s['id']: s['category'] for s in subjects}


def short_ref(stem: str) -> str:
    """Short badge code from a topic filename stem: RS1, B10, 3D1, or first word."""
    m = re.match(r'^([A-Za-z]+\d+[A-Za-z0-9]*)[-_]', stem)
    if m:
        return m.group(1).upper()
    seg = re.split(r'[-_]', stem, maxsplit=1)[0]
    return seg.upper() if any(c.isdigit() for c in seg) else seg.capitalize()


def get_topic_title(topic_file: str, topic_dir: str) -> str:
    """Extract readable title from topic filename"""
    name = topic_file.replace('.html', '')
    name = re.sub(r'^[A-Za-z]+\d+[A-Za-z0-9]*[-_]', '', name)
    return name.replace('-', ' ').replace('_', ' ').title()


def get_board_display_name(board: str) -> str:
    """Get display name for exam board"""
    names = {
        'AQA': 'AQA',
        'Edexcel': 'Pearson Edexcel',
        'OCR': 'OCR',
        'Eduqas': 'Eduqas',
        'CCEA': 'CCEA'
    }
    return names.get(board, board)


def generate_subject_page(subject_id: str, subject_name: str, category: str, boards: list, topic_dirs: dict, has_tiers: bool, tiers: list):
    """Generate a subject landing page with board-specific navigation"""
    
    # Board selector
    board_options = ''.join(f'<option value="{b.lower()}">{get_board_display_name(b)}</option>' for b in boards)
    
    tier_options = ""
    if has_tiers:
        tier_options = ''.join(f'<option value="{t.lower()}">{t}</option>' for t in tiers)
    
    selector_bar = f'''<div class="selector-bar">
  <div class="selector-group">
    <label for="board-select">Exam Board: </label>
    <select id="board-select" onchange="updateSubjectUrl()">
      {board_options}
    </select>
  </div>
  {'<div class="selector-group"><label for="tier-select">Tier: </label><select id="tier-select" onchange="updateSubjectUrl()">' + tier_options + '</select></div>' if has_tiers else ''}
</div>'''

    # Build topics grid - show topics from first board's directories as reference
    first_board = boards[0] if boards else None
    first_board_dirs = topic_dirs.get(first_board, []) if first_board else []
    
    sections_html = []
    for topic_dir_name in sorted(first_board_dirs):
        topic_dir_path = TOPICS_BASE / topic_dir_name
        if not topic_dir_path.exists():
            continue
        
        topic_files = sorted(topic_dir_path.glob('*.html'))
        if not topic_files:
            continue
        
        # Group by strand (first word of topic_dir)
        strand = topic_dir_name.split('-')[0].title() if '-' in topic_dir_name else subject_name
        
        cards = []
        for topic_file in topic_files:
            topic_id = short_ref(topic_file.stem)
            title = get_topic_title(topic_file.name, topic_dir_name)
            
            # Build board-specific link - link to first board's version
            # (with default tier for tiered subjects so links work without JS).
            # JavaScript will update based on selector
            default_tier = ('/' + tiers[0].lower()) if has_tiers and tiers else ''
            cards.append(f'''
      <a href="topics/{subject_id}/{first_board.lower()}{default_tier}/{topic_file.name}" class="topic-card">
        <span class="topic-id">{topic_id}</span>
        <span class="topic-name">{title}</span>
      </a>''')
        
        if cards:
            sections_html.append(f'''
  <section id="{topic_dir_name}" class="section">
    <h2>{strand} ({len(cards)} Topics)</h2>
    <div class="topics-grid">
{''.join(cards)}
    </div>
  </section>''')
    
    sections_html = '\n'.join(sections_html)
    
    # Count total topics across all boards
    num_topics = 0
    for board_dirs in topic_dirs.values():
        for d in board_dirs:
            d_path = TOPICS_BASE / d
            if d_path.exists():
                num_topics += len(list(d_path.glob('*.html')))
    
    # Generate the page
    script = f'''<script>
function updateSubjectUrl() {{
    const board = document.getElementById('board-select').value;
    const tier = document.getElementById('tier-select')?.value || 'foundation';
    
    document.querySelectorAll('.topic-card').forEach(card => {{
        const href = card.getAttribute('href');
        if (href && href.startsWith('topics/')) {{
            const match = href.match(/topics\\/[^/]+\\/(?:[^/]+\\/)*([^/]+\\.html)/);
            if (match) {{
                const fileName = match[1];
                let newHref;
                if ({str(has_tiers).lower() if isinstance(has_tiers, bool) else has_tiers}) {{
                    newHref = `topics/{subject_id}/` + board + `/` + tier + `/` + fileName;
                }} else {{
                    newHref = `topics/{subject_id}/` + board + `/` + fileName;
                }}
                card.setAttribute('href', newHref);
            }}
        }}
    }});
    
    const path = window.location.pathname;
    const boardMatch = path.match(/{subject_id}\\/([^/]+)\\//);
    const tierMatch = path.match(/{subject_id}\\/[^/]+\\/([^/]+)\\//);
    if (boardMatch) document.getElementById('board-select').value = boardMatch[1];
    if (tierMatch) document.getElementById('tier-select').value = tierMatch[1];
}}
document.addEventListener('DOMContentLoaded', updateSubjectUrl);
</script>'''

    # Build page using string parts to avoid f-string issues
    page_parts = []
    page_parts.append('<!DOCTYPE html>')
    page_parts.append('<html lang="en">')
    page_parts.append('<head>')
    page_parts.append('<script>/* gcanonical-redirect */(function(){var p=location.pathname,q=location.search,h=location.hash,m=new RegExp("^(.*)/index.html$").exec(p);if(m){location.replace(m[1]+"/"+q+h);return}if(!p.endsWith("/")&&!new RegExp(".[a-z0-9]{1,10}$", "i").test(p)){location.replace(p+".html"+q+h)}}})();</script>')
    page_parts.append('<meta charset="UTF-8">')
    page_parts.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    page_parts.append('<title>' + subject_name + ' - Free GCSE Revision Notes</title>')
    page_parts.append('<meta name="description" content="Free GCSE ' + subject_name + ' revision notes across ' + str(num_topics) + ' topics across all major exam boards.">')
    page_parts.append('<meta name="keywords" content="GCSE ' + subject_name + ', ' + subject_name + ' revision notes, past papers, ' + ', '.join(boards) + '">')
    page_parts.append('<meta property="og:title" content="GCSE ' + subject_name + ' - Free Revision Notes">')
    page_parts.append('<meta property="og:description" content="Free GCSE ' + subject_name + ' revision notes across ' + str(num_topics) + ' topics across all major exam boards.">')
    page_parts.append('<meta property="og:type" content="article">')
    page_parts.append('<meta property="og:url" content="https://scottrix.github.io/gcserevise/' + subject_id + '.html">')
    page_parts.append('<link rel="canonical" href="https://scottrix.github.io/gcserevise/' + subject_id + '.html">')
    page_parts.append('<meta property="og:site_name" content="GCSE Revise">')
    page_parts.append('<meta property="og:locale" content="en_US">')
    page_parts.append('<meta name="twitter:card" content="summary">')
    page_parts.append('<meta name="twitter:title" content="GCSE ' + subject_name + '">')
    page_parts.append('<meta name="twitter:description" content="Free GCSE ' + subject_name + ' revision notes across ' + str(num_topics) + ' topics.">')
    page_parts.append('<link rel="stylesheet" href="style.css">')
    page_parts.append('</head>')
    page_parts.append('<body>')
    page_parts.append('<header class="site-header">')
    page_parts.append('<div class="header-content">')
    page_parts.append('<a href="./" class="logo">📚 GCSE Revise</a>')
    page_parts.append('<nav class="nav">')
    page_parts.append('<a href="./#subjects">Subjects</a>')
    page_parts.append('<a href="./">Home</a>')
    page_parts.append('</nav>')
    page_parts.append('<button id="theme-toggle" class="theme-btn">🌙</button>')
    page_parts.append('</div>')
    page_parts.append('</header>')
    page_parts.append('<div class="mobile-nav" id="mobile-nav">')
    page_parts.append('<div class="mobile-nav-header">')
    page_parts.append('<span class="logo">📚 GCSE Revise</span>')
    page_parts.append('<button id="close-mobile" class="close-btn">✕</button>')
    page_parts.append('</div>')
    page_parts.append('<nav class="mobile-nav-links">')
    page_parts.append('<a href="https://scottrix.github.io/">Scottrix</a>')
    page_parts.append('<a href="./#subjects">Subjects</a>')
    page_parts.append('<a href="./#exam-boards">Exam Boards</a>')
    page_parts.append('<a href="./#about">About</a>')
    page_parts.append('</nav>')
    page_parts.append('</div>')
    page_parts.append('<div class="overlay" id="overlay"></div>')
    page_parts.append('')
    page_parts.append('<div class="main-layout">')
    page_parts.append('<div class="header-spacer"></div>')
    page_parts.append('<aside class="sidebar" id="sidebar-nav"></aside>')
    page_parts.append('<main class="topic-content">')
    page_parts.append('<div class="disclaimer-banner"><strong>GCSE Revision Aid:</strong> This resource is designed to support your revision and may contain errors. If you find a discrepancy with your class teaching, your teacher is correct — please let us know at <a href="mailto:gcserevise@scott.scottrix.co.uk">gcserevise@scott.scottrix.co.uk</a>.</div>')
    page_parts.append('')
    page_parts.append('<nav class="breadcrumb">')
    page_parts.append('<a href="./">Home</a> <span>›</span>')
    page_parts.append('<span>' + subject_name + '</span>')
    page_parts.append('</nav>')
    page_parts.append('')
    page_parts.append('<article class="topic-header">')
    page_parts.append('<h1>🧬 GCSE ' + subject_name + '</h1>')
    page_parts.append('<div class="topic-meta">')
    if has_tiers:
        page_parts.append('<span class="badge foundation">Foundation</span><span class="badge higher">Higher</span>')
    for b in boards:
        page_parts.append('<span class="badge">' + get_board_display_name(b) + '</span>')
    page_parts.append('</div>')
    page_parts.append('<p class="topic-desc">Complete revision notes for GCSE ' + subject_name + ' covering all topics across ' + ', '.join(boards) + ' specifications.</p>')
    page_parts.append('</article>')
    page_parts.append('')
    page_parts.append(selector_bar)
    page_parts.append('')
    page_parts.append(sections_html)
    page_parts.append('')
    page_parts.append('</main>')
    page_parts.append('<aside class="ad-right" id="ad-rail-right"></aside>')
    page_parts.append('</div>')  # close main-layout
    page_parts.append('<div class="footer-spacer"></div>')
    page_parts.append('<footer class="site-footer">')
    page_parts.append('<p>GCSE Revise - Free revision notes for all subjects and exam boards</p>')
    page_parts.append('<p>Content for educational purposes only. Always cross-reference with official specifications.</p>')
    page_parts.append('<p>This site contains affiliate links. We may earn a commission if you purchase through these links.</p></footer>')
    page_parts.append(script)
    page_parts.append('<script src="app.js"></script>')
    page_parts.append('<script src="sidebar.js"></script>')
    page_parts.append('</body>')
    page_parts.append('</html>')
    
    return '\n'.join(page_parts)


def main():
    for subject in subjects:
        subject_id = subject['id']
        subject_name = subject['name']
        category = CATEGORIES.get(subject_id, 'Other')
        boards = subject.get('boards', [])
        topic_dirs = subject.get('topicDirs', {})
        has_tiers = subject.get('hasTiers', False)
        tiers = subject.get('tiers', [])
        
        page = generate_subject_page(subject_id, subject_name, category, boards, topic_dirs, has_tiers, tiers)
        
        output_path = Path(f'/home/scott/src/gcserevise/{subject_id}.html')
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(page)
        
        print(f"Generated {output_path}")


if __name__ == '__main__':
    main()