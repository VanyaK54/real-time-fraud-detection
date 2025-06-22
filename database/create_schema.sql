-- Create Database
CREATE DATABASE RealTimeFraudDetection;
GO

USE RealTimeFraudDetection;
GO

-- Create Transactions Table
CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    timestamp DATETIME,
    user_id VARCHAR(50),
    amount DECIMAL(10,2),
    location VARCHAR(100),
    device_type VARCHAR(50)
);
GO

-- Create Processed Transactions Table (for ML pipeline)
CREATE TABLE TransactionsProcessed (
    transaction_id INT PRIMARY KEY,
    timestamp DATETIME,
    user_id VARCHAR(50),
    amount_scaled FLOAT,
    location_code INT,
    device_type_code INT
);
GO

-- Create Anomalies Table
CREATE TABLE Anomalies (
    id INT IDENTITY(1,1) PRIMARY KEY,
    transaction_id INT,
    anomaly_score FLOAT,
    is_anomaly BIT,
    detected_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (transaction_id) REFERENCES Transactions(transaction_id)
);
GO
