-- ========================================
-- DATA WAREHOUSE SCHEMA FOR FRAUD ANALYSIS
-- Database: FraudDetectionDWH
-- ========================================

-- Create DWH database
CREATE DATABASE FraudDetectionDWH;
GO

USE FraudDetectionDWH;
GO

-- =====================
-- DIMENSION TABLES
-- =====================

-- DimUser
CREATE TABLE DimUser (
    user_id VARCHAR(50) PRIMARY KEY,
    first_transaction_date DATETIME,
    location VARCHAR(100)
);
GO

-- DimDevice
CREATE TABLE DimDevice (
    device_type_code INT PRIMARY KEY,
    device_type_desc VARCHAR(50)
);
GO

-- DimLocation
CREATE TABLE DimLocation (
    location_code INT PRIMARY KEY,
    location_name VARCHAR(100),
    region VARCHAR(100)
);
GO

-- DimDate
CREATE TABLE DimDate (
    date_key INT PRIMARY KEY,
    full_date DATE,
    year INT,
    quarter INT,
    month INT,
    day INT,
    weekday_name VARCHAR(20)
);
GO

-- =====================
-- FACT TABLES
-- =====================

-- FactTransaction
CREATE TABLE FactTransaction (
    transaction_id INT PRIMARY KEY,
    date_key INT,
    user_id VARCHAR(50),
    device_type_code INT,
    location_code INT,
    amount DECIMAL(10, 2),
    amount_scaled FLOAT,
    is_anomaly BIT,
    anomaly_score FLOAT,
    detected_at DATETIME,
    
    FOREIGN KEY (date_key) REFERENCES DimDate(date_key),
    FOREIGN KEY (user_id) REFERENCES DimUser(user_id),
    FOREIGN KEY (device_type_code) REFERENCES DimDevice(device_type_code),
    FOREIGN KEY (location_code) REFERENCES DimLocation(location_code)
);
GO
