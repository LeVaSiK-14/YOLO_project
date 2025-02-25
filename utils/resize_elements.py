import cv2
import numpy as np
import os
import random

from utils.get_file_name import(
    get_file_name,
)
from utils.process_dirs import(
    create_dir,
)
from utils.get_files_from_dirs import(
    get_files_from_dir,
)
from utils.get_full_path import(
    get_full_path,
)
from utils.utils import(
    measure_time,
)
from utils.configs import(
    MEDIA,
    IMAGE_SIZE,
    OBJECT_SIZE,
    NUM_IMAGES,
)


@measure_time
def get_resized_images(images_dir_path: str, output_dir_path: str) -> None:

    create_dir(MEDIA)

    all_images = get_files_from_dir(images_dir_path)

    for image in all_images:
        image_path = get_full_path(images_dir_path, image)
        image_name = get_file_name(image)

        image_name_dir = get_full_path(output_dir_path, image_name)
        create_dir(image_name_dir)

        for i in range(NUM_IMAGES):
            bg_color = (255, 255, 255)
            img = np.full((IMAGE_SIZE, IMAGE_SIZE, 3), bg_color, dtype=np.uint8)
            
            object = cv2.imread(image_path)
            object = cv2.resize(object, (OBJECT_SIZE, OBJECT_SIZE))
            
            x_min = random.randint(0, IMAGE_SIZE - OBJECT_SIZE)
            y_min = random.randint(0, IMAGE_SIZE - OBJECT_SIZE)
            x_max = x_min + OBJECT_SIZE
            y_max = y_min + OBJECT_SIZE
            
            img[y_min:y_max, x_min:x_max] = object
            
            img_name = f"{image_name}_{i+1}.png"
            cv2.imwrite(os.path.join(image_name_dir, img_name), img)
    
