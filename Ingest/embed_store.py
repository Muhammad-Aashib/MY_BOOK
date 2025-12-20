# ingest/embed_store.py

import os
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from Ingest.chunk_docs import chunked_docs  # <-- IMPORTANT

# Ensure API key exists
assert "GOOGLE_API_KEY" in os.environ, "GOOGLE_API_KEY not set"

# Create embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001"
)

# Create FAISS vector store
db = FAISS.from_documents(chunked_docs, embeddings)

# Save locally
db.save_local("vector_store")

print("✅ Vector store created and saved.")
