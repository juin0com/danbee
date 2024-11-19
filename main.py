import os
import streamlit as st
from supabase import create_client, Client

# page setup
st.set_page_config(layout="wide")
st.logo("./assets/logo_05.png",size="large")
@st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()

# @st.cache_resource(ttl=600)
# def run_query():
#     return supabase.table("mytable").select("*").execute()
# rows = run_query()


st.image("./assets/banner.png", use_container_width=True)

# Session state initialization
if "user" not in st.session_state:
    st.session_state["user"] = None


@st.dialog("로그인")
def login():
    email = st.text_input("이메일", key="login_id")
    password = st.text_input("비밀번호", key="login_pw")
    if st.button("전송", key="login_dialog_btn"):
        try:
            auth_reaponse = supabase.auth.sign_in(email=email, password=password)
            st.session_state["user"] = auth_reaponse.user
            st.success("로그인이 성공하였습니다.")
        except Exception as e:
            st.error(f"로그인에 실패했습니다. : {str(e)}")

@st.dialog("회원가입") 
def signup():
    email = st.text_input("이에일", key="signup_id")
    password = st.text_input("비밀번호", type="password", key="signup_pw")
    password_confirm = st.text_input("비밀번호 확인", type="password", key="signup_pw_confirm")
    if st.button("회원가입", key="signup_dialog_btn"):
        if password != password_confirm:
            st.error("비밀번호가 일치하지 않습니다.")
        else:
            try:
                auth_response = supabase.auth.sign_up(email=email, password=password)
                st.success("회원가입이 완료되었습니다.")
                st.markdown("다시 로그인을 해주세요.")
                st.balloons()
            except Exception as e:
                st.error(f"회원가입에 실패했습니다. : {str(e)}")
        # 회원가입 처리 로직 추가 for supabase
        st.success("회원가입이 완료되었습니다.")
        st.markdown("다시 로그인을 해주세요.")
        st.balloons()

# Sidebar setup
with st.sidebar:
    st.header("계정정보")     
    col1, col2 = st.columns(2)
    with col1:
        if st.button("로그인", key="sidebar_login_btn"):
            # 로그인 처리 로직 추가
            login()
            pass
    with col2:
        if st.button("회원가입", key="sidebar_signup_btn"):
            # 회원가입 처리 로직 추가 
            signup()
            pass

# 구분선 추가
st.divider()

# PAGE SETUP
about_page = st.Page(
    page="views/about.py",
    title="단비노트에 대해서",
    icon=":material/account_circle:",
)
search_word_page = st.Page(
    page="views/search_word.py",
    title="단어검색",
    icon=":material/search:",
    default=True,
)
recommend_word_page = st.Page(
    page="views/recommend_word.py",
    title="추천단어",
    icon=":material/featured_play_list:",
)
history_word_page = st.Page(
    page="views/history_word.py",
    title="이전학습단어",
    icon=":material/import_contacts:",
)
statistic_word_page = st.Page(
    page="views/statistic_word.py",
    title="학습통계",
    icon=":material/insert_chart_outlined:",
)

# Navigation setup with sections
pg = st.navigation(
    {
        "단비노트": [about_page],
        "단어검색": [search_word_page, recommend_word_page, history_word_page],
        "학습통계": [statistic_word_page],
    }
)

# shared on all pages
st.sidebar.text("단비노트에서 나만의 단어장을 만들어보세요!")


# Run navigation
pg.run()