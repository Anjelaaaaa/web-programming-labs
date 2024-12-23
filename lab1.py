from flask import Blueprint, url_for, redirect
lab1 = Blueprint('lab1', __name__)


@lab1.route("/lab1/web")
def web():
    return '''<!doctype html>
        <html>
           <body>
               <h1>web-сервер на flask</h1>
               <a href="lab1/author">author</a>
           </body>
        </html>''', 200, {
            "X-Server": "sample",
            "Content-Type": "text/plane; charset=utf-8"
        }


@lab1.route("/lab1/author")
def author():
    style = url_for("static", filename="main.css")
    name = "Оноприенко Анжелика Андреевна"
    group = "ФБИ-21"
    faculty = "ФБ"
    return '''<!doctype html>
        <html>
            <head>
                <title>Автор</title>
                <link rel="stylesheet" href="''' + style + '''">
            </head>
            <body>
                <div class="menu">
                    <p>Студент: ''' + name + '''</p>
                    <p>Группа: ''' + group + '''</p>
                    <p>Факультет: ''' + faculty + '''</p>
                    <a href="/lab1/web">web</a>
                </div>
            </body>
        </html>'''


@lab1.route("/lab1/oak")
def oak():
    path = url_for("static", filename="lab1/oak.jpg")
    style = url_for("static", filename="lab1/lab1.css")
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

@lab1.route("/lab1/counter")
def counter():
    style = url_for("static", filename="main.css")
    global count
    count +=1
    return '''
<!doctype html>
<html>
    <head>
        <title>Счетчик</title>
        <link rel="stylesheet" href="''' + style + '''">
    </head>
    <body>
        <div class="counter">
            Сколько раз вы сюда заходили: ''' + str(count) + '''<br>
            <a href="/lab1/counter_clean">Очистить счетчик</a>
        </div>
    </body>
</html>'''


@lab1.route("/lab1/info")
def info():
    return redirect("/lab1/author")


resource = False

@lab1.route("/lab1/created")
def created():
    path = url_for("static", filename="lab1/jenga.webp")
    style = url_for("static", filename="main.css")
    global resource
    if resource:
        return '''
<!doctype html>
<html>
    <head>
        <title>Постройка башни</title>
        <link rel="stylesheet" href="''' + style + '''">
    </head>
    <body>
        <h1 class="resource">Отказано: башня уже построена</h1>
        <div class="center"><img class="tower" src="''' + path + '''"></div>
    </body>
</html>
''', 400
    else:
        resource = True
        return '''
<!doctype html>
<html>
    <head>
        <title>Постройка башни</title>
        <link rel="stylesheet" href="''' + style + '''">
    </head>
    <body>
        <h1 class="resource">Успешно: башня построена</h1>
        <div class="center"><img class="tower" src="''' + path + '''"></div>
    </body>
</html>
''', 201


@lab1.route("/lab1/delete")
def delete():
    path = url_for("static", filename="lab1/jengabroke.jpg")
    style = url_for("static", filename="main.css")
    global resource
    if resource:
        resource = False
        return '''
<!doctype html>
<html>
    <head>
        <title>Разрушение башни</title>
        <link rel="stylesheet" href="''' + style + '''">
    </head>
    <body>
        <h1 class="resource">Успешно: башня разрушена</h1>
        <div class="center"><img class="tower" src="''' + path + '''"></div>
    </body>
    </body>
</html>
''', 200
    else:
        return '''
<!doctype html>
<html>
    <head>
        <title>Разрушение башни</title>
        <link rel="stylesheet" href="''' + style + '''">
    </head>
    <body>
        <h1 class="resource">Отказано: башня еще не построена</h1>
    </body>
    </body>
</html>
''', 400


@lab1.route("/lab1/resource")
def resource_status():
    style = url_for("static", filename="main.css")
    if resource:
        status = "Башня построена"
    else:
        status = "Башня еще не построена"
    return '''
<!doctype html>
<html>
    <head>
        <title>Статус постройки</title>
        <link rel="stylesheet" href="''' + style + '''">
    </head>
    <body>
        <h1 class="resource">''' + status + '''</h1>
        <div class="resource">
            <a href="/lab1/status">Обновить статус</a><br>
        </div>
        <div class="resource">
            <a href="/lab1/created">Построить башню</a><br>
        </div>
        <div class="resource">
            <a href="/lab1/delete">Разрушить башню</a>
        </div>
    </body>
</html>
'''


@lab1.route("/lab1/status")
def update_status():
    return redirect("/lab1/resource")


