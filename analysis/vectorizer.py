"""
analysis/vectorizer.py

Author fingerprint aggregation.
"""

from analysis.features import extract_features


def aggregate_author_documents(documents):
    """
    Combine multiple document texts into a list
    of feature vectors.

    Args:
        documents:
            Iterable of document text strings.

    Returns:
        List of feature dictionaries.
    """

    return [
        extract_features(text)
        for text in documents
    ]


def build_author_vector(feature_vectors):
    """
    Aggregate document feature vectors into
    a single author fingerprint vector.

    Uses arithmetic mean for each feature.

    Args:
        feature_vectors:
            List of FeatureVector dictionaries.

    Returns:
        Author-level FeatureVector.
    """

    if not feature_vectors:
        return {}

    feature_names = feature_vectors[0].keys()

    author_vector = {}

    for feature_name in feature_names:

        values = [
            vector[feature_name]
            for vector in feature_vectors
        ]

        author_vector[feature_name] = (
            sum(values) / len(values)
        )

    return author_vector

from datetime import datetime


def generate_fingerprint_profile(
    author_id,
    documents,
):
    """
    Generate a complete fingerprint profile
    from an author's documents.

    Args:
        author_id:
            Numeric author identifier

        documents:
            Iterable of document texts

    Returns:
        FingerprintProfile-compatible dict
    """

    feature_vectors = aggregate_author_documents(
        documents
    )

    author_vector = build_author_vector(
        feature_vectors
    )

    total_words = sum(
        len(document.split())
        for document in documents
    )

    return {
        "author_id": author_id,
        "vector": author_vector,
        "doc_count": len(documents),
        "total_words": total_words,
        "last_updated": datetime.now().isoformat(),
    }
