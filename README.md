# 🔎 SourceQuery — Multi-Source Content Retrieval System

**SourceQuery** is a source-grounded, LLM-powered system that enables users to query information across **PDFs and live websites** using semantic search and controlled web crawling.  
It retrieves relevant context from multiple sources and generates **hallucination-safe answers strictly grounded in retrieved content**.

This project evolved from a single-document chatbot into a **general-purpose content retrieval and question-answering system**.

---

## 🚀 Key Features

- 📄 **PDF ingestion** (upload and query documents)
- 🌐 **Website & blog ingestion** with controlled crawling
- 🔗 **Internal link traversal** (same-domain, depth-limited)
- 🧠 **Semantic search** using FAISS embeddings
- ✂️ **Sentence-aware chunking** for improved retrieval accuracy
- 🛡️ **Hallucination control** (answers generated only from retrieved context)
- ❌ Graceful refusal when information is not present in sources
- 🔍 **Debug view** to inspect top-k retrieved chunks
- ⚙️ Modular architecture (ingestion → chunking → retrieval → generation)

---

## 🧠 How It Works

PDF / Website URL
↓
Text Extraction & Cleaning
↓
Sentence-Aware Chunking
↓
Embeddings (SentenceTransformers)
↓
FAISS Vector Index
↓
Top-K Relevant Chunks
↓
LLM (via OpenRouter)
↓
Source-Grounded Answer


---

## 🛠️ Tech Stack

| Tool / Framework | Purpose |
|------------------|--------|
| Python | Core backend logic |
| Streamlit | Web UI |
| SentenceTransformers | Text embeddings |
| FAISS | Vector similarity search |
| BeautifulSoup | Website content extraction |
| Requests | HTTP crawling with User-Agent |
| OpenRouter | LLM access (LLaMA / GPT models) |
| dotenv | Environment variable management |

---

## 🌐 Supported Data Sources

- ✅ PDF documents  
- ✅ Plain text files  
- ✅ Public websites (Wikipedia, blogs, documentation sites)

---

## 🛡️ Hallucination-Safe Design

SourceQuery is designed to **avoid hallucinations by default**:

- The LLM receives **only retrieved context**
- If the answer is not present in the retrieved chunks, the system responds:  
  **“Information not found in the provided sources.”**
- Retrieval accuracy is verified by inspecting FAISS top-k results

---



