#!/usr/bin/env python3
"""Generate board-specific topic pages from the new board-aware subjects.json"""

import json
import os
import html
import re
from pathlib import Path

BASE = Path('/home/scott/src/gcserevise')

# Load the new subjects.json with board/tier hierarchy
with open(BASE / 'subjects.json', 'r') as f:
    data = json.load(f)

# Board-specific content overrides - where boards differ significantly
BOARD_OVERRIDES = {
    "biology": {
        "AQA": {
            "topics": {
                "cell-structure": "B1-cell-structure.html",
                "cell-division": "B2-cell-division.html",
                "transport-in-cells": "B3-transport-in-cells.html",
                # ... etc
            }
        }
    },
    "mathematics": {
        "AQA": {"tier": "both"},
        "Edexcel": {"tier": "both"},
        "OCR": {"tier": "both"},
        "Eduqas": {"tier": "both"},
        "CCEA": {"tier": "both"},
    }
}

# Tier-specific content indicators
TIER_CONTENT = {
    "mathematics": {
        "foundation_only": ["A1-algebraic-notation", "A2-substitution", "A3-algebraic-terminology"],
        "higher_only": ["A6-algebraic-proof", "A20-iteration", "A21-modelling-with-algebra"],
    },
    "physics": {
        "higher_only": ["phys-atomic", "phys-magnetism", "phys-particle"],
    },
    "chemistry": {
        "higher_only": ["chem-organic", "chem-analysis"],
    },
    "biology": {
        "higher_only": ["bio-inheritance", "bio-homeostasis"],
    },
}

def slug(text):
    return text.lower().replace(" ", "-").replace("/", "-").replace(".", "-")

def get_topic_file(topic_dir, topic_file):
    """Get the source topic file path"""
    topic_path = BASE / 'topics' / topic_dir / topic_file
    if topic_path.exists():
        return topic_path
    return None

