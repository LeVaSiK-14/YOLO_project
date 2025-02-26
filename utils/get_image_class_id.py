from utils.process_dirs import(
    create_file,
)


def get_class_id_by_name(class_name: str, file_path: str) -> int:
    """
        Функция для получения ID класса по его названию
        Если в файле нет такого названия класса то оно дозаписывается и ему присваевается новый ID класса
        Принимает в себя:
        - class_name: str название класса
        - file_path: str путь к файлу в котром искать
        Возвращает ID класса
    """
    create_file(file_path) # Создаем файл для записи классов если его нет
    last_id: int = -1 # создаем глобальную переменную для нумерации классов по порядку, ставим -1 что бы начать нумерацию с 0
    class_dict: dict = dict() # Словарь для записи класса и его ID
    with open(file_path, 'r', encoding='utf-8') as file: # Открываем файл на чтение
        lines = file.readlines() # Получаем список строк из файла

    for line in lines: # Получаем каждую строку отдельно в цикле
        parts = line.strip().split(' ') # Удаляем пробелы в строке по краям и делим по пробелу на массив
        if len(parts) == 2: # Если длина массива равна 2
            class_id, name = parts # Записываем в class_id номер класса, а в name название класса
            class_dict[name] = int(class_id) # Записываем значения в словарь где название это ключ, а ID это значение
            last_id = max(last_id, int(class_id)) # Запоминаем последний ID класса для получения следущего в случае надобности
    
    if class_name in class_dict: # Если название класса есть в словаре
        return class_dict[class_name] # Возвращаем ID класса
    
    new_id = last_id + 1 # Создаем новый ID, взяв последний и прибавив 1
    with open(file_path, "a", encoding="utf-8") as file: # Открываем файл на запись
        file.write(f"{new_id} {class_name}\n") # Записываем новый класс с новым ID класса
    
    return new_id # Возвращаем ID класса
