# coding: utf-8

"""
Abstract interface for rate-limit state storage.

Implementations must store per-client, per-window (second / day) counters
so that both PHP and Python applications can share rate-limit knowledge
through a common backend (e.g. a shared database).
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional


class RateLimitStoreInterface(ABC):
    """Storage backend for per-client rate-limit state.

    Each record is keyed by *(client_id, window)* where *window* is either
    ``"second"`` or ``"day"``.  The stored payload is a dict with at least:

    * ``remaining`` – number of requests still allowed in the window (int)
    * ``timestamp`` – UNIX epoch (seconds) when the value was observed (int)
    """

    @abstractmethod
    def get(self, client_id: str, window: str) -> Optional[Dict[str, int]]:
        """Return stored data for *client_id* and *window*, or ``None``."""
        ...

    @abstractmethod
    def set(self, client_id: str, window: str, remaining: int, timestamp: int) -> None:
        """Persist *remaining* count for *client_id* / *window* at *timestamp*."""
        ...

    @abstractmethod
    def all_for_client(self, client_id: str) -> List[Dict[str, int]]:
        """Return all stored records for *client_id* (for debugging)."""
        ...
