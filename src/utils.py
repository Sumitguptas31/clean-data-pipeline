import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    return df.drop_duplicates()

def data_summary(df):
    print("\nDataset Summary")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("\nMissing Values:")
    print(df.isnull().sum())

