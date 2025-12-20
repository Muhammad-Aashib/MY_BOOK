# rag/qa.py

import os
import google.generativeai as genai
from Rag.prompt import SYSTEM_PROMPT

# Configure Gemini
assert "GOOGLE_API_KEY" in os.environ, "GOOGLE_API_KEY not set"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-pro")


def format_context(docs):
    """
    Formats retrieved docs with metadata for citations
    """
    formatted = []

    for i, doc in enumerate(docs, 1):
        chapter = doc.metadata.get("chapter", "Unknown Chapter")
        section = doc.metadata.get("section", "Unknown Section")
        source = doc.metadata.get("source", "Unknown Source")

        formatted.append(
            f"[{i}] Chapter: {chapter}\n"
            f"Section: {section}\n"
            f"Source: {source}\n"
            f"Content:\n{doc.page_content}\n"
        )

    return "\n---\n".join(formatted)


def ask_gemini(docs, question, level="student"):
    context = format_context(docs)

    prompt = f"""
{SYSTEM_PROMPT}

User expertise level: {level}

Rules:
- Answer ONLY from the provided context
- If the answer is not present, say "This is not covered in the book"
- Cite chapter and section explicitly
- Do not hallucinate or infer beyond the text

Context:
{context}

Question:
{question}

Answer (with citations):
"""

    response = model.generate_content(prompt)
    return response.text
