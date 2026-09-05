#!/usr/bin/env python3
"""Update subject landing pages with board/tier selectors"""

import json
import re
from pathlib import Path

BASE = Path('/home/scott/src/gcserevise')

# Load subjects
with open(BASE / 'subjects.json', 'r') as f:
    data = json.load(f)

SUBJECT_INFO = {s['id']: s for s in data['subjects']}

TIER_SUBJECTS = {"mathematics", "physics", "chemistry", "biology", "combined-science", "statistics"}

BOARD_URLS = {
    "AQA": "https://www.aqa.org.uk/find-past-papers-and-mark-schemes",
    "Edexcel": "https://qualifications.pearson.com/en/support/support-topics/exams/past-papers.html",
    "OCR": "https://www.ocr.org.uk/qualifications/past-paper-finder/",
    "Eduqas": "https://www.eduqas.co.uk/qualifications/past-papers/",
    "CCEA": "https://ccea.org.uk/past-papers/",
}

def generate_board_selector(subject_id, current_board=None):
    """Generate board selector dropdown HTML"""
    subject = SUBJECT_INFO.get(subject_id, {})
    boards = subject.get('boards', [])
    
    options = []
    for board in boards:
        selected = ' selected' if board == current_board else ''
        options.append(f'<option value="{board.lower()}"{selected}>{board}</option>')
    
    return f'''
<div class="board-selector">
  <label for="board-select">Exam Board: </label>
  <select id="board-select" onchange="window.location.href='/{subject_id}/' + this.value + '/' + (document.getElementById('tier-select') ? document.getElementById('tier-select').value + '/' : '')">
    {''.join(options)}
  </select>
</div>'''

def generate_tier_selector(subject_id, current_tier=None):
    """Generate tier selector dropdown HTML for tiered subjects"""
    if subject_id not in TIER_SUBJECTS:
        return ''
    
    options = []
    for tier in ['foundation', 'higher']:
        selected = ' selected' if tier == current_tier else ''
        options.append(f'<option value="{tier}"{selected}>{tier.capitalize()}</option>')
    
    return f'''
<div class="tier-selector">
  <label for="tier-select">Tier: </label>
  <select id="tier-select" onchange="window.location.href='/{subject_id}/' + (document.getElementById('board-select') ? document.getElementById('board-select').value + '/' : '') + this.value + '/'">
    {''.join(options)}
  </select>
</div>'''

def update_subject_page(subject_id):
    """Update a subject landing page with board/tier selectors"""
    subject = SUBJECT_INFO.get(subject_id)
    if not subject:
        return False
    
    file_path = Path('/home/scott/src/gcserevise') / f'{subject_id}.html'
    if not file_path.exists():
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    boards = subject.get('boards', [])
    has_tiers = subject_id in ["mathematics", "physics", "chemistry", "biology", "combined-science", "statistics"]
    
    # Generate board selector
    board_options = ''.join(f'<option value="{board.lower()}">{board}</option>' for board in boards)
    board_selector = f'''
<div class="selector-group">
  <label for="board-select">Exam Board: </label>
  <select id="board-select" onchange="updateSubjectUrl()">
    {''.join([f'<option value="{b.lower()}">{b}</option>' for b in boards])}
  </select>
</div>'''
    
    tier_selector = ''
    if subject['id'] in ["mathematics", "physics", "chemistry", "biology", "combined-science", "statistics"]:
        tier_selector = f'''
<div class="selector-group">
  <label for="tier-select">Tier: </label>
  <select id="tier-select" onchange="updateSubjectUrl()">
    <option value="foundation">Foundation</option>
    <option value="higher">Higher</option>
  </select>
</div>'''
    
    # Find the topic-header section and add selectors after topic-meta
    selector_html = f'''
<div class="selector-bar">
  {board_selector}
  {tier_selector}
</div>'''
    
    # Insert after topic-meta div
    pattern = r'(<div class="topic-meta">.*?</div>)'
    replacement = r'\1' + selector_html
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
# Update topic links to include board/tier
    script = f'''
<script>
function updateSubjectUrl() {{
    const board = document.getElementById('board-select')?.value || 'aqa';
    const tier = document.getElementById('tier-select')?.value || 'foundation';
    
    // Update all topic links
    document.querySelectorAll('.topic-card').forEach(card => {{
        const href = card.getAttribute('href');
        if (href && href.startsWith('topics/')) {{
            // Extract topic file name
            const match = href.match(/topics\\/([^\\/]+)\\/([^\\/]+)\\.html/);
            if (match) {{
                const topicDir = match[1];
                const fileName = match[2];
                const newHref = `topics/{subject_id}/${{board}}/${{tier}}/${{fileName}}`;
                card.setAttribute('href', newHref);
            }}
        }}
    }});
    
    // Set initial values from URL
    const path = window.location.pathname;
    const boardMatch = path.match(/{subject_id}\/([^\\/]+)\//);
    const tierMatch = path.match(/{subject_id}\\/[^\\/]+\\/([^\\/]+)\//);
    if (boardMatch) document.getElementById('board-select').value = boardMatch[1];
    if (tierMatch) document.getElementById('tier-select').value = tierMatch[1];
}}
document.addEventListener('DOMContentLoaded', updateSubjectUrl);
</script>'''
    
    # Insert script before </body>
    content = content.replace('</body>', script + '\n</body>')
    
    # Write updated file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    for subject in data['subjects']:
        subject_id = subject['id']
        update_subject_page(subject_id)
        print(f"Updated {subject_id}.html")

if __name__ == '__main__':
    main()