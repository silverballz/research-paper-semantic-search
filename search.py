import faiss
import numpy as np

class FAISSIndex:
    def __init__(self, embedding_dim=384):
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.paper_data = []  # Store papers for retrieval

    def add_papers(self, papers, embeddings):
        """Add papers to FAISS index."""
        self.index.add(embeddings)
        self.paper_data.extend(papers)

    def search(self, query_embedding, k=5):
        """Search for top-k closest papers in FAISS."""
        distances, indices = self.index.search(query_embedding, k)
        return [self.paper_data[i] for i in indices[0]]

# Initialize FAISS index
faiss_index = FAISSIndex()
