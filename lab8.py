from flask import Blueprint, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from db import db
from db.models import users, articles
from flask_login import login_user, login_required, current_user

lab8 = Blueprint('lab8', __name__)


@lab8.route('/lab8/')
def lab():
    return render_template('lab8/lab8.html')


@lab8.route('/lab8/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')

    login_form = request.form.get('login')
    password_form = request.form.get('password')

    if login_form == '':
        return render_template('lab8/register.html', error='Заполните имя пользователя')

    if password_form == '':
        return render_template('lab8/register.html', error='Заполните пароль')

    login_exists = users.query.filter_by(login = login_form).first()
    if login_exists:
        return render_template('lab8/register.html', error='Такой пользователь уже существует')

    password_hash = generate_password_hash(password_form)
    new_user = users(login = login_form, password = password_hash)
    db.session.add(new_user)
    db.session.commit()
    return render_template('lab8/success.html', login=login_form)


@lab8.route('/lab8/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab8/login.html')

    login_form = request.form.get('login')
    password_form = request.form.get('password')

    if login_form == '':
        return render_template('lab8/login.html', error='Заполните имя пользователя')

    if password_form == '':
        return render_template('lab8/login.html', error='Заполните пароль')

    user = users.query.filter_by(login = login_form).first()
    if user:
        if check_password_hash(user.password, password_form):
            login_user(user, remember = False)
            return render_template('lab8/success_login.html', login=login_form)
        
    return render_template('lab8/login.html', error='Ошибка входа: логин и/или пароль неверны')


@lab8.route('/lab8/articles/')
@login_required
def article_list():
    return "список статей"
