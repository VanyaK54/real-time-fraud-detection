# 💳 Real-Time Fraud Detection in Financial Transactions

Detect anomalous transactions in real time using unsupervised learning and simulate data streams for fraud monitoring in financial systems.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
![Azure](https://img.shields.io/badge/Azure-Enabled-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Project Overview

This project simulates financial transactions and applies **unsupervised ML models** to detect fraudulent behavior in real time. It is cloud-ready with support for **Azure Blob**, **SQL Server**, and includes a **Power BI** dashboard for monitoring.

---

## 📁 Folder Structure
```bash
real-time-fraud-detection/
├── data/ # Raw, processed, simulated datasets
├── database/ # MS SQL schema setup
├── models/ # Saved Isolation Forest model
├── notebooks/ # EDA + model training
├── outputs/ # Plots, logs
├── dashboards/ # Power BI visuals
├── src/ # Stream simulator, fraud detection logic
├── app/ # Optional Streamlit UI
├── requirements.txt # Python dependencies
├── README.md # Project overview
├── .gitignore # Ignore sensitive/system files
```

---

## 📌 Key Features

- ✅ Simulated real-time transactions using Python
- ✅ Unsupervised anomaly detection using Isolation Forest
- ✅ MS SQL Server integration for storage
- ✅ Azure Blob support for cloud pipelines
- ✅ Power BI dashboard for anomaly trends
- ✅ Streamlit dashboard (optional)

---

## ⚙️ How to Run

1. **Clone Repo**
```bash
git clone https://github.com/Vanya54/real-time-fraud-detection.git
cd real-time-fraud-detection
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Simulate Stream**

```bash
python src/stream_simulator.py
```
4. **Run Flask Detector**

```bash
python src/fraud_detector.py
```

5. **(Optional) Launch Streamlit UI**

```bash
streamlit run app/streamlit_app.py
```
##📊 Power BI Dashboard
Live anomaly monitoring

Device-wise fraud breakdown

Location heatmaps

Anomaly trend timelines

##☁️ Azure Integration
Upload .csv files to Azure Blob Storage

Store structured data in Azure SQL

