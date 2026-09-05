#!/usr/bin/env python3
"""Generate board-specific topic pages with proper tier/board structure"""

import json
import shutil
from pathlib import Path

BASE = Path('/home/scott/src/gcserevise')

# Load subjects.json
with open(BASE / 'subjects.json', 'r') as f:
    data = json.load(f)

# Map subject_id to its topic directories
SUBJECT_TOPIC_DIRS = {
    "mathematics": ["number", "algebra", "ratio", "geometry", "probability", "statistics"],
    "statistics": ["statistics", "stats-calculation", "stats-collection", "stats-interpretation", "stats-planning", "stats-presentation", "stats-exam-technique"],
    "biology": ["bio-cell", "bio-organisation", "bio-infection", "bio-bioenergetics", "bio-homeostasis", "bio-inheritance", "bio-ecology", "bioenergetics"],
    "chemistry": ["chem-atomic", "chem-bonding", "chem-quantitative", "chem-changes", "chem-energy", "chem-rate", "chem-organic", "chem-analysis", "chem-resources", "chem-energy", "chemical-changes", "chem-atomic", "organic"],
    "physics": ["phys-energy", "phys-electricity", "phys-particle", "phys-atomic", "phys-forces", "phys-waves", "phys-magnetism", "phys-energy", "phys-waves", "phys-atomic", "phys-forces", "phys-energy", "phys-magnetism", "phys-particle", "phys-waves"],
    "combined-science": ["bio-cell", "bio-organisation", "bio-infection", "bio-bioenergetics", "bio-homeostasis", "bio-inheritance", "bio-ecology", "chem-atomic", "chem-bonding", "chem-quantitative", "chem-changes", "chem-energy", "chem-rate", "chem-organic", "chem-analysis", "chem-resources", "phys-energy", "phys-electricity", "phys-particle", "phys-atomic", "phys-forces", "phys-waves", "phys-magnetism", "phys-energy", "phys-waves"],
    "english-language": ["reading", "writing", "writing-creative", "writing-transactional", "grammar", "spelling", "reading", "spelling"],
    "english-literature": ["shakespeare", "poetry", "modern", "nineteenth-century"],
    "history": ["elizabethan-england", "germany-1890-1945", "inter-war-years", "modern", "medicine", "norman-england", "cold-war", "american-west"],
    "geography": ["geo-tectonics", "geo-surface-processes", "physical-landscapes-uk", "changing-economic-world", "urban-issues", "resource-management", "geo-skills", "fieldwork"],
    "religious-studies": ["christianity-beliefs", "christianity-practices", "islam-beliefs", "islam-practices", "judaism", "religion-life", "religion-peace-conflict", "religion-crime-punishment"],
    "french": ["fr-grammar", "fr-vocab", "fr-listening", "fr-speaking", "fr-reading", "fr-writing"],
    "spanish": ["sp-grammar", "sp-vocab", "sp-listening", "sp-speaking", "sp-reading", "sp-writing"],
    "german": ["gm-grammar", "gm-vocab", "gm-listening", "gm-speaking", "gm-reading", "gm-writing"],
    "computer-science": ["computer-systems", "programming", "data-representation", "networks", "cyber-security", "algorithms", "databases-impacts"],
    "business": ["bs-finance", "bs-human-resources", "bs-influences", "bs-marketing", "bs-operations", "bs-real-world"],
    "economics": ["ec-foundations", "ec-markets", "ec-government", "ec-global", "ec-economy"],
    "psychology": ["ps-approaches", "ps-cognition", "ps-communication", "ps-neuro", "ps-problems", "ps-social"],
    "sociology": ["so-foundations", "so-families", "so-education", "so-crime", "so-stratification", "so-research-methods"],
    "pe": ["applied-anatomy-physiology", "movement-analysis", "physical-training", "sports-psychology", "health-fitness-wellbeing", "socio-cultural-influences"],
    "religious-studies": ["christianity-beliefs", "christianity-practices", "islam-beliefs", "islam-practices", "religion-life", "religion-peace-conflict", "religion-crime-punishment", "judaism"],
    "citizenship-studies": ["ci-active-citizenship", "ci-british-values", "ci-global-citizenship", "ci-law-justice", "ci-politics-participation", "ci-rights-responsibilities"],
    "media-studies": ["ms-key-concepts", "ms-media-forms", "ms-media-representations", "ms-media-industries", "ms-media-audiences"],
    "design-and-technology": ["dt-core-principles", "dt-designing-and-making", "dt-materials", "dt-specialist-technical"],
    "food-preparation-nutrition": ["fn-food-safety", "fn-nutrition-health", "fn-food-choice", "fn-food-provenance", "fn-food-science", "fn-cooking-techniques"],
    "dance": ["dance-performance-skills", "dance-choreography", "dance-dance-contexts", "dance-appreciation", "dance-exam-technique"],
    "drama": ["dr-performing-texts", "dr-devising", "dr-practitioners", "dr-live-theatre", "dr-theatrical-terms", "dr-exam-technique"],
    "music": ["mu-elements", "mu-performing", "mu-composing", "mu-aos1-western-classical", "mu-aos2-popular-music", "mu-aos3-traditional-music", "mu-aos4-classical-since-1910"],
    "art-and-design": ["ad-fine-art", "ad-graphic-communication", "ad-photography", "ad-textile-design", "ad-three-dimensional-design", "ad-art-craft-design"],
    "media-studies": ["ms-key-concepts", "ms-media-forms", "ms-media-representations", "ms-media-industries", "ms-media-audiences"],
    "food-preparation-nutrition": ["fn-food-safety", "fn-nutrition-health", "fn-food-choice", "fn-food-provenance", "fn-food-science", "fn-cooking-techniques"],
    "latin": ["latin-language", "latin-literature-prose", "latin-literature-verse"],
    "ancient-history": ["ah-athens", "ah-greece", "ah-persian-wars", "ah-rome-republic", "ah-rome-emperors", "ah-exam-technique"],
    "classical-civilisation": ["cc-city-rome", "cc-military-rome", "cc-mythology", "cc-homeric-world", "cc-exam-technique"],
    "law": ["law-english-legal-system", "law-criminal-law", "law-civil-law", "law-justice-law-reform", "law-rights-responsibilities", "law-exam-technique"],
    "dance": ["dance-performance-skills", "dance-choreography", "dance-dance-contexts", "dance-appreciation", "dance-exam-technique"],
    "film-studies": ["film-film-language", "film-genres", "film-global-film", "film-uk-film", "film-us-film", "film-exam-technique"],
    "electronics": ["elec-fundamentals", "elec-analogue-systems", "elec-digital-systems", "elec-applications", "elec-practical-circuits", "elec-exam-technique"],
    "engineering": ["eng-materials", "eng-processes", "eng-systems", "eng-testing", "eng-modern-tech", "eng-practical"],
    "statistics": ["stats-calculation", "stats-collection", "stats-interpretation", "stats-planning", "stats-presentation", "stats-exam-technique"],
    "astronomy": ["ast-exploration", "ast-galaxies-cosmology", "ast-observation", "ast-planet-earth", "ast-solar-system", "ast-stars"],
    "geology": ["geo-earth-structure", "geo-geological-time", "geo-minerals-rocks", "geo-surface-processes", "geo-applied-geology", "geo-tectonics"],
    "ancient-history": ["ah-athens", "ah-greece", "ah-persian-wars", "ah-rome-republic", "ah-rome-emperors", "ah-exam-technique"],
    "classical-civilisation": ["cc-city-rome", "cc-military-rome", "cc-mythology", "cc-homeric-world", "cc-exam-technique"],
    "law": ["law-english-legal-system", "law-criminal-law", "law-civil-law", "law-justice-law-reform", "law-rights-responsibilities", "law-exam-technique"],
    "dance": ["dance-performance-skills", "dance-choreography", "dance-dance-contexts", "dance-appreciation", "dance-exam-technique"],
    "film-studies": ["film-film-language", "film-genres", "film-global-film", "film-uk-film", "film-us-film", "film-exam-technique"],
    "electronics": ["elec-fundamentals", "elec-analogue-systems", "elec-digital-systems", "elec-applications", "elec-practical-circuits", "elec-exam-technique"],
    "engineering": ["eng-materials", "eng-processes", "eng-systems", "eng-testing", "eng-modern-tech", "eng-practical"],
    "statistics": ["stats-calculation", "stats-collection", "stats-interpretation", "stats-planning", "stats-presentation", "stats-exam-technique"],
    "citizenship-studies": ["ci-active-citizenship", "ci-british-values", "ci-global-citizenship", "ci-law-justice", "ci-politics-participation", "ci-rights-responsibilities"],
    "food-preparation-nutrition": ["fn-food-safety", "fn-nutrition-health", "fn-food-choice", "fn-food-provenance", "fn-food-science", "fn-cooking-techniques"],
    "film-studies": ["film-film-language", "film-genres", "film-global-film", "film-uk-film", "film-us-film", "film-exam-technique"],
    "electronics": ["elec-fundamentals", "elec-analogue-systems", "elec-digital-systems", "elec-applications", "elec-practical-circuits", "elec-exam-technique"],
    "engineering": ["eng-materials", "eng-processes", "eng-systems", "eng-testing", "eng-modern-tech", "eng-practical"],
    "statistics": ["stats-calculation", "stats-collection", "stats-interpretation", "stats-planning", "stats-presentation", "stats-exam-technique"],
    "citizenship-studies": ["ci-active-citizenship", "ci-british-values", "ci-global-citizenship", "ci-law-justice", "ci-politics-participation", "ci-rights-responsibilities"],
    "food-preparation-nutrition": ["fn-food-safety", "fn-nutrition-health", "fn-food-choice", "fn-food-provenance", "fn-food-science", "fn-cooking-techniques"],
    "film-studies": ["film-film-language", "film-genres", "film-global-film", "film-uk-film", "film-us-film", "film-exam-technique"],
    "electronics": ["elec-fundamentals", "elec-analogue-systems", "elec-digital-systems", "elec-applications", "elec-practical-circuits", "elec-exam-technique"],
    "engineering": ["eng-materials", "eng-processes", "eng-systems", "eng-testing", "eng-modern-tech", "eng-practical"],
    "statistics": ["stats-calculation", "stats-collection", "stats-interpretation", "stats-planning", "stats-presentation", "stats-exam-technique"],
}