def get_topic_content(topic_dir, topic_file):
    """Read a topic file and extract its content sections"""
    topic_path = BASE / 'topics' / topic_dir / topic_file
    if not topic_path.exists():
        return None
    
    with open(topic_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the main content (between <main class="topic-content"> and </main>)
    main_match = re.search(r'<main class="topic-content">(.*?)</main>', content, re.DOTALL)
    if main_match:
        return main_match.group(1)
    return content

def generate_board_topic_page(subject_id, board, topic_id, topic_title, tier, topic_dir, topic_file, 
                              subject_name, subject_category, base_url):
    """Generate a board-specific topic page"""
    
    # Read the source topic content
    main_content = get_topic_content(topic_dir, topic_file)
    if not main_content:
        return None
    
    # Determine if this topic is available for this board/tier
    tier_badge = ""
    if tier == "foundation":
        tier_badge = '<span class="badge foundation">Foundation</span>'
    elif tier == "higher":
        tier_badge = '<span class="badge higher">Higher</span>'
    else:
        tier_badge = '<span class="badge foundation">Foundation</span><span class="badge higher">Higher</span>'
    
    board_badge = f'<span class="badge">{board}</span>'
    
    # Get tier badge for this topic
    tier_badge_html = ""
    if tier != "both":
        tier_badge_html = tier_badge
    else:
        # Check if topic has tier-specific content
        if subject_id in TIER_CONTENT:
            if topic_id in TIER_CONTENT[subject_id].get("foundation_only", []):
                tier_badge_html = '<span class="badge foundation">Foundation</span>'
            elif topic_id in TIER_CONTENT[subject_id].get("higher_only", []):
                tier_badge_html = '<span class="badge higher">Higher</span>'
            else:
                tier_badge_html = '<span class="badge foundation">Foundation</span><span class="badge higher">Higher</span>'
        else:
            tier_badge_html = '<span class="badge foundation">Foundation</span><span class="badge higher">Higher</span>'
    
    # Generate the page
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<script>/* gcanonical-redirect */(function(){{var p=location.pathname,q=location.search,h=location.hash,m=/^(.*)\\/index\\.html$/.exec(p);if(m){{location.replace(m[1]+"/"+q+h);return}}if(!p.endsWith("/")&&!/\\.[a-z0-9]{{1,10}}$/i.test(p)){{location.replace(p+".html"+q+h)}}}})();</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{topic_title} - GCSE {subject_name} ({board}) Revision</title>
<meta name="description" content="{topic_title} revision notes for {board} GCSE {subject_name}.">
<meta name="keywords" content="GCSE {subject_name}, {topic_title}, {board}, revision notes, past papers">
<meta property="og:title" content="{topic_title} - GCSE {subject_name} ({board})">
<meta property="og:description" content="{topic_title} revision notes for {board} GCSE {subject_name}.">
<meta property="og:type" content="article">
<meta property="og:url" content="{base_url}/{subject_id}/{board}/{tier}/{topic_slug}.html">
<link rel="canonical" href="{base_url}/{subject_id}/{board}/{tier}/{topic_slug}.html">
<meta property="og:site_name" content="GCSE Revise">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{topic_title} - GCSE {subject_name} ({board})">
<meta name="twitter:description" content="{topic_title} revision notes for {board} GCSE {subject_name}.">
<link rel="stylesheet" href="../../../style.css">
</head>
<body>
<header class="site-header">
<div class="header-content">
<a href="../../../" class="logo">📚 GCSE Revise</a>
<nav class="nav">
<a href="../../../#subjects">Subjects</a>
<a href="../../../{subject_id}.html">{subject_name}</a>
<a href="../../../{subject_id}/{board}/">{board}</a>
<a href="../../../{subject_id}/{board}/{tier}/">{tier.capitalize()}</a>
</nav>
<button id="theme-toggle" class="theme-btn">🌙</button>
</div>
</header>

<main class="topic-content">
<div class="disclaimer-banner"><strong>GCSE Revision Aid:</strong> This resource is designed to support your revision and may contain errors. If you find a discrepancy with your class teaching, your teacher is correct — please let us know at <a href="mailto:gcserevise@scott.scottrix.co.uk">gcserevise@scott.scottrix.co.uk</a>.</div>

<nav class="breadcrumb">
<a href="../../../">Home</a> <span>›</span>
<a href="../../../{subject_id}.html">{subject_name}</a> <span>›</span>
<a href="../../../{subject_id}/{board}/">{board}</a> <span>›</span>
<a href="../../../{subject_id}/{board}/{tier}/">{tier.capitalize()}</a> <span>›</span>
<span>{topic_title}</span>
</nav>

<article class="topic-header">
<h1>{topic_title}</h1>
<div class="topic-meta">
{tier_badge_html}
<span class="badge">{board}</span>
</div>
<p class="topic-desc">{topic_title} revision for {board} GCSE {subject_name} ({tier.capitalize()})</p>
</article>

{main_content}

<nav class="topic-nav">
<a href="../../../{subject_id}/{board}/{tier}/">← Back to {board} {tier.capitalize()} {subject_name}</a>
<a href="../../../">All Subjects →</a>
</nav>
</main>
<footer class="site-footer">
<p>GCSE Revise - Free revision notes for all subjects and exam boards</p>
<p>Content for educational purposes only. Always cross-reference with official specifications.</p>
<p>This site contains affiliate links. We may earn a commission if you purchase through these links.</</footer>
<script>
document.getElementById('theme-toggle').addEventListener('click', function() {{
const root = document.documentElement;
if (root.classList.contains('light-mode')) {{
root.classList.remove('light-mode'); this.textContent = '🌙'; localStorage.setItem('gcserevise-theme', 'dark');
}} else {{
root.classList.add('light-mode'); this.textContent = '☀️'; localStorage.setItem('gcserevise-theme', 'light');
}}
}});
if (localStorage.getItem('gcserevise-theme') === 'light') {{
document.documentElement.classList.add('light-mode'); document.getElementById('theme-toggle').textContent = '☀️';
}}
</script>
<aside class="ad-right">
<!-- Affiliate cards would go here -->
</aside>
<script src="../../../sidebar.js"></script>
<script src="../../../affiliate-images.js"></script>
</body>
</html>
'''
    return page

def main():
    # Read subjects.json
    with open(BASE / 'subjects.json', 'r') as f:
        data = json.load(f)
    
    # For now, let's just create the board/tier directory structure
    # and copy existing topic files
    
    BASE_TOPICS = Path('/home/scott/src/gcserevise/topics')
    
    for subject in data['subjects']:
        subject_id = subject['id']
        subject_name = subject['name']
        boards = subject.get('boards', [])
        
        # Determine if subject has tiers
        has_tiers = subject_id in ['mathematics', 'physics', 'chemistry', 'biology', 'combined-science', 'statistics']
        
        for board in boards:
            board_slug = board.lower()
            
            if has_tiers:
                for tier in ['foundation', 'higher']:
                    tier_dir = BASE / 'topics' / subject_id / board_slug / tier
                    tier_dir.mkdir(parents=True, exist_ok=True)
                    
                    # Copy topic files
                    source_dir = Path('/home/scott/src/gcserevise/topics')
                    # Find the topic directory for this subject
                    for topic_dir in source_dir.iterdir():
                        if topic_dir.is_dir() and topic_dir.name.startswith(subject_id.replace('-', '')[:3]):
                            for html_file in topic_dir.glob('*.html'):
                                dest = tier_dir / html_file.name
                                if not dest.exists():
                                    import shutil
                                    shutil.copy2(html_file, dest)
            else:
                # No tiers - just board
                board_dir = BASE / 'topics' / subject_id / board_slug
                board_dir.mkdir(parents=True, exist_ok=True)
                
                source_dir = Path('/home/scott/src/gcserevise/topics')
                for topic_dir in source_dir.iterdir():
                    if topic_dir.is_dir() and topic_dir.name.startswith(subject_id.replace('-', '')[:3]):
                        for html_file in topic_dir.glob('*.html'):
                            dest = board_dir / html_file.name
                            if not dest.exists():
                                import shutil
                                shutil.copy2(html_file, dest)
    
    print("Board/tier directory structure created")

if __name__ == '__main__':
    main()