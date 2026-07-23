"""
Public demo endpoint - rate-limited since each message costs real money
via the Claude API.
"""
from fastapi import APIRouter, Request

from app.schemas.chatbot import ChatRequest, ChatResponse
from app.services.chatbot import get_chatbot_reply
from app.core.limiter import limiter

router = APIRouter(prefix="/api/chatbot", tags=["chatbot"])


@router.post("/message", response_model=ChatResponse)
@limiter.limit("5/minute")
def chat(request: Request, payload: ChatRequest):
    reply = get_chatbot_reply(payload.messages)
    return ChatResponse(reply=reply)
