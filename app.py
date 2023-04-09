# Mengimpor library
import pandas as pd
import streamlit as st
import pickle

# Menghilangkan warning
import warnings
warnings.filterwarnings("ignore")

# Menulis judul
st.markdown("<h1 style='text-align: center; '> Loan Prediction </h1>", unsafe_allow_html=True)
st.markdown('---'*10)

# Baris Pertama
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        loan_id = st.number_input('Loan ID', value=1012)
    with col2:
        gender = st.selectbox('Gender',['Male','Female'])
    with col3:
        married = st.selectbox('Married',['Yes','No'])
        
# Baris Kedua
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        dependents = st.selectbox('Dependents',['0','1','2','>3'])
    with col2:
        education = st.selectbox('Education',['Graduate','Not Graduate'])
    with col3:
        self_employed = st.selectbox('Self-Employed',['Yes','No'])        
        
# Baris Ketiga
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        app_inc = st.number_input('Applicant Income', value=2000)
    with col2:
        coapp_inc = st.number_input('Coapplicant Income', value=1000)
    
# Baris Keempat
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        loan_amount = st.number_input('Loan Amount', value=50)
    with col2:
        loan_amount_term = st.number_input('Loan Amount Term', value=360)

# Baris Kelima
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        credit_history = st.selectbox('Credit History',['0','1'])
    with col2:
        property_area = st.selectbox('Property Area',['Semiurban','urban', 'Rural']) 

# Inference
data = {
        'Loan_ID': loan_id,
        'Gender': gender,
        'Married': married,
        'Dependents': dependents,
        'Education': education,
        'Self_Employed': self_employed,
        'ApplicantIncome': app_inc,
        'CoapplicantIncome': coapp_inc,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_amount_term,
        'Credit_History': credit_history,
        'Property_Area': property_area        
        }

# Tabel data
kolom = list(data.keys())
df = pd.DataFrame([data.values()], columns=kolom)

# Load model
my_model = pickle.load(open('model_klasifikasi_loan.pkl', 'rb'))

# Prediksi
hasil = my_model.predict(df)
keputusan = ''
if hasil == 0:
    keputusan = 'Reject!'
else:
    keputusan = 'Approve!'

# Memunculkan hasil di Web
cust_num = '0000'
st.write('<center><b><h3>Customer Loan ID', cust_num+str(loan_id),'</b></h3>', unsafe_allow_html=True)
st.write('<center><b><h3>Decision = ', keputusan,'</b></h3>', unsafe_allow_html=True)