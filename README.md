# ⚖️ LawLens-Bot — Your Legal Document AI Assistant

**LawLens-Bot** is an intelligent, LLM-powered chatbot that helps users **understand and interact with legal documents** easily. It leverages **LangChain**, **Mistral-7B**, and **RAG (Retrieval-Augmented Generation)** to deliver accurate, context-aware responses from complex legal PDFs.

---

## 🚀 Features

- 📄 Upload and parse legal documents (PDFs)
- 💬 Ask natural language questions about the content
- 🧠 Retrieval-Augmented Generation (RAG) for precise context-based answers
- 💾 Vector similarity search via FAISS
- 🧩 Maintains conversation memory across user queries
- ⚙️ Powered by LangChain & Mistral-7B via OpenRouter

---

## 🛠️ Tech Stack

| Tool/Framework     | Purpose                                |
|--------------------|----------------------------------------|
| **LangChain**      | LLM orchestration and RAG pipeline     |
| **Mistral-7B**     | Language model (served via OpenRouter) |
| **FAISS**          | Vector similarity search engine        |
| **Streamlit**      | Web UI for user interaction            |
| **PyMuPDF**        | PDF content extraction                 |
| **Python**         | Core backend logic                     |

---

## 📸 Demo Preview

> 🌐 **[Live Demo](https://lawlens.streamlit.app/)** (⚠️ May take a few seconds to load if hosted on Streamlit)
>  
> 💻 **[GitHub Repository](https://github.com/traptijindal/LawLens-Bot)**



---

## 📦 Getting Started

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/lawlens-bot.git
cd lawlens-bot
pip install -r requirements.txt
streamlit run app.py
