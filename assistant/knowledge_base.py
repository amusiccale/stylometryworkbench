"""
assistant/knowledge_base.py
"""

from pathlib import Path


KNOWLEDGE_FILES = [

    "docs/INTERPRETING_RESULTS_AND_VISUALIZATIONS.md",

]


def get_knowledge_context():

    sections = []

    for filename in KNOWLEDGE_FILES:

        path = Path(
            filename
        )

        if path.exists():

            sections.append(
                path.read_text(
                    encoding="utf-8"
                )
            )

    return "\n\n".join(
        sections
    )
