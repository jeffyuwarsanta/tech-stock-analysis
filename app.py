import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Technology Stock Performance Explorer")

st.write("""
This beginner-friendly tool compares four major technology stocks:

- Apple (AAPL)
- Microsoft (MSFT)
- Nvidia (NVDA)
- Google / Alphabet (GOOGL)

The tool helps beginners compare stocks using four ideas:
1. Growth
2. Risk
3. Consistency
4. Downside risk
""")

st.subheader("How to Use This Tool")

st.write("""
1. Select stocks using the sidebar.
2. Look at growth to understand long-term performance.
3. Use risk vs return to compare volatility.
3. Check consistency to see reliability.
5. Review downside risk to understand possible losses.
""")

df = pd.read_csv("tech_stock_alltime.csv")
df["date"] = pd.to_datetime(df["date"])

stocks = st.sidebar.multiselect(
    "Select Tech Stocks",
    ["AAPL", "MSFT", "NVDA", "GOOGL"],
    default=["AAPL", "MSFT", "NVDA", "GOOGL"]
)

df = df[df["htsymbol"].isin(stocks)]

st.subheader("Summary Statistics")

summary = df.groupby("htsymbol")["monthly_return"].agg(
    average_return="mean",
    volatility="std",
    best_month="max",
    worst_month="min"
)

summary["positive_month_rate"] = df.groupby("htsymbol")["positive_month"].mean()

st.dataframe(summary)

st.subheader("1. Growth Over Time")
st.write("This chart shows how an investment would grow over time.")

fig1, ax1 = plt.subplots(figsize=(10, 5))

for stock in df["htsymbol"].unique():
    temp = df[df["htsymbol"] == stock]
    ax1.plot(temp["date"], temp["growth"], label=stock)

ax1.set_title("Growth Over Time")
ax1.set_xlabel("Date")
ax1.set_ylabel("Growth Index")
ax1.legend()
st.pyplot(fig1)

st.subheader("2. Risk vs Return")
st.write("This chart compares average return and volatility. Higher volatility means higher risk.")

risk_return = df.groupby("htsymbol")["monthly_return"].agg(["mean", "std"])

fig2, ax2 = plt.subplots(figsize=(8, 5))

for stock in risk_return.index:
    ax2.scatter(
        risk_return.loc[stock, "std"],
        risk_return.loc[stock, "mean"],
        label=stock
    )
    ax2.text(
        risk_return.loc[stock, "std"],
        risk_return.loc[stock, "mean"],
        stock
    )

ax2.set_title("Risk vs Return")
ax2.set_xlabel("Risk / Volatility")
ax2.set_ylabel("Average Monthly Return")
ax2.legend()
st.pyplot(fig2)

st.subheader("3. Consistency")
st.write("This chart shows how often each stock had a positive monthly return.")

consistency = df.groupby("htsymbol")["positive_month"].mean()

fig3, ax3 = plt.subplots(figsize=(8, 5))
consistency.plot(kind="bar", ax=ax3)

ax3.set_title("Positive Month Rate")
ax3.set_xlabel("Stock")
ax3.set_ylabel("Percentage of Positive Months")
st.pyplot(fig3)

st.subheader("4. Downside Risk")
st.write("This chart shows how far each stock fell from its previous peak. Lower values mean deeper losses.")

fig4, ax4 = plt.subplots(figsize=(10, 5))

for stock in df["htsymbol"].unique():
    temp = df[df["htsymbol"] == stock]
    ax4.plot(temp["date"], temp["drawdown"], label=stock)

ax4.set_title("Drawdown Over Time")
ax4.set_xlabel("Date")
ax4.set_ylabel("Drawdown")
ax4.legend()
st.pyplot(fig4)

st.subheader("Beginner Interpretation")

st.write("""
A beginner investor can use this tool in four ways:

- Growth shows which stock increased the most over time.
- Risk shows how unstable the stock is.
- Consistency shows how often the stock gives positive monthly returns.
- Downside risk shows how much the stock can fall during difficult periods.

A stock with high growth may also have high risk, so investors should not only look at price increase.
""")

st.subhead("Key Insights")

st.write("""
- Nvidia shows high growth but also high volatility.
- Microsoft appears more stable with lower risk.
- Apple provides a balanced performance between growth and risk.
- Google sits between stability and growth.

This shows that higher return often comes with higher risk.
""")

