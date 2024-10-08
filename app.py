from flask import Flask, url_for, redirect, render_template
app = Flask(__name__)

@app.route("/lab1/web")
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

@app.route("/lab1/author")
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

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

resource = False

@app.route("/lab1/created")
def created():
    path = url_for("static", filename="jenga.webp")
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

@app.route("/lab1/delete")
def delete():
    path = url_for("static", filename="jengabroke.jpg")
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

@app.route("/lab1/resource")
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

@app.route("/lab1/status")
def update_status():
    return redirect("/lab1/resource")

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

@app.route("/lab1/counter_clean")
def counter_clean():
    global count
    count = 0
    return redirect("/lab1/counter")

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
                </ol>
            </div>
        </main>

        <footer>
            &copy; Оноприенко Анжелика Андреевна, ФБИ-21, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1")
def lab1():
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
            <div>
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

@app.route("/lab1/error400")
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

@app.route("/lab1/error401")
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

@app.route("/lab1/error402")
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

@app.route("/lab1/error403")
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

@app.route("/lab1/error405")
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

@app.route("/lab1/error418")
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

@app.route("/lab2/a")
def a():
    return 'без слэша'

@app.route("/lab2/a/")
def a2():
    return 'со слэшем'

flower_list = [
    {'name': 'роза', 'price': 150},
    {'name': 'тюльпан', 'price': 160},
    {'name': 'незабудка', 'price': 200},
    {'name': 'ромашка', 'price': 100},
]

@app.route("/lab2/flowers/<int:flower_id>")
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return render_template('flower_id404.html'), 404
    else:
        return render_template('flower_id.html', flower_id=flower_id, flower_list=flower_list)

@app.route("/lab2/add_flower/<name>/<int:price>")
def add_flower(name, price):
    flower_list.append({'name': name, 'price': price})
    return render_template('add_flower.html', name=name, price=price, flower_list=flower_list)

@app.route("/lab2/add_flower/<name>")
def add_flower_noprice(name):
    return render_template('add_flower_noprice.html'), 400

@app.route("/lab2/add_flower/")
def flower():
    return render_template('add_flower400.html'), 400

@app.route("/lab2/all_flowers/")
def all_flowers():
    return render_template('all_flowers.html', flower_list=flower_list)

@app.route("/lab2/clean_flowers/")
def clean_flowers():
    global flower_list
    flower_list = []
    return render_template('clean_flowers.html')

@app.route("/lab2/delete_flower/<int:flower_id>")
def delete_flower_id(flower_id):
    if flower_id >= len(flower_list):
        return render_template('delete_flower_id404.html'), 404
    else:
        del flower_list[flower_id]
        return redirect("/lab2/all_flowers/")

@app.route("/lab2/delete_flower/")
def delete_flower():
    return render_template('delete_flower.html')

@app.route("/lab2/example")
def example():
    name = 'Анжелика Оноприенко'
    number = '2'
    group = 'ФБИ-21'
    course = '3 курс'
    fruits = [
        {'name':'яблоки', 'price': 100},
        {'name':'груши', 'price': 120},
        {'name':'апельсины', 'price': 80},
        {'name':'мандарины', 'price': 95},
        {'name':'манго', 'price': 321}
    ]
    return render_template('example.html', number=number, name=name, group=group, course=course, fruits=fruits)

@app.route("/lab2/")
def lab2():
    return render_template('lab2.html')

@app.route("/lab2/filters")
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase=phrase)

@app.route("/lab2/calc/<int:a>/<int:b>")
def calc(a,b):
    return render_template('calc.html', a=a, b=b)

@app.route("/lab2/calc/")
def calc1():
    return redirect("/lab2/calc/1/1")

@app.route("/lab2/calc/<int:a>")
def calc2(a):
    return redirect(f"/lab2/calc/{a}/1")

@app.route("/lab2/books")
def books():
    books = [
        {'author':'Лев Николаевич Толстой', 'title':'"Война и мир"' , 'genre':'роман', 'pages':1225},
        {'author':'Антуан де Сент-Экзюпери', 'title':'"Маленький принц"', 'genre':'философская сказка', 'pages':128},
        {'author':'Фёдор Михайлович Достоевский', 'title':'"Преступление и наказание"', 'genre':'роман', 'pages':656},
        {'author':'Александр Сергеевич Пушкин', 'title':'"Евгений Онегин"', 'genre':'роман в стихах', 'pages':384},
        {'author':'Михаил Афанасьевич Булгаков', 'title':'"Мастер и Маргарита"', 'genre':'роман', 'pages':496},
        {'author':'Иван Сергеевич Тургенев', 'title':'"Отцы и дети"', 'genre':'роман', 'pages':384},
        {'author':'Антон Павловиччехо Чехов', 'title':'"Вишнёвый сад"', 'genre':'пьеса', 'pages':128},
        {'author':'Михаил Юоьевич Лермонтов', 'title':'"Герой нашего времени"', 'genre':'роман', 'pages':320},
        {'author':'Рэй Брэдбери', 'title':'"Улыбка"', 'genre':'фантастика', 'pages':100},
        {'author':'Чарльз Диккенс', 'title':'"Приключения Оливера Твиста"', 'genre':'роман', 'pages':544}
    ]
    return render_template('books.html', books=books)

@app.route("/lab2/butterfly")
def butterfly():
    butterfly = [
    {
        'name': 'Морфо Пелеида',
        'image': '1butterfly.png',
        'description': 'Бабочка Морфо Пелеида является одним из самых удивительных и красивых существ в живой природе. Известная своей яркой и голубой окраской крыльев, эта бабочка не может не привлечь внимание.'
    },
    {
        'name': 'Парусник Маака',
        'image': '2butterfly.png',
        'description': 'Размах крыльев этой бабочки достигает 14 см. Самцы имеют очень красивую, яркую окраску - верхняя часть крыльев отливает зеленоватым, бирюзовым и голубоватым цветами.'
    },
    {
        'name': 'Золотая птицекрылка',
        'image': '3butterfly.png',
        'description': 'Это одна из самых крупных дневных бабочек, размах крыльев которой достигает 16 см. Передние крылья удлинённые, бархатисто-чёрные со светлыми жилками. Задние крылья ярко-жёлтые с широкой чёрной окантовкой.'
    },
    {
        'name': 'Парусник Палинур',
        'image': '4butterfly.png',
        'description': 'Очаровательная переливающаяся тропическая бабочка, которую иногда называют бабочкой-павлином. Меняют свой цвет от изумрудно-зелёного до бирюзово-голубого.'
    },
    {
        'name': 'Препона Демофон',
        'image': '5butterfly.png',
        'description': 'Уникальность этой крылатки в ее черных крыльях с синими и голубыми вкраплениями на них. Полет Препона ровный, крылья при этом немного потрескивают.'
    },
    {
        'name': 'Парусник Румянцева',
        'image': '6butterfly.png',
        'description': 'Сверху крылья самцов имеют на черном фоне серое-серебристую пыльцу, а нижние отличаются синевато-серой пыльцой. С обратной стороны присутствуют крупные красновато-розовые отметины.'
    },
    {
        'name': 'Парусник Аскалаф',
        'image': '7butterfly.png',
        'description': 'Размах крыльев 140—160 мм. Доминирующая окраска крыльев чёрная. На наружный поверхности вдоль жилок серебристо-серое напыление. На задних крыльях располагается по одному хвостику длиной 3—7 мм.'
    }
]
    return render_template('butterfly.html', butterfly=butterfly)
