


def get_file_name(path: str) -> str:
    full_name = path.split('/')[-1]
    name = full_name.split('.')[0]
    return name
