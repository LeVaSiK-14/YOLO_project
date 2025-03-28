# **Создание аннотированных данных для обучения нейронной сети YOLO**

## **Создание dataset для YOLO**

### 1. **Описание проекта**
- В проект загружается свой набор изначальных элементов которые мы хотим научить **YOLO** искать на изображениях<br>
- Софт создает дубликаты изображений, а так же искажает их<br>
- Первоначальные элементы должны быть в как можно более лучшем качестве<br>
- Создается указанное колличество элементов, сколько создавать элементов указывается в файле конфига(**utils/configs.py**)

### 2. **Инструкция по установке и запуску**
#### **Скачиваем проект** 
- Используйте команду `git clone https://github.com/LeVaSiK-14/YOLO_project.git` для установки проекта
- Перейдите в директорию с проектом командой `cd YOLO_project`
- Создайте виртуальное окружение `python3 -m venv env`
- Активируйте виртуальное окружение `source env/bin/activate`
- Установите все зависимости `python3 -m pip install -r requirements.txt`
- В корневом каталоге создайте директорию **elements** если ее нет и поместите в нее картинки которые вы хотите размножить и аннотировать
- Запустите команду `python3 main.py` и у вас запустится обработка изображений, в терминале будет видно на каком этапе сейчас выполнение кода и за сколько отрабатывают основные функции

### 3. **Результат выполнения работы**
- Вы увидите новую созданную директорию **dataset/**
> Внутри будет
1. Файл **data.yaml** в котором будет хранится вся структура для запуска обучения **YOLO**
2. Директория **images/** которая содержит еще 2 директории **train/** и **val/** 
3. Директория **labels/** которая содержит еще 2 директории **train/** и **val/** 
4. В директории **dataset/images/train/** будут готовые картинки для обучения
5. В директории **dataset/images/val/** будут готовые картинки для валидации
6. В директории **dataset/labels/train/** будут готовые анотации для каждой картинки для обучения
7. В директории **dataset/labels/val/** будут готовые анотации для каждой картинки для валидации

- **Теперь вы можете использовать директорию dataset/ для обучения YOLO**

### 4. **Запуск обучения нейронки YOLO v5x**
1. Для запуска перейдите в директорию **yolov5** командой `cd yolov5`
2. Запустите процесс обучения 
> `python train.py --img 640 --batch 32 --epochs 40 --data ../dataset/data.yaml --weights yolov5x.pt`
> `python train.py --img 640 --batch 16 --epochs 20 --data ../dataset/data.yaml --weights runs/train/exp3/weights/best.pt`
3. После успешного обучения запустите команду для обнаружения элементов на чертежах
> `python detect.py --weights runs/train/exp6/weights/best.pt --source ../images/one_big.png --img 1920 --conf 0.45 --view`
> `python detect.py --weights runs/train/exp6/weights/best.pt --source ../images/ --img 1920 --conf 0.45 --view --project ../images/detection_results --name images_results`


> **АКТУАЛЬНЫЕ ВЕСА runs/train/exp2** ДАТАСЕТ НА КАРТИНКАХ БЕЗ НОВЫХ ЭЛЕМЕНТОВ
> **АКТУАЛЬНЫЕ ВЕСА БОЛЕЕ НОВЫЕ runs/train/exp3** ДАТАСЕТ С НОВЫМИ ЭЛЕМЕНТАМИ
> **ЛУЧШИЕ АКТУАЛЬНЫЕ ВЕСА runs/train/exp** ДАТАСЕТ С ЭЛЕМЕНТАМИ ЧЕРТЕЖА(МАЛЕНЬКИЙ 16ШТ) хорошо ищет крупные элементы и 40-50% мелких
> **ЛУЧШИЕ АКТУАЛЬНЫЕ ВЕСА runs/train/exp5** ДАТАСЕТ С ЭЛЕМЕНТАМИ ЧЕРТЕЖА(БОЛЬШОЙ 360ШТ) хорошо ищет мелкие элементы но не ищет крупные

### 4. **Контакты**
> Создатель: **Бойко Лев**<br>
> Gmail: **lev201611@gmail.com**<br>
> Telegram: **[Mr_LeVaSiK_Z](https://t.me/Mr_LeVaSiK_Z)**


##### **Смотреть состояние видеокарты**
> `watch -n 1 nvidia-smi`

##### **Смотреть на графике RAM, CPU, GPU**
> `psensor`




python train.py --img 640 --batch 16 --epochs 30 --data ../dataset/data.yaml --weights yolov5m.pt
python train.py --img 640 --batch 16 --epochs 300 --data ../dataset_full/data.yaml --weights runs/train/exp/weights/best.pt


python detect.py --weights runs/train/exp2/weights/best.pt --source ../images/one.png --img 640 --conf 0.45 --view
python detect.py --weights runs/train/exp2/weights/best.pt --source ../images/one_big.png --img 1920 --conf 0.30 --view
python detect2.py --weights runs/train/exp5/weights/best.pt --source ../images1920/ --img 1920 --conf 0.45 --view --project ../images --name images_results_1920_new_exp5_id


all_elements/ - список всех элементов
dataset/ - датасет из элементов по 1 на изображении(автогенерация)
dataset2/ - Датасет на основе чертежей 640 на 640(16 шт)
dataset3/ - Датасет на основе чертежей из 360 картинок 640 на 640 но аннотированно не все(багует)
dataset_full/ - тот же dataset3 но проаннотированно все
