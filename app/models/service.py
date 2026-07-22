"""
The services you offer (Website Development, App Development, AI Bots, Digital
Marketing, etc.) - shown on your homepage/services page.
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, func

from app.db.database import Base


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(120), nullable=False)
    slug = Column(String(140), unique=True, nullable=False, index=True)
    short_description = Column(String(300), nullable=False)
    description = Column(Text, nullable=True)
    icon = Column(String(100), nullable=True)  # e.g. an icon name/class used by frontend
    created_at = Column(DateTime(timezone=True), server_default=func.now())
