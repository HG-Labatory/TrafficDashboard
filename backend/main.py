from fastapi import FastAPI
from backend.api import news

app = FastAPI(title="Traffic Dashboard API")

app.include_router(news.router, prefix="/traffic/news", tags=["traffic-news"])
