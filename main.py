import os 
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import get_files_info

def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key = api_key)

    if len(sys.argv) <= 1:
        print("Usage: python main.py '<your question here>'")
        sys.exit(1)
    
    prompt = sys.argv[1]

    messages = [
        types.Content(role='user', parts = [types.Part(text=prompt)])]
    
    response = client.models.generate_content(
        model = "gemini-2.0-flash-001",
        contents = prompt, 
    )

    print(response.text)

if __name__ == "__main__":  
    main()