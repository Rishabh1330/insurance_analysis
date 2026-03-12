import streamlit as st

st.set_page_config(
    page_title="Insurance Analytics Platform",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Health Insurance Analytics Platform")

st.markdown("""
Welcome to the **Health Insurance Analytics and Prediction System**.

This project demonstrates:

### 🔮 Insurance Cost Prediction
Predict insurance costs using a trained Machine Learning model.

### 📊 Data Analytics Dashboard
Explore trends in insurance data through interactive visualizations.

### 🧠 Model Insights
Understand which features impact insurance costs.

Use the **sidebar on the left** to navigate between pages.
""")

st.info("Navigate using the sidebar to access Prediction and Analytics Dashboard.")