# TrafficDashboard
TrafficDashboard

┌──────────────┐
│   RSS / Web  │
└──────┬───────┘
       ▼
┌──────────────────────┐
│ Python Scraper       │
│ (run_all.py)         │
│  → INSERT / UPDATE   │
└──────┬───────────────┘
       ▼
┌──────────────────────┐
│ PostgreSQL DB        │
│ traffic_items        │
└──────┬───────────────┘
       ▼
┌──────────────────────┐
│ Export-Skript        │
│ DB → JSON            │
└──────┬───────────────┘
       ▼
┌──────────────────────┐
│ docs/data/news.json  │
└─────────┬────────────┘
          ▼
┌──────────────────────┐
│ GitHub Pages (HTML)  │
└──────────────────────┘
