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
    delete_dirs
)
from utils.utils import(
    measure_time,
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
)


@measure_time
def main():
    delete_dirs(DATASET_IMAGES)
    
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


if __name__ == "__main__":
    main()
