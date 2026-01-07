import feedparser
from scraper.base import BaseScraper
from datetime import datetime


class DVBRssScraper(BaseScraper):
    source_name = "DVB"
    category = "traffic_news"

    FEED_URL = "https://www.dvb.de/de-de/meta/aktuelle-meldungen?sc_device=Feed"

    def fetch(self):
        feed = feedparser.parse(self.FEED_URL)
        items = []

        for entry in feed.entries:
            title = entry.get("title", "").strip()
            url = entry.get("link")
            summary = entry.get("summary", "").strip()

            if not title or not url:
                continue

            # ✅ RICHTIGES Datum aus feedparser
            published_parsed = entry.get("published_parsed")
            published_date = datetime(*published_parsed[:6]) if published_parsed else None

            items.append(
                {
                    "title": title,
                    "summary": summary,
                    "region": "Dresden",
                    "published_date": published_date,
                    "url": url,
                }
            )

        return items
