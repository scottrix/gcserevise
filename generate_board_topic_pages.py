#!/usr/bin/env python3
"""Generate GCSE board-specific topic pages from board-specific topic directories"""

import json
import os
from pathlib import Path

BASE = Path('/home/scott/src')
TOPICS_BASE = BASE / 'gcserevise' / 'topics'
OUTPUT_BASE = BASE / 'gcserevise' / 'topics'

# Load GCSE subjects
with open(BASE / 'gcserevise' / 'subjects.json', 'r') as f:
    data = json.load(f)

subjects = data['subjects']


def get_topic_title(topic_file: str, topic_dir: str) -> str:
    """Extract readable title from topic filename"""
    name = topic_file.replace('.html', '')
    # Remove leading codes like "A1-", "B2-", etc.
    if '-' in name and name[0].isalpha() and name[1:3].isdigit():
        name = name[name.index('-')+1:]
    elif '_' in name and name[0].isalpha() and name[1:3].isdigit():
        name = name[name.index('_')+1:]
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


def generate_board_topic_page(subject_id: str, subject_name: str, board: str, topic_dir: str, topic_file: str, has_tiers: bool = False, tier: str = None):
    """Generate a single board-specific topic page"""
    
    topic_title = get_topic_title(topic_file, topic_dir)
    board_display = get_board_display_name(board)
    
    # Build canonical URL path
    if has_tiers and tier:
        canonical_path = f"/gcserevise/topics/{subject_id}/{board.lower()}/{tier.lower()}/{topic_file}"
    else:
        canonical_path = f"/gcserevise/topics/{subject_id}/{board.lower()}/{topic_file}"
    
    # Read existing topic content if it exists
    topic_path = TOPICS_BASE / topic_dir / topic_file
    existing_content = ""
    if topic_path.exists():
        with open(topic_path, 'r') as f:
            existing_content = f.read()
    
    # Extract main content from existing file (between <main> tags)
    import re
    main_match = re.search(r'<main[^>]*>(.*?)</main>', existing_content, re.DOTALL)
    topic_content = main_match.group(1) if main_match else ""
    
    # If no existing content, create placeholder
    if not topic_content.strip():
        topic_content = f"""
        <section class="section">
            <h2>{topic_title}</h2>
            <p class="placeholder">Revision notes for <strong>{topic_title}</strong> ({board_display}) coming soon.</p>
            <div class="card-grid" style="margin-top: 2rem;">
                <div class="card">
                    <h3>Key Concepts</h3>
                    <p>Core ideas and definitions for this topic.</p>
                </div>
                <div class="card">
                    <h3>Exam Questions</h3>
                    <p>Typical {board_display} question types for this topic.</p>
                </div>
                <div class="card">
                    <h3>Practice</h3>
                    <p>Self-assessment questions with model answers.</p>
                </div>
            </div>
        </section>
        """
    
    # Board selector options
    subject_obj = next(s for s in subjects if s['id'] == subject_id)
    boards = subject_obj.get('boards', [])
    
    board_options = ""
    for b in boards:
        selected = "selected" if b == board else ""
        board_options += f'<option value="{b.lower()}" {selected}>{get_board_display_name(b)}</option>'
    
    # Tier selector for Maths
    tier_options = ""
    if has_tiers:
        tiers = subject_obj.get('tiers', ['Foundation', 'Higher'])
        for t in tiers:
            selected = "selected" if t.lower() == tier else ""
            tier_options += f'<option value="{t.lower()}" {selected}>{t}</option>'
    
    # Build page
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<script>/* gcanonical-redirect */(function(){{var p=location.pathname,q=location.search,h=location.hash,m=new RegExp("^(.*)/index.html$").exec(p);if(m){{location.replace(m[1]+"/"+q+h);return}}if(!p.endsWith("/")&&!new RegExp(".[a-z0-9]{{1,10}}$", "i").test(p)){{location.replace(p+".html"+q+h)}}}})();</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{topic_title} - {subject_name} ({board_display}) - GCSE Revise</title>
<meta name="description" content="Free GCSE {subject_name} revision notes for {topic_title} - {board_display} specification.">
<meta name="keywords" content="GCSE {subject_name}, {topic_title}, {board_display}, revision notes, past papers">
<meta property="og:title" content="{topic_title} - {subject_name} ({board_display})">
<meta property="og:description" content="Free GCSE {subject_name} revision notes for {topic_title} - {board_display} specification.">
<meta property="og:type" content="article">
<meta property="og:url" content="https://scottrix.github.io{canonical_path}">
<link rel="canonical" href="https://scottrix.github.io{canonical_path}">
<meta property="og:site_name" content="GCSE Revise">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{topic_title} - {subject_name} ({board_display})">
<meta name="twitter:description" content="Free GCSE {subject_name} revision notes for {topic_title} - {board_display} specification.">
<link rel="stylesheet" href="../../../../style.css">
</head>
<body>
<header class="site-header">
<div class="header-content">
<a href="../../../../" class="logo">📚 GCSE Revise</a>
<nav class="nav">
<a href="../../../../#subjects">Subjects</a>
<a href="../../../../">Home</a>
</nav>
<button id="theme-toggle" class="theme-btn">🌙</button>
</div>
</header>

