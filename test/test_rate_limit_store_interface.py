# coding: utf-8

"""Tests for RateLimitStoreInterface."""

from unittest.mock import MagicMock

from rbczpremiumapi.RateLimit.rate_limit_store_interface import RateLimitStoreInterface


class TestRateLimitStoreInterface:
    def test_get_returns_none_by_default(self):
        mock = MagicMock(spec=RateLimitStoreInterface)
        mock.get.return_value = None
        result = mock.get("client", "second")
        assert result is None

    def test_get_returns_dict(self):
        mock = MagicMock(spec=RateLimitStoreInterface)
        mock.get.return_value = {"remaining": 10, "timestamp": 1000}
        result = mock.get("client", "second")
        assert isinstance(result, dict)
        assert result["remaining"] == 10

    def test_set_does_not_throw(self):
        mock = MagicMock(spec=RateLimitStoreInterface)
        mock.set("client", "second", 10, 1000)
        mock.set.assert_called_once_with("client", "second", 10, 1000)

    def test_all_for_client_returns_list(self):
        mock = MagicMock(spec=RateLimitStoreInterface)
        mock.all_for_client.return_value = []
        result = mock.all_for_client("client")
        assert isinstance(result, list)
