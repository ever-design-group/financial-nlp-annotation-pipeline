# Methodology – Project 1B Annotation Pipeline

## 1. Project Design Philosophy

This project follows a **defence-in-depth annotation quality architecture** built across four disciplines:

1. **Taxonomic Design** – Stress-tested every label boundary with edge cases
2. **Calibration Phase** – Aligned annotator interpretations through worked examples
3. **Measurement Phase** – Continuously tracked agreement statistics
4. **Resolution Phase** – Documented adjudication protocols converting disagreements into guideline improvements

---

## 2. Data Preparation

### 2.1 Corpus Composition

| Channel | Count | Percentage |
|---------|-------|------------|
| Email | 175 | 35% |
| Live Chat | 150 | 30% |
| Social Media | 100 | 20% |
| Call Transcript | 75 | 15% |
| **Total** | **500** | **100%** |

### 2.2 Generation Strategy

Used **persona-based generation** with 15 customer personas:
- Senior citizens (pension issues, healthcare concerns)
- Tech-savvy millennials (app issues, digital banking)
- Small business owners (transaction volumes, fees)
- NRIs (cross-border payments, forex)
- Rural customers (KYC, UPI issues)

---

## 3. Taxonomy Design

### 3.1 Three-Dimensional Schema

**Dimension 1: Sentiment (4 sub-dimensions × 1-5 Likert)**
- Satisfaction (valence)
- Urgency (time-sensitivity)
- Frustration (emotional friction)
- Confusion (lack of understanding)

**Dimension 2: Intent (5 categories, multi-label)**
- Complaint, Query, Request, Feedback, Escalation

**Dimension 3: Topic (5 categories, multi-label)**
- Billing, Fraud, Account Access, Product Inquiry, Regulatory Complaint

### 3.2 Theoretical Label Space

---

## 4. Quality Assurance

### 4.1 Four-Layer QA Model

| Layer | Timing | Activity |
|-------|--------|----------|
| 1: Preventive | Before annotation | Guidelines, calibration, pilot testing |
| 2: In-Process | During annotation | Real-time monitoring, gold standard insertion |
| 3: Post-Batch | After each batch | Batch IAA computation, outlier detection |
| 4: Cumulative | Dataset completion | Corpus statistics, final IAA, bias audit |

### 4.2 Quality Metrics Computed

- **Cohen's Kappa** (pairwise, weighted for ordinal)
- **Krippendorff's Alpha** (per dimension)
- **Adjudication Rate** (% requiring resolution)
- **Gold Standard Accuracy** (% alignment with expert labels)

---

## 5. Bias Detection & Mitigation

| Bias Type | Detection Method | Mitigation |
|-----------|------------------|------------|
| Central Tendency | Histogram analysis | Forced extreme scores |
| Cultural Bias | Cross-annotator comparison | India-specific calibration |
| Acquiescence | Average labels/item | Default "Not Present" |
| Sarcasm Over-detection | Sarcasm flag rate | Barclays sarcasm protocol |
| Fatigue | Temporal analysis | Session limits (30 max) |

---

## 6. Disagreement Resolution Protocol

### 6.1 Tiered Process

| Tier | Trigger | Action |
|------|---------|--------|
| 1 | IAA > 0.75 | Median/Mode (automatic) |
| 2 | IAA 0.40-0.75 | 3-person Panel (2/3 vote) |
| 3 | IAA < 0.40 or Panel Tie | NLP Lead adjudication |

### 6.2 Outcomes

- **42 items adjudicated** (8.4% of corpus)
- **14 guideline updates** triggered
- **All resolved** with documented rationale

---

## 7. ML Team Handoff

### 7.1 Model Training Recommendations

- **Sentiment**: Ordinal regression with macro-weighted loss
- **Intent/Topic**: Multi-label classification with class weights
- **Sample weighting**: Use agreement score as training weight
- **Curriculum learning**: High-agreement data first
- **Model backbone**: FinBERT or XLM-RoBERTa

### 7.2 Expected Performance

| Task | Expected Metric |
|------|-----------------|
| Intent Classification | F1 > 0.85 |
| Sentiment Prediction | MAE < 0.6 |
| Topic Classification | F1 > 0.88 |

---

**Version:** 1.0  
**Last Updated:** 2026-06-22
