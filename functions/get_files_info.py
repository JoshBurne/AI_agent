import os

def get_files_info(working_directory, directory=None):
    
    absolute_working_directory = get_path(working_directory)
    combined_target_directory = os.path.join(absolute_working_directory, directory)
    absolute_target_directory = os.path.abspath(combined_target_directory)

    
    if os.path.isdir(absolute_target_directory):
    
        if absolute_target_directory.startswith(absolute_working_directory):
            directory_contents = ""

            for content in list_contents(absolute_target_directory):
                content_path = os.path.join(absolute_target_directory, content)

                file_name = content
                directory_contents = directory_contents + "- " + file_name + ": "
                
                file_size = get_size(content_path)
                directory_contents = directory_contents + file_size
                
                is_directory = validate_directory(content_path)
                directory_contents = directory_contents + is_directory + "\n"
            
            return directory_contents
           
        else:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    else:
        return f'Error: "{directory}" is not a directory'



def get_path(dir):
    return os.path.abspath(dir)

def list_contents(dir_path):
    return os.listdir(dir_path)

def get_size(file_path):
    return f"file_size={os.path.getsize(file_path)}, "

def validate_directory(path):
    return f"is_dir={os.path.isdir(path)}"

