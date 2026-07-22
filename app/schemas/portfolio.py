from datetime import datetime
from pydantic import BaseModel


class PortfolioItemCreate(BaseModel):
    title: str
    slug: str
    client_name: str | None = None
    summary: str
    description: str | None = None
    cover_image_url: str | None = None
    tech_used: str | None = None
    project_url: str | None = None


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
