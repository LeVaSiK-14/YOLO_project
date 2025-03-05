"""
Прописаны все пути к директориям и файлам, а так же конфиги картинок
"""

MEDIA: str = 'media'
DATASET: str = 'dataset'
ELEMENTS: str = 'all_elements/elements3'

AUGMENTED_IMAGES: str = 'augmented_images'
OUTPUT_TRAIN_DIR: str = 'output_train_dir'
OUTPUT_VAL_DIR: str = 'output_val_dir'

DATASET_IMAGES: str = 'dataset/images'
DATASET_LABEL: str = 'dataset/labels'

DATASET_IMAGE_TRAIN: str = 'dataset/images/train'
DATASET_IMAGE_VAL: str = 'dataset/images/val'

DATASET_LABEL_TRAIN: str = 'dataset/labels/train'
DATASET_LABEL_VAL: str = 'dataset/labels/val'


NUM_TRAIN: int = 20 # Колличество искаженных картинок для обучения из 1
NUM_VAL: int = 5 # Колличество искаженных картинок для валидации из 1

IMAGE_SIZE: int = 256 # Желаемый размер картинки 256х256
OBJECT_SIZE: int = 110 # Изначальный размер картинки 110х110
NUM_IMAGES: int = 20 #Колличество картинок из 1 разного позицианирования на холсте 256х256


CLASSES: str = 'classes.txt'
DATA_YAML: str = 'dataset/data.yaml'
