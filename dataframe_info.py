import pandas as pd

def dataframe_info(dataframe_path):
    """
    Function to read a DataFrame from a given path and provide details about it.
    
    Args:
        dataframe_path (str): Path to the DataFrame file.
        
    Returns:
        dict: A dictionary containing various details of the DataFrame.
    """
    # Read the DataFrame from the specified path
    try:
        df = pd.read_csv(dataframe_path)
    except FileNotFoundError:
        return {"error": "File not found"}
    except pd.errors.ParserError:
        return {"error": "Error parsing DataFrame"}
    
    # Get total number of rows and columns
    num_rows, num_cols = df.shape
    
    # Get column types
    column_types = df.dtypes
    
    # Identify numeric and string columns
    numeric_columns = column_types[column_types.apply(lambda x: pd.api.types.is_numeric_dtype(x))].index.tolist()
    string_columns = column_types[column_types.apply(lambda x: pd.api.types.is_string_dtype(x))].index.tolist()
    
    # Get total null values in each column
    null_counts = df.isnull().sum()
    
    # Get list of columns with null values
    columns_with_nulls = null_counts[null_counts > 0].index.tolist()
    
    # Prepare dictionary to store details
    details = {
        "total_rows": num_rows,
        "total_columns": num_cols,
        "numeric_columns": numeric_columns,
        "string_columns": string_columns,
        "null_values_per_column": null_counts.to_dict(),
        "columns_with_null_values": columns_with_nulls
    }
    
    return details

