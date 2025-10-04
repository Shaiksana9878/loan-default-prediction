import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

# Load trained model
model = joblib.load("model.pkl")

st.title("💰 Loan Default Prediction App")

# ---------------- Input fields ----------------
income = st.number_input("Applicant Income", min_value=0.0, value=50000.0)
loan_amount = st.number_input("Loan Amount", min_value=0.0, value=100000.0)
term = st.selectbox("Term (months)", [12, 36, 60])

# Prepare DataFrame with all expected columns
user_data = pd.DataFrame({
    "income": [income],
    "loan_amount": [loan_amount],
    "term": [term],
    # You can add more fields from your dataset as needed
})

# ---------------- Preprocessing ----------------
# Handle missing values
imputer = SimpleImputer(strategy='most_frequent')
user_data = pd.DataFrame(imputer.fit_transform(user_data), columns=user_data.columns)

# Example: label encode categorical columns if needed
categorical_cols = ["term"]  # add more if needed
for col in categorical_cols:
    user_data[col] = LabelEncoder().fit_transform(user_data[col].astype(str))

# One-hot encode low-cardinality columns
user_data = pd.get_dummies(user_data, drop_first=True)

# Ensure user_data has same columns as model
for col in model.feature_names_in_:
    if col not in user_data.columns:
        user_data[col] = 0
user_data = user_data[model.feature_names_in_]

# ---------------- Predict ----------------
if st.button("Predict"):
    prediction = model.predict(user_data)[0]
    probability = model.predict_proba(user_data)[:, 1][0]

    st.subheader("Prediction")
    if prediction == 1:
        st.error("⚠️ Loan will Default")
    else:
        st.success("✅ Loan will NOT Default")

    st.subheader("Default Probability")
    st.write(f"{probability*100:.2f}%")

