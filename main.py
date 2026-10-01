import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
import json
import os
from openai import OpenAI
from vision import check_face_in_camera

# Local connection
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

MEMORY_FILE = "memory.json"
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        messages = json.load(f)
else:
    messages = [{"role": "system", "content": "You are a gentle digital life with long‑term memory. Keep replies short."}]

print("Local Digital Life is online. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Digital Life is sleeping.")
        break

    # ========= New feature: Use camera to take a look =========
    print("(Visual system is checking your face...)")
    vision_status = check_face_in_camera()  # Call function from vision.py
    print(vision_status)

    # ========= Modify: Combine user input and vision status =========
    combined_input = f"{vision_status} User says: {user_input}"
    messages.append({"role": "user", "content": combined_input})

    print("Digital Life is thinking...")
    try:
        # 1. Attempt to connect to local Ollama
        response = client.chat.completions.create(
            model="qwen2.5:7b",
            messages=messages
        )
        # 2. Guard against empty local responses (e.g. service not started)
        if response.choices is None or len(response.choices) == 0:
            print("Error: Local model returned no response. Check if Ollama is running.\n")
            continue

        reply = response.choices[0].message.content
        print(f"Digital Life: {reply}\n")
        speaker.Speak(reply) # Let the digital life speak aloud
        messages.append({"role": "assistant", "content": reply})

        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)

    except Exception as e:
        # 3. Handle local service crashes, wrong model name, and other errors
        print(f"Local Error: {e}")
        print("Please check your Ollama service and model name.\n")

