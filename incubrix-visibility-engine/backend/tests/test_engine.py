import pytest
from backend.processors.deduplicator import deduplicate_questions, normalize_text
from backend.processors.validator import validate_question_record, validate_dataset
from backend.scoring.visibility_scorer import calculate_question_score, compute_aggregate_metrics

def test_normalize_text():
    assert normalize_text("  How To Make Shorts?!! ") == "how to make shorts"
    assert normalize_text("Opus Clip vs. Descript") == "opus clip vs descript"

def test_deduplicator():
    sample = [
        {"question_id": "Q01", "question": "How to make shorts?"},
        {"question_id": "Q02", "question": "how to make shorts"},  # duplicate
        {"question_id": "Q03", "question": "Best AI video tool"}
    ]
    unique, dup_count = deduplicate_questions(sample)
    assert len(unique) == 2
    assert dup_count == 1
    assert unique[0]["question_id"] == "Q01"
    assert unique[1]["question_id"] == "Q03"

def test_validator():
    valid_record = {
        "question_id": "Q001",
        "question": "How to edit video?",
        "intent": "Informational",
        "source_type": "PAA",
        "source_url": "https://google.com",
        "market": "United States",
        "google_position": 1,
        "answer_box_or_ai_overview": "AI Overview",
        "chatgpt": "Yes",
        "gemini": "No",
        "perplexity": "Yes",
        "claude_or_copilot": "No",
        "check_date_day1": "2026-11-15",
        "check_date_day2": "2026-11-17",
        "raw_answers_url": "evidence/raw_answers/Q001.json"
    }
    is_valid, missing = validate_question_record(valid_record)
    assert is_valid is True
    assert len(missing) == 0

    invalid_record = valid_record.copy()
    invalid_record["market"] = ""
    is_valid, missing = validate_question_record(invalid_record)
    assert is_valid is False
    assert "market" in missing

def test_scoring():
    record = {
        "google_position": 2,  # 20 pts
        "answer_box_or_ai_overview": "AI Overview",
        "quoted_source_url": "https://incubrix.com/guide",  # 30 pts
        "chatgpt": "Yes",  # 12.5 pts
        "gemini": "Yes",   # 12.5 pts
        "perplexity": "No",
        "claude_or_copilot": "No"
    }
    score = calculate_question_score(record)
    assert score == 75.0
