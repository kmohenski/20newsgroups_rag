from rag.vectorstore import VectorstoreHandler

class RetrieverHandler():
    def __init__(self):
        vectorstore_handler = VectorstoreHandler()
        self.retriever = vectorstore_handler.vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})