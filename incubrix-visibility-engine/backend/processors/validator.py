REQUIRED_QUESTION_FIELDS = [
    "question_id", "question", "intent", "source_type", "source_url", "market",
    "google_position", "answer_box_or_ai_overview", "chatgpt", "gemini",
    "perplexity", "claude_or_copilot", "check_date_day1", "check_date_day2",
    "raw_answers_url"
]

def validate_question_record(q: dict) -> tuple[bool, list[str]]:
    """
    Validates that all mandatory fields are present and non-empty.
    Returns: (is_valid, missing_fields)
    """
    missing = []
    for f in REQUIRED_QUESTION_FIELDS:
        val = q.get(f)
        if val is None or str(val).strip() == "":
            missing.append(f)
            
    is_valid = len(missing) == 0
    return is_valid, missing

def validate_dataset(questions_list):
    """
    Validates a list of questions, separating valid from rejected items.
    """
    valid_items = []
    rejected_items = []
    
    for q in questions_list:
        ok, missing = validate_question_record(q)
        if ok:
            valid_items.append(q)
        else:
            rejected_items.append({"question_id": q.get("question_id"), "missing": missing})
            
    return valid_items, rejected_items
