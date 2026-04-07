import subprocess
import json
import snscrape.modules.twitter as sntwitter
import requests
from bs4 import BeautifulSoup

class DataCollector:

    def fetch_youtube(self, query="crypto news"):
        """Fetch top YouTube videos using yt-dlp."""
        command = [
            "yt-dlp", f"ytsearch5:{query}",
            "--dump-json"
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        videos = [json.loads(line) for line in result.stdout.split("\n") if line.strip()]
        return [
            {
                "title": v.get("title"),
                "url": v.get("webpage_url"),
                "views": v.get("view_count", 0)
            }
            for v in videos
        ]

    def fetch_twitter(self, query="crypto", limit=10):
        """Fetch viral tweets using snscrape."""
        tweets = []
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            if len(tweets) > limit:
                break
            tweets.append({
                "content": tweet.rawContent,
                "likes": tweet.likeCount,
                "retweets": tweet.retweetCount
            })
        return tweets

    def fetch_reddit(self):
        """Scrape trending crypto posts from Reddit."""
        url = "https://www.reddit.com/r/cryptocurrency/hot/"
        headers = {"User-Agent": "Mozilla/5.0"}
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")

        posts = []
        for post in soup.find_all("h3")[:10]:
            posts.append({"title": post.text})
        return posts

    def fetch_news(self):
        """Scrape crypto news headlines."""
        url = "https://cointelegraph.com/tags/crypto"
        headers = {"User-Agent": "Mozilla/5.0"}
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")

        headlines = [h.text.strip() for h in soup.select("span.post-card__title")[:10]]
        return headlines
