"""
Routes for lead/contact form submissions.
This is the single most important endpoint in your whole app - it's how
leads reach you. Everything else can wait; this can't.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.lead import Lead
from app.schemas.lead import LeadCreate, LeadResponse

router = APIRouter(prefix="/api/leads", tags=["leads"])


@router.post("/", response_model=LeadResponse, status_code=201)
def create_lead(lead_in: LeadCreate, db: Session = Depends(get_db)):
    """
    Public endpoint - hit by your contact form on the frontend.
    Later: this is also where you'll trigger a notification email to yourself.
    """
    lead = Lead(**lead_in.model_dump())
    db.add(lead)
    db.commit()
    db.refresh(lead)
    return lead


@router.get("/", response_model=list[LeadResponse])
def list_leads(db: Session = Depends(get_db)):
    """
    Admin-only endpoint (auth to be added in Step 3) - view all inquiries.
    """
    return db.query(Lead).order_by(Lead.created_at.desc()).all()
