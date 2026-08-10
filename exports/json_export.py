"""
exports/json_export.py
"""

import json
from models.author import list_authors
from models.fingerprint import load_fingerprint


def export_fingerprints_json(
    output_path,
):
    data = []

    for author in list_authors():

        fp = load_fingerprint(
            author.author_id
        )

        if fp is None:
            continue

        data.append(
            {
                "author_id":
                    fp.author_id,
                "vector":
                    fp.vector,
                "doc_count":
                    fp.doc_count,
                "total_words":
                    fp.total_words,
            }
        )

    export_json(
        data,
        output_path,
    )

def export_json(
    data,
    output_path,
):
    """
    Generic JSON export.
    """

    with open(
        output_path,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            indent=2,
            ensure_ascii=False,
        )

def export_attribution_json(
    attribution_result,
    output_path,
):
    """
    Export AttributionResult to JSON.
    """

    export_json(
        attribution_result,
        output_path,
    )
