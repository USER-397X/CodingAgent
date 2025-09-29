from pathlib import Path
from google.genai import types # type: ignore 



def get_file_content(work_dir: str, file_path: str, max_chars: int):
    workdir = Path(work_dir).resolve()
    target = (workdir / file_path).resolve()

    # Security check: must stay inside working dir
    if workdir not in target.parents and target != workdir:
        return f'Error: File "{file_path}" not within working directory "{work_dir}".'

    # Check if target is an existing file
    if not target.is_file():
        return f'Error: "{file_path}" is not a valid file.'

    try:
        content = target.read_text(encoding="utf-8")[:max_chars]
        if target.stat().st_size > max_chars:
            content += "\n...[truncated]"
        return content
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a file and prints them as a plain text file, constrained to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to get the content from, relative to the working directory.",
            ),
            "max_chars": types.Schema(
                type=types.Type.INTEGER,
                description="The maximum number of characters that will be read from the file. If the number of characters in the file exceeds this number it will not be included in the output of the function"
            )
        },
    ),
)