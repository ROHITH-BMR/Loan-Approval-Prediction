#streamlit run app.py

import pickle
import streamlit as st
import numpy as np
from datetime import date



st.title("Loan Approval Prediction")
name = st.text_input("Applicant Name")
age = st.number_input("Age",min_value=18,max_value=65)
dob = st.date_input("Date-of-Birth",min_value=date(1900,1,1),max_value=date.today())
gender = st.radio("Gender",("Male","Female"))
education = st.radio("Education",('Educated','Uneducated'))
employed = st.radio("Employment",('Salaried','Self-employed','Un-employed'))
income = st.number_input("Annual Income")
cibil_score = st.number_input("Cibil Score")

#gender
if gender == "Male":
    gender = 1
else:
    gender = 0

#education
if education == "Educated":
    education = 1
else:
    education = 0
    
#employed
if employed == "Salaried":
    employed = 1
elif employed == "Self-employed":
    employed = 2
else:
    employed = 3

#income
if employed == 1 and income / 12 > 15000:
    income = 1
elif employed == 2 and income > 300000:
    income = 1
else:
    income = 0
    
if cibil_score > 600 and income == 1:
    cibil_score = 1
else:
    cibil_score = 0


if st.button("Predict"):
    if age < 18 and age > 60 and employed == 1:
        cibil_score = 0
        st.write("Sorry, your age is not elligible...")
    
    if age < 21 and age > 65 and employed == 2:
        cibil_score = 0
        st.write("Sorry, your age is not elligible...")
    
    model = pickle.load(open('LogisticRegression.pkl','rb'))
    
    custom_input = [cibil_score,education,gender]
    
    prediction = model.predict([np.array(custom_input)])
    
    if prediction == 1:
        st.header("You Are Elligible !")
    elif prediction == 0:
        st.header("Sorry, You Are Not Elligible...")
    
