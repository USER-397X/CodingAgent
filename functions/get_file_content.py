import os

def get_file_content(working_dir, file_path, max_chars):
    abs_working_dir = os.path.abspath(working_dir)
    abs_file_path = os.path.abspath(os.path.join(working_dir, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: File {file_path} not within working directory {working_dir}.'

    if not os.path.isfile(abs_file_path):
        return f'Error: {file_path} is not a valid file.'

    try:
        with open(abs_file_path, 'r') as file:
            content = file.read(max_chars)
            if len(content) >= max_chars:
                content += "\n...[truncated]"
            return content

    except Exception as e:
        return f'Error reading file {file_path}: {str(e)}'