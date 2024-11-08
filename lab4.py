from flask import Blueprint, render_template, request, redirect, session
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')


@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')


@lab4.route('/lab4/div', methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Все поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/div.html', error0='На ноль делить нельзя!')
    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/multiplication-form')
def multiplication_form():
    return render_template('lab4/multiplication-form.html')


@lab4.route('/lab4/multiplication', methods = ['POST'])
def multiplication():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '':
        x1 = 1
    else:
        x1 = int(x1)
    if x2 == '':
        x2 = 1
    else:
        x2 = int(x2)
    result = x1 * x2
    return render_template('lab4/multiplication.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/addition-form')
def addition_form():
    return render_template('lab4/addition-form.html')


@lab4.route('/lab4/addition', methods = ['POST'])
def addition():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '':
        x1 = 0
    else:
        x1 = int(x1)
    if x2 == '':
        x2 = 0
    else:
        x2 = int(x2)
    result = x1 + x2
    return render_template('lab4/addition.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/subtraction-form')
def subtraction_form():
    return render_template('lab4/subtraction-form.html')


@lab4.route('/lab4/subtraction', methods = ['POST'])
def subtraction():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/subtraction.html', error='Все поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    result = x1 - x2
    return render_template('lab4/subtraction.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/exponentiation-form')
def exponentiation_form():
    return render_template('lab4/exponentiation-form.html')


@lab4.route('/lab4/exponentiation', methods = ['POST'])
def exponentiation():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/exponentiation.html', error='Все поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    if x1 == 0 and x2 == 0:
        return render_template('lab4/exponentiation.html', error0='Оба значения равны нулю!')
    result = x1 ** x2
    return render_template('lab4/exponentiation.html', x1=x1, x2=x2, result=result)
    

tree_count = 0

@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    operation = request.form.get('operation')
    if operation == 'cut':
        tree_count -=1
    elif operation == 'plant':
        tree_count +=1
    if tree_count < 0:
        tree_count = 0
        return render_template('lab4/tree.html', error='Вы не можете срубить больше деревьев', tree_count=tree_count)
    return redirect('/lab4/tree')


users = [
    {'name': 'Alexander Miller', 'login': 'alex', 'password': '123', 'sex': 'мужской'},
    {'name': 'Robert Davis', 'login': 'bob', 'password': '555', 'sex': 'мужской'},
    {'name': 'Anjelika Onoprienko', 'login': 'anjela', 'password': '176', 'sex': 'женский'},
    {'name': 'Barbara Williams', 'login': 'barbara', 'password': '987', 'sex': 'женский'}
]

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'name' in session:
            authorized = True
            name = session['name']
        else:
            authorized=False
            name = ''
        return render_template('lab4/login.html', authorized=authorized, name=name)
    name = request.form.get('name')
    login = request.form.get('login')
    password = request.form.get('password')
    sex = request.form.get('sex')
    for user in users:
        if login == user['login'] and password == user['password'] and name == user['name'] and sex == user['sex']:
            session['name'] = name
            return redirect('/lab4/login')
    error = 'Неверно введены данные'
    if name == '':
        error = 'Не введёно имя пользователя'
    elif login == '':
        error = 'Не введён логин'
    elif password == '':
        error = 'Не введён пароль'
    return render_template('lab4/login.html', error=error, authorized=False, login=login, password=password, name=name, sex=sex)


@lab4.route('/lab4/registration', methods = ['GET', 'POST'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
        sex = request.form.get('sex')
        if name and login and password:
            users.append({'name': name, 'login': login, 'password': password, 'sex': sex})
            return redirect('/lab4/login')
    return render_template('lab4/registration.html')


@lab4.route('/lab4/users')
def users_list():
    if 'name' not in session:
        return redirect('/lab4/login')
    return render_template('lab4/users.html', users=users, authorized=True)


@lab4.route('/lab4/delete', methods=['POST'])
def delete_user():
    if 'name' in session:
        for user in users: 
            if user['name'] == session['name']:
                users.remove(user)
        session.pop('name', None)
    return redirect('/lab4/login')


@lab4.route('/lab4/edit', methods=['GET', 'POST'])
def edit_user():
    if 'name' not in session:
        return redirect('/lab4/login')
    user = None
    for current_user in users:
        if current_user['name'] == session['name']:
            user = current_user
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name and name != user['name']:  
            user['name'] = name
        if password:  
            user['password'] = password
        if name and name != session['name']:
            session['name'] = name 
        return redirect('/lab4/users')
    return render_template('lab4/edit.html', user=user) 


@lab4.route('/lab4/logout', methods = ['POST'])
def logout():
    session.pop('name', None)
    return redirect('/lab4/login')


@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    message = ''
    snowflake_count = 0
    if request.method == 'POST':
        temperature = request.form.get('temperature')
        if temperature == '':
            message = 'Температура не задана'
        else:
            temperature = int(temperature)
            if temperature < -12:
                message = 'Не удалось установить температуру — слишком низкое значение'
            elif temperature > -1:
                message = 'Не удалось установить температуру — слишком высокое значение'
            elif -12 <= temperature <= -9:
                message = f'Установлена температура: {temperature}°C'
                snowflake_count = 3
            elif -8 <= temperature <= -5:
                message = f'Установлена температура: {temperature}°C'
                snowflake_count = 2
            elif -4 <= temperature <= -1:
                message = f'Установлена температура: {temperature}°C'
                snowflake_count = 1
    return render_template('lab4/fridge.html', message=message, snowflake_count=snowflake_count)


grain_prices = [
    {'name': 'ячмень', 'price': '12345'},
    {'name': 'овёс', 'price': '8522'},
    {'name':'пшеница', 'price': '8722'},
    {'name': 'рожь', 'price': '14111'}
]

@lab4.route('/lab4/grain', methods=['GET', 'POST'])
def grain():
    if request.method == 'POST':
        grain_type = request.form.get('grain_type')
        weight = request.form.get('weight')
        if weight == '':
            message = 'Вес не указан'
            return render_template('lab4/grain.html', message=message)
        weight = int(weight)
        if weight <= 0:
            message = 'Вес должен быть больше 0'
            return render_template('lab4/grain.html', message=message) 
        elif weight > 500:
            message = 'Такого объёма сейчас нет в наличии'
            return render_template('lab4/grain.html', message=message)  
        else:
            for grain_price in grain_prices:
                if grain_price['name'] == grain_type:
                    price = grain_price['price']
        price = int(price)  
        total_cost = price * weight
        discount = 0
        if weight > 50:
            discount = total_cost * 0.1
            total_cost = total_cost * 0.9
        return render_template('lab4/pay.html', weight=weight, grain_type=grain_type, total_cost=total_cost, discount=discount)
    return render_template('lab4/grain.html')


@lab4.route('/lab4/pay')
def pay():
    return render_template('lab4/pay.html')

