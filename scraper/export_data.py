import json
from pathlib import Path
from datetime import datetime

from backend.db import SessionLocal
from backend.models import TrafficItem

# Zielpfad für GitHub Pages
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "docs" / "data"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "news.json"

db = SessionLocal()

items = db.query(TrafficItem).order_by(TrafficItem.published_date.desc()).all()

db.close()

export = {
    "generated_at": datetime.utcnow().isoformat(),
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

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(export, f, ensure_ascii=False, indent=2)

print(f"✅ Exportiert: {len(items)} Einträge → {OUTPUT_FILE}")
