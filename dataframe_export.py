import pandas as pd
import boto3  # For AWS S3 integration
from azure.storage.blob import BlobServiceClient  # For Azure Blob Storage integration
from google.cloud import storage  # For Google Cloud Storage integration
import sqlalchemy  # For SQL database integration

def dataframe_export(df, export_type, **kwargs):
    """
    Export processed data from a Pandas DataFrame to specified formats or destinations.

    Supported export types:
    - 'csv': Export data to CSV file.
    - 'excel': Export data to Excel file (XLSX format).
    - 'json': Export data to JSON file.
    - 'sql': Upload data to an SQL database table.
    - 'aws_s3': Upload data to AWS S3 bucket.
    - 'azure_blob': Upload data to Azure Blob Storage container.
    - 'gcp_storage': Upload data to Google Cloud Storage bucket.

    Parameters:
    df (pd.DataFrame): DataFrame containing the processed data to be exported.
    export_type (str): Type of export operation ('csv', 'excel', 'json', 'sql', 'aws_s3', 'azure_blob', 'gcp_storage').
    **kwargs: Additional keyword arguments specific to each export type (e.g., file_path, table_name, bucket_name, object_name).

    Returns:
    bool: True if export operation is successful, False otherwise.
    """
    try:
        if export_type == 'csv':
            file_path = kwargs.get('file_path', 'exported_data.csv')
            df.to_csv(file_path, index=False)
            return True

        elif export_type == 'excel':
            file_path = kwargs.get('file_path', 'exported_data.xlsx')
            df.to_excel(file_path, index=False)
            return True

        elif export_type == 'json':
            file_path = kwargs.get('file_path', 'exported_data.json')
            df.to_json(file_path, orient='records')
            return True

        elif export_type == 'sql':
            dialect = kwargs['dialect']
            if dialect == 'snowflake':
                connection_string = (
                    f"snowflake://{kwargs['username']}:{kwargs['password']}@{kwargs['account_name']}/{kwargs['database_name']}/{kwargs['schema_name']}?warehouse={kwargs['warehouse_name']}"
                )
            elif dialect == 'postgresql':
                connection_string = (
                    f"postgresql://{kwargs['username']}:{kwargs['password']}@{kwargs['host']}:{kwargs['port']}/"
                    f"{kwargs['database_name']}"
                )
            elif dialect == 'mysql':
                connection_string = (
                    f"mysql+mysqlconnector://{kwargs['username']}:{kwargs['password']}@{kwargs['host']}:{kwargs['port']}/"
                    f"{kwargs['database_name']}"
                )
            elif dialect == 'sqlite':
                connection_string = f"sqlite:///{kwargs['database_name']}"

            engine = sqlalchemy.create_engine(connection_string)
            df.to_sql(kwargs['table_name'], con=engine, if_exists='replace', index=False)
            return True        
        elif export_type == 'aws_s3':
            bucket_name = kwargs['bucket_name']
            object_name = kwargs.get('object_name', 'exported_data.csv')
            csv_buffer = df.to_csv(index=False).encode()
            s3 = boto3.client('s3')
            s3.put_object(Bucket=bucket_name, Key=object_name, Body=csv_buffer)
            return True

        elif export_type == 'azure_blob':
            connection_string = kwargs['connection_string']
            blob_service_client = BlobServiceClient.from_connection_string(connection_string)
            blob_client = blob_service_client.get_blob_client(container=kwargs['container_name'], blob=kwargs['blob_name'])
            blob_client.upload_blob(df.to_csv(index=False))
            return True

        elif export_type == 'gcp_storage':
            bucket_name = kwargs['bucket_name']
            blob_name = kwargs.get('blob_name', 'exported_data.csv')
            storage_client = storage.Client()
            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(blob_name)
            blob.upload_from_string(df.to_csv(index=False))
            return True

        else:
            raise ValueError(f"Unsupported export type: {export_type}. Please specify a valid export type.")

    except Exception as e:
        print(f"Error occurred during export: {e}")
        return False
    