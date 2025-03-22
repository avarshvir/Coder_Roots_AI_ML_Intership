import streamlit as st
import base64
import requests

st.set_page_config("Weather Page", page_icon=":sun_small_cloud:")



with open('img-1.jpg','rb') as f:
    data=f.read()
imgs= base64.b64encode(data).decode()

# css=f"""
#     <style>
#     [data-testid="stAppViewContainer"]{{
#         background-image: url('data:image/png;base64,{imgs}');
#         background-size:cover
#     }}
#     [data-testid="stButton"]{{
#         color:yellow
#     }}
#     </style>
# """
css=f"""
    <style>
    .vi{{
        position:fixed;
        min-width:100%;
        min-height:100%;
        right:0;
        botton:0
        
    }}
    
    </style>
    
    <video autoplay loop muted  class="vi">
    <source src="https://cdn.discordapp.com/attachments/1255732288021594145/1350320700279226448/file_example_MP4_480_1_5MG_1.mp4?ex=67d64fa6&is=67d4fe26&hm=2d3dc84fbc10aa8d8de1e397e179064b01b063cc442c22d08b323141f16c8b6e&"  type="video/mp4">
    </video>
"""

# st.button("Save Button")
st.markdown(css, unsafe_allow_html=True)

st.title("Weather App")

API_KEY="api_key"
city="Mohali"
lat=30.7046
lon=76.7179
# api_address="https://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=" + API_KEY
api_address=f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY}"

res= requests.get(api_address)

st.write(res.json())