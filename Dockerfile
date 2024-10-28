FROM python:3.9-slim

WORKDIR /code

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Устанавливаем необходимые пакеты для работы с PostgreSQL
RUN apt-get update && apt-get install -y gcc libpq-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000
COPY . .
CMD ["flask", "run"]
