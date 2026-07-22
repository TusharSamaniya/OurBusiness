from datetime import datetime
from pydantic import BaseModel


class BlogPostCreate(BaseModel):
    title: str
    slug: str
    excerpt: str | None = None
    content: str
    cover_image_url: str | None = None
    is_published: bool = False


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
