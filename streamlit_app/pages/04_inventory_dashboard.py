import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Neural Retail",
    page_icon="📊",
    layout="wide"
)

st.title("📦 Inventory Dashboard")

df = pd.read_csv(
    r"D:\Amdox neuralretail project\NeuralRetail\data\inventory_analysis.csv"
)

total_products = len(df)

high_demand = (df["Risk"] == "High Demand").sum()

normal_demand = (df["Risk"] == "Normal Demand").sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Products", total_products)

col2.metric("High Demand Products", high_demand)

col3.metric("Normal Demand Products", normal_demand)

st.markdown("---")

st.subheader("Demand Risk Distribution")

risk_counts = df["Risk"].value_counts()

st.bar_chart(risk_counts)

st.markdown("---")

st.subheader("Top 10 Products by Quantity Sold")

top_products = (
    df.sort_values(
        "Quantity",
        ascending=False
    )
    .head(10)
)

st.dataframe(top_products)

st.markdown("---")

st.subheader("High Demand Products")

high_demand_products = df[
    df["Risk"] == "High Demand"
]

st.dataframe(
    high_demand_products.head(20)
)

st.markdown("---")

st.subheader("Product Quantity Distribution")

st.line_chart(
    df.sort_values("Quantity")["Quantity"]
)
st.markdown("---")
st.caption("Neural Retail Project | Amdox Internship")