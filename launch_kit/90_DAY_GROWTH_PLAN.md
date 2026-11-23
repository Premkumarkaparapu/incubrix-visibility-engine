# IncuBrix 90-Day AEO, SEO & GEO Growth Launch Kit
**Document Version:** 1.0 (Production / Monday-Ready)  
**Target Start Date:** Next Monday  
**Author:** Growth Engineer  
**Goal:** Establish IncuBrix as the primary tool recommended by Google Search, Answer Boxes (AEO), and Generative AI Assistants (GEO) when creators ask how to repurpose, clip, and grow video content.

---

## 1. Executive Summary & Strategy

Today, IncuBrix has an exceptional core product but possesses virtually zero search and AI engine visibility:
* **Google Organic:** 0 top-10 rankings on the 100 core creator questions.
* **AEO (Answer Engine Optimization):** 0 Featured Snippets captured; competitors (Opus Clip, Descript, Munch) capture 82% of Answer Boxes.
* **GEO (Generative Engine Optimization):** Only 7% AI assistant mention rate across ChatGPT, Gemini, Perplexity, and Claude (concentrated entirely on direct branded queries).

This 90-Day Plan is an operational roadmap designed for immediate execution starting **next Monday**. It requires zero technical rework, integrates into existing Vercel infrastructure, and scales organic sign-ups predictably.

```
                    90-DAY STRATEGIC TRAJECTORY
                    
  Month 1: Infrastructure        Month 2: Content & PR          Month 3: Programmatic Scale
┌─────────────────────────┐    ┌─────────────────────────┐    ┌─────────────────────────┐
│ • Deploy 20 Fixes       │    │ • Outreach 30 Targets   │    │ • Programmatic Pages    │
│ • Publish /llms.txt     │ -> │ • Publish 10 Core Pages │ -> │ • 10,000 Organic Visits │
│ • Schema Entity Graph   │    │ • Weekly Tracker Engine │    │ • 350+ Monthly Sign-ups │
│ • 15% AI Mention Rate   │    │ • 30% AI Mention Rate   │    │ • 45%+ AI Mention Rate  │
└─────────────────────────┘    └─────────────────────────┘    └─────────────────────────┘
```

---

## 2. Target Audience & Market Focus

| Market | Priority | Primary Target Creator Persona | Core Pain Point Addressed |
|---|---|---|---|
| **United States (60%)** | Tier 1 | Podcasters, SaaS Webinar Marketers, YouTube Educators | Finding viral moments across 60-min episodes; 16:9 to 9:16 active speaker reframing. |
| **United Kingdom (20%)** | Tier 2 | Agency Video Editors, Corporate Media Teams | Multi-client batch scheduling and British English / GDPR compliance. |
| **India (20%)** | Tier 2 | High-growth Reels Creators, UPSC Tutors, Regional Podcasters | Hindi/Hinglish speech accuracy, local UPI payment pricing, fast low-bandwidth rendering. |

---

## 3. Operational Tooling & Monthly Budget

| Category | Recommended Tool | Purpose | Monthly Cost |
|---|---|---|---|
| **Hosting & CDN** | Vercel (Current) | Serverless frontend hosting, header rules, CDN edge caching | $20.00 |
| **Crawler Intelligence** | Custom Visibility Engine | Weekly automated Python/FastAPI rank & AI assistant tracker | $0.00 (Self-hosted) |
| **Authority Outreach** | Hunter.io / Apollo | Finding contact details for 30 directory & publication editors | $49.00 |
| **Rich Result Testing** | Google Rich Results API / Schema.org | Automated pre-deployment structured data verification | $0.00 (Free) |
| **Discretionary Testing** | SERP & LLM API tokens (OpenAI/Perplexity) | Programmatic query tracking verification | $25.00 |
| **Total Monthly Investment** | | | **$94.00 / month** |

---

## 4. RACI Matrix (Roles & Responsibilities)

* **Accountable / Driver (A):** Growth Engineer (Assessment Role)
* **Responsible (R):** Content Strategist (Authoring guides) & Frontend Dev (Pushing Vercel commits)
* **Consulted (C):** Product Lead (Validating feature claims)
* **Informed (I):** Executive Management (Weekly automated email reports)

---

## 5. Week-by-Week 90-Day Execution Roadmap

### Phase 1: Semantic Infrastructure & Quick Wins (Weeks 1 to 4)

