import streamlit as st
import requests

data =requests.get("https://appfake.azurewebsites.net/data").json()

st.title("suuuuuuuuuuuuu")

if st.button("getdata"):

    st.write(data)
