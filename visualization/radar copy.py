"""
visualization/radar.py

Author fingerprint radar chart.
"""

import plotly.graph_objects as go


RADAR_FEATURES = [
    "avg_word_length",
    "type_token_ratio",
    "mattr",
    "hapax_ratio",
    "sentence_length_mean",
    "paragraph_length_mean",
    "uppercase_ratio",
    "character_entropy",
]


def create_radar_chart(
    feature_vector,
    title="Author Fingerprint",
    normalization="raw",
):
    """
    Generate a Plotly radar chart from
    a feature vector.
    """

    from analysis.normalization import (
        minmax_normalize_vector,
        log_normalize_vector,
    )

    if normalization == "minmax":

        feature_vector = (
            minmax_normalize_vector(
                feature_vector
            )
        )

    elif normalization == "log":

        feature_vector = (
            log_normalize_vector(
                feature_vector
            )
        )

    labels = []
    values = []

    
    for feature_name in RADAR_FEATURES:

        if feature_name in feature_vector:

            labels.append(feature_name)

            values.append(
                feature_vector[feature_name]
            )

    if labels:

        labels.append(labels[0])
        values.append(values[0])

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=labels,
            fill="toself",
            name=title,
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
            )
        ),
        showlegend=False,
        title=title,
    )

    return fig
