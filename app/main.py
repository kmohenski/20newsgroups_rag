from rag.generator import RAG

import streamlit as st


rag = RAG()

# # Streamlit UI
st.title("Retrieval-Augmented Generation using LangChain")

st.write("A RAG model using using the 20 Newsgroups science and computer messages.")
st.write("Questions you could ask:")
st.write("\"How could I become an astronaut?\"")
st.write("\"What is the bmp format?\"")
st.write("\"What are the risks of smoking?\"")
st.write("\"Is Mac better then Windows?\"")

input_text = st.text_input("Ask a question")

if st.button("Answer question"):
    if input_text:
        # Display the result
        out = rag.invoke(input_text)
        st.write("Answer:")
        st.write(out["answer"])
        st.write("Retrieved messages:")
        st.write(out["retrieved_docs"])
    else:
        st.write("Please enter a question.")