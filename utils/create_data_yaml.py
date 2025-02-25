
from utils.get_all_classes import(
    get_all_classes,
)


def write_data_yaml(data_yaml_path: str, classes_file_path: str, train_path: str, val_path: str) -> None:

    class_amount, classes = get_all_classes(classes_file_path)

    with open(data_yaml_path, 'a', encoding='utf-8') as file:
        file.write(f'train: {train_path}\n')
        file.write(f'val: {val_path}\n\n')
        file.write(f'nc: {class_amount}\n\n')
        file.write(f'names:\n')

        for k, v in classes.items():
            file.write(f"    {v}: '{k}'\n")
