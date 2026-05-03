# coding: utf-8

"""
Rate limiter that enforces per-second and per-day request limits.

The logic mirrors the PHP ``RateLimiter`` class so that both PHP and Python
applications sharing the same ``RateLimitStoreInterface`` backend will
cooperatively respect the API rate limits.
"""

import logging
import time

from rbczpremiumapi.RateLimit.rate_limit_exceeded_exception import RateLimitExceededException
from rbczpremiumapi.RateLimit.rate_limit_store_interface import RateLimitStoreInterface

logger = logging.getLogger(__name__)


class RateLimiter:
    """Enforces per-client rate limits using a pluggable storage backend.

    :param store: storage backend for per-client rate-limit state
    :param wait_mode: if ``True`` the limiter sleeps until the window resets;
        if ``False`` it raises :class:`RateLimitExceededException`
    """

    def __init__(self, store: RateLimitStoreInterface, wait_mode: bool = True) -> None:
        self._store = store
        self._wait_mode = wait_mode

    def is_wait_mode(self) -> bool:
        """Return ``True`` if the limiter is configured to wait on exhaustion."""
        return self._wait_mode

    def handle_rate_limits(
        self,
        client_id: str,
        remaining_second: int,
        remaining_day: int,
        timestamp: int,
    ) -> None:
        """Store remaining rate-limit counts for both windows.

        :param client_id: fingerprint identifying the client
            (e.g. certificate SHA-1, serial + issuer)
        :param remaining_second: remaining requests in the 1-second window
        :param remaining_day: remaining requests in the 24-hour window
        :param timestamp: UNIX timestamp when the limits were observed
        """
        self._store.set(client_id, "second", remaining_second, timestamp)
        self._store.set(client_id, "day", remaining_day, timestamp)

    def check_before_request(self, client_id: str) -> None:
        """Ensure the client is allowed to make the next request.

        For the **second** window the limiter always waits (it is at most 1 s).
        For the **day** window behaviour depends on *wait_mode*: sleep or raise.

        :param client_id: identifier of the client whose limits are checked
        :raises RateLimitExceededException: if a day limit is exceeded and
            wait mode is disabled
        """
        now = int(time.time())

        second = self._store.get(client_id, "second")
        day = self._store.get(client_id, "day")

        # second window
        if second and second["remaining"] <= 0:
            wait = max(0, 1 - (now - second["timestamp"]))
            if wait > 0:
                logger.warning(
                    "Rate-limit (second window) exceeded. Waiting %d seconds", wait
                )
                time.sleep(wait)

        # day window
        if day and day["remaining"] <= 0:
            wait = max(0, 86400 - (now - day["timestamp"]))
            if wait > 0:
                if self._wait_mode:
                    logger.warning(
                        "Rate-limit (day window) exceeded. Waiting %d seconds", wait
                    )
                    time.sleep(wait)
                else:
                    raise RateLimitExceededException(
                        "Rate-limit (day window) exceeded"
                    )
