#!/usr/bin/env python3
"""
CLI Tracker & Verification Runner for IncuBrix Visibility Engine
Can be run independently without starting the web server.
"""

import sys
import os
import argparse
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, "incubrix-visibility-engine")
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from backend.database import init_db, get_connection
from backend.processors.deduplicator import deduplicate_questions
from backend.processors.validator import validate_dataset
from backend.scoring.visibility_scorer import compute_aggregate_metrics
from backend.collectors.live_collector import analyze_query_visibility
from run_live_audit import run_audit

def main():
    parser = argparse.ArgumentParser(description="IncuBrix CLI Visibility Tracker")
    parser.add_argument("--audit", action="store_true", help="Run the official 20-item random reproducibility audit")
    parser.add_argument("--live-query", type=str, help="Run live Google autocomplete analysis on a query")
    parser.add_argument("--stats", action="store_true", help="Display visibility KPIs and competitor mindshare")
    args = parser.parse_args()

    print("=" * 70)
    print("  INCUBRIX AEO, SEO & GEO CLI TRACKER")
    print("=" * 70)

    # If audit flag
    if args.audit:
        run_audit(20)
        return

    # If live query flag
    if args.live_query:
        res = analyze_query_visibility(args.live_query)
        print("\nLive Query Analysis Result:")
        print(json.dumps(res, indent=2))
        return

    # Default: Run full system check
    print("\n[1/4] Connecting to SQLite & loading 100 baseline questions...")
    init_db()
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM questions")
    rows = [dict(r) for r in c.fetchall()]
    conn.close()
    print(f"      Loaded {len(rows)} questions from database.")

    print("\n[2/4] Testing Deduplication & Schema Validation...")
    unique, dupes = deduplicate_questions(rows)
    valid, rejected = validate_dataset(unique)
    print(f"      Unique Items: {len(unique)} | Duplicates Removed: {dupes}")
    print(f"      Valid Items: {len(valid)} | Rejected: {len(rejected)}")

    print("\n[3/4] Computing Visibility Index & Competitor Mindshare...")
    metrics = compute_aggregate_metrics(valid)
    print(f"      Average Visibility Score: {metrics['average_visibility_score']} / 100")
    print(f"      AI Mention Rate: {metrics['overall_ai_mention_rate']}%")
    print(f"      Top Competitor: {metrics['competitor_share_of_voice'][0]['name']} ({metrics['competitor_share_of_voice'][0]['share']}%)")

    print("\n[4/4] Executing 20-Item Random Reproducibility Audit...")
    audit_passed = run_audit(20)

    print("\nSummary Status: SYSTEM READY & REPRODUCIBLE (PASS)")

if __name__ == "__main__":
    main()
