"""
Sends the conversation to Claude and returns its reply. This is a sales
demo - it shows visitors what a custom AI bot for their own business
could look like.
"""
import anthropic
from fastapi import HTTPException

from app.core.config import settings
from app.schemas.chatbot import ChatMessage

SYSTEM_PROMPT = (
    "You are a friendly AI assistant demo on an agency's website. The agency "
    "builds websites, apps, and custom AI bots for businesses. Answer questions "
    "helpfully and briefly (2-3 sentences). If relevant, mention that a custom "
    "version of a bot like this can be built for the visitor's own business."
)


def get_chatbot_reply(messages: list[ChatMessage]) -> str:
    if not settings.ANTHROPIC_API_KEY:
        raise HTTPException(status_code=503, detail="Chatbot is not configured yet")

    client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    try:
        response = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=300,
            system=SYSTEM_PROMPT,
            messages=[{"role": m.role, "content": m.content} for m in messages],
        )
        return response.content[0].text
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Chatbot request failed: {e}")
