#!/usr/bin/env python3
"""Generate Past Papers landing pages for each subject and board combination"""

import os
from pathlib import Path

BASE = Path('/home/scott/src/gcserevise')

# Past paper finder URLs
PAST_PAPER_URLS = {
    "AQA": "https://www.aqa.org.uk/find-past-papers-and-mark-schemes",
    "Edexcel": "https://qualifications.pearson.com/en/support/support-topics/exams/past-papers.html",
    "OCR": "https://www.ocr.org.uk/qualifications/past-paper-finder/",
    "Eduqas": "https://www.eduqas.co.uk/qualifications/past-papers/",
    "CCEA": "https://ccea.org.uk/past-papers/",
}

# Subject info with boards
SUBJECT_INFO = {
    "mathematics": {"name": "Mathematics", "boards": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"], "category": "Core"},
    "statistics": {"name": "Statistics", "boards": ["AQA", "Edexcel", "CCEA"], "category": "Mathematics"},
    "combined-science": {"name": "Combined Science", "boards": ["AQA", "Edexcel", "OCR", "CCEA"], "category": "Science"},
    "biology": {"name": "Biology", "boards": ["AQA", "Edexcel", "OCR", "CCEA"], "category": "Science"},
    "chemistry": {"name": "Chemistry", "boards": ["AQA", "Edexcel", "OCR", "CCEA"], "category": "Science"},
    "physics": {"name": "Physics", "boards": ["AQA", "Edexcel", "OCR", "CCEA"], "category": "Science"},
    "english-language": {"name": "English Language", "boards": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"], "category": "Core"},
    "english-literature": {"name": "English Literature", "boards": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"], "category": "Core"},
    "history": {"name": "History", "boards": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"], "category": "Humanities"},
    "geography": {"name": "Geography", "boards": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"], "category": "Humanities"},
    "religious-studies": {"name": "Religious Studies", "boards": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"], "category": "Humanities"},
    "french": {"name": "French", "boards": ["AQA", "Edexcel", "Eduqas", "CCEA"], "category": "Languages"},
    "spanish": {"name": "Spanish", "boards": ["AQA", "Edexcel", "Eduqas", "CCEA"], "category": "Languages"},
    "german": {"name": "German", "boards": ["AQA", "Edexcel", "Eduqas", "CCEA"], "category": "Languages"},
    "computer-science": {"name": "Computer Science", "boards": ["AQA", "Edexcel", "OCR", "Eduqas"], "category": "Science"},
    "business": {"name": "Business Studies", "boards": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"], "category": "Other"},
    "economics": {"name": "Economics", "boards": ["AQA", "Edexcel", "OCR", "CCEA"], "category": "Other"},
    "psychology": {"name": "Psychology", "boards": ["AQA", "Edexcel", "OCR"], "category": "Other"},
    "sociology": {"name": "Sociology", "boards": ["AQA", "Edexcel", "Eduqas"], "category": "Other"},
    "pe": {"name": "Physical Education", "boards": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"], "category": "Other"},
    "religious-studies": {"name": "Religious Studies", "boards": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"], "category": "Humanities"},
    "citizenship-studies": {"name": "Citizenship Studies", "boards": ["AQA", "Edexcel", "OCR"], "category": "Humanities"},
    "media-studies": {"name": "Media Studies", "boards": ["AQA", "Eduqas"], "category": "Creative"},
    "design-and-technology": {"name": "Design and Technology", "boards": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"], "category": "Technical"},
    "food-preparation-nutrition": {"name": "Food Preparation and Nutrition", "boards": ["AQA", "Edexcel", "OCR", "Eduqas"], "category": "Technical"},
    "dance": {"name": "Dance", "boards": ["AQA"], "category": "Creative"},
    "drama": {"name": "Drama", "boards": ["AQA", "Edexcel", "OCR"], "category": "Creative"},
    "music": {"name": "Music", "boards": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"], "category": "Creative"},
    "art-and-design": {"name": "Art and Design", "boards": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"], "category": "Creative"},
    "media-studies": {"name": "Media Studies", "boards": ["AQA", "Eduqas"], "category": "Creative"},
    "food-preparation-nutrition": {"name": "Food Preparation and Nutrition", "boards": ["AQA", "Edexcel", "OCR", "Eduqas"], "category": "Technical"},
    "latin": {"name": "Latin", "boards": ["Edexcel", "OCR", "Eduqas"], "category": "Languages"},
    "ancient-history": {"name": "Ancient History", "boards": ["OCR"], "category": "Humanities"},
    "classical-civilisation": {"name": "Classical Civilisation", "boards": ["OCR"], "category": "Humanities"},
    "law": {"name": "Law", "boards": ["AQA"], "category": "Other"},
    "dance": {"name": "Dance", "boards": ["AQA"], "category": "Creative"},
    "film-studies": {"name": "Film Studies", "boards": ["Eduqas"], "category": "Creative"},
    "electronics": {"name": "Electronics", "boards": ["Eduqas"], "category": "Science"},
    "engineering": {"name": "Engineering", "boards": ["AQA", "Edexcel", "CCEA"], "category": "Technical"},
    "statistics": {"name": "Statistics", "boards": ["AQA", "Edexcel", "CCEA"], "category": "Mathematics"},
    "astronomy": {"name": "Astronomy", "boards": ["Edexcel"], "category": "Science"},
    "geology": {"name": "Geology", "boards": ["Eduqas"], "category": "Science"},
    "ancient-history": {"name": "Ancient History", "boards": ["OCR"], "category": "Humanities"},
    "classical-civilisation": {"name": "Classical Civilisation", "boards": ["OCR"], "category": "Humanities"},
    "law": {"name": "Law", "boards": ["AQA"], "category": "Other"},
    "dance": {"name": "Dance", "boards": ["AQA"], "category": "Creative"},
    "film-studies": {"name": "Film Studies", "boards": ["Eduqas"], "category": "Creative"},
    "electronics": {"name": "Electronics", "boards": ["Eduqas"], "category": "Science"},
    "engineering": {"name": "Engineering", "boards": ["AQA", "Edexcel", "CCEA"], "category": "Technical"},
    "statistics": {"name": "Statistics", "boards": ["AQA", "Edexcel", "CCEA"], "category": "Mathematics"},
    "citizenship-studies": {"name": "Citizenship Studies", "boards": ["AQA", "Edexcel", "OCR"], "category": "Humanities"},
    "food-preparation-nutrition": {"name": "Food Preparation and Nutrition", "boards": ["AQA", "Edexcel", "OCR", "Eduqas"], "category": "Technical"},
    "film-studies": {"name": "Film Studies", "boards": ["Eduqas"], "category": "Creative"},
    "electronics": {"name": "Electronics", "boards": ["Eduqas"], "category": "Science"},
    "engineering": {"name": "Engineering", "boards": ["AQA", "Edexcel", "CCEA"], "category": "Technical"},
    "statistics": {"name": "Statistics", "boards": ["AQA", "Edexcel", "CCEA"], "category": "Mathematics"},
}

PAST_PAPER_URLS = {
    "AQA": "https://www.aqa.org.uk/find-past-papers-and-mark-schemes",
    "Edexcel": "https://qualifications.pearson.com/en/support/support-topics/exams/past-papers.html",
    "OCR": "https://www.ocr.org.uk/qualifications/past-paper-finder/",
    "Eduqas": "https://www.eduqas.co.uk/qualifications/past-papers/",
    "CCEA": "https://ccea.org.uk/past-papers/",
}

def generate_past_papers_page(subject_id, subject_info):
    """Generate a Past Papers landing page for a subject"""
    name = subject_info["name"]
    boards = subject_info["boards"]
    category = subject_info.get("category", "Other")
    subject_slug = subject_id
    
    board_cards = ""
    for board in boards:
        url = f"https://www.aqa.org.uk/find-past-papers-and-mark-schemes"
        if board == "Edexcel":
            url = "https://qualifications.pearson.com/en/support/support-topics/exams/past-papers.html"
        elif board == "OCR":
            url = "https://www.ocr.org.uk/qualifications/past-paper-finder/"
        elif board == "Eduqas":
            url = "https://www.eduqas.co.uk/qualifications/past-papers/"
        elif board == "CCEA":
            url = "https://ccea.org.uk/past-papers/"
        
        board_cards += f'''
        <div class="board-card">
            <h3>{board}</h3>
            <p>Access {name} past papers, mark schemes, and examiner reports for {board}.</p>
            <a href="{url}" class="btn" target="_blank" rel="noopener">View {board} Past Papers</a>
        </div>
'''
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<script>/* gcanonical-redirect */(function(){{var p=location.pathname,q=location.search,h=location.hash,m=/^(.*)\\/index\\.html$/.exec(p);if(m){{location.replace(m[1]+"/"+q+h);return}}if(!p.endsWith("/")&&!/\\.[a-z0-9]{{1,10}}$/i.test(p)){{location.replace(p+".html"+q+h)}}}})();</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} Past Papers - GCSE Revision</title>
<meta name="description" content="Find past papers, mark schemes, and examiner reports for GCSE {name} across all exam boards.">
<meta name="keywords" content="GCSE {name}, past papers, mark schemes, examiner reports, AQA, Edexcel, OCR, Eduqas, CCEA">
<meta property="og:title" content="{name} Past Papers - GCSE Revise">
<meta property="og:description" content="Find past papers, mark schemes, and examiner reports for GCSE {name} across all exam boards.">
<meta property="og:type" content="article">
<meta property="og:url" content="https://scottrix.github.io/gcserevise/{subject_slug}-past-papers.html">
<link rel="canonical" href="https://scottrix.github.io/gcserevise/{subject_slug}-past-papers.html">
<meta property="og:site_name" content="GCSE Revise">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{name} Past Papers">
<meta name="twitter:description" content="Find past papers, mark schemes, and examiner reports for GCSE {name} across all exam boards.">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site-header">
<div class="header-content">
<a href="../" class="logo">📚 GCSE Revise</a>
<nav class="nav">
<a href="../#subjects">Subjects</a>
<a href="../index.html">Home</a>
</nav>
<button id="theme-toggle" class="theme-btn">🌙</button>
</div>
</header>

<main class="topic-content">
<div class="disclaimer-banner"><strong>GCSE Revision Aid:</strong> This resource is designed to support your revision and may contain errors. If you find a discrepancy with your class teaching, your teacher is correct — please let us know at <a href="mailto:gcserevise@scott.scottrix.co.uk">gcserevise@scott.scottrix.co.uk</a>.</div>

<nav class="breadcrumb">
<a href="../">Home</a> <span>›</span>
<a href="../{subject_slug}.html">{name}</a> <span>›</span>
<span>Past Papers</span>
</nav>

<article class="topic-header">
<h1>📄 {name} Past Papers</h1>
<div class="topic-meta">
<span class="badge">{category}</span>
</div>
<p class="topic-desc">Find past papers, mark schemes, and examiner reports for GCSE {name} across all major exam boards.</p>
</article>

<section class="section">
<h2>📚 Past Papers by Exam Board</h2>
<div class="boards-grid">
{board_cards}
</div>
</section>

<section class="section">
<h2>📋 How to Use Past Papers Effectively</h2>
<div class="key-point">
<strong>Tip:</strong> Start with untimed practice using your notes, then progress to timed conditions as you gain confidence.
</div>
<ol>
<li><strong>Start early</strong> - Don't leave past papers until the last minute</li>
<li><strong>Use mark schemes</strong> - Mark your own work honestly to identify gaps</li>
<li><strong>Track your scores</strong> - Keep a log of your scores to track progress</li>
<li><strong>Focus on weak areas</strong> - Spend more time on topics where you lose marks</li>
<li><strong>Simulate exam conditions</strong> - Practice under timed conditions without notes</li>
<li><strong>Review examiner reports</strong> - Learn from common mistakes other students make</li>
</ol>
</section>

<section class="section">
<h2>🔗 Quick Links</h2>
<ul>
'''

    for board in boards:
        url = PAST_PAPER_URLS.get(board, "")
        if url:
            subject_lower = subject_id.replace("-", "+").replace(" ", "+")
            board_lower = board.lower()
            quick_url = f"{url}?subject={subject_lower}&board={board_lower}"
            html += f'<li><a href="{quick_url}" target="_blank" rel="noopener">{board} {name} Past Papers</a></li>\n'
    
    html += f'''</ul>
</section>

<section class="section">
<h2>📝 Topic-Based Practice</h2>
<p>Looking for questions on a specific topic? Visit the <a href="../{subject_slug}.html">{name} subject page</a> to find topic-by-topic revision notes with exam questions and practice questions.</</section>

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
<script src="../sidebar.js"></script>
<script src="../affiliate-images.js"></script>
</body>
</html>
'''
    return html

def main():
    output_dir = BASE / 'gcserevise'
    output_dir.mkdir(exist_ok=True)
    
    for subject_id, subject_info in SUBJECT_INFO.items():
        if not subject_info.get("boards"):
            continue
            
        html = generate_past_papers_page(subject_id, subject_info)
        output_file = BASE / f'{subject_id}-past-papers.html'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"Generated: {output_file}")

if __name__ == '__main__':
    main()