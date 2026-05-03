# coding: utf-8

"""
Exception raised when a rate limit is exceeded and wait mode is disabled.
"""


class RateLimitExceededException(Exception):
    """Raised when a rate limit is exceeded and the limiter is not in wait mode."""
