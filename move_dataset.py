import os, shutil



dir_path = '/home/lev/Downloads/dataset_full/obj_train_data/combined_pngs'
output_dir_parh = 'dataset_full'


image_train_path = f'{output_dir_parh}/images/train'
image_val_path = f'{output_dir_parh}/images/val'
label_train_path = f'{output_dir_parh}/labels/train'
label_val_path = f'{output_dir_parh}/labels/val'


def get_file_name(path: str) -> str:
    full_name = path.split('/')[-1] # Обрезаем весь путь к файлу
    name, suffix = full_name.split('.') # Убираем расширение файла
    return name, suffix


def get_full_path(dir_path: str, image_name: str) -> str:
    path = os.path.join(dir_path, image_name) # Создаем путь
    return path


def move_dirs(path_from: str, path_to: str) -> None:
    for item in os.listdir(path_from): # Получаем каждый элемент из директории для переноса
        item_path = get_full_path(path_from, item) # Получаем полный путь к файлу или директории которые нужно переместить
        shutil.move(item_path, path_to) # Перемещаем элементы в новую директорию


def get_files_from_dir(dir_path: str) -> list:

    items: list = list() # Создаем массив для хранения названий
    txt: list = list()
    for item in os.listdir(dir_path): # Получаем каждый элемент из директории
        full_path_image = get_full_path(dir_path, item)
        if os.path.isfile(full_path_image): # Если элемент файл то добавляем его в массив файлов
            name, suffix = get_file_name(full_path_image)
            items.append(name) # Добавляем в массив файлов
            
    items = list(set(items))
    trains = items[:280]
    vals = items[280:]
    
    for train in trains:
        img_path = f'{dir_path}/{train}.png'
        txt_path = f'{dir_path}/{train}.txt'
        shutil.move(img_path, image_train_path)
        shutil.move(txt_path, label_train_path)
        
    for val in vals:
        img_path = f'{dir_path}/{val}.png'
        txt_path = f'{dir_path}/{val}.txt'
        shutil.move(img_path, image_val_path)
        shutil.move(txt_path, label_val_path)

print(get_files_from_dir(dir_path))