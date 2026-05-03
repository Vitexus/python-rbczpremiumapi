# coding: utf-8

"""
Abstract SQL dialect interface for database-backed rate-limit stores.

Mirrors the PHP ``SqlDialect`` interface so that the same database can be
accessed from both PHP and Python with dialect-specific SQL generation.
"""

from abc import ABC, abstractmethod


class SqlDialect(ABC):
    """Provides dialect-specific helpers for SQL-backed rate-limit stores."""

    @abstractmethod
    def now(self) -> int:
        """Return the current UNIX timestamp (seconds)."""
        ...

    @abstractmethod
    def placeholder(self, name: str) -> str:
        """Return a parameter placeholder for the given *name*.

        Examples: ``:name`` (PDO/SQLite), ``%s`` (psycopg2), ``?`` (sqlite3).
        """
        ...
