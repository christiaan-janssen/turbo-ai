import os


def write_file(working_directory: str, file_path: str, content: str):
    work_dir_path = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(work_dir_path, file_path))

    if not target_path.startswith(work_dir_path):
        print(
            f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        )
        return

    if os.path.isdir(target_path):
        print(f'Error: Cannot write to "{file_path}" as its a directory')
        return

    os.makedirs(work_dir_path, exist_ok=True)

    try:
        with open(target_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except:
        return "Error: problem writing to file"
