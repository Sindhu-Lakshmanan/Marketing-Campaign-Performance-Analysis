import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv("df_all.csv")
st.set_page_config(layout="wide")

st.title("👥 Customer Analysis")    

# -----------------------------
# KPI SECTION
# -----------------------------

total_revenue = df['Revenue'].sum()
total_leads = df['Leads'].sum()
total_conversions = df['Conversions'].sum()
avg_roi = df['ROI'].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Revenue", f"₹{total_revenue:,.0f}")

with col2:
    st.metric("Total Leads", f"{total_leads:,.0f}")

with col3:
    st.metric("Total Conversions", f"{total_conversions:,.0f}")

with col4:
    st.metric("Average ROI", f"{avg_roi:.2f}")

st.divider()

# -----------------------------
# CUSTOMER SEGMENT SUMMARY
# -----------------------------

customer_summary = (
    df.groupby('Customer_Segment')
    .agg({
        'Revenue':'sum',
        'Leads':'sum',
        'Conversions':'sum',
        'ROI':'mean'
    })
    .reset_index()
)

# -----------------------------
# REVENUE BY SEGMENT
# -----------------------------

fig1 = px.bar(
    customer_summary,
    x='Customer_Segment',
    y='Revenue',
    title='Revenue by Customer Segment',
    text_auto='.2s'
)
fig1.update_yaxes(
    range=[16000000000,16500000000])

st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# LEADS BY SEGMENT
# -----------------------------

fig2 = px.bar(
    customer_summary,
    x='Customer_Segment',
    y='Leads',
    title='Leads by Customer Segment',
    text_auto='.2s'
)
fig2.update_yaxes(
    range=[55000000,60000000])

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# CONVERSIONS BY SEGMENT
# -----------------------------

fig3 = px.bar(
    customer_summary,
    x='Customer_Segment',
    y='Conversions',
    title='Conversions by Customer Segment',
    text_auto='.2s'
)
fig3.update_yaxes(
    range=[32000000,33000000])

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# ROI BY SEGMENT
# -----------------------------

fig4 = px.bar(
    customer_summary,
    x='Customer_Segment',
    y='ROI',
    title='Average ROI by Customer Segment',
    text_auto='.2f'
)
fig4.update_yaxes(
    range=[5900,6200])

st.plotly_chart(fig4, use_container_width=True)

# -----------------------------
# CONVERSION SHARE
# -----------------------------

fig5 = px.pie(
    customer_summary,
    names='Customer_Segment',
    values='Conversions',
    title='Conversion Share by Customer Segment'
)

st.plotly_chart(fig5, use_container_width=True)


# -----------------------------
# TOP CUSTOMER SEGMENTS TABLE
# -----------------------------

st.subheader("Customer Segment Performance")

top_segments = customer_summary.sort_values(
    by='Revenue',
    ascending=False
)

st.dataframe(
    top_segments,
    use_container_width=True
)