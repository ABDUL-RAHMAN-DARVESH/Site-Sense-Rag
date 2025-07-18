
# SiteSence RAG

## 🚀 Overview  
**SiteSence RAG** is a FastAPI-based AI chatbot that allows users to input any website URL and ask questions about its content. It scrapes the webpage, chunks the text, embeds it, and answers questions using Groq’s LLaMA 3 model powered by a Retrieval-Augmented Generation (RAG) architecture.

---

## 🎯 Features  
- Scrape and process public website content  
- Chunk large content with overlap  
- Generate embeddings using Sentence Transformers (`all-MiniLM-L6-v2`)  
- Perform fast vector search with FAISS  
- Answer queries using Groq’s LLaMA 3 model  
- Built with FastAPI and LangChain

---

## 🏗️ Installation  

**Follow these steps to set up and run the project locally:**

### 1. Clone the repository  
```bash
git clone https://github.com/your-username/sitesence-rag.git
```

### 2. Navigate to the project folder  
```bash
cd sitesence-rag
```

### 3. Create a virtual environment and activate it  
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 4. Install dependencies  
```bash
pip install -r requirements.txt
```

### 5. Set up environment variables  
Create a `.env` file in the root directory and add your Groq API key:  
```env
GROQ_API_KEY=your_api_key_here
```

You can get your API key from [https://console.groq.com](https://console.groq.com)

---

## ▶️ Running the Application  

Run the FastAPI server using Uvicorn:  
```bash
uvicorn main:app --reload
```

Then open your browser and navigate to:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

This will open Swagger UI where you can test the API.

---

## 🛠 Technologies Used  
- **Python**  
- **FastAPI**  
- **BeautifulSoup**  
- **FAISS**  
- **SentenceTransformers**  
- **LangChain**  
- **Groq LLaMA 3 API**

---

## 📢 How to Use  

1. Enter a public website URL and your question via the `/query` endpoint.  
2. The backend scrapes the content and splits it into chunks.  
3. Chunks are embedded using Sentence Transformers.  
4. Relevant chunks are retrieved via FAISS.  
5. The context is passed to Groq’s LLaMA 3 model along with your question.  
6. You get a meaningful, AI-generated answer based on the website content.

---

## 🔗 Example Usage  

**POST** `/query`  
**Request:**  
```json
{
  "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
  "question": "What is artificial intelligence?"
}
```

**Response:**  
```json
{
  "answer": "Artificial intelligence is the simulation of human intelligence in machines that are programmed to think and learn."
}
```

---

## 🤝 Contributing  

Feel free to fork this project, create a feature branch, and submit a pull request.  
Your contributions are welcome and appreciated.

---

## 📜 License  

**This project is licensed under the MIT License.**

---

## 👨‍💻 Author  

**Abdul Rahman Darvesh**

---

## 📧 Contact  

For questions or feedback, feel free to reach out:  
**abdulrahmandarvesh56@gmail.com**
