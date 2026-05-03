# coding: utf-8

"""Tests for RateLimiter."""

import time
from unittest.mock import MagicMock

import pytest

from rbczpremiumapi.RateLimit.rate_limiter import RateLimiter
from rbczpremiumapi.RateLimit.rate_limit_exceeded_exception import RateLimitExceededException
from rbczpremiumapi.RateLimit.rate_limit_store_interface import RateLimitStoreInterface


def _make_store() -> MagicMock:
    return MagicMock(spec=RateLimitStoreInterface)


class TestRateLimiter:
    def test_is_wait_mode_default_true(self):
        limiter = RateLimiter(_make_store())
        assert limiter.is_wait_mode() is True

    def test_is_wait_mode_false(self):
        limiter = RateLimiter(_make_store(), wait_mode=False)
        assert limiter.is_wait_mode() is False

    def test_handle_rate_limits_calls_store_set(self):
        store = _make_store()
        limiter = RateLimiter(store)
        now = int(time.time())
        limiter.handle_rate_limits("client", 1, 2, now)
        assert store.set.call_count == 2
        store.set.assert_any_call("client", "second", 1, now)
        store.set.assert_any_call("client", "day", 2, now)

    def test_check_before_request_does_not_throw(self):
        store = _make_store()
        store.get.return_value = {"remaining": 1, "timestamp": int(time.time())}
        limiter = RateLimiter(store)
        limiter.check_before_request("client")  # should not raise

    def test_check_before_request_raises_when_day_exceeded_no_wait(self):
        store = _make_store()
        store.get.side_effect = lambda cid, window: {
            "second": {"remaining": 5, "timestamp": int(time.time())},
            "day": {"remaining": 0, "timestamp": int(time.time())},
        }[window]
        limiter = RateLimiter(store, wait_mode=False)
        with pytest.raises(RateLimitExceededException):
            limiter.check_before_request("client")
