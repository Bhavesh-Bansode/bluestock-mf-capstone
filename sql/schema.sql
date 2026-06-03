CREATE TABLE dim_fund (
amfi_code INTEGER PRIMARY KEY,
fund_house TEXT,
scheme_name TEXT,
category TEXT,
sub_category TEXT,
plan TEXT,
launch_date DATE,
benchmark TEXT,
fund_manager TEXT,
risk_category TEXT,
sebi_category_code TEXT);

CREATE TABLE dim_date (
date_key INTEGER PRIMARY KEY,
full_date DATE,
year INTEGER,
quarter INTEGER,
month INTEGER,
day INTEGER);

CREATE TABLE fact_nav (
nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code INTEGER NOT NULL,
date_key INTEGER NOT NULL,
nav REAL NOT NULL,
FOREIGN KEY (amfi_code)REFERENCES dim_fund(amfi_code),
FOREIGN KEY (date_key)REFERENCES dim_date(date_key));

CREATE TABLE fact_transactions (
transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
investor_id INTEGER,
amfi_code INTEGER NOT NULL,
date_key INTEGER NOT NULL,
transaction_type TEXT,
amount_inr REAL,
state TEXT,
city TEXT,
city_tier TEXT,
age_group TEXT,
gender TEXT,
annual_income_lakh REAL,
payment_mode TEXT,
kyc_status TEXT,
FOREIGN KEY (amfi_code)REFERENCES dim_fund(amfi_code),
FOREIGN KEY (date_key)REFERENCES dim_date(date_key));

CREATE TABLE fact_performance (
performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code INTEGER NOT NULL,
return_1yr_pct REAL,
return_3yr_pct REAL,
return_5yr_pct REAL,
benchmark_3yr_pct REAL,
alpha REAL,
beta REAL,
sharpe_ratio REAL,
sortino_ratio REAL,
std_dev_ann_pct REAL,
max_drawdown_pct REAL,
aum_crore REAL,
expense_ratio_pct REAL,
morningstar_rating REAL,
risk_grade TEXT,
FOREIGN KEY (amfi_code)REFERENCES dim_fund(amfi_code));

CREATE TABLE fact_aum (
aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
date_key INTEGER NOT NULL,
fund_house TEXT,
aum_lakh_crore REAL,
aum_crore REAL,
num_schemes INTEGER,
FOREIGN KEY (date_key)REFERENCES dim_date(date_key));