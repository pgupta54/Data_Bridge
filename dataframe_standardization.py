def dataframe_standardization(df, standardization_type='z-score'):
    """
    Perform standardization (scaling) on numerical columns of a DataFrame.

    Parameters:
    df (pd.DataFrame): Input DataFrame containing numerical columns to be standardized.
    standardization_type (str): Type of standardization to apply:
        - 'z-score': Standardization (subtract mean and divide by standard deviation).
        - 'min-max': Min-max scaling (scale to a specified range, default 0-1).

    Returns:
    pd.DataFrame: Standardized DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")

    # Select numerical columns
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()

    if not numeric_columns:
        raise ValueError("No numerical columns found in the DataFrame.")

    # Apply standardization based on the specified type
    if standardization_type == 'z-score':
        df[numeric_columns] = (df[numeric_columns] - df[numeric_columns].mean()) / df[numeric_columns].std()
    elif standardization_type == 'min-max':
        df[numeric_columns] = (df[numeric_columns] - df[numeric_columns].min()) / (df[numeric_columns].max() - df[numeric_columns].min())
    else:
        raise ValueError(f"Unsupported standardization type: {standardization_type}. Use 'z-score' or 'min-max'.")

    return df