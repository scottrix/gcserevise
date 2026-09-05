#!/usr/bin/env python3
"""Fix relative paths in board/tier topic files (depth >= 4 from topics root)"""

import os
import re
from pathlib import Path

BASE = Path('/home/scott/src/gcserevise/topics')

def fix_relative_paths(content, depth):
    """Fix relative paths based on depth from site root"""
    # depth = number of directory levels from site root (gcserevise/)
    # e.g., topics/mathematics/aqa/foundation/A1.html -> depth = 5
    levels_up = depth
    root_prefix = '../' * levels_up
    
    content = content
    
    # Fix style.css reference
    content = re.sub(r'href="\.\./style\.css"', f'href="{ "../" * levels_up }style.css"', content)
    content = re.sub(r'href="\.\./\.\./style\.css"', f'href="{ "../" * levels_up }style.css"', content)
    
    # Fix subject landing page links: ../../subject.html -> ../../../../subject.html
    subjects = [
        'mathematics', 'english-language', 'english-literature', 'biology', 'chemistry', 'physics',
        'combined-science', 'computer-science', 'history', 'geography', 'religious-studies',
        'french', 'spanish', 'german', 'latin', 'computer-science', 'business', 'economics',
        'psychology', 'sociology', 'citizenship-studies', 'media-studies', 'design-and-technology',
        'food-preparation-nutrition', 'dance', 'drama', 'music', 'art-and-design', 'media-studies',
        'food-preparation-nutrition', 'pe', 'business', 'economics', 'psychology', 'sociology',
        'citizenship-studies', 'film-studies', 'electronics', 'engineering', 'statistics',
        'astronomy', 'geology', 'ancient-history', 'classical-civilisation', 'law', 'dance',
        'film-studies', 'electronics', 'engineering', 'statistics', 'citizenship-studies',
        'food-preparation-nutrition', 'film-studies', 'electronics', 'engineering', 'statistics'
    ]
    
    for subj in subjects:
        # ../../subject.html -> ../../../../subject.html
        content = content.replace(f'href="../../{subj}.html"', f'href="{ "../" * 4 }{subj}.html"')
        content = content.replace(f'href="../../{subj}.html#', f'href="../../../../{subj}.html#')
    
    # Fix combined-science specifically
    content = content.replace('href="../../combined-science.html"', 'href="../../../../combined-science.html"')
    content = content.replace('href="../../combined-science.html#', 'href="../../../../combined-science.html#')
    
    # Fix anchor links
    content = content.replace('href="../../mathematics.html#', 'href="../../../../mathematics.html#')
    content = content.replace('href="../../english-language.html#', 'href="../../../../english-language.html#')
    content = content.replace('href="../../english-literature.html#', 'href="../../../../english-literature.html#')
    content = content.replace('href="../../biology.html#', 'href="../../../../biology.html#')
    content = content.replace('href="../../chemistry.html#', 'href="../../../../chemistry.html#')
    content = content.replace('href="../../physics.html#', 'href="../../../../physics.html#')
    content = content.replace('href="../../combined-science.html#', 'href="../../../../combined-science.html#')
    content = content.replace('href="../../computer-science.html#', 'href="../../../../computer-science.html#')
    content = content.replace('href="../../english-language.html#', 'href="../../../../english-language.html#')
    content = content.replace('href="../../english-literature.html#', 'href="../../../../english-literature.html#')
    content = content.replace('href="../../history.html#', 'href="../../../../history.html#')
    content = content.replace('href="../../geography.html#', 'href="../../../../geography.html#')
    content = content.replace('href="../../religious-studies.html#', 'href="../../../../religious-studies.html#')
    content = content.replace('href="../../french.html#', 'href="../../../../french.html#')
    content = content.replace('href="../../spanish.html#', 'href="../../../../spanish.html#')
    content = content.replace('href="../../german.html#', 'href="../../../../german.html#')
    content = content.replace('href="../../latin.html#', 'href="../../../../latin.html#')
    content = content.replace('href="../../computer-science.html#', 'href="../../../../computer-science.html#')
    content = content.replace('href="../../business.html#', 'href="../../../../business.html#')
    content = content.replace('href="../../economics.html#', 'href="../../../../economics.html#')
    content = content.replace('href="../../psychology.html#', 'href="../../../../psychology.html#')
    content = content.replace('href="../../sociology.html#', 'href="../../../../sociology.html#')
    content = content.replace('href="../../citizenship-studies.html#', 'href="../../../../citizenship-studies.html#')
    content = content.replace('href="../../media-studies.html#', 'href="../../../../media-studies.html#')
    content = content.replace('href="../../design-and-technology.html#', 'href="../../../../design-and-technology.html#')
    content = content.replace('href="../../food-preparation-nutrition.html#', 'href="../../../../food-preparation-nutrition.html#')
    content = content.replace('href="../../pe.html#', 'href="../../../../pe.html#')
    content = content.replace('href="../../business.html#', 'href="../../../../business.html#')
    content = content.replace('href="../../economics.html#', 'href="../../../../economics.html#')
    content = content.replace('href="../../psychology.html#', 'href="../../../../psychology.html#')
    content = content.replace('href="../../sociology.html#', 'href="../../../../sociology.html#')
    content = content.replace('href="../../citizenship-studies.html#', 'href="../../../../citizenship-studies.html#')
    content = content.replace('href="../../media-studies.html#', 'href="../../../../media-studies.html#')
    content = content.replace('href="../../food-preparation-nutrition.html#', 'href="../../../../food-preparation-nutrition.html#')
    content = content.replace('href="../../film-studies.html#', 'href="../../../../film-studies.html#')
    content = content.replace('href="../../electronics.html#', 'href="../../../../electronics.html#')
    content = content.replace('href="../../engineering.html#', 'href="../../../../engineering.html#')
    content = content.replace('href="../../statistics.html#', 'href="../../../../statistics.html#')
    content = content.replace('href="../../citizenship-studies.html#', 'href="../../../../citizenship-studies.html#')
    content = content.replace('href="../../food-preparation-nutrition.html#', 'href="../../../../food-preparation-nutrition.html#')
    content = content.replace('href="../../film-studies.html#', 'href="../../../../film-studies.html#')
    content = content.replace('href="../../electronics.html#', 'href="../../../../electronics.html#')
    content = content.replace('href="../../engineering.html#', 'href="../../../../engineering.html#')
    content = content.replace('href="../../statistics.html#', 'href="../../../../statistics.html#')
    content = content.replace('href="../../citizenship-studies.html#', 'href="../../../../citizenship-studies.html#')
    content = content.replace('href="../../food-preparation-nutrition.html#', 'href="../../../../food-preparation-nutrition.html#')
    content = content.replace('href="../../film-studies.html#', 'href="../../../../film-studies.html#')
    content = content.replace('href="../../electronics.html#', 'href="../../../../electronics.html#')
    content = content.replace('href="../../engineering.html#', 'href="../../../../engineering.html#')
    content = content.replace('href="../../statistics.html#', 'href="../../../../statistics.html#')
    
    return content

def main():
    BASE = Path('/home/scott/src/gcserevise/topics')
    
    updated = 0
    for file_path in BASE.rglob('*.html'):
        # Only process files in board/tier directories (depth >= 4 from topics root)
        rel = file_path.relative_to(BASE)
        parts = rel.parts
        
        # Check if in board/tier structure (depth >= 3: subject/board/tier/file.html or subject/board/file.html)
        if len(parts) >= 4:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = fix_relative_paths(content, 4)  # depth 4 for board/tier files
            
            if content != new_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed: {file_path.relative_to(Path('/home/scott/src/gcserevise/topics'))}")
    
    print("Done fixing paths")

if __name__ == '__main__':
    main()