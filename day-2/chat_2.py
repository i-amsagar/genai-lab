from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

system_prompt = """
You are an AI Assistant who is specailized in maths.
You should not answer any query that is not realted to maths.

For a given query help user to solve that along with explanation.

Example:
Input: 2 + 2
Output: 2 + 2 i s4 which is calculated by adding 2 with 2.

Input: 3 * 10
Output: 3 * 10 which is calculated by multipling 3 by 10. Funfact you can even mutiply 10 * 3 which gave same result.

Input: Why is sky blue
Output: Bruh? You alright? Is it maths query?
"""

# Few short prompting
# give examples and set of instruction to give better result
# System Prompt : use for set background (inital context) / instruction
result = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role":"system", "content": system_prompt},
        {"role": "user", "content": "What is 6 * 40"}
    ],
)

print(result.choices[0].message.content)
