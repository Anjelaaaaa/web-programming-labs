from flask import Blueprint, render_template, request, make_response, redirect
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    age = request.cookies.get('age')
    if name is None:
        name = "Незвестный"
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
    return render_template('lab3/success.html', price=price)


@lab3.route('/lab3/settings', methods=['GET', 'POST']) 
def settings():
    if request.method == 'POST':  
        color = request.form.get('color') 
        backgroundcolor = request.form.get('backgroundcolor')
        fontsize = request.form.get('fontsize')
        headerfooter = request.form.get('headerfooter')  
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


# @lab3.route('/lab3/train')
# def success():
#     return render_template('lab3/train.html')

