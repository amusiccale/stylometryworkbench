"""
models/author.py

Author CRUD operations.
"""

from dataclasses import dataclass
from datetime import datetime

from database.db import get_connection


@dataclass
class AuthorRecord:
    author_id: int
    display_name: str
    created_date: str
    notes: str


def create_author(author_id: int,
                  display_name: str = "",
                  notes: str = "") -> None:

    conn = get_connection()

    try:
        conn.execute(
            """
            INSERT INTO authors (
                author_id,
                display_name,
                created_date,
                notes
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                author_id,
                display_name,
                datetime.now().isoformat(),
                notes,
            ),
        )

        conn.commit()

    finally:
        conn.close()


def get_author(author_id: int) -> AuthorRecord | None:

    conn = get_connection()

    try:
        row = conn.execute(
            """
            SELECT *
            FROM authors
            WHERE author_id = ?
            """,
            (author_id,),
        ).fetchone()

        if row is None:
            return None

        return AuthorRecord(
            author_id=row["author_id"],
            display_name=row["display_name"],
            created_date=row["created_date"],
            notes=row["notes"],
        )

    finally:
        conn.close()


def update_author(author_id: int,
                  display_name: str,
                  notes: str) -> bool:

    conn = get_connection()

    try:
        cursor = conn.execute(
            """
            UPDATE authors
            SET display_name = ?,
                notes = ?
            WHERE author_id = ?
            """,
            (
                display_name,
                notes,
                author_id,
            ),
        )

        conn.commit()

        return cursor.rowcount > 0

    finally:
        conn.close()


def delete_author(author_id: int) -> bool:

    conn = get_connection()

    try:
        cursor = conn.execute(
            """
            DELETE FROM authors
            WHERE author_id = ?
            """,
            (author_id,),
        )

        conn.commit()

        return cursor.rowcount > 0

    finally:
        conn.close()


def list_authors() -> list[AuthorRecord]:

    conn = get_connection()

    try:
        rows = conn.execute(
            """
            SELECT *
            FROM authors
            ORDER BY author_id
            """
        ).fetchall()

        return [
            AuthorRecord(
                author_id=row["author_id"],
                display_name=row["display_name"],
                created_date=row["created_date"],
                notes=row["notes"],
            )
            for row in rows
        ]

    finally:
        conn.close()
