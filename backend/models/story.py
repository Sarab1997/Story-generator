from datetime import datetime
from typing import List
from sqlalchemy import String, Integer, Boolean, DateTime, ForeignKey, JSON, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from db.database import Base 


class Story(Base):
    __tablename__ = "stories"
    
    # Primary key
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    # Regular columns
    title: Mapped[str] = mapped_column(String, index=True)
    session_id: Mapped[str] = mapped_column(String, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now()
    )
    
    # Relationship - one Story has many StoryNodes
    nodes: Mapped[List["StoryNode"]] = relationship(
        "StoryNode", 
        back_populates="story"
    )


class StoryNode(Base):
    __tablename__ = "story_nodes"
    
    # Primary key
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    # Foreign key
    story_id: Mapped[int] = mapped_column(
        Integer, 
        ForeignKey("stories.id"), 
        index=True
    )
    
    # Regular columns
    content: Mapped[str] = mapped_column(String)
    is_root: Mapped[bool] = mapped_column(Boolean, default=False)
    is_ending: Mapped[bool] = mapped_column(Boolean, default=False)
    is_winning_ending: Mapped[bool] = mapped_column(Boolean, default=False)
    options: Mapped[list] = mapped_column(JSON, default=list)
    
    # Relationship - each StoryNode belongs to one Story
    story: Mapped["Story"] = relationship("Story", back_populates="nodes")