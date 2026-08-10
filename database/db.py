"""
database/db.py

SQLite connection management for the
Stylometric Fingerprint Workbench.
"""

import sqlite3

from config import DATABASE_PATH
from database.schema import create_schema


def get_connection() -> sqlite3.Connection:
    """
    Return a SQLite connection.
    """
    conn = sqlite3.connect(DATABASE_PATH)

    # Enable named column access
    conn.row_factory = sqlite3.Row

    # Enable foreign key constraints
    conn.execute("PRAGMA foreign_keys = ON")

    return conn


def initialize_database() -> None:
    """
    Create database schema if it does not exist.
    """
    conn = get_connection()

    try:
        create_schema(conn)
    finally:
        conn.close()
