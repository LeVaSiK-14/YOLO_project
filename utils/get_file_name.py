import re


def get_file_name(path: str) -> str:
    """
        Функция для получения названия файла без расширения из полного пути к файлу 
        Принимает в себя:
        - path: str путь к картинке
        Возвращает название файла
    """
    full_name = path.split('/')[-1] # Обрезаем весь путь к файлу
    name = full_name.split('.')[0] # Убираем расширение файла
    return name 


def get_file_name_for_class(path: str) -> str:
    """
        Функция для получения простого названия файла без нумерации и ключевых слов
        Нужна для создания класса для группы картинок
        Принимает в себя:
        - path: str путь к картинке
        Возвращает простое название

    """
    full_name = get_file_name(path) # Получаем название файла 
    result = re.sub(r'_\d+__\d+$', '', full_name) # Используя регулярку удаляем лишнюю нумерацию
    result = result.replace('train_', '').replace('val_', '') # Убираем лишние слова из названия, такие как: train_ и val_
    result = result.split('___')[-1]
    return result
