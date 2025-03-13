import os
import cv2

from utils.services.get_file_name import(
    get_file_name_for_class,
)
from utils.services.get_full_path import(
    get_full_path,
)
from utils.services.get_files_from_dirs import(
    get_files_from_dir,
)
from utils.services.get_image_class_id import(
    get_class_id_by_name,
)
from utils.services.utils import(
    measure_time,
)
from tqdm import tqdm


@measure_time # Декоратор для замера скорости работы функции
def create_annotation_for_image(images_dir: str, labels_dir: str, classes_file_path: str) -> None:
    """
        Функция для анотирования каждой картинки из папок 
        dataset/images/train/
        dataset/images/val/

        Помещение анотаций в папки
        dataset/labels/train/
        dataset/labels/val/
        В зависимости от того что за картинка

        Принимает в себя:
        - images_dir: str путь к директории с картинками для аннотирования
        - labels_dir: str путь к директории куда помещать анотации картинок
        - classes_file_path: str путь к файлу с id и названием класса картинок для YOLO
    """
    images_dir_elements = get_files_from_dir(images_dir)

    for file_name in tqdm(images_dir_elements): # Получаем все картинки из папки

        if file_name.lower().endswith(".png"): # Смотрим что бы расширение картинки было .png
            img_path = get_full_path(images_dir, file_name) # Получаем полный путь к картинке
            img_name = get_file_name_for_class(img_path) # Получаем название картинки для определения класса
            
            class_id = get_class_id_by_name(img_name, classes_file_path) # По названию картинки получаем ID класса

            img = cv2.imread(img_path) # Читаем картинку
            h_img, w_img, _ = img.shape # Получаем изначальную высоту и ширину картинки

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Переводим картинку в серый цвет для openCV

            _, thresh = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY_INV) # Преобразует картинку в черно-белый где все пиксели ниже 250 становятся черными, а остальные белыми
            
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Ищем контуры
            if not contours: # Проверяем были ли найдены контуры, если нет то пропускаем картинку сообщая об этом
                print(f'Контуры в картинке {img_path} не были найдены!')
                return
            
            c = max(contours, key=cv2.contourArea) # Берем максимальные контуры
            
            x, y, w, h = cv2.boundingRect(c) # Получаем 4 значения
            # x — координата по оси X (левый верхний угол) прямоугольника.
            # y — координата по оси Y (верхний левый угол) прямоугольника.
            # w — ширина прямоугольника.
            # h — высота прямоугольника.
            
            x_center = (x + w/2) / w_img # Определяем центр объекта на картинке по Х
            y_center = (y + h/2) / h_img # Определяем центр объекта на картинке по У
            width = w / w_img # Определяем ширину объекта
            height = h / h_img # Определяем высоту объекта
            
            txt_name = os.path.splitext(os.path.basename(img_path))[0] + ".txt" # Создаем дубликат файла .txt с названием как у картинки
            txt_path = get_full_path(labels_dir, txt_name) # Создаем путь к этому файлу внутри директории куда помещаем аннотации
            
            with open(txt_path, "w") as f: # Открываем файл на запись
                f.write(f"{class_id} {x_center} {y_center} {width} {height}\n") # Записываем ранее полученые значения
