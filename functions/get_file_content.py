import os

def get_file_content(working_directory, file_path):

    absolute_working_directory = get_path(working_directory)
    print(f"absolute_working_directory = {absolute_working_directory}")
    print(f"file path = {file_path}")
    
    combined_target_directory = os.path.join(absolute_working_directory, file_path)
    print(f"combined_working_directory = {combined_target_directory}")
    absolute_target_directory = os.path.abspath(combined_target_directory)
    print(f"absolute_target_directory = {absolute_target_directory}")

    # if path is a file:
    if os.path.isfile(absolute_target_directory):
        print(f"the path is a 'file' file type.")
        
        # if path is inside the working directory:
        if absolute_target_directory.startswith(absolute_working_directory):
            
            max_chars = 10000
            with open(file_path,"r") as f:
                file_content_string = f.read(max_chars)
                resulting_string = file_content_string
                if len(file_content_string) > 10000:
                    resulting_string = resulting_string + f'[...File "{file_path}" truncated at "{max_chars}" characters].'
                    

        
        
        else:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    else:
        return f'Error: File not found or is not a regular file: "{file_path}"'

  
    




def get_path(dir):
    return os.path.abspath(dir)

def list_contents(dir_path):
    return os.listdir(dir_path)

def get_size(file_path):
    return f"file_size={os.path.getsize(file_path)}, "

def validate_directory(path):
    return f"is_dir={os.path.isdir(path)}"

if __name__ == "__main__":
    # Try running your function with some test inputs
    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "does_not_exist.txt"))