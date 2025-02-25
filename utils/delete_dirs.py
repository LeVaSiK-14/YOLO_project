import shutil


def delete_dirs(path_to_dir: str) -> None:
    shutil.rmtree(path_to_dir)
