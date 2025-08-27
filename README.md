# Sentiment Analysis of User Reviews

**Author:** MennatAllah Naemat Almassri
**Domain:** Data Science & Artificial Intelligence  
**Language:** Python (pandas, matplotlib)

---

## Project Overview

This mini-project classifies short user reviews (e.g., about a product or movie) as **Positive**, **Negative**, or **Neutral** using a lexicon-based NLP method. The goal is to demonstrate a full data pipeline: data preparation, sentiment analysis, visualization, and reporting.

---

## Project Contents

- `sentiment_project_report.pdf` — A polished PDF report with methodology, charts, sample outputs, and conclusions.
- `sentiment_labeled_dataset.csv` — The labeled dataset including sentiment scores.
- `sentiment_project_code.py` — Fully functional Python script used to generate results (proof of work).
- `README.md` — This file (project description and instructions).

---

## Methodology

- **Data Source:** Synthetic dataset (~100 short comments) simulates real-world user feedback.
- **Approach:** Lexicon-based sentiment classification — each positive word receives +1, each negative word −1. Reviews labeled based on final score:  
  - ≥ +1 → Positive  
  - ≤ −1 → Negative  
  - Between → Neutral
- **Tools:** Python, pandas, matplotlib — used for data processing and visualization.
  
---

## Results Summary

The analysis shows a distribution across sentiment categories:
- Percentage breakdown of Positive, Negative, Neutral.
- Bar chart of counts and a pie chart of distribution.
- Top matched opinion words shown in a visual chart.
- Sample reviews for each category provided, demonstrating classification.

See **sentiment_project_report.pdf** for full visual results and conclusions.

---

## How to Use

1. Clone or download the repository.
2. Run `sentiment_project_code.py` in a Python environment (requires `pandas`, `matplotlib`).
3. View `sentiment_project_report.pdf` for formatted results.

---

## Why This Project Matters

- Demonstrates understanding of key AI-related concepts in NLP and data workflows.
- Presents an end-to-end project with documentation, data, and code — ideal for university applications or scholarship review.
- Easily expandable: could evolve to use real datasets, advanced models, or interactive dashboards in the future.

