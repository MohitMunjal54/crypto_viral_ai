# crypto_viral_ai

The system:
Collects viral crypto content from YouTube, Twitter, Reddit & crypto news
Identifies patterns, hooks, keywords, and narratives
Generates viral-ready content ideas using local LLMs (Ollama + Llama3)
Fully open-source & local



# Architecture of code :

┌──────────────────────┐
             │   YouTube Scraper    │
             └──────────┬───────────┘
                        │
             ┌──────────▼───────────┐
             │    Twitter Scraper    │
             └──────────┬───────────┘
                        │
             ┌──────────▼───────────┐
             │     Reddit Scraper    │
             └──────────┬───────────┘
                        │
             ┌──────────▼───────────┐
             │  Crypto News Scraper  │
             └──────────┬───────────┘
                        │
                        ▼
        ┌──────────────────────────────────┐
        │          PATTERN ANALYZER        │
        │ (keywords + hooks + narratives)  │
        └──────────────────┬───────────────┘
                           │
                           ▼
        ┌──────────────────────────────────┐
        │       AI VIRAL IDEA GENERATOR     │
        │      (Llama3 via Ollama local)    │
        └──────────────────────────────────┘
---------------------------------------------

# Features 
1. Viral Content Collection
 YouTube viral video titles & views
 Twitter viral posts using snscrape
 Reddit trending crypto discussions
 Crypto news headlines (CoinTelegraph etc.)
2. Pattern Recognition
  Extract trending keywords (KeyBERT)
  Find common hooks & storytelling styles
  Detect narratives (bullish, FUD, cycles,     AI-crypto etc.)
3. AI Content Generator
  5 viral Instagram Reel ideas
  3 YouTube video ideas
  3 Twitter threads
  Optional script outlines

## Installation and setup 
# 1. Clone repository 
git clone https://github.com/YourName/crypto-viral-ai.git
cd crypto-viral-ai

# 2. Install Dependencies 
pip install -r requirements.txt

# 3. Install local AI model
ollama pull llama3

# 4. Run the system 
python main.py

