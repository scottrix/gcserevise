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
    
    # Generate board selector
    board_options = ''.join(f'<option value="{board.lower()}">{board}</option>' for board in boards)
    board_selector = f'''<div class="selector-group">
  <label for="board-select">Exam Board: </label>
  <select id="board-select" onchange="updateSubjectUrl()">
    {board_options}
  </select>
</div>'''
    
    tier_selector = ''
    if subject['id'] in ["mathematics", "physics", "chemistry", "biology", "combined-science", "statistics"]:
        tier_selector = '''<div class="selector-group">
  <label for="tier-select">Tier: </label>
  <select id="tier-select" onchange="updateSubjectUrl()">
    <option value="foundation">Foundation</option>
    <option value="higher">Higher</option>
  </select>
</div>'''
    
    # Find the topic-header section and add selectors after topic-meta
    selector_html = f'''<div class="selector-bar">
  <div class="selector-group">
    <label for="board-select">Exam Board: </label>
    <select id="board-select" onchange="updateSubjectUrl()">
      {''.join(f'<option value="{b.lower()}">{b}</option>' for b in boards)}
    </select>
  </div>
  <div class="selector-group">
    <label for="tier-select">Tier: </label>
    <select id="tier-select" onchange="updateSubjectUrl()">
      <option value="foundation">Foundation</option>
      <option value="higher">Higher</option>
    </select>
  </div>
</div>''' if subject['id'] in ["mathematics", "physics", "chemistry", "biology", "combined-science", "statistics"] else f'''<div class="selector-bar">
  <div class="selector-group">
    <label for="board-select">Exam Board: </label>
    <select id="board-select" onchange="updateSubjectUrl()">
      {''.join(f'<option value="{b.lower()}">{b}</option>' for b in boards)}
    </select>
  </div>
</div>'''
    
    # Insert after topic-meta div
    pattern = r'(<div class="topic-meta">.*?</div>)'
    replacement = r'\1' + selector_html
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Add JavaScript to handle URL updates
    script = f'''<script>
function updateSubjectUrl() {{
    const board = document.getElementById('board-select')?.value || 'aqa';
    const tier = document.getElementById('tier-select')?.value || 'foundation';
    
    // Update all topic links
    document.querySelectorAll('.topic-card').forEach(card => {{
        const href = card.getAttribute('href');
        if (href && href.startsWith('topics/')) {{
            const match = href.match(/topics\\/([^\\/]+)\\/([^\\/]+)\\.html/);
            if (match) {{
                const fileName = match[2];
                const newHref = `topics/{subject_id}/${{board}}/${{tier}}/${{fileName}}`;
                card.setAttribute('href', newHref);
            }}
        }}
    }});
    
    // Set initial values from URL
    const path = window.location.pathname;
    const boardMatch = path.match(/{subject_id}\/([^/]+)\//);
    const tierMatch = path.match(/{subject_id}\/[^/]+\/([^/]+)\//);
    if (boardMatch) document.getElementById('board-select').value = boardMatch[1];
    if (tierMatch) document.getElementById('tier-select').value = tierMatch[1];
}}
document.addEventListener('DOMContentLoaded', updateSubjectUrl);
</script>'''
    
    # Remove any existing updateSubjectUrl function to avoid duplicates
    content = re.sub(r'<script[^>]*>[\s\S]*?updateSubjectUrl[\s\S]*?</script>', '', content, flags=re.DOTALL)
    
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