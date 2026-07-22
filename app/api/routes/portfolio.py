from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.portfolio import PortfolioItem
from app.schemas.portfolio import PortfolioItemCreate, PortfolioItemResponse

router = APIRouter(prefix="/api/portfolio", tags=["portfolio"])


@router.get("/", response_model=list[PortfolioItemResponse])
def list_portfolio(db: Session = Depends(get_db)):
    """Public - feeds your portfolio/case studies page."""
    return db.query(PortfolioItem).order_by(PortfolioItem.created_at.desc()).all()


@router.get("/{slug}", response_model=PortfolioItemResponse)
def get_portfolio_item(slug: str, db: Session = Depends(get_db)):
    item = db.query(PortfolioItem).filter(PortfolioItem.slug == slug).first()
    if not item:
        raise HTTPException(status_code=404, detail="Portfolio item not found")
    return item


@router.post("/", response_model=PortfolioItemResponse, status_code=201)
def create_portfolio_item(item_in: PortfolioItemCreate, db: Session = Depends(get_db)):
    """Admin-only once auth is added (Step 3)."""
    item = PortfolioItem(**item_in.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
