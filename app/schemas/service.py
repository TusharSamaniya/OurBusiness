from datetime import datetime
from pydantic import BaseModel, field_validator

from app.core.sanitize import sanitize_plain_text, sanitize_rich_text


class ServiceCreate(BaseModel):
    title: str
    slug: str
    short_description: str
    description: str | None = None
    icon: str | None = None

    @field_validator("title", "slug", "short_description")
    @classmethod
    def clean_plain_fields(cls, v: str) -> str:
        return sanitize_plain_text(v)

    @field_validator("description")
    @classmethod
    def clean_description(cls, v: str | None) -> str | None:
        return sanitize_rich_text(v) if v else v


class ServiceResponse(BaseModel):
    id: int
    title: str
    slug: str
    short_description: str
    description: str | None
    icon: str | None
    created_at: datetime

    model_config = {"from_attributes": True}
