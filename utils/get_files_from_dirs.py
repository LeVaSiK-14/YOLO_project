import os

from utils.get_full_path import(
    get_full_path,
)


def get_files_from_dir(dir_path: str) -> list:
    """
        Функция для получения списка файлов из директории
        Принимает в себя:
        - dir_path: str путь к директории с файлами
        Возвращает список с названиями файлов
    """
    items: list = list() # Создаем массив для хранения названий
    for item in os.listdir(dir_path): # Получаем каждый элемент из директории
        if os.path.isfile(get_full_path(dir_path, item)): # Если элемент файл то добавляем его в массив файлов
            items.append(item) # Добавляем в массив файлов
    
    return items


def get_dirs_from_dir(dir_path: str) -> list:
    """
        Функция для получения списка директорий внутри другой директории
        Принимает в себя:
        - dir_path: str путь к директории
        Возвращает список директорий из первичной
    """
    folders = [item for item in os.listdir(dir_path) if os.path.isdir(get_full_path(dir_path, item))] 
    return folders



# val = len(get_files_from_dir('media/output_val_dir'))
# train = len(get_files_from_dir('media/output_train_dir'))
# print(val, 'В папке val')
# print(train, 'В папке train')
# print(val + train, "Всего")

