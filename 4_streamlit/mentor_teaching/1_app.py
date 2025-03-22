import streamlit as st 

st.set_page_config("HomePage", page_icon=":horse_racing:",)

st.header("First Page")
st.subheader("Sub heading")

st.text_input("Name", placeholder='Enter Name here...')

st.number_input("Age")

st.text_area("Description")
st.date_input("Select your DOB")

st.write("Hello This is Gurminder")


btn= st.button("Save")

if btn:
    # st.success("Button clicked")
    st.balloons()
    

# age= st.number_input("Enter Your Age ", min_value=10, max_value=90, disabled=)
age= st.number_input("Enter Your Age ", min_value=10, max_value=90)


st.radio("Gender",options=['Male','Female'],horizontal=True )
st.checkbox("Accept terms and conditions")

if st.button("Check Eligibilty"):
    st.success("You're Eligible")
    st.write("Your age is ",age)
    
    
# col1, col2= st.columns((1,1))
col1, col2= st.columns((2,1))

with col1:
     st.text_input("Enter Name", placeholder='Enter Name here...', key='name')

with col2:
    st.number_input("Age", key='age')