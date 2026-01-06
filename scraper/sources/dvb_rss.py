import feedparser
from scraper.base import BaseScraper


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

            items.append(
                {"title": title, "summary": summary, "region": "Dresden", "published_date": entry.get("published_parsed"), "url": url}
            )

        return items

