# coding: utf-8

"""Tests for DbRateLimitStore."""

import sqlite3

import pytest

from rbczpremiumapi.RateLimit.db_rate_limit_store import DbRateLimitStore


def _make_store() -> DbRateLimitStore:
    conn = sqlite3.connect(":memory:")
    return DbRateLimitStore(conn)


class TestDbRateLimitStore:
    def test_get_returns_none_when_empty(self):
        store = _make_store()
        assert store.get("client", "second") is None

    def test_set_and_get(self):
        store = _make_store()
        store.set("client", "second", 9, 1000)
        result = store.get("client", "second")
        assert result == {"remaining": 9, "timestamp": 1000}

    def test_set_overwrites(self):
        store = _make_store()
        store.set("client", "second", 9, 1000)
        store.set("client", "second", 5, 2000)
        result = store.get("client", "second")
        assert result == {"remaining": 5, "timestamp": 2000}

    def test_all_for_client(self):
        store = _make_store()
        store.set("client", "second", 9, 1000)
        store.set("client", "day", 4999, 1000)
        data = store.all_for_client("client")
        assert "second" in data
        assert "day" in data
        assert data["second"] == {"remaining": 9, "timestamp": 1000}

    def test_all_for_client_empty(self):
        store = _make_store()
        assert store.all_for_client("nonexistent") == {}

    def test_table_schema_compatible_with_php(self):
        """Verify the table schema matches the PHP PdoRateLimitStore."""
        conn = sqlite3.connect(":memory:")
        store = DbRateLimitStore(conn)

        cur = conn.cursor()
        cur.execute("PRAGMA table_info(rate_limits)")
        columns = {row[1]: row[2] for row in cur.fetchall()}

        assert "client_id" in columns
        assert "window" in columns
        assert "remaining" in columns
        assert "timestamp" in columns

    def test_multiple_clients(self):
        store = _make_store()
        store.set("client1", "second", 9, 1000)
        store.set("client2", "second", 7, 2000)
        assert store.get("client1", "second")["remaining"] == 9
        assert store.get("client2", "second")["remaining"] == 7
        assert store.all_for_client("client1") != store.all_for_client("client2")
