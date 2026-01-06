import requests
from bs4 import BeautifulSoup
from scraper.base import BaseScraper


class TrafficNewsScraper(BaseScraper):
    """Scraper for traffic news articles from a specific source.

    This scraper fetches a traffic news overview page, parses the HTML,
    and returns a list of normalized news item dictionaries.
    """

    source_name = "Beispiel Quelle"
    category = "traffic_news"

    def fetch(self):
        """Fetch traffic news items from the configured source.

        This method retrieves the traffic news overview page and extracts
        individual news items into a normalized list of dictionaries.

        Returns:
            list[dict]: A list of traffic news items, each containing
                title, summary, region, published_date, and url fields.
        """
        # Fetch and parse the traffic news page
        response = requests.get(
            "https://www.autobahn.de/betrieb-verkehr/verkehrsmeldungen?tx_kesearch_pi1%5Bsword%5D=&tx_kesearch_pi1%5Bpage%5D=1&tx_kesearch_pi1%5BresetFilters%5D=0&tx_kesearch_pi1%5BshowMap%5D=&tx_kesearch_pi1%5Bfilter_1%5D=&search_terms=&tx_kesearch_pi1%5Bfilter_2%5D=syscat294&search_terms=#search"
        )

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        print()
        items = []

        for entry in soup.select(".news-item"):
            items.append(
                {
                    "title": entry.h2.text.strip(),
                    "summary": entry.p.text.strip(),
                    "region": "Deutschland",
                    "published_date": None,
                    "url": entry.a["href"],
                }
            )

        return items
