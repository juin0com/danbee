import streamlit as st

# 테스트용 단어 목록 생성
import random
import string

def generate_random_words(num_words):
    words = []
    themes = ['자연', '기술', '예술', '과학', '문학']
    for _ in range(num_words):
        word = ''.join(random.choices(string.ascii_lowercase, k=5))
        importance = random.randint(1, 10)
        theme = random.choice(themes)
        words.append({'word': word, 'importance': importance, 'theme': theme})
    return words

word_list = generate_random_words(50)

st.title("추천단어")

# 카테고리 선택 (radio)
selected_theme = st.radio(
    "카테고리를 선택하세요",
    options=['전체', '자연', '기술', '예술', '과학', '문학', '경제', '스포츠', '역사'] , 
    label_visibility="hidden",
    horizontal=True,
)

# 중요도 선택 (slider)
importance_level = st.slider("중요도를 선택하세요 (1: 기초 ~ 10: 고급)", 1, 10, 5)

# 선택한 카테고리와 중요도로 단어 필터링
filtered_words = [word for word in word_list 
                 if word['importance'] == importance_level 
                 and (selected_theme == '전체' or word['theme'] == selected_theme)]

# 단어 목록 표시
with st.container():
    if filtered_words:
        for word in filtered_words:
            if st.button(f"{word['word']} ({word['theme']})"):
                st.session_state['search_word'] = word['word']
                st.experimental_set_query_params()
                st.experimental_rerun()
    else:
        st.write("선택한 조건의 단어가 없습니다.")

# 검색 페이지로 연결
if 'search_word' in st.session_state:
    import webbrowser
    search_url = f"/views/search_word.py?query={st.session_state['search_word']}"
    webbrowser.open(search_url)