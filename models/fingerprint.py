"""
models/fingerprint.py

Fingerprint storage and retrieval.
"""

from dataclasses import dataclass
from datetime import datetime
import json

from database.db import get_connection


@dataclass
class FingerprintProfile:
    author_id: int
    vector: dict
    doc_count: int
    total_words: int
    last_updated: str


def save_fingerprint(
    author_id: int,
    vector: dict,
    doc_count: int,
    total_words: int,
) -> None:
    """
    Create or update an author's fingerprint.
    """

    conn = get_connection()

    try:
        conn.execute(
            """
            INSERT OR REPLACE INTO fingerprints (
                author_id,
                feature_json,
                total_words,
                total_docs,
                updated
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                author_id,
                json.dumps(vector),
                total_words,
                doc_count,
                datetime.now().isoformat(),
            ),
        )

        conn.commit()

    finally:
        conn.close()


def load_fingerprint(author_id: int) -> FingerprintProfile | None:
    """
    Load an author's fingerprint.
    """

    conn = get_connection()

    try:
        row = conn.execute(
            """
            SELECT *
            FROM fingerprints
            WHERE author_id = ?
            """,
            (author_id,),
        ).fetchone()

        if row is None:
            return None

        return FingerprintProfile(
            author_id=row["author_id"],
            vector=json.loads(row["feature_json"]),
            doc_count=row["total_docs"],
            total_words=row["total_words"],
            last_updated=row["updated"],
        )

    finally:
        conn.close()
