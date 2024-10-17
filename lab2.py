from flask import Blueprint, url_for, redirect, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route("/lab2/a")
def a():
    return 'без слэша'


@lab2.route("/lab2/a/")
def a2():
    return 'со слэшем'


flower_list = [
    {'name': 'роза', 'price': 150},
    {'name': 'тюльпан', 'price': 160},
    {'name': 'незабудка', 'price': 200},
    {'name': 'ромашка', 'price': 100},
]

@lab2.route("/lab2/flowers/<int:flower_id>")
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return render_template('flower_id404.html'), 404
    else:
        return render_template('flower_id.html', flower_id=flower_id, flower_list=flower_list)


@lab2.route("/lab2/add_flower/<name>/<int:price>")
def add_flower(name, price):
    flower_list.lab2end({'name': name, 'price': price})
    return render_template('add_flower.html', name=name, price=price, flower_list=flower_list)


@lab2.route("/lab2/add_flower/<name>")
def add_flower_noprice(name):
    return render_template('add_flower_noprice.html'), 400


@lab2.route("/lab2/add_flower/")
def flower():
    return render_template('add_flower400.html'), 400


@lab2.route("/lab2/all_flowers/")
def all_flowers():
    return render_template('all_flowers.html', flower_list=flower_list)


@lab2.route("/lab2/clean_flowers/")
def clean_flowers():
    global flower_list
    flower_list = []
    return render_template('clean_flowers.html')


@lab2.route("/lab2/delete_flower/<int:flower_id>")
def delete_flower_id(flower_id):
    if flower_id >= len(flower_list):
        return render_template('delete_flower_id404.html'), 404
    else:
        del flower_list[flower_id]
        return redirect("/lab2/all_flowers/")


@lab2.route("/lab2/delete_flower/")
def delete_flower():
    return render_template('delete_flower.html')


@lab2.route("/lab2/example")
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


@lab2.route("/lab2/")
def lab():
    return render_template('lab2.html')


@lab2.route("/lab2/filters")
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase=phrase)


@lab2.route("/lab2/calc/<int:a>/<int:b>")
def calc(a,b):
    return render_template('calc.html', a=a, b=b)


@lab2.route("/lab2/calc/")
def calc1():
    return redirect("/lab2/calc/1/1")


@lab2.route("/lab2/calc/<int:a>")
def calc2(a):
    return redirect(f"/lab2/calc/{a}/1")


@lab2.route("/lab2/books")
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


@lab2.route("/lab2/butterfly")
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

