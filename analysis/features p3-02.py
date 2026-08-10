"""
analysis/features.py

Feature extraction framework for the
Stylometric Fingerprint Workbench.
"""

import re
from collections import Counter
from typing import Any


# ============================================================
# Tokenization Helpers
# ============================================================

def tokenize_words(text: str) -> list:
    #Convert text into lowercase word tokens.

    #Preserves contractions while ignoring punctuation.
    
    return re.findall(r"\b[\w']+\b", text.lower())


# ============================================================
# P3-02 Lexical Metrics
###============================================================"""

def average_word_length(tokens: list[str]) -> float:
    """
    Average number of characters per word.
    """

    if not tokens:
        return 0.0

    return sum(len(token) for token in tokens) / len(tokens)


def type_token_ratio(tokens: list[str]) -> float:
    """
    Unique words divided by total words.
    """

    if not tokens:
        return 0.0

    return len(set(tokens)) / len(tokens)


def hapax_ratio(tokens: list[str]) -> float:
    """
    Ratio of words occurring exactly once.
    """

    if not tokens:
        return 0.0

    counts = Counter(tokens)

    hapax = sum(
        1 for count in counts.values()
        if count == 1
    )

    return hapax / len(tokens)


def mattr(
    tokens: list[str],
    window_size: int = 50
) -> float:
    """
    Moving Average Type Token Ratio.
    """

    if not tokens:
        return 0.0

    if len(tokens) < window_size:
        return type_token_ratio(tokens)

    scores = []

    for i in range(
        len(tokens) - window_size + 1
    ):
        window = tokens[i:i + window_size]

        scores.append(
            len(set(window)) / window_size
        )

    return sum(scores) / len(scores)


def mtld(
    tokens: list[str],
    threshold: float = 0.72
) -> float:
    """
    Measure of Textual Lexical Diversity.

    Simplified implementation suitable
    for MVP development.
    """

    if len(tokens) < 10:
        return 0.0

    factors = 0
    types = set()
    token_count = 0

    for token in tokens:

        token_count += 1
        types.add(token)

        ttr = len(types) / token_count

        if ttr <= threshold:
            factors += 1
            types.clear()
            token_count = 0

    if token_count:

        partial_factor = (
            1 - (len(types) / token_count)
        ) / (1 - threshold)

        factors += partial_factor

    if factors == 0:
        return float(len(tokens))

    return len(tokens) / factors


def extract_lexical_features(
    text: str
) -> dict[str, float]:
    """
    Extract all lexical features.
    """

    tokens = tokenize_words(text)

    return {
        "avg_word_length":
            average_word_length(tokens),

        "type_token_ratio":
            type_token_ratio(tokens),

        "mattr":
            mattr(tokens),

        "mtld":
            mtld(tokens),

        "hapax_ratio":
            hapax_ratio(tokens),
    }


# ============================================================
# P3-03 Structural Metrics (Placeholder)
# ============================================================

def extract_structural_features(
    text: str
) -> dict[str, float]:

    return {}


# ============================================================
# P3-04 Function Word Metrics (Placeholder)
# ============================================================

def extract_function_word_features(
    text: str
) -> dict[str, float]:

    return {}


# ============================================================
# P3-05 Punctuation Metrics (Placeholder)
# ============================================================

def extract_punctuation_features(
    text: str
) -> dict[str, float]:

    return {}


# ============================================================
# P3-06 Character Metrics (Placeholder)
# ============================================================

def extract_character_features(
    text: str
) -> dict[str, float]:

    return {}


# ============================================================
# P3-07 POS Metrics (Placeholder)
# ============================================================

def extract_pos_features(
    text: str
) -> dict[str, float]:

    return {}


# ============================================================
# Master Extraction API
# ============================================================

def extract_features(
    text: str
) -> dict[str, Any]:
    """
    Master feature extraction entry point.

    Returns:
        FeatureVector dictionary.
    """

    feature_vector = {}

    feature_vector.update(
        extract_lexical_features(text)
    )

    feature_vector.update(
        extract_structural_features(text)
    )

    feature_vector.update(
        extract_function_word_features(text)
    )

    feature_vector.update(
        extract_punctuation_features(text)
    )

    feature_vector.update(
        extract_character_features(text)
    )

    feature_vector.update(
        extract_pos_features(text)
    )

    return feature_vector
