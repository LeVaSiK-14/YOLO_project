import cv2
import albumentations as A
import os

from utils.configs import(
    MEDIA,
    NUM_TRAIN,
    NUM_VAL,
)
from utils.get_files_from_dirs import(
    get_dirs_from_dir,
)
from utils.process_dirs import(
    create_dir,
    delete_dirs,
)
from utils.get_full_path import(
    get_full_path,
)
from utils.get_file_name import(
    get_file_name,
)
from utils.utils import(
    measure_time,
)


@measure_time # Декоратор для замера скорости работы функции
def create_duplicate_elements(source_dir: str, output_train_dir: str, output_val_dir: str) -> None:
    """
        Функция для создания искаженных элементов каждой картинки для лучшего обучения нейросети YOLO
        Принимает в себя:
        - source_dir: str путь к директории с директориями внутри которых картинки которые нужно дублировать
        - output_train_dir: str путь к директории куда сохранять картинки для обучения
        - output_val_dir: str путь к директории куда сохранять картинки для валидации
    """
    # Создание рандомной трансформации картинок
    transform = A.Compose([
        A.Affine(
            rotate=(-30, 30),
            translate_percent={"x": (-0.1, 0.1), "y": (-0.1, 0.1)},
            scale=(0.8, 1.2),
            # shear=(-20, 20),
            interpolation=cv2.INTER_LINEAR,
            border_mode=cv2.BORDER_CONSTANT,
            fill=(255, 255, 255),
            p=0.7
        ),
        A.HorizontalFlip(p=0.5),
        A.VerticalFlip(p=0.5),
        # A.RandomBrightnessContrast(
        #     brightness_limit=(-0.1, 0),
        #     contrast_limit=(-0.2, 0.2), 
        #     p=0.5
        # )
    ])

    create_dir(MEDIA) # Создаем директорию media для хранения картинок(временного)

    full_output_train_dir = get_full_path(MEDIA, output_train_dir) # Получаем полный путь к папке для картинок для тренировки
    full_output_val_dir = get_full_path(MEDIA, output_val_dir) # Получаем полный путь к папке для картинок для валидации
    full_source_dir = get_full_path(MEDIA, source_dir) # Получаем полный путь к папке с папками внутри которй картинки для дублирования

    create_dir(full_output_train_dir) # Создание папки для картинок для обучения
    create_dir(full_output_val_dir) # Создание папки для картинок для валидации

    all_dirs = get_dirs_from_dir(full_source_dir) # Получаем список всех папок из изначальной папки
    
    for dir in all_dirs: # Получаем каждуй папку отдельно из массива в цикле
        dir_path = get_full_path(full_source_dir, dir) # Получаем полный путь к папке с картинками

        image_files = [f for f in os.listdir(dir_path) if f.endswith('.png')] # Получаем список картинок для дубликации внутри папки

        for img_name in image_files: # Получаем каждую картинку отдельно в цикле
            img_path = get_full_path(dir_path, img_name) # Получаем полный путь к картинке
            img = cv2.imread(img_path) # Читаем картинку с openCV

            
            for i in range(NUM_TRAIN): # Запускаем цикл NUM_TRAIN раз для создания дубликатов для обучения
                augmented = transform(image=img) # Создаем искаженное изображение
                aug_img = augmented['image'] # Получаем это изображение
                new_img_name = f"train_{get_file_name(img_path)}__{i+1}.png" # Присваеваем новое название с порядковым номером
                cv2.imwrite(get_full_path(full_output_train_dir, new_img_name), aug_img) # Сохраняем изображение

            
            for i in range(NUM_VAL): # Запускаем цикл NUM_VAL раз для создания дубликатов для валидации
                augmented = transform(image=img) # Создаем искаженное изображение
                aug_img = augmented['image'] # Получаем это изображение
                new_img_name = f"val_{get_file_name(img_path)}__{i+1}.png" # Присваеваем новое название с порядковым номером
                cv2.imwrite(get_full_path(full_output_val_dir, new_img_name), aug_img) # Сохраняем изображение

    delete_dirs(full_source_dir) # Удаляем изначальную директорию со всеми картинками за ненадобностью
