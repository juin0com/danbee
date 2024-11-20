import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.markdown(
    """
    <style>
    .stContainer {
        margin-top: 0rem;
        margin-bottom: 0rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container(border=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        input_word = st.text_input("단어를 입력하세요.", value="", label_visibility="collapsed")
    with col2:
        search_button = st.button("검색")
    with col3:
        options = ["의미", "예시", "발음"]
        selected_options = st.pills("", options, key="pills", selection_mode="multi")
    
    if search_button and input_word:
        if not selected_options:
            st.warning("하나 이상의 검색 옵션을 선택해주세요.")
        else:
            # 선택된 옵션에 따라 질문 생성
            questions = []
            if "의미" in selected_options:
                questions.append(f"{input_word}의 의미와 설명을 알려주세요.")
            if "예시" in selected_options:
                questions.append(f"{input_word}를 사용한 예문을 3개 알려주세요.")
            if "발음" in selected_options:
                questions.append(f"{input_word}의 발음 방법과 음성기호를 알려주세요.")
            
            combined_question = "\n".join(questions)
            
            # OpenAI API 호출
            response = openai.chat.completions.create(
                model=st.secrets["OPENAI_API_MODEL"],
                temperature=st.secrets["OPENAI_API_TEMPERATURE"],
                messages=[
                    {"role": "system", "content": "You are a teacher who helps you learn English words well"},
                    {"role": "user", "content": combined_question}
                ]
            )
            
            # 응답 표시
            with st.container():
                st.write(response.choices[0].message.content)     

with st.container(border=True):
    with st.expander("AI 와 대화하기", expanded=True):
        st.write("AI와 대화를 통해 단어에 대한 이해도를 높이세요")
    
    st.write("This is ganerated by " + st.secrets["OPENAI_API_MODEL"])
