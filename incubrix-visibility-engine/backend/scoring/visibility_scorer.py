from collections import Counter

def calculate_question_score(q: dict) -> float:
    """
    Computes a 0-100 Visibility Score for a single question based on:
    - Google Organic Rank (Weight: 20%)
    - Google Answer Box / AI Overview Citation (Weight: 30%)
    - 4 AI Assistants Mentions (Weight: 50%, 12.5% each)
    """
    score = 0.0
    
    # 1. Google Organic Rank (20 pts)
    pos = int(q.get("google_position", 0))
    if 1 <= pos <= 3:
        score += 20.0
    elif 4 <= pos <= 10:
        score += 12.0
    elif 11 <= pos <= 20:
        score += 5.0
        
    # 2. Google Answer Box / AIO (30 pts)
    # If IncuBrix is quoted in answer box
    box = q.get("answer_box_or_ai_overview", "")
    quoted = q.get("quoted_source_url", "")
    if "incubrix.com" in quoted.lower():
        score += 30.0
    elif box in ["AI Overview", "Featured Snippet"]:
        # Opportunity score: search engine has high AEO intent
        score += 0.0
        
    # 3. AI Assistants (50 pts total - 12.5 pts each)
    for model_key in ["chatgpt", "gemini", "perplexity", "claude_or_copilot"]:
        if q.get(model_key, "").lower() == "yes":
            score += 12.5
            
    return round(score, 1)

def compute_aggregate_metrics(questions_list):
    """
    Computes system-level visibility KPIs and competitor share-of-voice.
    """
    total = len(questions_list)
    if total == 0:
        return {}
        
    scores = [calculate_question_score(q) for q in questions_list]
    avg_score = round(sum(scores) / total, 1)
    
    chatgpt_count = sum(1 for q in questions_list if q.get("chatgpt", "").lower() == "yes")
    gemini_count = sum(1 for q in questions_list if q.get("gemini", "").lower() == "yes")
    perp_count = sum(1 for q in questions_list if q.get("perplexity", "").lower() == "yes")
    claude_count = sum(1 for q in questions_list if q.get("claude_or_copilot", "").lower() == "yes")
    
    total_ai_checks = total * 4
    total_ai_mentions = chatgpt_count + gemini_count + perp_count + claude_count
    overall_ai_mention_rate = round((total_ai_mentions / total_ai_checks) * 100, 1)
    
    # Competitor mindshare
    competitor_counter = Counter()
    for q in questions_list:
        comps = q.get("competitors_named", "")
        if comps:
            for c in [x.strip() for x in comps.split(",")]:
                if c:
                    competitor_counter[c] += 1
                    
    competitor_breakdown = [
        {"name": k, "count": v, "share": round((v / total) * 100, 1)}
        for k, v in competitor_counter.most_common(8)
    ]
    
    # Markets breakdown
    markets = Counter(q.get("market") for q in questions_list)
    
    # Intent breakdown
    intents = Counter(q.get("intent") for q in questions_list)
    
    return {
        "total_questions": total,
        "average_visibility_score": avg_score,
        "overall_ai_mention_rate": overall_ai_mention_rate,
        "ai_mentions_by_model": {
            "ChatGPT": chatgpt_count,
            "Gemini": gemini_count,
            "Perplexity": perp_count,
            "Claude / Copilot": claude_count
        },
        "competitor_share_of_voice": competitor_breakdown,
        "market_distribution": dict(markets),
        "intent_distribution": dict(intents)
    }
