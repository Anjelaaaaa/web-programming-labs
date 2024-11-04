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
        return render_template('lab4/tree.html', error='Вы не можете срубить больше деревьев')
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


@lab4.route('/lab4/logout', methods = ['POST'])
def logout():
    session.pop('name', None)
    return redirect('/lab4/login')


    