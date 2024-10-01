import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

import pandas as pd
import psycopg2 as db
from elasticsearch import Elasticsearch

# Function to query PostgreSQL
def queryPostgresql():
    '''
    Fetches data from the PostgreSQL database and saves it to a CSV file.

    This function connects to the PostgreSQL database using a connection string,
    executes a SQL query to retrieve all records from the `table_m3`, and saves
    the result as a CSV file. Finally, it closes the database connection.
    '''
    # Connect to the PostgreSQL database
    conn_string = "dbname='milestone3' host='postgres' user='airflow' password='airflow'"
    conn = db.connect(conn_string)

    # Select data using SQL query
    df = pd.read_sql("SELECT * FROM table_m3", conn)

    # Save data to CSV
    df.to_csv('/opt/airflow/dags/P2M3_danisa_data_raw.csv', index=False)

    # Close the database connection
    conn.close()
    print("-------Data Saved------")


# Function to clean data
def cleaningData():
    '''
    Cleans the fetched data by dropping duplicates, handling missing values, 
    and normalizing column names.

    This function reads the raw data from a CSV file, removes any duplicate rows,
    ensures that column names are in lowercase and spaces are replaced with underscores,
    drops rows with missing values, and saves the cleaned data to a new CSV file.
    '''
    # Read data after fetch from PostgreSQL
    df_clean = pd.read_csv('/opt/airflow/dags/P2M3_danisa_data_raw.csv')

    # Drop duplicates
    df_clean = df_clean.drop_duplicates()

    # Lowercase columns
    df_clean.columns = df_clean.columns.str.lower()

    # Replace spaces with underscores in column names
    df_clean.columns = df_clean.columns.str.replace(" ", "_")

    # Drop rows with missing data
    df_clean = df_clean.dropna()

    # Save cleaned data to CSV
    df_clean.to_csv('/opt/airflow/dags/P2M3_danisa_data_clean.csv', index=False)

    print("-------Data Cleaning------")


# Function to insert data into Elasticsearch
def insertElasticsearch():
    '''
    Inserts cleaned data into Elasticsearch.

    This function connects to the Elasticsearch service, reads the cleaned data 
    from a CSV file, and inserts each row into an Elasticsearch index called `milestone3`.
    '''
    # Connect to Elasticsearch
    es = Elasticsearch('http://elasticsearch:9200')

    # Read cleaned data from CSV
    df = pd.read_csv('/opt/airflow/dags/P2M3_danisa_data_clean.csv')

    # Insert data into Elasticsearch
    for i, r in df.iterrows():
        doc = r.to_json()
        res = es.index(index="milestone3", body=doc)
        print(res)


with DAG('milestone3',
        start_date= dt.datetime(2024, 9, 12),
        schedule_interval= '30 6 * * *',  # Run every 06.30 AM
         ) as dag:

    # Task to query PostgreSQL
    getData = PythonOperator(task_id='QueryPostgreSQL',
                             python_callable=queryPostgresql)

    # Task to clean data
    cleanData = PythonOperator(task_id='CleanData',
                               python_callable=cleaningData)

    # Task to insert data into Elasticsearch
    insertData = PythonOperator(task_id='InsertDataElasticsearch',
                                python_callable=insertElasticsearch)

# Define task flow
getData >> cleanData >> insertData