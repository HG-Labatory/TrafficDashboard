# backend/api/news.py
from fastapi import APIRouter
from backend.db import SessionLocal
from backend.models import TrafficItem

router = APIRouter()



@router.get("/")
def get_all_news():
    db = SessionLocal()
    items = db.query(TrafficItem).all()
    db.close()
    return items


