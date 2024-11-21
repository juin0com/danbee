import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_plotly_events import plotly_events

st.title("학습통계")

# 임시 데이터 생성
data = {
    'date': pd.date_range(start='2023-10-01', periods=7, freq='D'),
    'words_learned': [20, 15, 30, 25, 10, 5, 18]
}
df = pd.DataFrame(data)

# Plotly 바 차트 생성
fig = px.bar(df, x='date', y='words_learned', hover_data=['date', 'words_learned'])

# 차트 표시 및 클릭 이벤트 처리
selected_points = plotly_events(fig, click_event=True)

if selected_points:
    selected_date = selected_points[0]['x']
    st.write(f"{selected_date}의 학습 내역으로 이동합니다.")
    # 여기에 view/history_word.py로의 페이지 전환 로직 추가