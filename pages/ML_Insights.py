import streamlit as st
import pandas as pd
import joblib


# =====================================================
# SELECT PREDICTION TYPE
# =====================================================

prediction_type = st.radio(
    "Select Prediction",
    ["Revenue Prediction", "Profit/Loss Prediction"],
    horizontal=True,
    key="prediction_type"
)


# =====================================================
# REVENUE PREDICTION
# =====================================================

if prediction_type == "Revenue Prediction":

    st.title("Revenue Prediction")

    # Load model and feature columns
    revenue_model = joblib.load("roi_model.pkl")
    X = pd.read_csv("X.csv")

    # Numerical inputs
    duration = st.number_input(
        "Duration",
        min_value=1,
        key="revenue_duration"
    )

    impressions = st.number_input(
        "Impressions",
        min_value=0,
        key="revenue_impressions"
    )

    clicks = st.number_input(
        "Clicks",
        min_value=0,
        key="revenue_clicks"
    )

    leads = st.number_input(
        "Leads",
        min_value=0,
        key="revenue_leads"
    )

    conversions = st.number_input(
        "Conversions",
        min_value=0,
        key="revenue_conversions"
    )

    acquisition_cost = st.number_input(
        "Acquisition Cost",
        min_value=0.0,
        key="revenue_acquisition_cost"
    )

    engagement_score = st.number_input(
        "Engagement Score",
        min_value=0.0,
        key="revenue_engagement_score"
    )

    roi = st.number_input(
        "ROI",
        min_value=0.0,
        key="revenue_roi"
    )

    # Channel
    channel = st.selectbox(
        "Channel Used",
        [
            "Email",
            "Facebook",
            "Google",
            "Instagram",
            "WhatsApp",
            "YouTube"
        ],
        key="revenue_channel"
    )

    # Campaign Type
    campaign_type = st.selectbox(
        "Campaign Type",
        [
            "Influencer",
            "Paid Ads",
            "SEO",
            "Social Media"
        ],
        key="revenue_campaign_type"
    )

    # Target Audience
    target_audience = st.selectbox(
        "Target Audience",
        [
            "Premium Shoppers",
            "Tier 2 City Customers",
            "Working Women",
            "Youth"
        ],
        key="revenue_target_audience"
    )

    # Language
    language = st.selectbox(
        "Language",
        [
            "English",
            "Hindi",
            "Tamil"
        ],
        key="revenue_language"
    )

    # Customer Segment
    customer_segment = st.selectbox(
        "Customer Segment",
        [
            "Premium Shoppers",
            "Tier 2 City Customers",
            "Working Women",
            "Youth"
        ],
        key="revenue_customer_segment"
    )

    # Predict Revenue
    if st.button("Predict Revenue", key="predict_revenue"):

        # Create dataframe with training columns
        input_data = pd.DataFrame(
            0,
            index=[0],
            columns=X.columns
        )

        # Numerical features
        input_data.loc[0, "Duration"] = duration
        input_data.loc[0, "Impressions"] = impressions
        input_data.loc[0, "Clicks"] = clicks
        input_data.loc[0, "Leads"] = leads
        input_data.loc[0, "Conversions"] = conversions
        input_data.loc[0, "Acquisition_Cost"] = acquisition_cost
        input_data.loc[0, "Engagement_Score"] = engagement_score
        input_data.loc[0, "ROI"] = roi

        # Channel
        input_data.loc[0, channel] = 1

        # Campaign Type
        input_data.loc[
            0,
            f"Campaign_Type_{campaign_type}"
        ] = 1

        # Target Audience
        input_data.loc[
            0,
            f"Target_Audience_{target_audience}"
        ] = 1

        # Language
        input_data.loc[
            0,
            f"Language_{language}"
        ] = 1

        # Customer Segment
        input_data.loc[
            0,
            f"Customer_Segment_{customer_segment}"
        ] = 1

        # Prediction
        revenue_pred = revenue_model.predict(input_data)[0]

        st.success("Prediction Completed")

        st.metric(
            "Predicted Revenue",
            f"₹{revenue_pred:,.2f}"
        )


