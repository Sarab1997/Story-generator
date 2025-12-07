# db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define Base ONCE, here
class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    # Import models so they register with Base
    from models import story, job  # ← Import model modules
    
    print("🔧 Creating database tables...")
    print(f"📦 Tables to create: {list(Base.metadata.tables.keys())}")
    
    Base.metadata.create_all(bind=engine)
    
    print("✅ Tables created:", list(Base.metadata.tables.keys()))