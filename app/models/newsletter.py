"""
Newsletter/marketing list signups - separate from leads because these people
just want updates, they haven't necessarily requested a project quote.
"""
from sqlalchemy import Column, Integer, String, DateTime, func

from app.db.database import Base


class NewsletterSubscriber(Base):
    __tablename__ = "newsletter_subscribers"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    subscribed_at = Column(DateTime(timezone=True), server_default=func.now())
