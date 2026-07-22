"""
Routes for lead/contact form submissions.
This is the single most important endpoint in your whole app - it's how
leads reach you. Everything else can wait; this can't.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.lead import Lead
from app.models.user import User
from app.schemas.lead import LeadCreate, LeadResponse, LeadStatusUpdate
from app.api.deps import get_current_user
from app.services.email import send_lead_notification

router = APIRouter(prefix="/api/leads", tags=["leads"])


@router.post("/", response_model=LeadResponse, status_code=201)
def create_lead(lead_in: LeadCreate, db: Session = Depends(get_db)):
    """Public endpoint - hit by your contact form on the frontend."""
    lead = Lead(**lead_in.model_dump())
    db.add(lead)
    db.commit()
    db.refresh(lead)

    send_lead_notification(lead)  # best-effort - won't break this request if it fails

    return lead


@router.get("/", response_model=list[LeadResponse])
def list_leads(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Admin-only - requires a valid login token."""
    return db.query(Lead).order_by(Lead.created_at.desc()).all()


@router.patch("/{lead_id}", response_model=LeadResponse)
def update_lead_status(
    lead_id: int,
    payload: LeadStatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Admin-only - mark a lead as contacted/converted/etc."""
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    lead.status = payload.status
    db.commit()
    db.refresh(lead)
    return lead
