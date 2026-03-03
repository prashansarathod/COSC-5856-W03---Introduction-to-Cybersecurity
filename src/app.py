import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb

st.title("Insider Threat Detection System")

st.write("Upload behavioral feature CSV to detect insider risk.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("Preview of data:")
    st.dataframe(df.head())

    feature_cols = [
    'logon_dev',
    'file_dev',
    'device_dev',
    'after_hours_logons',
    'logon_count',
    'file_access_count',
    'unique_files',
    'device_activity_count'
]

    X = df[feature_cols]

    # Load model safely
    model = xgb.XGBClassifier()
    model.load_model("src/xgb_model.json")

    probs = model.predict_proba(X)[:,1]
    df["insider_probability"] = probs
    df["predicted_insider"] = (probs >= 0.82).astype(int)

    st.write("Prediction Results:")
    st.dataframe(df.head())

    st.write("High Risk Users:")
    st.dataframe(df[df["predicted_insider"] == 1])