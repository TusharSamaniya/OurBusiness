from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceResponse

router = APIRouter(prefix="/api/services", tags=["services"])


@router.get("/", response_model=list[ServiceResponse])
def list_services(db: Session = Depends(get_db)):
    """Public - feeds your homepage/services page."""
    return db.query(Service).order_by(Service.created_at.desc()).all()


@router.get("/{slug}", response_model=ServiceResponse)
def get_service(slug: str, db: Session = Depends(get_db)):
    service = db.query(Service).filter(Service.slug == slug).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service


@router.post("/", response_model=ServiceResponse, status_code=201)
def create_service(service_in: ServiceCreate, db: Session = Depends(get_db)):
    """Admin-only once auth is added (Step 3)."""
    service = Service(**service_in.model_dump())
    db.add(service)
    db.commit()
    db.refresh(service)
    return service
