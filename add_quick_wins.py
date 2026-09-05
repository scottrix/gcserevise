#!/usr/bin/env python3
"""Add quick wins to all GCSE topic pages:
1. Board badges in topic header
2. Exam Questions by Topic section with board-specific links
3. Tier badges for Maths/Science topics
"""

import os
import re
from pathlib import Path

BASE = Path('/home/scott/src/gcserevise')

# Subject -> board mapping (from subjects.json)
SUBJECT_BOARDS = {
    "combined-science": ["AQA", "Edexcel", "OCR", "CCEA"],
    "biology": ["AQA", "Edexcel", "OCR", "CCEA"],
    "chemistry": ["AQA", "Edexcel", "OCR", "CCEA"],
    "physics": ["AQA", "Edexcel", "OCR", "CCEA"],
    "mathematics": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"],
    "english-language": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"],
    "english-literature": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"],
    "history": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"],
    "geography": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"],
    "religious-studies": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"],
    "french": ["AQA", "Edexcel", "Eduqas", "CCEA"],
    "spanish": ["AQA", "Edexcel", "Eduqas", "CCEA"],
    "german": ["AQA", "Edexcel", "Eduqas", "CCEA"],
    "computer-science": ["AQA", "Edexcel", "OCR", "Eduqas"],
    "business": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"],
    "economics": ["AQA", "Edexcel", "OCR", "CCEA"],
    "psychology": ["AQA", "Edexcel", "OCR"],
    "sociology": ["AQA", "Edexcel", "Eduqas"],
    "computer-science": ["AQA", "Edexcel", "OCR", "Eduqas"],
    "pe": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"],
    "religious-studies": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"],
    "citizenship-studies": ["AQA", "Edexcel", "OCR"],
    "media-studies": ["AQA", "Eduqas"],
    "design-and-technology": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"],
    "food-preparation-nutrition": ["AQA", "Edexcel", "OCR", "Eduqas"],
    "dance": ["AQA"],
    "drama": ["AQA", "Edexcel", "OCR"],
    "music": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"],
    "art-and-design": ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"],
    "media-studies": ["AQA", "Eduqas"],
    "food-preparation-nutrition": ["AQA", "Edexcel", "OCR", "Eduqas"],
    "latin": ["Edexcel", "OCR", "Eduqas"],
    "ancient-history": ["OCR"],
    "classical-civilisation": ["OCR"],
    "law": ["AQA"],
    "dance": ["AQA"],
    "film-studies": ["Eduqas"],
    "electronics": ["Eduqas"],
    "engineering": ["AQA", "Edexcel", "CCEA"],
    "statistics": ["AQA", "Edexcel", "CCEA"],
    "astronomy": ["Edexcel"],
    "geology": ["Eduqas"],
    "ancient-history": ["OCR"],
    "classical-civilisation": ["OCR"],
    "law": ["AQA"],
    "dance": ["AQA"],
    "film-studies": ["Eduqas"],
    "electronics": ["Eduqas"],
    "engineering": ["AQA", "Edexcel", "CCEA"],
    "statistics": ["AQA", "Edexcel", "CCEA"],
    "citizenship-studies": ["AQA", "Edexcel", "OCR"],
    "food-preparation-nutrition": ["AQA", "Edexcel", "OCR", "Eduqas"],
    "film-studies": ["Eduqas"],
}

# Topic directories that need tier badges (Foundation/Higher)
TIER_SUBJECTS = {
    "mathematics", "statistics", "combined-science", "biology", "chemistry", "physics"
}

# Subject -> past paper finder URLs
PAST_PAPER_URLS = {
    "AQA": "https://www.aqa.org.uk/find-past-papers-and-mark-schemes",
    "Edexcel": "https://qualifications.pearson.com/en/support/support-topics/exams/past-papers.html",
    "OCR": "https://www.ocr.org.uk/qualifications/past-paper-finder/",
    "Eduqas": "https://www.eduqas.co.uk/qualifications/past-papers/",
    "CCEA": "https://ccea.org.uk/past-papers/",
}

