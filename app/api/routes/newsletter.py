from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.newsletter import NewsletterSubscriber
from app.schemas.newsletter import NewsletterSubscribeRequest, NewsletterSubscriberResponse
from app.core.limiter import limiter

router = APIRouter(prefix="/api/newsletter", tags=["newsletter"])


@router.post("/subscribe", response_model=NewsletterSubscriberResponse, status_code=201)
@limiter.limit("5/minute")
def subscribe(request: Request, payload: NewsletterSubscribeRequest, db: Session = Depends(get_db)):
    """Public - called from a newsletter signup form (footer, blog, etc.). Rate-limited to prevent spam."""
    subscriber = NewsletterSubscriber(email=payload.email)
    db.add(subscriber)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="This email is already subscribed")
    db.refresh(subscriber)
    return subscriber
