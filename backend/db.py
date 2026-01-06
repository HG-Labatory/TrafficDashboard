from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database connection URL
DATABASE_URL = "postgresql://traffic_user:traffic@localhost/traffic_db"

# Set up the database engine and session factory
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(bind=engine)
