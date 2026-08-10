"""
exports/csv_export.py
"""

import csv
from models.author import list_authors
from models.fingerprint import load_fingerprint
import json


def export_fingerprints_csv(
    output_path,
):
    rows = []

    for author in list_authors():

        fp = load_fingerprint(
            author.author_id
        )

        if fp is None:
            continue

        rows.append(
            {
                "author_id":
                    fp.author_id,

                "doc_count":
                    fp.doc_count,

                "total_words":
                    fp.total_words,

                "vector":
                    json.dumps(
                        fp.vector
                    ),
            }
        )

    export_csv(
        rows,
        output_path,
    )

def export_csv(
    records,
    output_path,
):
    """
    Generic CSV export.
    """

    if not records:
        return

    fieldnames = list(
        records[0].keys()
    )

    with open(
        output_path,
        "w",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
        )

        writer.writeheader()

        writer.writerows(records)

def export_attribution_csv(
    attribution_result,
    output_path,
):
    """
    Export attribution rankings to CSV.
    """

    rankings = attribution_result.get(
        "rankings",
        []
    )

    export_csv(
        rankings,
        output_path,
    )
