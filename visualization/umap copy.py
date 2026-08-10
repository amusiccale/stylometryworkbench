"""
visualization/umap.py

UMAP visualization.
"""

import plotly.express as px


def create_umap_plot(
    coordinates,
    title="UMAP Author Space",
):
    """
    Create UMAP scatter plot.
    """

    fig = px.scatter(
        coordinates,
        x="x",
        y="y",
        text="label",
        title=title,
    )

    fig.update_traces(
        textposition="top center"
    )

    return fig
