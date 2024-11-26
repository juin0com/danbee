import whisper
import tempfile
import os
import streamlit as st

def transcribe_audio(audio_file):
    model = whisper.load_model("base")
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(audio_file.name)[1]) as tmp_file:
        tmp_file.write(audio_file.getvalue())
        tmp_file_path = tmp_file.name

    print(f"Temporary file path: {tmp_file_path}")  # 디버깅용

    try:
        result = model.transcribe(tmp_file_path)
        return result["text"]
    finally:
        os.unlink(tmp_file_path)

st.title("음성 인식 앱")

uploaded_file = st.file_uploader("오디오 파일을 업로드하세요", type=["wav", "mp3", "m4a"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")
    
    if st.button("음성 인식 시작"):
        with st.spinner("음성을 인식하는 중..."):
            text = transcribe_audio(uploaded_file)
        st.write(text)