import os
from config import character_limit

def get_file_content(working_directory, file_path):
    print(":::NEW CALL:::")

    
    # CONVERT THE FILE PATH AND DIRECTORY TO FULL PATHS AND JOIN THEM.
    full_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_directory = os.path.abspath(working_directory)
    print(f"DEBUG ::- full file path = {full_file_path}")
    print(f"DEBUG ::- abs_working_directory = {abs_working_directory}")
    

 
    
    # If the file path is outside of the working directory:
    if not full_file_path.startswith(abs_working_directory):
        print(f'DEBUG ::- Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        print("\n")
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            
    # If the file path is inside the working directory:
    else:
        print(f"DEBUG ::- file: '{file_path}' is inside the working directory:'{working_directory}'")
        print("\n")


        # CHECK IF THE FILEPATH IS NOT A FILE TYPE:
        if not os.path.isfile(full_file_path):
            print(f'DEBUG ::- Error: File not found or is not a regular file: "{full_file_path}"')
            print("\n")
            return f'Error: File not found or is not a regular file: "{full_file_path}"'
        
        else:
            print(f"DEBUG ::- file:{file_path} is a file type, and is within the working directory {working_directory}")

            with open(full_file_path, "r") as f:
                file_content_string = f.read(character_limit +1)
                character_length = len(file_content_string)
                if character_length > character_limit:
                    return file_content_string[:character_limit] + f'[...File "{file_path}" truncated at "{character_limit}" characters].'
                else: 
                    return f'{file_content_string}'
            
    print("\n")
    print("\n")















