from utils.rotate_images import rotate_images
from utils.duplicate_elements import(
    create_duplicate_elements,
)
from utils.services.get_full_path import(
    get_full_path,
)
from utils.services.process_dirs import(
    move_dirs,
    delete_dirs,
)
from utils.services.utils import(
    measure_time,
    create_dataset_dir,
)
from utils.create_annotations import(
    create_annotation_for_image,
)
from utils.create_data_yaml import(
    write_data_yaml,
)
from utils.services.utils import(
    create_media_dir,
)
from utils.services.configs import(
    ANGELS,
    ELEMENTS,
    MEDIA,
    OUTPUT_TRAIN_DIR, 
    OUTPUT_VAL_DIR,
    DATASET_IMAGE_VAL,
    DATASET_IMAGE_TRAIN,
    CLASSES,
    DATA_YAML,
    DATASET_LABEL_TRAIN,
    DATASET_LABEL_VAL,
    DATASET,
    ROTATED_IMAGES,
)


@measure_time # Декоратор для замера скорости работы функции(покажет общее время работы программы)
def main():
    """
        Главная функция которая ничего в себя не принимает
        Нужна для запуска всех функций
        Шаги:
        1) Удаляем директорию dataset/ если она есть, что бы файлы не путались
        2) Удаляем файл classes.txt, что бы записывались новые классы
        3) Создаем новую пустую директорию dataset/ со всеми вложенностями
        4) Запускаем функцию по изменению размера картинок и их рандомному позицианированию
        5) Запускаем функцию по созданию искаженных дубликатов для каждой картинки
        6) Перемещаем файлы валидации в директорию dataset/images/val
        7) Перемещаем файлы обучения в директорию dataset/images/train
        8) Удаляем директорию media/ за ненадобностью
        9) Создание аннотаций для картинок валидации
        10) Создание аннотаций для картинок обучения
        11) Запись структуры в dataset/data.yaml 
        12) Удаления файла classses.txt
    """
    delete_dirs(DATASET)
    delete_dirs(MEDIA)
    create_media_dir(
        MEDIA,
        ROTATED_IMAGES,
    )
    create_dataset_dir(
        DATA_YAML,
        DATASET_IMAGE_TRAIN,
        DATASET_IMAGE_VAL,
        DATASET_LABEL_TRAIN,
        DATASET_LABEL_VAL,
        ROTATED_IMAGES,
    )
    rotate_images(
        ELEMENTS,
        ROTATED_IMAGES,
        ANGELS
    )
    create_duplicate_elements(
        ROTATED_IMAGES, 
        OUTPUT_TRAIN_DIR, 
        OUTPUT_VAL_DIR
    )
    move_dirs(
        get_full_path(MEDIA, OUTPUT_VAL_DIR),
        DATASET_IMAGE_VAL
    )
    move_dirs(
        get_full_path(MEDIA, OUTPUT_TRAIN_DIR),
        DATASET_IMAGE_TRAIN
    )
    create_annotation_for_image(
        DATASET_IMAGE_VAL,
        DATASET_LABEL_VAL,
        CLASSES,
    )
    create_annotation_for_image(
        DATASET_IMAGE_TRAIN,
        DATASET_LABEL_TRAIN,
        CLASSES,
    )
    write_data_yaml(
        DATA_YAML,
        CLASSES,
        DATASET_IMAGE_TRAIN,
        DATASET_IMAGE_VAL
    )
    delete_dirs(MEDIA)


if __name__ == "__main__":
    main()
