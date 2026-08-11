"""
assistant/intents.py
"""

import json

from llm.client import ask_llm

from models.author import (
    list_authors,
)


def build_author_context():
    """
    Build a list of known authors that
    can be injected into the prompt.
    """

    authors = list_authors()

    lines = []

    for author in authors:

        name = (
            author.display_name.strip()
            if author.display_name
            else f"Author {author.author_id}"
        )

        lines.append(
            f"{author.author_id}: {name}"
        )

    return "\n".join(lines)


def identify_intent(prompt):

    author_context = (
        build_author_context()
    )

    system_prompt = f"""
You are an intent parser.

Return ONLY valid JSON.

You MUST NOT answer the user's question.

You MUST NOT generate analysis.

You MUST NOT invent results.

You MUST ONLY determine the
requested action and parameters.

Known Authors:

{author_context}

Allowed intents:

compare_authors
compare_documents
attribute_sample
explain_results
list_authors
list_documents
unknown

Examples:

User:
Compare authors 1 and 2

Output:
{{
    "intent": "compare_authors",
    "author_a": 1,
    "author_b": 2
}}

User:
Compare Shakespeare and Marlowe

Output:
{{
    "intent": "compare_authors",
    "author_a": 3,
    "author_b": 7
}}

User:
Compare document 4 and document 9

Output:
{{
    "intent": "compare_documents",
    "document_a": 4,
    "document_b": 9
}}

User:
Who wrote this sample?

Output:
{{
    "intent": "attribute_sample"
}}

User:
What does MTLD mean?

Output:
{{
    "intent": "explain_results"
}}
"""

    response = ask_llm(
        prompt,
        system_prompt,
    )

    try:

        parsed = json.loads(
            response
        )

        if not isinstance(
            parsed,
            dict,
        ):

            raise ValueError(
                "Intent must be a dictionary."
            )

        return parsed

    except Exception:

        return {
            "intent": "unknown",
            "raw_response": response,
        }