# =====================================================
# PROFIT / LOSS PREDICTION
# =====================================================

elif prediction_type == "Profit/Loss Prediction":

    st.title("Profit / Loss Prediction")

    # Load model and feature columns
    profit_model = joblib.load("profit_model.pkl")
    X = pd.read_csv("profit_loss_X.csv")

    # Numerical inputs
    duration = st.number_input(
        "Duration",
        min_value=1,
        value=1,
        key="profit_duration"
    )

    impressions = st.number_input(
        "Impressions",
        min_value=0,
        value=0,
        key="profit_impressions"
    )

    clicks = st.number_input(
        "Clicks",
        min_value=0,
        value=0,
        key="profit_clicks"
    )

    leads = st.number_input(
        "Leads",
        min_value=0,
        value=0,
        key="profit_leads"
    )

    conversions = st.number_input(
        "Conversions",
        min_value=0,
        value=0,
        key="profit_conversions"
    )

    acquisition_cost = st.number_input(
        "Acquisition Cost",
        min_value=0.0,
        value=0.0,
        key="profit_acquisition_cost"
    )

    engagement_score = st.number_input(
        "Engagement Score",
        min_value=0.0,
        value=0.0,
        key="profit_engagement_score"
    )

    # Channel
    channel = st.selectbox(
        "Channel Used",
        [
            "Email",
            "Facebook",
            "Google",
            "Instagram",
            "WhatsApp",
            "YouTube"
        ],
        key="profit_channel"
    )

    # Campaign Type
    campaign_type = st.selectbox(
        "Campaign Type",
        [
            "Influencer",
            "Paid Ads",
            "SEO",
            "Social Media"
        ],
        key="profit_campaign_type"
    )

    # Target Audience
    target_audience = st.selectbox(
        "Target Audience",
        [
            "Premium Shoppers",
            "Tier 2 City Customers",
            "Working Women",
            "Youth"
        ],
        key="profit_target_audience"
    )

    # Language
    language = st.selectbox(
        "Language",
        [
            "English",
            "Hindi",
            "Tamil"
        ],
        key="profit_language"
    )

    # Customer Segment
    customer_segment = st.selectbox(
        "Customer Segment",
        [
            "Premium Shoppers",
            "Tier 2 City Customers",
            "Working Women",
            "Youth"
        ],
        key="profit_customer_segment"
    )

    # Predict Profit / Loss
    if st.button(
        "Predict Profit / Loss",
        key="predict_profit_loss"
    ):

        # Create dataframe with training columns
        input_data = pd.DataFrame(
            0,
            index=[0],
            columns=X.columns
        )

        # Numerical features
        input_data.loc[0, "Duration"] = duration
        input_data.loc[0, "Impressions"] = impressions
        input_data.loc[0, "Clicks"] = clicks
        input_data.loc[0, "Leads"] = leads
        input_data.loc[0, "Conversions"] = conversions
        input_data.loc[0, "Acquisition_Cost"] = acquisition_cost
        input_data.loc[0, "Engagement_Score"] = engagement_score

        # Channel
        input_data.loc[0, channel] = 1

        # Campaign Type
        input_data.loc[
            0,
            f"Campaign_Type_{campaign_type}"
        ] = 1

        # Target Audience
        input_data.loc[
            0,
            f"Target_Audience_{target_audience}"
        ] = 1

        # Language
        input_data.loc[
            0,
            f"Language_{language}"
        ] = 1

        # Customer Segment
        input_data.loc[
            0,
            f"Customer_Segment_{customer_segment}"
        ] = 1

        # Prediction
        prediction = profit_model.predict(input_data)[0]

        # Display result
        if prediction == "Profit":

            st.success(
                "The campaign is predicted to generate PROFIT."
            )

        else:

            st.error(
                "The campaign is predicted to result in LOSS."
            )
