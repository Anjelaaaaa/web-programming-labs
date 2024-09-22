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
        <h3>Такой старницы у нас нет, но есть другие!</h3>
        <div class="b"><img class="b" src="''' + path1 + '''"></div>
    </body>
</html>
''', 404

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

@app.route("/lab1")
def lab1():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <title>Лабораторная 1</title>
    </head>
    <body>
        <main>
            <div>
                Flask &mdash; фреймворк для создания веб-приложений на языке
                программирования Python, использующий набор инструментов
                Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                называемых микрофреймворков &mdash; минималистичных каркасов
                веб-приложений, сознательно предоставляющих лишь самые базовые
                возможности.
            </div>

            <a href="/">Список лабораторных</a>
        </main>
    </body>
</html>
'''

@app.route("/lab1/error400")
def error400():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <body>
        <h1>Bad Request</h1>
    </body>
</html>
''', 400

@app.route("/lab1/error401")
def error401():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <body>
        <h1>Unauthorized</h1>
    </body>
</html>
''', 401

@app.route("/lab1/error402")
def error402():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <body>
        <h1>Payment Required</h1>
    </body>
</html>
''', 402

@app.route("/lab1/error403")
def error403():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <body>
        <h1>Forbidden</h1>
    </body>
</html>
''', 403

@app.route("/lab1/error405")
def error405():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <body>
        <h1>Method Not Allowed</h1>
    </body>
</html>
''', 405

@app.route("/lab1/error418")
def error418():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <body>
        <h1>I'm a teapot</h1>
    </body>
</html>
''', 418

@app.route("/lab1/error500")
def error500():
    number = 500
    return '''
<!DOCTYPE html>
<html lang="ru">
    <body>
        <h1>Ошибка ''' + number + '''</h1>
    </body>
</html>
'''

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

@app.route("/lab1/text")
def text():
    style = url_for("static", filename="text.css")
    path = url_for("static", filename="udav.jpg")
    path1 = url_for("static", filename="udavoutside.jpg")
    path2 = url_for("static", filename="udavinside.jpg")
    return '''
<!doctype html>
<html lang="ru">
<head>
    <title>Маленький принц</title>
    <link rel="stylesheet" href="''' + style + '''">
</head>
    <body>
        <h1>Маленький принц</h1>
        <div>
            Когда мне было шесть лет, в книге под названием «Правдивые
            истории», где рассказывалось про девственные леса, я увидел
            однажды удивительную картинку. На картинке огромная змея —
            удав — глотала хищного зверя. Вот как это было нарисовано:
        </div>
        <img class="a" src="''' + path + '''">
        <div>
            В книге говорилось: «Удав заглатывает свою жертву целиком,
            не жуя. После этого он уже не может шевельнуться и спит
            полгода подряд, пока не переварит пищу».
        </div>
        <div>
            Я много раздумывал о полной приключений жизни джунглей и
            тоже нарисовал цветным карандашом свою первую картинку. Это
            был мой рисунок №1. Вот что я нарисовал:
        </div>
        <img class="b" src="''' + path1 + '''">
        <div>
            Я показал мое творение взрослым и спросил, не страшно ли им.
        </div>
        <div>
            — Разве шляпа страшная? — возразили мне.
        </div>
        <div>
            А это была совсем не шляпа. Это был удав, который проглотил
            слона. Тогда я нарисовал удава изнутри, чтобы взрослым было
            понятнее. Им ведь всегда нужно все объяснять. Это мой
            рисунок №2:
        </div>
        <img class="c" src="''' + path2 + '''">
        <div>
            Взрослые посоветовали мне не рисовать змей ни снаружи, ни
            изнутри, а побольше интересоваться географией, историей,
            арифметикой и правописанием. Вот как случилось, что шести
            лет я отказался от блестящей карьеры художника. Потерпев
            неудачу с рисунками №1 и №2, я утратил веру в себя.
            Взрослые никогда ничего не понимают сами, а для детей очень
            утомительно без конца им все объяснять и растолковывать.
        </div>
        <div>
            Итак, мне пришлось выбирать другую профессию, и я выучился
            на летчика. Облетел я чуть ли не весь свет. И география,
            по правде сказать, мне очень пригодилась. Я умел с первого
            взгляда отличить Китай от Аризоны. Это очень полезно, если
            ночью собьешься с пути.
        </div>
        <div>
            На своем веку я много встречал разных серьезных людей. Я
            долго жил среди взрослых. Я видел их совсем близко. И от
            этого, признаться, не стал думать о них лучше.
        </div>
        <div>
            Когда я встречал взрослого, который казался мне разумней
            и понятливей других, я показывал ему свой рисунок №1 — я
            его сохранил и всегда носил с собою. Я хотел знать, вправду
            ли этот человек что-то понимает. Но все они отвечали мне:
            «Это шляпа». И я уже не говорил с ними ни об удавах, ни о
            джунглях, ни о звездах. Я применялся к их понятиям. Я говорил
            с ними об игре в бридж и гольф, о политике и о галстуках.
            И взрослые были очень довольны, что познакомились с таким
            здравомыслящим человеком.
        </div>
    </body>
</html>
''', {
    "Content-Language": "ru",
    "Target-Audience": "children",
    "Author": "Antoine de Saint-Exupery"
}
