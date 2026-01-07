import logging

from backend.db import SessionLocal
from backend.models import TrafficItem

from scraper.sources.dvb_rss import DVBRssScraper
from scraper.sources.dlr_rss import DLRRssScraper

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
    DLRRssScraper(),
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

    for scraper in SCRAPERS:
        logger.info(f"Starte Scraper: {scraper.source_name}")

        try:
            items = scraper.fetch()
        except Exception as e:
            logger.exception(f"Fehler beim Fetch von {scraper.source_name}")
            errors += 1
            continue

        for item in items:
            try:
                exists = db.query(TrafficItem).filter(TrafficItem.url == item["url"]).first()

                if exists:
                    skipped += 1
                    continue

                db.add(
                    TrafficItem(
                        title=item["title"],
                        summary=item.get("summary", ""),
                        region=item.get("region", ""),
                        category=scraper.category,
                        url=item["url"],
                        published_date=item.get("published_date"),
                    )
                )

                inserted += 1

            except Exception as e:
                logger.exception(f"Fehler bei Item {item.get('url')}")
                errors += 1

    db.commit()
    db.close()

    logger.info(f"Scraping beendet | Neu: {inserted}, " f"Übersprungen: {skipped}, Fehler: {errors}")


# --------------------------------------------------
# Einstiegspunkt
# --------------------------------------------------
if __name__ == "__main__":
    main()
