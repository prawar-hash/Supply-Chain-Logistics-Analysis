import pandas as pd
from pathlib import Path

file_path = Path("../dataset/clean_supply_chain.csv")

df = pd.read_csv(file_path)

print("\n--- CLEANED DATASET ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum()[df.isnull().sum() > 0])

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- SAMPLE DATA ---")
print(df.head().to_string())