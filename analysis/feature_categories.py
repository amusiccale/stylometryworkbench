"""
analysis/feature_categories.py

Feature grouping definitions.
"""

FEATURE_CATEGORIES = {

    "lexical": [

        "avg_word_length",
        "type_token_ratio",
        "mattr",
        "mtld",
        "hapax_ratio",
    ],

    "structural": [

        "sentence_length_mean",
        "sentence_length_variance",
        "paragraph_length_mean",
        "paragraph_length_variance",
    ],

    "character": [

        "uppercase_ratio",
        "digit_ratio",
        "whitespace_ratio",
        "character_entropy",
    ],

    "punctuation": [

        "comma_ratio",
        "semicolon_ratio",
        "colon_ratio",
        "dash_ratio",
        "parenthesis_ratio",
        "quote_ratio",
        "question_ratio",
        "exclamation_ratio",
    ],

    "pos": [

        "noun_ratio",
        "verb_ratio",
        "adjective_ratio",
        "adverb_ratio",
        "pronoun_ratio",
        "conjunction_ratio",
        "determiner_ratio",
    ],

    "function_words": [

        # populate using your actual
        # function-word feature names

        "fw_the",
        "fw_and",
        "fw_but",
        "fw_if",
        "fw_because",
        "fw_while",
    ],
}

def all_features():

    features = []

    for category in FEATURE_CATEGORIES.values():

        features.extend(category)

    return sorted(
        set(features)
    )

def feature_checkbox_state():

    return {
        feature: True
        for feature in all_features()
    }

def features_from_categories(
    categories,
):
    """
    Return feature list from category names.
    """

    selected = []

    for category in categories:

        selected.extend(
            FEATURE_CATEGORIES.get(
                category,
                [],
            )
        )

    return sorted(
        set(selected)
    )
