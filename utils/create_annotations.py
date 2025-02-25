import os
import cv2

from utils.get_file_name import(
    get_file_name_for_class,
)
from utils.get_full_path import(
    get_full_path,
)
from utils.get_files_from_dirs import(
    get_files_from_dir,
)
from utils.get_image_class_id import(
    get_class_id_by_name,
)


def create_annotation_for_image(images_dir: str, labels_dir: str, classes_file_path: str):

    for file_name in get_files_from_dir(images_dir):
        if file_name.lower().endswith(".png"):
            img_path = get_full_path(images_dir, file_name)
            img_name = get_file_name_for_class(img_path)
            
            class_id = get_class_id_by_name(img_name, classes_file_path)

            img = cv2.imread(img_path)
            h_img, w_img, _ = img.shape

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY_INV)
            
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if not contours:
                return
            
            c = max(contours, key=cv2.contourArea)
            
            x, y, w, h = cv2.boundingRect(c)
            
            x_center = (x + w/2) / w_img
            y_center = (y + h/2) / h_img
            width = w / w_img
            height = h / h_img
            
            txt_name = os.path.splitext(os.path.basename(img_path))[0] + ".txt"
            txt_path = os.path.join(labels_dir, txt_name)
            
            with open(txt_path, "w") as f:
                f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")
