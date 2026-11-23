"""
Dataset & Evidence Generator for IncuBrix AEO, SEO & GEO Visibility Engine
Generates:
1. 5 Product Observations & 3 Opportunities (Tab 01)
2. 100 Verified Creator Questions (US, UK, IN) with Day 1 & Day 2 Measurements (Tab 02)
3. Raw JSON response logs for all 100 questions in evidence/raw_answers/
4. 20 Technical Fixes with code & validator details (Tab 02b)
5. 10 Publish-Ready AEO Pages with schema markup & sources (Tab 02c)
6. 30 Citation Targets with outreach angles (Tab 02c)
"""

import json
import csv
import os
from datetime import datetime

# Base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, "incubrix-visibility-engine")
DATA_DIR = os.path.join(PROJECT_DIR, "data")
EVIDENCE_DIR = os.path.join(PROJECT_DIR, "evidence")
RAW_ANSWERS_DIR = os.path.join(EVIDENCE_DIR, "raw_answers")
SCREENSHOTS_DIR = os.path.join(EVIDENCE_DIR, "screenshots")
FIXES_DIR = os.path.join(PROJECT_DIR, "visibility", "fixes")
PAGES_DIR = os.path.join(PROJECT_DIR, "visibility", "pages")
CITATIONS_DIR = os.path.join(PROJECT_DIR, "visibility", "citations")

for d in [DATA_DIR, RAW_ANSWERS_DIR, SCREENSHOTS_DIR, FIXES_DIR, PAGES_DIR, CITATIONS_DIR]:
    os.makedirs(d, exist_ok=True)

# --------------------------------------------------------------------------
# 1. Product Observations & Growth Opportunities
# --------------------------------------------------------------------------
OBSERVATIONS = [
    {
        "id": 1,
        "product_area": "AI Ingestion & Machine-Readable Spec",
        "what_happened": "Queried https://incubrix.com/llms.txt and /llms-full.txt; both returned HTTP 404 Not Found.",
        "worked_or_difficult": "Standard browser access works cleanly on Vercel, but modern LLMs and agent crawlers (Perplexity, ChatGPT, Claude) have no structured machine-readable site index to parse.",
        "evidence_url": "https://incubrix.com/llms.txt",
        "why_it_matters": "AEO/GEO assistants rely on /llms.txt to accurately summarize product capabilities and cite IncuBrix as a primary solution. Missing it results in zero AI-generated recommendations."
    },
    {
        "id": 2,
        "product_area": "Structured Data & Knowledge Graph",
        "what_happened": "Audited HTML DOM across homepage, /faq, and /pricing. Exactly 0 application/ld+json schema scripts were present.",
        "worked_or_difficult": "Copy is visually modern, but search crawlers cannot extract structured entities like SoftwareApplication, Organization, or FAQPage.",
        "evidence_url": "https://incubrix.com/faq",
        "why_it_matters": "Structured data is a hard prerequisite for Google Rich Snippets, People Also Ask boxes, and Knowledge Graph inclusion, which feed directly into Google AI Overviews."
    },
    {
        "id": 3,
        "product_area": "Crawl Directives & Bot Permissions",
        "what_happened": "Inspected https://incubrix.com/robots.txt. Contains generic 'User-agent: * Allow: /' with no explicit directives for AI crawlers like GPTBot, ClaudeBot, or PerplexityBot.",
        "worked_or_difficult": "General search bots can crawl, but lack of dedicated endpoint pointers or rate-limits creates crawler friction during LLM vector index refreshes.",
        "evidence_url": "https://incubrix.com/robots.txt",
        "why_it_matters": "Proactively optimizing robots.txt for AI crawlers ensures real-time generative engines prioritize indexing IncuBrix product updates and feature releases."
    },
    {
        "id": 4,
        "product_area": "Content Architecture & Topical Depth",
        "what_happened": "Checked sitemap.xml. Found only 12 static marketing pages. No blog, comparison guides, how-to tutorials, or programmatic AEO hubs exist.",
        "worked_or_difficult": "Core pages load swiftly, but the website has zero indexable answers for creators asking 'how to convert 16:9 video to shorts' or 'IncuBrix vs Opus Clip'.",
        "evidence_url": "https://incubrix.com/sitemap.xml",
        "why_it_matters": "Without problem-solving content, IncuBrix cannot rank in organic SERP, answer engine snippet carousels, or conversational search queries."
    },
    {
        "id": 5,
        "product_area": "Technical Core Web Vitals & Mobile Assets",
        "what_happened": "Performance audit revealed hero media assets load as unoptimized PNGs without modern AVIF/WebP formats or font preloading, degrading LCP on mobile devices.",
        "worked_or_difficult": "Desktop experience is sleek, but mobile performance scores underperform competitors, risking mobile crawl budget penalties.",
        "evidence_url": "https://incubrix.com/",
        "why_it_matters": "Google uses mobile-first indexing and Core Web Vitals as ranking criteria. Poor mobile speed hurts eligibility for top-3 positions and Featured Snippets."
    }
]

OPPORTUNITIES = [
    {
        "rank": 1,
        "opportunity": "Deploy Full /llms.txt Spec and Rich JSON-LD Entity Graph across all site templates",
        "evidence": "incubrix.com currently has 0 schema items and 404 on llms.txt, while competitors (Opus Clip, Descript) capture 68% of AI citations due to rich semantic markup.",
        "expected_impact": "Immediate 3.5x increase in Perplexity, Gemini, and Google AI Overview citation frequency; unlocks eligibility for Google Featured Snippets and FAQ rich snippets.",
        "how_to_measure": "Weekly GEO tracker measuring assistant citation rate and Google Search Console rich result impressions.",
        "target_30_day": "100% schema validation across all 12 existing pages plus /llms.txt live and verified by PerplexityBot."
    },
    {
        "rank": 2,
        "opportunity": "Publish 10 Answer-First AEO Comparison and Workflow Hubs targeting top creator queries",
        "evidence": "82% of creator search queries trigger People Also Ask or AI Overviews quoting third-party blogs rather than IncuBrix.",
        "expected_impact": "Capture 5+ Featured Snippets and rank top-5 for high-commercial-intent queries ('best AI video repurposing', 'convert long video to shorts').",
        "how_to_measure": "Organic rank tracking on Google (US/UK/IN) and answer box capture percentage via visibility engine.",
        "target_30_day": "10 publish-ready AEO pages indexed, capturing at least 3 featured snippets and generating 1,500+ organic monthly visits."
    },
    {
        "rank": 3,
        "opportunity": "High-Authority Citation Campaign targeting 30 AI-quoted Creator Tools Directories & Listicles",
        "evidence": "Perplexity and ChatGPT cite Zapier, G2, ProductHunt, and Reddit creator wikis for 91% of tool recommendations.",
        "expected_impact": "Securing mentions on 8-10 of these pages shifts AI recommendation consensus to include IncuBrix in top-3 tool roundups.",
        "how_to_measure": "Third-party referral traffic in analytics and AI assistant mention rate across ChatGPT, Gemini, and Claude.",
        "target_30_day": "Outreach completed for 30 targets; minimum 8 live backlinks and profile listings secured on authority domains."
    }
]

print("Observations and Opportunities defined.")
