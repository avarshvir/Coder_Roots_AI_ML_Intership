"""1. Create a Streamlit-based form where users can submit task details. 
The form should include the following elements:

Task Name: A text input field to enter the task name.
Task Description: A text area for detailed task information.
Priority Selection: A radio button to select the priority level (Low, Medium, High).
Due Date: A date picker to select the deadline.
Completion Status: A checkbox to mark if the task is completed.
Submit Button: On submission, the entered details should be displayed as a summary.


Expected Functionality:
Users fill out the form and click submit.
A success message appears upon submission.
The task details are displayed dynamically below the form."""

import streamlit as st

st.set_page_config(page_title='Task Manager', layout="wide")
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