def get_subject_for_topic_dir(topic_dir):
    """Map topic directory to subject"""
    topic_to_subject = {
        # Maths
        "number": "mathematics", "algebra": "mathematics", "ratio": "mathematics",
        "geometry": "mathematics", "probability": "mathematics", "statistics": "mathematics",
        # Science
        "bio-cell": "biology", "bio-organisation": "biology", "bio-infection": "biology",
        "bio-bioenergetics": "biology", "bio-homeostasis": "biology", "bio-inheritance": "biology",
        "bio-ecology": "biology", "chem-atomic": "chemistry", "chem-bonding": "chemistry",
        "chem-quantitative": "chemistry", "chem-changes": "chemistry", "chem-energy": "chemistry",
        "chem-rate": "chemistry", "chem-organic": "chemistry", "chem-analysis": "chemistry",
        "chem-resources": "chemistry", "phys-energy": "physics", "phys-electricity": "physics",
        "phys-particle": "physics", "phys-atomic": "physics", "phys-forces": "physics",
        "phys-waves": "physics", "phys-magnetism": "physics", "phys-energy": "physics",
        "phys-waves": "physics", "combined-science": "combined-science",
        # Other subjects - map directory prefix to subject
    }
    
    # Try exact match first
    if topic_dir in topic_to_subject:
        return topic_to_subject[topic_dir]
    
    # Try prefix matching
    for prefix, subject in topic_to_subject.items():
        if topic_dir.startswith(prefix):
            return subject
    
    # Try to infer from directory name
    if topic_dir.startswith("bio-"):
        return "biology"
    elif topic_dir.startswith("chem-"):
        return "chemistry"
    elif topic_dir.startswith("phys-"):
        return "physics"
    elif topic_dir.startswith("geo-"):
        return "geography"
    elif topic_dir.startswith("hist-") or topic_dir.startswith("ah-"):
        return "history"
    elif topic_dir.startswith("eng-") or topic_dir.startswith("lit-") or topic_dir.startswith("poetry") or topic_dir.startswith("shakespeare"):
        return "english-literature"
    elif topic_dir.startswith("lang-") or topic_dir.startswith("grammar") or topic_dir.startswith("reading") or topic_dir.startswith("writing"):
        return "english-language"
    elif topic_dir.startswith("comp-") or topic_dir.startswith("data-") or topic_dir.startswith("algo-") or topic_dir.startswith("network") or topic_dir.startswith("cyber"):
        return "computer-science"
    elif topic_dir.startswith("bus-") or topic_dir.startswith("ec-"):
        return "business"
    elif topic_dir.startswith("psy-"):
        return "psychology"
    elif topic_dir.startswith("soc-"):
        return "sociology"
    elif topic_dir.startswith("rel-"):
        return "religious-studies"
    elif topic_dir.startswith("geo-"):
        return "geography"
    elif topic_dir.startswith("hist-") or topic_dir.startswith("ah-"):
        return "history"
    elif topic_dir.startswith("pe-") or topic_dir.startswith("phys-"):
        return "pe"
    elif topic_dir.startswith("bs-"):
        return "business"
    elif topic_dir.startswith("ec-"):
        return "economics"
    elif topic_dir.startswith("psy-"):
        return "psychology"
    elif topic_dir.startswith("cit-"):
        return "citizenship-studies"
    elif topic_dir.startswith("med-"):
        return "media-studies"
    elif topic_dir.startswith("dt-") or topic_dir.startswith("eng-") or topic_dir.startswith("dr-"):
        return "design-and-technology"
    elif topic_dir.startswith("fn-"):
        return "food-preparation-nutrition"
    elif topic_dir.startswith("dance"):
        return "dance"
    elif topic_dir.startswith("drama"):
        return "drama"
    elif topic_dir.startswith("mu-"):
        return "music"
    elif topic_dir.startswith("art-") or topic_dir.startswith("ad-"):
        return "art-and-design"
    elif topic_dir.startswith("ms-"):
        return "media-studies"
    elif topic_dir.startswith("fn-"):
        return "food-preparation-nutrition"
    elif topic_dir.startswith("pe-") or topic_dir.startswith("phys-") or topic_dir.startswith("movement") or topic_dir.startswith("sports"):
        return "pe"
    elif topic_dir.startswith("rel-"):
        return "religious-studies"
    elif topic_dir.startswith("cit-"):
        return "citizenship-studies"
    elif topic_dir.startswith("law-"):
        return "law"
    elif topic_dir.startswith("stats-"):
        return "statistics"
    elif topic_dir.startswith("prob") or topic_dir.startswith("ratio"):
        return "mathematics"
    elif topic_dir.startswith("fn-"):
        return "food-preparation-nutrition"
    elif topic_dir.startswith("ast-"):
        return "astronomy"
    elif topic_dir.startswith("geo-"):
        return "geology"
    elif topic_dir.startswith("law-"):
        return "law"
    elif topic_dir.startswith("ancient") or topic_dir.startswith("cc-"):
        return "ancient-history"
    elif topic_dir.startswith("classical") or topic_dir.startswith("cc-"):
        return "classical-civilisation"
    elif topic_dir.startswith("electron"):
        return "electronics"
    elif topic_dir.startswith("eng-"):
        return "engineering"
    elif topic_dir.startswith("film-"):
        return "film-studies"
    elif topic_dir.startswith("latin-"):
        return "latin"
    elif topic_dir.startswith("dance"):
        return "dance"
    elif topic_dir.startswith("drama"):
        return "drama"
    elif topic_dir.startswith("mus-") or topic_dir.startswith("mu-"):
        return "music"
    elif topic_dir.startswith("art-") or topic_dir.startswith("ad-"):
        return "art-and-design"
    elif topic_dir.startswith("ms-"):
        return "media-studies"
    elif topic_dir.startswith("fn-"):
        return "food-preparation-nutrition"
    elif topic_dir.startswith("pe-") or topic_dir.startswith("movement") or topic_dir.startswith("sports"):
        return "pe"
    elif topic_dir.startswith("rel-"):
        return "religious-studies"
    elif topic_dir.startswith("cit-"):
        return "citizenship-studies"
    elif topic_dir.startswith("law-"):
        return "law"
    elif topic_dir.startswith("dance"):
        return "dance"
    elif topic_dir.startswith("drama"):
        return "drama"
    elif topic_dir.startswith("mus-") or topic_dir.startswith("mu-"):
        return "music"
    elif topic_dir.startswith("art-") or topic_dir.startswith("ad-"):
        return "art-and-design"
    elif topic_dir.startswith("ms-"):
        return "media-studies"
    elif topic_dir.startswith("fn-"):
        return "food-preparation-nutrition"
    elif topic_dir.startswith("sp-") or topic_dir.startswith("gm-") or topic_dir.startswith("fr-") or topic_dir.startswith("sp-"):
        # Languages
        if topic_dir.startswith("sp-"):
            return "spanish"
        elif topic_dir.startswith("fr-") or topic_dir.startswith("gm-"):
            return "french" if topic_dir.startswith("fr-") else "german"
        return "french"
    elif topic_dir.startswith("number") or topic_dir.startswith("algebra") or topic_dir.startswith("geometry") or topic_dir.startswith("probability") or topic_dir.startswith("ratio") or topic_dir.startswith("stats"):
        return "mathematics"
    
    return None

