import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown(
    """
    # 📈 Mutual Fund Analytics Platform

    Analyze fund performance, risk metrics,
    investor trends and recommendations
    in a single dashboard.
    """
)
st.set_page_config(
    page_title="Mutual Fund Analytics Platform",
    page_icon="📈",
    layout="wide"
)



performance = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

transactions = pd.read_csv(
    "data/processed/08_investor_transactions_clean.csv"
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Funds",
    len(performance)
)

col2.metric(
    "Avg Sharpe",
    round(
        performance["sharpe_ratio"].mean(),
        2
    )
)

col3.metric(
    "Avg 3Y Return %",
    round(
        performance["return_3yr_pct"].mean(),
        2
    )
)

col4.metric(
    "Highest Return %",
    round(
        performance["return_3yr_pct"].max(),
        2
    )
)
st.subheader(
    "Return vs Risk Analysis"
)

fig = px.scatter(
    performance,
    x="std_dev_ann_pct",
    y="return_3yr_pct",
    color="risk_grade",
    hover_name="scheme_name",
    size="aum_crore"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.subheader("Fund Performance Table")

st.dataframe(
    performance[
        [
            "scheme_name",
            "return_3yr_pct",
            "sharpe_ratio",
            "risk_grade"
        ]
    ]
)
risk_filter = st.selectbox(
    "Select Risk Grade",
    performance["risk_grade"].unique()
)

filtered = performance[
    performance["risk_grade"]
    == risk_filter
]

st.dataframe(
    filtered[
        [
            "scheme_name",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ]
)
st.subheader(
    "🏆 Top 10 Funds by Sharpe Ratio"
)

top10 = (
    performance
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(10)
)

st.dataframe(top10)

st.subheader(
    "🤖 Fund Recommendation Engine"
)
risk_filter = st.selectbox(
    "Select Risk Appetite",
    performance["risk_grade"].unique()
)
recommended = (
    performance[
        performance["risk_grade"]
        == risk_filter
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

st.success(
    f"Top 3 recommendations for {risk_filter} risk investors"
)

st.table(
    recommended[
        [
            "scheme_name",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ]
)
st.subheader(
    "📊 Investor Insights"
)

st.info(
    """
    • Highest performing funds delivered strong risk-adjusted returns.

    • Diversified funds exhibited lower drawdowns.

    • SIP investors showed consistent long-term participation.

    • High Sharpe funds dominated recommendation rankings.
    """
)
st.sidebar.title(
    "Navigation"
)

page = st.sidebar.radio(
    "Select Section",
    [
        "Dashboard",
        "Recommendations"
    ]
)