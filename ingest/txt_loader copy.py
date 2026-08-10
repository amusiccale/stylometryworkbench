"""
ingest/txt_loader.py

TXT file ingestion.
"""

from pathlib import Path
from ingest.normalization import normalize_text

def load_txt(path: str | Path) -> str:
    path = Path(path)

    with open(
        path,
        "r",
        encoding="utf-8",
        errors="replace"
    ) as infile:
        return normalize_text(text)
