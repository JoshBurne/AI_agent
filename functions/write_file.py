import os

def write_file(working_directory, file_path, content):
    print(f"\nDEBUG :: - NEW FUNCTION CALL ::")
    full_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_directory = os.path.abspath(working_directory)

    print(f"DEBUG :: - {full_file_path}")
    print(f"DEBUG :: - {abs_working_directory}")

    if not full_file_path.startswith(abs_working_directory):
        print(f"DEBUG :: - {file_path} not found in {working_directory}.")
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    else:
        directory_of_file_path = os.path.dirname(full_file_path)
        print(f"DEBUG :: - directory_of_file_path = {directory_of_file_path}")
        exist_check = os.path.exists(directory_of_file_path)
        print(f"DEBUG :: - existence check = {exist_check}")
        
        if exist_check == False:
            new_dir = os.makedirs(directory_of_file_path)
            print(f"new directory made = {new_dir}")
            print(f"DEBUG :: -  directory exists {directory_of_file_path}")
        with open(full_file_path, "w") as f:
            f.write(content)
            
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
