"""import streamlit as st
import requests

st.title("Live currency convertor")
amount = st.number_input("Enter the amount in INR", min_value=1)
target_currency = st.selectbox("Conver to:", ["USD", "EUR", "GBP", "JPY"])


if st.button("Convert"):
    url= 
    response=requests.get(url)


    if response.status_code == 200:
        data = response.json()
        rate = data ["rates"][target_currency]
        converted = rate * amount
        st.success (f"{amount} INR = {converted} {target_currency}")
    else:
        st.error("Failled to fetch the coversion rate")"""