import streamlit as st

from forms.contact import contact_form

st.title("계정정보")

@st.dialog("문의하기")
def show_contact_form():
    contact_form()

if st.button("문의하기"):
    show_contact_form()

