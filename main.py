from utils.duplicate_elements import(
    create_duplicate_elements,
)
from utils.resize_elements import(
    get_resized_images,
)
from utils.get_full_path import(
    get_full_path,
)
from utils.configs import(
    ELEMENTS,
    MEDIA,
    AUGMENTED_IMAGES,
    OUTPUT_TRAIN_DIR, 
    OUTPUT_VAL_DIR,
)


def main():
    get_resized_images(
        ELEMENTS,
        get_full_path(MEDIA, AUGMENTED_IMAGES)
    )
    create_duplicate_elements(
        AUGMENTED_IMAGES, 
        OUTPUT_TRAIN_DIR, 
        OUTPUT_VAL_DIR
    )


if __name__ == "__main__":
    main()
