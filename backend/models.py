from sqlalchemy import Column, Integer, Text, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class TrafficItem(Base):
    """Database model for a single traffic-related item.

    This model represents a normalized record of traffic information
    such as news, incidents, or advisories stored in the database.
    """
    __tablename__ = "traffic_items"

    id = Column(Integer, primary_key=True)
    category = Column(Text, nullable=False)
    title = Column(Text, nullable=False)
    summary = Column(Text)
    region = Column(Text)
    published_date = Column(Date)
    scraped_at = Column(DateTime, server_default=func.now())
    url = Column(Text, unique=True)
