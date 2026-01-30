import streamlit as st


from loaders.pdf_loader import extract_text_from_pdf
from loaders.text_loader import extract_text_from_txt
from loaders.web_loader import crawl_website
from processing.chunker import chunk_text
from processing.vector_store import build_faiss_index, retrieve_chunks
from llm.openrouter_client import ask_openrouter



st.set_page_config(page_title="SourceQuery", layout="centered")
st.title("SourceQuery - Multi-Source Content Retrieval System")

# -------- Input Selection --------
source_type = st.radio(
    "Choose data source:",
    ["PDF / TXT", "Website URL"]
)

documents = []

if source_type == "PDF / TXT":
    uploaded_file = st.file_uploader("Upload document", type=["pdf", "txt"])

    if uploaded_file:
        if uploaded_file.type == "application/pdf":
            text = extract_text_from_pdf(uploaded_file)
        else:
            text = extract_text_from_txt(uploaded_file)

        documents.append({
            "source": uploaded_file.name,
            "content": text
        })

else:
    website_url = st.text_input("Enter website or blog URL")

    if website_url:
        with st.spinner("Crawling website..."):
            documents = crawl_website(website_url)

# -------- Build Knowledge Base --------
if documents:
    all_chunks = []

    for doc in documents:
        chunks = chunk_text(doc["content"])
        all_chunks.extend(chunks)

    index, stored_chunks = build_faiss_index(all_chunks)
    st.success("Knowledge base created successfully.")

# -------- Question Answering --------
question = st.text_input("Ask a question:")

if question and documents:
    with st.spinner("Thinking..."):
        relevant_chunks = retrieve_chunks(question, index, stored_chunks)
        answer = ask_openrouter(relevant_chunks, question)

    st.markdown("### 📌 Answer")
    st.write(answer)
