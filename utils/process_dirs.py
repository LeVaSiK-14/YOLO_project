import shutil
import os

from utils.get_full_path import(
    get_full_path,
)


def create_dir(dir_name: str) -> None:
    os.makedirs(dir_name, exist_ok=True)


def move_dirs(path_from: str, path_to: str) -> None:
    create_dir(path_to)
    for item in os.listdir(path_from):
        item_path = get_full_path(path_from, item)
        shutil.move(item_path, path_to)


def delete_dirs(path_to_dir: str) -> None:
    if os.path.exists(path_to_dir):
        shutil.rmtree(path_to_dir)


def create_file(file_name: str) -> None:
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            pass


def delete_file(file_path: str) -> None:
    if os.path.exists(file_path):
        os.remove(file_path)
