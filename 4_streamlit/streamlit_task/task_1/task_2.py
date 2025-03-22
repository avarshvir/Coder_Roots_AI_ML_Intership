"""2. Create a Streamlit multi-page application using streamlit-option-menu for navigation. 
The app should have multiple pages with different functionalities.
Requirements:
Home Page:
Displays a welcome message and an overview of the app.
Task Manager Page:
A form to add tasks with fields like task name, description, priority, and due date.
Displays a list of submitted tasks.
Functionality:
Users navigate between pages using an option menu in the sidebar."""

import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Multi Page App", layout="wide")
with st.sidebar:
    st.title("Menu Bar")
    selected = option_menu(
        menu_title=None,
        options=["Home", "Task Manager"],
        icons=["house", "list-task"],
    )

if selected == "Home":
    st.title("Welcome to task management app")

elif selected == "Task Manager":
    st.title("Task Management form")

    task_in = st.text_input(label="Enter your task",placeholder="e.g. buy vegetables at 7 pm.")

    task_des = st.text_area(label="Enter you task description",placeholder="e.g. buy vegetable from ram shop and vegetables must be fresh.")

    task_pri = st.radio(label="How Important this task ?",options=['not important','somewhat important','most important'],horizontal=True)

    task_date = st.date_input(label="Due Date")

    task_com = st.checkbox(label="Task is completed")

    task_sub = st.button(label="Submit")

    if(task_sub):
        if not task_in:
            st.error("Plese Enter task name")
        else:
            st.success("task successful")
            st.balloons()
    
            st.divider()
            st.subheader("Task summary")
            st.write("Task Name:",task_in)
            st.write("Task Description: ",task_des)
            st.write("Task Priority: ",task_pri)
            st.write("Due Date: ",task_date)
            st.write("Completion status: ","completed" if task_com else "Not completed")





