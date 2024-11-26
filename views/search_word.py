import streamlit as st
import  openai
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_tools_agent, load_tools
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain.agents import AgentExecutor, create_openai_tools_agent, load_tools

openai.api_key = st.secrets["OPENAI_API_KEY"]

# Session state initialization
if 'search_result' not in st.session_state:
    st.session_state['search_result'] = ""

st.subheader("🤖단어 검색")

# CSS를 페이지 상단에 추가
st.markdown("""
<style>
div[data-testid="stHorizontalBlock"] {
    align-items: center;
}
</style>
""", unsafe_allow_html=True)

@st.fragment
def search_word():
    with st.container(border=True):
        with st.form(key="search_form"):
            col1, col2, col3 = st.columns(3)
            with col1:
                input_word = st.text_input("단어를 입력하세요.", value="", label_visibility="collapsed")
            with col2:
                search_button = st.form_submit_button(label="검색")
            with col3:
                options = ["의미", "예시", "발음"]
                selected_options = st.pills("", options, key="pills", selection_mode="multi", default=options)  

    if search_button and input_word:
        if not selected_options:
            st.warning("하나 이상의 검색 옵션을 선택해주세요.")
        else:
            with st.spinner("검색 중입니다..."):
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
                # save search result to session state
                st.session_state['search_result'] = response.choices[0].message.content
                if st.session_state['search_result']:
                    st.write(st.session_state['search_result'])    

search_word()



# agent making
def create_agent_chain(history):
    chat = ChatOpenAI(
        # st.secrets() 함수 호출 방식이 잘못됨
        model=st.secrets["OPENAI_API_MODEL"],
        temperature=st.secrets["OPENAI_API_TEMPERATURE"],
    )
    
    # Duolingo, Memrise는 기본 제공 도구가 아님
    #tools = load_tools(["wikipedia","ddg-search"])
    tools = load_tools(["wikipedia","ddg-search"])
    
    prompt = hub.pull("hwchase17/openai-tools-agent")
    memory = ConversationBufferMemory(
        chat_memory=history, 
        memory_key="chat_history", # chat_key -> chat_history
        return_messages=True
    )
    
    agent = create_openai_tools_agent(chat, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, memory=memory)

@st.fragment
def chatbot():
    with st.container(border=True):
        st.subheader("🎈단비노트 챗봇서비스🎈")

        history = StreamlitChatMessageHistory()
        prompt = st.chat_input("추가질문 할 내용을 입력하세요.")

        if prompt:
            with st.chat_message("user"):
                history.add_user_message(prompt)
                st.markdown(prompt)
        
            with st.chat_message("assistant"):
                callback = StreamlitCallbackHandler(st.container())
                agent_chain = create_agent_chain(history)
                response = agent_chain.invoke(
                    {"input": prompt},
                    callbacks=[callback]  # {"callback": [callback]} -> callbacks=[callback]
                )
                st.markdown(response["output"])

chatbot()
