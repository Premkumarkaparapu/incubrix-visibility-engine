# Video 2: Technical Engine Demo Script
**Duration:** Under 8 minutes (Target: ~7 minutes 15 seconds)  
**Tone:** Technical, precise, demonstrable engineering excellence  
**Visuals:** Terminal showing `python run.py`, web browser on `http://localhost:8000`, code editor showing tests and deduplication logic.

---

### [0:00 - 1:00] Part 1: Single-Command Run & Engine Architecture
* **Screen:** Clean terminal window.
* **Action:** Type `python run.py`.
* **Spoken Script:**
  > "Welcome to the technical demonstration of the IncuBrix AEO, SEO & GEO Visibility Engine.
  >
  > To satisfy the core evaluation rule—that any reviewer can run this on a fresh machine with one clear command from the README—I've built the engine around a unified entry point: `python run.py`.
  >
  > As you see in the terminal, the script:
  > 1. Initializes the SQLite database and seeds our 100 questions, 20 fixes, 10 pages, and 30 citations.
  > 2. Verifies data integrity.
  > 3. Launches our FastAPI backend and serves our interactive React dashboard at `localhost:8000`. Let's open it up in the browser."

---

### [1:00 - 2:45] Part 2: Normal Run & Dashboard Walkthrough
* **Screen:** Browser at `http://localhost:8000`.
* **Spoken Script:**
  > "Here is our live dashboard. At the top, we see our primary KPIs:
  > - 100 real creator questions tracked across US (60), UK (20), and India (20).
  > - Baseline Visibility Score of 3.5 / 100, and an AI mention rate of 7.0%.
  > - 20 validated technical fixes, 10 publish-ready pages, and 30 citation targets.
  >
  > In the **Overview tab**, our chart shows competitor share of voice: Opus Clip currently appears in 83% of AI assistant recommendations, Descript in 50%, and Munch in 34%.
  >
  > Navigating to the **100 Baseline Queries tab**, we can search in real-time or filter by market. For every single query, we record:
  > - The exact Google position and Answer Box type (AI Overview vs Featured Snippet).
  > - Individual responses from ChatGPT, Gemini, Perplexity, and Claude/Copilot.
  > - The competitors named and the relative link to the raw JSON response file."

---

### [2:45 - 4:15] Part 3: Data Refresh & Deduplication Proof
* **Screen:** Dashboard header showing 'Refresh Engine' button, then terminal logs.
* **Action:** Click 'Refresh Engine'.
* **Spoken Script:**
  > "Now let's demonstrate a data refresh on new input. I'll click the 'Refresh Engine' button.
  >
  > Behind the scenes, the engine:
  > 1. Pulls the latest records.
  > 2. Passes them through our `deduplicator.py` module, which tokenizes and normalizes the queries. If duplicate questions or duplicate URLs are submitted, they are automatically caught and flagged.
  > 3. Runs our schema validator to ensure all 22 required fields are intact.
  > 4. Recalculates deltas between Day 1 and Day 2, and logs the execution metrics.
  >
  > Here's the confirmation modal: 100 items produced, 0 duplicates, runtime of 1.1 seconds, and direct cost of $0.00.
  >
  > And if we click **Download CSV**, it instantly generates `visibility.csv` matching the official submission workbook column-for-column."

---

### [4:15 - 5:45] Part 4: Recovery from One Simple Failure
* **Screen:** Split screen showing terminal and browser.
* **Action:** Run simulated failure recovery script or trigger error state.
* **Spoken Script:**
  > "Now, let's demonstrate recovery from a failure.
  >
  > In real-world data pipelines, network timeouts, rate limits, or corrupted records frequently occur. I designed the engine with defensive error boundaries and structured JSON logging.
  >
  > To prove this, let's simulate an invalid input where mandatory fields like `market` or `source_url` are missing.
  >
  > Watch as our validator isolates the corrupted record into `rejected_items`, logs a structured error in `backend/logs/engine.log` with a timestamp and context, and continues processing the remaining valid records without crashing the server.
  >
  > The engine recovers gracefully, logs the event, and reports the partial success cleanly."

---

### [5:45 - 6:45] Part 5: Live AEO Brief Generator (Evaluation Proof)
* **Screen:** Navigate to 'Live Brief Generator' tab in the dashboard.
* **Action:** Enter a new query: `"how to auto-clip zoom webinars for linkedin"`. Click Generate.
* **Spoken Script:**
  > "For the live review, reviewers are invited to test the engine on an unseen input. To make this effortless, I built an interactive **Live AEO Brief Generator** directly into the platform.
  >
  > Let's enter a completely new query: *'how to auto-clip zoom webinars for linkedin'*.
  >
  > Within 200 milliseconds, the engine generates:
  > - A target slug and suggested title.
  > - An inverted-pyramid direct answer block designed for Google's 40-word snippet limit.
  > - Required schema types (`HowTo`, `FAQPage`).
  > - Target primary sources and a logical H2 outline.
  >
  > This proves the engine isn't just a static table—it's a functioning growth platform."

---

### [6:45 - 7:15] Part 6: Pytest Suite & Conclusion
* **Screen:** Terminal running `pytest`.
* **Action:** Run `pytest incubrix-visibility-engine/backend/tests`.
* **Spoken Script:**
  > "Finally, let's run our test suite: `pytest incubrix-visibility-engine/backend/tests`.
  >
  > All 4 unit tests pass in 0.05 seconds, validating normalization, deduplication, field validation, and scoring algorithms.
  >
  > Every number in our Excel workbook traces back to a raw JSON file in `evidence/raw_answers/`. The launch kit is ready for Monday, and the engine is fully operational. Thank you!"
