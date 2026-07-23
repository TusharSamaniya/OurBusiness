from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str  # "user" or "assistant"
    content: str


class ChatRequest(BaseModel):
    messages: list[ChatMessage]  # full conversation so far, sent by the frontend each time


class ChatResponse(BaseModel):
    reply: str
