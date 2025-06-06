from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

from langchain_qdrant import QdrantVectorStore
import openai

load_dotenv()

# Get API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

pdf_path = Path(__file__).parent / "nodejs.pdf"

# PyPDFLoader

loader = PyPDFLoader(file_path=pdf_path)
# list of document and create pages into page 1,2 and on
# chunking
docs = loader.load()

# Text splitters
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, # 1000 chracter create chunk size
    chunk_overlap=200, # chunk with overlap each other so get back data with 200 character
)
split_docs = text_splitter.split_documents(documents=docs)

# Embedding - create function for use Embeder
embedder = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=openai_api_key
)

# Create qdrant vector store

# Step 1: Inject store in collection new
# vectoe_store = QdrantVectorStore.from_documents(
#     documents=[],
#     url="http://localhost:6333",
#     collection_name="learning_langchain",
#     embedding=embedder
# )

# vectoe_store.add_documents(documents=split_docs)
# print("Injection Done")

# Step 2: Retriver store
# If collection already exists and populated
retriever = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_langchain",
    embedding=embedder
)

def ask_question(question: str) -> str:
    # Retrieve similar chunks
    relevant_chunks = retriever.similarity_search(query=question)
    context = "\n\n".join([doc.page_content for doc in relevant_chunks])

    SYSTEM_PROMPT = f"""
    You are a helpful assistant. Use the following context to answer the user's question.
    Context:
    {context}
    """

    # Format system prompt
    system_prompt = SYSTEM_PROMPT.format(context=context)

    # Chat messages for GPT-4o
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]

    # Call OpenAI chat completion
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.2
    )

    return response.choices[0].message.content

# print(docs[45])
print("DOCS", len(docs))
print("SPLIT", len(split_docs))

while True:
    user_question = input("\nAsk a question about the PDF (or type 'exit' to quit): ")
    if user_question.lower() == "exit":
        break

    try:
        answer = ask_question(user_question)
        print("\nAnswer:\n", answer)
    except Exception as e:
        print(f"An error occurred: {e}")
