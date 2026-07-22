# Agency Backend (FastAPI)

Step 1 scaffold: project foundation. This has been tested end-to-end
(health check, create lead, list leads all working).

## Folder structure

```
app/
  main.py              -> app entry point, run this
  core/config.py       -> centralized settings, reads from .env
  db/database.py       -> SQLAlchemy engine/session setup
  models/lead.py       -> SQLAlchemy table definition
  schemas/lead.py       -> Pydantic request/response validation
  api/routes/leads.py  -> the actual endpoints
requirements.txt
.env.example           -> copy to .env and fill in
```

## Setup

1. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and fill in your real values.
   - For quick local testing without installing Postgres, you can use:
     `DATABASE_URL=sqlite:///./test.db`
   - For real use, set up a free Postgres DB on Supabase or Neon and
     paste its connection string here instead.

4. Run the server:
   ```
   uvicorn app.main:app --reload
   ```

5. Open http://localhost:8000/docs — FastAPI auto-generates interactive
   API documentation where you can test every endpoint directly in the
   browser. This is one of the best things about FastAPI over Express/Django.

## What's included in this Step 1 scaffold

- Working `/health` endpoint
- Working `POST /api/leads/` — this is what your contact form will call
- Working `GET /api/leads/` — lists submitted leads (will be admin-only
  once auth is added)
- Auto-creates DB tables on startup (fine for early dev; switch to
  Alembic migrations once you have real data you can't afford to lose)
- CORS configured so your frontend (e.g. Next.js on localhost:3000) can
  call this API

## What's NOT in this scaffold yet (next steps)

- Step 2: More tables — services, portfolio, blog_posts, newsletter_subscribers
- Step 3: Authentication (JWT) to protect admin endpoints like GET /api/leads/
- Step 4/5: More public + admin routes for the other tables
- Step 6: Email notifications on new lead (Resend/SendGrid), file uploads,
  spam protection (rate limiting + captcha)
- Alembic migrations instead of `create_all`

Let me know when you're ready and we'll build the next piece.
