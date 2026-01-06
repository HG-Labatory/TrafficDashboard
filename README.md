# Verkehrs-Dashboard

## Überblick

Dieses Projekt ist ein **statisches Verkehrs-Dashboard**, das aktuelle Verkehrsmeldungen sammelt, strukturiert speichert und als **statische Webseite** bereitstellt.
Der Fokus liegt auf **Zuverlässigkeit**, **Einfachheit** und **kontrollierter Aktualisierung** ohne dauerhaft laufendes Backend.

Die Anwendung richtet sich an die **Allgemeinheit** und stellt Informationen aus der Verkehrswelt übersichtlich dar (z. B. Verkehrsmeldungen, perspektivisch Verkehrsprojekte und Verkehrswissenschaft).

---

## Grundidee

Statt einer klassischen Webanwendung mit dauerhaft laufendem Server folgt das Projekt einem **Build-Time-Ansatz**:

* Daten werden **periodisch gesammelt** (Scraper)
* strukturiert in einer **Datenbank** gespeichert
* **beim Deploy** aus der Datenbank in **JSON-Dateien exportiert**
* die Webseite liest **nur statische JSON-Daten** (GitHub Pages)

👉 Kein Backend-Server, keine API zur Laufzeit, keine offenen Ports.

---

## Architektur

```
RSS / Webseiten
        ↓
Python Scraper (run_all.py)
        ↓
PostgreSQL Datenbank (traffic_items)
        ↓
Export-Skript (export_data.py)
        ↓
JSON-Dateien (docs/data/news.json)
        ↓
Statische Webseite (GitHub Pages)
```

### Architekturprinzip

> **Die Datenbank ist die interne Quelle der Wahrheit.**
> **Die Webseite konsumiert ausschließlich statische Export-Artefakte.**

---

## Komponenten

### 1. Scraper

* Implementiert in Python
* Nutzt RSS-Feeds und ggf. strukturierte Webseiten
* Erkennt Duplikate (z. B. über `url`)
* Schreibt neue oder aktualisierte Einträge in die Datenbank

Beispielhafte Aufgaben:

* Verkehrsmeldungen sammeln
* Quellen vereinheitlichen
* Daten normalisieren

### 2. Datenbank (PostgreSQL)

Die Datenbank dient **nur der internen Verarbeitung**:

* Tabelle `traffic_items`
* saubere Struktur (Titel, Zusammenfassung, Region, URL, Datum)
* ermöglicht spätere Erweiterungen (Filter, Projekte, Wissenschaft)

Die Datenbank wird **nicht direkt von der Webseite angesprochen**.

### 3. Export-Skript

* Läuft **manuell oder automatisiert beim Deploy**
* Liest Daten aus der Datenbank
* Erzeugt JSON-Dateien für die Webseite

Beispiel:

* `docs/data/news.json`

Damit ersetzt das Export-Skript vollständig eine klassische API.

### 4. Statische Webseite

* Reines HTML, CSS und JavaScript
* Gehostet über GitHub Pages
* Lädt Daten über `fetch()` aus JSON-Dateien
* Keine dynamischen Server-Abfragen

Die Webseite ist dadurch:

* schnell
* kostengünstig
* stabil
* leicht wartbar

---

## Projektstruktur

```
traffic-dashboard/
├── backend/
│   ├── db.py
│   └── models.py
│
├── scraper/
│   ├── run_all.py        # Scraper → Datenbank
│   └── export_data.py   # Datenbank → JSON
│
├── docs/
│   ├── index.html
│   ├── app.js
│   ├── style.css
│   └── data/
│       └── news.json    # generiert
│
└── README.md
```

---

## Deploy-Workflow

Ein typischer Aktualisierungs- und Deploy-Ablauf:

```bash
1. Neue Daten sammeln

python -m scraper.run_all  

2. DB → JSON exportieren 

python -m scraper/export_data

# 3. Änderungen deployen
git add docs/data/news.json
git commit -m "Update traffic data"
git push
```

GitHub Pages übernimmt anschließend automatisch das Deployment der statischen Webseite.

---

## Warum diese Architektur?

### Vorteile

* ✅ Keine Serverkosten
* ✅ Kein dauerhaft laufendes Backend
* ✅ Klare Trennung von Datensammlung und Darstellung
* ✅ Hohe Stabilität
* ✅ Gut erweiterbar

### Bewusste Entscheidungen

* **Datenbank**: für saubere Datenhaltung und Erweiterbarkeit
* **Kein FastAPI**: da keine Laufzeit-API benötigt wird
* **Statische Webseite**: maximale Einfachheit beim Hosting
* **JSON als Austauschformat**: leichtgewichtig und browserfreundlich

---

## Erweiterungsmöglichkeiten

* zusätzliche Kategorien (Verkehrsprojekte, Wissenschaft)
* mehrere JSON-Exports
* automatische Updates per GitHub Actions
* Filter und Sortierung im Frontend
* späterer Übergang zu einer API bei Bedarf

---

## Fazit

Dieses Projekt zeigt, wie man mit einfachen Mitteln ein **robustes, wartungsarmes Verkehrs-Dashboard** umsetzen kann:

* **Scraper + Datenbank** für Qualität
* **Build-Time-Export** für Kontrolle
* **Statische Webseite** für Zuverlässigkeit

Eine bewusste Architekturentscheidung zugunsten von Klarheit statt Komplexität.
