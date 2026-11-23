import re

def normalize_text(text: str) -> str:
    """Normalize question text by removing punctuation, extra spaces, and lowercasing."""
    if not text:
        return ""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def deduplicate_questions(questions_list):
    """
    Deduplicates a list of question dictionaries based on normalized question strings.
    Returns: (unique_questions, duplicates_count)
    """
    seen = set()
    unique = []
    duplicates_count = 0
    
    for q in questions_list:
        norm = normalize_text(q.get("question", ""))
        if norm in seen:
            duplicates_count += 1
            continue
        seen.add(norm)
        unique.append(q)
        
    return unique, duplicates_count
