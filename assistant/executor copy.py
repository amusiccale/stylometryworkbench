"""
assistant/executor.py
"""

from models.fingerprint import (
    load_fingerprint,
)

from analysis.similarity import (
    similarity_result,
)

from analysis.feature_differences import (
    calculate_feature_differences,
)

from models.author import (
    get_author,
)

def format_author_comparison(
    result
):

    sim = (
        result["result"]
        ["similarity"]
    )

    dist = (
        result["result"]
        ["distance"]
    )

    lines = []

    lines.append(
        "# Author Comparison"
    )

    lines.append("")

    lines.append(
        f"Similarity: "
        f"{sim:.4f}"
    )

    lines.append(
        f"Distance: "
        f"{dist:.4f}"
    )

    lines.append("")
    lines.append(
        "## Top Differences"
    )
    lines.append("")

    for idx, item in enumerate(
        result[
            "top_differences"
        ][:5],
        start=1,
    ):

        lines.append(
            f"{idx}. "
            f"{item['feature']} "
            f"({item['difference']:.4f})"
        )

    return "\n".join(
        lines
    )

def execute_intent(intent):

    #
    # Compare Authors
    #

    if intent["intent"] == "compare_authors":

        author_a = result["result"]["source_author"]
        author_b = result["result"]["target_author"]

        author_a_record = get_author(
            author_a
        )

        author_b_record = get_author(
            author_b
        )

        name_a = (
            author_a_record.display_name
            if author_a_record
            else str(author_a)
        )

        name_b = (
            author_b_record.display_name
            if author_b_record
            else str(author_b)
        )

        fp_a = load_fingerprint(
            author_a
        )

        fp_b = load_fingerprint(
            author_b
        )

        if fp_a is None:

            return {
                "error":
                f"Author {author_a} "
                f"has no fingerprint."
            }

        if fp_b is None:

            return {
                "error":
                f"Author {author_b} "
                f"has no fingerprint."
            }

        result = similarity_result(
            author_a,
            author_b,
            fp_a.vector,
            fp_b.vector,
            method="cosine",
        )

        differences = (
            calculate_feature_differences(
                fp_a.vector,
                fp_b.vector,
            )
        )

        return {

            "intent":
                "compare_authors",

            "result":
                result,

            "top_differences":
                differences[:10],
        }

    return {
        "error":
        f"Unsupported intent: "
        f"{intent['intent']}"
    }
