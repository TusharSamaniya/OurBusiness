"""
Pydantic schemas define what shape of data your API accepts (request) and
returns (response). Keeping these separate from SQLAlchemy models is
intentional - it stops you from accidentally exposing internal DB fields.
"""
from datetime import datetime
from pydantic import BaseModel, EmailStr


class LeadCreate(BaseModel):
    """What the public contact form sends us."""
    name: str
    email: EmailStr
    phone: str | None = None
    service_interested: str | None = None
    message: str


class LeadResponse(BaseModel):
    """What we send back after creating/reading a lead."""
    id: int
    name: str
    email: EmailStr
    phone: str | None
    service_interested: str | None
    message: str
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}  # allows reading from SQLAlchemy objects
