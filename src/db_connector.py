import pyodbc

def connect_to_sql():
    return pyodbc.connect(
        'DRIVER={SQL Server};SERVER=localhost;DATABASE=RealTimeFraudDetection;Trusted_Connection=yes;'
    )

def insert_transaction(tx):
    conn = connect_to_sql()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Transactions (transaction_id, timestamp, user_id, amount, location, device_type)
        VALUES (?, ?, ?, ?, ?, ?)
    """, tx['transaction_id'], tx['timestamp'], tx['user_id'], tx['amount'], tx['location'], tx['device_type'])

    conn.commit()
    conn.close()

def insert_anomaly(anomaly):
    conn = connect_to_sql()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Anomalies (transaction_id, anomaly_score, is_anomaly)
        VALUES (?, ?, ?)
    """, anomaly['transaction_id'], anomaly['score'], int(anomaly['is_anomaly']))

    conn.commit()
    conn.close()
