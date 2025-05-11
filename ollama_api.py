from fastapi import FastAPI
from ollama import Client
from fastapi import Body

app = FastAPI()
ollama_client = Client(host='http://localhost:11434')

ollama_client.pull('gemma3:1b')

@app.get("/")
def read_root():
    return {"message": "Welcome to the Ollama API!"}

@app.post("/chat")
def chat(message: str = Body(...,description="Chat Message")):
    response = ollama_client.chat(model='gemma3:1b', messages=[
        {"role": "user", "content": message}
    ])
    return response['message']['content']