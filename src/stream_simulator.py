import pandas as pd
import time
import requests

# Simulated data source
df = pd.read_csv('data/simulation/simulated_transactions.csv')

# Simulated endpoint (local inference API or logging)
ENDPOINT = "http://localhost:8000/stream"

for _, row in df.iterrows():
    payload = row.to_dict()
    print(f"Sending: {payload}")
    # Simulate POST to API (could be fraud_detector)
    try:
        requests.post(ENDPOINT, json=payload)
    except:
        pass
    time.sleep(1)  # simulate 1 transaction/sec
