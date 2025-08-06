import os
from dotenv import load_dotenv
from embedder import model  # using same embedding model
from vector_store import search_index
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableMap, RunnablePassthrough

# Load environment variables
load_dotenv()

def answer_question(user_question, chunks, index):
    # Embed the question
    question_embedding = model.encode([user_question])[0]

    # Find top matches from index
    matched_indexes = search_index(index, question_embedding)
    matched_texts = [chunks[i] for i in matched_indexes]

    # Combine matched chunks
    context = "\n\n".join(matched_texts)

    # Prompt setup
    prompt = ChatPromptTemplate.from_template(
        "You are a helpful website assistant. Use this content to answer:\n\n{context}\n\nQuestion: {question}"
    )

    # Load Groq LLM with the API key from the .env file
    groq_llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),  # Get the API key from environment
        model="llama3-8b-8192"
    )

    # Build pipeline
    chain = RunnableMap({
        "context": lambda x: x["context"],
        "question": lambda x: x["question"]
    }) | prompt | groq_llm

    # Run the chain
    result = chain.invoke({"context": context, "question": user_question})
    return result.content
