import streamlit as st

st.set_page_config(page_title="First Page", page_icon=":dolphin:",layout="wide",initial_sidebar_state="collapsed")

st.header("Streamlit")
st.subheader("Sub Header Line")

st.write("write")

st.text_input("Name",placeholder="Enter your Name")
st.number_input("Number",min_value=10,max_value=90)
st.text_area("Description")
st.date_input("DOB")


st.divider()
col1, col2, col3 = st.columns((1,1,1))

with col1:
    st.text_input("Name",placeholder="Enter your Name",key="name")
with col2:
    st.date_input("Date of Birth")
with col3:
    st.radio("Gender",options=['Male','Female'],horizontal=True)


st.checkbox("Terms and Conditions")

btn = st.button("Save")

if btn:
    st.success("Information save")
    st.balloons()

st.selectbox("Tech",options=['ML/AI','Software Development','Frontend','Backend','Embedded System'])

st.info("Information")
st.error("Error")

exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

st.image("https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",width=500)