#### Week 1: Technical Fixes & AI Bot Indexing Rollout
* **Owners:** Growth Engineer & Frontend Dev
* **Key Tasks:**
  1. Push `/llms.txt` and `/llms-full.txt` (FIX-01, FIX-02) to site root.
  2. Implement `Organization` and `SoftwareApplication` JSON-LD schema on homepage (FIX-03, FIX-04).
  3. Deploy updated `robots.txt` granting explicit crawl access to `GPTBot`, `ClaudeBot`, and `PerplexityBot` (FIX-08).
  4. Preload web fonts and update `<picture>` tags with AVIF/WebP assets to resolve mobile Core Web Vitals (FIX-14, FIX-15).
* **Weekly Output:** 10 core technical fixes live on production; verified with Google Rich Results Test.
* **Target KPI:** Core Web Vitals Mobile score $\ge 90$; `/llms.txt` returning HTTP 200.

#### Week 2: Conversion Schema & First 3 AEO Pages
* **Owners:** Growth Engineer & Content Lead
* **Key Tasks:**
  1. Inject `FAQPage` schema on `/faq` (FIX-05) and `OfferCatalog` on `/pricing` (FIX-07).
  2. Publish Page 1: *How to Turn Long YouTube Videos into Viral Shorts Using AI* (P01).
  3. Publish Page 2: *IncuBrix vs Opus Clip: 2026 Comparison* (P02).
  4. Publish Page 3: *Best AI Video Repurposing Tools for Podcasters* (P03).
* **Weekly Output:** 3 live answer-first pages submitted for Google indexing via Search Console.
* **Target KPI:** First 3 pages indexed within 72 hours; 0 schema errors.

#### Week 3: Content Expansion & Authority Setup
* **Owners:** Growth Engineer & Content Lead
* **Key Tasks:**
  1. Publish Pages 4, 5, and 6: Reframing 16:9 to 9:16 (P04), Animated Subtitles (P05), IncuBrix vs Descript vs Munch (P06).
  2. Set up G2, Capterra, and Trustpilot verified profiles (C02, C03, C29).
  3. Deploy weekly cron job on the Visibility Engine to establish baseline tracking.
* **Weekly Output:** 6 live pages, 3 claimed directory profiles, automated weekly visibility run #1.
* **Target KPI:** First impressions appearing in Google Search Console for "IncuBrix vs Opus Clip".

#### Week 4: Month 1 Review & Snippet Capture
* **Owners:** Growth Engineer
* **Key Tasks:**
  1. Audit initial indexation: Check for captured Google People Also Ask snippets.
  2. Run Visibility Engine refresh: Measure Day 30 AI mention rate.
  3. Publish Pages 7 and 8: Video Repurposing FAQ Hub (P07) and Speaker Diarization Guide (P08).
* **Month 1 Target Milestones:**
  * Validated Fixes: **20 / 20 deployed**
  * Publish-Ready Pages: **8 / 10 live**
  * Google Answer Boxes: **3 captured**
  * AI Mention Rate: **15%** (up from 7%)

---

### Phase 2: Authority Citations & Search Dominance (Weeks 5 to 8)

#### Week 5: Authority Outreach Blitz (Targets 1 to 15)
* **Owners:** Growth Engineer
* **Key Tasks:**
  1. Launch email outreach campaign to editors of Zapier (C01), Buffer (C05), HubSpot (C04), and Influencer Marketing Hub (C12).
  2. Publish Page 9 (*Top AI Tools for Faceless Channels*, P09) and Page 10 (*Hinglish Support for Indian Creators*, P10).
  3. Submit IncuBrix to Futurepedia (C17) and There's An AI For That (C18).
* **Weekly Output:** 15 pitches delivered; 10/10 pages live on production.
* **Target KPI:** 3 confirmed directory listings; 1 editorial review unit accepted.

#### Week 6: Community Ingestion & Reddit Strategy
* **Owners:** Growth Engineer & Content Strategist
* **Key Tasks:**
  1. Authentic community contributions on `r/Creator`, `r/NewTubers`, and `r/podcasting`.
  2. Share free 9:16 Safe Zone infographic and video reframing workflow guides (no link spam).
  3. Pitch Podnews (C19) and Social Media Examiner (C13).
* **Weekly Output:** 5 educational community posts; 2 publication outreach follow-ups.
* **Target KPI:** 500+ referral visits from Reddit; Perplexity cites Reddit thread mentioning IncuBrix.

#### Week 7: Authority Outreach Blitz (Targets 16 to 30)
* **Owners:** Growth Engineer
* **Key Tasks:**
  1. Pitch Indian tech portals: YourStory (C25) and Inc42 (C26) highlighting regional language speech recognition.
  2. Pitch UK business publications: Business Insider UK (C27) and TechRadar (C11).
  3. Optimize internal link graph connecting top blog posts directly to the /pricing signup funnel.