@lab1.route("/lab1/counter_clean")
def counter_clean():
    global count
    count = 0
    return redirect("/lab1/counter")


@lab1.route("/lab1")
def lab():
    style = url_for("static", filename="main.css")
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + style + '''">
        <title>Лабораторная 1</title>
    </head>
    <body>
        <main>
            <div class='flask'>
                <h2 class="header1">Flask</h2> &mdash; фреймворк для создания веб-приложений на языке
                программирования Python, использующий набор инструментов
                Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                называемых микрофреймворков &mdash; минималистичных каркасов
                веб-приложений, сознательно предоставляющих лишь самые базовые
                возможности.
            </div>

            <div class="list lab1">
                <a href="/">Список лабораторных</a>
            </div>

            <div class="list lab1">
                <h2 class="header1">Список роутов</h2>

                <ul>
                    <li>
                        <a href="/lab1/web">Веб</a>
                    </li>
                    <li>
                        <a href="/lab1/author">Автор</a>
                    </li>
                    <li>
                        <a href="/lab1/oak">Дуб</a>
                    </li>
                    <li>
                        <a href="/lab1/counter">Счетчик</a>
                    </li>
                    <li>
                        <a href="/lab1/info">Информация</a>
                    </li>
                    <li>
                        <a href="/lab1/created">Постройка башни</a>
                    </li>
                    <li>
                        <a href="/lab1/error404">Ошибка 404</a>
                    </li>
                    <li>
                        <a href="/lab1/counter_clean">Очистка счетчика</a>
                    </li>
                    <li>
                        <a href="/lab1/error400">Ошибка 400</a>
                    </li>
                    <li>
                        <a href="/lab1/error401">Ошибка 401</a>
                    </li>
                    <li>
                        <a href="/lab1/error402">Ошибка 402</a>
                    </li>
                    <li>
                        <a href="/lab1/error403">Ошибка 403</a>
                    </li>
                    <li>
                        <a href="/lab1/error405">Ошибка 405</a>
                    </li>
                    <li>
                        <a href="/lab1/error418">Ошибка 418</a>
                    </li>
                    <li>
                        <a href="/lab1/error500">Ошибка 500</a>
                    </li>
                    <li>
                        <a href="/lab1/text">Текст</a>
                    </li>
                    <li>
                        <a href="/lab1/delete">Разрушение башни</a>
                    </li>
                    <li>
                        <a href="/lab1/resource">Статус постройки</a>
                    </li>
                    <li>
                        <a href="/lab1/status">Обновление статуса постройки</a>
                    </li>
                </ul>
            </div>
        </main>
    </body>
</html>
'''


@lab1.route("/lab1/error400")
def error400():
    style = url_for("static", filename="main.css")
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + style + '''">
        <title>Bad Request</title>
    </head>
    <body>
        <h1 class="error400">Bad Request</h1>
    </body>
</html>
''', 400


@lab1.route("/lab1/error401")
def error401():
    style = url_for("static", filename="main.css")
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + style + '''">
        <title>Unauthorized</title>
    </head>
    <body>
        <h1 class="error401">Unauthorized</h1>
    </body>
</html>
''', 401


@lab1.route("/lab1/error402")
def error402():
    style = url_for("static", filename="main.css")
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + style + '''">
        <title>Payment Required</title>
    </head>
    <body>
        <h1 class="error402">Payment Required</h1>
    </body>
</html>
''', 402


@lab1.route("/lab1/error403")
def error403():
    style = url_for("static", filename="main.css")
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + style + '''">
        <title>Forbidden</title>
    </head>
    <body>
        <h1 class="error403">Forbidden</h1>
    </body>
</html>
''', 403


@lab1.route("/lab1/error405")
def error405():
    style = url_for("static", filename="main.css")
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + style + '''">
        <title>Method Not Allowed</title>
    </head>
    <body>
        <h1 class="error405">Method Not Allowed</h1>
    </body>
</html>
''', 405


@lab1.route("/lab1/error418")
def error418():
    style = url_for("static", filename="main.css")
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + style + '''">
        <title>I'm a teapot</title>
    </head>
    <body>
        <h1 class="error418">I'm a teapot</h1>
    </body>
</html>
''', 418


@lab1.route("/lab1/error500")
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


@lab1.route("/lab1/text")
def text():
    style = url_for("static", filename="lab1/text.css")
    path = url_for("static", filename="lab1/udav.jpg")
    path1 = url_for("static", filename="lab1/udavoutside.jpg")
    path2 = url_for("static", filename="lab1/udavinside.jpg")
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

