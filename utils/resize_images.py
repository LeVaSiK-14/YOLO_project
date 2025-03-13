from utils.services.utils import(
    measure_time,
)
from PIL import Image
from utils.services.get_files_from_dirs import(
    get_files_from_dir, get_full_path,
)
from tqdm import tqdm


@measure_time
def resize_images(input_dir: str, output_dir: str) -> None:

    input_files = get_files_from_dir(input_dir)
    
    for filename in tqdm(input_files):
        input_path = get_full_path(input_dir, filename)
            
        try:
            img = Image.open(input_path)
            
            width, height = img.size
            
            new_img = Image.new('RGB', (640, 640), (255, 255, 255))
            
            x_offset = (640 - width) // 2
            y_offset = (640 - height) // 2
            
            new_img.paste(img, (x_offset, y_offset))
            
            output_path = get_full_path(output_dir, filename)
            new_img.save(output_path, quality=95)

        except Exception as e:
            print(f"Ошибка с файлом {filename}: {e}")
