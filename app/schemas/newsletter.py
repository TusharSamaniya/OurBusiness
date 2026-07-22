from datetime import datetime
from pydantic import BaseModel, EmailStr


class NewsletterSubscribeRequest(BaseModel):
    email: EmailStr


class NewsletterSubscriberResponse(BaseModel):
    id: int
    email: EmailStr
    subscribed_at: datetime

    model_config = {"from_attributes": True}
