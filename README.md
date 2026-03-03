# COSC-5856-W03---Introduction-to-Cybersecurity
---

# Insider Threat Detection Using Behavioral Anomaly Modeling

## Abstract

This project implements a behavioral anomaly–based insider threat detection system using supervised machine learning techniques. The objective is to identify potentially malicious insiders by analyzing deviations in user activity patterns such as login frequency, file access behavior, and device usage anomalies.

The system applies gradient boosting (XGBoost) to engineered behavioral features and optimizes classification thresholds using Precision–Recall analysis to address class imbalance.

---

## Problem Definition

Insider threats represent a significant cybersecurity risk due to the difficulty of distinguishing malicious activity from legitimate user behavior. Traditional rule-based detection systems are often insufficient due to high false positive rates.

This project models insider detection as a binary classification problem:

* Class 0 → Normal User Behavior
* Class 1 → Insider Threat

The primary challenge addressed is class imbalance and anomaly detection within behavioral data.

---

## Data Representation

Each observation corresponds to a user-day aggregation of behavioral activity. Features are engineered from structured activity logs inspired by the CERT Insider Threat dataset.

The dataset itself is not included in this repository due to size and licensing constraints.

---

## Feature Engineering

The following behavioral features are used:

* `logon_count`
* `after_hours_logons`
* `file_access_count`
* `unique_files`
* `device_activity_count`
* `logon_dev`
* `file_dev`
* `device_dev`

Deviation-based features quantify divergence from historical baselines and improve anomaly detection sensitivity.

---

## Model Architecture

* Algorithm: XGBoost Classifier
* Evaluation Metric: F1-score (minority class)
* Class Imbalance Handling: Threshold tuning via Precision–Recall curve
* Decision Threshold: Optimized (~0.82)

---

## Experimental Results

Performance evaluation includes:

* Confusion Matrix
* Precision–Recall Curve
* Threshold vs Recall Analysis
* Feature Importance Analysis

Observed performance:

* Insider-class F1-score ≈ 0.29–0.30
* Insider recall > 0.80 after threshold optimization
* High accuracy due to majority class dominance

Feature importance analysis indicates that behavioral deviation metrics and device activity features contribute most strongly to classification decisions.

---

## Implementation

The system is deployed using Streamlit to allow interactive prediction.

Users may:

1. Upload engineered behavioral feature CSV
2. Generate insider probability scores
3. Identify high-risk users

---

## Repository Structure

```
notebooks/      Model development and analysis
src/
    app.py      Streamlit application
    xgb_model.json  Trained model
requirements.txt
README.md
```

---

## Limitations

* Requires pre-engineered features (raw logs not processed in current phase)
* Precision affected by class imbalance
* Not integrated into a real-time monitoring pipeline

---

## Future Work

* Automated feature engineering from raw log ingestion
* Real-time SOC integration
* Threshold adjustment interface
* Model explainability using SHAP
* Temporal modeling using sequence-based approaches

---

## Conclusion

This project demonstrates a structured approach to insider threat detection through:

* Behavioral feature engineering
* Supervised anomaly classification
* Threshold optimization
* Deployable cybersecurity analytics interface

It provides a foundation for scalable insider threat monitoring systems.

---

