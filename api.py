from fastapi import FastAPI
import asyncio
import numpy as np
from fetch_papers import fetch_papers
from embeddings import compute_embeddings
from search import faiss_index

app = FastAPI()

@app.get("/search")
async def search(query: str):
    """Semantic search for research papers."""
    papers = await fetch_papers(query)  # Get papers from API
    abstracts = [p["abstract"] for p in papers if p["abstract"]]
    embeddings = compute_embeddings(abstracts)  # Convert to vectors

    # Store papers in FAISS
    faiss_index.add_papers(papers, embeddings)

    # Query FAISS
    query_embedding = compute_embeddings([query])
    results = faiss_index.search(query_embedding)

    return {"results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
