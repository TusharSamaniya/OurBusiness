from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.portfolio import PortfolioItem
from app.models.user import User
from app.schemas.portfolio import PortfolioItemCreate, PortfolioItemResponse
from app.api.deps import get_current_user

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
def create_portfolio_item(item_in: PortfolioItemCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Admin-only - requires a valid login token."""
    item = PortfolioItem(**item_in.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.put("/{slug}", response_model=PortfolioItemResponse)
def update_portfolio_item(slug: str, item_in: PortfolioItemCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Admin-only - replaces all fields of an existing portfolio item."""
    item = db.query(PortfolioItem).filter(PortfolioItem.slug == slug).first()
    if not item:
        raise HTTPException(status_code=404, detail="Portfolio item not found")

    for field, value in item_in.model_dump().items():
        setattr(item, field, value)

    db.commit()
    db.refresh(item)
    return item


@router.delete("/{slug}", status_code=204)
def delete_portfolio_item(slug: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Admin-only - permanently removes a portfolio item."""
    item = db.query(PortfolioItem).filter(PortfolioItem.slug == slug).first()
    if not item:
        raise HTTPException(status_code=404, detail="Portfolio item not found")

    db.delete(item)
    db.commit()
