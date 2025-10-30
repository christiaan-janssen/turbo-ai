import os
import sys


def get_files_info(working_directory: str, directory="."):
    work_dir_path = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(work_dir_path, directory))

    print(target_path == work_dir_path)

    if not target_path.startswith(work_dir_path):
        print(
            f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        )
        return

    if not os.path.isdir(target_path):
        print(f'Error: "{directory}" is not a directory')

    dir_contents = os.listdir(target_path)
    for item in dir_contents:
        item_path = os.path.join(target_path, item)
        print(
            f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}"
        )
