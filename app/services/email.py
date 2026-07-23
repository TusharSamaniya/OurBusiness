"""
Sends you an email the moment a new lead comes in. This is "best effort" -
if the email fails to send for any reason, we just log it and move on.
The lead is already saved in the database by the time this runs, so a
broken email service should never cause a lead to be lost.
"""
import html

import resend

from app.core.config import settings
from app.models.lead import Lead

resend.api_key = settings.RESEND_API_KEY


def send_lead_notification(lead: Lead) -> None:
    if not settings.RESEND_API_KEY or not settings.EMAIL_TO:
        print("Email not configured (missing RESEND_API_KEY or EMAIL_TO) - skipping notification")
        return

    try:
        resend.Emails.send({
            "from": settings.EMAIL_FROM,
            "to": settings.EMAIL_TO,
            "subject": f"New lead: {html.escape(lead.name)}",
            "html": f"""
                <p><strong>Name:</strong> {html.escape(lead.name)}</p>
                <p><strong>Email:</strong> {html.escape(lead.email)}</p>
                <p><strong>Phone:</strong> {html.escape(lead.phone or '-')}</p>
                <p><strong>Service interested:</strong> {html.escape(lead.service_interested or '-')}</p>
                <p><strong>Message:</strong> {html.escape(lead.message)}</p>
            """,
        })
    except Exception as e:
        # Never let an email failure break lead creation - just log it.
        print(f"Failed to send lead notification email: {e}")