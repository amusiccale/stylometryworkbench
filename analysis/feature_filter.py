"""
analysis/feature_filter.py

Feature selection helpers.
"""


def filter_features(
    vector,
    selected_features,
):
    """
    Return a vector containing only the
    requested features.
    """

    if not selected_features:
        return dict(vector)

    return {
        key: value
        for key, value in vector.items()
        if key in selected_features
    }
