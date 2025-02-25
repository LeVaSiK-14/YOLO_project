from utils.get_files_from_dirs import(
    get_files_from_dir,
)
from utils.get_full_path import(
    get_full_path,
)
from utils.get_file_name import(
    get_file_name_for_class,
)
from utils.process_dirs import(
    create_file,
)


def get_class_id_by_name(class_name: str, file_path: str) -> int:
    create_file(file_path)
    last_id = -1
    class_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.strip().split(' ')
        if len(parts) == 2:
            class_id, name = parts
            class_dict[name] = int(class_id)
            last_id = max(last_id, int(class_id))
    
    if class_name in class_dict:
        return class_dict[class_name]
    
    new_id = last_id + 1
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"{new_id} {class_name}\n")
    
    return new_id


def get_image_class_ids(images_dir: str, file_path: str) -> None:
    create_file(file_path)
    for file_name in get_files_from_dir(images_dir):
        if file_name.lower().endswith(".png"):
            img_path = get_full_path(images_dir, file_name)
            img_name = get_file_name_for_class(img_path)
            get_class_id_by_name(img_name, file_path)
