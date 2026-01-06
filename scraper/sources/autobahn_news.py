from playwright.sync_api import sync_playwright
from scraper.base import BaseScraper


class AutobahnNewsScraper(BaseScraper):
    source_name = "Autobahn GmbH"
    category = "traffic_news"

    def fetch(self):
        items = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto(
                "https://www.autobahn.de/betrieb-verkehr/verkehrsmeldungen?tx_kesearch_pi1%5Bsword%5D=&tx_kesearch_pi1%5Bpage%5D=1&tx_kesearch_pi1%5BresetFilters%5D=0&tx_kesearch_pi1%5BshowMap%5D=&tx_kesearch_pi1%5Bfilter_1%5D=&search_terms=&tx_kesearch_pi1%5Bfilter_2%5D=syscat294&search_terms=#search",
                timeout=60_000,
            )

            # WICHTIG: warten bis Meldungen geladen sind
            page.wait_for_selector("article", timeout=60_000)

            articles = page.query_selector_all("article")

            for a in articles:
                title = a.inner_text().split("\n")[0]

                items.append(
                    {
                        "title": title,
                        "summary": a.inner_text(),
                        "region": "DE",
                        "published_date": None,
                        "url": "https://www.autobahn.de/verkehrsmeldungen",
                    }
                )

            browser.close()

        return items
