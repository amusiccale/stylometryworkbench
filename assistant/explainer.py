"""
assistant/explainer.py
"""

from llm.client import ask_llm

from assistant.knowledge_base import (
    get_knowledge_context,
)


def explain_author_comparison(
    result,
):

    context = (
        get_knowledge_context()
    )

    prompt = f"""
Interpret this stylometric comparison.

Similarity:
{result["result"]["similarity"]}

Distance:
{result["result"]["distance"]}

Top Differences:
{result["top_differences"][:5]}
"""

    system_prompt = f"""
You are the Stylometric
Fingerprint Workbench
Assistant.

Interpret results using
the supplied documentation.

Be concise.

Documentation:

{context}
"""

    return ask_llm(
        prompt,
        system_prompt,
    )

def explain_document_comparison(
    result,
):

    context = (
        get_knowledge_context()
    )

    prompt = f"""
Interpret this document comparison.

Similarity:
{result["result"]["similarity"]}

Distance:
{result["result"]["distance"]}

Top Differences:
{result["top_differences"][:5]}

Explain:

1. What the similarity suggests.
2. What the distance suggests.
3. What the top differences suggest.
4. Important cautions.

Keep the explanation concise.
"""

    system_prompt = f"""
You are the Stylometric
Fingerprint Workbench Assistant.

Interpret results using the
supplied documentation.

Documentation:

{context}
"""

    return ask_llm(
        prompt,
        system_prompt,
    )
