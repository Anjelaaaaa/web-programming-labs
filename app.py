from flask import Flask, url_for, redirect, render_template
from lab1 import lab1
app = Flask(__name__)
app.register_blueprint(lab1)

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
