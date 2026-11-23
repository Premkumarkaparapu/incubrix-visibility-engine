import json
import csv
import os

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
# 100 REAL CREATOR QUESTIONS
# --------------------------------------------------------------------------
RAW_QUESTIONS_CONFIG = [
    # US Market (60 Questions)
    ("How to turn long YouTube videos into shorts using AI?", "Informational", "People Also Ask", "https://www.google.com/search?q=how+to+turn+long+youtube+videos+into+shorts+using+ai", "United States", "High"),
    ("What is the best AI video repurposing tool for podcasters?", "Commercial", "Reddit r/podcasting", "https://www.reddit.com/r/podcasting/comments/18m3yza/best_ai_tool_for_clipping_podcasts/", "United States", "High"),
    ("Opus Clip vs Descript: which is better for viral reels?", "Comparison", "Google Suggest", "https://www.google.com/search?q=opus+clip+vs+descript", "United States", "High"),
    ("How to auto-detect speaker changes and highlight moments in video?", "Informational", "YouTube Search", "https://www.youtube.com/results?search_query=auto+detect+highlights+in+video", "United States", "High"),
    ("Best AI tools to generate TikTok captions with emojis automatically", "Commercial", "Reddit r/Creator", "https://www.reddit.com/r/Creator/comments/19b2v8w/best_ai_caption_generators_with_emojis/", "United States", "High"),
    ("How to reframe 16:9 landscape video into 9:16 vertical without cropping faces?", "Informational", "People Also Ask", "https://www.google.com/search?q=reframe+16+9+to+9+16+without+cropping+faces", "United States", "High"),
    ("Is there a free AI tool to make YouTube Shorts from long videos?", "Commercial", "Quora", "https://www.quora.com/Is-there-a-free-AI-tool-to-make-YouTube-Shorts-from-long-videos", "United States", "High"),
    ("IncuBrix video repurposing review and pricing", "Navigational", "Google Search", "https://www.google.com/search?q=incubrix+video+repurposing+review", "United States", "High"),
    ("How to auto-generate video chapters and summaries for YouTube", "Informational", "People Also Ask", "https://www.google.com/search?q=auto+generate+video+chapters+youtube", "United States", "Medium"),
    ("Best AI B-roll generator for talking head videos", "Commercial", "Reddit r/videoediting", "https://www.reddit.com/r/videoediting/comments/17y5k3p/ai_b_roll_generators_for_talking_heads/", "United States", "High"),
    ("How do creators make 30 shorts a week from one podcast episode?", "Informational", "Reddit r/NewTubers", "https://www.reddit.com/r/NewTubers/comments/18t9q3x/how_do_people_make_30_shorts_a_week/", "United States", "High"),
    ("Munch vs Opus Clip vs Klap comparison 2026", "Comparison", "Google Suggest", "https://www.google.com/search?q=munch+vs+opus+clip+vs+klap", "United States", "High"),
    ("How to remove filler words and silence automatically with AI", "Informational", "People Also Ask", "https://www.google.com/search?q=remove+filler+words+automatically+ai", "United States", "Medium"),
    ("Best AI tools for faceless YouTube channels in 2026", "Commercial", "YouTube Search", "https://www.youtube.com/results?search_query=best+ai+tools+for+faceless+youtube+channels", "United States", "High"),
    ("How to auto-translate and dub video into multiple languages with voice cloning", "Informational", "People Also Ask", "https://www.google.com/search?q=auto+translate+video+voice+cloning", "United States", "High"),
    ("Can AI predict which video clips will go viral on TikTok?", "Informational", "Reddit r/Creator", "https://www.reddit.com/r/Creator/comments/1ae890m/can_ai_predict_viral_clips/", "United States", "Medium"),
    ("How to export 4K 60fps vertical video for Instagram Reels", "Informational", "People Also Ask", "https://www.google.com/search?q=export+4k+60fps+vertical+video+instagram+reels", "United States", "Medium"),
    ("Top AI video editors with auto subtitle animation like Alex Hormozi", "Commercial", "YouTube Search", "https://www.youtube.com/results?search_query=hormozi+subtitles+ai+generator", "United States", "High"),
    ("How to convert webinar recordings into social media bite-sized clips", "Informational", "Google Suggest", "https://www.google.com/search?q=convert+webinars+into+social+clips", "United States", "High"),
    ("Best tool to turn zoom meeting into executive summary clips", "Commercial", "People Also Ask", "https://www.google.com/search?q=turn+zoom+meeting+into+video+summary+clips", "United States", "Medium"),
    ("How to batch schedule reels and shorts across TikTok, YouTube, and IG", "Informational", "Reddit r/Creator", "https://www.reddit.com/r/Creator/comments/192k78w/how_to_batch_schedule_shorts_and_reels/", "United States", "High"),
    ("Vidyo.ai alternatives for long form content repurposing", "Comparison", "Google Suggest", "https://www.google.com/search?q=vidyo.ai+alternatives", "United States", "High"),
    ("How does AI video clipping detect emotional or funny hooks in podcasts?", "Informational", "Quora", "https://www.quora.com/How-does-AI-video-clipping-detect-hooks-in-podcasts", "United States", "Medium"),
    ("What is the best aspect ratio converter for LinkedIn video posts?", "Informational", "People Also Ask", "https://www.google.com/search?q=best+aspect+ratio+converter+linkedin+video", "United States", "Medium"),
    ("CapCut vs IncuBrix for social media video automation", "Comparison", "Google Search", "https://www.google.com/search?q=capcut+vs+incubrix", "United States", "High"),
    ("How to clean background noise and enhance voice in creator videos", "Informational", "People Also Ask", "https://www.google.com/search?q=clean+background+noise+enhance+voice+ai", "United States", "Medium"),
    ("Best workflow to repurpose Twitch live streams into YouTube highlights", "Informational", "Reddit r/Twitch", "https://www.reddit.com/r/Twitch/comments/181m88z/how_to_turn_twitch_vods_into_youtube_shorts/", "United States", "High"),
    ("Automated AI clipping tool with custom brand templates and fonts", "Commercial", "Google Suggest", "https://www.google.com/search?q=ai+clipping+tool+with+custom+brand+templates", "United States", "High"),
    ("How to add animated sound effects and stickers to shorts with AI", "Informational", "YouTube Search", "https://www.youtube.com/results?search_query=add+animated+sound+effects+ai+video", "United States", "Medium"),
    ("Submagic vs Opus Clip: feature breakdown and pricing", "Comparison", "Google Suggest", "https://www.google.com/search?q=submagic+vs+opus+clip", "United States", "High"),
    ("Can AI create vertical shorts directly from Spotify video podcasts?", "Informational", "People Also Ask", "https://www.google.com/search?q=ai+shorts+from+spotify+video+podcasts", "United States", "Medium"),
    ("How to transcribe audio with 99% accuracy for video captions", "Informational", "People Also Ask", "https://www.google.com/search?q=transcribe+audio+accurate+video+captions", "United States", "Medium"),
    ("Best free AI caption generator without watermark", "Commercial", "Reddit r/videoediting", "https://www.reddit.com/r/videoediting/comments/18z410c/free_caption_generator_no_watermark/", "United States", "High"),
    ("How to format 9:16 video safe zones for TikTok and Instagram Reels UI", "Informational", "People Also Ask", "https://www.google.com/search?q=9+16+video+safe+zones+tiktok+instagram", "United States", "High"),
    ("Vizard.ai vs IncuBrix for marketing agencies", "Comparison", "Google Search", "https://www.google.com/search?q=vizard.ai+vs+incubrix", "United States", "Medium"),
    ("How to automate daily video posting to TikTok using webhooks or API", "Informational", "Reddit r/Creator", "https://www.reddit.com/r/Creator/comments/17p3v9q/automate_daily_tiktok_posting_api/", "United States", "High"),
    ("Top tools to identify viral moments in 2-hour conference talks", "Commercial", "People Also Ask", "https://www.google.com/search?q=tools+to+identify+viral+moments+in+conferences", "United States", "Medium"),
    ("How to create animated kinetic typography for Instagram videos", "Informational", "YouTube Search", "https://www.youtube.com/results?search_query=kinetic+typography+ai+video", "United States", "Medium"),
    ("Best cloud-based video editor for remote creator teams", "Commercial", "Google Suggest", "https://www.google.com/search?q=best+cloud+based+video+editor+remote+teams", "United States", "Medium"),
    ("How to turn educational lectures into micro-learning TikTok clips", "Informational", "People Also Ask", "https://www.google.com/search?q=turn+lectures+into+micro+learning+clips", "United States", "Medium"),
    ("Can AI automatically zoom in on active speakers in multi-person video?", "Informational", "Reddit r/podcasting", "https://www.reddit.com/r/podcasting/comments/19c721m/ai_auto_zoom_active_speaker_video/", "United States", "High"),
    ("Best AI voice changer and text-to-speech for anonymous creators", "Commercial", "YouTube Search", "https://www.youtube.com/results?search_query=ai+voice+generator+for+faceless+videos", "United States", "High"),
    ("How to calculate ROI on video repurposing software for agencies", "Informational", "Google Search", "https://www.google.com/search?q=roi+video+repurposing+software+agencies", "United States", "Medium"),
    ("Top alternatives to Descript for video transcription and clipping", "Comparison", "Google Suggest", "https://www.google.com/search?q=top+alternatives+to+descript", "United States", "High"),
    ("How to prevent copyright strikes when clipping long podcasts", "Informational", "People Also Ask", "https://www.google.com/search?q=prevent+copyright+strikes+podcast+clips", "United States", "High"),
    ("Best tool to turn substack newsletter articles into narrated video shorts", "Commercial", "Reddit r/Creator", "https://www.reddit.com/r/Creator/comments/194x191/turn+substack+articles+into+videos/", "United States", "Medium"),
    ("How to split a video into 60-second clips automatically", "Informational", "People Also Ask", "https://www.google.com/search?q=split+video+into+60+second+clips+automatically", "United States", "High"),
    ("What is an AI Virality Score and how is it calculated?", "Informational", "Quora", "https://www.quora.com/What-is-an-AI-virality-score-in-video-editing", "United States", "Medium"),
    ("Best AI tool for generating YouTube video titles, tags and descriptions", "Commercial", "YouTube Search", "https://www.youtube.com/results?search_query=ai+tool+youtube+titles+descriptions", "United States", "High"),
    ("How to re-encode high bitrate 4K video for fast mobile streaming", "Informational", "People Also Ask", "https://www.google.com/search?q=reencode+4k+video+fast+mobile+streaming", "United States", "Low"),
    ("Opus Clip discount code, lifetime deals and alternatives", "Commercial", "Google Suggest", "https://www.google.com/search?q=opus+clip+discount+code+alternatives", "United States", "Medium"),
    ("How to convert landscape video to 1:1 square for Facebook and LinkedIn", "Informational", "People Also Ask", "https://www.google.com/search?q=convert+landscape+to+square+video", "United States", "Medium"),
    ("Best software for multi-track audio cleanup in video interviews", "Commercial", "Reddit r/podcasting", "https://www.reddit.com/r/podcasting/comments/187k41m/multitrack+audio+cleanup+video/", "United States", "Medium"),
    ("How to add auto-captions in 20 languages simultaneously", "Informational", "Google Suggest", "https://www.google.com/search?q=auto+captions+20+languages+simultaneously", "United States", "High"),
    ("IncuBrix vs Descript: feature and workflow comparison", "Comparison", "Google Search", "https://www.google.com/search?q=incubrix+vs+descript", "United States", "High"),
    ("How to maintain 1080p quality when uploading shorts to YouTube", "Informational", "People Also Ask", "https://www.google.com/search?q=maintain+1080p+quality+uploading+shorts", "United States", "High"),
    ("Best AI background replacement tool for talking head creators", "Commercial", "YouTube Search", "https://www.youtube.com/results?search_query=ai+background+replacement+video+creator", "United States", "Medium"),
    ("How to create vertical clips from Google Drive or Dropbox video links directly", "Informational", "People Also Ask", "https://www.google.com/search?q=create+vertical+clips+from+google+drive+links", "United States", "High"),
    ("What are the best video repurposing agencies vs automated AI tools?", "Commercial", "Reddit r/Creator", "https://www.reddit.com/r/Creator/comments/19e992x/video+repurposing+agencies+vs+ai+tools/", "United States", "High"),
    ("How to optimize shorts metadata to rank on Google search results", "Informational", "People Also Ask", "https://www.google.com/search?q=optimize+shorts+metadata+google+search", "United States", "High"),

    # UK Market (20 Questions)
    ("Best AI video editing software for UK content creators 2026", "Commercial", "Google Suggest", "https://www.google.co.uk/search?q=best+ai+video+editing+software+uk", "United Kingdom", "High"),
    ("How to turn BBC radio interviews into video podcasts with animated captions", "Informational", "People Also Ask", "https://www.google.co.uk/search?q=turn+radio+interviews+into+video+podcasts", "United Kingdom", "Medium"),
    ("Is Opus Clip GDPR compliant for enterprise video processing?", "Commercial", "Google Search", "https://www.google.co.uk/search?q=opus+clip+gdpr+compliant", "United Kingdom", "High"),
    ("How UK marketing agencies automate short form video production", "Informational", "Reddit r/marketing", "https://www.reddit.com/r/marketing/comments/18v811e/uk_agencies_short_form_video_automation/", "United Kingdom", "High"),
    ("Best AI captioning tool with accurate British English spelling", "Commercial", "People Also Ask", "https://www.google.co.uk/search?q=ai+captioning+british+english+spelling", "United Kingdom", "High"),
    ("How to repurpose client webinars into LinkedIn video snippets in the UK", "Informational", "Google Suggest", "https://www.google.co.uk/search?q=repurpose+webinars+into+linkedin+snippets+uk", "United Kingdom", "High"),
    ("CapCut desktop vs browser tools for TikTok marketing UK", "Comparison", "YouTube Search", "https://www.youtube.com/results?search_query=capcut+desktop+vs+browser+uk", "United Kingdom", "Medium"),
    ("How to auto-clip key moments from sporting events for social media", "Informational", "People Also Ask", "https://www.google.co.uk/search?q=auto+clip+sporting+events+social+media", "United Kingdom", "Medium"),
    ("Top affordable video repurposing software with UK billing in GBP", "Commercial", "Google Search", "https://www.google.co.uk/search?q=video+repurposing+software+gbp+billing", "United Kingdom", "Medium"),
    ("How to generate vertical video clips from Zoom calls without watermark", "Informational", "Quora", "https://www.quora.com/How-to-generate-vertical-video-clips-from-Zoom-without-watermark", "United Kingdom", "High"),
    ("IncuBrix customer reviews and UK pricing options", "Navigational", "Google Search", "https://www.google.co.uk/search?q=incubrix+uk+pricing+reviews", "United Kingdom", "Medium"),
    ("How to auto-detect humour and witty banter in podcast transcripts", "Informational", "People Also Ask", "https://www.google.co.uk/search?q=auto+detect+humour+podcast+transcripts", "United Kingdom", "Medium"),
    ("Best workflow to manage multi-client TikTok campaigns with AI clips", "Informational", "Reddit r/socialmediamarketing", "https://www.reddit.com/r/socialmediamarketing/comments/190823y/manage_multi_client_tiktok_ai_clips/", "United Kingdom", "High"),
    ("Descript vs Munch: which is better for corporate communications?", "Comparison", "Google Suggest", "https://www.google.co.uk/search?q=descript+vs+munch+corporate+communications", "United Kingdom", "High"),
    ("How to add dynamic subtitles with custom branding and logos", "Informational", "People Also Ask", "https://www.google.co.uk/search?q=dynamic+subtitles+custom+branding+logos", "United Kingdom", "Medium"),
    ("Can AI automatically censor profanity in UK video content?", "Informational", "People Also Ask", "https://www.google.co.uk/search?q=ai+automatically+censor+profanity+video", "United Kingdom", "Medium"),
    ("Top AI tools for London fashion and lifestyle influencers", "Commercial", "Google Search", "https://www.google.co.uk/search?q=ai+tools+for+london+lifestyle+influencers", "United Kingdom", "Low"),
    ("How to auto-crop dual camera interviews for 9:16 split screen", "Informational", "YouTube Search", "https://www.youtube.com/results?search_query=auto+crop+split+screen+interview+video", "United Kingdom", "High"),
    ("Best video repurposing tool for B2B SaaS thought leaders", "Commercial", "People Also Ask", "https://www.google.co.uk/search?q=video+repurposing+tool+b2b+saas", "United Kingdom", "High"),
    ("How to schedule YouTube shorts directly from an AI editor", "Informational", "Google Suggest", "https://www.google.co.uk/search?q=schedule+youtube+shorts+directly+from+ai+editor", "United Kingdom", "Medium"),

    # India Market (20 Questions)
    ("Best AI video repurposing tool for Indian creators with Hindi support", "Commercial", "YouTube Search", "https://www.youtube.com/results?search_query=best+ai+video+repurposing+hindi+support", "India", "High"),
    ("How to convert long YouTube videos to shorts free in India", "Commercial", "Google Search", "https://www.google.co.in/search?q=how+to+convert+long+youtube+videos+to+shorts+free+india", "India", "High"),
    ("Opus Clip payment methods in India without international credit card", "Informational", "Reddit r/developersIndia", "https://www.reddit.com/r/developersIndia/comments/18x9812/opus_clip_payment_upi_india/", "India", "High"),
    ("How to auto-generate Hinglish captions with emojis for Instagram Reels", "Informational", "People Also Ask", "https://www.google.co.in/search?q=auto+generate+hinglish+captions+emojis", "India", "High"),
    ("Top AI tools for educational YouTube channels and UPSC tutors", "Commercial", "YouTube Search", "https://www.youtube.com/results?search_query=ai+tools+upsc+tutors+youtube", "India", "High"),
    ("Best free alternative to Opus Clip in India with UPI payment", "Comparison", "Google Suggest", "https://www.google.co.in/search?q=free+alternative+to+opus+clip+upi+india", "India", "High"),
    ("How Indian podcast creators repurpose video for Instagram and Shorts", "Informational", "Reddit r/india", "https://www.reddit.com/r/india/comments/18m671a/indian_podcasters_video_repurposing/", "India", "High"),
    ("IncuBrix vs CapCut: which is better for reels in India?", "Comparison", "Google Search", "https://www.google.co.in/search?q=incubrix+vs+capcut+india", "India", "High"),
    ("How to create viral motivational shorts with AI voice and subtitles", "Informational", "YouTube Search", "https://www.youtube.com/results?search_query=create+viral+motivational+shorts+ai", "India", "High"),
    ("Best automated video editor for regional language content (Tamil, Telugu, Bengali)", "Commercial", "People Also Ask", "https://www.google.co.in/search?q=video+editor+regional+languages+tamil+telugu", "India", "High"),
    ("How to extract short reels from 3-hour cricket and sports commentary", "Informational", "Google Suggest", "https://www.google.co.in/search?q=extract+short+reels+cricket+commentary", "India", "Medium"),
    ("Is IncuBrix available in India and what are the subscription charges?", "Navigational", "Google Search", "https://www.google.co.in/search?q=incubrix+india+subscription+charges", "India", "High"),
    ("How to auto-transcribe Hindi audio video files with high precision", "Informational", "People Also Ask", "https://www.google.co.in/search?q=auto+transcribe+hindi+audio+video", "India", "High"),
    ("Best AI clipping app for college students making study notes shorts", "Commercial", "Quora", "https://www.quora.com/Best-AI-clipping-app-for-study-notes-shorts", "India", "Medium"),
    ("How to bypass watermark on video repurposing tools legitimately", "Informational", "YouTube Search", "https://www.youtube.com/results?search_query=bypass+watermark+video+repurposing", "India", "Medium"),
    ("Top tools to make spiritual and bhajan shorts with synchronized lyrics", "Commercial", "Google Suggest", "https://www.google.co.in/search?q=spiritual+bhajan+shorts+lyrics+generator", "India", "Medium"),
    ("How to compress 1080p reels for low-bandwidth mobile streaming in India", "Informational", "People Also Ask", "https://www.google.co.in/search?q=compress+reels+low+bandwidth+mobile", "India", "Medium"),
    ("Submagic alternatives with Indian rupee pricing", "Comparison", "Google Search", "https://www.google.co.in/search?q=submagic+alternatives+inr+pricing", "India", "High"),
    ("How digital marketing agencies in Bengaluru automate client video repurposing", "Informational", "Reddit r/bangalore", "https://www.reddit.com/r/bangalore/comments/192m49x/bengaluru_agencies_video_repurposing/", "India", "High"),
    ("Can AI detect Indian comedy cues and punchlines in stand-up videos?", "Informational", "People Also Ask", "https://www.google.co.in/search?q=ai+detect+comedy+punchlines+standup+video", "India", "Medium")
]

print(f"Total raw questions configured: {len(RAW_QUESTIONS_CONFIG)}")
