import streamlit as st
from supabase import create_client, Client

# Supabase 클라이언트 초기화
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

# 카테고리 목록 가져오기
response = supabase.table('word_list').select('category').execute()
categories = list(set([item['category'] for item in response.data if item['category']]))
categories.insert(0, '전체')  # '전체' 옵션 추가

st.markdown("""
<style>
    .st-emotion-cache-1igbibe {
       /* background-color: #FAB12F;*/
    }
</style>
""", unsafe_allow_html=True)

st.subheader("🔎 검색조건을 입력하세요")
with st.container(border=True):
    # 사용자 입력 받기
    selected_category = st.radio(
        "카테고리를 선택하세요",
        options=categories,
        label_visibility="hidden",
        horizontal=True,
    )

    # 중요도 선택 (slider)
    importance_level = st.slider("중요도를 선택하세요 (1: 기초 ~ 10: 고급)", 1, 10, 1)

# 단어 필터링
query = supabase.table('word_list').select('lemma', 'category').eq('rank', importance_level)
if selected_category != '전체':
    query = query.eq('category', selected_category)
query = query.limit(20)  # 단어를 20개로 제한
result = query.execute()  # execute() 메서드를 호출하여 쿼리 실행

st.divider()
# 단어 목록 표시
st.subheader("👍추천 단어")
with st.container():
    if result:
        max_cols = 5  # 한 행에 표시할 최대 버튼 수
        words = result.data
        rows = [words[i:i+max_cols] for i in range(0, len(words), max_cols)]
        for row in rows:
            cols = st.columns(len(row))
            for col, word in zip(cols, row):
                category = f" ({word['category']})" if word['category'] else ""
                with col:
                    if st.button(f"{word['lemma']}{category}"):
                        st.session_state['search_word'] = word['lemma']
                        st.switch_page("views/search_word.py")
    else:
        st.write("선택한 조건의 단어가 없습니다")

# 검색 페이지로 연결
# if 'search_word' in st.session_state:
#     import webbrowser
#     search_url = f"/views/search_word.py?query={st.session_state['search_word']}"
#     webbrowser.open(search_url)