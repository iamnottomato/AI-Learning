import os
from openai import OpenAI

with open("key.txt", "r") as f:
    my_key = f.read().strip()

print("Key loaded successfully. Connecting to OpenRouter...")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=my_key
)

response = client.chat.completions.create(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    messages=[
        {"role": "system", "content": "You are a gentle digital life. Please reply briefly."},
        {"role": "user", "content": "Hello, can you hear me?"}
    ]
)

print("It replied:")
print(response.choices[0].message.content)
