import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config={
        "response_mime_type": "application/json",
        "temperature": 0.2
    }
)

def call_gemini(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text

def list_available_models():
    from google.generativeai import list_models
    models = list_models()
    print("Available models:")
    for model in models:
        print(model)

if __name__ == "__main__":
    list_available_models()
