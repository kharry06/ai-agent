from google.genai import types
import subprocess
import os

def run_python_file(working_directory, file_path, args=None):
    try:
        file = os.path.join(working_directory, file_path)
        wd_abs = os.path.abspath(working_directory)
        file_abs = os.path.abspath(file)


        if os.path.commonpath([wd_abs, file_abs]) != wd_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_abs):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_abs.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", file_abs]
        if args != None:
            command.extend(args)

        result = subprocess.run(command, capture_output=True, text=True, cwd=working_directory, timeout=30)
        
        if result.returncode != 0:
            return f"Process exited with code {result.returncode}"
        if not result.stderr and not result.stdout:
            return "No output produced"
        
        if not result.stderr:
            return f"STDOUT: {result.stdout}"
        if not result.stdout:
            return f"STDERR: {result.stderr}"

        return f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"
    
    except Exception as e:
        return f'Error: executing Python file: {e}'
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file in the specified working directory with optional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of arguments to pass to the Python script",
            ),
        },
    ),
)