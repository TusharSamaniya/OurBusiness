from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.newsletter import NewsletterSubscriber
from app.schemas.newsletter import NewsletterSubscribeRequest, NewsletterSubscriberResponse

router = APIRouter(prefix="/api/newsletter", tags=["newsletter"])


@router.post("/subscribe", response_model=NewsletterSubscriberResponse, status_code=201)
def subscribe(payload: NewsletterSubscribeRequest, db: Session = Depends(get_db)):
    """Public - called from a newsletter signup form (footer, blog, etc.)."""
    subscriber = NewsletterSubscriber(email=payload.email)
    db.add(subscriber)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="This email is already subscribed")
    db.refresh(subscriber)
    return subscriber
