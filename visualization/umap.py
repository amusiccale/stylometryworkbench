"""
visualization/umap.py

UMAP visualization.
"""

import plotly.express as px
import plotly.graph_objects as go


def create_umap_plot(
    coordinates,
    title="UMAP Author Space",
):
    """
    Create UMAP scatter plot.
    """

    if not coordinates:

        fig = go.Figure()

        fig.update_layout(
            title=(
                f"{title}<br>"
                "Not enough samples "
                "for UMAP projection"
            )
        )

        return fig

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
