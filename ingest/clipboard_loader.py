"""
ingest/clipboard_loader.py

Clipboard text ingestion.
"""
from ingest.normalization import normalize_text

def load_clipboard(text: str) -> str:
    """
    Accept pasted text and normalize line endings.

    Converts:
        Windows CRLF (\r\n)
        Classic Mac CR (\r)

    To:
        Unix LF (\n)

    Args:
        text: Pasted text content.

    Returns:
        Text with normalized line endings.
    """

    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    return normalize_text(text)
