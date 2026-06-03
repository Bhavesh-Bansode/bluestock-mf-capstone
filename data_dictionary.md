# Data Dictionary

## Dataset: fund_master

| Column             | Data Type | Description                   |
| ------------------ | --------- | ----------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme code       |
| fund_house         | Text      | Asset Management Company name |
| scheme_name        | Text      | Mutual fund scheme name       |
| category           | Text      | Fund category                 |
| sub_category       | Text      | Fund sub-category             |
| plan               | Text      | Direct/Regular plan           |
| launch_date        | Date      | Scheme launch date            |
| benchmark          | Text      | Benchmark index               |
| expense_ratio_pct  | Real      | Expense ratio percentage      |
| exit_load_pct      | Real      | Exit load percentage          |
| min_sip_amount     | Real      | Minimum SIP investment amount |
| min_lumpsum_amount | Real      | Minimum lump sum investment   |
| fund_manager       | Text      | Fund manager name             |
| risk_category      | Text      | Risk category                 |
| sebi_category_code | Text      | SEBI classification code      |
-----------------------------------------------------------------

## Dataset: nav_history

| Column    | Data Type | Description       |
| --------- | --------- | ----------------- |
| amfi_code | Integer   | Scheme identifier |
| date      | Date      | NAV date          |
| nav       | Real      | Net Asset Value   |
---------------------------------------------

## Dataset: aum

| Column         | Data Type | Description       |
| -------------- | --------- | ----------------- |
| date           | Date      | Reporting date    |
| fund_house     | Text      | Fund house        |
| aum_lakh_crore | Real      | AUM in lakh crore |
| aum_crore      | Real      | AUM in crore      |
| num_schemes    | Integer   | Number of schemes |
--------------------------------------------------

## Dataset: sip_data

| Column                    | Data Type | Description                    |
| ------------------------- | --------- | ------------------------------ |
| month                     | Text      | Reporting month                |
| sip_inflow_crore          | Real      | SIP inflow amount              |
| active_sip_accounts_crore | Real      | Active SIP accounts            |
| new_sip_accounts_lakh     | Real      | New SIP accounts               |
| sip_aum_lakh_crore        | Real      | SIP AUM                        |
| yoy_growth_pct            | Real      | Year-on-year growth percentage |
--------------------------------------------------------------------------

## Dataset: category_flow

| Column           | Data Type | Description       |
| ---------------- | --------- | ----------------- |
| month            | Text      | Reporting month   |
| category         | Text      | Fund category     |
| net_inflow_crore | Real      | Net inflow amount |
----------------------------------------------------

## Dataset: folio_data

| Column              | Data Type | Description     |
| ------------------- | --------- | --------------- |
| month               | Text      | Reporting month |
| total_folios_crore  | Real      | Total folios    |
| equity_folios_crore | Real      | Equity folios   |
| debt_folios_crore   | Real      | Debt folios     |
| hybrid_folios_crore | Real      | Hybrid folios   |
| others_folios_crore | Real      | Other folios    |
-----------------------------------------------------

## Dataset: scheme_performance

| Column             | Data Type | Description                   |
| ------------------ | --------- | ----------------------------- |
| amfi_code          | Integer   | Scheme identifier             |
| return_1yr_pct     | Real      | One-year return               |
| return_3yr_pct     | Real      | Three-year return             |
| return_5yr_pct     | Real      | Five-year return              |
| alpha              | Real      | Alpha measure                 |
| beta               | Real      | Beta measure                  |
| sharpe_ratio       | Real      | Sharpe ratio                  |
| sortino_ratio      | Real      | Sortino ratio                 |
| std_dev_ann_pct    | Real      | Annualized standard deviation |
| max_drawdown_pct   | Real      | Maximum drawdown              |
| aum_crore          | Real      | Scheme AUM                    |
| expense_ratio_pct  | Real      | Expense ratio                 |
| morningstar_rating | Integer   | Morningstar rating            |
| risk_grade         | Text      | Risk grade                    |
------------------------------------------------------------------

## Dataset: investor_transactions

| Column             | Data Type | Description             |
| ------------------ | --------- | ----------------------- |
| investor_id        | Integer   | Investor identifier     |
| transaction_date   | Date      | Transaction date        |
| amfi_code          | Integer   | Scheme identifier       |
| transaction_type   | Text      | SIP/Lumpsum/Redemption  |
| amount_inr         | Real      | Transaction amount      |
| state              | Text      | Investor state          |
| city               | Text      | Investor city           |
| city_tier          | Text      | City classification     |
| age_group          | Text      | Investor age group      |
| gender             | Text      | Investor gender         |
| annual_income_lakh | Real      | Annual income           |
| payment_mode       | Text      | Payment method          |
| kyc_status         | Text      | KYC verification status |
------------------------------------------------------------

## Dataset: portfolio_holdings

| Column            | Data Type | Description              |
| ----------------- | --------- | ------------------------ |
| amfi_code         | Integer   | Scheme identifier        |
| stock_symbol      | Text      | Stock symbol             |
| stock_name        | Text      | Company name             |
| sector            | Text      | Industry sector          |
| weight_pct        | Real      | Portfolio weight         |
| market_value_cr   | Real      | Market value             |
| current_price_inr | Real      | Current stock price      |
| portfolio_date    | Date      | Portfolio reporting date |
------------------------------------------------------------

## Dataset: market_index

| Column      | Data Type | Description         |
| ----------- | --------- | ------------------- |
| date        | Date      | Market date         |
| index_name  | Text      | Market index name   |
| close_value | Real      | Closing index value |
-------------------------------------------------

