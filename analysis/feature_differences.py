"""
analysis/feature_differences.py

Feature-level comparison helpers.
"""


def calculate_feature_differences(
    vec_a,
    vec_b,
    selected_features=None,
):
    """
    Calculate per-feature differences.

    Positive:
        Author A > Author B

    Negative:
        Author B > Author A
    """

    if selected_features:

        feature_names = selected_features

    else:

        feature_names = sorted(
            set(vec_a.keys()) |
            set(vec_b.keys())
        )

    results = []

    for feature in feature_names:

        value_a = vec_a.get(
            feature,
            0.0,
        )

        value_b = vec_b.get(
            feature,
            0.0,
        )

        results.append(
            {
                "feature": feature,
                "difference":
                    value_a - value_b,
            }
        )

    return sorted(
        results,
        key=lambda item:
            abs(item["difference"]),
        reverse=True,
    )
