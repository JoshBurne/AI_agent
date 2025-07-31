import os
from google.genai import types


def write_file(working_directory, file_path, content):
    full_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_directory = os.path.abspath(working_directory)


    if not full_file_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    else:
        directory_of_file_path = os.path.dirname(full_file_path)
        exist_check = os.path.exists(directory_of_file_path)

        
        if exist_check == False:
            new_dir = os.makedirs(directory_of_file_path)
            print(f"new directory made = {new_dir}")
        with open(full_file_path, "w") as f:
            f.write(content)
            
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite files",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the desired write/overwrite location",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The newly added content written to the file"
            )
        },
    ),
)