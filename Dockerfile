# установка базового образа (host OS)
FROM python:3.9
# установка рабочей директории в контейнере
WORKDIR /code
# копирование файла зависимостей в рабочую директорию
COPY /requirements.txt code/requirements.txt
# установка зависимостей
RUN pip3 install -r code/requirements.txt
# копирование содержимого локальнх директорий в рабочую директорию
COPY /db/ /code/db/
COPY /handlers/ /code/handlers/
COPY /keyboards/ /code/keyboards/
COPY /log /code/log/
COPY /src/ /code/src/
COPY /states /code/states/
COPY /.env /code/.env
COPY /app.py /code/app.py
COPY /loader.py /code/loader.py

EXPOSE 8002

# команда, выполняемая при запуске контейнера
CMD [ "python", "app.py" ]

