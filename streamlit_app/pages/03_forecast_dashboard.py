import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Neural Retail",
    page_icon="📊",
    layout="wide"
)

st.title("📈 Forecast Dashboard")

df = pd.read_csv(
    r"D:\Amdox neuralretail project\NeuralRetail\data\sales_forecast.csv"
)
import matplotlib.pyplot as plt

st.markdown("---")

st.subheader("Sales Forecast Trend")

fig, ax = plt.subplots(figsize=(8,4))

ax.plot(
    df["Forecast_Month"],
    df["Predicted_Revenue"],
    marker="o"
)

ax.set_title("Revenue Forecast")
ax.set_xlabel("Forecast Month")
ax.set_ylabel("Predicted Revenue")

st.pyplot(fig)
st.markdown("---")
st.caption("Neural Retail Project | Amdox Internship")