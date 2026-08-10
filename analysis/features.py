"""
analysis/features.py

Feature extraction framework for the
Stylometric Fingerprint Workbench.
"""

import re
import statistics
import math
import spacy
try:
    NLP = spacy.load("en_core_web_sm")
except OSError:
    NLP = None
from collections import Counter
from typing import Any


#===defining function words p3-04======

FUNCTION_WORDS = [
    "the",
    "and",
    "but",
    "however",
    "therefore",
    "thus",
    "if",
    "because",
    "while",
    "although",
    "yet",
    "of",
    "to",
    "in",
    "for",
    "on",
    "with",
    "at",
    "by",
    "from",
]

#--defining full features

REQUIRED_FEATURES = [
    # Lexical
    "avg_word_length",
    "type_token_ratio",
    "mattr",
    "mtld",
    "hapax_ratio",

    # Structural
    "sentence_length_mean",
    "sentence_length_variance",
    "paragraph_length_mean",
    "paragraph_length_variance",

    # Function words
    *[f"fw_{word}" for word in FUNCTION_WORDS],

    # Punctuation
    "comma_ratio",
    "semicolon_ratio",
    "colon_ratio",
    "dash_ratio",
    "quote_ratio",
    "parenthesis_ratio",

    # Character
    "uppercase_ratio",
    "digit_ratio",
    "whitespace_ratio",
    "character_entropy",

    # POS
    "noun_ratio",
    "verb_ratio",
    "adjective_ratio",
    "adverb_ratio",
    "pronoun_ratio",
]
#Feature Validation, p3-08

import math


def validate_feature_vector(feature_vector):
    """
    Ensure all required features exist
    and contain valid numeric values.
    """

    for feature_name in REQUIRED_FEATURES:

        if feature_name not in feature_vector:
            raise ValueError(
                f"Missing feature: {feature_name}"
            )

        value = feature_vector[feature_name]

        if not isinstance(value, (int, float)):
            raise ValueError(
                f"Non-numeric feature: {feature_name}"
            )

        if math.isnan(value):
            raise ValueError(
                f"NaN feature: {feature_name}"
            )

    return True

# ============================================================
# Tokenization Helpers
# ============================================================

def tokenize_words(text: str) -> list:
    #Convert text into lowercase word tokens.

    #Preserves contractions while ignoring punctuation.
    
    return re.findall(r"\b[\w']+\b", text.lower())

# ==== P3-03 Structural Metrics====

def split_sentences(text):
    """
    Simple sentence segmentation.

    Splits on:
        .
        !
        ?

    Removes empty results.
    """

    sentences = re.split(r"[.!?]+", text)

    return [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]

def split_paragraphs(text):
    """
    Split text into paragraphs.

    Assumes normalization has already
    collapsed excess blank lines.
    """

    paragraphs = text.split("\n\n")

    return [
        paragraph.strip()
        for paragraph in paragraphs
        if paragraph.strip()
    ]

def sentence_lengths(text):
    """
    Return sentence lengths in words.
    """

    sentences = split_sentences(text)

    return [
        len(tokenize_words(sentence))
        for sentence in sentences
    ]

def paragraph_lengths(text):
    """
    Return paragraph lengths in words.
    """

    paragraphs = split_paragraphs(text)

    return [
        len(tokenize_words(paragraph))
        for paragraph in paragraphs
    ]

#===P3-04 function word helper function

def function_word_frequencies(tokens):
    """
    Compute normalized function-word frequencies.
    """

    token_count = len(tokens)

    if token_count == 0:
        return {
            f"fw_{word}": 0.0
            for word in FUNCTION_WORDS
        }

    counts = Counter(tokens)

    return {
        f"fw_{word}":
            counts.get(word, 0) / token_count
        for word in FUNCTION_WORDS
    }
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
# P3-03 Structural Metrics (now implemented)
# ============================================================

def extract_structural_features(text):
    """
    Extract structural stylometric metrics.
    """

    sentence_counts = sentence_lengths(text)
    paragraph_counts = paragraph_lengths(text)

    if sentence_counts:
        sentence_mean = statistics.mean(
            sentence_counts
        )

        sentence_variance = (
            statistics.variance(sentence_counts)
            if len(sentence_counts) > 1
            else 0.0
        )
    else:
        sentence_mean = 0.0
        sentence_variance = 0.0

    if paragraph_counts:
        paragraph_mean = statistics.mean(
            paragraph_counts
        )

        paragraph_variance = (
            statistics.variance(paragraph_counts)
            if len(paragraph_counts) > 1
            else 0.0
        )
    else:
        paragraph_mean = 0.0
        paragraph_variance = 0.0

    return {
        "sentence_length_mean":
            sentence_mean,

        "sentence_length_variance":
            sentence_variance,

        "paragraph_length_mean":
            paragraph_mean,

        "paragraph_length_variance":
            paragraph_variance,
    }


