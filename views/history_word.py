import streamlit as st
import random
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.markdown(
    """
    <style>
        .st-emotion-cache-1igbibe  {
           /* background-color: #FFD09B;*/  
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("이전학습단어")

# 기간 선택
period = st.selectbox("기간 선택", ["오늘", "지난주", "지난월"])

# 기간에 따른 단어 목록 불러오기 (예시 데이터 사용)
def get_words_by_period(period):
    # 실제로는 데이터베이스나 파일에서 이전 학습 단어를 불러와야 합니다.
    words_dict = {
        "오늘": ["apple", "banana", "cherry", "date", "fig"],
        "지난주": ["grape", "honeysuckle", "kiwi", "lemon", "mango"],
        "지난월": ["nectarine", "orange", "papaya", "quince", "raspberry"]
    }
    return words_dict.get(period, [])

# 복습할 단어 목록 생성
words = get_words_by_period(period)
review_words = random.sample(words, len(words))

# 워드클라우드 생성
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(review_words))

# 워드클라우드 표시
fig, ax = plt.subplots(figsize=(15, 7.5))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

# 단어 클릭 시 검색 페이지로 이동
st.write("단어를 클릭하면 검색 페이지로 이동합니다:")

for word in review_words:
    # search_url = f"/?query={word}"
    # aTag = f"<a href='{search_url}' target='_self'>{word}</a> "
    # st.markdown(f"- {aTag}", unsafe_allow_html=True)
    if st.button(f"{word}"):
        st.session_state['search_word'] = word
        st.switch_page("views/search_word.py")