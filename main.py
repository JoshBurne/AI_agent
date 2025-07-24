import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv) > 1:
    arg_response = sys.argv[1]
else:
    print("Error: Please run the code with an argument")
    sys.exit(1)
    

response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=arg_response)
print(response.text)
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
