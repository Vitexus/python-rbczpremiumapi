# coding: utf-8

"""Tests for JsonRateLimitStore."""

import json
import os
import tempfile

import pytest

from rbczpremiumapi.RateLimit.json_rate_limit_store import JsonRateLimitStore


class TestJsonRateLimitStore:
    def _tmpfile(self, tmp_path):
        return str(tmp_path / "rate_limits.json")

    def test_get_returns_none_when_empty(self, tmp_path):
        store = JsonRateLimitStore(self._tmpfile(tmp_path))
        assert store.get("client", "second") is None

    def test_set_and_get(self, tmp_path):
        path = self._tmpfile(tmp_path)
        store = JsonRateLimitStore(path)
        store.set("client", "second", 9, 1000)
        result = store.get("client", "second")
        assert result == {"remaining": 9, "timestamp": 1000}

    def test_persistence_across_instances(self, tmp_path):
        path = self._tmpfile(tmp_path)
        store1 = JsonRateLimitStore(path)
        store1.set("client", "day", 4999, 2000)

        store2 = JsonRateLimitStore(path)
        result = store2.get("client", "day")
        assert result == {"remaining": 4999, "timestamp": 2000}

    def test_all_for_client(self, tmp_path):
        path = self._tmpfile(tmp_path)
        store = JsonRateLimitStore(path)
        store.set("client", "second", 9, 1000)
        store.set("client", "day", 4999, 1000)
        data = store.all_for_client("client")
        assert "second" in data
        assert "day" in data

    def test_all_for_client_empty(self, tmp_path):
        store = JsonRateLimitStore(self._tmpfile(tmp_path))
        assert store.all_for_client("nonexistent") == {}

    def test_json_file_format_compatible_with_php(self, tmp_path):
        """Verify the JSON file uses the same structure as the PHP JsonRateLimitStore."""
        path = self._tmpfile(tmp_path)
        store = JsonRateLimitStore(path)
        store.set("abc123", "second", 8, 1714780000)
        store.set("abc123", "day", 4998, 1714780000)

        with open(path) as f:
            data = json.load(f)

        assert data == {
            "abc123": {
                "second": {"remaining": 8, "timestamp": 1714780000},
                "day": {"remaining": 4998, "timestamp": 1714780000},
            }
        }

    def test_loads_php_written_json(self, tmp_path):
        """Verify Python can read a JSON file written by the PHP implementation."""
        path = self._tmpfile(tmp_path)
        php_data = {
            "client1": {
                "second": {"remaining": 5, "timestamp": 1714780000},
                "day": {"remaining": 3000, "timestamp": 1714780000},
            }
        }
        with open(path, "w") as f:
            json.dump(php_data, f, indent=4)

        store = JsonRateLimitStore(path)
        assert store.get("client1", "second") == {"remaining": 5, "timestamp": 1714780000}
        assert store.get("client1", "day") == {"remaining": 3000, "timestamp": 1714780000}
