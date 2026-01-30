from google.genai import types
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
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
    ),
)