import openai
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the new OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_docs(prompt):
    response = client.chat.completions.create(  # Updated syntax
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

print(generate_docs("Write MkDocs markdown for a GET /shipments endpoint"))