def get_boards_for_topic_dir(topic_dir):
    """Get exam boards for a topic directory"""
    subject = get_subject_for_topic_dir(topic_dir)
    if subject and subject in SUBJECT_BOARDS:
        return SUBJECT_BOARDS[subject]
    return ["AQA", "Edexcel", "OCR", "Eduqas", "CCEA"]

def get_tier_badges(topic_dir):
    """Get tier badges for Maths/Science subjects"""
    subject = get_subject_for_topic_dir(topic_dir)
    if subject in TIER_SUBJECTS:
        return '<span class="badge foundation">Foundation</span><span class="badge higher">Higher</span>'
    return ''

def generate_board_badges(boards):
    """Generate board badge HTML"""
    badges = []
    for board in boards:
        badges.append(f'<span class="badge">{board}</span>')
    return ''.join(badges)

def generate_exam_questions_section(boards):
    """Generate Exam Questions by Topic section"""
    items = []
    for board in boards:
        url = PAST_PAPER_URLS.get(board, "")
        if url:
            items.append(f'<li><a href="{url}" target="_blank" rel="noopener">{board} Past Papers - Topic Questions</a> -- {board}</li>')
    
    if not items:
        return ""
    
    return f'''<section class="section">
<h2>📝 Exam Questions by Topic</h2>
<ul>
{"".join(items)}
</ul>
</section>'''

