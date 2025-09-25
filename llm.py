from langchain_upstage import UpstageEmbeddings
from langchain_upstage import ChatUpstage
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQA
from langchain_pinecone import PineconeVectorStore

def get_ai_message(user_message: str) -> str:
    embedding = UpstageEmbeddings(model="embedding-query")
    index_name = 'tax-markdown-index'
    # 이미 생성된 데이터베이스를 사용할 때 
    database = PineconeVectorStore.from_existing_index(index_name=index_name, embedding=embedding)

    llm = ChatUpstage(model='solar-mini')
    prompt = hub.pull("rlm/rag-prompt")
    retriever = database.as_retriever(search_kwargs={"k":4})
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt":prompt}
    )

    dictionary = ["사람을 나타내는 표현 -> 거주자"]

    prompt = ChatPromptTemplate.from_template(f"""
        사용자의 질문을 보고, 우리의 사전을 참고해서 사용자의 질문을 변경해주세요.
        만약 변경할 필요가 없다고 판단된다면, 사용자의 질문을 변경하지 않아도 됩니다.                                          
        사전: {dictionary}
        
        질문: {{question}}                      
    """)

    dictionary_chain = prompt | llm | StrOutputParser()

    tax_chain = {"query": dictionary_chain} | qa_chain
    ai_message =  tax_chain.invoke({"question": user_message})
    return ai_message['result']
