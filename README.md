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

**Day 2: Mastering Prompting Techniques**

### Install Google Generative AI SDK:

```bash
pip install google-genai
```

Explore different prompting techniques:

- ✅ Zero-shot Prompting → `chat_gemini.py`
- ✅ Few-shot Prompting → `chat_2.py`
- ✅ Chain-of-Thought Prompting → `chat_3.py`
- ✅ OpenAI Chat Example → `chat_1.py`

## ✅ Tips

- Always keep your `.env` file in `.gitignore` to protect your API keys.
- You can run each script independently to experiment with different techniques.
