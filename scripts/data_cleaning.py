import pandas as pd

print("Cleaning nav_history.csv...")
print("\nReading NAV history")
nav_df = pd.read_csv("data/raw/02_nav_history.csv")

#Row counting
original_rows = len(nav_df)

print("\nChanging date format in NAV history")
nav_df["date"] = pd.to_datetime(nav_df["date"])

print("\nSorting Values")
nav_df = nav_df.sort_values(by=["amfi_code", "date"])

print("\nDropping Duplicates")
nav_df = nav_df.drop_duplicates()

print("\nValidating NAV>0")
nav_df = nav_df[nav_df["nav"] > 0]


print("\nForward fill NAV values")
nav_df["nav"] = nav_df.groupby("amfi_code")["nav"].ffill()

#Checking removed rows
final_rows = len(nav_df)

print("Original Rows:", original_rows)
print("Final Rows:", final_rows)
print("Rows Removed:", original_rows - final_rows)

print("\nSaving Clean Files")
nav_df.to_csv("data/processed/02_nav_history_clean.csv",index=False)

print("nav_history cleaned successfully")

###################################################################################################################################################################

print("\nCleaning investor_transactions.csv...")

txn_df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("\nChanging date format in Investor Transaction")
txn_df["transaction_date"] = pd.to_datetime(txn_df["transaction_date"])

print("\nStandardisation of transaction_type in Investor Transaction")
txn_df["transaction_type"] = (txn_df["transaction_type"].str.strip().str.title())

print("\nValidating amount_inr>0")
txn_df = txn_df[txn_df["amount_inr"] > 0]


valid_kyc = ["Verified", "Pending"]

txn_df = txn_df[txn_df["kyc_status"].isin(valid_kyc)]

txn_df.to_csv("data/processed/08_investor_transactions_clean.csv",index=False)

print("investor_transactions cleaned")

################################################################################################################################

print("\nCleaning scheme_performance.csv...")

perf_df = pd.read_csv("data/raw/07_scheme_performance.csv")

return_cols = ["return_1yr_pct","return_3yr_pct","return_5yr_pct"]

for col in return_cols:
    perf_df[col] = pd.to_numeric(perf_df[col],errors="coerce")


perf_df["expense_ratio_pct"] = pd.to_numeric(perf_df["expense_ratio_pct"],errors="coerce")


anomalies = perf_df[(perf_df["return_1yr_pct"] > 100) | (perf_df["return_1yr_pct"] < -100)]

print("Suspicious Return Records:",len(anomalies))

invalid_expense = perf_df[(perf_df["expense_ratio_pct"] < 0.1) | (perf_df["expense_ratio_pct"] > 2.5)]

print("Invalid Expense Ratios:",len(invalid_expense))

perf_df.to_csv("data/processed/07_scheme_performance_clean.csv",index=False)

print("scheme_performance cleaned")

###############################################################################################################################

from pathlib import Path

raw_folder = Path("data/raw")
processed_folder = Path("data/processed")

processed_folder.mkdir(exist_ok=True)

skip_files = [
    "02_nav_history.csv",
    "08_investor_transactions.csv",
    "07_scheme_performance.csv"
]

for file in raw_folder.glob("*.csv"):

    if file.name in skip_files:
        continue

    print(f"\nCleaning {file.name}...")

    df = pd.read_csv(file)

    original_rows = len(df)
    df = df.drop_duplicates()
    df.columns = df.columns.str.strip()
    for col in df.columns:
        if "date" in col.lower():
            df[col] = pd.to_datetime(df[col],errors="coerce")
            df[col] = df[col].dt.strftime("%Y-%m-%d")
    print("\nMissing Values:")
    print(df.isnull().sum())
    output_name = file.stem + "_clean.csv"
    df.to_csv(processed_folder / output_name,index=False)
