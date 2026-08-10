"""
analysis/similarity.py

Feature vector comparison functions.
"""

import math
import statistics
from analysis.feature_filter import (
    filter_features,
)

def vector_to_lists(vec_a, vec_b):
    """
    Convert two feature dictionaries into
    aligned numeric lists.
    """

    common_keys = sorted(
        set(vec_a.keys()) &
        set(vec_b.keys())
    )

    values_a = [
        vec_a[key]
        for key in common_keys
    ]

    values_b = [
        vec_b[key]
        for key in common_keys
    ]

    return values_a, values_b


def cosine_similarity(vec_a, vec_b):
    """
    Cosine similarity.

    Returns:
        0.0 -> dissimilar
        1.0 -> identical direction
    """

    a, b = vector_to_lists(vec_a, vec_b)

    dot_product = sum(
        x * y
        for x, y in zip(a, b)
    )

    magnitude_a = math.sqrt(
        sum(x * x for x in a)
    )

    magnitude_b = math.sqrt(
        sum(y * y for y in b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (
        magnitude_a * magnitude_b
    )


def euclidean_distance(vec_a, vec_b):
    """
    Euclidean distance between vectors.
    """

    a, b = vector_to_lists(vec_a, vec_b)

    return math.sqrt(
        sum(
            (x - y) ** 2
            for x, y in zip(a, b)
        )
    )


def manhattan_distance(vec_a, vec_b):
    """
    Manhattan distance between vectors.
    """

    a, b = vector_to_lists(vec_a, vec_b)

    return sum(
        abs(x - y)
        for x, y in zip(a, b)
    )

def burrows_delta(vec_a, vec_b):
    """
    Classic Burrows Delta.

    Computes average absolute z-score distance
    between two feature vectors.

    Returns:
        Lower values indicate greater similarity.
    """

    a, b = vector_to_lists(vec_a, vec_b)

    deltas = []

    for x, y in zip(a, b):

        values = [x, y]

        mean = statistics.mean(values)

        stdev = statistics.pstdev(values)

        if stdev == 0:
            continue

        z_x = (x - mean) / stdev
        z_y = (y - mean) / stdev

        deltas.append(
            abs(z_x - z_y)
        )

    if not deltas:
        return 0.0

    return sum(deltas) / len(deltas)

def jensen_shannon_distance(vec_a, vec_b):
    """
    Jensen-Shannon Distance between two
    feature vectors.

    Returns:
        0.0 = identical distributions
        Higher values = more different
    """

    a, b = vector_to_lists(vec_a, vec_b)

    total_a = sum(abs(x) for x in a)
    total_b = sum(abs(x) for x in b)

    if total_a == 0 or total_b == 0:
        return 0.0

    p = [abs(x) / total_a for x in a]
    q = [abs(x) / total_b for x in b]

    m = [
        (pi + qi) / 2
        for pi, qi in zip(p, q)
    ]

    def kl_divergence(dist_a, dist_b):

        value = 0.0

        for a_i, b_i in zip(dist_a, dist_b):

            if a_i == 0:
                continue

            value += a_i * math.log2(
                a_i / b_i
            )

        return value

    js_divergence = (
        kl_divergence(p, m)
        + kl_divergence(q, m)
    ) / 2

    return math.sqrt(js_divergence)

def compare_vectors(
    vec_a,
    vec_b,
    method="cosine",
    selected_features=None,
):
    """
    Unified vector comparison API.

    Args:
        vec_a:
            First feature vector

        vec_b:
            Second feature vector

        method:
            Comparison algorithm

    Returns:
        Numeric comparison score
    """

    method = method.lower()

    vec_a = filter_features(
        vec_a,
        selected_features,
    )

    vec_b = filter_features(
        vec_b,
        selected_features,
    )   

    if method == "cosine":
        return cosine_similarity(
            vec_a,
            vec_b,
        )

    elif method == "euclidean":
        return euclidean_distance(
            vec_a,
            vec_b,
        )

    elif method == "manhattan":
        return manhattan_distance(
            vec_a,
            vec_b,
        )

    elif method == "burrows_delta":
        return burrows_delta(
            vec_a,
            vec_b,
        )

    elif method == "jensen_shannon":
        return jensen_shannon_distance(
            vec_a,
            vec_b,
        )

    raise ValueError(
        f"Unsupported comparison method: {method}"
    )

def similarity_result(
    source_author,
    target_author,
    vec_a,
    vec_b,
    method="cosine",
    selected_features=None,
):
    """
    Generate a standardized SimilarityResult.
    """

    score = compare_vectors(
        vec_a,
        vec_b,
        method,
        selected_features=selected_features,
    )

    if method == "cosine":

        similarity = score
        distance = 1.0 - score

    else:

        distance = score

        similarity = (
            1.0 / (1.0 + score)
        )

    return {
        "source_author": source_author,
        "target_author": target_author,
        "distance": distance,
        "similarity": similarity,
    }
