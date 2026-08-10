"""
visualization/heatmap.py

Similarity heatmap visualization.
"""

import plotly.graph_objects as go


def create_similarity_heatmap(
    similarity_matrix,
    author_names,
    title="Author Similarity Heatmap",
):
    """
    Create a similarity heatmap.

    Args:
        similarity_matrix:
            Square matrix of similarity values.

        author_names:
            Labels for rows and columns.
    """

    fig = go.Figure(
        data=go.Heatmap(
            z=similarity_matrix,
            x=author_names,
            y=author_names,
            colorscale="Viridis",
            zmin=0,
            zmax=1,
        )
    )

    fig.update_layout(
        title=title,
        xaxis_title="Author",
        yaxis_title="Author",
    )

    return fig
