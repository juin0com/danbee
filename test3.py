import streamlit as st
from supabase import create_client, Client

@st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()

# 세션 상태 초기화
if "user" not in st.session_state:
    st.session_state["user"] = None

# 로그인 Dialog
@st.dialog("로그인")
def login():
    email = st.text_input("이메일", key="login_email")
    password = st.text_input("비밀번호", type="password", key="login_password")
    if st.button("로그인", key="login_button"):
        try:
            auth_response = supabase.auth.sign_in_with_password({'email': email, 'password':password})
            st.session_state["user"] = auth_response.user
            st.success("로그인에 성공하였습니다.")
        except Exception as e:
            st.error(f"로그인에 실패하였습니다: {str(e)}")

# 회원가입 Dialog
@st.dialog("회원가입")
def signup():
    email = st.text_input("이메일", key="signup_email")
    password = st.text_input("비밀번호", type="password", key="signup_password")
    password_confirm = st.text_input("비밀번호 확인", type="password", key="signup_password_confirm")
    if st.button("회원가입", key="signup_button"):
        if password != password_confirm:
            st.error("비밀번호가 일치하지 않습니다.")
        else:
            try:
                auth_response = supabase.auth.sign_up({"email": email, "password": password})
                st.success("회원가입에 성공하였습니다.")
                st.rerun()
            except Exception as e:
                st.error(f"회원가입에 실패하였습니다: {str(e)}")

# 메인 화면
st.image("./assets/banner.png", use_container_width=True)

if st.session_state["user"] is None:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("로그인"):
            login()
    with col2:
        if st.button("회원가입"):
            signup()
else:
    st.write(f"안녕하세요, {st.session_state['user']['email']}님!")
    if st.button("로그아웃"):
        st.session_state["user"] = None
        st.success("로그아웃되었습니다.")