# coding: utf-8

"""
Database-backed rate-limit store using Python DB-API 2.0 connections.

Uses the same ``rate_limits`` table schema as the PHP ``PdoRateLimitStore``
so that PHP and Python applications sharing the same database will
cooperatively respect API rate limits.

Table schema::

    CREATE TABLE IF NOT EXISTS rate_limits (
        client_id TEXT NOT NULL,
        window    TEXT NOT NULL,
        remaining INTEGER NOT NULL,
        timestamp INTEGER NOT NULL,
        PRIMARY KEY (client_id, window)
    )
"""

import sqlite3
from typing import Any, Dict, List, Optional, Union

from rbczpremiumapi.RateLimit.rate_limit_store_interface import RateLimitStoreInterface

# Accept any DB-API 2.0 connection object.  sqlite3.Connection is the most
# common one and the only one we type-hint explicitly, but any PEP 249
# compliant connection will work.
Connection = Union[sqlite3.Connection, Any]


class DbRateLimitStore(RateLimitStoreInterface):
    """Rate-limit store backed by a SQL database (DB-API 2.0).

    Compatible with ``sqlite3``, ``psycopg2``, ``mysql-connector-python``, etc.

    :param connection: an open DB-API 2.0 connection
    :param placeholder: parameter placeholder style (``"?"`` for sqlite3,
        ``"%s"`` for psycopg2 / mysql-connector, etc.)
    """

    def __init__(self, connection: Connection, placeholder: str = "?") -> None:
        self._conn = connection
        self._ph = placeholder
        self._init_table()

    # -- public interface ----------------------------------------------------

    def get(self, client_id: str, window: str) -> Optional[Dict[str, int]]:
        ph = self._ph
        cur = self._conn.cursor()
        cur.execute(
            f"SELECT remaining, timestamp FROM rate_limits"
            f" WHERE client_id = {ph} AND window = {ph}",
            (client_id, window),
        )
        row = cur.fetchone()
        if row is None:
            return None
        return {"remaining": int(row[0]), "timestamp": int(row[1])}

    def set(self, client_id: str, window: str, remaining: int, timestamp: int) -> None:
        ph = self._ph
        cur = self._conn.cursor()
        cur.execute(
            f"REPLACE INTO rate_limits (client_id, window, remaining, timestamp)"
            f" VALUES ({ph}, {ph}, {ph}, {ph})",
            (client_id, window, remaining, timestamp),
        )
        self._conn.commit()

    def all_for_client(self, client_id: str) -> Dict[str, Dict[str, int]]:
        ph = self._ph
        cur = self._conn.cursor()
        cur.execute(
            f"SELECT window, remaining, timestamp FROM rate_limits"
            f" WHERE client_id = {ph}",
            (client_id,),
        )
        results: Dict[str, Dict[str, int]] = {}
        for row in cur.fetchall():
            results[row[0]] = {"remaining": int(row[1]), "timestamp": int(row[2])}
        return results

    # -- private helpers -----------------------------------------------------

    def _init_table(self) -> None:
        cur = self._conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS rate_limits ("
            "  client_id TEXT NOT NULL,"
            "  window TEXT NOT NULL,"
            "  remaining INTEGER NOT NULL,"
            "  timestamp INTEGER NOT NULL,"
            "  PRIMARY KEY (client_id, window)"
            ")"
        )
        self._conn.commit()
