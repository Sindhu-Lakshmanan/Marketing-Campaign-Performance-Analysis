import pandas as pd
import numpy as np
import streamlit as st
df = pd.read_csv("df_all.csv")
st.title("👥 Marketing Analysis")
# Display basic information
st.subheader("Dataset Overview")

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.metric("Total Records", f"{len(df):,}")

with col2:
    st.metric("Total Revenue", f"₹{df['Revenue'].sum():,.2f}")

with col3:
    st.metric("Average ROI", f"{df['ROI'].mean():.2f}")

col4, col5 = st.columns(2)

with col4:
    st.metric("Total Leads", f"{df['Leads'].sum():,.2f}")

with col5:
    st.metric("Total Conversions", f"{df['Conversions'].sum():,.2f}")


st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

st.subheader("Dashboard Sections")

if st.button("📈 Campaign Analysis"):
    st.switch_page("pages/Campaign_Analysis.py")

if st.button("📣 Channel Analysis"):
    st.switch_page("pages/Channel_Analysis.py")

if st.button("👥 Customer Segment Analysis"):
    st.switch_page("pages/Customer_Analysis.py")

if st.button("🏷️ Brand Analysis"):
    st.switch_page("pages/Brand_Analysis.py")

if st.button("🤖 Machine Learning Insights"):
    st.switch_page("pages/ML_Insights.py")
