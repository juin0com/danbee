import streamlit as st

#from forms.contact import contact_form

st.subheader("👍단비노트에 대해서")

# @st.dialog("단비노트 슬로건")
# def show_contact_form():
#     contact_form()

# if st.button("문의하기"):
#     show_contact_form()

st.write("GPT가 아래와 같은 문장을 추천해주었습니다.")

with st.container():
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- <span style='color:red'>단</span>어를 학습하는 <span style='color:red'>비</span>법노트", unsafe_allow_html=True)
        st.write("- 머리속 사막에 단비를 뿌려주는 노트")
        st.write("- 메마른 기억에 내리는 지식의 단비")
        st.write("- 단비노트를 통해 일상을 기록하고, 공유해보세요.")
    with col2:
        st.image("./assets/logo_about.jpg", use_container_width=True)

st.write("")
st.write("단비노트는 당신의 일상을 기록하고, 공유할 수 있는 서비스입니다.")
st.markdown("**올인원 Pass! 인공지능 프로젝트 마스터** 과정의 네모난상상 팀의 프로젝트입니다.")
st.write("아직은 부족한게 많지만 더 나은 서비스를 위해 응원부탁드립니다.")
