import os

def create_dir(dir_name: str) -> None:
    os.makedirs(dir_name, exist_ok=True)
