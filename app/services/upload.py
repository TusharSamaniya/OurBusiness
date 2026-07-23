"""
Uploads an image file to Cloudinary and returns its permanent URL.
We never save uploaded files to the server's own disk - Docker containers
are disposable, so anything saved there would be lost on a rebuild.
"""
import cloudinary
import cloudinary.uploader
from fastapi import UploadFile, HTTPException

from app.core.config import settings

cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET,
)


def upload_image(file: UploadFile) -> str:
    """Returns the uploaded image's URL, or raises a clear error if it fails."""
    if not settings.CLOUDINARY_CLOUD_NAME:
        raise HTTPException(status_code=503, detail="Image upload is not configured yet")

    try:
        result = cloudinary.uploader.upload(file.file, folder="agency")
        return result["secure_url"]
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Image upload failed: {e}")
