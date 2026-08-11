"""
assistant/executor.py
"""

from models.fingerprint import (
    load_fingerprint,
)

from models.author import (
    get_author,
)

from analysis.similarity import (
    similarity_result,
)

from analysis.feature_differences import (
    calculate_feature_differences,
)

from analysis.document_comparison import (
    compare_documents,
    build_document_vector,
)

from models.document import (
    get_document,
)

from models.author import (
    list_authors,
)

from models.document import (
    list_documents,
)

def format_author_list(
    result
):

    lines = [
        "# Available Authors",
        "",
    ]

    for author in result["authors"]:

        lines.append(
            f"{author['id']} - {author['name']}"
        )

    return "\n".join(lines)


def format_document_list(
    result
):

    lines = [
        "# Available Documents",
        "",
    ]

    for document in result["documents"]:

        lines.append(
            f"{document['id']} - {document['filename']}"
        )

    return "\n".join(lines)

def format_author_comparison(
    result
):
    """
    Convert structured comparison data
    into user-friendly markdown.
    """

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
        f"**Author A:** "
        f"{result['author_a_name']}"
    )

    lines.append(
        f"**Author B:** "
        f"{result['author_b_name']}"
    )

    lines.append("")

    lines.append(
        f"**Similarity:** "
        f"{sim:.4f}"
    )

    lines.append(
        f"**Distance:** "
        f"{dist:.4f}"
    )

    lines.append("")

    lines.append(
        "## Top Differences"
    )

    lines.append("")

    for idx, item in enumerate(
        result["top_differences"][:5],
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


def execute_intent(
    intent
):
    """
    Execute a parsed assistant intent.
    """


    if (
        intent["intent"]
        == "list_authors"
    ):

        authors = list_authors()

        return {
            "intent": "list_authors",
            "authors": [
                {
                    "id": a.author_id,
                    "name": a.display_name,
                }
                for a in authors
            ],
        }

    if (
        intent["intent"]
        == "list_documents"
    ):

        documents = list_documents()

        return {
            "intent": "list_documents",
            "documents": [
                {
                    "id": d.document_id,
                    "filename": d.filename,
                }
                for d in documents[:100]
            ],
        }
        
    if (
        intent["intent"]
        == "compare_documents"
    ):

        document_a = int(
            intent["document_a"]
        )

        document_b = int(
            intent["document_b"]
        )

        result = compare_documents(
            document_a,
            document_b,
            method="cosine",
        )

        vec_a = build_document_vector(
            document_a
        )

        vec_b = build_document_vector(
            document_b
        )

        differences = (
            calculate_feature_differences(
                vec_a,
                vec_b,
            )
        )

        return {
            "intent":
                "compare_documents",

            "document_a":
                document_a,

            "document_b":
                document_b,

            "result":
                result,

            "top_differences":
                differences[:10],

            "all_differences":
                differences,

            "vector_a":
                vec_a,

            "vector_b":
                vec_b,
        }

    if (
        intent["intent"]
        == "compare_authors"
    ):

        author_a = int(
            intent["author_a"]
        )

        author_b = int(
            intent["author_b"]
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

        author_a_record = get_author(
            author_a
        )

        author_b_record = get_author(
            author_b
        )

        name_a = (
            author_a_record.display_name
            if (
                author_a_record
                and
                author_a_record.display_name
            )
            else f"Author {author_a}"
        )

        name_b = (
            author_b_record.display_name
            if (
                author_b_record
                and
                author_b_record.display_name
            )
            else f"Author {author_b}"
        )

        return {

            "intent":
                "compare_authors",

            "author_a":
                author_a,

            "author_b":
                author_b,

            "author_a_name":
                name_a,

            "author_b_name":
                name_b,

            "result":
                result,

            "top_differences":
                differences[:10],

            "all_differences":
                differences,

            "fingerprint_a":
                fp_a.vector,

            "fingerprint_b":
                fp_b.vector,
        }

    return {

        "error":
        "Unsupported intent: "
        f"{intent['intent']}"
    }


def format_document_comparison(
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
        "# Document Comparison"
    )

    lines.append("")

    lines.append(
        f"Similarity: {sim:.4f}"
    )

    lines.append(
        f"Distance: {dist:.4f}"
    )

    lines.append("")

    lines.append(
        "## Top Differences"
    )

    lines.append("")

    for idx, item in enumerate(
        result["top_differences"][:5],
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