def inject_quick_wins(html, topic_dir):
    """Inject quick wins into topic page HTML"""
    boards = get_boards_for_topic_dir(topic_dir)
    
    # 1. Update topic-meta badges (add board badges, update tier badges)
    tier_badges = get_tier_badges(topic_dir)
    board_badges = generate_board_badges(get_boards_for_topic_dir(topic_dir))
    
    # Update topic-meta div
    # Find the topic-meta div and replace its content
    meta_pattern = r'(<div class="topic-meta">)(.*?)(</div>)'
    def replace_meta(match):
        meta_content = match.group(2)
        # Replace "All Boards" badge with actual board badges
        new_content = meta_content.replace(
            '<span class="badge">All Boards</span>',
            board_badges
        )
        # Update tier badges if present
        if tier_badges and '<span class="badge foundation">' not in new_content:
            # Add tier badges if not present
            new_content = new_content.replace(
                '</div>',
                tier_badges + '</div>'
            )
        return match.group(1) + new_content + match.group(3)
    
    html = re.sub(meta_pattern, replace_meta, html, flags=re.DOTALL)
    
    # 2. Add Exam Questions section after Practice Questions section
    exam_questions_section = generate_exam_questions_section(get_boards_for_topic_dir(topic_dir))
    
    # Find the last </section> before the Video Resources section or share section
    # Insert before Video Resources section
    video_section_pattern = r'(<section class="section">\s*<h2>🎬 Video Resources</h2>)'
    exam_section = f'{generate_exam_questions_section(get_boards_for_topic_dir(topic_dir))}\n\n'
    html = re.sub(video_section_pattern, exam_section + r'\1', html)
    
    return html

def process_topic_page(file_path):
    """Process a single topic page"""
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Determine topic directory from path
    rel_path = file_path.relative_to(BASE / 'topics')
    topic_dir = rel_path.parent.name
    
    # Check if already has Exam Questions section
    if 'Exam Questions by Topic' in html:
        print(f"  Already has quick wins: {file_path}")
        return False
    
    html = inject_quick_wins(html, topic_dir)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return True

def main():
    topics_dir = BASE / 'topics'
    updated = 0
    skipped = 0
    
    for topic_dir in topics_dir.iterdir():
        if not topic_dir.is_dir():
            continue
        
        # Skip board-specific subdirectories
        if topic_dir.name in ['aqa', 'edexcel', 'ocr', 'wjec', 'eduqas', 'ccea']:
            continue
            
        for html_file in topic_dir.glob('*.html'):
            if process_topic_page(html_file):
                updated += 1
            else:
                skipped += 1
    
    print(f"Updated: {updated}, Skipped: {skipped}")

if __name__ == '__main__':
    main()