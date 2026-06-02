import requests
import pandas as pd

funds = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in funds.items():

    print(f"\nFetching {fund_name}...")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = f"data/raw/{fund_name}.csv"

        nav_df.to_csv(file_name, index=False)

        print("Saved:", file_name)

    else:

        print("Failed for:", fund_name)