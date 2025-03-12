import streamlit as st

st.set_page_config(page_title="User Info", page_icon=":symbols:")

st.header("User Information")
st.divider()

if 'user_info' in st.session_state:
    user_info = st.session_state['user_info']

    st.write(f"**First Name:** {user_info['First Name']}")
    st.write(f"**Middle Name:** {user_info['Middle Name']}")
    st.write(f"**Last Name:** {user_info['Last Name']}")
    st.write(f"**Email:** {user_info['Email']}")
    st.write(f"**Gender:** {user_info['Gender']}")
    st.write(f"**Date of Birth:** {user_info['Date of Birth']}")

    st.write("### Programming Languages")
    st.write(", ".join(user_info['Programming Languages']) if user_info['Programming Languages'] else "None")

    st.write(f"**Role:** {user_info['Role']}")

    st.write("### Tools and Frameworks")
    st.write(", ".join(user_info['Tools and Frameworks']) if user_info['Tools and Frameworks'] else "None")

    if user_info['Resume']:
        st.write(f"**Resume:** {user_info['Resume']}")
else:
    st.warning("No user information found. Please fill out the form first.")

# Add a back button
if st.button("Back to Form"):
    st.switch_page("main.py")
