"""
analysis/attribution.py

Unknown sample attribution.
"""

from analysis.features import extract_features
from models.author import list_authors
from models.fingerprint import load_fingerprint

from analysis.similarity import compare_vectors

##def attribute_text(sample_text):
##    """
##    Extract features from an unknown sample.
##
##    P6-01 implementation.
##
##    Returns a structure that will later
##    be expanded by P6-02 through P6-05.
##    """
##
##    feature_vector = extract_features(
##        sample_text
##    )
##
##    comparisons = compare_against_authors(
##        feature_vector,
##    )
##
##    return {
##        "sample_features":
##            feature_vector,
##
##        "comparisons":
##            comparisons,
##    }

def attribute_text(
    sample_text,
    method="cosine",
    selected_features=None,
):
    """
    Full MVP attribution workflow.
    """

    feature_vector = extract_features(
        sample_text
    )

    comparisons = compare_against_authors(
        feature_vector,
        method,
        selected_features,
    )

    rankings = rank_candidates(
        comparisons,
        method,
    )

    if not rankings:

        return {
            "sample_id": "unknown",
            "predicted_author": None,
            "confidence": 0.0,
            "rankings": [],
        }

    confidence = compute_confidence(
        rankings,
        method,
    )

    return {
        "sample_id": "unknown",
        "predicted_author":
            rankings[0]["author_id"],

        "confidence":
            confidence,

        "rankings":
            rankings,
    }

def compare_against_authors(
    sample_vector,
    method="cosine",
    selected_features=None,
):
    """
    Compare a sample feature vector
    against all known author fingerprints.

    Returns:
        List of comparison results.
    """

    results = []

    authors = list_authors()

    for author in authors:

        fingerprint = load_fingerprint(
            author.author_id
        )

        if fingerprint is None:
            continue

        score = compare_vectors(
        sample_vector,
        fingerprint.vector,
        method,
        selected_features=selected_features,
    )

        results.append(
            {
                "author_id":
                    author.author_id,

                "display_name":
                    author.display_name,

                "score":
                    score,
            }
        )

    return results

def rank_candidates(
    comparisons,
    method="cosine",
):
    """
    Sort attribution candidates from
    best to worst match.
    """

    if method == "cosine":

        return sorted(
            comparisons,
            key=lambda x: x["score"],
            reverse=True,
        )

    return sorted(
        comparisons,
        key=lambda x: x["score"],
    )

def compute_confidence(
    rankings,
    method="cosine",
):
    """
    Convert ranking separation
    into a confidence percentage.
    """

    if len(rankings) < 2:
        return 100.0

    best = rankings[0]["score"]
    second = rankings[1]["score"]

    if method == "cosine":

        gap = max(0.0, best - second)

        confidence = min(
            100.0,
            gap * 1000.0,
        )

    else:

        if best == 0:
            return 100.0

        gap = max(
            0.0,
            second - best,
        )

        confidence = min(
            100.0,
            (gap / best) * 100.0,
        )

    return round(
        confidence,
        2,
    )
