# Базовый образ
FROM python:3.13

# Установка Poetry через pip (надёжнее, чем curl)
RUN python3 -m pip install poetry

# Добавляем poetry в PATH
ENV PATH="/root/.local/bin:${PATH}"

# Отключаем виртуальное окружение
ENV POETRY_VIRTUALENVS_CREATE=false

# Рабочая директория
WORKDIR /app

# Проверка: доступен ли poetry
RUN poetry --version || (echo "Poetry не установлен!" && exit 1)

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock README.md ./

# Устанавливаем зависимости
RUN poetry install --only main --no-root

# Копируем исходный код
COPY . .

# Собираем статику
RUN mkdir -p /app/staticfiles
RUN python manage.py collectstatic --noinput

# Порт
EXPOSE 8000

# Запуск
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]