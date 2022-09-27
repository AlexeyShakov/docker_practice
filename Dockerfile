#FROM python:3.10
## Задаем рабочую директорию(app) внутри контейнера
#WORKDIR /usr/src/app
## Запрещаем Python писать файлы .pyc на диск
#ENV PYTHONDONTWRITEBYTECODE 1
## Запрещает Python буферизовать stdout и stderr
#ENV PYTHONUNBUFFERED 1
#RUN pip install --upgrade pip
## Копируем файл из рабочей директории на диске в рабочую директорию(/usr/src/app) контейнера
#COPY requirements.txt .
#RUN pip install -r requirements.txt
## Копирует все файлы из рабочей директории на диске в рабочую директорию контейнера
#COPY . .
#CMD ["python", "manage.py", "runserver"]

FROM python:3.10
# Задаем рабочую директорию(app) внутри контейнера
WORKDIR /usr/src/app
# Запрещаем Python писать файлы .pyc на диск
ENV PYTHONDONTWRITEBYTECODE 1
# Запрещает Python буферизовать stdout и stderr
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
# Копируем файл из рабочей директории на диске в рабочую директорию(/usr/src/app) контейнера
COPY requirements.txt .
RUN pip install -r requirements.txt
# Копирует все файлы из рабочей директории на диске в рабочую директорию контейнера
COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"
#CMD ["python", "manage.py", "runserver"]

