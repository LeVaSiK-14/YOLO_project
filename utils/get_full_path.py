import os

def get_full_path(dir_path: str, image_name: str) -> str:
    path = os.path.join(dir_path, image_name)
    return path
