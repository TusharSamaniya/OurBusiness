"""
Blog posts - for content marketing / SEO. Kept simple for now: no author
table yet since it's just you/your team, and no auth on users table exists
yet either.
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, func

from app.db.database import Base


class BlogPost(Base):
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    slug = Column(String(220), unique=True, nullable=False, index=True)
    excerpt = Column(String(300), nullable=True)
    content = Column(Text, nullable=False)
    cover_image_url = Column(String(500), nullable=True)
    is_published = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    published_at = Column(DateTime(timezone=True), nullable=True)
