import streamlit as st
from openai import OpenAI

# OpenAI 클라이언트 초기화
client = OpenAI(api_key = st.secrets["OPENAI_API_KEY"])

kwargs = {
    "prompt": "멋진 강아지 사진 만들어줘"
}

# 이미지 생성
im = client.images.generate(**kwargs)
print(im)
img_url = im.data[0].url

# Streamlit을 사용하여 이미지 표시
st.image(img_url, caption="Generated Image")