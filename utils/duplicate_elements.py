import cv2
import albumentations as A
import os

from utils.configs import(
    MEDIA,
)
from utils.get_files_from_dirs import(
    get_dirs_from_dir,
)
from utils.create_dir import(
    create_dir,
)
from utils.get_full_path import(
    get_full_path,
)
from utils.get_file_name import(
    get_file_name,
)


def create_duplicate_elements(source_dir: str, output_train_dir: str, output_val_dir: str) -> None:

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
        A.RandomBrightnessContrast(p=0.5)
    ])

    create_dir(MEDIA)

    full_output_train_dir = get_full_path(MEDIA, output_train_dir)
    full_output_val_dir = get_full_path(MEDIA, output_val_dir)
    full_source_dir = get_full_path(MEDIA, source_dir)

    create_dir(full_output_train_dir)
    create_dir(full_output_val_dir)

    all_dirs = get_dirs_from_dir(full_source_dir)
    
    for dir in all_dirs:
        dir_path = get_full_path(full_source_dir, dir)

        image_files = [f for f in os.listdir(dir_path) if f.endswith('.png')]

        for img_name in image_files:
            img_path = os.path.join(dir_path, img_name)
            img = cv2.imread(img_path)

            num_train = 8
            num_val = 3
            
            for i in range(num_train):
                augmented = transform(image=img)
                aug_img = augmented['image']
                new_img_name = f"train_{get_file_name(img_path)}__{i+1}.png"
                cv2.imwrite(os.path.join(full_output_train_dir, new_img_name), aug_img)

            
            for i in range(num_val):
                augmented = transform(image=img)
                aug_img = augmented['image']
                new_img_name = f"val_{get_file_name(img_path)}__{i+1}.png"
                cv2.imwrite(os.path.join(full_output_val_dir, new_img_name), aug_img)


