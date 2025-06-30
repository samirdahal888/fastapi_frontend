 # Streamlit helper functions for API calls
#CRUD Operation for student 

import streamlit as st
import requests
from config import API_URL



def get_students(token):
        
        '''This function helps to communicate with API end point and help to get all the students
        present in the database

        token :JWT token for verification - only proper token can access the content , if not then raise error
        
        '''

        headers = {"Authorization": f"Bearer {token}"}
        try:
            r = requests.get(f"{API_URL}/student", timeout=5,headers=headers)

            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            st.error(f"Error fetching  students: {e}")
            return []
        

def create_student(name: str, age: int,rollno:int,password:str,token):
    '''
    This is the function that helps to create the student aftew varifying the token
    
    '''
    headers = {"Authorization": f"Bearer {token}"}

    payload = {"name": name, "age": age,"rollno":rollno,"password":password}
    try:
        r = requests.post(f"{API_URL}/student", json=payload, timeout=5,headers=headers)
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        st.error(f"Error creating hero: {e}")
        return None
    
def update_student(student_id:int,name: str, age: int,rollno:int,username:str,password:str,token):
    ''' 
    Update Function That will help to update students
    
    '''
    headers = {"Authorization": f"Bearer {token}"}

    payload = {"name": name, 
                "age": age,
                "rollno":rollno,
                "username":username,
                "password":password}
    try:
        r = requests.patch(f"{API_URL}/student/{student_id}", json=payload, timeout=5,headers=headers)
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        st.error(f"Student ID is not present in database")
        return None
    
def Delet_Student(student_id:int,token):

    '''
    This function help to delet the student with the student id
    
    '''
    headers = {"Authorization": f"Bearer {token}"}

    try:
        r = requests.delete(f"{API_URL}/student/{student_id}", timeout=5,headers=headers)
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        st.error(f"Student ID is not present in database")
        return None
