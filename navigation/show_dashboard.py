import streamlit as st
from api import get_students,update_student,Delet_Student,create_student
import base64
from set_background import set_background
from dashboard_tabs import view,Add,update,delete

def show_Dashboard()-> None:

    '''
    SHows the Dashboard with different tabs for CRUD oprtaion for students
    '''

    set_background('background.jpg')


    st.set_page_config(layout="wide", page_title="Student Manager", page_icon="📚")
    st.title("Student Management System")


    
    #tabs

    tabs = st.tabs(["🎯 View", "➕ Add", "✏️ Update", "🗑️ Delete"])

    with tabs[0]:
        view()
    with tabs[1]:
        Add()
    with tabs[2]:
        update()  
    with tabs[3]:
        delete()



    
