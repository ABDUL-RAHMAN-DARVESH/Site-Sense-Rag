from sentence_transformers import SentenceTransformer

# Load the embedding model once
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def get_embeddings(text_chunks):
    embeddings = model.encode(text_chunks)
    return embeddings
