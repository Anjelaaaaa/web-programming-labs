from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.route("/lab1/web")
def web():
    return """<!doctype html>
        <html>
           <body>
               <h1>web-сервер на flask</h1>
               <a href="lab1/author">author</a>
           </body>
        </html>""", 200, {
            "X-Server": "sample",
            "Content-Type": "text/plane; charset=utf-8"
        }

@app.route("/lab1/author")
def author():
    name = "Оноприенко Анжелика Андреевна"
    group = "ФБИ-21"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
           <body>
               <p>Студент: """ + name + """</p>
               <p>Группа: """ + group + """</p>
               <p>Факультет: """ + faculty + """</p>
               <a href="/lab1/web">web</a>
           </body>
        </html>"""

@app.route("/lab1/oak")
def oak():
    path = url_for("static", filename="oak.jpg")
    style = url_for("static", filename="lab1.css")
    return '''
<!doctype html>
<html>
<head>
    <title>Дуб</title>
    <link rel="stylesheet" href="''' + style + '''">
</head>
    <body>
        <h1>Дуб</h1>
        <div><img src="''' + path + '''"></div>
    </body>
</html>'''

count = 0

@app.route("/lab1/counter")
def counter():
    global count
    count +=1
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили: ''' + str(count) + '''<br>
        <a href="/lab1/counter_clean">Очистить счетчик</a>
    </body>
</html>'''

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
    </body>
</html>
''', 201

@app.errorhandler(404)
def not_found(err):
    return "нет такой страницы", 404

@app.route("/lab1/counter_clean")
def counter_clean():
    global count
    count = 0
    return redirect("/lab1/counter")

@app.route("/")
@app.route("/index")
def index():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <main>
            <ol>
                <li>
                    <a href="/lab1">Первая лабораторная</a>
                </li>
            </ol>
        </main>

        <footer>
            &copy;Оноприенко Анжелика Андреевна, ФБИ-21, 2 курс, 2024
        </footer>
    </body>
</html>
'''
