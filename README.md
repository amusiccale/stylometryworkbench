# Stylometric Fingerprint Workbench

The Stylometric Fingerprint Workbench is a desktop application for exploring writing style, comparing texts, and investigating authorship.

The Workbench can compare authors, compare documents, generate visualizations, and help researchers identify stylistic similarities and differences across a corpus.

---
<img width="584" height="1003" alt="Screenshot 2026-08-10 at 1 46 33 PM" src="https://github.com/user-attachments/assets/54a9fb77-7213-4ab6-9de5-042caa00f328" />
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

- Ollama*
- KoboldCpp*
- LM Studio*
- vLLM*
- OpenAI-compatible APIs (see llm_settings.json and customize as needed)

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
```

---

# Current Status

The Workbench is under active development and is intended for:

- Digital humanities research
- Classroom demonstrations
- Corpus exploration
- Stylometric analysis
- Authorship studies
