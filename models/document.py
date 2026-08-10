"""
models/document.py

Document CRUD operations.
"""

from dataclasses import dataclass
from datetime import datetime

from database.db import get_connection



@dataclass
class DocumentRecord:
    document_id: int
    author_id: int
    filename: str
    text: str
    word_count: int
    created_date: str


def create_document(
    author_id: int,
    filename: str,
    text: str,
) -> int:
    """
    Create a document record.

    Returns:
        Newly-created document ID.
    """

    word_count = len(text.split())

    conn = get_connection()

    try:
        cursor = conn.execute(
            """
            INSERT INTO documents (
                author_id,
                filename,
                text,
                word_count,
                date_added
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                author_id,
                filename,
                text,
                word_count,
                datetime.now().isoformat(),
            ),
        )

        conn.commit()

        document_id = cursor.lastrowid

        from analysis.fingerprint_manager import update_author_fingerprint

        update_author_fingerprint(author_id)

        return document_id

    finally:
        conn.close()


def get_document(document_id: int) -> DocumentRecord | None:
    """
    Retrieve a document by ID.
    """

    conn = get_connection()

    try:
        row = conn.execute(
            """
            SELECT *
            FROM documents
            WHERE document_id = ?
            """,
            (document_id,),
        ).fetchone()

        if row is None:
            return None

        return DocumentRecord(
            document_id=row["document_id"],
            author_id=row["author_id"],
            filename=row["filename"],
            text=row["text"],
            word_count=row["word_count"],
            created_date=row["date_added"],
        )

    finally:
        conn.close()


def list_documents(author_id: int | None = None) -> list[DocumentRecord]:
    """
    List all documents, or only documents
    belonging to  """

    conn = get_connection()

    try:
        if author_id is None:
            rows = conn.execute(
                """
                SELECT *
                FROM documents
                ORDER BY document_id
                """
            ).fetchall()
        else:
            rows = conn.execute(
                """
                SELECT *
                FROM documents
                WHERE author_id = ?
                ORDER BY document_id
                """,
                (author_id,),
            ).fetchall()

        return [
            DocumentRecord(
                document_id=row["document_id"],
                author_id=row["author_id"],
                filename=row["filename"],
                text=row["text"],
                word_count=row["word_count"],
                created_date=row["date_added"],
            )
            for row in rows
        ]

    finally:
        conn.close()
