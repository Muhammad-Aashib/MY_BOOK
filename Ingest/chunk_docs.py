## ingest/chunk_docs.py

from langchain_text_splitters import MarkdownHeaderTextSplitter
from Ingest.load_docs import docs

headers_to_split_on = [
    ("#", "chapter"),
    ("##", "section"),
]

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on,
    strip_headers=False,
)

chunked_docs = []

for doc in docs:
    splits = splitter.split_text(doc.page_content)

    for chunk in splits:
        # Preserve source filename
        chunk.metadata["source"] = doc.metadata.get("source", "unknown")
        chunked_docs.append(chunk)

print(f"✅ Created {len(chunked_docs)} chunks")

