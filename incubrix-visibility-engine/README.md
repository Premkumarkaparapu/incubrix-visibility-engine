# IncuBrix Search & AI Visibility Engine
**Growth Engineer Assessment — Option 3 (AEO, SEO & GEO Engine)**  
**Candidate:** Prem Kumar  

This repository contains my submission for the IncuBrix Growth Engineer 7-day assessment. It includes:
1. **Visibility Baseline:** 100 creator questions measured across Google and 4 AI assistants (ChatGPT, Gemini, Perplexity, Claude) across 3 markets (US, UK, India).
2. **Technical Fixes:** 20 prioritized, validated fixes for `incubrix.com` (including `/llms.txt`, JSON-LD schemas, and `robots.txt`).
3. **10 AEO Pages:** Answer-first content pieces written to capture Featured Snippets and AI Overviews.
4. **Citation Plan:** 30 high-authority third-party pages currently quoted by AI assistants with outreach angles.
5. **Repeatable Engine:** A FastAPI + SQLite application with an interactive dashboard and CLI tracker.
6. **Launch Kit:** A 90-day step-by-step growth plan starting next Monday.

---

## ⚡ How to Run the Project (Single Command)

To run the complete application on a local machine:

```bash
# 1. Install dependencies (standard Python 3.10+)
pip install -r requirements.txt

# 2. Start the application
python run.py
```

Once started, open your browser and navigate to:  
👉 **http://localhost:8000**

---

## 🔍 CLI Commands & Reproducibility Tests

If you prefer testing directly from the terminal without opening a browser:

```bash
# 1. Run the 20-item random reproducibility audit (checks raw evidence & quoted sources)
python run_live_audit.py

# 2. Run the failure and recovery demonstration
python test_recovery_demo.py

# 3. Test a new query live via Google Autocomplete collector
python run_tracker.py --live-query "how to make shorts with AI"

# 4. Run the unit test suite
pytest incubrix-visibility-engine/backend/tests
```

---

## 📁 Repository Structure

```text
├── IncuBrix_2027_Growth_Engineer_Option_3_AEO_SEO_GEO_Submission_Workbook.xlsx  # Official completed workbook
├── run.py                                                                       # Single-command launcher
├── run_tracker.py                                                               # Standalone CLI tracker
├── run_live_audit.py                                                            # 20-item random audit test
├── test_recovery_demo.py                                                        # Simple failure recovery test
├── LIVE_REVIEW_DEFENSE_GUIDE.md                                                 # 45-minute live interview guide
├── README.md                                                                    # This guide
│
├── visibility/                                                                  # Main Output Folder
│   ├── visibility.csv                                                           # 100 questions matching workbook schema
│   ├── fixes/                                                                   # 20 validated code patches
│   ├── pages/                                                                   # 10 publish-ready AEO markdown pages
│   └── citations/                                                               # 30 citation target profiles
│
├── evidence/                                                                    # Grounded Evidence
│   ├── raw_answers/                                                             # 100 raw JSON files (Q001 to Q100)
│   └── screenshots/                                                             # Diagnostic audit screenshots
│
├── launch_kit/
│   └── 90_DAY_GROWTH_PLAN.md                                                    # Actionable 90-day plan
│
├── incubrix-visibility-engine/                                                  # Engine Source Code
│   ├── backend/                                                                 # FastAPI + SQLite + Collectors
│   └── static/                                                                  # Dashboard UI (React + Tailwind)
│
└── videos/
    ├── video_1_product_walkthrough.md                                           # Video 1 script (< 5 mins)
    └── video_2_technical_demo.md                                                # Video 2 script (< 8 mins)
```

---

## 📝 Methodology & Disclosures

* **Data Collection:** Questions were curated from Google "People Also Ask", Reddit communities (`r/podcasting`, `r/Creator`, `r/NewTubers`), and YouTube search suggestions across the US, UK, and India.
* **AI Tool Disclosure:** Python 3.13, FastAPI, SQLite, React, BeautifulSoup4, and OpenPyXL were used to build the engine. ChatGPT was utilized for initial question clustering and drafting outlines.
* **Direct Cost:** **$0.00**. No paid scraping tools or private databases were used. All data was verified through authorized public endpoints and browser verification.
