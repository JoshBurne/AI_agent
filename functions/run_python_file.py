import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):

    full_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    full_working_directory = os.path.abspath(working_directory)
    print(f"\n \nfull_file_path = {full_file_path}")
    print(f"working directory = {full_working_directory}")

    if not full_file_path.startswith(full_working_directory):
        print(f"DEBUG :: - Error! - file is outside the working directory")
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    else:
        exists_check = os.path.exists(full_file_path)
        if not exists_check:
            print(f"DEBUG :: - Error! - file path does not point to an existing file")
            return f'Error: File "{file_path}" not found.'
        else:
            print(f"DEBUG :: - Success! - file path points to an existing file in the working directory")

            if not full_file_path.endswith(".py"):
                print(f"DEBUG :: - Error! - File is not a Python file.")
                return f'Error: "{file_path}" is not a Python file.'
        
            else:
                print(f"DEBUG :: - Success! - File is a .py file")
                
                try:
                    result = subprocess.run(
                        ["python", full_file_path] + args, 
                        capture_output=True, 
                        text=True,
                        timeout=30,
                        cwd=full_working_directory
                        )
                    
                    
                    if not result.stdout.strip() and not result.stderr.strip():
                        return f'No output produced'
                    else:
                        if result.returncode != 0:
                            return f'STDOUT:\n{result.stdout}\n\nSTDERR: {result.stderr}\n\nProcess exited with code {result.returncode}'
                        return f'STDOUT:\n{result.stdout}\n\nSTDERR {result.stderr}'
                except:
                    return f"Error: executing Python file: {file_path}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files with optional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the the file that needs to run",
            ),
        },
    ),
)