# 🎬 Bike Sales in Europe

<img src="https://static01.nyt.com/images/2023/09/01/multimedia/00vanmoof-sale-print-jkqw/00vanmoof-sale-hfo-jkqw-videoSixteenByNineJumbo1600.jpg" alt="Bike Sales in Europe">

## 📊 Project Overview

This project conducts an in-depth analysis of the Bike Sales in Europe dataset using advanced data processing techniques and robust quality assurance methods. It showcases the implementation of Apache Airflow for ETL processes and Great Expectations for comprehensive data validation, providing valuable insights into European bike sales patterns and trends.

## ⏳ Features

- **ETL Pipeline**: Automated data extraction, transformation, and loading using Apache Airflow.
- **Data Validation**: Comprehensive data quality checks using Great Expectations.
- **Elasticsearch Integration**: Efficient data storage and retrieval for analytics.
- **Visualization**: Interactive dashboards for data exploration and presentation.
- **Scalable Architecture**: Designed to handle large datasets efficiently.

## 🛠 Technologies Used

- ![Apache Airflow](https://img.shields.io/badge/-Apache%20Airflow-017CEE?style=flat-square&logo=Apache%20Airflow&logoColor=white) Apache Airflow
- ![Great Expectations](https://img.shields.io/badge/-Great%20Expectations-3C4C65?style=flat-square&logo=Great%20Expectations&logoColor=white) Great Expectations
- ![Elasticsearch](https://img.shields.io/badge/-Elasticsearch-005571?style=flat-square&logo=Elasticsearch&logoColor=white) Elasticsearch
- ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=Python&logoColor=white) Python
- ![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=Pandas&logoColor=white) Pandas
- ![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat-square&logo=PostgreSQL&logoColor=white) PostgreSQL
- ![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=Docker&logoColor=white) Docker
- ![Jupyter](https://img.shields.io/badge/-Jupyter-F37626?style=flat-square&logo=Jupyter&logoColor=white) Jupyter Notebooks

## 📁 Project Structure

```
amazon-prime-user-analysis/
│
├── dashboard-kibana/
│   ├── conclusions.png
│   ├── dashboard.jpg
│   ├── introduction & objective.png
│   ├── plot & insight 01.png
│   ├── plot & insight 02.png
│   ├── plot & insight 03.png
│   ├── plot & insight 04.png
│   ├── plot & insight 05.png
│   └── plot & insight 06.png
│
├── dataset/
│   ├── dataset_cleaned.csv
│   └── dataset_raw.csv
│
├── images/
│   ├── airflow-2.jpg
│   ├── airflow.jpg
│   └── amazon-prime.jpg
│
├── validation_results/
│   ├── amazon_prime_userbase_expectations.json
│   └── validation_results.json
│
├── automation_script_DAG.py
├── data-validation-great-expectation.ipynb
├── posgresql-query.txt
└── README.md
```

## 📊 Dataset

The dataset used in this project is the Amazon Prime Userbase Dataset, available on Kaggle:
[Bike Sales in EUR Dataset](https://www.kaggle.com/datasets/sadiqshah/bike-sales-in-europe)

## 🗄️ Database Setup

The project uses PostgreSQL for data storage. Here's the SQL query used to create the database and table:

```sql
CREATE DATABASE milestone3;

CREATE TABLE table_m3 (
    "ID" SERIAL PRIMARY KEY,              -- Kolom auto-increment
    "Date" date,                          -- Kolom tanggal
    "Day" INT,                            -- Kolom hari
    "Month" VARCHAR(20),                  -- Kolom bulan (dalam bentuk teks)
    "Year" INT,                           -- Kolom tahun
    "Customer Age" INT,                   -- Kolom umur pelanggan
    "Age Group" VARCHAR(20),              -- Kelompok umur (teks)
    "Customer Gender" VARCHAR(10),        -- Gender pelanggan
    "Country" VARCHAR(50),                -- Negara pelanggan
    "State" VARCHAR(50),                  -- Negara bagian
    "Product Category" VARCHAR(50),       -- Kategori produk
    "Sub_Category" VARCHAR(50),           -- Sub-kategori produk
    "Product" VARCHAR(100),               -- Produk
    "Order Quantity" INT,                 -- Kuantitas pesanan
    "Unit Cost" INT,                      -- Biaya per unit
    "Unit Price" INT,                     -- Harga per unit
    "Profit" INT,                         -- Profit dari transaksi
    "Cost" INT,                           -- Total biaya
    "Revenue" INT                         -- Total revenue
);

COPY table_m3(
    "ID",
    "Date",
    "Day",
    "Month",
    "Year",
    "Customer Age",
    "Age Group",
    "Customer Gender",
    "Country",
    "State",
    "Product Category",
    "Sub_Category",
    "Product",
    "Order Quantity",
    "Unit Cost",
    "Unit Price",
    "Profit",
    "Cost",
    "Revenue"
) FROM '/tmp/sales_processed.csv' 
DELIMITER ',' 
CSV HEADER;
```

## 🔍 Data Validation

Great Expectations is used to ensure data quality. Key expectations include:

- Primary key must be unique
- Date year must start in 2011 and max year 2016
- Column must contain one of the following categories
- etc ...

> 💡 **Note:** For a comprehensive view of the data validation process and all expectations, please refer to the `P2M3_danisa_GX.ipynb` notebook in the project root directory. This notebook contains detailed explanations, code, and results of the Great Expectations implementation.

## 📈 Visualization

The project includes interactive dashboards created using Kibana. These visualizations provide insights into:

- 🧾 Average order quantity
- 🧔👧 Gender Preferences
- 👫 Age Groups 
- 🇪🇺 Average State Order Quantity
- 💰 Profit by Products Categories
- 📈 Revenue by Year

## 🚀 Running the ETL Pipeline

To run the ETL pipeline:

1. Ensure Airflow is running
2. Navigate to the Airflow UI (default: http://localhost:8080)
3. Trigger the `P2M3_danisa_DAG.py` DAG