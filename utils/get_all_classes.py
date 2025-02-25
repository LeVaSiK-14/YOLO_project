

def get_all_classes(classes_file_path: str):
    classes: dict = dict()

    with open(classes_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        pair = line.strip().split(' ')
        if len(pair) == 2:
            id_, class_ = pair
            classes[class_] = id_

    class_amount = len(lines)

    return class_amount, classes
