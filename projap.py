from click import option
import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
import pickle
import pandas as pd

#1

st.sidebar.title('Car Price Prediction')
html_temp = """
<div style="background-color:blue;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit Projapp(assigment)</h2>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)


#2

car_model=st.sidebar.selectbox("Select model of your car",("A1","A2", "A3", "Opel Astra","Opel Insignia","Opel Corsa","Renault Clio","Renault Escape","Renault Duster"))
km = st.sidebar.slider("What is the km of your car", 0,200000, step=500)
age = st.sidebar.selectbox("What is the age of your car:",(0,1,2,3,4))
hp_kW = st.sidebar.slider("What is the hp of your car?", 60, 200, step=5)

#3


model_name=="XGBOOST":
model=pickle.load(open("xgb_modelc.zip","rb")) 
   

#4
my_dict = {
    "make_model":car_model,
    "km": km,
    "age": age,
    "hp_kW": hp_kW,    
}

df=pd.DataFrame.from_dict([my_dict])

#5
columns= ['age','hp', 'km',"A1","A2", "A3", "Opel Astra","Opel Insignia","Opel Corsa","Renault Clio","Renault Escape","Renault Duster"]

df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)

#6
st.subheader("Press predict if configuration is okay")

if st.button("Predict"):
    prediction = model.predict(df)
    st.success("The estimated price of your car is €{}. ".format(int(prediction[0])))