import streamlit as st
import joblib
import pandas as pd
model=joblib.load('adult_census_income.pkl')
st.set_page_config(page_title='adult_census_income',page_icon=':smiley:',layout='wide')
st.title("Adult Census Income")
st.write("Welcome to Adult Census Income Application!!!")
# 'age', 'workclass', 'education', 'education.num', 'marital.status',
    #   'occupation', 'relationship', 'race', 'sex', 'capital.gain',
      #  'capital.loss', 'hours.per.week', 'native.country'
age=st.number_input("enter age:")
workclass=st.selectbox('workclass',
                       ['Never-worked','Private','State-gov','Federal-gov', 'Self-emp-not-inc','Self-emp-inc','Local-gov','Without-pay'])
education=st.selectbox('education',['High-School','Dropout','School','Doctorate','Graduate','Bachelors','Masters','College','Preschool'])
education_num=st.number_input("enter education in years:")
marital_status=st.selectbox('marital.status',['Widowed', 'Divorced', 'Separated', 'Single', 'Married'])
occupation=st.selectbox('occupation',['Jobless','Exec-managerial', 'Machine-op-inspct','Prof-specialty','Other-service','Adm-clerical',
      'Craft-repair','Transport-moving','Handlers-cleaners','Sales',   'Farming-fishing',      'Tech-support',
   'Protective-serv','Armed-Forces','Priv-house-serv'])
relationship=st.selectbox('relationship',['Not-in-family', 'Unmarried', 'Own-child', 'Other-relative', 'Husband','Wife'])
race=st.selectbox('race',['White', 'Black', 'Asian-Pac-Islander', 'Other', 'Amer-Indian-Eskimo'])
sex=st.radio("Gender",['Female', 'Male'])
capital_gain=st.number_input("enter capital gain:")
capital_loss=st.number_input("enter capital loss:")
hours_per_week=st.number_input("enter no.of hours worked per week:")
native_country=st.selectbox("native.country",
               ['United-States',            'Unknown_country',
                     'Mexico',                     'Greece',
                    'Vietnam',                      'China',
                     'Taiwan',                      'India',
                'Philippines',            'Trinadad&Tobago',
                     'Canada',                      'South',
         'Holand-Netherlands',                'Puerto-Rico',
                     'Poland',                       'Iran',
                    'England',                    'Germany',
                      'Italy',                      'Japan',
                       'Hong',                   'Honduras',
                       'Cuba',                    'Ireland',
                   'Cambodia',                       'Peru',
                  'Nicaragua',         'Dominican-Republic',
                      'Haiti',                'El-Salvador',
                    'Hungary',                   'Columbia',
                  'Guatemala',                    'Jamaica',
                    'Ecuador',                     'France',
                 'Yugoslavia',                   'Scotland',
                   'Portugal',                       'Laos',
                   'Thailand', 'Outlying-US(Guam-USVI-etc)'])
if st.button("predict income"):
  input_data = pd.DataFrame({
    'age':[age],
    'workclass':[workclass],
    'education':[education],
    'education.num':[education_num],
    'marital.status':[marital_status],
    'occupation':[occupation],
    'relationship':[relationship],
    'race':[race],
    'sex':[sex],
    'capital.gain':[capital_gain],
    'capital.loss':[capital_loss],
    'hours.per.week':[hours_per_week],
    'native.country':[native_country]
      })
  # 1. Run the prediction on user input data
  prediction = model.predict(input_data)

  # 2. Extract the string result from the array
  result = prediction[0]

  # 3. Display the clean output to the user using Streamlit components
  if result == ">50K":
      st.success("Prediction: This individual likely earns **>50K $** per year.")
  else:
      st.info("Prediction: This individual likely earns **<=50K $** per year.")

