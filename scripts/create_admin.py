"""
Run once to create your admin login. There's no public /register endpoint
on purpose - you don't want strangers creating admin accounts.

Usage (inside the app container):
    docker compose exec app python scripts/create_admin.py
"""
import sys
from pathlib import Path

# Running this file directly (not as a package) means Python doesn't
# automatically know where the "app" package lives - this line adds the
# project root to the path so "from app..." imports below work.
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.db.database import SessionLocal
from app.models.user import User
from app.core.security import hash_password

email = input("Admin email: ").strip()
password = input("Admin password: ").strip()

db = SessionLocal()

existing = db.query(User).filter(User.email == email).first()
if existing:
    print(f"A user with email {email} already exists.")
else:
    user = User(email=email, hashed_password=hash_password(password))
    db.add(user)
    db.commit()
    print(f"Admin user created: {email}")

db.close()