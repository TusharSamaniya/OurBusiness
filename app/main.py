"""
App entry point. Run with: uvicorn app.main:app --reload
Then visit http://localhost:8000/docs for the auto-generated interactive API docs.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes import leads, services, portfolio, blog, newsletter, auth, upload

# Table creation is now handled by Alembic migrations (see alembic/ folder
# and README) instead of Base.metadata.create_all(). Run `alembic upgrade
# head` after pulling new model changes.

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(leads.router)
app.include_router(services.router)
app.include_router(portfolio.router)
app.include_router(blog.router)
app.include_router(newsletter.router)
app.include_router(auth.router)
app.include_router(upload.router)


@app.get("/health")
def health_check():
    """Simple endpoint to confirm the server + DB config are up."""
    return {"status": "ok", "environment": settings.ENVIRONMENT}
