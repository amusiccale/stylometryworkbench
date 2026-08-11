# Stylometric Fingerprint Workbench

The Stylometric Fingerprint Workbench is a desktop application for exploring writing style, comparing texts, and investigating authorship.

The Workbench can compare authors, compare documents, generate visualizations, and help researchers identify stylistic similarities and differences across a corpus.

---

# Main Features

## Compare Authors

Compare two authors using stylometric fingerprints.

Results include:

- Similarity score
- Distance score
- Radar charts
- Difference charts
- Interpretive commentary

---

## Compare Documents

Compare two individual documents.

Results include:

- Similarity score
- Distance score
- Radar charts
- Difference charts
- Interpretive commentary

---

## Author Fingerprints

Build a stylistic profile from one or more documents.

Fingerprints capture features such as:

- Vocabulary usage
- Function words
- Sentence structure
- Punctuation habits
- Character-level patterns
- Parts of speech

---

## Authorship Attribution

Compare an unknown text against known author fingerprints to identify likely stylistic matches.

---

## Corpus Explorer

Browse authors, documents, and corpus content.

---

# Visualizations

## Radar Charts

Visual summaries of writing style across multiple feature categories.

Recommended display mode:

```text
log_relative
```

---

## Difference Charts

Show which features contribute most strongly to stylistic differences between authors or documents.

---

# Workbench Assistant (Experimental)

The Workbench Assistant provides a natural-language interface to many Workbench features.

Examples:

```text
Compare Woolf and Joyce

Compare document 12 and document 19

List authors

List documents
```

The assistant can:

- Run comparisons
- Explain results
- Generate visualizations
- Answer questions about stylometric concepts

Supported local LLM backends include:

- Ollama
- KoboldCpp
- LM Studio
- vLLM
- OpenAI-compatible APIs

The assistant is optional and the Workbench works normally without it.

---

# Recommended Workflow

1. Import documents.
2. Build author fingerprints.
3. Compare authors or documents.
4. Review charts and explanations.
5. Perform attribution analysis when appropriate.

---

# Documentation

Additional guides are included in the project:

```text
INTERPRETING_RESULTS_AND_VISUALIZATIONS.md

APPENDIX_C_WORKBENCH_ASSISTANT_ROADMAP.md
```

---

# Current Status

The Workbench is under active development and is intended for:

- Digital humanities research
- Classroom demonstrations
- Corpus exploration
- Stylometric analysis
- Authorship studies
