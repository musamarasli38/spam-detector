import pandas as pd
import os
from glob import glob

def load_data(data_dir):
    # csv laden in dataframe
    all_files = glob(os.path.join(data_dir, "*.csv"))
    df_list = [pd.read_csv(f) for f in all_files]
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df

def preprocess_data(df):
    # datum naar datetime converteren
    if 'DATE' in df.columns:
        df['DATE'] = pd.to_datetime(df['DATE'])
    # cleaning: lowercase vervangen van whitespace
    df['CONTENT'] = df['CONTENT'].str.lower().str.replace(r'\W', ' ', regex=True)
    df.dropna(inplace=True)
    return df
