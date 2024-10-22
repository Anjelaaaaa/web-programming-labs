from flask import Blueprint, render_template, request, make_response, redirect
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    age = request.cookies.get('age')
    if name is None:
        name = "Незвестный"
    if age is None:
        age = "Неизвестен"
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'rgb(137, 120, 211)')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name')
    resp.set_cookie('age')
    resp.set_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    age = request.args.get('age')
    sex = request.args.get('sex')
    if user == '':
        errors['user'] = '*'
        errors['textuser'] = '*Заполните поле ввода имени!'
    elif age == '':
        errors['age'] = '*'
        errors['textage'] = '*Заполните поле ввода возраста!'
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')


@lab3.route('/lab3/pay')
def pay():
    global price
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80 
    else:
        price = 70 
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10  
    return render_template('lab3/pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    return render_template('lab3/success.html')


@lab3.route('/lab3/settings') 
def settings():
    color = request.args.get('color') 
    backgroundcolor = request.args.get('backgroundcolor')
    fontsize = request.args.get('fontsize')
    headerfooter = request.args.get('headerfooter')

    if color or backgroundcolor or fontsize or headerfooter: 
        resp = make_response(redirect('/lab3/settings')) 
        resp.set_cookie('color', color) 
        resp.set_cookie('backgroundcolor', backgroundcolor)
        resp.set_cookie('fontsize', fontsize)
        resp.set_cookie('headerfooter', headerfooter)  
        return resp 
 
    color = request.cookies.get('color') 
    backgroundcolor = request.cookies.get('backgroundcolor')
    fontsize = request.cookies.get('fontsize')
    headerfooter = request.cookies.get('headerfooter')   
    resp = make_response(render_template('lab3/settings.html', color=color, backgroundcolor=backgroundcolor, fontsize=fontsize, headerfooter=headerfooter)) 
    return resp

@lab3.route('/lab3/del_settings')
def del_settings():
    resp = make_response(redirect('/lab3/settings'))
    resp.set_cookie('color') 
    resp.set_cookie('backgroundcolor')
    resp.set_cookie('fontsize')
    resp.set_cookie('headerfooter')
    return resp

@lab3.route('/lab3/ticket')
def ticket():
    ticket = 0
    FIO = request.args.get('FIO')
    age = request.args.get('age', 0)
    shelf = request.args.get('shelf')
    linen = request.args.get('linen')
    baggage = request.args.get('baggage')
    place1 = request.args.get('place1')
    place2 = request.args.get('place2')
    date = request.args.get('date')
    belay = request.args.get('belay')
    if int(age) < 18:
        ticket += 700
        ticket_type = "Детский билет"
    else:
        ticket += 1000
        ticket_type = "Взрослый билет"
    if shelf == 'lower' or shelf == 'lower-side':
        ticket += 100
    if linen == 'withlinen':
        ticket += 75
    if baggage == 'withbaggage':
        ticket += 250
    if belay == 'withbelay':
        ticket += 150
    return render_template('lab3/ticket.html', FIO=FIO, age=age, ticket=ticket, shelf=shelf, linen=linen, baggage=baggage, belay=belay, ticket_type=ticket_type, place1=place1, place2=place2, date=date)


games = [
    {'name': 'Cyberpunk 2077', 'price': 2999, 'genre': 'RPG', 'weight': 57},
    {'name': 'The Witcher 3: Wild Hunt', 'price': 599, 'genre': 'RPG', 'weight': 32},
    {'name': 'Grand Theft Auto V', 'price': 2199, 'genre': 'Action', 'weight': 85},
    {'name': 'Red Dead Redemption 2', 'price': 2493, 'genre': 'Action', 'weight': 150},
    {'name': 'Elden Ring', 'price': 3899, 'genre': 'RPG', 'weight': 47},
    {'name': 'God of War', 'price': 1968, 'genre': 'Action', 'weight': 118},
    {'name': 'Horizon Zero Dawn', 'price': 1999, 'genre': 'Action', 'weight': 67},
    {'name': 'Ghost of Tsushima', 'price': 1549, 'genre': 'Action', 'weight': 46},
    {'name': 'Marvels Spider-Man', 'price': 2550, 'genre': 'Action', 'weight': 54},
    {'name': 'Death Stranding', 'price': 1299, 'genre': 'Action', 'weight': 35},
    {'name': 'The Last of Us Part II', 'price': 3499, 'genre': 'Action', 'weight': 82},
    {'name': 'Uncharted 4: A Thiefs End', 'price': 2200, 'genre': 'Action', 'weight': 32},
    {'name': 'Resident Evil Village', 'price': 4353, 'genre': 'Horror', 'weight': 91},
    {'name': 'Doom Eternal', 'price': 999, 'genre': 'Shooter', 'weight': 28},
    {'name': 'Hades', 'price': 799, 'genre': 'Roguelike', 'weight': 23},
    {'name': 'Stardew Valley', 'price': 650, 'genre': 'Simulation', 'weight': 19},
    {'name': 'Terraria', 'price': 575, 'genre': 'Sandbox', 'weight': 15},
    {'name': 'Minecraft', 'price': 500, 'genre': 'Sandbox', 'weight': 24},
    {'name': 'Among Us', 'price': 499, 'genre': 'Multiplayer', 'weight': 10},
    {'name': 'Rocket League', 'price': 876, 'genre': 'Sports', 'weight': 16}
]

@lab3.route('/lab3/games')
def games_search():
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')

    if min_price is None or max_price is None:
        return render_template('lab3/games.html', filtered_games=games, min_price=min_price, max_price=max_price)
    
    min_price = int(min_price)
    max_price = int(max_price)

    if max_price < min_price:
        return render_template('lab3/games.html', error="Максимальная цена не может быть меньше минимальной", min_price=min_price, max_price=max_price)
    
    filtered_games = [game for game in games if min_price <= game['price'] <= max_price]

    return render_template('lab3/games.html', filtered_games=filtered_games, min_price=min_price, max_price=max_price)

