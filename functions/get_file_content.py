import os
from .config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str):
    work_dir_path = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(work_dir_path, file_path))

    if not target_path.startswith(work_dir_path):
        print(
            f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        )
        return

    if not os.path.isfile(target_path):
        print(f'Error: File not found or is not a regular file: "{file_path}"')
        return

    file_content_string = ""
    with open(target_path) as f:
        file_content_string = f.read(MAX_CHARS)

    if len(file_content_string) == MAX_CHARS:
        return (
            file_content_string
            + f'[...File "{file_path}" truncated at 10000 characters]'
        )

    return file_content_string
