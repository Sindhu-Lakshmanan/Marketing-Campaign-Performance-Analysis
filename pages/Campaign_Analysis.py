import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
df = pd.read_csv("df_all.csv")

# Page Title
st.title("📈 Campaign Analysis")

st.markdown("### Campaign Performance Overview")

# -------------------
# KPI SECTION
# -------------------

total_campaigns = df["Campaign_Type"].nunique()
total_revenue = df["Revenue"].sum()
avg_roi = df["ROI"].mean()
total_conversions = df["Conversions"].sum()

col1, col2 = st.columns(2)

with col1:
    st.metric("Campaign Types", total_campaigns)

with col2:
    st.metric("Total Revenue", f"₹{total_revenue:,.2f}")
col3,col4=st.columns(2)
with col3:
    st.metric("Average ROI", f"{avg_roi:.2f}")

with col4:
    st.metric("Total Conversions", f"{total_conversions:,.0f}")

st.divider()

# -------------------
# CAMPAIGN SUMMARY
# -------------------

campaign_summary = (
    df.groupby("Campaign_Type")
    .agg(
        Revenue=("Revenue", "sum"),
        ROI=("ROI", "mean"),
        Leads=("Leads", "sum"),
        Conversions=("Conversions", "sum")
    )
    .reset_index()
)

# -------------------
# REVENUE CHART
# -------------------

st.subheader("💰 Revenue by Campaign Type")

fig1 = px.bar(
    campaign_summary,
    x="Campaign_Type",
    y="Revenue",
    text_auto=".2s",
    title="Revenue by Campaign Type"
)
fig1.update_yaxes(
    range=[16000000000, 16400000000]
)

st.plotly_chart(fig1, use_container_width=True)

# -------------------
# ROI CHART
# -------------------

st.subheader("📊 Average ROI by Campaign Type")

fig2 = px.bar(
    campaign_summary,
    x="Campaign_Type",
    y="ROI",
    text_auto=".2f",
    title="Average ROI by Campaign Type"
)
fig2.update_yaxes(
    range=[5000,6500]
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------
# LEADS CHART
# -------------------

st.subheader("👥 Leads by Campaign Type")

fig3 = px.bar(
    campaign_summary,
    x="Campaign_Type",
    y="Leads",
    text_auto=".2s",
    title="Leads by Campaign Type"
)
fig3.update_yaxes(
    range=[58000000,60000000]
)

st.plotly_chart(fig3, use_container_width=True)

# -------------------
# CONVERSIONS CHART
# -------------------

st.subheader("🎯 Conversions by Campaign Type")

fig4 = px.bar(
    campaign_summary,
    x="Campaign_Type",
    y="Conversions",
    text_auto=".2s",
    title="Conversions by Campaign Type"
)
fig4.update_yaxes(
    range=[32000000,34000000]
)
st.plotly_chart(fig4, use_container_width=True)

# -------------------
# SUMMARY TABLE
# -------------------

st.subheader("📋 Campaign Summary Table")

st.dataframe(
    campaign_summary,
    use_container_width=True
)