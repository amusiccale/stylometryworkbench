# Stylometric Fingerprint Workbench

A local-first stylometric analysis and authorship attribution environment designed for digital humanities research, teaching, and exploratory corpus analysis.

The Workbench allows researchers to build stylometric fingerprints for authors, compare authors and documents, visualize feature differences, perform authorship attribution, and explore stylistic patterns across a corpus.

---

# Status

Current Development Phase:

```text
Phase A
    Core Data Model
        Complete

Phase B
    Analysis and Visualization
        Largely Complete

Phase C
    Workbench Assistant
        In Progress
```

---

# Major Features

## Author Fingerprints

Build stylometric profiles from one or more documents.

Fingerprints currently aggregate:

```text
Lexical Features

Structural Features

Function Word Frequencies

Character Features

Punctuation Features

Part-of-Speech Features
```

---

## Author Comparison

Compare two authors using:

```text
Cosine Similarity

Distance Measures

Feature Difference Analysis
```

Outputs include:

```text
Similarity Score

Distance Score

Radar Charts

Difference Charts

Interpretive Commentary
```

---

## Document Comparison

Compare two individual documents.

Outputs include:

```text
Similarity Score

Distance Score

Radar Charts

Difference Charts

Interpretive Commentary
```

---

## Authorship Attribution

Compare unknown samples against known author fingerprints.

Current workflow supports:

```text
Fingerprint Matching

Similarity Ranking

Attribution Analysis
```

---

## Corpus Management

Manage:

```text
Authors

Documents

Fingerprints
```

through the Workbench interface.

---

# Visualizations

## Radar Charts

Supported Modes:

```text
raw

log

relative

log_relative
```

Recommended:

```text
log_relative
```

because it provides the most useful balance between large and small feature values.

---

## Difference Charts

Feature-level comparisons showing:

```text
Largest Positive Differences

Largest Negative Differences

Overall Stylistic Separation
```

---

# Workbench Assistant

Status:

```text
Experimental
```

The Workbench Assistant provides optional natural-language access to existing Workbench functionality.

Supported Backends:

```text
Ollama

KoboldCpp

LM Studio

vLLM

OpenAI-Compatible APIs
```

The assistant is completely optional.

The Workbench remains fully functional without any LLM integration.

---

## Current Assistant Capabilities

### Knowledge Assistant

Users may ask:

```text
What does MTLD mean?

How should radar charts be interpreted?

What does a similarity score represent?
```

The assistant answers using Workbench documentation.

---

### Author Comparison

Example:

```text
Compare Woolf and Joyce
```

Workflow:

```text
Natural Language

↓

Intent Recognition

↓

Workbench Analysis

↓

Interpretation

↓

Visualizations
```

---

### Document Comparison

Example:

```text
Compare document 12 and document 19
```

Outputs:

```text
Similarity

Distance

Difference Analysis

Interpretive Commentary

Visualizations
```

---

# Assistant Architecture

The assistant does not perform stylometric analysis.

The architecture is:

```text
User Prompt

↓

Intent Detection

↓

Existing Workbench Functions

↓

Result Formatting

↓

Interpretation
```

The LLM acts as:

```text
Planner

Interpreter

Narrator
```

The Workbench remains responsible for:

```text
Feature Extraction

Similarity Calculation

Attribution

Visualization

Analysis
```

---

# Design Principles

## Local First

The Workbench is intended to function without cloud services whenever possible.

---

## Existing Engine Is Authoritative

All analytical results originate from the Workbench codebase.

The assistant does not calculate:

```text
Similarity

Distance

Attribution Scores

Feature Differences
```

directly.

---

## Maximum Reuse

Whenever possible:

```text
Assistant
    ↓
Existing Workbench Function
```

instead of:

```text
Assistant
    ↓
New Analysis Layer
```

---

# Project Structure

```text
analysis/
    Feature Extraction
    Similarity
    Attribution
    Feature Differences

models/
    Authors
    Documents
    Fingerprints

visualization/
    Radar Charts
    Difference Charts

gui/
    NiceGUI Interface

assistant/
    Intent Recognition
    Execution
    Formatting
    Explanation

llm/
    OpenAI-Compatible Client
```

---

# Documentation

Key references:

```text
INTERPRETING_RESULTS_AND_VISUALIZATIONS.md

APPENDIX_C_WORKBENCH_ASSISTANT_ROADMAP.md
```

---

# Current Roadmap

Recent Milestones:

```text
✅ Knowledge Assistant

✅ Intent Recognition

✅ Author Comparison Execution

✅ Document Comparison Execution

✅ Interpretation Layer

✅ Embedded Comparison Visualizations
```

Upcoming:

```text
Document Discovery Improvements

Chart-Specific Requests

Attribution Through Assistant

Research Dashboard

HTML Report Integration
```

---

# License

Project license and distribution terms have not yet been finalized.