<main class="container">
<nav class="breadcrumb" aria-label="Breadcrumb">
<ol>
<li><a href="../../../../">Home</a></li>
<li><a href="../../../../#subjects">Subjects</a></li>
<li><a href="../../../">{subject_name}</a></li>
<li><a href="../">{board_display}</a></li>
{f'<li><a href="./">{tier}</a></li>' if has_tiers and tier else ''}
<li aria-current="page">{topic_title}</li>
</ol>
</nav>

<div class="topic-header">
<h1>{topic_title}</h1>
<div class="topic-meta">
<span class="badge subject-badge">{subject_name}</span>
<span class="badge board-badge">{board_display}</span>
{f'<span class="badge tier-badge">{tier}</span>' if has_tiers and tier else ''}
</div>
</div>

<div class="topic-toolbar">
<div class="board-selector">
<label for="board-select">Exam Board: </label>
<select id="board-select" onchange="updateBoardUrl()">
{board_options}
</select>
</div>
{'' if not has_tiers else f'''
<div class="tier-selector">
<label for="tier-select">Tier: </label>
<select id="tier-select" onchange="updateTierUrl()">
{tier_options}
</select>
</div>
'''}
</div>

{topic_content}

<!-- Flashcards Section -->
<section class="section">
<h2>🧠 Flashcards (Spaced Repetition)</h2>
<div id="flashcard-container"></div>
</section>

<!-- Exam Questions Section -->
<section class="section">
<h2>📝 Exam Questions by Topic</h2>
<div id="exam-questions-container"></div>
</section>

<!-- Target Tests Section -->
<section class="section">
<h2>🎯 Target Tests (Auto-Graded)</h2>
<div id="target-tests-container"></div>
</section>

<!-- Exam Questions by Topic (Legacy Links) -->
<section class="section">
<h2>📝 Exam Questions by Topic</h2>
<ul class="resource-links">
<li><a href="https://www.aqa.org.uk/find-past-papers-and-mark-schemes" target="_blank" rel="noopener">AQA Past Papers - Topic Questions</a></li>
<li><a href="https://qualifications.pearson.com/en/support/support-topics/exams/past-papers.html" target="_blank" rel="noopener">Edexcel Past Papers - Topic Questions</a></li>
<li><a href="https://www.ocr.org.uk/qualifications/past-paper-finder/" target="_blank" rel="noopener">OCR Past Papers - Topic Questions</a></li>
<li><a href="https://www.eduqas.co.uk/qualifications/past-papers/" target="_blank" rel="noopener">Eduqas Past Papers - Topic Questions</a></li>
<li><a href="https://ccea.org.uk/past-papers/" target="_blank" rel="noopener">CCEA Past Papers - Topic Questions</a></li>
</ul>
</section>

