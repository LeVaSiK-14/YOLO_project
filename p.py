import cv2

def draw_green_square(image_path, output_path):
    # Загружаем изображение
    image = cv2.imread(image_path)
    if image is None:
        print(f"Не удалось загрузить изображение: {image_path}")
        return

    # Преобразуем в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Применяем пороговую бинаризацию (инвертируем, если фон светлый)
    # Порог можно настроить в зависимости от условий изображения
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Находим внешние контуры
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        print("Контуры не найдены")
        return

    # Выбираем контур с максимальной площадью, предполагая, что он соответствует элементу
    main_contour = max(contours, key=cv2.contourArea)
    
    # Получаем ограничивающий прямоугольник
    x, y, w, h = cv2.boundingRect(main_contour)
    
    # Рисуем зеленый прямоугольник (цвет: (0, 255, 0), толщина 2 пикселя)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
    
    # Сохраняем результат
    cv2.imwrite(output_path, image)
    print(f"Изображение сохранено как: {output_path}")


draw_green_square("dataset/images/train/train_rotated_10_0___blue_lamp_13w__1.png", "annotated_image2.png")
