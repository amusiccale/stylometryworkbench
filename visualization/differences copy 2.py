"""
visualization/differences.py
"""

import pandas as pd
import plotly.express as px


def create_difference_plot(
    differences,
    title="Feature Differences",
    normalization="raw",
):

    top_features = differences[:20]

    df = pd.DataFrame(
        top_features
    )

    df["raw_difference"] = (
        df["difference"]
    )

    if normalization == "minmax":

        max_abs = max(
            abs(x)
            for x in df["difference"]
        )

        if max_abs > 0:

            df["difference"] = (
                df["difference"]
                / max_abs
            )

    elif normalization == "log":

        import math

        transformed = []

        for value in df["difference"]:

            sign = (
                1
                if value >= 0
                else -1
            )

            transformed.append(
                sign
                *
                math.log1p(
                    abs(value)
                )
            )

        df["difference"] = transformed

    fig = px.bar(

        df,

        x="difference",

        y="feature",

        orientation="h",

        title=f"{title} ({normalization})",

        hover_data={
            "raw_difference": True,
            "difference": False,
        },
    )

    fig.update_layout(

        yaxis={
            "categoryorder":
            "total ascending"
        }
    )

    return fig
