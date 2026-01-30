from google.genai import types
import os

def get_file_content(working_directory, file_path):
    try:
        file = os.path.join(working_directory, file_path)
        wd_abs = os.path.abspath(working_directory)
        file_abs = os.path.abspath(file)


        if os.path.commonpath([wd_abs, file_abs]) != wd_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        content = ""
        with open(file_abs, "r") as f:
            content = f.read(10000)
            if f.read(1):
                content += (
                    f'[...File "{file_path}" truncated at {10000} characters]'
                )
            return content
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the content of a specified file relative to the working directory",
    parameters=types.Schema(
        required=["file_path"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            ),
        },
    ),
)