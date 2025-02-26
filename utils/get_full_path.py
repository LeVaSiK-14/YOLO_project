import os


def get_full_path(dir_path: str, image_name: str) -> str:
    """
        Функция для получения полного пути
        Принимает в себя 
        - dir_path: str в какую папку добавить
        - image_name: str какую картинку или папку добавить
    """
    path = os.path.join(dir_path, image_name) # Создаем путь
    return path
