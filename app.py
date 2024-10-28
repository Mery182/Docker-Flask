import time
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Конфигурация для подключения к базе данных PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/counterdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Модель для хранения данных о запросах
class Counter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String, nullable=False)
    client_info = db.Column(db.String, nullable=False)

# Создаем таблицу, если её нет
with app.app_context():
    db.create_all()

@app.route('/')
def hello():
    # Добавление записи о запросе в базу данных
    new_entry = Counter(
        datetime=datetime.now().strftime("%d/%b/%Y %H:%M:%S"),
        client_info=request.headers.get('User-Agent')
    )
    db.session.add(new_entry)
    db.session.commit()

    count = Counter.query.count()  # Получаем текущее количество записей
    return 'Hello World! I have been seen {} times.\n'.format(count)

