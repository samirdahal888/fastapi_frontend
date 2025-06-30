import streamlit as st
import requests
import os 
from dotenv import load_dotenv
load_dotenv()
from config import API_URL
print(API_URL)
# API_URL="http://127.0.0.1:8000"


def show_signin():
    """
    Sign in section for Admin 
    
    
    """
    st.subheader("🔐 Admin Sign In")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        data = {"username": username, "password": password}
        res = requests.post(f"{API_URL}/Admin/login", data=data)


        if res.status_code == 200:
            token = res.json()["access_token"]
            st.session_state.token=token
            st.success('Login successfully')
            st.session_state.page= "Dashboard"
            st.rerun()

        else:
            st.error("Invalid credentials")

       
