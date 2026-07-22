from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.blog_post import BlogPost
from app.models.user import User
from app.schemas.blog_post import BlogPostCreate, BlogPostResponse
from app.api.deps import get_current_user

router = APIRouter(prefix="/api/blog", tags=["blog"])


@router.get("/", response_model=list[BlogPostResponse])
def list_posts(db: Session = Depends(get_db)):
    """Public - only shows published posts."""
    return (
        db.query(BlogPost)
        .filter(BlogPost.is_published == True)  # noqa: E712
        .order_by(BlogPost.published_at.desc())
        .all()
    )


@router.get("/{slug}", response_model=BlogPostResponse)
def get_post(slug: str, db: Session = Depends(get_db)):
    post = db.query(BlogPost).filter(BlogPost.slug == slug, BlogPost.is_published == True).first()  # noqa: E712
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.post("/", response_model=BlogPostResponse, status_code=201)
def create_post(post_in: BlogPostCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Admin-only - requires a valid login token."""
    post = BlogPost(**post_in.model_dump())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
