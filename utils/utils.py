import time
import functools


def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"Функция {func.__name__} выполнилась за {elapsed:.2f} сек")
        return result
    return wrapper
