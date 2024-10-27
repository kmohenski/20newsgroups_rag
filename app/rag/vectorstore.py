import os

from sklearn.datasets import fetch_20newsgroups
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document
from langchain_chroma import Chroma

class VectorstoreHandler():
    def __init__(self, persist_directory="chroma_db"):
        embedding_function = OpenAIEmbeddings()
        
        if os.path.exists(persist_directory) and os.listdir(persist_directory):
            self.vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embedding_function)
        else:
            newsgroups_data = fetch_20newsgroups(
                subset = 'train',
                categories = [
                    'sci.electronics',
                    'sci.crypt',
                    'sci.med',
                    'sci.space',
                    'comp.graphics',
                    'comp.windows.x',
                    'comp.sys.ibm.pc.hardware',
                    'comp.sys.mac.hardware',
                    'comp.os.ms-windows.misc',
                ]
            )
            documents = [Document(page_content=text) for text in newsgroups_data["data"]]
            
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=258)

            splits = text_splitter.split_documents(documents)
            
            self.vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embedding_function)
            batch_size = 5000
            for i in range(0, len(splits), batch_size):
                self.vectorstore.add_documents(splits[i:i + batch_size])