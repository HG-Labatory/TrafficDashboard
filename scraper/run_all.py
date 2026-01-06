from backend.db import SessionLocal
from sources.traffic_news import TrafficNewsScraper
from backend.repository import save_items

db = SessionLocal()

scraper = TrafficNewsScraper()
items = scraper.fetch()
save_items(db, items)

db.commit()
db.close()


