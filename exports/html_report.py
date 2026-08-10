"""
exports/html_report.py
"""

from pathlib import Path


def export_html_report(
    attribution_result,
    output_path,
):
    """
    Create a simple HTML report.
    """

    predicted_author = (
        attribution_result.get(
            "predicted_author",
            "Unknown",
        )
    )

    confidence = (
        attribution_result.get(
            "confidence",
            0,
        )
    )

    rankings = (
        attribution_result.get(
            "rankings",
            []
        )
    )

    rows = []

    for rank in rankings:

        rows.append(
            f"""
            <tr>
                <td>{rank['author_id']}</td>
                <td>{rank['display_name']}</td>
                <td>{rank['score']:.4f}</td>
            </tr>
            """
        )

    html = f"""
    <html>
    <head>
        <title>
            Stylometric Attribution Report
        </title>
    </head>

    <body>

        <h1>
            Stylometric Attribution Report
        </h1>

        <h2>
            Prediction
        </h2>

        <p>
            Predicted Author:
            <strong>{predicted_author}</strong>
        </p>

        <p>
            Confidence:
            <strong>{confidence}%</strong>
        </p>

        <h2>
            Rankings
        </h2>

        <table border="1">

            <tr>
                <th>Author ID</th>
                <th>Name</th>
                <th>Score</th>
            </tr>

            {''.join(rows)}

        </table>

    </body>
    </html>
    """

    Path(output_path).write_text(
        html,
        encoding="utf-8",
    )
