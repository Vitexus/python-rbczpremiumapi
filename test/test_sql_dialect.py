# coding: utf-8

"""Tests for SqlDialect."""

import time
from unittest.mock import MagicMock

from rbczpremiumapi.RateLimit.sql_dialect import SqlDialect


class TestSqlDialect:
    def test_now_returns_int(self):
        mock = MagicMock(spec=SqlDialect)
        mock.now.return_value = int(time.time())
        assert isinstance(mock.now(), int)

    def test_placeholder_returns_string(self):
        mock = MagicMock(spec=SqlDialect)
        mock.placeholder.return_value = ":test"
        assert isinstance(mock.placeholder("test"), str)
