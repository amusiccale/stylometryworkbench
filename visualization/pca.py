"""
visualization/pca.py

PCA visualization.
"""

import plotly.express as px


def create_pca_plot(
    coordinates,
    title="PCA Author Space",
):
    """
    Create PCA scatter plot.
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
