import streamlit as st
from navigation.signin import show_signin
from navigation.signup import show_signup
from navigation.show_dashboard import show_Dashboard
from navigation.home import show_home
# from test import test


st.set_page_config(page_title="Student Management system",page_icon='🎓')

# Set default page
if "page" not in st.session_state:
    st.session_state.page = "Home"


# Navigation sidebar
with st.sidebar:
    st.title("🔐 School Management")
    if "token" not in st.session_state:
        if st.button("Home"):
            st.session_state.page = "Home"
        if st.button("Sign In"):
            st.session_state.page = "Sign In"
        if st.button("Sign Up"):
            st.session_state.page = "Sign Up"
        # st.rerun()
      

    else:
        if st.button("Dashboard"):
            st.session_state.page = "Dashboard"
        if st.button("Logout"):
            st.session_state.pop("token", None)
            st.session_state.page = "Sign In"
            st.rerun()

if st.session_state.page == "Sign In":
    show_signin()
elif st.session_state.page == "Sign Up":
    show_signup()
elif st.session_state.page == "Dashboard":
    show_Dashboard()
elif st.session_state.page =='Home':
    show_home()
    


