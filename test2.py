import streamlit as st
from supabase import create_client, Client
import os

# Supabase 설정
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

# 페이지 설정
st.set_page_config(layout="wide")

st.image("./assets/banner.png", use_container_width=True)

# 세션 상태 초기화
if 'user' not in st.session_state:
    st.session_state['user'] = None

# 로그인 함수
def login():
    st.subheader("로그인")
    email = st.text_input("이메일", key="login_email")
    password = st.text_input("비밀번호", type="password", key="login_password")
    if st.button("로그인"):
        try:
            auth_response = supabase.auth.sign_in(email=email, password=password)
            st.session_state['user'] = auth_response.user
            st.success("로그인에 성공했습니다.")
        except Exception as e:
            st.error(f"로그인에 실패했습니다: {e}")

# 회원가입 함수
def signup():
    st.subheader("회원가입")
    email = st.text_input("이메일", key="signup_email")
    password = st.text_input("비밀번호", type="password", key="signup_password")
    password_confirm = st.text_input("비밀번호 확인", type="password", key="signup_password_confirm")
    if st.button("회원가입"):
        if password != password_confirm:
            st.error("비밀번호가 일치하지 않습니다.")
        else:
            try:
                auth_response = supabase.auth.sign_up({'email': email, 'password': password})                st.success("회원가입이 완료되었습니다. 로그인해주세요.")
            except Exception as e:
                st.error(f"회원가입에 실패했습니다: {e}")

# 메인 내용
def main():
    if st.session_state['user']:
        st.write(f"환영합니다, {st.session_state['user'].email}님")
        if st.button("로그아웃"):
            supabase.auth.sign_out()
            st.session_state['user'] = None
            st.success("로그아웃되었습니다.")
    else:
        option = st.selectbox("메뉴 선택", ["로그인", "회원가입"])
        if option == "로그인":
            login()
        else:
            signup()

# 사이드바 설정
with st.sidebar:
    st.title("메뉴")
    main()