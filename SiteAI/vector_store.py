import faiss
import numpy as np

# Create FAISS index and add embeddings
def create_faiss_index(embeddings):
    dim = embeddings.shape[1]  # length of each embedding
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index

# Search for top k similar chunks
def search_index(index, query_embedding, k=3):
    D, I = index.search(np.array([query_embedding]), k)
    return I[0]  # return list of matched indexes