<!-- Past Papers Landing -->
<section class="section">
<h2>📄 Past Papers for {subject_name} ({board_display})</h2>
<ul class="resource-links">
<li><a href="https://www.aqa.org.uk/find-past-papers-and-mark-schemes" target="_blank" rel="noopener">AQA Past Papers & Mark Schemes</a></li>
<li><a href="https://qualifications.pearson.com/en/support/support-topics/exams/past-papers.html" target="_blank" rel="noopener">Edexcel Past Papers & Mark Schemes</a></li>
<li><a href="https://www.ocr.org.uk/qualifications/past-paper-finder/" target="_blank" rel="noopener">OCR Past Papers & Mark Schemes</a></li>
<li><a href="https://www.eduqas.co.uk/qualifications/past-papers/" target="_blank" rel="noopener">Eduqas Past Papers & Mark Schemes</a></li>
<li><a href="https://ccea.org.uk/past-papers/" target="_blank" rel="noopener">CCEA Past Papers & Mark Schemes</a></li>
</ul>
<p class="note">For the most accurate and up-to-date past papers, always check the official exam board websites.</p>
</section>

</main>

<footer class="site-footer">
<div class="footer-content">
<p>&copy; 2025 GCSE Revise. Free revision notes for all GCSE subjects.</p>
<nav class="footer-nav">
<a href="../../../../privacy.html">Privacy</a>
<a href="../../../../terms.html">Terms</a>
<a href="../../../../contact.html">Contact</a>
</nav>
</div>
</footer>

<script src="../../../../flashcards/flashcards.js"></script>
<script src="../../../../exam-questions/exam-questions.js"></script>
<script src="../../../../target-tests/target-tests.js"></script>
<script>
function updateBoardUrl() {{
    const select = document.getElementById('board-select');
    const board = select.value;
    const path = window.location.pathname;
    const newPath = path.replace(/topics\\/([^\\/]+)\\/([^\\/]+)/, `topics/${{board}}`);
    window.location.href = newPath;
}}

function updateTierUrl() {{
    const select = document.getElementById('tier-select');
    const tier = select.value;
    const path = window.location.pathname;
    const newPath = path.replace(/topics\\/([^\\/]+)\\/([^\\/]+)\\/([^\\/]+)/, `topics/${{board}}/${{tier}}`);
    window.location.href = newPath;
}}

document.addEventListener('DOMContentLoaded', () => {{
    const path = window.location.pathname;
    const boardMatch = path.match(/{subject_id}\\/([^\\/]+)/);
    const tierMatch = path.match(/{subject_id}\\/[^\\/]+\\/([^\\/]+)/);
    if (boardMatch) document.getElementById('board-select').value = boardMatch[1];
    if (tierMatch) document.getElementById('tier-select').value = tierMatch[1];
}});
</script>
</body>
</html>"""

    # Determine output path
    if has_tiers and tier:
        output_dir = OUTPUT_BASE / subject_id / board.lower() / tier.lower()
    else:
        output_dir = OUTPUT_BASE / subject_id / board.lower()
    
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / topic_file
    
    with open(output_file, 'w') as f:
        f.write(page)
    
    return str(output_file)


def main():
    """Generate all board-specific topic pages"""
    generated = 0
    
    for subject in subjects:
        subject_id = subject['id']
        subject_name = subject['name']
        boards = subject.get('boards', [])
        has_tiers = subject.get('hasTiers', False)
        tiers = subject.get('tiers', [])
        topic_dirs = subject.get('topicDirs', {})
        
        for board in boards:
            board_dirs = topic_dirs.get(board, [])
            
            if has_tiers:
                for tier in tiers:
                    tier_lower = tier.lower()
                    # Find the directory for this tier
                    tier_dir = None
                    for d in board_dirs:
                        if tier_lower in d.lower():
                            tier_dir = d
                            break
                    if not tier_dir and board_dirs:
                        tier_dir = board_dirs[0]  # fallback
                    
                    if tier_dir and (TOPICS_BASE / tier_dir).exists():
                        topic_files = sorted((TOPICS_BASE / tier_dir).glob('*.html'))
                        for topic_file in topic_files:
                            generate_board_topic_page(subject_id, subject_name, board, tier_dir, topic_file.name, has_tiers=True, tier=tier)
                            generated += 1
            else:
                for topic_dir in board_dirs:
                    if (TOPICS_BASE / topic_dir).exists():
                        topic_files = sorted((TOPICS_BASE / topic_dir).glob('*.html'))
                        for topic_file in topic_files:
                            generate_board_topic_page(subject_id, subject_name, board, topic_dir, topic_file.name)
                            generated += 1
    
    print(f"Generated {generated} board-specific topic pages")


if __name__ == '__main__':
    main()