# Import necessary modules and functions
from dataframe_info import dataframe_info
from dataframe_imputation import dataframe_imputation
from dataframe_standardization import dataframe_standardization
from dataframe_visualization import dataframe_visualization
from dataframe_import import dataframe_import
from dataframe_export import dataframe_export

def main():
    # Example file paths and parameters
    file_path = 'your_file_path_here.csv'

    # Import data
    df = dataframe_import('csv', file_path)
    print("Data Imported\n", df.head())

    # Get data info
    info = dataframe_info(df)
    print("Data Info:\n", info)

    # Impute missing values
    df_imputed, imputed_columns, dropped_columns = dataframe_imputation(df)
    print("Imputation Complete. Imputed columns:", imputed_columns, "Dropped columns:", dropped_columns)

    # Standardize data
    df_standardized = dataframe_standardization(df_imputed)
    print("Standardization Complete\n", df_standardized.head())

    # Visualize data
    print("Visualizing Data")
    dataframe_visualization(df_standardized)

    # Export data
    success = dataframe_export(df_standardized, 'csv', file_path='processed_data.csv')
    print("Data Exported:", success)

if __name__ == "__main__":
    main()
