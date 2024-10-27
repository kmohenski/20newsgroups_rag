from rag.retriever import RetrieverHandler
from config import BaseConfig

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


config = BaseConfig()
OPENAI_API_KEY = config.OPENAI_API_KEY

class RAG():
    def __init__(self):
        llm = ChatOpenAI(model="gpt-4o-mini")
        self.retriever_handler = RetrieverHandler()
        prompt = PromptTemplate.from_template("""
            You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
            Question: {question} 
            Context: {context} 
            Answer: """
        )
        
        self.chain = (
            {"context": self.retriever_handler.retriever | self.format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
    
    def format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    def invoke(self, query: str) -> dict[str, str]:
        return {"answer": self.chain.invoke(query), "retrieved_docs": self.retriever_handler.retriever.invoke(query)}