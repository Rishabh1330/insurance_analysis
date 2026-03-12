import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

st.title("📊 Insurance Data Analytics Dashboard")

df = pd.read_csv("insurance.csv")

# -----------------------
# KPI CARDS
# -----------------------

st.subheader("Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

avg_claim = df["claim"].mean()
max_claim = df["claim"].max()
avg_bmi = df["bmi"].mean()
smoker_percent = (df["smoker"].value_counts(normalize=True).get("Yes",0))*100

col1.metric("Average Claim", f"${avg_claim:,.0f}")
col2.metric("Maximum Claim", f"${max_claim:,.0f}")
col3.metric("Average BMI", f"{avg_bmi:.1f}")
col4.metric("Smokers %", f"{smoker_percent:.1f}%")

st.divider()

# -----------------------
# FILTERS
# -----------------------

st.sidebar.header("Filters")

age_range = st.sidebar.slider(
    "Age Range",
    int(df.age.min()),
    int(df.age.max()),
    (20,60)
)

bmi_range = st.sidebar.slider(
    "BMI Range",
    float(df.bmi.min()),
    float(df.bmi.max()),
    (18.0,35.0)
)

filtered_df = df[
    (df.age >= age_range[0]) &
    (df.age <= age_range[1]) &
    (df.bmi >= bmi_range[0]) &
    (df.bmi <= bmi_range[1])
]

# -----------------------
# Claim Distribution
# -----------------------

st.subheader("Claim Distribution")

fig1 = px.histogram(
    filtered_df,
    x="claim",
    nbins=30,
    title="Distribution of Insurance Claims"
)

st.plotly_chart(fig1, use_container_width=True)

# -----------------------
# Age vs Claim
# -----------------------

st.subheader("Age vs Insurance Claim")

fig2 = px.scatter(
    filtered_df,
    x="age",
    y="claim",
    color="smoker",
    size="bmi",
    title="Age vs Claim Cost"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------
# Smoker Impact
# -----------------------

st.subheader("Average Claim by Smoking Status")

smoker_claim = filtered_df.groupby("smoker")["claim"].mean().reset_index()

fig3 = px.bar(
    smoker_claim,
    x="smoker",
    y="claim",
    color="smoker"
)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------
# Correlation Heatmap
# -----------------------

st.subheader("Feature Correlation")

corr = filtered_df.corr(numeric_only=True)

fig4 = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu_r"
)

st.plotly_chart(fig4, use_container_width=True)

# -----------------------
# Feature Importance
# -----------------------

st.subheader("Model Feature Importance")

model = joblib.load("best_model.pkl")

features = ["age","bmi","children","bloodpressure","smoker","diabetic","gender"]

importance = model.feature_importances_

importance_df = pd.DataFrame({
    "Feature":features,
    "Importance":importance
}).sort_values("Importance",ascending=False)

fig5 = px.bar(
    importance_df,
    x="Importance",
    y="Feature",
    orientation="h"
)

st.plotly_chart(fig5, use_container_width=True)