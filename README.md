# COSC-5856-W03---Introduction-to-Cybersecurity
Insider Threat Detection System
Project Overview

This project implements a machine learning–based insider threat detection system using behavioral anomaly detection techniques on user activity data inspired by the CERT insider threat dataset.

The goal is to identify high-risk users based on abnormal behavioral patterns such as after-hours logins, unusual file access activity, and device usage anomalies.

System Architecture

Raw logs → Feature Engineering

Behavioral aggregation (user-day level)

XGBoost classification model

Threshold optimization using Precision–Recall curve

Streamlit deployment for interactive prediction

Features Used

logon_count

after_hours_logons

file_access_count

unique_files

device_activity_count

logon_dev

file_dev

device_dev

These features capture behavioral deviation and access anomalies.

Model

Algorithm: XGBoost Classifier

Class imbalance handled

Threshold optimized using PR curve

Best F1 score achieved: ~0.30 (minority insider class)

Results

Precision-Recall curve analysis

Feature importance analysis

High-risk user identification

Interactive probability-based prediction

How to Run
pip install -r requirements.txt
streamlit run src/app.py
