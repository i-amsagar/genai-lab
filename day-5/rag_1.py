from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

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
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=""
)

# print(docs[45])
print("DOCS", len(docs))
print("SPLIT", len(split_docs))