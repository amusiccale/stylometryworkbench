"""
analysis/normalization.py
"""

import math


def minmax_normalize_vector(vector):

    values = list(vector.values())

    if not values:
        return dict(vector)

    min_value = min(values)
    max_value = max(values)

    if min_value == max_value:

        return {
            key: 1.0
            for key in vector
        }

    return {

        key: (
            (value - min_value)
            /
            (max_value - min_value)
        )

        for key, value
        in vector.items()
    }


def log_normalize_vector(vector):

    result = {}

    for key, value in vector.items():

        if value <= 0:

            result[key] = 0.0

        else:

            result[key] = math.log1p(
                value
            )

    return result

def relative_scale_vector(vector):
    """
    Scale values to the range:

        0.0 -> 1.0

    relative to the maximum value.

    Display only.
    """

    if not vector:
        return {}

    max_value = max(
        abs(value)
        for value in vector.values()
    )

    if max_value == 0:
        return dict(vector)

    return {
        key: value / max_value
        for key, value
        in vector.items()
    }
