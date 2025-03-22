import streamlit as st

st.set_page_config(page_title="Input Form",page_icon=":symbols:",layout="wide")

st.header("Sign up form")
st.divider()

col1, col2, col3 = st.columns((1,1,1))

with col1:
    first_name = st.text_input("First Name",placeholder="e.g. john")

with col2:
    mid_name = st.text_input("Middle Name",placeholder="e.g. doe")

with col3:
    last_name = st.text_input("Last Name",placeholder="e.g william")

col4, col5, col6 = st.columns((1,1,1))

with col4:
    email = st.text_input("Email",placeholder="e.g. example@gmail.com")

with col5:
    gender = st.radio("Gender",options=['Male','Female','Other'],horizontal=True)

with col6:
    dob = st.date_input("Date of Birth")

col7, col8, col9 = st.columns((1,1,1))

with col7:
    p_lang = st.multiselect("Programming Language",options=['Assembly','C','C++','Java','Python','Embedded C','MicroPython','Arduino C'])

with col8:
    role = st.radio("Role",options=['AI/ML Engineer','Embedded Engineer','Software Engineer','Robotics Engineer'], horizontal=True)

with col9:
    tools = st.multiselect("Tools and Frameworks",options=['Proteus','TensorFlow','Arduino/Raspberry Pi','Cortex ARM','PyTorch/TensorFlow/Kerad','Electronics Sensors','Computer Vision','NLP'])

st.markdown("### Upload your resume")
resume = st.file_uploader("resume",type=['pdf','docs'])


btn = st.button("Save Information",type="primary")

if btn:
    st.success("Info saved successfully")
    st.balloons()
    #st.switch_page("pages/3_user_info.py")

    st.divider()

    st.write("Name: ",first_name, mid_name, last_name)
    st.write("Email: ", email)
    st.write("Gender: ",gender)
    st.write("Programming Language: ",p_lang)
    st.write("Date of Birth: ", dob)
    st.write("Tools: ",tools)
    
    st.write("Programming Language")
    for lang in p_lang:
        st.write(f"- {lang}")