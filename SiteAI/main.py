# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scraper import scrape_website
from text_chunker import split_text
from embedder import get_embeddings
from vector_store import create_faiss_index
from qa_agent import answer_question

app = FastAPI()

# Input model for API
class QueryRequest(BaseModel):
    url: str
    question: str

@app.get("/")
def root():
    return {"message": "Welcome to SiteSence RAG API 🔍"}

@app.post("/query")
def query_site(data: QueryRequest):
    print("🚀 API called with URL:", data.url)

    # Step 1: Scrape content
    content = scrape_website(data.url)
    print(f"🔍 Scraped content (first 300 chars):\n{content[:300]}")
    if content.startswith("Error:") or len(content.strip()) < 50:
        raise HTTPException(status_code=400, detail="400: Failed to scrape website.")

    # Step 2: Chunk text
    chunks = split_text(content)
    print(f"✂️ Total chunks created: {len(chunks)}")

    # Step 3: Embed chunks
    embeddings = get_embeddings(chunks)
    print(f"📐 Embeddings shape: {embeddings.shape}")

    # Step 4: Create FAISS index
    index = create_faiss_index(embeddings)
    print("🧠 FAISS index created.")

    # Step 5: Answer user question
    print("🤖 Answering question:", data.question)
    response = answer_question(data.question, chunks, index)

    return {"answer": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
