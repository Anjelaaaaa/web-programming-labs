from flask import Flask, url_for
import os
from os import path
from flask_sqlalchemy import SQLAlchemy
from db import db
from db.models import users
from flask_login import LoginManager

from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9
from rgz import rgz

app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_users(login_id):
    return users.query.get(int(login_id))

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'super_secret_key')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'onoprienko_anjelika_orm'
    db_user = 'onoprienko_anjelika_orm'
    db_password = '176'
    host_ip = '127.0.0.1'
    host_port = 5432
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "onoprienko_anjelika_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)
app.register_blueprint(rgz)


@app.route("/")
@app.route("/index")
def index():
    style = url_for("static", filename="main.css")
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + style + '''">
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <main>
            <div class="spisok">
                <ol>
                    <li>
                        <a href="/lab1">Первая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab2">Вторая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab3/">Третья лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab4/">Четвертая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab5/">Пятая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab6/">Шестая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab7/">Седьмая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab8/">Восьмая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab9/">Девятая лабораторная</a>
                    </li>
                    <li>
                        <a href="/rgz/">Расчетно-графическое задание</a>
                    </li>
                </ol>
            </div>
        </main>

        <footer>
            &copy; Оноприенко Анжелика Андреевна, ФБИ-21, 3 курс, 2024
        </footer>
    </body>
</html>
'''


@app.errorhandler(404)
def not_found(err):
    style = url_for("static", filename="error404.css")
    path = url_for("static", filename="sad.webp")
    path1 = url_for("static", filename="bingo.webp")
    path2 = url_for("static", filename="disgust.jpg")
    return '''
<!doctype html>
<html>
    <head>
        <title>Not Found</title>
        <link rel="stylesheet" href="''' + style + '''">
    </head>
    <body>
        <img class="c" src="''' + path2 + '''">
        <h1><span class="e">4</span><span class="d">0</span>4</h1>
        <h2>Ошибка</h2>
        <div class="a"><img class="a" src="''' + path + '''"></div>
        <h3>Такой страницы у нас нет, но есть другие!</h3>
        <div class="b"><img class="b" src="''' + path1 + '''"></div>
    </body>
</html>
''', 404


@app.errorhandler(500)
def internal_server_error(err):
    style = url_for("static", filename="error500.css")
    path = url_for("static", filename="simka.png")
    path1 = url_for("static", filename="nolik.png")
    path2 = url_for("static", filename="masya.png")
    return '''
<!doctype html>
<html>
<head>
    <title>Internal Server Error</title>
    <link rel="stylesheet" href="''' + style + '''">
</head>
    <body>
        <img class="a" src="''' + path + '''">
        <img class="b" src="''' + path1 + '''">
        <img class="c" src="''' + path2 + '''">
        <h1><span class="e">5</span><span class="d">0</span>0</h1>
        <h2>Ошибка</h2>
        <h3>
            На нашем сервере произошла небольшая ошибка, вскоре она будет
            исправлена, мы уже работаем над ней!
        </h3>
    </body>
</html>
''', 500

