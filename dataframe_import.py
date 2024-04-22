import pandas as pd
import json
import xml.etree.ElementTree as ET
import pyarrow.parquet as pq
import openpyxl
import sqlite3
import mysql.connector
import psycopg2
import cx_Oracle
import snowflake.connector

def dataframe_import(file_type, file_path, **kwargs):
    """
    Load a file of specified type into a Pandas DataFrame.

    Supported file types:
    - 'json': JSON file
    - 'xml': XML file
    - 'parquet': Parquet file
    - 'csv': CSV file
    - 'excel': Excel file (both .xls and .xlsx formats)
    - 'txt': Text file (e.g., CSV-like data with custom delimiter)
    - 'sql': SQL query to fetch data from a database (SQLite, MySQL, PostgreSQL, Oracle, Snowflake)

    Parameters:
    file_type (str): Type of the input file ('json', 'xml', 'parquet', 'csv', 'excel', 'txt', 'sql').
    file_path (str): Path to the input file or SQL query (depending on file_type).
    **kwargs: Additional keyword arguments for database connection (e.g., host, user, password, database_name)
              required for 'sql' file_type.

    Returns:
    pd.DataFrame: DataFrame containing the loaded data from the input file or database query.
    """
    if file_type == 'json':
        with open(file_path, 'r') as file:
            data = json.load(file)
            df = pd.DataFrame(data)

    elif file_type == 'xml':
        tree = ET.parse(file_path)
        root = tree.getroot()

        data = []
        for child in root:
            row = {}
            for subchild in child:
                row[subchild.tag] = subchild.text
            data.append(row)

        df = pd.DataFrame(data)

    elif file_type == 'parquet':
        table = pq.read_table(file_path)
        df = table.to_pandas()

    elif file_type == 'csv':
        df = pd.read_csv(file_path)

    elif file_type == 'excel':
        excel_file = pd.ExcelFile(file_path)
        sheet_names = excel_file.sheet_names
        if len(sheet_names) > 1:
            # If multiple sheets are present, load the first sheet by default
            df = pd.read_excel(file_path, sheet_name=sheet_names[0])
        else:
            df = pd.read_excel(file_path)

    elif file_type == 'txt':
        # Assuming kwargs contain 'delimiter' parameter for custom delimiter (default is comma)
        delimiter = kwargs.get('delimiter', ',')
        df = pd.read_csv(file_path, delimiter=delimiter)

    elif file_type == 'sql':
        # Assuming kwargs contain 'connection_type' parameter for database type
        connection_type = kwargs.get('connection_type', 'sqlite') # If the key 'connection_type' does not exist in kwargs, the method returns the default value 'sqlite'.

        if connection_type == 'sqlite':
            conn = sqlite3.connect(kwargs['database_name'])
        elif connection_type == 'mysql':
            conn = mysql.connector.connect(
                host=kwargs['host'],
                user=kwargs['user'],
                password=kwargs['password'],
                database=kwargs['database_name']
            )
        elif connection_type == 'postgresql':
            conn = psycopg2.connect(
                host=kwargs['host'],
                user=kwargs['user'],
                password=kwargs['password'],
                database=kwargs['database_name']
            )
        elif connection_type == 'snowflake':
            conn = snowflake.connector.connect(
                account=kwargs['account'],
                warehouse=kwargs['warehouse'],
                database=kwargs['database'],
                user=kwargs['user'],
                password=kwargs['password']
            )
        else:
            raise ValueError(f"Unsupported database connection type: {connection_type}")

        # Execute SQL query and fetch data into DataFrame
        sql_query = file_path
        df = pd.read_sql(sql_query, conn)

        # Close database connection
        conn.close()

    else:
        raise ValueError(f"Unsupported file type: {file_type}. Please specify a valid file type.")

    return df