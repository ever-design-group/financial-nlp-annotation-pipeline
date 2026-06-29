# Changelog – Project 1B Annotation Pipeline

## [v3.0] – 2026-06-22

### Added
- Final dataset with 500 annotated communications
- Bias correction applied to all scores
- Sarcasm detection protocol (from Barclays case study)
- 42 adjudication cases with documented rationale

### Changed
- Confusion scoring clarified with 15 new anchor examples
- "Kindly" rule added: Frustration +1 for formal Indian complaints
- Intent tie-breaker: Request > Complaint when ambiguous

### Fixed
- Confusion α improved from 0.65 → 0.71
- A2 cultural bias corrected (Frustration avg 2.8 → 4.0)
- A4 sarcasm false positive rate reduced 28% → 9%

## [v2.0] – 2026-06-15

### Added
- 10 calibration exercises (50 items total)
- Annotator bias profiles for 5 annotators
- Gold standard set (50 expert-annotated items)

## [v1.0] – 2026-06-08

### Added
- Initial 3-dimensional taxonomy
- Basic annotation guidelines
- Corpus statistics
