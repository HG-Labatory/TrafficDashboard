import feedparser
from scraper.base import BaseScraper


class DLRRssScraper(BaseScraper):
    source_name = "DLR"
    category = ""

    FEED_URL = "https://www.dlr.de/++api++/@@rss?portal_type=News%20Item&research_domains=0a65b8491e3447dba8e36e1fa48ce5e0&Language=de"

    def fetch(self):
        feed = feedparser.parse(self.FEED_URL)
        items = []

        for entry in feed.entries:
            title = entry.get("title", "").strip() # type: ignore
            url = entry.get("link")
            summary = entry.get("description", "").strip()  # type: ignore

            if not title or not url:
                continue

            items.append({"title": title, "summary": summary, "region": "", "published_date": entry.get("pubDate"), "url": url})

        return items
