# IncuBrix Visibility Engine — Live System Verification & Test Report

**Execution Timestamp:** 2026-11-23 11:24:45 IST  
**Environment:** Windows (PowerShell / Python 3.13)  
**Host Target:** `http://127.0.0.1:8000`  
**Candidate Name:** Prem Kumar (`CAND-2027-GROWTH-03`)  
**Assessment Option:** Option 3 — AEO, SEO & GEO Visibility Engine  

---

## Executive Summary

| Test Domain | Target Requirement | Status | Score / Metric |
| :--- | :--- | :---: | :--- |
| **1. Unit Test Suite** | Backend deduplication, scoring, validation | **PASS** | 4 / 4 passed (100%) |
| **2. Random Audit Check** | 20 randomly sampled items traced to raw evidence | **PASS** | 20 / 20 verified (100.0%) |
| **3. Failure & Recovery** | Malformed / corrupted record isolation | **PASS** | 100% defensive stability |
| **4. Engine Live Health** | FastAPI REST endpoints & SQLite connectivity | **PASS** | `200 OK` (Healthy) |
| **5. Live Search Engine Query** | Real Google Autocomplete query in US, UK & IN | **PASS** | 0.24s – 0.48s live latency |
| **6. Automated Refresh Engine** | Pipeline deduplication, re-scoring & audit trail | **PASS** | 100 items processed in 1.11s |
| **7. Official Dataset Export** | `visibility.csv` (100 rows, 20 columns) | **PASS** | 47,217 bytes generated |

---

## Detailed Test Logs & Verification

### 1. Automated Unit Tests (`pytest`)
* **Test Module:** `incubrix-visibility-engine/backend/tests/test_engine.py`
* **Command:** `pytest incubrix-visibility-engine/backend/tests`
* **Results:**
  * `test_normalize_text` &rarr; **PASSED**
  * `test_deduplicate_questions` &rarr; **PASSED**
  * `test_validate_dataset_clean` &rarr; **PASSED**
  * `test_validate_dataset_missing_fields` &rarr; **PASSED**
* **Duration:** 0.06 seconds

---

### 2. Live Random Reproducibility Audit (20 Items)
Evaluates whether a randomly selected sample of 20 questions can be traced to genuine, non-synthetic raw evidence JSON files.

* **Audit Command:** `python run_live_audit.py`
* **Audit Sample:**
  * `Q082` (India) &bull; Domain: `buffer.com` &bull; `evidence/raw_answers/Q082.json` &bull; **PASS**
  * `Q015` (United States) &bull; Domain: `vidiq.com` &bull; `evidence/raw_answers/Q015.json` &bull; **PASS**
  * `Q004` (United States) &bull; Domain: `hubspot.com` &bull; `evidence/raw_answers/Q004.json` &bull; **PASS**
  * `Q095` (India) &bull; Domain: `vidiq.com` &bull; `evidence/raw_answers/Q095.json` &bull; **PASS**
  * `Q036` (United States) &bull; Domain: `hubspot.com` &bull; `evidence/raw_answers/Q036.json` &bull; **PASS**
  * `Q032` (United States) &bull; Domain: `pcmag.com` &bull; `evidence/raw_answers/Q032.json` &bull; **PASS**
  * `Q029` (United States) &bull; Domain: `influencermarketinghub.com` &bull; `evidence/raw_answers/Q029.json` &bull; **PASS**
  * `Q018` (United States) &bull; Domain: `buffer.com` &bull; `evidence/raw_answers/Q018.json` &bull; **PASS**
  * `Q014` (United States) &bull; Domain: `reddit.com` &bull; `evidence/raw_answers/Q014.json` &bull; **PASS**
  * `Q087` (India) &bull; Domain: `vidiq.com` &bull; `evidence/raw_answers/Q087.json` &bull; **PASS**
  * `Q070` (United Kingdom) &bull; Domain: `reddit.com` &bull; `evidence/raw_answers/Q070.json` &bull; **PASS**
  * `Q012` (United States) &bull; Domain: `hubspot.com` &bull; `evidence/raw_answers/Q012.json` &bull; **PASS**
  * `Q076` (United Kingdom) &bull; Domain: `hubspot.com` &bull; `evidence/raw_answers/Q076.json` &bull; **PASS**
  * `Q055` (United States) &bull; Domain: `vidiq.com` &bull; `evidence/raw_answers/Q055.json` &bull; **PASS**
  * `Q005` (United States) &bull; Domain: `influencermarketinghub.com` &bull; `evidence/raw_answers/Q005.json` &bull; **PASS**
  * `Q028` (United States) &bull; Domain: `hubspot.com` &bull; `evidence/raw_answers/Q028.json` &bull; **PASS**
  * `Q030` (United States) &bull; Domain: `reddit.com` &bull; `evidence/raw_answers/Q030.json` &bull; **PASS**
  * `Q065` (United Kingdom) &bull; Domain: `zapier.com` &bull; `evidence/raw_answers/Q065.json` &bull; **PASS**
  * `Q078` (United Kingdom) &bull; Domain: `reddit.com` &bull; `evidence/raw_answers/Q078.json` &bull; **PASS**
  * `Q072` (United Kingdom) &bull; Domain: `pcmag.com` &bull; `evidence/raw_answers/Q072.json` &bull; **PASS**
* **Score:** **100.0% Pass Rate** (Exceeds required &ge; 85.0% Strong Hire threshold).

---

### 3. Defensive Error Isolation & Fault Tolerance
* **Command:** `python test_recovery_demo.py`
* **Test Case:** Ingestion of a batch with 1 deliberately corrupted record (missing mandatory schema fields).
* **Outcome:**
  * System trapped corrupted record `CORRUPTED_ROW_02`.
  * Wrote structured error to `backend/logs/recovery_demo.log`.
  * Continued pipeline execution without crashing; processed remaining 2 valid records cleanly.
  * **Result:** 100% defensive recovery pass.

---

### 4. Real-Time Search Engine Collector Tests
Tested live query ingestion across 3 locales via Google's public endpoint:

| Query Tested | Market Locale | Intent Detected | Suggestions Returned | Live Latency |
| :--- | :---: | :---: | :---: | :---: |
| *"best ai tool to repurpose long video into shorts"* | United States | Commercial Investigation | 5 live terms | **0.480s** |
| *"how to auto generate captions for tiktok"* | United Kingdom | Comparison / Evaluation | 8 live terms | **0.287s** |
| *"youtube video to instagram reels converter ai"* | India | General Informational | Real autocomplete output | **0.247s** |

---

### 5. Refresh Pipeline & SQLite Logging
* **Endpoint:** `POST /api/refresh`
* **Input Dataset:** 100 questions
* **Items Produced:** 100 valid items
* **Duplicates Rejected:** 0 duplicates
* **Execution Latency:** 1.11 seconds
* **Direct Cost:** $0.00
* **Audit Trail Entry:** Added new execution row to SQLite `engine_runs` table.

---

### 6. Main CSV Export Verification
* **Endpoint:** `GET /api/export/csv`
* **Status:** `200 OK`
* **Payload Size:** 47,217 bytes
* **Headers:** `Content-Disposition: attachment; filename=visibility.csv`
* **Schema Verification:** Matches the exact 20 columns required by the submission workbook.
