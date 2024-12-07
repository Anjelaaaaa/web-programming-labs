from flask import Blueprint, render_template, request
from datetime import datetime

lab7 = Blueprint('lab7', __name__)


@lab7.route('/lab7/')
def lab():
    return render_template('lab7/lab7.html')


films = [
    {
        "title_ru": "Никто",
        "title": "Nobody",
        "year": 2021,
        "description": "Непримечательный и незаметный семьянин \
            Хатч живёт скучной жизнью обычного аудитора, пока \
            однажды в его дом не вламываются грабители. И это \
            бы сошло им с рук, если бы они не забрали браслетик \
            его маленькой дочки. Не в силах это терпеть, Хатч \
            отправляется на поиски наглецов, а на обратном пути \
            ввязывается в драку с пьяными хулиганами, \
            пристававшими к девушке в общественном транспорте. \
            От души помахав кулаками, наш аудитор отправляет \
            дебоширов в больницу, но оказывается, что один из \
            пострадавших — брат влиятельного русского бандита. \
            И он теперь жаждет мести."
    },
    {
        "title_ru": "Шерлок",
        "title": "Sherlock",
        "year": 2010,
        "description": "События разворачиваются в наши дни. \
            Он прошел Афганистан, остался инвалидом. По \
            возвращении в родные края встречается с загадочным, \
            но своеобразным гениальным человеком. Тот в поиске \
            соседа по квартире. Лондон, 2010 год. Происходят \
            необъяснимые убийства. Скотланд-Ярд без понятия, \
            за что хвататься. Существует лишь один человек, \
            который в силах разрешить проблемы и найти ответы \
            на сложные вопросы."
    },
    {
        "title_ru": "Зеленая книга",
        "title": "Green Book",
        "year": 2018,
        "description": "1960-е годы. После закрытия нью-йоркского \
            ночного клуба на ремонт вышибала Тони по прозвищу Болтун \
            ищет подработку на пару месяцев. Как раз в это время \
            Дон Ширли — утонченный светский лев, богатый и \
            талантливый чернокожий музыкант, исполняющий классическую \
            музыку — собирается в турне по южным штатам, где ещё \
            сильны расистские убеждения и царит сегрегация. Он \
            нанимает Тони в качестве водителя, телохранителя и \
            человека, способного решать текущие проблемы. У этих \
            двоих так мало общего, и эта поездка навсегда изменит \
            жизнь обоих."
    },
    {
        "title_ru": "1+1",
        "title": "Intouchables",
        "year": 2011,
        "description": "Пострадав в результате несчастного случая, \
            богатый аристократ Филипп нанимает в помощники человека, \
            который менее всего подходит для этой работы, – молодого \
            жителя предместья Дрисса, только что освободившегося \
            из тюрьмы. Несмотря на то, что Филипп прикован к \
            инвалидному креслу, Дриссу удается привнести в \
            размеренную жизнь аристократа дух приключений."
    },
    {
        "title_ru": "Благие знамения",
        "title": "Good Omens",
        "year": 2019,
        "description": "Ангел Азирафель и демон Кроули несколько \
            тысяч лет живут среди людей и за это время успели \
            подружиться, хотя это и противоречит строгим правилам \
            небесной и адской канцелярий. Узнав о предстоящем \
            конце света, они решают объединить усилия, чтобы \
            предотвратить апокалипсис, поскольку уже успели \
            привыкнуть к жизни на Земле."
    },
]


@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return films


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if id < 0 or id >= len(films):
        return {"error": "Film not found"}, 404
    return films[id]


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if id < 0 or id >= len(films):
        return {"error": "Film not found"}, 404
    del films[id]
    return '', 204


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if id < 0 or id >= len(films):
        return {"error": "Film not found"}, 404
    film = request.get_json()
    if film['title_ru'] == '':
        return {'title_ru': 'Укажите русское название'}, 400
    if film['year'] == '':
        return {'year': 'Укажите год'}, 400
    current_year = datetime.now().year
    year = int(film['year'])
    if year < 1895 or year > current_year:
        return {'year': f'Год должен быть от 1895 до {current_year}'}, 400
    if film['description'] == '':
        return {'description': 'Заполните описание'}, 400
    if film['title'] == '':
        film['title'] = film['title_ru']
    films[id] = film
    return films[id]


@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json()
    if film['title'] == '' and film['title_ru'] == '':
        return {'title': 'Укажите оригинальное название'}, 400
    if film['title_ru'] == '':
        return {'title_ru': 'Укажите русское название'}, 400
    if film['year'] == '':
        return {'year': 'Укажите год'}, 400
    current_year = datetime.now().year
    year = int(film['year'])
    if year < 1895 or year > current_year:
        return {'year': f'Год должен быть от 1895 до {current_year}'}, 400
    if film['description'] == '':
        return {'description': 'Заполните описание'}, 400
    description = film.get('description', '')
    if len(description) > 2000:
        return {'description': 'Описание превышает 2000 символов'}, 400
    if film['title'] == '':
        film['title'] = film['title_ru']
    films.append(film)
    id = {'id': len(films) - 1}
    return id

