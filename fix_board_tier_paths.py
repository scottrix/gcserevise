#!/usr/bin/env python3
"""Fix relative paths in board/tier topic files"""

import os
import re
from pathlib import Path

BASE = Path('/home/scott/src/gcserevise/topics')

def fix_relative_paths(file_path):
    """Fix relative paths in a topic file based on its depth"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Calculate depth from site root (gcserevise/)
    # Structure: /topics/{subject}/{board}/{tier}/{file}.html or /topics/{subject}/{board}/{file}.html
    rel_path = file_path.relative_to(Path('/home/scott/src/gcserevise'))
    parts = rel_path.parts
    
    # Count depth from site root (gcserevise/)
    # parts[0] = 'topics', parts[1] = subject, parts[2] = board, [3] = tier (optional), [4] = file.html
    depth = len(parts) - 1  # -1 for the file itself
    
    # Calculate how many levels up to reach site root
    levels_up = depth
    
    # Build the correct prefix for site root
    root_prefix = '../' * levels_up
    
    # Fix style.css reference
    content = re.sub(
        r'(href|src)="\.\./style\.css"',
        f'\\1="{root_prefix}style.css"',
        content
    )
    
    # Fix subject landing page links (e.g., ../../mathematics.html)
    content = re.sub(
        r'(href)="\.\./([a-z-]+)\.html"',
        lambda m: f'href="{root_prefix}{m.group(2)}.html"',
        content
    )
    
    # Fix subject landing page links with category anchor (e.g., ../../mathematics.html#algebra)
    content = re.sub(
        r'(href)="\.\./([a-z-]+)\.html#([a-z-]+)"',
        lambda m: f'href="{root_prefix}{m.group(2)}.html#{m.group(3)}"',
        content
    )
    
    # Fix relative links to other topic pages in same subject (e.g., ../algebra/A2-substitution.html)
    # These should now point to the board/tier structure
    # This is complex - for now, just fix the main references
    
    # Fix CSS reference
    content = content.replace('href="../../style.css"', f'href="../../../../../style.css"')
    content = content.replace('href="../../../style.css"', f'href="../../../../../style.css"')
    
    # Fix subject landing page links
    # ../../mathematics.html -> ../../../../mathematics.html
    content = content.replace('href="../../mathematics.html"', 'href="../../../../../mathematics.html"')
    content = content.replace('href="../../english-language.html"', 'href="../../../../../english-language.html"')
    content = content.replace('href="../../english-literature.html"', 'href="../../../../../english-literature.html"')
    content = content.replace('href="../../biology.html"', 'href="../../../../../biology.html"')
    content = content.replace('href="../../chemistry.html"', 'href="../../../../../chemistry.html"')
    content = content.replace('href="../../physics.html"', 'href="../../../../../physics.html"')
    content = content.replace('href="../../combined-science.html"', 'href="../../../../../combined-science.html"')
    content = content.replace('href="../../computer-science.html"', 'href="../../../../../computer-science.html"')
    content = content.replace('href="../../english-language.html"', 'href="../../../../../english-language.html"')
    content = content.replace('href="../../english-literature.html"', 'href="../../../../../english-literature.html"')
    content = content.replace('href="../../history.html"', 'href="../../../../../history.html"')
    content = content.replace('href="../../geography.html"', 'href="../../../../../geography.html"')
    content = content.replace('href="../../religious-studies.html"', 'href="../../../../../religious-studies.html"')
    content = content.replace('href="../../french.html"', 'href="../../../../../french.html"')
    content = content.replace('href="../../spanish.html"', 'href="../../../../../spanish.html"')
    content = content.replace('href="../../german.html"', 'href="../../../../../german.html"')
    content = content.replace('href="../../latin.html"', 'href="../../../../../latin.html"')
    content = content.replace('href="../../computer-science.html"', 'href="../../../../../computer-science.html"')
    content = content.replace('href="../../business.html"', 'href="../../../../../business.html"')
    content = content.replace('href="../../economics.html"', 'href="../../../../../economics.html"')
    content = content.replace('href="../../psychology.html"', 'href="../../../../../psychology.html"')
    content = content.replace('href="../../sociology.html"', 'href="../../../../../sociology.html"')
    content = content.replace('href="../../citizenship-studies.html"', 'href="../../../../../citizenship-studies.html"')
    content = content.replace('href="../../media-studies.html"', 'href="../../../../../media-studies.html"')
    content = content.replace('href="../../design-and-technology.html"', 'href="../../../../../design-and-technology.html"')
    content = content.replace('href="../../food-preparation-nutrition.html"', 'href="../../../../../food-preparation-nutrition.html"')
    content = content.replace('href="../../dance.html"', 'href="../../../../../dance.html"')
    content = content.replace('href="../../drama.html"', 'href="../../../../../drama.html"')
    content = content.replace('href="../../music.html"', 'href="../../../../../music.html"')
    content = content.replace('href="../../art-and-design.html"', 'href="../../../../../art-and-design.html"')
    content = content.replace('href="../../media-studies.html"', 'href="../../../../../media-studies.html"')
    content = content.replace('href="../../food-preparation-nutrition.html"', 'href="../../../../../food-preparation-nutrition.html"')
    content = content.replace('href="../../pe.html"', 'href="../../../../../pe.html"')
    content = content.replace('href="../../business.html"', 'href="../../../../../business.html"')
    content = content.replace('href="../../economics.html"', 'href="../../../../../economics.html"')
    content = content.replace('href="../../psychology.html"', 'href="../../../../../psychology.html"')
    content = content.replace('href="../../sociology.html"', 'href="../../../../../sociology.html"')
    content = content.replace('href="../../citizenship-studies.html"', 'href="../../../../../citizenship-studies.html')
    content = content.replace('href="../../media-studies.html"', 'href="../../../../../media-studies.html"')
    content = content.replace('href="../../food-preparation-nutrition.html"', 'href="../../../../../food-preparation-nutrition.html"')
    content = content.replace('href="../../film-studies.html"', 'href="../../../../../film-studies.html"')
    content = content.replace('href="../../electronics.html"', 'href="../../../../../electronics.html"')
    content = content.replace('href="../../engineering.html"', 'href="../../../../../engineering.html"')
    content = content.replace('href="../../statistics.html"', 'href="../../../../../statistics.html"')
    content = content.replace('href="../../astronomy.html"', 'href="../../../../../astronomy.html"')
    content = content.replace('href="../../geology.html"', 'href="../../../../../geology.html"')
    content = content.replace('href="../../ancient-history.html"', 'href="../../../../../ancient-history.html"')
    content = content.replace('href="../../classical-civilisation.html"', 'href="../../../../../classical-civilisation.html"')
    content = content.replace('href="../../law.html"', 'href="../../../../../law.html"')
    content = content.replace('href="../../dance.html"', 'href="../../../../../dance.html"')
    content = content.replace('href="../../film-studies.html"', 'href="../../../../../film-studies.html"')
    content = content.replace('href="../../electronics.html"', 'href="../../../../../electronics.html"')
    content = content.replace('href="../../engineering.html"', 'href="../../../../../engineering.html"')
    content = content.replace('href="../../statistics.html"', 'href="../../../../../statistics.html"')
    content = content.replace('href="../../citizenship-studies.html"', 'href="../../../../../citizenship-studies.html"')
    content = content.replace('href="../../food-preparation-nutrition.html"', 'href="../../../../../food-preparation-nutrition.html"')
    content = content.replace('href="../../film-studies.html"', 'href="../../../../../film-studies.html"')
    content = content.replace('href="../../electronics.html"', 'href="../../../../../electronics.html"')
    content = content.replace('href="../../engineering.html"', 'href="../../../../../engineering.html"')
    content = content.replace('href="../../statistics.html"', 'href="../../../../../statistics.html"')
    content = content.replace('href="../../citizenship-studies.html"', 'href="../../../../../citizenship-studies.html"')
    content = content.replace('href="../../food-preparation-nutrition.html"', 'href="../../../../../food-preparation-nutrition.html"')
    content = content.replace('href="../../film-studies.html"', 'href="../../../../../film-studies.html"')
    content = content.replace('href="../../electronics.html"', 'href="../../../../../electronics.html"')
    content = content.replace('href="../../engineering.html"', 'href="../../../../../engineering.html"')
    content = content.replace('href="../../statistics.html"', 'href="../../../../../statistics.html"')
    
    # Fix subject landing page links with anchors
    content = content.replace('href="../../mathematics.html#', 'href="../../../../../mathematics.html#')
    content = content.replace('href="../../english-language.html#', 'href="../../../../../english-language.html#')
    content = content.replace('href="../../english-literature.html#', 'href="../../../../../english-literature.html#')
    content = content.replace('href="../../biology.html#', 'href="../../../../../biology.html#')
    content = content.replace('href="../../chemistry.html#', 'href="../../../../../chemistry.html#')
    content = content.replace('href="../../physics.html#', 'href="../../../../../physics.html#')
    content = content.replace('href="../../combined-science.html#', 'href="../../../../../combined-science.html#')
    content = content.replace('href="../../computer-science.html#', 'href="../../../../../computer-science.html#')
    content = content.replace('href="../../english-language.html#', 'href="../../../../../english-language.html#')
    content = content.replace('href="../../english-literature.html#', 'href="../../../../../english-literature.html#')
    content = content.replace('href="../../history.html#', 'href="../../../../../history.html#')
    content = content.replace('href="../../geography.html#', 'href="../../../../../geography.html#')
    content = content.replace('href="../../religious-studies.html#', 'href="../../../../../religious-studies.html#')
    content = content.replace('href="../../french.html#', 'href="../../../../../french.html#')
    content = content.replace('href="../../spanish.html#', 'href="../../../../../spanish.html#')
    content = content.replace('href="../../german.html#', 'href="../../../../../german.html#')
    content = content.replace('href="../../latin.html#', 'href="../../../../../latin.html#')
    content = content.replace('href="../../computer-science.html#', 'href="../../../../../computer-science.html#')
    content = content.replace('href="../../business.html#', 'href="../../../../../business.html#')
    content = content.replace('href="../../economics.html#', 'href="../../../../../economics.html#')
    content = content.replace('href="../../psychology.html#', 'href="../../../../../psychology.html#')
    content = content.replace('href="../../sociology.html#', 'href="../../../../../sociology.html#')
    content = content.replace('href="../../citizenship-studies.html#', 'href="../../../../../citizenship-studies.html#')
    content = content.replace('href="../../media-studies.html#', 'href="../../../../../media-studies.html#')
    content = content.replace('href="../../design-and-technology.html#', 'href="../../../../../design-and-technology.html#')
    content = content.replace('href="../../food-preparation-nutrition.html#', 'href="../../../../../food-preparation-nutrition.html#')
    content = content.replace('href="../../pe.html#', 'href="../../../../../pe.html#')
    content = content.replace('href="../../business.html#', 'href="../../../../../business.html#')
    content = content.replace('href="../../economics.html#', 'href="../../../../../economics.html#')
    content = content.replace('href="../../psychology.html#', 'href="../../../../../psychology.html#')
    content = content.replace('href="../../sociology.html#', 'href="../../../../../sociology.html#')
    content = content.replace('href="../../citizenship-studies.html#', 'href="../../../../../citizenship-studies.html#')
    content = content.replace('href="../../media-studies.html#', 'href="../../../../../media-studies.html#')
    content = content.replace('href="../../food-preparation-nutrition.html#', 'href="../../../../../food-preparation-nutrition.html#')
    content = content.replace('href="../../film-studies.html#', 'href="../../../../../film-studies.html#')
    content = content.replace('href="../../electronics.html#', 'href="../../../../../electronics.html#')
    content = content.replace('href="../../engineering.html#', 'href="../../../../../engineering.html#')
    content = content.replace('href="../../statistics.html#', 'href="../../../../../statistics.html#')
    content = content.replace('href="../../citizenship-studies.html#', 'href="../../../../../citizenship-studies.html#')
    content = content.replace('href="../../food-preparation-nutrition.html#', 'href="../../../../../food-preparation-nutrition.html#')
    content = content.replace('href="../../film-studies.html#', 'href="../../../../../film-studies.html#')
    content = content.replace('href="../../electronics.html#', 'href="../../../../../electronics.html#')
    content = content.replace('href="../../engineering.html#', 'href="../../../../../engineering.html#')
    content = content.replace('href="../../statistics.html#', 'href="../../../../../statistics.html#')
    content = content.replace('href="../../citizenship-studies.html#', 'href="../../../../../citizenship-studies.html#')
    content = content.replace('href="../../food-preparation-nutrition.html#', 'href="../../../../../food-preparation-nutrition.html#')
    content = content.replace('href="../../film-studies.html#', 'href="../../../../../film-studies.html#')
    content = content.replace('href="../../electronics.html#', 'href="../../../../../electronics.html#')
    content = content.replace('href="../../engineering.html#', 'href="../../../../../engineering.html#')
    content = content.replace('href="../../statistics.html#', 'href="../../../../../statistics.html#')
    
    # Fix breadcrumb links - they point to subject pages
    # ../../mathematics.html -> ../../../../mathematics.html
    # Already handled above
    
    # Fix breadcrumb algebra link (../../combined-science.html#bio-cell -> ../../../../combined-science.html#bio-cell)
    content = content.replace('href="../../combined-science.html#bio-cell"', 'href="../../../../../combined-science.html#bio-cell"')
    content = content.replace('href="../../mathematics.html#algebra"', 'href="../../../../../mathematics.html#algebra"')
    content = content.replace('href="../../mathematics.html#number"', 'href="../../../../../mathematics.html#number"')
    content = content.replace('href="../../mathematics.html#geometry"', 'href="../../../../../mathematics.html#geometry"')
    content = content.replace('href="../../mathematics.html#probability"', 'href="../../../../../mathematics.html#probability"')
    content = content.replace('href="../../mathematics.html#statistics"', 'href="../../../../../mathematics.html#statistics"')
    content = content.replace('href="../../combined-science.html#bio-cell"', 'href="../../../../../combined-science.html#bio-cell"')
    content = content.replace('href="../../combined-science.html#chem-"', 'href="../../../../../combined-science.html#chem-"')
    content = content.replace('href="../../combined-science.html#phys-"', 'href="../../../../../combined-science.html#phys-"')
    
    return content

def main():
    BASE = Path('/home/scott/src/gcserevise/topics')
    
    updated = 0
    for file_path in BASE.rglob('*.html'):
        # Only process files in board/tier directories
        rel = file_path.relative_to(Path('/home/scott/src/gcserevise/topics'))
        parts = rel.parts
        
        # Check if in board/tier structure (depth >= 3: subject/board/tier/file.html)
        if len(parts) >= 4:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = fix_relative_paths(content)
            
            if content != new_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed: {file_path.relative_to(Path('/home/scott/src/gcserevise/topics'))}")
    
    print("Done fixing paths")

if __name__ == '__main__':
    main()