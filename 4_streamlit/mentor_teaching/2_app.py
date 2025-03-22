import streamlit as st 
from streamlit_option_menu import option_menu

st.set_page_config("Menu Bar", layout='wide')
st.selectbox("Country",options=['India','Pakistan','America','Dubai','China'], index=2)

st.select_slider("Age",options=[10,20,30,40,50])

st.slider("Age",max_value=50, min_value=10)

with st.sidebar:
    st.header("Menu Bar")
    option= st.selectbox("Option Menu", options=['Home','About','Blog'])
    
print(option)

if option=="Home":
    st.header("Home Page")

elif option=="About":
    st.header("About Page")
else:
    st.header("Blog Page")

#option_menu("Main Menu",options=['Home','Blog','About','Contact'],orientation='horizontal', menu_icon='list'  , icons=['house','pencil', 'info-circle','telephone'])
option_menu("",options=['Home','Blog','About','Contact'],orientation='horizontal',  icons=['house','pencil', 'info-circle','telephone'])

#st.image('post-1.jpg', width=200)
#st.video('')
#st.audio('')
