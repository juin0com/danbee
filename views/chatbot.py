import streamlit as st
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_tools_agent, load_tools
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_openai import ChatOpenAI
from collections.abc import MutableSet


def create_agent_chain(history):
    chat = ChatOpenAI(
        model=st.secrets("OPENAI_API_MODEL"),
        temperature=st.secrets("OPENAI_API_TEMPERATURE"),
    )
    tools = load_tools(["Duolingo", "wikipedia","Memrise"])
    prompt = hub.pull("hwchase17/openai-tools-agent")
    memory = ConversationBufferMemory(
        chat_memory=history, memory_key="chat_key", return_messages=True
    )
    
    agent = create_openai_tools_agent(chat, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, memory=memory)

st.title("🎈단비노트 챗봇서비스🎈")

history = StreamlitChatMessageHistory()
prompt = st.chat_input("검색할 단어를 입력하세요.")

if prompt:
    with st.chat_message("user"):
        history.add_user_message(prompt)
        st.markdown(prompt)

    with st.chat_message("assistant"):
        callback = StreamlitCallbackHandler(st.container())
        agent_chain = create_agent_chain(history)
        response = agent_chain.invoke(
            {"input": prompt},
            {"callback": [callback]},
        )
        st.markdown(response["output"])