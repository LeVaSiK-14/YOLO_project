# **Создание аннотированных данных для обучения нейронной сети YOLO**

## **Создание dataset для YOLO**

### 1. **Описание проекта**
- В проект загружается свой набор изначальных элементов которые мы хотим научить YOLO искать на изображениях<br>
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
1. Файл **data.yaml** в котором будет хранится вся структура для запуска обучения YOLO
2. Директория **images/** которая содержит еще 2 директории **train/** и **val/** 
3. Директория **labels/** которая содержит еще 2 директории **train/** и **val/** 
4. В директории **dataset/images/train/** будут готовые картинки для обучения
5. В директории **dataset/images/val/** будут готовые картинки для валидации
6. В директории **dataset/labels/train/** будут готовые анотации для каждой картинки для обучения
7. В директории **dataset/labels/val/** будут готовые анотации для каждой картинки для валидации

- **Теперь вы можете использовать директорию dataset/ для обучения YOLO**

### 4. **Контакты**
> Создатель: **Бойко Лев**<br>
> Gmail: **lev201611@gmail.com**<br>
> Telegram: **[Mr_LeVaSiK_Z](https://t.me/Mr_LeVaSiK_Z)**