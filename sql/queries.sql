SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

SELECT substr(date,1,7) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

SELECT month, yoy_growth_pct
FROM sip_data_clean
ORDER BY month;

SELECT state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

SELECT scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

SELECT fund_house,
SUM(aum_crore) AS total_aum
FROM fact_performance
GROUP BY fund_house
ORDER BY total_aum DESC;

SELECT category,
AVG(return_3yr_pct) AS avg_return
FROM fact_performance
GROUP BY category;

SELECT amfi_code,
MAX(nav) AS highest_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY highest_nav DESC
LIMIT 10;

SELECT kyc_status,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY kyc_status;

SELECT category,
COUNT(*) AS total_funds
FROM dim_fund
GROUP BY category
ORDER BY total_funds DESC;
