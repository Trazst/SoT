import streamlit as st
import os

# https://github.com/megadose/holehe
# https://github.com/soxoj/maigret
# https://github.com/megadose/ignorant

st.set_page_config(page_title="Streamlit OSINT Tool", layout="wide", page_icon=":tada:")

#with st.container():
#  st.markdown("<h1 style='text-align: center; color: grey;'>OSINT</h1>", unsafe_allow_html=True)
#  st.write("##")

with st.container():
  st.write("---")
  col_1, col_2 = st.columns(2)
  with col_1:
    st.write("""
     # Streamlit OSINT Tool
     Testing *holehe, maigret & ignorant* using **streamlit**
     """)
    emailInput = st.text_input("Enter e-mail", "…")
    if(st.button("Start holehe")):
      email = emailInput.title()
      st.text("Search started for "+email)
    nicknameInput = st.text_input("Enter nickname", "…")
    if(st.button("Start maigret")):
      nickname = nicknameInput.title()
      st.text("Search started for "+nickname)
    phoneInput = st.text_input("Enter phone number 32 412345678", "…")
    if(st.button("Start ignorant")):
      phone = phoneInput.title()
      st.text("Search started for "+phone)

  with col_2:
    st.image("https://th.bing.com/th/id/OIP.hYeGrnKXhFBetuYyy-sXlwHaHa?pid=ImgDet&rs=1")
  st.write("---")

with st.container():
  try:
    resultholehe=os.popen("holehe "+email).read()
    st.text(resultholehe)
    st.text("Search for "+email+" complete")
  except:
    pass

  try:
    resultmaigret=os.popen("maigret "+nickname).read()
    st.text(resultmaigret)
    st.text("Search for "+nickname+" complete")
  except:
    pass

with st.container():
  try:
    resultignorant=os.popen("ignorant "+phone).read()
    st.text(resultignorant)
    st.text("Search for "+phone+" complete")
  except:
    pass
