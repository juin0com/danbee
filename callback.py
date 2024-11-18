import os
import streamlit as st
from supabase import create_client

# Supabase 설정
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
supabase = create_client(supabase_url, supabase_key)

def handle_auth_callback():
    # URL 파라미터에서 코드 추출
    params = st.experimental_get_query_params()
    
    if 'code' in params:
        try:
            # GitHub 인증 코드로 세션 생성
            auth_response = supabase.auth.exchange_code_for_session(params['code'][0])
            # 세션에 사용자 정보 저장
            st.session_state['user'] = auth_response.user
            st.session_state['access_token'] = auth_response.session.access_token
            # 메인 페이지로 리다이렉션
            st.switch_page("main.py")
        except Exception as e:
            st.error(f"인증 오류: {str(e)}")

handle_auth_callback()

