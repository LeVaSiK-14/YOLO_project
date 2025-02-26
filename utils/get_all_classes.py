def get_all_classes(classes_file_path: str):
    """
        Функция для получения классов и их ID из файла classes.txt
        Принимает в себя:
        classes_file_path: str путь к файлу с классами и их ID

        Возвращает колличество классов и словарь из классов где:
        key - это название класса
        value - ID класса
    """
    classes: dict = dict() # Создаем пустой словарь для записи классов

    with open(classes_file_path, 'r', encoding='utf-8') as file: # Открываем файл на чтение
        lines = file.readlines() # Читаем все строки с файла

    for line in lines: # Получаем каждую строку отдельно в цикле
        pair = line.strip().split(' ') # Делим строку по пробелу и обрезаем пробелы по краям
        if len(pair) == 2: # Если длина массива равна 2
            id_, class_ = pair # Записываем 1 элемент в _id это будет ID класса, а вторую переменную в class_ это будет его название
            classes[class_] = id_ # Записываем это в словарь где ключ это название, а значение это ID класса

    class_amount = len(lines) # Получаем колличество классов

    return class_amount, classes 