# ============================================================
# P3-04 Function Word Metrics (now implemented, p3-04)
# ============================================================

def extract_function_word_features(text):
    """
    Extract normalized function-word frequencies.
    """

    tokens = tokenize_words(text)

    return function_word_frequencies(tokens)


# ============================================================
# P3-05 Punctuation Metrics (now implemented p3-05)
# ============================================================

def punctuation_frequencies(text):
    """
    Compute normalized punctuation frequencies.
    """

    total_chars = len(text)

    if total_chars == 0:
        return {
            "comma_ratio": 0.0,
            "semicolon_ratio": 0.0,
            "colon_ratio": 0.0,
            "dash_ratio": 0.0,
            "quote_ratio": 0.0,
            "parenthesis_ratio": 0.0,
        }

    comma_count = text.count(",")

    semicolon_count = text.count(";")

    colon_count = text.count(":")

    dash_count = (
        text.count("-")
        + text.count("—")
        + text.count("–")
    )

    quote_count = (
        text.count('"')
        + text.count("'")
    )

    parenthesis_count = (
        text.count("(")
        + text.count(")")
    )

    return {
        "comma_ratio":
            comma_count / total_chars,

        "semicolon_ratio":
            semicolon_count / total_chars,

        "colon_ratio":
            colon_count / total_chars,

        "dash_ratio":
            dash_count / total_chars,

        "quote_ratio":
            quote_count / total_chars,

        "parenthesis_ratio":
            parenthesis_count / total_chars,
    }

def extract_punctuation_features(text):
    """
    Extract punctuation-based stylometric metrics.
    """

    return punctuation_frequencies(text)

# ============================================================
# P3-06 Character Metrics (added and working)
# ============================================================

import math


def character_metrics(text):
    """
    Compute character-level stylometric metrics.
    """

    total_chars = len(text)

    if total_chars == 0:
        return {
            "uppercase_ratio": 0.0,
            "digit_ratio": 0.0,
            "whitespace_ratio": 0.0,
            "character_entropy": 0.0,
        }

    uppercase_count = sum(
        1 for c in text
        if c.isupper()
    )

    digit_count = sum(
        1 for c in text
        if c.isdigit()
    )

    whitespace_count = sum(
        1 for c in text
        if c.isspace()
    )

    # Shannon entropy
    counts = Counter(text)

    entropy = 0.0

    for count in counts.values():

        probability = count / total_chars

        entropy -= (
            probability
            * math.log2(probability)
        )

    return {
        "uppercase_ratio":
            uppercase_count / total_chars,

        "digit_ratio":
            digit_count / total_chars,

        "whitespace_ratio":
            whitespace_count / total_chars,

        "character_entropy":
            entropy,
    }

def extract_character_features(text):
    """
    Extract character-level stylometric metrics.
    """

    return character_metrics(text)


# ============================================================
# P3-07 POS Metrics (implemented)
# ============================================================

def pos_metrics(text):
    """
    Compute normalized part-of-speech ratios.
    """

    if NLP is None:
        return {
            "noun_ratio": 0.0,
            "verb_ratio": 0.0,
            "adjective_ratio": 0.0,
            "adverb_ratio": 0.0,
            "pronoun_ratio": 0.0,
        }

    doc = NLP(text)

    tokens = [
        token
        for token in doc
        if not token.is_space
    ]

    total_tokens = len(tokens)

    if total_tokens == 0:
        return {
            "noun_ratio": 0.0,
            "verb_ratio": 0.0,
            "adjective_ratio": 0.0,
            "adverb_ratio": 0.0,
            "pronoun_ratio": 0.0,
        }

    noun_count = sum(
        1 for token in tokens
        if token.pos_ in ("NOUN", "PROPN")
    )

    verb_count = sum(
        1 for token in tokens
        if token.pos_ == "VERB"
    )

    adjective_count = sum(
        1 for token in tokens
        if token.pos_ == "ADJ"
    )

    adverb_count = sum(
        1 for token in tokens
        if token.pos_ == "ADV"
    )

    pronoun_count = sum(
        1 for token in tokens
        if token.pos_ == "PRON"
    )

    return {
        "noun_ratio":
            noun_count / total_tokens,

        "verb_ratio":
            verb_count / total_tokens,

        "adjective_ratio":
            adjective_count / total_tokens,

        "adverb_ratio":
            adverb_count / total_tokens,

        "pronoun_ratio":
            pronoun_count / total_tokens,
    }

def extract_pos_features(text):
    """
    Extract part-of-speech stylometric metrics.
    """

    return pos_metrics(text)


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

    validate_feature_vector(feature_vector)

    return feature_vector
