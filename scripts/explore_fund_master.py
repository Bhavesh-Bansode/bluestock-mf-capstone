import pandas as pd
df=pd.read_csv("data/raw/01_fund_master.csv")

print("\nFund Houses:")
print(df["fund_house"].unique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nRisk Grades:")
print(df["risk_category"].unique())

print("\nNumber of Fund Houses:", df["fund_house"].nunique())
print("Number of Categories:", df["category"].nunique())
print("Number of Sub Categories:", df["sub_category"].nunique())
print("Number of Risk Grade:", df["risk_category"].nunique())

print("\nNow for AMFI Code : ")
print(df["amfi_code"].head())
