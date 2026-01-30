# import requests
# import os

# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# def ask_openrouter(context_chunks, question):
#     context = "\n\n".join(context_chunks)

#     payload = {
#         "model": "mistralai/mistral-7b-instruct-v0.2",
#         "messages": [
#             {
#                 "role": "system",
#                 "content": (
#                     "Answer ONLY using the provided context. "
#                     "If the answer is not present, say "
#                     "'Information not found in the provided sources.'"
#                 )
#             },
#             {
#                 "role": "user",
#                 "content": f"Context:\n{context}\n\nQuestion:\n{question}"
#             }
#         ]
#     }

#     response = requests.post(
#         "https://openrouter.ai/api/v1/chat/completions",
#         headers={
#             "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#             "Content-Type": "application/json"
#         },
#         json=payload
#     )

#     return response.json()["choices"][0]["message"]["content"]
import requests
import os
from dotenv import load_dotenv


load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def ask_openrouter(context_chunks, question):
    if not OPENROUTER_API_KEY:
        return "Error: OPENROUTER_API_KEY not found."

    context = "\n\n".join(context_chunks)

    payload = {
        "model": "meta-llama/llama-3.1-8b-instruct",
        "messages": [
            {
                "role": "system",
                "content": (
                    "Answer ONLY using the provided context. "
                    "If the answer is not present, say: "
                    "'Information not found in the provided sources.'"
                )
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{question}"
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8501",
        "X-Title": "LawLens v2"
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload
    )

    try:
        data = response.json()
    except Exception:
        return "Error: Invalid response from LLM API."

    if "choices" not in data:
        return f"LLM Error: {data}"

    return data["choices"][0]["message"]["content"]
