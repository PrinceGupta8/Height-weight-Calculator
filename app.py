import pandas as pd
import streamlit as st
import pickle

data=pd.read_csv('height_weight_data.csv')
st.title('Height Weight Calculator')
height=st.text_input('Height')
if height:
    lr_model=pickle.load(open('data.pkl','rb'))
    standard_scaler=pickle.load(open('scaler.pkl','rb'))
    new_data_scaled=standard_scaler.transform([[height]])
    result=lr_model.predict(new_data_scaled)

    st.write(f'Your weight should be: {result[0].round(2)} kg')
    #st.write(result[0])
