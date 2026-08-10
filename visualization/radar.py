"""
visualization/radar.py

Author fingerprint radar chart.
"""

import plotly.graph_objects as go

from analysis.normalization import (
    log_normalize_vector,
)
from analysis.normalization import (
    log_normalize_vector,
    relative_scale_vector,
)

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
    Display-only scaling.

    Raw values remain untouched.
    """

    plot_features = {}

    for feature_name in RADAR_FEATURES:

        if feature_name in feature_vector:

            plot_features[
                feature_name
            ] = feature_vector[
                feature_name
            ]

    raw_features = dict(
        plot_features
    )

    if normalization == "log":

        plot_features = (
            log_normalize_vector(
                plot_features
            )
        )

    elif normalization == "relative":

        plot_features = (
            relative_scale_vector(
                plot_features
            )
        )

    elif normalization == "log_relative":

        plot_features = (
            log_normalize_vector(
                plot_features
            )
        )

        plot_features = (
            relative_scale_vector(
                plot_features
            )
        )

    labels = list(
        plot_features.keys()
    )

    values = [
        plot_features[name]
        for name in labels
    ]

    raw_values = [
        raw_features[name]
        for name in labels
    ]

    if labels:

        labels.append(
            labels[0]
        )

        values.append(
            values[0]
        )

        raw_values.append(
            raw_values[0]
        )

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=labels,
            fill="toself",
            name=title,
            customdata=raw_values,
            hovertemplate=
                "<b>%{theta}</b><br>"
                "Displayed: %{r:.4f}<br>"
                "Raw: %{customdata:.4f}"
                "<extra></extra>",
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
            )
        ),
        showlegend=False,
        title=f"{title} ({normalization})",
    )

    return fig
