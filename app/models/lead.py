"""
SQLAlchemy model for a contact/lead inquiry - the most important table since
it's how potential clients reach you through the contact form.
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, func

from app.db.database import Base


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    email = Column(String(255), nullable=False, index=True)
    phone = Column(String(30), nullable=True)
    service_interested = Column(String(100), nullable=True)  # e.g. "AI Bot", "Website"
    message = Column(Text, nullable=False)
    status = Column(String(30), default="new")  # new / contacted / converted / closed
    created_at = Column(DateTime(timezone=True), server_default=func.now())
