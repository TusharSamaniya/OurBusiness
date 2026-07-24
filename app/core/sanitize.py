"""
Strips dangerous HTML (scripts, event handlers, iframes, etc.) from any
text before it's saved to the database. Two levels:
- sanitize_rich_text: allows a safe subset of formatting tags (for content
  fields like blog posts, where basic formatting is expected)
- sanitize_plain_text: strips ALL html (for titles, summaries, etc. -
  these should never contain markup at all)
"""
import bleach

ALLOWED_TAGS = ["p", "br", "strong", "em", "ul", "ol", "li", "a", "h2", "h3", "blockquote", "code", "pre"]
ALLOWED_ATTRS = {"a": ["href", "title"]}


def sanitize_rich_text(text: str) -> str:
    return bleach.clean(text, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRS, strip=True)


def sanitize_plain_text(text: str) -> str:
    return bleach.clean(text, tags=[], attributes={}, strip=True)
