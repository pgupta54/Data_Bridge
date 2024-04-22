import pandas as pd
from sklearn.impute import SimpleImputer

def dataframe_imputation(data, threshold=0.3):
    """
    Handle missing values in DataFrame by dropping or imputing columns.

    Parameters:
    data (pd.DataFrame): Input DataFrame containing the data.
    threshold (float): Threshold to determine when to drop a column (proportion of missing values).
    
    Returns:
    pd.DataFrame: Processed DataFrame after handling missing values.
    list: List of columns that were imputed.
    list: List of columns that were dropped.
    """
    # Calculate proportion of missing values for each column
    missing_counts = data.isnull().sum()
    missing_proportion = missing_counts / len(data)

    # Determine columns to drop based on missing value proportion
    columns_to_drop = missing_proportion[missing_proportion > threshold].index
    data_processed = data.drop(columns=columns_to_drop)
    dropped_columns = list(columns_to_drop)

    # Determine columns to impute based on remaining missing values
    columns_to_impute = missing_proportion[missing_proportion <= threshold].index
    imputed_columns = []

    # Impute missing values based on column data types and characteristics
    for col in columns_to_impute:
        if data_processed[col].dtype == 'object':
            # For categorical columns, impute using mode
            imputer = SimpleImputer(strategy='most_frequent')
        else:
            # For numeric columns, determine optimal imputation strategy based on data characteristics
            if data_processed[col].nunique() > 10:
                # If unique values > 10, use median (more robust against outliers)
                imputer = SimpleImputer(strategy='median')
            else:
                # Otherwise, use mean (for columns with limited unique values)
                imputer = SimpleImputer(strategy='mean')

        # Impute missing values in the selected column
        data_processed[col] = imputer.fit_transform(data_processed[[col]])
        imputed_columns.append((col, imputer.strategy))

    return data_processed, imputed_columns, dropped_columns

