# установка базового образа (host OS)
FROM python:3.9
# установка рабочей директории в контейнере
WORKDIR /code
# копирование файла зависимостей в рабочую директорию
COPY requirements.txt /code
# установка зависимостей
RUN pip install -r requirements.txt
# копирование содержимого локальной директории src в рабочую директорию
COPY db/ /code
COPY handlers/ /code
COPY keyboards/ /code
COPY log/ /code
COPY src/ .
COPY states/ .
COPY .env .
COPY app.py .
COPY loader.py .

EXPOSE 8002

# команда, выполняемая при запуске контейнера
CMD [ "python", "./app.py" ]

