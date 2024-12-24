# Используем базовый образ с Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /bakruptapp

# Копируем requirements.txt в контейнер
COPY requirements.txt /bankruptapp/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /bankruptapp/

# Указываем команду для запуска вашего скрипта
CMD ["python", "bot.py"]
