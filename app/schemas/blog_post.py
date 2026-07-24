from datetime import datetime
from pydantic import BaseModel, field_validator

from app.core.sanitize import sanitize_plain_text, sanitize_rich_text


class BlogPostCreate(BaseModel):
    title: str
    slug: str
    excerpt: str | None = None
    content: str
    cover_image_url: str | None = None
    is_published: bool = False

    @field_validator("title", "slug")
    @classmethod
    def clean_plain_fields(cls, v: str) -> str:
        return sanitize_plain_text(v)

    @field_validator("excerpt")
    @classmethod
    def clean_excerpt(cls, v: str | None) -> str | None:
        return sanitize_plain_text(v) if v else v

    @field_validator("content")
    @classmethod
    def clean_content(cls, v: str) -> str:
        return sanitize_rich_text(v)


class BlogPostResponse(BaseModel):
    id: int
    title: str
    slug: str
    excerpt: str | None
    content: str
    cover_image_url: str | None
    is_published: bool
    created_at: datetime
    published_at: datetime | None

    model_config = {"from_attributes": True}
