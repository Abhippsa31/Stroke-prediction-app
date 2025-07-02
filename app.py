import streamlit as st
import pandas as pd
import numpy as np
import joblib

#Load trained model and scaler
model = joblib.load('stroke_model.pkl')
scaler = joblib.load('scaler.pkl')

#App title
st.title(" Stroke Risk Prediction App")
st.markdown("Enter patient data to assess stroke risk.")

#Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 1, 100, 30)
hypertension = st.selectbox("Hypertension", ["No", "Yes"])
heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])
ever_married = st.selectbox("Ever Married", ["No", "Yes"])
work_type = st.selectbox("Work Type", ["Private", "Self-employed", "Govt_job", "children", "Never_worked"])
residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])
avg_glucose = st.number_input("Average Glucose Level", min_value=50.0, max_value=300.0, value=100.0)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=22.0)
smoking_status = st.selectbox("Smoking Status", ["formerly smoked", "never smoked", "smokes", "Unknown"])

# Encode inputs (same as training)
input_dict = {
    "gender": 1 if gender == "Male" else 0,
    "age": age,
    "hypertension": 1 if hypertension == "Yes" else 0,
    "heart_disease": 1 if heart_disease == "Yes" else 0,
    "ever_married": 1 if ever_married == "Yes" else 0,
    "work_type": {"Private": 2, "Self-employed": 3, "Govt_job": 0, "children": 1, "Never_worked": 4}[work_type],
    "Residence_type": 1 if residence_type == "Urban" else 0,
    "avg_glucose_level": avg_glucose,
    "bmi": bmi,
    "smoking_status": {"formerly smoked": 1, "never smoked": 2, "smokes": 3, "Unknown": 0}[smoking_status]
}

input_df = pd.DataFrame([input_dict])
scaled_input = scaler.transform(input_df)

# Predict
if st.button("Predict Stroke Risk"):
    prediction = model.predict(scaled_input)
    prob = model.predict_proba(scaled_input)[0][1] * 100

    if prediction[0] == 1:
        st.error(f"⚠️ High risk of stroke ({prob:.2f}% confidence)")
    else:
        st.success(f"✅ Low risk of stroke ({100 - prob:.2f}% confidence)")

# Visualization of stroke risk
st.subheader("🔬 Stroke Risk Confidence")

# Progress Bar
st.write("**Probability of Stroke:**")
st.progress(int(prob))

# Percent Display
st.metric(label="Stroke Risk (%)", value=f"{prob:.2f}%")

# Custom Text Indicator
if prob >= 75:
    st.warning("⚠️ Very High Risk! Immediate medical consultation recommended.")
elif prob >= 50:
    st.warning("⚠️ Moderate to High Risk. Monitor closely.")
elif prob >= 25:
    st.info("ℹ️ Low to Moderate Risk. Maintain a healthy lifestyle.")
else:
    st.success("✅ Low Risk. Keep up the good health!")

# Bar chart using st.bar_chart
st.write("**Probability Comparison**")
st.bar_chart(pd.DataFrame({
    "Risk Type": ["Stroke", "No Stroke"],
    "Probability (%)": [prob, 100 - prob]
}).set_index("Risk Type"))
