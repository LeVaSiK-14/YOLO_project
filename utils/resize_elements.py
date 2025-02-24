import cv2
import numpy as np
import os
import random

from utils.get_file_name import(
    get_file_name,
)
from utils.create_dir import(
    create_dir,
)
from utils.get_files_from_dirs import(
    get_files_from_dir,
)
from utils.get_full_path import(
    get_full_path,
)
from utils.configs import(
    MEDIA,
)


def get_resized_images(images_dir_path: str, output_dir_path: str) -> None:

    create_dir(MEDIA)


    image_size = 256
    object_size = 110

    num_images = 8

    all_images = get_files_from_dir(images_dir_path)

    for image in all_images:
        image_path = get_full_path(images_dir_path, image)
        image_name = get_file_name(image)

        image_name_dir = get_full_path(output_dir_path, image_name)
        create_dir(image_name_dir)

        for i in range(num_images):
            bg_color = (255, 255, 255)
            img = np.full((image_size, image_size, 3), bg_color, dtype=np.uint8)
            
            object = cv2.imread(image_path)
            object = cv2.resize(object, (object_size, object_size))
            
            x_min = random.randint(0, image_size - object_size)
            y_min = random.randint(0, image_size - object_size)
            x_max = x_min + object_size
            y_max = y_min + object_size
            
            img[y_min:y_max, x_min:x_max] = object
            
            img_name = f"{image_name}_{i+1}.png"
            cv2.imwrite(os.path.join(image_name_dir, img_name), img)
    
