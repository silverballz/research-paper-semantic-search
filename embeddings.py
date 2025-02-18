from sentence_transformers import SentenceTransformer
import numpy as np

# Load a pre-trained model
model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_embeddings(texts):
    """Generate embeddings for a list of texts."""
    return np.array(model.encode(texts))

if __name__ == "__main__":
    sample_texts = ["Deep learning in medicine", "AI applications in physics"]
    print(compute_embeddings(sample_texts))
