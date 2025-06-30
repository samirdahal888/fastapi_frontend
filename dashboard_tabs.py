import streamlit as st
from api import get_students,create_student,update_student,Delet_Student


def view():
        st.subheader("Students in database")
        if st.button("Refresh list", use_container_width=True):
            st.rerun()
        students = get_students(st.session_state.token)
        if students:
            st.dataframe(students, use_container_width=True,hide_index=False)
        else:
                st.info("No studens found.")

def Add():
        st.subheader("Add a New student")
        with st.form("add_hero", clear_on_submit=True):
            name = st.text_input("Name", placeholder="e.g., Wonder Woman")
            age  = st.number_input("Age", min_value=0, step=1, value=0, format="%d")
            rollno = st.number_input('Roll number', value=0,format="%d")
            password = st.text_input("password",max_chars=10,type='password')
            submitted = st.form_submit_button("Create Student")
            if submitted:
                created = create_student(name,age,rollno,password,st.session_state.token)
                if created:
                    st.success(f"student created with ID {created['id']}")

def update():
    st.subheader("Update the student with studentID")

    with st.form("update_form"):
        Student_id = st.text_input("studentID",placeholder=1,value=0,max_chars=4)
        name = st.text_input("Name", placeholder="e.g., Wonder Woman")
        age  = st.number_input("Age", min_value=0, step=1, value=0, format="%d")
        rollno = st.number_input('Roll number', value=0,format="%d")
        username = st.text_input("username",placeholder=" your Full name")
        password = st.text_input("password",max_chars=10,type='password')
        save = st.form_submit_button("Save Changes")
        if save:
            updated = update_student(Student_id,name,age,rollno,username,password,st.session_state.token)
            if updated:
                st.success("Student updated.")
            else:
                st.info("No Student to update.")

def delete(): 
    st.subheader("Delete the student with studentID")
    with st.form("Delet with studentID"):
        Student_id = st.text_input("studentID",placeholder=1,value=0,max_chars=4)
        save = st.form_submit_button(f"Delet student with id {Student_id}")
        if save:
            delet = Delet_Student(Student_id,st.session_state.token)
            if delet:

                st.success(f"Student with id {Student_id} is deleted")
            else:
                st.info("Student  not  deleted")

    
