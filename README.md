# Bluestock Mutual Fund Analytics Capstone Project

## Project Overview

This project is an end-to-end Mutual Fund Analytics Platform developed to analyze, visualize, and derive insights from mutual fund data. The project covers the complete data lifecycle, including data ingestion, cleaning, database management, exploratory data analysis, performance analytics, risk analysis, dashboard development, forecasting, portfolio optimization, and automation.

The solution enables investors and analysts to evaluate fund performance, understand investor behavior, monitor market trends, and generate actionable investment insights through interactive dashboards and analytical models.

---

## Business Problem

Mutual fund investors often face challenges in evaluating fund performance, comparing investment options, understanding risk levels, and identifying suitable funds based on their investment goals.

The objective of this project is to build a comprehensive analytics platform that simplifies mutual fund analysis through data engineering, business intelligence, and advanced analytics techniques.

---

## Project Objectives

* Build an automated ETL pipeline for mutual fund data.
* Store and manage data using a structured SQLite database.
* Perform data cleaning and validation.
* Conduct exploratory data analysis (EDA).
* Calculate key performance metrics such as CAGR, Sharpe Ratio, Sortino Ratio, Alpha, Beta, and Maximum Drawdown.
* Develop interactive Power BI and Streamlit dashboards.
* Perform advanced risk analysis using VaR and CVaR.
* Implement portfolio optimization and NAV forecasting models.
* Automate reporting and data update workflows.

---

## Data Sources

The project utilizes multiple datasets, including:

* Fund Master Data
* NAV History
* AUM Data by Fund House
* Investor Transactions
* Monthly SIP Inflow Data
* Category Inflows
* Industry Folio Count
* Scheme Performance Count
* Portfolio Holdings
* Benchmark Indices

Data is stored and processed within the project pipeline and managed using SQLite.

---

## Project Architecture

Raw Data → Data Cleaning → SQLite Database → Analytics Layer → Dashboards & Reports

### Workflow

1. Data Ingestion
2. Data Cleaning & Validation
3. SQLite Database Creation
4. Exploratory Data Analysis
5. Performance Analytics
6. Advanced Analytics
7. Dashboard Development
8. Automated Reporting

---

## Folder Structure

```text
company_mf_capstone/
│
├── data/
├── notebooks/
├── scripts/
├── dashboard/
├── reports/
├── sql/
├── streamlit_app/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* Matplotlib
* Seaborn
* Plotly
* Streamlit
* Power BI
* Git & GitHub

---

## Key Analyses Performed

### Exploratory Data Analysis

* AUM Growth Analysis
* SIP Inflow Trends
* Investor Demographics
* Geographic Distribution Analysis
* Category-wise Fund Flow Analysis
* Sector Allocation Analysis

### Performance Analytics

* Daily Returns
* CAGR Analysis
* Sharpe Ratio
* Sortino Ratio
* Alpha and Beta
* Maximum Drawdown
* Fund Scorecard
* Benchmark Comparison

### Advanced Analytics

* Value at Risk (VaR)
* Conditional Value at Risk (CVaR)
* Rolling Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Fund Recommendation Engine
* Monte Carlo Simulation
* Portfolio Optimization (Efficient Frontier)

---

## Dashboard Features

### Power BI Dashboard

* Industry Overview
* Fund Performance
* Investor Analytics
* SIP & Market Trends

### Streamlit Dashboard

* KPI Cards
* Fund Performance Analysis
* Risk-Based Recommendations
* Interactive Data Exploration

---

## Key Findings

* Equity-oriented funds delivered higher long-term returns but exhibited greater volatility.
* SIP participation increased significantly during the analysis period.
* Risk-adjusted performance varied considerably across fund categories.
* Portfolio concentration differed among funds, highlighting diversification opportunities.
* Consistent SIP investors demonstrated stronger long-term investment behavior.

---

## How to Run the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run ETL Pipeline

```bash
python scripts/run_pipeline.py
```

### Launch Streamlit Dashboard

```bash
streamlit run streamlit_app/app.py
```

### Open Power BI Dashboard

Open:

```text
dashboard/company_mf_dashboard.pbix
```

using Microsoft Power BI Desktop.

---

## Future Enhancements

* Real-time mutual fund data integration
* Cloud deployment
* Advanced recommendation engine
* Portfolio rebalancing suggestions
* Mobile dashboard support

---

## Author

Bluestock Mutual Fund Analytics Capstone Project

Version: 1.0
