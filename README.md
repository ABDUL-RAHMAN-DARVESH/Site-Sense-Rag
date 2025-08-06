# Site Sense RAG

A Retrieval-Augmented Generation (RAG) system for website content analysis and question answering.

## Features

- Web scraping and content extraction
- Text chunking and embedding generation
- Vector storage with FAISS
- Question-answering with Groq LLM
- FastAPI backend

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Site-Sense-Rag
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp SiteAI/.env.example SiteAI/.env
```
Edit `.env` and add your Groq API key.

4. Run the application:
```bash
cd SiteAI
python main.py
```

## Project Structure

- `scraper.py` - Web scraping functionality
- `text_chunker.py` - Text processing and chunking
- `embedder.py` - Text embedding generation
- `vector_store.py` - Vector database operations
- `qa_agent.py` - Question-answering logic
- `main.py` - Main application entry point

## Requirements

- Python 3.8+
- Groq API key

## License

MIT License