import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Real-Time Fraud Monitor", layout="wide")

st.title("💳 Real-Time Fraud Detection Dashboard")
st.markdown("Monitor incoming transactions and view predicted anomalies in real time.")

# Placeholder for storing recent transactions
if 'history' not in st.session_state:
    st.session_state.history = []

# Simulated endpoint (same as used by simulator)
ENDPOINT = "http://localhost:8000/stream"

# File upload for testing
uploaded_file = st.file_uploader("Upload a new transaction CSV to simulate", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())

    responses = []
    for _, row in df.iterrows():
        payload = row.to_dict()
        response = requests.post(ENDPOINT, json=payload)
        result = response.json()
        st.session_state.history.append(result)
        responses.append(result)

    result_df = pd.DataFrame(responses)
    st.success("✅ Stream complete. Anomalies detected below.")

    st.dataframe(result_df)

# Show past results
if len(st.session_state.history):
    st.subheader("📊 Latest Stream Results")
    hist_df = pd.DataFrame(st.session_state.history[-10:])
    st.dataframe(hist_df.style.applymap(
        lambda v: "background-color: salmon" if v is True else "",
        subset=["is_anomaly"]
    ))
