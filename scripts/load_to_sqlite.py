import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

processed_folder = Path("data/processed")

csv_files = list(
    processed_folder.glob("*.csv")
)

for file in csv_files:

    table_name = file.stem

    df = pd.read_csv(file)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"{table_name} loaded",
        f"({len(df)} rows)"
    )

print("\nAll cleaned datasets loaded")