# Subjects with tiers
TIER_SUBJECTS = {"mathematics", "physics", "chemistry", "biology", "combined-science", "statistics"}

def main():
    with open('/home/scott/src/gcserevise/subjects.json', 'r') as f:
        data = json.load(f)
    
    BASE_TOPICS = Path('/home/scott/src/gcserevise/topics')
    
    for subject in data['subjects']:
        subject_id = subject['id']
        subject_name = subject['name']
        boards = subject.get('boards', [])
        
        # Get topic directories for this subject
        topic_dirs = SUBJECT_TOPIC_DIRS.get(subject_id, [])
        if not topic_dirs:
            # Try to infer from subject_id
            topic_dirs = [d for d in Path('/home/scott/src/gcserevise/topics').iterdir() 
                         if d.is_dir() and d.name.startswith(subject_id[:3])]
            topic_dirs = [d.name for d in topic_dirs]
        
        if not topic_dirs:
            print(f"No topic dirs found for {subject_id}")
            continue
        
        # Determine if subject has tiers
        has_tiers = subject_id in TIER_SUBJECTS
        
        for board in subject.get('boards', []):
            board_slug = board.lower()
            
            if has_tiers:
                for tier in ['foundation', 'higher']:
                    tier_dir = BASE / 'topics' / subject_id / board.lower() / tier
                    tier_dir.mkdir(parents=True, exist_ok=True)
                    
                    # Copy topic files from all topic dirs for this subject
                    for topic_dir_name in topic_dirs:
                        topic_dir = Path('/home/scott/src/gcserevise/topics') / topic_dir_name
                        if not topic_dir.exists():
                            continue
                        
                        for html_file in topic_dir.glob('*.html'):
                            dest = tier_dir / html_file.name
                            if not dest.exists():
                                shutil.copy2(html_file, dest)
                                print(f"Copied {html_file.name} -> {tier_dir.name}/{dest.name}")
            else:
                # No tiers - just board
                board_dir = BASE / 'topics' / subject_id / board.lower()
                board_dir.mkdir(parents=True, exist_ok=True)
                
                for topic_dir_name in topic_dirs:
                    topic_dir = Path('/home/scott/src/gcserevise/topics') / topic_dir_name
                    if not topic_dir.exists():
                        continue
                    
                    for html_file in topic_dir.glob('*.html'):
                        dest = board_dir / html_file.name
                        if not dest.exists():
                            shutil.copy2(html_file, dest)
                            print(f"Copied {html_file.name} -> {board_dir.name}/{dest.name}")

    print("Board/tier directory structure created and files copied")

if __name__ == '__main__':
    main()