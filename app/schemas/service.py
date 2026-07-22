from datetime import datetime
from pydantic import BaseModel


class ServiceCreate(BaseModel):
    title: str
    slug: str
    short_description: str
    description: str | None = None
    icon: str | None = None


class ServiceResponse(BaseModel):
    id: int
    title: str
    slug: str
    short_description: str
    description: str | None
    icon: str | None
    created_at: datetime

    model_config = {"from_attributes": True}
