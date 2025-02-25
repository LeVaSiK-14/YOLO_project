import time
import functools

from utils.process_dirs import(
    create_dir,
    create_file,
)


def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"Функция {func.__name__} выполнилась за {elapsed:.2f} сек")
        return result
    return wrapper


def create_dataset_dir(file: str, *dirs: list) -> None:
    for dir in dirs:
        create_dir(dir)
    
    create_file(file)
