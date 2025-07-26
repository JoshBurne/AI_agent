import os

def get_files_info(working_directory, directory="."):
    
    # DEBUG CONSOLE CODE
    print("\n")
    print("DEBUG: /// ANALYSING NEW DIRECTORIES ///")
    print(f"DEBUG: Working directory: {working_directory}")
    print(f"DEBUG: Directory: {directory}")
    # \ DEBUG CONSOLE CODE



    print(f"DEBUG: Absolute path of 'directory': {os.path.abspath(directory)}")
    absolute_directory = os.path.abspath(os.path.join(working_directory, directory))

    # CHECK IF THE DIRECTORY ARGUMENT IS ACTUALLY A DIRECTORY
    if os.path.isdir(absolute_directory):
        print(f"DEBUG: Validated that:'{directory}' is a directory type \n")

        
        

        # CHECK IF THE DIRECTORY ARGUMENT IS (NOT) INSIDE THE WORKING DIRECTORY
        target_dir_path = os.path.abspath(working_directory)
        if not absolute_directory.startswith(target_dir_path):
            print(f"DEBUG: Error: Cannot list '{directory}' as it is outside the permitted working directory")
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        


        # IF IT IS, EXECUTE:
        else:
            print(f"DEBUG: directory:'{directory}' was found in the working directory")
            print("\n")
            print (f"DEBUG: full path = {absolute_directory}")

            dir_contents = os.listdir(absolute_directory)
            print(f"DEBUG: directory contents = {dir_contents}")
            print("\n")

            
            dir_analysis = ""
            item_number = 0
            # CYCLE THROUGH THE ITEMS IN THE DIRECTORY
            for item in dir_contents:
                item_number +=1
                
                item_path = os.path.join(absolute_directory, item)
                size = os.path.getsize(item_path)
                is_dir = os.path.isdir(item_path)
                
                if len(dir_contents) == item_number:
                    dir_analysis = dir_analysis + f"- {item}: file_size={size} bytes, is_dir={is_dir}"
                else:
                    dir_analysis = dir_analysis + f"- {item}: file_size={size} bytes, is_dir={is_dir}" + "\n"
            print(dir_analysis)
            return dir_analysis
        
    

                   

    # IF THE DIRECTORY ARGUMENT IS NOT A DIRECTORY TYPE.        
    else:
        print(f"{directory} is not a directory")
        return f'Error: "{directory}" is not a directory'

    

    
