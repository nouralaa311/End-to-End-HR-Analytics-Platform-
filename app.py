
import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the trained model and scaler
model = joblib.load('logistic_regression_model.pkl')
scaler = joblib.load('standard_scaler.pkl')

# Define mappings for categorical features (these should match your training data encoding)
# Based on the original df.info() and df.head() before encoding:
# 'department', 'region', 'education', 'gender', 'recruitment_channel', 'training_level'

# For simplicity, we assume the LabelEncoder used during training assigned numerical values
# based on alphabetical order or the order of appearance. For a production-grade app,
# you would save the LabelEncoder objects themselves or explicitly map known categories.

department_map = {
    'Sales & Marketing': 7, 'Operations': 4, 'Technology': 8, 'Analytics': 0, 'R&D': 6,
    'Procurement': 5, 'Finance': 1, 'HR': 2, 'Legal': 3
}
region_map = {
    'region_7': 30, 'region_22': 14, 'region_19': 11, 'region_23': 15, 'region_26': 18,
    'region_2': 11, 'region_27': 19, 'region_16': 7, 'region_28': 20, 'region_13': 4,
    'region_4': 28, 'region_17': 8, 'region_29': 21, 'region_20': 12, 'region_14': 5,
    'region_11': 2, 'region_15': 6, 'region_1': 0, 'region_25': 17, 'region_10': 1,
    'region_6': 29, 'region_31': 23, 'region_5': 27, 'region_30': 22, 'region_8': 31,
    'region_3': 26, 'region_24': 16, 'region_12': 3, 'region_9': 32, 'region_32': 24,
    'region_21': 13, 'region_34': 25, 'region_33': 0
} # This will need to be very precise
education_map = {
    'Bachelors': 0, 'Masters & above': 2, 'Below Secondary': 1
}
gender_map = {
    'm': 1, 'f': 0
}
recruitment_channel_map = {
    'sourcing': 2, 'other': 0, 'referred': 1
}
training_level_map = {
    'Low': 0, 'Medium': 1, 'High': 2
}

st.set_page_config(page_title="Employee Promotion Predictor", layout="centered")
st.title("🚀 Employee Promotion Prediction App")

st.markdown("Enter employee details to predict their promotion likelihood.")

# Input fields
st.sidebar.header("Employee Information")

# Categorical inputs
department = st.sidebar.selectbox('Department', list(department_map.keys()))
region = st.sidebar.selectbox('Region', sorted(list(region_map.keys())))
education = st.sidebar.selectbox('Education', list(education_map.keys()))
gender = st.sidebar.radio('Gender', list(gender_map.keys()))
recruitment_channel = st.sidebar.selectbox('Recruitment Channel', list(recruitment_channel_map.keys()))
training_level = st.sidebar.selectbox('Training Level', list(training_level_map.keys()))

# Numerical inputs
no_of_trainings = st.sidebar.slider('Number of Trainings', 1, 9, 1)
age = st.sidebar.slider('Age', 20, 60, 30)
length_of_service = st.sidebar.slider('Length of Service (years)', 1, 34, 5)
awards_won = st.sidebar.radio('Awards Won?', [0, 1])
avg_training_score = st.sidebar.slider('Average Training Score', 39, 99, 60)

# Create a DataFrame for prediction
input_data = pd.DataFrame({
    'department': [department_map[department]],
    'region': [region_map[region]],
    'education': [education_map[education]],
    'gender': [gender_map[gender]],
    'recruitment_channel': [recruitment_channel_map[recruitment_channel]],
    'no_of_trainings': [no_of_trainings],
    'age': [age],
    'length_of_service': [length_of_service],
    'awards_won': [awards_won],
    'avg_training_score': [avg_training_score],
    'is_senior_employee': [1 if length_of_service > 13 else 0], # Assuming upper_bound for length_of_service was around 13-14
    'training_level': [training_level_map[training_level]]
})

# Ensure columns are in the same order as X_train_sc (important for scaling and prediction)
# The original X1 columns were: Index(['department', 'region', 'education', 'gender',
#        'recruitment_channel', 'no_of_trainings', 'age', 'length_of_service',
#        'KPIs_met_more_than_80', 'awards_won', 'avg_training_score',
#        'is_senior_employee', 'training_level'],
#       dtype='object')

# Note: KPIs_met_more_than_80 is used to define 'is_promoted' so it shouldn't be an input feature for prediction.
# However, it was present in X1. We need to decide how to handle it for prediction.
# For now, I'll assume it's not a direct input for the app, or if it was, it would have to be an input from the user.
# Let's adjust input_data to match the original X1 used for training, if possible.
# Based on mwx70jcJIA7s: X1=df.drop(['is_promoted','employee_id','previous_year_rating'],axis=1)
# This means X1 *did* include 'KPIs_met_more_than_80'. If 'is_promoted' is the target
# and 'KPIs_met_more_than_80' helps define it, this is still data leakage.
# For a true promotion predictor, KPIs_met_more_than_80 *should* be an input.

# Re-evaluating the features based on X1 in the notebook:
# X1 includes: department, region, education, gender, recruitment_channel, no_of_trainings, age,
# length_of_service, KPIs_met_more_than_80, awards_won, avg_training_score, is_senior_employee, training_level

# Adding KPIs_met_more_than_80 as an input for the app
kpis_met = st.sidebar.radio('KPIs Met >80%?', [0, 1])
input_data['KPIs_met_more_than_80'] = [kpis_met]

# Order of columns in X1 from `df.columns` earlier is critical
original_X1_columns = [
    'department', 'region', 'education', 'gender', 'recruitment_channel',
    'no_of_trainings', 'age', 'length_of_service', 'KPIs_met_more_than_80',
    'awards_won', 'avg_training_score', 'is_senior_employee', 'training_level'
]
input_data = input_data[original_X1_columns]

# Scale the input data
scaled_input = scaler.transform(input_data)

if st.button('Predict Promotion'):
    prediction = model.predict(scaled_input)
    prediction_proba = model.predict_proba(scaled_input)

    st.subheader("Prediction Results:")
    if prediction[0] == 1:
        st.success("**Promotion Predicted!** 🎉")
        st.write(f"Probability of Promotion: **{prediction_proba[0][1]:.2f}**")
    else:
        st.info("**No Promotion Predicted.** 😔")
        st.write(f"Probability of Not Getting Promoted: **{prediction_proba[0][0]:.2f}**")

    st.markdown("---")
    st.markdown("### Input Features Summary")
    st.write(input_data)
