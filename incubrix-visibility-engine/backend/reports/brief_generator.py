def generate_aeo_content_brief(target_query: str, intent: str = "Informational", market: str = "United States") -> dict:
    """
    Generates a high-converting, answer-first AEO/GEO content brief
    for any target query to capture Google AI Overviews & Perplexity citations.
    """
    return {
        "target_query": target_query,
        "market": market,
        "intent": intent,
        "primary_keyword": target_query,
        "suggested_title": f"{target_query.title()}: Complete Creator Workflow & Benchmarks",
        "recommended_slug": target_query.lower().replace(" ", "-").replace("?", "").replace(":", ""),
        "direct_answer_formula": {
            "sentence_1": f"To execute {target_query}, creators use an automated AI video repurposing workflow that ingests long-form video, analyzes speech for viral engagement cues, and auto-reframes to 9:16 vertical.",
            "sentence_2": f"Compared to manual multi-track editing, this reduces production time by 85% while automatically generating animated subtitles and multi-platform social posts."
        },
        "target_schemas": ["FAQPage", "HowTo", "SoftwareApplication"],
        "required_h2_outline": [
            "Quick Answer & Benchmark Comparison Table",
            "Why Traditional Manual Editing Causes Production Bottlenecks",
            "Step-by-Step AI Repurposing Workflow (Ingest -> Highlight -> Reframe -> Schedule)",
            "Safe Zone Formatting for TikTok, Shorts, and Instagram Reels",
            "Frequently Asked Questions"
        ],
        "sources_to_cite": [
            "YouTube Creator Academy Best Practices",
            "Wistia Video Analytics Report 2026",
            "TikTok Creator Portal 9:16 Safe Zone Guidelines"
        ],
        "internal_links_to_include": [
            {"anchor": "AI Video Repurposing Studio", "url": "https://incubrix.com/"},
            {"anchor": "Creator Pricing Plans", "url": "https://incubrix.com/pricing"},
            {"anchor": "How It Works Guide", "url": "https://incubrix.com/how-it-works"}
        ]
    }
