"""
analysis/document_comparison.py

Document-level comparison helpers.
"""

from models.document import (
    get_document,
)

from analysis.features import (
    extract_features,
)


def build_document_vector(
    document_id,
):
    """
    Build a FeatureVector from a single
    document.
    """

    document = get_document(
        document_id
    )

    if document is None:

        raise ValueError(
            f"Document {document_id} "
            f"not found."
        )

    return extract_features(
        document.text
    )

from analysis.similarity import (
    similarity_result,
)


def compare_documents(
    document_a_id,
    document_b_id,
    method="cosine",
    selected_features=None,
):
    """
    Compare two individual documents.
    """

    vec_a = build_document_vector(
        document_a_id
    )

    vec_b = build_document_vector(
        document_b_id
    )

    return similarity_result(
        document_a_id,
        document_b_id,
        vec_a,
        vec_b,
        method=method,
        selected_features=
            selected_features,
    )
