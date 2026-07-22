"""
Portfolio / case study items - proof of work to show prospective clients.
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, func

from app.db.database import Base


class PortfolioItem(Base):
    __tablename__ = "portfolio_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    slug = Column(String(170), unique=True, nullable=False, index=True)
    client_name = Column(String(150), nullable=True)
    summary = Column(String(300), nullable=False)
    description = Column(Text, nullable=True)
    cover_image_url = Column(String(500), nullable=True)
    tech_used = Column(String(300), nullable=True)  # comma-separated for simplicity, e.g. "FastAPI,Next.js"
    project_url = Column(String(500), nullable=True)  # live link, if any
    created_at = Column(DateTime(timezone=True), server_default=func.now())
