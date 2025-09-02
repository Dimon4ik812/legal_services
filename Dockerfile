# Базовый образ
FROM python:3.13

# Установка Poetry
RUN curl -sSL https://install.python-poetry.org -o get-poetry.py
RUN python3 get-poetry.py --version
RUN python3 get-poetry.py
RUN ls -la /root/.local/bin/
RUN ls -la ~/.local/bin/poetry || echo "Файл poetry не найден"
RUN which poetry || find / -name poetry 2>/dev/null || echo "poetry нигде не найден"

# Явно добавляем в PATH (на случай, если предыдущий export не сохранился)
ENV PATH="/root/.local/bin:${PATH}"

# Отключаем виртуальное окружение
ENV POETRY_VIRTUALENVS_CREATE=false

# Проверка: где poetry?
RUN which python3 || (echo "python3 not found" && exit 1)
RUN ls -la /root/.local/bin/ || echo "No binaries in bin"
RUN which poetry || (echo "Poetry not found in PATH" && exit 1)

# Рабочая директория
WORKDIR /app

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock README.md ./

# Устанавливаем зависимости
RUN poetry install --only main --no-root

# Копируем код
COPY . .

# Собираем статику
RUN mkdir -p /app/staticfiles
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]