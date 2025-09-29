from pathlib import Path
import subprocess
from google.genai import types #type: ignore

def run_python_file(work_dir: str, file_path: str, args = []):
    work_dir = Path(work_dir).resolve()
    target = (work_dir / file_path).resolve()

    #Check to see if the target is within the allowed directory
    if work_dir not in target.parents:
            return f'Error: "{file_path}" is outside the working directory'

    #Check to see if the file exists
    if not target.is_file():
          return f'Error: "{file_path}" is not a file'

    #Check to see if the file is a python file
    if not target.suffix == '.py':
          return f'Error: "{file_path}" is not a python file'
    
    #Run python program
    try:
        result = subprocess.run(
              ['python3', file_path] + args, 
              text = True,
              cwd = work_dir, timeout=30, 
              capture_output=True
        )
        
        output = []
        if result.stdout:
              output.append(f'STDOUT:\n{result.stdout}')
        if result.stderr:
              output.append(f'STDERROR:\n{result.stderr}')
        if result.returncode != 0:
              output.append(f'Process exited with code {result.returncode}')

        return '\n'.join(output) if output else 'No output produced'

    except Exception as e:
          return f'Error: executing Python file: {e}'

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)
    