from datetime import datetime
from typing import Optional
from sqlalchemy import String, Integer, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from db.database import Base  



class StoryJob(Base):
    __tablename__ = "story_jobs"
    
    # Primary key
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    # Job tracking
    job_id: Mapped[str] = mapped_column(String, index=True, unique=True)
    session_id: Mapped[str] = mapped_column(String, index=True)
    
    # Story details
    theme: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    
    # Link to generated story (nullable - empty until story is created)
    story_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    
    # Error tracking (nullable - empty unless job fails)
    error: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    
    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now()
    )
    completed_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), 
        nullable=True
    )