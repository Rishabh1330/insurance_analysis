# 💰 Health Insurance Cost Prediction & Analytics Platform

## 📌 Project Overview

This project is a **complete end-to-end data analytics and machine learning application** that predicts health insurance costs and provides interactive analytics dashboards.

The system combines **Data Analysis, Machine Learning, Web Deployment, and Business Intelligence dashboards** to simulate a real-world insurance analytics platform used by companies to estimate claim costs and analyze customer trends.

The application allows users to:

* Predict **health insurance claim costs**
* Explore **interactive analytics dashboards**
* Analyze **customer health risk patterns**
* Visualize insights through **Power BI dashboards**

---

# 🚀 Key Features

### 🔮 1. Insurance Cost Prediction

A machine learning model predicts the **expected insurance payment** based on user inputs such as:

* Age
* BMI
* Number of children
* Blood pressure
* Gender
* Smoking status
* Diabetes status

The prediction model is deployed using **Streamlit** for real-time interaction.

---

### 📊 2. Interactive Analytics Dashboard (Streamlit)

The project includes an **analytics dashboard** that allows users to explore insights from the dataset.

Visualizations include:

* 📈 Age vs Insurance Claim analysis
* 📊 Claim cost distribution
* 🚬 Smoker vs Non-Smoker claim comparison
* 📉 BMI vs Claim relationship
* 🔥 Correlation heatmap for all variables
* 🎛 Interactive filters for:

  * Age
  * BMI
  * Smoking status

These dashboards help in identifying **health risk patterns and cost drivers**.

---

### 📊 3. Business Intelligence Dashboard (Power BI)

To simulate real enterprise reporting systems, the dataset is also analyzed using **Power BI dashboards**.

The Power BI dashboard includes:

* KPI Cards

  * Average Claim
  * Maximum Claim
  * Total Customers
  * Percentage of Smokers

* Visualizations

  * Claim cost by Age Group
  * Claim cost by BMI category
  * Smoker vs Non-Smoker comparison
  * Gender-based claim distribution
  * Interactive slicers and filters

Power BI provides **business-level insights for insurance companies** to understand customer risk segments.

---

# 🧠 Machine Learning Model

The project uses **Supervised Regression models** to predict insurance costs.

Steps involved:

1️⃣ Data Cleaning
2️⃣ Feature Engineering
3️⃣ Label Encoding of categorical variables
4️⃣ Feature Scaling using **StandardScaler**
5️⃣ Model Training and Evaluation

Models tested include:

* Linear Regression
* Random Forest Regressor
* XGBoost Regressor

The **best performing model** was selected and saved using **Joblib** for deployment.

---

# 🏗️ Project Architecture

```
Health Insurance Cost Prediction
│
├── app.py
│
├── pages
│   ├── 1_Insurance_Prediction.py
│   └── 2_Data_Analytics_Dashboard.py
│
├──insurance_data.csv
|
│──insurance_with_predictions  
│
├── best_model.pkl
│    
|── scaler.pkl
│── label_encoders.pkl
│
├──insurance_dashboard.pbix 
│ 
│
└── README.md
```

---

# 🛠️ Technologies Used

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn
* Plotly
* Streamlit

### Machine Learning

* Scikit-learn
* XGBoost

### Business Intelligence

* Power BI

### Model Deployment

* Streamlit Web App

---

# 📊 Dataset Features

The dataset contains health and demographic information used to predict insurance claim costs.

| Feature       | Description                             |
| ------------- | --------------------------------------- |
| Age           | Age of the individual                   |
| BMI           | Body Mass Index                         |
| Children      | Number of children covered by insurance |
| BloodPressure | Blood pressure level                    |
| Gender        | Male / Female                           |
| Smoker        | Yes / No                                |
| Diabetic      | Yes / No                                |
| Claim         | Insurance claim amount                  |

---

# ⚙️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/insurance-cost-prediction.git
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

or install manually

```bash
pip install streamlit pandas numpy scikit-learn matplotlib seaborn plotly xgboost joblib
```

---

### 3️⃣ Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 📊 Power BI Dashboard

Open the **Power BI file**:

```
powerbi/insurance_dashboard.pbix
```

This dashboard provides **advanced business insights and KPIs** for insurance claim analysis.

---

# 📈 Example Insights

The analysis reveals several patterns:

* Smokers tend to have **significantly higher insurance claims**
* Higher BMI is associated with **increased claim costs**
* Age is positively correlated with **insurance expenses**
* Certain health conditions increase claim probability

These insights help insurance companies **identify high-risk customer segments**.

---

# 🌍 Future Improvements

Possible enhancements include:

* Deploying the application on **Streamlit Cloud**
* Adding **Deep Learning models**
* Real-time API integration
* Automated report generation
* Advanced Power BI dashboards

---

# 👨‍💻 Author

**Rishabh Verma**
B.Tech – Computer Science
Dronacharya College of Engineering

📧 Email: [rxverma2004@gmail.com](mailto:rxverma2004@gmail.com)
🔗 LinkedIn: https://www.linkedin.com/in/rishabh-verma-58489026a/

---

# ⭐ If you found this project useful, consider giving it a star on GitHub!
