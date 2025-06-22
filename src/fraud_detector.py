import pandas as pd
from joblib import load
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)
model = load('models/isolation_forest_model.pkl')

@app.route('/stream', methods=['POST'])
def detect():
    tx = request.get_json()
    
    # Simple encoding (should match training logic)
    location_map = {'Toronto': 3, 'Calgary': 1, 'Montreal': 2, 'Vancouver': 0, 'Ottawa': 4, 'Edmonton': 5}
    device_map = {'Mobile': 2, 'Web': 1, 'POS': 0, 'ATM': 3}

    try:
        location_code = location_map.get(tx['location'], -1)
        device_type_code = device_map.get(tx['device_type'], -1)
        amount_scaled = float(tx['amount']) / 10000

        features = [[amount_scaled, location_code, device_type_code]]
        score = model.decision_function(features)[0]
        is_anomaly = model.predict(features)[0] == -1

        print(f"[{datetime.datetime.now()}] Score: {score:.4f} | Anomaly: {is_anomaly}")

        return jsonify({
            "transaction_id": tx['transaction_id'],
            "score": score,
            "is_anomaly": bool(is_anomaly)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(port=8000)

