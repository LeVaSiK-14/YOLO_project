from utils.services.get_all_classes import(
    get_all_classes,
)


def write_data_yaml(data_yaml_path: str, classes_file_path: str, train_path: str, val_path: str) -> None:
    """
        Запись данных в файл dataset/data.yaml для запуска обучения YOLO
        Принимает в себя:
        - data_yaml_path: str путь к файлу куда записывать
        - classes_file_path: str путь к файлу с классами и их ID
        - train_path: str путь к директории с картинками для тренировки dataset/images/train
        - val_path: str путь к директории с картинками для валидации dataset/images/val
    """

    class_amount, classes = get_all_classes(classes_file_path) # Получаем список всех классов в формате dict()

    with open(data_yaml_path, 'a', encoding='utf-8') as file: # Открываем файл для дозаписи
        file.write(f'train: ../{train_path}\n') # 1 строка путь к картинкам для тренировки
        file.write(f'val: ../{val_path}\n\n') # 2 строка путь к картинкам для валидации
        file.write(f'nc: {class_amount}\n\n') # 4 строка общее колличество классов
        file.write(f'names:\n') # 6 строка обозначение для перечисления классов картинок

        for k, v in classes.items(): # Получаем каждуй класс и ID класса где: k это название, а v это ID класса
            file.write(f"    {v}: '{k}'\n") # Начиная с 7 строки поочередно записываем все классы 
