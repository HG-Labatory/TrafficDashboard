

class BaseScraper:
    """Base interface for concrete traffic data scrapers.

    This class defines the common attributes and required fetch behavior
    that all scraper implementations must provide.
    """
    source_name: str
    category: str

    def fetch(self) -> list[dict]:
        raise NotImplementedError

