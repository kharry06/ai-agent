import os

def write_file(working_directory, file_path, content):
    try:
        file = os.path.join(working_directory, file_path)
        wd_abs = os.path.abspath(working_directory)
        file_abs = os.path.abspath(file)


        if os.path.commonpath([wd_abs, file_abs]) != wd_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(file_abs):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        parent_dir = os.path.dirname(file_abs)
        os.makedirs(parent_dir, exist_ok=True)
        with open(file_abs, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error writing file "{file_path}": {e}'