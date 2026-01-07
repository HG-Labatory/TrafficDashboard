import json
from pathlib import Path
from datetime import datetime, timezone

from backend.db import SessionLocal
from backend.models import TrafficItem

# Zielpfad für GitHub Pages
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "docs" / "data"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

NEWS_FILE = OUTPUT_DIR / "news.json"
SCIENCE_FILE = OUTPUT_DIR / "science.json"

db = SessionLocal()


def export_category(category: str, output_file: Path):
    items = (
        db.query(TrafficItem)
        .filter(TrafficItem.category == category)
        .order_by(TrafficItem.published_date.desc().nullslast(), TrafficItem.id.desc())
        .limit(10)
        .all()
    )

    export = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "category": category,
        "count": len(items),
        "items": [
            {
                "id": item.id,
                "title": item.title,
                "summary": item.summary,
                "region": item.region,
                "url": item.url,
                "published_date": (item.published_date.isoformat() if item.published_date else None),
            }
            for item in items
        ],
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(export, f, ensure_ascii=False, indent=2)

    print(f"✅ Exportiert {len(items)} Einträge → {output_file.name}")


export_category("traffic_news", NEWS_FILE)
export_category("traffic_science", SCIENCE_FILE)

db.close()
