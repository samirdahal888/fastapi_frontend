#for background image

import streamlit as st
import base64
def get_base64(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()


def set_background(background_image):
    img_base64 = get_base64(background_image)

    st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{img_base64}");
                background-size: cover;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )