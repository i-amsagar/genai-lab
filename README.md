# 🧠 Gen AI Project

## 🔧 First-Time Project Setup

### 1. Create a virtual environment

```cmd
python -m venv venv
```

### 2. Activate the virtual environment

#### On Windows:

```cmd
.\venv\Scripts\Activate
```

### 3. Install `tiktoken`

```cmd
pip install tiktoken
```

### 4. Save dependencies to `requirements.txt`

```cmd
pip freeze > requirements.txt
```

### 5. Run a Python file

```cmd
python ./file_name.py
```

### 6. Deactivate the virtual environment

To exit the virtual environment when you're done:

```bash
deactivate
```

## 📁 Project Structure

```
├── .env                   # Store your OpenAI API key
└── requirements.txt       # Python dependencies
```

## 🧩 Tokenization

- **File:** `tokenization.py`
- **Library:** `tiktoken`

## 📌 Embedding

- **File:** `embedding.py`
- **Libraries:** `openai`, `python-dotenv`

### Install:

```bash
pip install openai python-dotenv
```

### Update `requirements.txt`:

```bash
pip freeze > requirements.txt
```

### Create a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

## 🧪 Prompt Engineering

# 📅 Day 2: Mastering Prompting Techniques

### Install Google Generative AI SDK:

```bash
pip install google-genai
```

Explore different prompting techniques:

- ✅ Zero-shot Prompting → `chat_gemini.py`
- ✅ Few-shot Prompting → `chat_2.py`
- ✅ Chain-of-Thought Prompting → `chat_3.py`
- ✅ OpenAI Chat Example → `chat_1.py`

# 📅 Day 3: Create agents

- `gym_agent.py`: Provides fitness and gym-related advice.
- `weather_agent.py`: Retrieves and provides weather information.

# 📅 Day 4: Run LLM on local machine

## 🎯 Objective

- Runing a Large Language Model (LLM) locally using Docker, FastAPI, and Ollama. This setup will allow you to interact with the LLM via an API, which you can access through FastAPI’s interactive docs.
- `docker-compose.yml`: Defines the Docker configuration for the Ollama service.
- `ollama_api.py`: FastAPI app that exposes the LLM API.

```bash
pip install uvicorn fastapi ollama
```

```bash
docker compose up
python ollama_api.py
uvicorn ollama_api:app --port 8000
```

- Open fastapi docs : http://127.0.0.1:8000/docs

# 📅 Day 5: RAG - Retrieval Augmented Generation

## 🎯 Objective

Enhance LLM responses using **RAG (Retrieval Augmented Generation)** by injecting relevant data into the prompt.

## 📦 Dependencies & Setup

### 1. 🔍 PyPDFLoader

- Used to load and parse PDF documents.

```bash
pip install langchain_community pypdf
```

### 2. 🔍 Text splitters

- Text splitters split documents into smaller chunks for use in downstream applications.

```bash
pip install langchain_text_splitters
```

### 3. 🔍 Embedding model

- create a vector representation of a piece of text
- OpenAIEmbeddings : use this model

```bash
pip install langchain-openai
```

### 4. 🔍 Qdrant

- docker-compose.db.yml

```bash
docker compose -f docker-compose.db.yml up
```

- open and check
  http://localhost:6333/
  http://localhost:6333/dashboard

- LangChain Qdrant : is a vector similarity search engine. It provides a production-ready service with a convenient API to store, search, and manage vectors with additional payload and extended filtering support

```bash
pip install langchain-qdrant
```

## ✅ Tips

- Always keep your `.env` file in `.gitignore` to protect your API keys.
- You can run each script independently to experiment with different techniques.
