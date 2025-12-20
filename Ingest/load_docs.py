# ingest/load_docs.py
from langchain_community.document_loaders import TextLoader


loader = TextLoader(
    path="data/docs",
    glob="**/*.md"
)

docs = loader.load()
print(f"Loaded {len(docs)} markdown files")
