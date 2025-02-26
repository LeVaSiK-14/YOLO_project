import shutil
import os

from utils.get_full_path import(
    get_full_path,
)


def create_dir(dir_name: str) -> None:
    """
        Функция для создания новой директории
        Принимает в себя:
        - dir_name: str путь к директории которую нужно создать
    """
    os.makedirs(dir_name, exist_ok=True) # Создаем директорию если ее не существует


def move_dirs(path_from: str, path_to: str) -> None:
    """
        Функция для перемещения файлов и папок из одной директории в другую
        Принимает в себя:
        - path_from: str путь из какой директории переместить
        - path_to: str путь в какую директорию переместить
    """
    create_dir(path_to) # Создаем директорию для перемещения если ее нет
    for item in os.listdir(path_from): # Получаем каждый элемент из директории для переноса
        item_path = get_full_path(path_from, item) # Получаем полный путь к файлу или директории которые нужно переместить
        shutil.move(item_path, path_to) # Перемещаем элементы в новую директорию


def delete_dirs(path_to_dir: str) -> None:
    """
        Функция для удаления директории и всех ее вложеностей если такая директория существует
        Принимает в себя:
        - path_to_dir: str путь к директории которую нужно удалить
    """
    if os.path.exists(path_to_dir): # Проверяем если директория существует
        shutil.rmtree(path_to_dir) # Удаляем эту директорию


def create_file(file_name: str) -> None:
    """
        Функция для создания файла если его нет
        Принимает в себя:
        - file_name: str путь к файлу который нужно создать
    """
    if not os.path.exists(file_name): # Проверяем если файла нет
        with open(file_name, "w") as f: # открываем этот файл на запись
            pass # Ничего не записываем в этот файл, таким образом просто получаем новый пустой файл


def delete_file(file_path: str) -> None:
    """
        Функция для удаления файла если он существует
        Принимает в себя:
        - file_path: str путь к файлу который нужно удалить
    """
    if os.path.exists(file_path): # Проверяем существует ли файл
        os.remove(file_path) # Удаляем файл если он существует
