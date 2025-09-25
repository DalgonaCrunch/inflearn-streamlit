import streamlit as st

from dotenv import load_dotenv
from llm import get_ai_message

# 환경변수 불러옴
load_dotenv()

st.set_page_config(page_title="소득세 챗봇", page_icon="🤖")

st.title("🤖 소득세 챗봇")
st.caption("소득세에 관련된 모든것을 답해드립니다!")

st.write("소득세 관련 질문이 있으시면 물어보세요!")
st.write("예시 질문:")
st.write("- 소득세 신고 방법이 궁금해요.")
st.write("- 근로소득과 사업소득의 차이점은 무엇인가요?")
st.write("- 소득세 공제 항목에는 어떤 것들이 있나요?")
st.write("- 소득세 신고 기한은 언제인가요?")
st.write("- 소득세 신고 시 필요한 서류는 무엇인가요?")
st.write("- 소득세 신고 후 환급 절차는 어떻게 되나요?")
st.write("- 소득세 신고 시 환급금은 언제 받을 수 있나요?")
st.write("- 소득세 신고 시 세액공제와 세액감면의 차이점은 무엇인가요?")

if 'message_list' not in st.session_state:
    st.session_state.message_list = [] 

# 세션에 쌓인 메시지 출력
for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"]) # st.markdown(message["content"])

if user_question := st.chat_input(placeholder="소득세에 대해 궁금한 점이 있나요? 질문을 입력해주세요!"):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})
    
    with st.spinner("답변을 생성하는 중입니다..."):
        ai_message = get_ai_message(user_question)

        with st.chat_message("ai"):
            st.write(ai_message) #st.markdown(ai_message)
            st.session_state.message_list.append({"role": "ai", "content": ai_message})

        
    # st.chat_message("user").markdown(user_question)

    # with st.chat_message("assistant"):
    #     st.markdown("답변을 준비 중입니다...")

    #     # 여기에 실제 답변 생성 로직을 추가하세요.
    #     # 예: response = generate_response(user_question)
    #     response = "죄송합니다, 현재 답변 생성 기능이 구현되지 않았습니다."

    #     st.markdown(response)
        
        
# st.write("소득세 관련 질문이 있으시면 물어보세요!")
# st.write("예시 질문:")
# st.write("- 소득세 신고 방법이 궁금해요.")
# st.write("- 근로소득과 사업소득의 차이점은 무엇인가요?")
# st.write("- 소득세 공제 항목에는 어떤 것들이 있나요?")
# st.write("- 소득세 신고 기한은 언제인가요?")
# st.write("- 소득세 신고 시 필요한 서류는 무엇인가요?")
# st.write("- 소득세 신고 시 주의할 점이 있나요?")
# st.write("- 소득세 신고 후 환급 절차는 어떻게 되나요?")
# st.write("- 소득세 신고 시 환급금은 언제 받을 수 있나요?")
# st.write("- 소득세 신고 시 세액공제와 세액감면의 차이점은 무엇인가요?")