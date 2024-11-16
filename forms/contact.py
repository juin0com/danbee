import streamlit as st

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("이름")
        email = st.text_input("이메일")
        message = st.text_area("문의내용")
        submit_button = st.form_submit_button("문의하기")

        if submit_button:
            st.success("문의가 성공적으로 접수되었습니다.")