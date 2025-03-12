import os
from PIL import Image


def resize_images(input_dir: str, output_dir: str) -> None:
    for filename in os.listdir(input_dir):
        # Полный путь к файлу
        input_path = os.path.join(input_dir, filename)
        
        # Проверяем, является ли файл изображением (можно дополнительно проверить расширение)
        if not os.path.isfile(input_path):
            continue
        
        try:
            # Открываем изображение
            img = Image.open(input_path)
            
            # Получаем его размеры
            width, height = img.size
            
            # Создаем новое изображение 640х640 с белым фоном (RGB, белый=(255,255,255))
            new_img = Image.new('RGB', (640, 640), (255, 255, 255))
            
            # Считаем, куда нужно «вклеить» исходное изображение, чтобы оно оказалось по центру
            x_offset = (640 - width) // 2
            y_offset = (640 - height) // 2
            
            # «Вклеиваем» (paste) исходное изображение поверх белого фона
            new_img.paste(img, (x_offset, y_offset))
            
            # Сохраняем результат в папку output_images
            output_path = os.path.join(output_dir, filename)
            new_img.save(output_path, quality=95)
            
            print(f"Обработано: {filename}")
        except Exception as e:
            print(f"Ошибка с файлом {filename}: {e}")
