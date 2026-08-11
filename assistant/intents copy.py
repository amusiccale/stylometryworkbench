import json

from llm.client import ask_llm


def identify_intent(prompt):

    system_prompt = """
Return ONLY JSON.

Allowed intents:

compare_authors

compare_documents

attribute_sample

explain_results

unknown

Examples:

Compare authors 1 and 2

{
  "intent": "compare_authors",
  "author_a": 1,
  "author_b": 2
}
"""

    response = ask_llm(
        prompt,
        system_prompt,
    )

    return json.loads(
        response
    )
