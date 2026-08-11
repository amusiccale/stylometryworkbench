"""
assistant/intents.py
"""

import json

from llm.client import ask_llm

from models.author import (
    list_authors,
)


def build_author_context():

    authors = list_authors()

    entries = []

    for author in authors:

        name = (
            author.display_name.strip()
            if author.display_name
            else f"Author {author.author_id}"
        )

        entries.append(
            {
                "author_id": author.author_id,
                "name": name,
            }
        )

    return entries


def build_examples(authors):

    #
    # Dynamic author example
    #

    if len(authors) >= 2:

        a = authors[0]
        b = authors[1]

        return f"""
User:
Compare {a['name']} and {b['name']}

Output:
{{
    "intent": "compare_authors",
    "author_a": {a['author_id']},
    "author_b": {b['author_id']}
}}

User:
Compare author {a['author_id']} and author {b['author_id']}

Output:
{{
    "intent": "compare_authors",
    "author_a": {a['author_id']},
    "author_b": {b['author_id']}
}}
"""

    #
    # Empty corpus fallback
    #

    return """
User:
Compare author 1 and author 2

Output:
{
    "intent": "compare_authors",
    "author_a": 1,
    "author_b": 2
}
"""


def identify_intent(prompt):

    authors = build_author_context()

    author_lines = []

    for author in authors:

        author_lines.append(
            f"{author['author_id']}: "
            f"{author['name']}"
        )

    examples = build_examples(
        authors
    )

    system_prompt = f"""
You are an intent parser.

Return ONLY valid JSON.

You MUST NOT answer questions.

You MUST NOT generate analysis.

You MUST NOT invent results.

You MUST ONLY determine:

1. intent
2. parameters

Known Authors:

{chr(10).join(author_lines)}

Allowed intents:

compare_authors
compare_documents
attribute_sample
explain_results
list_authors
list_documents
unknown

{examples}

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
            raise ValueError

        return parsed

    except Exception:

        return {
            "intent": "unknown",
            "raw_response": response,
        }
