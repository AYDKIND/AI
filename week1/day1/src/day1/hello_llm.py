import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv(Path(__file__).parent / ".env")

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is missing. Check your .env file.")

client = Groq(api_key=api_key)

messages = [
    {"role": "system", "content": "Answer briefly. If you don't know something, say so."},
    {"role": "user", "content": "Do you know Padho with Pratyush"},
]

try:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        max_tokens=300,
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Request failed: {e}")