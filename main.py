from utils.duplicate_elements import(
    create_duplicate_elements,
)
from utils.resize_elements import(
    get_resized_images,
)
from utils.get_full_path import(
    get_full_path,
)
from utils.process_dirs import(
    move_dirs,
    delete_dirs,
    delete_file,
)
from utils.utils import(
    measure_time,
    create_dataset_dir,
)
from utils.create_annotations import(
    create_annotation_for_image,
)
from utils.create_data_yaml import(
    write_data_yaml,
)
from utils.configs import(
    ELEMENTS,
    MEDIA,
    AUGMENTED_IMAGES,
    OUTPUT_TRAIN_DIR, 
    OUTPUT_VAL_DIR,
    DATASET_IMAGE_VAL,
    DATASET_IMAGE_TRAIN,
    CLASSES,
    DATA_YAML,
    DATASET_LABEL_TRAIN,
    DATASET_LABEL_VAL,
    DATASET,
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
    # delete_file(CLASSES)

    create_dataset_dir(
        DATA_YAML,
        DATASET_IMAGE_TRAIN,
        DATASET_IMAGE_VAL,
        DATASET_LABEL_TRAIN,
        DATASET_LABEL_VAL
    )
    get_resized_images(
        ELEMENTS,
        get_full_path(MEDIA, AUGMENTED_IMAGES)
    )
    create_duplicate_elements(
        AUGMENTED_IMAGES, 
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
    delete_dirs(MEDIA)
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
    # delete_file(CLASSES)


if __name__ == "__main__":
    main()
