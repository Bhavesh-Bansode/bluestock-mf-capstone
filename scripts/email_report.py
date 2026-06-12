import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

performance = pd.read_csv("data/processed/07_scheme_performance_clean.csv")

top_fund = performance.sort_values(
    "sharpe_ratio",
    ascending=False
).iloc[0]

html_report = f"""
<h1>Weekly Mutual Fund Summary</h1>

<h2>Top Performing Fund</h2>
<p>{top_fund['scheme_name']}</p>

<h2>Sharpe Ratio</h2>
<p>{top_fund['sharpe_ratio']:.2f}</p>

<h2>3-Year Return</h2>
<p>{top_fund['return_3yr_pct']:.2f}%</p>
"""

with open(
    "reports/weekly_report.html",
    "w",
    encoding="utf-8"
) as f:

    f.write(html_report)