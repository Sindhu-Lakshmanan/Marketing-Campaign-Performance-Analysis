import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Brand Analysis")
df = pd.read_csv("df_all.csv")
# Group by Brand
brand_summary = df.groupby("Brand_name").agg({
    "Revenue": "sum",
    "ROI": "mean",
    "Leads": "sum",
    "Conversions": "sum"
}).reset_index()

# Top KPI Cards
col1, col2= st.columns(2)

with col1:
    st.metric("Total Brands", brand_summary["Brand_name"].nunique())

with col2:
    st.metric("Total Revenue", f"₹{brand_summary['Revenue'].sum():,.0f}")

col3, col4= st.columns(2)
with col3:
    st.metric("Total Leads", f"{brand_summary['Leads'].sum():,.0f}")

with col4:
    st.metric("Total Conversions", f"{brand_summary['Conversions'].sum():,.0f}")

# Revenue by Brand
fig1 = px.bar(
    brand_summary.sort_values("Revenue", ascending=False),
    x="Brand_name",
    y="Revenue",
    title="Revenue by Brand"
)
fig1.update_yaxes(
    range=[28000000000,28800000000])

st.plotly_chart(fig1, use_container_width=True)

# Conversions by Brand
fig2 = px.bar(
    brand_summary.sort_values("Conversions", ascending=False),
    x="Brand_name",
    y="Conversions",
    title="Conversions by Brand"
)
fig2.update_yaxes(
    range=[56900000,57000000])

st.plotly_chart(fig2, use_container_width=True)

# ROI by Brand
fig3 = px.bar(
    brand_summary.sort_values("ROI", ascending=False),
    x="Brand_name",
    y="ROI",
    title="Average ROI by Brand"
)
fig3.update_yaxes(
    range=[6000,6200])
st.plotly_chart(fig3, use_container_width=True)

# Detailed Table
st.subheader("Brand Performance Summary")
st.dataframe(brand_summary)


brand_profit_pct = (
    df.groupby('Brand_name')['Profit_Loss']
    .apply(lambda x: (x == 'Profit').mean() * 100)
    .reset_index(name='Profit_Percentage')
)

fig = px.bar(
    brand_profit_pct,
    x='Brand_name',
    y='Profit_Percentage',
    title='Profit Percentage by Brand'
)
fig.update_yaxes(
    range=[99,100])

st.plotly_chart(fig, use_container_width=True)