"""
One shared limiter instance, used by any route that needs rate limiting.
Limits are tracked per visitor IP address.
"""
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
