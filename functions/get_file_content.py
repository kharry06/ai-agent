import os

def get_file_content(working_directory, file_path):
    file = os.path.join(working_directory, file_path)
    wd_abs = os.path.abspath(working_directory)
    file_abs = os.path.abspath(file)


    if not file_abs.startswith(wd_abs + os.sep):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        content = ""
        with open(file, 'r') as f:
            content = f.read(10000)
            if len(content) == 10000 and f.read(1):
                content += f'[...File "{file_path}" truncated at {1000} characters]'
        return content
    except:
        return f'Error: Could not read file: "{file_path}"'