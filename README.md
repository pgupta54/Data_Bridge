# DATA BRIDGE LIBRARY PACKAGE

# Data Engineering Python Library

This Python library provides tools for importing, cleaning, preprocessing, exploring, transforming, and exporting data effortlessly.


## Features

- **Data Import**
- **Data Cleaning and Preprocessing**
- **Interactive Data Exploration and Visualization**
- **Data Transformation and Reshaping**
- **Data Integration and Export**

## Installation

Install all dependencies using pip:

```bash
pip install pandas numpy matplotlib seaborn simplejson pyarrow openpyxl mysql-connector-python psycopg2-binary cx-Oracle snowflake-connector-python boto3 azure-storage-blob google-cloud-storage sqlalchemy
```

## Functions

### 1. `dataframe_info`

#### Purpose
Provides details about a DataFrame.

#### Arguments
- `dataframe_path` (str): Path to the DataFrame file.

#### Returns
- `dict`: A dictionary containing various details of the DataFrame.

#### Example Usage
```python
from your_library import dataframe_info

info = dataframe_info('path_to_dataframe.csv')
print(info)
```


### 2. `dataframe_imputation`

#### Purpose
Handles missing values in a DataFrame by dropping or imputing columns based on a specified threshold.

#### Arguments
- `data` (pd.DataFrame): Input DataFrame containing the data.
- `threshold` (float): Threshold to determine when to drop a column (proportion of missing values).

#### Returns
- `pd.DataFrame`: Processed DataFrame after handling missing values.
- `list`: List of columns that were imputed.
- `list`: List of columns that were dropped.

#### Example Usage
```python
from your_library import dataframe_imputation

df_processed, imputed_cols, dropped_cols = dataframe_imputation(df, threshold=0.3)
print("Processed DataFrame:", df_processed)
print("Imputed Columns:", imputed_cols)
print("Dropped Columns:", dropped_cols)
```


### 3. `dataframe_standardization`

#### Purpose
Standardizes (scales) numerical columns of a DataFrame using either z-score or min-max scaling.

#### Arguments
- `df` (pd.DataFrame): Input DataFrame containing numerical columns to be standardized.
- `standardization_type` (str): Type of standardization to apply: 'z-score' or 'min-max'.

#### Returns
- `pd.DataFrame`: Standardized DataFrame.


#### Example Usage
```python
from your_library import dataframe_standardization

df_standardized = dataframe_standardization(df, standardization_type='z-score')
print("Standardized DataFrame:", df_standardized)
```


### 4. `dataframe_visualization`

#### Purpose
Generates various data visualizations (histograms, pair plots, box plots, bar charts) to explore the DataFrame.

#### Arguments
- `df` (pd.DataFrame): Input DataFrame containing the data to visualize.

#### Returns
- None (Plots are displayed interactively).


#### Example Usage
```python
from your_library import dataframe_visualization

dataframe_visualization(df)
```



### 5. `dataframe_import`

#### Purpose
Loads data from different file formats or databases into a Pandas DataFrame.


#### Arguments
- `file_type` (str): Type of the input data ('json', 'xml', 'parquet', 'csv', 'excel', 'txt', 'sql').
- `file_path` (str): Path to the input file or SQL query.
- `**kwargs`: Additional keyword arguments for database connection (e.g., host, user, password, database_name) required for 'sql' file_type.

#### Returns
- `pd.DataFrame`: DataFrame containing the loaded data.


#### Example Usage
```python
from your_library import dataframe_import

df = dataframe_import('csv', 'path_to_file.csv')
print(df.head())
```


### 6. `dataframe_export`

#### Purpose
Exports processed data from a DataFrame to various file formats or destinations.

#### Arguments
- `df` (pd.DataFrame): DataFrame containing the processed data to be exported.
- `export_type` (str): Type of export operation ('csv', 'excel', 'json', 'sql', 'aws_s3', 'azure_blob', 'gcp_storage').
- `**kwargs`: Additional keyword arguments specific to each export type.

#### Returns
- `bool`: True if export operation is successful, False otherwise.


#### Example Usage
```python
from your_library import dataframe_export

success = dataframe_export(df, 'csv', file_path='exported_data.csv')
print("Export successful:", success)
```





