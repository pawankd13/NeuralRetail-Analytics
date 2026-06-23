import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Neural Retail",
    page_icon="📊",
    layout="wide"
)

st.title("👥 Customer Dashboard")

df = pd.read_csv(
    r"D:\Amdox neuralretail project\NeuralRetail\data\rfm_customers.csv"
)

st.write(df.head())

total_customers = df["Customer ID"].nunique()

champions = (df["Segment"] == "Champions").sum()

loyal = (df["Segment"] == "Loyal Customers").sum()

at_risk = (df["Segment"] == "At Risk").sum()

col1,col2,col3,col4 = st.columns(4)

col1.metric("Customers", total_customers)
col2.metric("Champions", champions)
col3.metric("Loyal", loyal)
col4.metric("At Risk", at_risk)

st.markdown("---")

st.subheader("Customer Segments")

segment_counts = df["Segment"].value_counts()

st.bar_chart(segment_counts)

st.markdown("---")

st.subheader("Revenue Contribution by Segment")

segment_revenue = df.groupby(
    "Segment"
)["Monetary"].sum()

st.bar_chart(segment_revenue)

st.markdown("---")

st.subheader("Top 10 Customers")

top_customers = df.sort_values(
    "Monetary",
    ascending=False
).head(10)

st.dataframe(
    top_customers[
        ["Customer ID",
         "Monetary",
         "Segment"]
    ]
)
st.markdown("---")
st.caption("Neural Retail Project | Amdox Internship")
