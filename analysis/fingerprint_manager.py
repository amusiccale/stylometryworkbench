"""
analysis/fingerprint_manager.py

Fingerprint update workflow.
"""

from models.document import list_documents
from models.fingerprint import save_fingerprint

from analysis.vectorizer import (
    generate_fingerprint_profile,
)


def update_author_fingerprint(author_id):
    """
    Rebuild an author's fingerprint from
    all currently stored documents.
    """

    documents = list_documents(
        author_id=author_id
    )

    document_texts = [
        document.text
        for document in documents
    ]

    profile = generate_fingerprint_profile(
        author_id=author_id,
        documents=document_texts,
    )

    save_fingerprint(
        author_id=profile["author_id"],
        vector=profile["vector"],
        doc_count=profile["doc_count"],
        total_words=profile["total_words"],
    )

    return profile
