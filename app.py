# Credit Risk Prediction - Streamlit UI (run train.py first)

import streamlit as st
import pandas as pd
import pickle

# Load saved models and data
data = pickle.load(open('model.pkl', 'rb'))
models = data['models']
scaler = data['scaler']
columns = data['columns']
results = data['results']

st.title("Credit Risk Prediction System")

# ---------- Input fields ----------
col1, col2 = st.columns(2)

with col1:
    loan_amnt = st.number_input("Loan Amount ($)", value=10000.0)
    int_rate = st.number_input("Interest Rate (%)", value=12.5)
    annual_inc = st.number_input("Annual Income ($)", value=60000.0)
    dti = st.number_input("Debt-to-Income Ratio", value=15.0)
    fico = st.number_input("FICO Score", value=700.0)

with col2:
    emp_length = st.number_input("Employment Length (yrs)", value=5.0)
    term = st.selectbox("Term (months)", [36, 60])
    grade = st.selectbox("Grade", ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    home_ownership = st.selectbox("Home Ownership", ['RENT', 'MORTGAGE', 'OWN'])
    purposes = sorted(c.replace('purpose_', '') for c in columns if c.startswith('purpose_'))
    purpose = st.selectbox("Purpose", purposes)

model_name = st.selectbox("Select Model", list(models.keys()))

# ---------- Prediction ----------
if st.button("Predict Risk"):
    x = dict.fromkeys(columns, 0)
    x['loan_amnt'] = loan_amnt
    x['int_rate'] = int_rate
    x['annual_inc'] = annual_inc
    x['dti'] = dti
    x['fico_range_low'] = fico
    x['emp_length'] = emp_length
    x['term'] = term
    x['grade'] = 'ABCDEFG'.index(grade) + 1
    x['home_ownership_' + home_ownership] = 1
    x['purpose_' + purpose] = 1

    X = scaler.transform(pd.DataFrame([x])[columns])
    prob = models[model_name].predict_proba(X)[0][1]

    st.subheader(f"Default Probability: {prob*100:.1f}%")
    if prob < 0.4:
        st.success("LOW RISK - Approve Loan")
    elif prob < 0.6:
        st.warning("MEDIUM RISK - Review Carefully")
    else:
        st.error("HIGH RISK - Reject Loan")

# ---------- Model Comparison ----------
st.subheader("Model Performance Comparison")
st.dataframe(results, hide_index=True)
st.bar_chart(results.set_index('Model'))
