import re


def get_file_name(path: str) -> str:
    full_name = path.split('/')[-1]
    name = full_name.split('.')[0]
    return name


def get_file_name_for_class(path: str) -> str:
    full_name = get_file_name(path)
    result = re.sub(r'_\d+__\d+$', '', full_name)
    result = result.replace('train_', '').replace('val_', '')
    return result
