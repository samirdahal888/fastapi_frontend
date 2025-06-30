import streamlit as st
import requests
import os 
from dotenv import load_dotenv
load_dotenv()
from config import API_URL

def show_signup():
    st.subheader("📝 Sign Up")
    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type="password")

    if st.button("Create Account"):
        res = requests.post(f"{API_URL}/Admin", json={
            "username": username,
            "password": password
        })

        if res.status_code == 200:
            st.success("Account created! Go to Sign In.")
        else:
            st.error(res.json().get("detail", "Something went wrong."))


