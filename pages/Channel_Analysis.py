import plotly.express as px
import streamlit as st
import plotly.express as px
import pandas as pd

st.subheader("📢 Channel Analysis")
df = pd.read_csv("df_all.csv")
# Create a copy
channel_df = df.copy()

# Split channels into list
channel_df['Channel_Used'] = channel_df['Channel_Used'].str.split(',')

# Convert each channel into separate row
channel_df = channel_df.explode('Channel_Used')

# Remove extra spaces
channel_df['Channel_Used'] = channel_df['Channel_Used'].str.strip()

# Channel Summary
channel_summary = channel_df.groupby('Channel_Used').agg({
    'Revenue': 'mean',
    'ROI': 'mean',
    'Conversions': 'sum',
    'Clicks': 'sum',
    'Impressions': 'sum'
}).reset_index()

# CTR and Conversion Rate
channel_summary['CTR (%)'] = (
    channel_summary['Clicks'] /
    channel_summary['Impressions'] * 100
)

channel_summary['Conversion Rate (%)'] = (
    channel_summary['Conversions'] /
    channel_summary['Clicks'] * 100
)

# KPI
best_channel = channel_summary.sort_values(
    'ROI',
    ascending=False
).iloc[0]

total_channels = channel_summary['Channel_Used'].nunique()
highest_roi = channel_summary['ROI'].max()
total_conversions = channel_summary['Conversions'].sum()

col1, col2, col3= st.columns([1,1,2])



with col1:
    st.metric("Total Channels", total_channels)

with col2:
    st.metric("Highest ROI", f"{highest_roi:.2f}")

with col3:
    st.metric("Total Conversions", f"{total_conversions:,.2f}")




st.metric(
    "Best Performing Channel",
    best_channel['Channel_Used']
)

# Display summary table
st.dataframe(channel_summary)

# Average Revenue by Channel
fig = px.bar(
    channel_summary,
    x='Channel_Used',
    y='Revenue',
    title='Average Revenue by Channel'
)
fig.update_yaxes(
    range=[510000,520000])
st.plotly_chart(fig, use_container_width=True)

# Average ROI by Channel
fig = px.bar(
    channel_summary,
    x='Channel_Used',
    y='ROI',
    title='Average ROI by Channel'
)
fig.update_yaxes(
    range=[6000,6200])
st.plotly_chart(fig, use_container_width=True)

# Total Conversions by Channel
fig = px.bar(
    channel_summary,
    x='Channel_Used',
    y='Conversions',
    title='Total Conversions by Channel'
)
fig.update_yaxes(
    range=[53000000,55000000])
st.plotly_chart(fig, use_container_width=True)

# CTR by Channel
fig = px.bar(
    channel_summary,
    x='Channel_Used',
    y='CTR (%)',
    title='CTR (%) by Channel'
)
fig.update_yaxes(
    range=[8,9])
st.plotly_chart(fig, use_container_width=True)

# Conversion Rate by Channel
fig = px.bar(
    channel_summary,
    x='Channel_Used',
    y='Conversion Rate (%)',
    title='Conversion Rate (%) by Channel'
)
fig.update_yaxes(
    range=[20,22])
st.plotly_chart(fig, use_container_width=True)
