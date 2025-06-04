# Simple Script to download the e-commerce dataset
# Script by: Aly Kaamoush
# Project Name: ecommerce-analytics-project
# Date: June 04, 2025

import pandas as pd
import os

def dowmload_ecommerce_data():
    print("Downloading e-commerce dataset...")

    # Create data folser if they don't exist
    os.makedirs('data/raw', exist_ok=True)

    # Download the dataset
    url= "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"

    try:
        # Read the excel file directly from url
        df = pd.read_excel(url)

        # Save it to data folder
        df.to_excel('data/raw/online_retail.xlsx', index=False)

        print("Success! Dataset downloaded and saved.")
        print(f"Dataset contains {len(df):,} rows and {len(df.columns)} columns")
        print(f"Saved to: data/raw/online_retail.xlsx")

        # Show us what the data looks like
        print("\n Here's our data looks like:")
        print(df.head())

        print("\n Column names:")
        for i, col in enumerate(df.columns, 1):
            print(f"   {i}. {col}")

    except Exception as e:
        print(f"Error: {e}")
        print("Try checking your internet connection and run again.")
if __name__ == "__main__":
    dowmload_ecommerce_data()        