from pathlib import Path
import json
import feedparser
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = DATA_DIR / "news.json"


FEEDS = [
    {
        "name": "DVB",
        "region": "Dresden",
        "url": "https://www.dvb.de/de-de/meta/aktuelle-meldungen?sc_device=Feed",
    },
]

items = []

for feed_cfg in FEEDS:
    feed = feedparser.parse(feed_cfg["url"])

    for entry in feed.entries:
        title = entry.get("title")
        link = entry.get("link")

        if not title or not link:
            continue

        items.append(
            {
                "source": feed_cfg["name"],
                "region": feed_cfg["region"],
                "title": title.strip(),
                "summary": entry.get("summary", "").strip(),
                "url": link,
                "published": entry.get("published"),
            }
        )

output = {
    "generated_at": datetime.utcnow().isoformat(),
    "count": len(items),
    "items": items,
}

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"✅ {len(items)} Einträge geschrieben")
