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
from utils.configs import(
    ELEMENTS,
    MEDIA,
    AUGMENTED_IMAGES,
    OUTPUT_TRAIN_DIR, 
    OUTPUT_VAL_DIR,
    DATASET_IMAGE_VAL,
    DATASET_IMAGE_TRAIN,
    DATASET_IMAGES,
    CLASSES,
    DATA_YAML,
    DATASET_LABEL_TRAIN,
    DATASET_LABEL_VAL,
    DATASET,
)


@measure_time
def main():

    delete_dirs(DATASET)
    delete_file(CLASSES)
    
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
        CLASSES
    )
    create_annotation_for_image(
        DATASET_IMAGE_TRAIN,
        DATASET_LABEL_TRAIN,
        CLASSES
    )


if __name__ == "__main__":
    main()
