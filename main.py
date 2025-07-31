import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt
from functions.call_function import available_functions, call_function
import sys

def main ():
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
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            ),
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
        

    if not response.function_calls:
        print (response.text)
        sys.exit(0)

    for function_call_part in response.function_calls:
        # call the functuion and get the result
        function_result = call_function(function_call_part, verbose="--verbose" in sys.argv)

        if not function_result.parts or not function_result.parts[0].function_response or not function_result.parts[0].function_response.response:
            # Did the function have no parts at all? If yes, thats bad
            # OR
            # Did the first part exist, but it doesn't contain the function's response. Still bad.
            # OR
            # The function ran, but it didn’t return any result inside the expected structure. Still bad.
            raise Exception ("Fatal error, function did not return a valid response")
        
        response_content = function_result.parts[0].function_response.response.get("result")
        if "--verbose" in sys.argv:
            print(f"-> {response_content}")
        else:
            print(response_content)
        





if __name__ == "__main__":
    main()