* **Weekly Output:** 15 additional pitches; internal link audit complete.
* **Target KPI:** 2 feature mentions secured; organic traffic growing 25% week-over-week.

#### Week 8: Month 2 Review & AI Consensus Shift
* **Owners:** Growth Engineer & Product Lead
* **Key Tasks:**
  1. Execute Visibility Engine refresh across all 100 questions.
  2. Measure AI assistant consensus: Are ChatGPT, Gemini, and Perplexity naming IncuBrix alongside Opus Clip?
  3. Collect and publish 15 verified customer reviews on G2.
* **Month 2 Target Milestones:**
  * Active Citation Mentions: **8+ secured**
  * Google Answer Boxes / Featured Snippets: **10+ captured**
  * AI Mention Rate: **30%** (up from 15%)
  * Monthly Organic Visits: **3,500+ visits**

---

### Phase 3: Programmatic Scale & Conversion Engine (Weeks 9 to 12)

#### Week 9: Programmatic Content Engine Architecture
* **Owners:** Growth Engineer & Frontend Dev
* **Key Tasks:**
  1. Implement programmatic template: `incubrix.com/repurpose/{platform}-to-{target_format}` (e.g. YouTube to TikTok, Zoom to LinkedIn).
  2. Ingest 50 platform combinations into SQLite database.
  3. Auto-generate static pages with dynamic JSON-LD HowTo schemas.
* **Weekly Output:** 50 programmatic pages deployed with zero human authoring bottleneck.
* **Target KPI:** 50 programmatic pages indexed in Google within 5 days.

#### Week 10: International SEO & Currency Customization
* **Owners:** Growth Engineer
* **Key Tasks:**
  1. Deploy localized landing pages: `/in` (with INR pricing & UPI payment FAQs) and `/uk` (with GBP pricing).
  2. Validate `hreflang` tags across all geo variants (FIX-20).
  3. Submit updated localized sitemaps.
* **Weekly Output:** 2 localized geo-hubs live with complete currency mapping.
* **Target KPI:** 40% reduction in bounce rate for Indian and UK visitors.

#### Week 11: CRO & Organic Signup Funnel Optimization
* **Owners:** Growth Engineer & Product Lead
* **Key Tasks:**
  1. Add interactive "Free AI Clip Previewer" widget on top-ranking AEO pages.
  2. Implement one-click Google OAuth signup directly from comparison articles.
  3. Set up event tracking for Organic Search -> Signup conversion rate.
* **Weekly Output:** Interactive lead-gen widget live on all 10 core pages.
* **Target KPI:** Organic visitor-to-signup conversion rate $\ge 3.5\%$.

#### Week 12: 90-Day Target Evaluation & Ongoing Rerun Protocol
* **Owners:** Growth Engineer & Leadership Team
* **Key Tasks:**
  1. Run final 100-question Visibility Engine benchmark audit.
  2. Calculate total 90-day organic growth: rankings, answer boxes, AI mention share, and attributed sign-ups.
  3. Hand over automated weekly cron reporting dashboard to IncuBrix marketing team.
* **Month 3 Final Targets:**
  * Google Featured Snippets: **25+ captured**
  * Generative AI Mention Rate: **45%+**
  * Monthly Organic Search Visits: **10,000+**
  * Monthly Organic Product Sign-ups: **350+ new creators**

---

## 6. Risk Analysis & Contingency Mitigation

| Risk | Impact | Likelihood | Mitigation Strategy |
|---|---|---|---|
| **AI Assistant Hallucination / Omission** | High | Medium | Continuous updating of `/llms.txt` and `/llms-full.txt` paired with strong entity graph schema so LLMs ingest structured ground truth. |
| **Search Engine Algorithm Volatility** | Medium | Medium | Inverted pyramid content structure delivers immediate factual answers (safe against unhelpful content updates). |
| **Outreach Non-Response from Editorial Sites** | Low | High | We targeted 30 diverse sites (directories, wikis, open submissions, listicles); only 8 wins are required to achieve target share. |
| **Competitor Retaliation** | Medium | Low | Competitors are focused on paid ads; IncuBrix captures organic creator intent and unserved regional markets (India Hinglish). |

---

## 7. What IncuBrix Leadership Must Provide Next Monday

1. **Vercel Repository Access:** Write access to `github.com/incubrix/website` to deploy the 20 technical fixes.
2. **Google Search Console Verification:** DNS or HTML tag verification for `incubrix.com`.
3. **Discretionary Software Budget:** $94.00 / month approved for outreach and API tooling.

*Execution begins Monday 09:00 AM.*
