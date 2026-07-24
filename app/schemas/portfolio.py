from datetime import datetime
from pydantic import BaseModel, field_validator

from app.core.sanitize import sanitize_plain_text, sanitize_rich_text


class PortfolioItemCreate(BaseModel):
    title: str
    slug: str
    client_name: str | None = None
    summary: str
    description: str | None = None
    cover_image_url: str | None = None
    tech_used: str | None = None
    project_url: str | None = None

    @field_validator("title", "slug", "summary")
    @classmethod
    def clean_plain_fields(cls, v: str) -> str:
        return sanitize_plain_text(v)

    @field_validator("client_name", "tech_used")
    @classmethod
    def clean_optional_plain_fields(cls, v: str | None) -> str | None:
        return sanitize_plain_text(v) if v else v

    @field_validator("description")
    @classmethod
    def clean_description(cls, v: str | None) -> str | None:
        return sanitize_rich_text(v) if v else v


class PortfolioItemResponse(BaseModel):
    id: int
    title: str
    slug: str
    client_name: str | None
    summary: str
    description: str | None
    cover_image_url: str | None
    tech_used: str | None
    project_url: str | None
    created_at: datetime

    model_config = {"from_attributes": True}
