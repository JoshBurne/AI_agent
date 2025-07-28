import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)



# PROMPT IS CHOSEN FROM THE SECOND CLI ARGUMENT AFTER THE SCRIPT NAME
if len(sys.argv) > 1:
    arg_response = sys.argv[1]
else:
    # exit with error code if not second cli arg is given.
    print("Error: Please run the code with an argument")
    sys.exit(1)
    

messages = [
    types.Content(role="user", parts=[types.Part(text=arg_response)]),
]

#generate a response using google gemini:
response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
if len(sys.argv) >= 3:
    if sys.argv[2] == "--verbose":
        # print the users prompt
        print(f"User prompt: {arg_response}")
        # print the tokens used in the prompt
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        # print the tokens used in the response
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else: 
        raise Exception ("sys.argv[2] should only be 'None' or '--verbose'")
# print the response
print(response.text)



