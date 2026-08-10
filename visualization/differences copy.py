"""
visualization/differences.py
"""

import plotly.express as px
from analysis.normalization import (
    minmax_normalize_vector,
    log_normalize_vector,
)

def create_difference_plot(
    differences,
    title="Feature Differences",
    normalization="raw",
):
    """
    Create horizontal feature-difference plot.
    """

    top_features = differences[:20]

    fig = px.bar(
        top_features,
        x="difference",
        y="feature",
        orientation="h",
        title=title,
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"}
    )

    return fig
