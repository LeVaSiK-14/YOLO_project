import os


def get_files_from_dir(dir_path: str) -> list:
    items = []
    for item in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, item)):
            items.append(item)
    
    return items


def get_dirs_from_dir(dir_path: str) -> list:
    folders = [item for item in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, item))]
    return folders



# val = len(get_files_from_dir('media/output_val_dir'))
# train = len(get_files_from_dir('media/output_train_dir'))
# print(val, 'В папке val')
# print(train, 'В папке train')
# print(val + train, "Всего")

