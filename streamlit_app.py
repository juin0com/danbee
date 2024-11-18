import streamlit as st

st.image("./assets/banner.png", use_container_width=True)

# PAGE SETUP
about_page = st.Page(
    page="views/about.py",
    title="단비노트",
    # icon="👤",
    icon=":material/account_circle:",
)
search_word_page = st.Page(
    page="views/search_word.py",
    title="단어검색",
    # icon="🔍",
    icon=":material/search:",
    default=True,
)
recommend_word_page = st.Page(
    page="views/recommend_word.py",
    title="추천단어",
    # icon="✌️",
    icon=":material/featured_play_list:",
)
history_word_page = st.Page(
    page="views/history_word.py",
    title="이전학습단어",
    # icon="📖",
    icon=":material/import_contacts:",
)
statistic_word_page = st.Page(
    page="views/statistic_word.py",
    title="학습통계",
    # icon="📊",
    icon=":material/insert_chart_outlined:",
)

# Navigation setup
# pg = st.navigation(pages=[account_page, recommend_word_page, history_word_page, statistic_word_page])

# Navigation setup with sections
pg = st.navigation(
    {
        "계정": [about_page],
        "단어검색": [search_word_page, recommend_word_page, history_word_page],
        "학습통계": [statistic_word_page],
    }
)

# shared on all pages
#st.logo("assets/banner.png")
st.sidebar.text("단비노트에서 나만의 단어장을 만들어보세요!")

# Run navigation
pg.run()
