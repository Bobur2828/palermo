FROM python:3.12-alpine

WORKDIR /app

RUN apk add --no-cache \
    build-base \
    postgresql-dev \
    musl-dev \
    gcc \
    python3-dev \
    libffi-dev \
    jpeg-dev \
    zlib-dev


COPY requirements.txt .


RUN pip install -r requirements.txt


COPY . .

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
