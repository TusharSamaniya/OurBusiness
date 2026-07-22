"""
Admin user - just for you/your team to log in and manage content.
No public signup - accounts are created via scripts/create_admin.py only.
"""
from sqlalchemy import Column, Integer, String

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
