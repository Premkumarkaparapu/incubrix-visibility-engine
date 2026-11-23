import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "incubrix_visibility.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Questions & Measurements
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        question_id TEXT PRIMARY KEY,
        question TEXT NOT NULL,
        intent TEXT,
        source_type TEXT,
        source_url TEXT,
        market TEXT,
        google_position INTEGER DEFAULT 0,
        answer_box_or_ai_overview TEXT,
        quoted_source_url TEXT,
        chatgpt TEXT DEFAULT 'No',
        gemini TEXT DEFAULT 'No',
        perplexity TEXT DEFAULT 'No',
        claude_or_copilot TEXT DEFAULT 'No',
        competitors_named TEXT,
        check_date_day1 TEXT,
        check_date_day2 TEXT,
        changed_on_day2 TEXT DEFAULT 'No',
        raw_answers_url TEXT,
        priority TEXT DEFAULT 'Medium',
        notes TEXT
    )
    """)
    
    # Technical Fixes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS technical_fixes (
        fix_id TEXT PRIMARY KEY,
        page_url TEXT,
        problem TEXT,
        evidence_url TEXT,
        fix_summary TEXT,
        code_or_text_url TEXT,
        validator_used TEXT,
        validated TEXT DEFAULT 'Yes',
        impact TEXT,
        effort TEXT
    )
    """)
    
    # Content Pages & Citations
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pages_citations (
        item_id TEXT PRIMARY KEY,
        type TEXT,
        target_question_ids TEXT,
        title_or_page_url TEXT,
        draft_or_evidence_url TEXT,
        why_it_matters TEXT,
        angle_or_schema TEXT,
        sources_cited TEXT,
        status TEXT
    )
    """)
    
    # Run Logs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS engine_runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        run_type TEXT,
        input_size INTEGER,
        items_produced INTEGER,
        items_rejected INTEGER,
        duplicates_removed INTEGER,
        runtime_sec REAL,
        direct_cost TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print(f"Database initialized at {DB_PATH}")
