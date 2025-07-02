# Stroke-prediction-app

This is a Streamlit web application that predicts the likelihood of a stroke based on user-provided health parameters. It utilizes a pre-trained machine learning model to make predictions and visualize the associated risk level.

## 🔍 Overview

The Stroke Risk Prediction App is designed to help healthcare practitioners and individuals assess the potential risk of stroke using basic medical and lifestyle inputs such as age, gender, glucose level, BMI, and smoking status.

### 💡 Features
- Predicts stroke risk based on patient inputs
- Displays confidence percentage for prediction
- Provides a visual breakdown of risk levels
- Offers health guidance based on prediction confidence

---

## 🚀 How to Run the App Locally

### 🛠️ Prerequisites
- Python 3.7 or above
- `streamlit`, `pandas`, `numpy`, `joblib`, and `scikit-learn` installed

Install dependencies:

```bash
pip install streamlit pandas numpy scikit-learn joblib

▶️ Running the App
Clone this repository:

bash
Copy
Edit
git clone https://github.com/your-username/stroke-risk-predictor.git
cd stroke-risk-predictor
Ensure the following files are present:

app.py – Main Streamlit application

stroke_model.pkl – Trained machine learning model

scaler.pkl – Scaler used during model training

Start the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Open in browser at: http://localhost:8501

🧾 Input Parameters
Parameter	Description
Gender	Male / Female
Age	Slider input (1-100)
Hypertension	Yes / No
Heart Disease	Yes / No
Ever Married	Yes / No
Work Type	Private / Self-employed / Govt_job / children / Never_worked
Residence Type	Urban / Rural
Average Glucose	Numeric input (50.0 - 300.0 mg/dL)
BMI	Numeric input (10.0 - 60.0)
Smoking Status	formerly smoked / never smoked / smokes / Unknown

📊 Output
Prediction: High or Low Risk of Stroke

Confidence: Probability of stroke in percentage

Visualizations:

Progress bar for stroke risk

Metric widget showing confidence

Bar chart comparing stroke vs no-stroke probability

Health Guidance Message: Based on predicted risk level
