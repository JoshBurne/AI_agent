import os
from google.genai import types


def get_files_info(working_directory, directory="."):
    
    absolute_directory = os.path.abspath(os.path.join(working_directory, directory))

    # CHECK IF THE DIRECTORY ARGUMENT IS ACTUALLY A DIRECTORY
    if os.path.isdir(absolute_directory):

        # CHECK IF THE DIRECTORY ARGUMENT IS (NOT) INSIDE THE WORKING DIRECTORY
        target_dir_path = os.path.abspath(working_directory)
        if not absolute_directory.startswith(target_dir_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # IF IT IS, EXECUTE:
        else:
            dir_contents = os.listdir(absolute_directory) 
            dir_analysis = ""
            item_number = 0

            if directory == ".":
                name = "current_directory"
            else:
                name = directory


            
            # CYCLE THROUGH THE ITEMS IN THE DIRECTORY
            for item in dir_contents:
                item_number +=1
                item_path = os.path.join(absolute_directory, item)
            
                if len(dir_contents) == item_number:
                    dir_analysis = dir_analysis + f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}"
                else:
                    dir_analysis = dir_analysis + f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}" + "\n"

            return f"Result for '{name}' directory:" + "\n" + dir_analysis + "\n"
        

    # IF THE DIRECTORY ARGUMENT IS NOT A DIRECTORY TYPE.        
    else:
        return f'Error: "{directory}" is not a directory'

    

    


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)