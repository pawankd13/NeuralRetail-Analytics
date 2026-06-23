import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Neural Retail",
    page_icon="📊",
    layout="wide"
)
st.title("📶 Sales Dashboard")
df = pd.read_csv(
    r"D:\Amdox neuralretail project\NeuralRetail\data\cleaned_retail.csv"
)

total_revenue = df["Revenue"].sum()

total_orders = df["Invoice"].nunique()

total_customers = df["Customer ID"].nunique()

avg_order_value = total_revenue / total_orders

col1,col2,col3,col4 = st.columns(4)

col1.metric("Revenue", f"${total_revenue:,.0f}")
col2.metric("Orders", total_orders)
col3.metric("Customers", total_customers)
col4.metric("AOV", f"${avg_order_value:,.2f}")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

monthly_sales = (
    df.groupby(
        pd.Grouper(
            key="InvoiceDate",
            freq="ME"
        )
    )["Revenue"]
    .sum()
)

st.markdown("---")

st.subheader("Monthly Revenue Trend")

st.line_chart(monthly_sales)

country_sales = (
    df.groupby("Country")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

st.markdown("---")

st.subheader("Top Countries by Revenue")

st.bar_chart(country_sales)
st.markdown("---")
st.caption("Neural Retail Project | Amdox Internship")