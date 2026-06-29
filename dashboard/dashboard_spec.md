# Quality Metrics Dashboard Specification

## Overview

This dashboard provides real-time visibility into annotation quality metrics for the 500 financial customer communications project.

---

## 8 Metric Types

### 1. Krippendorff's Alpha by Axis
- **Display:** Bar chart
- **Metrics:** Satisfaction, Urgency, Frustration, Confusion, Intent, Topic
- **Target:** ≥0.70 (Sentiment), ≥0.75 (Intent), ≥0.80 (Topic)
- **Current:** 0.74, 0.70, 0.76, 0.71, 0.79, 0.83

### 2. Annotator Performance Heatmap
- **Display:** 6x6 color-coded grid
- **Metric:** Pairwise Cohen's Kappa
- **Colors:** Green (≥0.80), Yellow (0.60-0.80), Red (<0.60)

### 3. Label Distribution Monitor
- **Display:** Histograms per annotator
- **Alert:** >2 SD from team mean

### 4. Disagreement Rate Tracker
- **Display:** Line chart over time
- **Target:** <15%
- **Current:** 8.4%

### 5. Gold Standard Accuracy
- **Display:** Line chart per annotator
- **Target:** >80%
- **Current:** All >85%

### 6. Annotation Velocity
- **Display:** Items/hour per annotator
- **Alert:** Speed increase >50% from baseline

### 7. Cultural Bias Monitor
- **Display:** Hinglish vs English scores
- **Expected:** Hinglish ≥ English

### 8. Sarcasm Flag Rate
- **Display:** % flagged per annotator
- **Target:** 10-15%
- **Current:** 12% team average

---

## Implementation Technology

- **Backend:** Python + Flask
- **Frontend:** Plotly/Dash
- **Data Source:** JSON dataset + gold standard
- **Update Frequency:** Real-time (batch processing)
