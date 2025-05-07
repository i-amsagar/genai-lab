from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

text = "During the meeting, the AI assistant suggested a coffee break every time it detected a drop in morale — now it's the most popular member of the team."

response = client.embeddings.create(
    input=text,
    model='text-embedding-3-small'
)

print("Vector Embeddings", response.data[0].embedding)