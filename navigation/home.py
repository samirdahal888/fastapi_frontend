import streamlit as st

def show_home():
    st.set_page_config(page_title="School Management System", layout="wide")

    # Basic custom CSS
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500&display=swap');

        html, body, [class*="css"] {
            font-family: 'Quicksand', sans-serif;
            background: linear-gradient(135deg, #f0f8ff, #ffffff);
        }

        .main-title {
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            color: #0D47A1;
        }

        .subtitle {
            font-size: 20px;
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }

        .quote {
            font-style: italic;
            text-align: center;
            color: #555;
            margin-top: 30px;
        }

        .footer {
            text-align: center;
            font-size: 13px;
            color: #777;
            margin-top: 40px;
        }

        hr {
            border: 2px solid #1976D2;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="main-title">🎓 hello 🎓</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Empowering Students. Supporting Teachers. Streamlining Education.</div>', unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # Optional image (can be removed or replaced with valid path or URL)
    st.image("home_background.jpg")

    st.markdown("### 📌 About the System")
    st.markdown("""
    This School Management System helps manage:
    - 🧑‍🎓 Student Records (Admin Only)
    # How to use it 
    - If you are already sign up then just goto sign in section at the left
    - If not then do sign up first then sign in

    Our goal is to simplify administration and enhance learning for all.
    """)

    st.markdown('<div class="quote">“Education is the passport to the future, for tomorrow belongs to those who prepare for it today.” – Malcolm X</div>', unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown('<div class="footer">Made with ❤️ using Streamlit | Developed by Samir Dahal</div>', unsafe_allow_html=True)
