# coding: utf-8

"""
JSON file–backed rate-limit store.

Uses the same JSON structure as the PHP ``JsonRateLimitStore`` so that
PHP and Python applications sharing the same file will cooperatively
respect API rate limits.

JSON layout::

    {
        "<client_id>": {
            "second": {"remaining": 9, "timestamp": 1714780000},
            "day":    {"remaining": 4999, "timestamp": 1714780000}
        }
    }
"""

import fcntl
import json
import logging
import os
from typing import Any, Dict, List, Optional

from rbczpremiumapi.RateLimit.rate_limit_store_interface import RateLimitStoreInterface

logger = logging.getLogger(__name__)


class JsonRateLimitStore(RateLimitStoreInterface):
    """Rate-limit store persisted as a JSON file with advisory file locking.

    :param filename: path to the JSON file (created on first write if missing)
    """

    def __init__(self, filename: str) -> None:
        self._filename = filename
        self._data: Dict[str, Any] = {}
        if os.path.exists(filename):
            self._load()

    # -- public interface ----------------------------------------------------

    def get(self, client_id: str, window: str) -> Optional[Dict[str, int]]:
        return self._data.get(client_id, {}).get(window)

    def set(self, client_id: str, window: str, remaining: int, timestamp: int) -> None:
        self._data.setdefault(client_id, {})[window] = {
            "remaining": remaining,
            "timestamp": timestamp,
        }
        self._save()

    def all_for_client(self, client_id: str) -> List[Dict[str, int]]:
        return self._data.get(client_id, {})

    # -- private helpers -----------------------------------------------------

    def _load(self) -> None:
        try:
            with open(self._filename, "r+b") as fh:
                fcntl.flock(fh, fcntl.LOCK_SH)
                try:
                    raw = fh.read()
                    if raw:
                        self._data = json.loads(raw)
                    else:
                        self._data = {}
                except (json.JSONDecodeError, ValueError) as exc:
                    logger.error("Failed to decode rate limit JSON: %s", exc)
                    self._data = {}
                finally:
                    fcntl.flock(fh, fcntl.LOCK_UN)
        except OSError as exc:
            logger.error("Failed to read rate limit store from %s: %s", self._filename, exc)
            self._data = {}

    def _save(self) -> None:
        try:
            with open(self._filename, "wb") as fh:
                fcntl.flock(fh, fcntl.LOCK_EX)
                try:
                    fh.write(json.dumps(self._data, indent=4).encode("utf-8"))
                    fh.flush()
                finally:
                    fcntl.flock(fh, fcntl.LOCK_UN)
        except OSError as exc:
            logger.error("Failed to write rate limit store to %s: %s", self._filename, exc)
