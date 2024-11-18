import os
import streamlit as st
from supabase import create_client

#Supabase setup
supabase_url = os.environ.get("SUPABASE_URL")
supaabse_key = os.environ.get("SUPABASE_KEY")
# supabase = create_client(supabase_url, supabase_key)

# page setup
st.set_page_config(layout="wide")

st.image("./assets/banner.png", use_container_width=True)

@st.dialog("로그인")
def login():
    st.text_input("아이디", key="login_id")
    st.text_input("비밀번호", key="login_pw")
    if st.button("로그인", key="login_dialog_btn"):
        # 로그인 처리 로직 추가
        pass

@st.dialog("회원가입") 
def signup():
    st.text_input("아이디", key="signup_id")
    st.text_input("비밀번호", key="signup_pw")
    st.text_input("비밀번호 확인", key="signup_pw_confirm")
    if st.button("회원가입", key="signup_dialog_btn"):
        # 회원가입 처리 로직 추가
        pass

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