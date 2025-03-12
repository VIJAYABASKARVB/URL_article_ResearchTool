import os
import pickle
import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


GROQ_API_KEY="your_key"

# Streamlit UI setup
st.title("News Research Tool")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i + 1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store_HF.pkl"

main_placeholder = st.empty()


llm = ChatGroq(
    api_key=GROQ_API_KEY,  
    model="qwen-2.5-32b",
    temperature=0.8
)


if process_url_clicked:
    # Ensure at least one URL is provided
    if not any(urls):
        st.warning("Please provide at least one URL.")
    else:
        # Load data from URLs
        loader = UnstructuredURLLoader(urls=urls)
        data = loader.load()
        main_placeholder.text("Loaded data from URLs.")

        # Split data into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", "\n", ".", ","],
            chunk_size=1000
        )
        main_placeholder.text("Splitting text into chunks...")
        docs = text_splitter.split_documents(data)

        # Create embeddings
        main_placeholder.text("Generating embeddings...")
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectorstore_HF = FAISS.from_documents(docs, embeddings)

        # Save FAISS index to a pickle file
        with open(file_path, "wb") as f:
            pickle.dump(vectorstore_HF, f)


query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists(file_path):
        with open(file_path,"rb") as f:
            vectorstore = pickle.load(f)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm,retriever= vectorstore.as_retriever())
            result = chain({"question":query},return_only_outputs=True)

            st.header("Answer")
            st.write(result["answer"])

            # Display sources, if available
            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                sources_list = sources.split("\n") 
                for source in sources_list:
                    st.write(source)