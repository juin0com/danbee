import streamlit as st

st.markdown(
    """
    <style>
    .stContainer {
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        input = st.text_input("단어를 입력하세요.", value="", label_visibility="collapsed")
    with col2:
        search_button = st.button("검색")
    placeholder = st.empty()
    if search_button:
        placeholder.text(f"'{input}'에 대한 검색 결과입니다.")


st.divider()

with st.container(border=True):
    with st.expander("단어 검색"):
        st.write("This is inside a container")
        st.write("You can put any content you like here")
    
    with st.container(border=True):
        st.write("This is inside a nested container")
        st.write("You can put any content you like here")
        st.write("Like text, images, or even interactive widgets")
        st.write("You can also nest containers inside other containers")

    st.write("This is after the nested container")
