import streamlit as st 
from prediction_helper import predict

st.set_page_config(
    page_title="Health Insurance Cost Predictor",
    layout="wide",
)


st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #1e1e2f, #2c3e50);
            color: #f0f0f0;
            padding: 2rem;
        }

        h1 {
            color: #f9fafb;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
        }

        .block-container {
            padding: 1rem 2rem;
        }

        .stNumberInput input, .stSelectbox div[data-baseweb="select"] {
            background-color: #2a2a40;
            color: white;
            border-radius: 8px;
            border: 1px solid #4b5563;
        }

        label {
            color: #e5e7eb !important;
        }

        .st-expander {
            background-color: #1f2937 !important;
            border-radius: 10px;
            padding: 10px;
        }

        .stButton>button {
            background-color: #3b82f6;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            padding: 0.6em 1.5em;
            border: none;
        }

        .stButton>button:hover {
            background-color: #2563eb;
        }

        div[data-testid="stAlert-success"] {
            background-color: #d1fae5 !important;
            color: #065f46 !important;
            font-weight: bold;
            border-radius: 10px;
            padding: 15px;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)


st.title('Health Insurance Cost Predictor')


categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}


with st.expander("🧾 Basic Information", expanded=True):
    row1 = st.columns(3)
    with row1[0]:
        age = st.number_input('Age', min_value=18, step=1, max_value=100)
    with row1[1]:
        number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
    with row1[2]:
        income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)

    row2 = st.columns(3)
    with row2[0]:
        genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
    with row2[1]:
        insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
    with row2[2]:
        employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

with st.expander("🩺 Medical & Lifestyle", expanded=True):
    row3 = st.columns(3)
    with row3[0]:
        gender = st.selectbox('Gender', categorical_options['Gender'])
    with row3[1]:
        marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
    with row3[2]:
        bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

    row4 = st.columns(3)
    with row4[0]:
        smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
    with row4[1]:
        region = st.selectbox('Region', categorical_options['Region'])
    with row4[2]:
        medical_history = st.selectbox('Medical History', categorical_options['Medical History'])


input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

if st.button('Predict'):
    prediction = predict(input_dict)
    st.markdown(f"""
        <div style="background-color: #d1fae5; padding: 1rem; border-radius: 10px; border-left: 6px solid #10b981; margin-top: 1rem;">
            <p style="margin: 0; font-size: 1.2rem; font-weight: bold; color: #065f46;">
                Predicted Health Insurance Cost: ₹ {prediction} 
            </p>
        </div>
    """, unsafe_allow_html=True)