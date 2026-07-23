"""
Single endpoint: send an image, get back a URL. Admin-only since only you
should be uploading content images (not public visitors).
"""
from fastapi import APIRouter, Depends, UploadFile, File

from app.models.user import User
from app.api.deps import get_current_user
from app.services.upload import upload_image

router = APIRouter(prefix="/api/upload", tags=["upload"])


@router.post("/image")
def upload_image_route(file: UploadFile = File(...), current_user: User = Depends(get_current_user)):
    url = upload_image(file)
    return {"url": url}
