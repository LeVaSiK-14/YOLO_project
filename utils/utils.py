import time
import functools

from utils.process_dirs import(
    create_dir,
    create_file,
)


def measure_time(func):
    """
        Функция для замера скорости работы других
        Используется в качестве декоратора
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"Функция {func.__name__} выполнилась за {elapsed:.2f} сек")
        return result
    return wrapper


def create_dataset_dir(file: str, *dirs: list) -> None:
    """
        Вспомогательная функция для создания директории dataset и всех ее вложенностей
        Принимает в себя:
        - file: str путь к файлу для создания
        - *dirs: list неограниченное колличество директорий которые будут создаваться в директории dataset
    """
    for dir in dirs: # Получаем каждую директорию по одной в цикле
        create_dir(dir) # Создаем эту директорию если ее нет
    create_file(file) # Создаем файл dataset/data.yaml
