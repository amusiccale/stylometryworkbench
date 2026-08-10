"""
analysis/clustering.py

Dimensionality reduction helpers.
"""

from sklearn.decomposition import PCA
import umap

def generate_pca_coordinates(
    feature_vectors,
    labels,
):
    """
    Generate 2D PCA coordinates.

    Args:
        feature_vectors:
            List of FeatureVector dictionaries

        labels:
            Corresponding author labels

    Returns:
        List of coordinate dictionaries
    """

    if len(feature_vectors) < 2:
        return []

    feature_names = sorted(
        set().union(
            *[
                vector.keys()
                for vector in feature_vectors
            ]
        )
    )

    matrix = [
        [
            vector.get(name, 0.0)
            for name in feature_names
        ]
        for vector in feature_vectors
    ]

    pca = PCA(n_components=2)

    coords = pca.fit_transform(matrix)

    results = []

    for label, point in zip(
        labels,
        coords,
    ):

        results.append(
            {
                "label": label,
                "x": float(point[0]),
                "y": float(point[1]),
            }
        )

    return results

def generate_umap_coordinates(
    feature_vectors,
    labels,
):
    """
    Generate 2D UMAP coordinates.

    Returns:
        List of coordinate dictionaries.
    """

    sample_count = len(feature_vectors)

    if sample_count < 3:
        return []

    feature_names = sorted(
        set().union(
            *[
                vector.keys()
                for vector in feature_vectors
            ]
        )
    )

    matrix = [
        [
            vector.get(name, 0.0)
            for name in feature_names
        ]
        for vector in feature_vectors
    ]

    # UMAP needs neighbor count smaller
    # than dataset size.

    n_neighbors = min(
        15,
        max(2, sample_count - 1)
    )

    try:

        reducer = umap.UMAP(
            n_components=2,
            n_neighbors=n_neighbors,
            random_state=42,
        )

        coords = reducer.fit_transform(
            matrix
        )

    except Exception:

        # Tiny datasets can still
        # cause failures in UMAP's
        # spectral initialization.

        return []

    results = []

    for label, point in zip(
        labels,
        coords,
    ):

        results.append(
            {
                "label": label,
                "x": float(point[0]),
                "y": float(point[1]),
            }
        )

    return results
