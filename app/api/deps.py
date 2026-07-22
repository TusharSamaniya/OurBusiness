"""
Add `current_user: User = Depends(get_current_user)` to any route to
require login. FastAPI runs this automatically before the route's own
code - if it raises, the route never even executes.
"""
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.user import User
from app.core.security import decode_access_token

# tokenUrl just tells FastAPI's /docs page where the "Authorize" button
# should send login requests - it doesn't affect how tokens are checked.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    email = decode_access_token(token)
    if email is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User no longer exists")

    return user
