import cv2
import numpy as np
import random

from utils.services.get_file_name import(
    get_file_name,
)
from utils.services.process_dirs import(
    create_dir,
)
from utils.services.get_files_from_dirs import(
    get_files_from_dir,
)
from utils.services.get_full_path import(
    get_full_path,
)
from utils.services.utils import(
    measure_time,
)
from utils.services.configs import(
    IMAGE_SIZE,
    OBJECT_SIZE,
    NUM_IMAGES,
)


@measure_time # Декоратор для замера скорости работы функции
def get_resized_images(images_dir_path: str, output_dir_path: str) -> None:
    """
        Функция для изменения размеров картинки и создание дубликатов это картинки с расположением в разных частях белого холста
        Принимает в себя:
        - images_dir_path: str путь к директории с картинками
        - output_dir_path: str путь к директории куда сохранять обработаные картинки
    """

    all_images = get_files_from_dir(images_dir_path) # Получаем список картинок из директории

    for image in all_images: # Получаем каждую картинку отдельно в цикле
        image_path = get_full_path(images_dir_path, image) # Получаем полный путь к картинке
        image_name = get_file_name(image) # Получаем название картинки

        image_name_dir = get_full_path(output_dir_path, image_name) # Создаем путь куда сохраним картинку
        create_dir(image_name_dir) # Создаем директорию куда сохраним картинку

        for i in range(NUM_IMAGES): # Запускаем цикл NUM_IMAGES раз для создания такого колличества картинок 
            bg_color = (255, 255, 255) # Задаем цвет для заднего фона на шаблоне
            img = np.full((IMAGE_SIZE, IMAGE_SIZE, 3), bg_color, dtype=np.uint8) # Создаем картинку нужного размера IMAGE_SIZE Х IMAGE_SIZE
            
            object = cv2.imread(image_path) # Читаем картинку с openCV
            object = cv2.resize(object, (OBJECT_SIZE, OBJECT_SIZE)) # Изменяем размер картинки
            
            x_min = random.randint(0, IMAGE_SIZE - OBJECT_SIZE) # Получаем минимальное значение по Х
            y_min = random.randint(0, IMAGE_SIZE - OBJECT_SIZE) # Получаем минимальное значение по У
            x_max = x_min + OBJECT_SIZE # Получаем максимальное значение по Х
            y_max = y_min + OBJECT_SIZE # Получаем максимальное значение по У
            
            img[y_min:y_max, x_min:x_max] = object # Помещаем картинку на белый фон
            
            img_name = f"{image_name}_{i+1}.png" # Создаем название файла
            cv2.imwrite(get_full_path(image_name_dir, img_name), img) # Сохраняем картинку
