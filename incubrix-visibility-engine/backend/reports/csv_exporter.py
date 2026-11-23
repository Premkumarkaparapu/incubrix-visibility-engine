import csv
import io

CSV_HEADERS = [
    "question_id", "question", "intent", "source_type", "source_url", "market",
    "google_position", "answer_box_or_ai_overview", "quoted_source_url",
    "chatgpt", "gemini", "perplexity", "claude_or_copilot",
    "competitors_named", "check_date_day1", "check_date_day2", "changed_on_day2",
    "raw_answers_url", "priority", "notes"
]

def export_questions_to_csv_string(questions_list) -> str:
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=CSV_HEADERS)
    writer.writeheader()
    for q in questions_list:
        row = {h: q.get(h, "") for h in CSV_HEADERS}
        writer.writerow(row)
    return output.getvalue()
