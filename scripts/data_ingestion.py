import pandas as pd
from pathlib import Path

folder = Path("data/raw")

files = list(folder.glob("*.csv"))

print("Number of files found:", len(files))

for file in files:
    print("\n","="*100)
    print("Reading file:", file.name)

    df = pd.read_csv(file)

    print("\nShape of File :")
    print(df.shape)

    print("\nInformation of File:")
    print(df.dtypes)

    print("\nFirst 5 Data:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())