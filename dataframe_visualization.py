import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def dataframe_visualization(df):
    """
    Automatically generate data visualizations for exploration.

    Parameters:
    df (pd.DataFrame): Input DataFrame containing the data to visualize.

    Returns:
    None
    """
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")

    # Generate histograms for all numerical columns
    numerical_columns = df.select_dtypes(include=[np.number]).columns
    for col in numerical_columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.show()

    # Generate pair plot for numerical columns
    sns.pairplot(df.select_dtypes(include=[np.number]))
    plt.show()

    # Generate box plots for numerical columns
    for col in numerical_columns:
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=df[col])
        plt.title(f'Box plot of {col}')
        plt.show()

    # Generate bar charts for categorical columns
    categorical_columns = df.select_dtypes(exclude=[np.number]).columns
    for col in categorical_columns:
        plt.figure(figsize=(8, 6))
        sns.countplot(x=df[col], order=df[col].value_counts().index)
        plt.title(f'Bar chart of {col}')
        plt.xticks(rotation=45)
        plt.show()

