"""
ingest/normalization.py

Shared text normalization utilities.
"""

import re


def normalize_text(text: str) -> str:
    """
    Normalize text while preserving content useful
    for stylometric analysis.

    Rules:
    - Normalize line endings
    - Remove trailing whitespace
    - Collapse multiple blank lines
    - Preserve punctuation
    - Preserve capitalization
    """

    # Normalize line endings
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # Remove trailing whitespace on each line
    lines = [line.rstrip() for line in text.split("\n")]

    text = "\n".join(lines)

    # Collapse 3+ blank lines to 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove leading/trailing file whitespace
    text = text.strip()

    return text
