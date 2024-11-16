import streamlit as st

add_selectbox = st.sidebar.selectbox(
    '어떤 단어가 궁금하십니까?',
    (
        # {
        #     'school', 'study', 'teacher', 'homework',
        # },
        # {
            'deficit', 'inflation', 'president','friction','peripheral','addition',
          'fragment', 'versetile', 'anatomy', 'terminology',
        # },
    )
)

add_slider = st.sidebar.slider(
    '난이도를 선택하세요~',
    0, 10,(5)
)