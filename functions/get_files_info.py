from pathlib import Path
from google.genai import types # type: ignore 

def get_files_info(work_dir, directory="."):
    workdir = Path(work_dir).resolve()
    target_dir = (workdir / (directory)).resolve()

    # Security check: must stay inside workdir
    if workdir not in target_dir.parents and target_dir != workdir:
        return f'Error: Directory "{directory}" not within working directory "{work_dir}".'

    try:
        contents = []
        for item in target_dir.iterdir():
            contents.append(
                f"- {item.name}: filesize {item.stat().st_size} bytes, is directory: {item.is_dir()}"
            )
        return "\n".join(contents)
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
