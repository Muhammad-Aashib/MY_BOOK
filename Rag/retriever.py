# rag/retriever.py

from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Create embeddings INSTANCE (important)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001"
)

# Load FAISS vector store
db = FAISS.load_local(
    "vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)

# Create retriever
retriever = db.as_retriever(search_kwargs={"k": 4})
