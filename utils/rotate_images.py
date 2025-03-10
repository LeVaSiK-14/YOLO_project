import cv2

from utils.services.get_file_name import get_file_name
from utils.services.get_files_from_dirs import get_files_from_dir
from utils.services.get_full_path import get_full_path
from utils.services.utils import measure_time


@measure_time
def rotate_images(images_dir_path: str, output_images_dir_path: str, angles: list) -> None:
    all_images = get_files_from_dir(images_dir_path)
    
    for image in all_images:
        image_path = get_full_path(images_dir_path, image)
        img = cv2.imread(image_path)
        
        (h, w) = img.shape[:2]
        (cX, cY) = (w // 2, h // 2)
        
        for angle in angles:
            M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
            rotated_img = cv2.warpAffine(img, M, (w, h), borderValue=(255, 255, 255))
            file_name = get_file_name(image_path)
            output_file_name = f'{output_images_dir_path}/rotated_{angle}_{file_name}.png'
            cv2.imwrite(output_file_name, rotated_img)
