1. Neue Daten sammeln - 
schreibt Daten in die Datenbank traffic_db in die Tabelle traffic_items

python -m scraper.run_all  

2. DB → JSON exportieren 
öffnet die DB und holt sich Items und beschreibt die news.json

python -m scraper/export_data

3. Statische Seite aktualisieren

git add docs/data/news.json
git commit -m "Update traffic data"
git push
