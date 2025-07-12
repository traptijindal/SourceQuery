import streamlit as st
import requests
from utils import extract_text_from_pdf, extract_text_from_txt
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    st.error("API key not found. Please check your .env file.")

st.set_page_config(page_title="Legal Document Chatbot", layout="centered")
st.title("🧾 LawLens")


uploaded_file = st.file_uploader("Upload a legal document (PDF or TXT)", type=["pdf", "txt"])
document_text = ""

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        document_text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type == "text/plain":
        document_text = extract_text_from_txt(uploaded_file)

    if document_text:
        st.success("Document successfully extracted.")
        with st.expander("📄 View Extracted Document Text"):
            st.write(document_text[:3000] + ("..." if len(document_text) > 3000 else ""))


question = st.text_input("Ask a question related to the document:")


def ask_openrouter(document: str, query: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",  
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a legal expert chatbot. Answer only from the provided document."},
            {"role": "user", "content": f"Document: {document}\n\nQuestion: {query}"}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.text}"


if question and document_text:
    with st.spinner("Thinking..."):
        answer = ask_openrouter(document_text, question)
        st.markdown("**📌 Answer:**")
        st.write(answer)
