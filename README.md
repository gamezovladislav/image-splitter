# Разделитель изображений

Это простое приложение на Python с графическим интерфейсом, которое позволяет пользователям загружать изображение, разделять его на две части и сохранять каждую часть отдельно.

## Возможности

- Загрузка изображений форматов PNG, JPG и BMP
- Интерактивное разделение изображения с помощью слайдера
- Предварительный просмотр разделения в реальном времени
- Сохранение левой и правой частей изображения отдельно

## Требования

- Python 3.6+
- PyQt5

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your-username/image-splitter.git
   cd image-splitter
   ```

2. Создайте виртуальное окружение (рекомендуется):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux и macOS
   venv\Scripts\activate  # Для Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Использование

1. Запустите приложение:
   ```bash
   python main.py
   ```

2. Нажмите кнопку "Загрузить изображение" и выберите файл изображения.

3. Используйте слайдер для выбора позиции разделения изображения.

4. Нажмите кнопку "Сохранить разделенные изображения" для сохранения левой и правой частей.

5. Выберите место сохранения для каждой части изображения.

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности смотрите в файле LICENSE.