from pathlib import Path
from google.genai import types #type: ignore


def write_file(work_dir = None, file_path = "default.txt", content = "loremipsum"):
    if work_dir is None:
        work_dir = Path.cwd()
    
    try: 
        work_dir = Path(work_dir).resolve()
        target = (work_dir / file_path).resolve()

        #Check if requested file path is within working directory

        if work_dir not in target.parents:
            return f'Error: "{file_path}" is outside the working directory'

        #Prevent overwriting a directory
        if target.exists() and target.is_dir():
            return f'Error: "{file_path}" is a directory, not a file'
        
        # Create parent dirs and write
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

        return f'Successfully wrote to \"{file_path}\" ({len(content)} characters)'

    except Exception as e:
        return f"Error: {e}"

    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes a plain text file to the specified file and if it doesn't exist it will create the file. All files must end on .txt",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file that needs to be written relative to the working directory. If folders are specified within the path they will also be created as long as no folders of the same name exist. By default all files are created in the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content of the file that will be written. It does not add to a file, so it will always overwrite the previous content and start from a blank slate",
            )
        },
    ),
)