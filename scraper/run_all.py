import logging
from datetime import datetime

from backend.db import SessionLocal
from backend.models import TrafficItem

from scraper.sources.dvb_rss import DVBRssScraper

# später: weitere Scraper importieren


# --------------------------------------------------
# 1. Logging konfigurieren
# --------------------------------------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

logger = logging.getLogger(__name__)


# --------------------------------------------------
# 2. Scraper registrieren
# --------------------------------------------------
SCRAPERS = [
    DVBRssScraper(),
    # später: SaechsischeRssScraper(), BMDV-RSS, …
]

# --------------------------------------------------
# 3. Hauptfunktion
# --------------------------------------------------
def main():
    logger.info("Scraping gestartet")

    db = SessionLocal()
    inserted = 0
    skipped = 0
    errors = 0

    try:
        for scraper in SCRAPERS:
            logger.info(f"Starte Scraper: {scraper.source_name}")

            try:
                items = scraper.fetch()
                logger.info(f"   → {len(items)} Einträge gefunden")

            except Exception as e:
                logger.error(f"❌ Fehler beim Scrapen von {scraper.source_name}: {e}")
                errors += 1
                continue

            for item in items:
                print("fehler"+item["url"])
                try:
                    # Prüfen, ob der Eintrag bereits existiert
                    exists = db.query(TrafficItem).filter(TrafficItem.url == item["url"]).first()

                    if exists:
                        skipped += 1
                        continue

                    db_item = TrafficItem(
                        category=scraper.category,
                        title=item["title"],
                        summary=item.get("summary"),
                        region=item.get("region"),
                        published_date=item.get("published_date"),
                        url=item["url"],
                    )

                    db.add(db_item)
                    inserted += 1

                except Exception as e:
                    logger.error(f"❌ DB-Fehler bei URL {item.get('url')}: {e}")
                    errors += 1

        db.commit()
        logger.info("💾 Änderungen erfolgreich gespeichert")

    except Exception as fatal:
        db.rollback()
        logger.critical(f"🔥 Kritischer Fehler – Rollback: {fatal}")

    finally:
        db.close()
        logger.info("🔒 DB-Verbindung geschlossen")

        logger.info(f"✅ Fertig | Neu: {inserted}, " f"Übersprungen: {skipped}, " f"Fehler: {errors}")


# --------------------------------------------------
# 4. Einstiegspunkt
# --------------------------------------------------
if __name__ == "__main__":
    main()
