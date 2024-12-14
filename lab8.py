from flask import Blueprint, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from db import db
from db.models import users, articles
from flask_login import login_user, login_required, current_user, logout_user

lab8 = Blueprint('lab8', __name__)


@lab8.route('/lab8/')
def lab():
    if current_user.is_authenticated:
        return render_template('lab8/lab8.html', login=current_user.login)
    return render_template('lab8/lab8.html')


@lab8.route('/lab8/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return render_template('lab8/register.html', login=current_user.login, message='Вы не можете зарегистрироваться, находясь в аккаунте. Хотите выйти?')
    
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
    login_user(new_user)
    return render_template('lab8/success_login.html', login=login_form)


@lab8.route('/lab8/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return render_template('lab8/success_login.html', login=current_user.login)
        
    if request.method == 'GET':
        return render_template('lab8/login.html')

    login_form = request.form.get('login')
    password_form = request.form.get('password')

    if login_form == '':
        return render_template('lab8/login.html', error='Заполните имя пользователя')

    if password_form == '':
        return render_template('lab8/login.html', error='Заполните пароль')

    user = users.query.filter_by(login = login_form).first()
    remember = request.form.get('remember', 'False') == 'True'
    
    if user:
        if check_password_hash(user.password, password_form):
            login_user(user, remember=remember)
            return render_template('lab8/success_login.html', login=login_form)
        
    return render_template('lab8/login.html', error='Ошибка входа: логин и/или пароль неверны')


@lab8.route('/lab8/articles/')
@login_required
def article_list():
    articles_list = articles.query.filter_by(login_id=current_user.id).all()
    return render_template('lab8/articles.html', articles=articles_list, login=current_user.login)


@lab8.route('/lab8/logout')
@login_required
def logout():
    logout_user()
    return redirect('/lab8/')


@lab8.route('/lab8/create', methods=['GET', 'POST'])
@login_required
def create_article():
    if request.method == 'GET':
        return render_template('lab8/create_article.html')

    title = request.form.get('title')
    article_text = request.form.get('article_text')

    if title == '' or article_text == '':
        return render_template('lab8/create_article.html', error='Заполните все поля')

    new_article = articles(title=title, article_text=article_text, login_id=current_user.id)
    db.session.add(new_article)
    db.session.commit()
    return redirect('/lab8/articles/')


@lab8.route('/lab8/edit/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):
    article = articles.query.get_or_404(article_id)

    if article.login_id != current_user.id:
        return redirect('/lab8/articles/')

    if request.method == 'GET':
        return render_template('lab8/edit_article.html', article=article)

    title = request.form.get('title')
    article_text = request.form.get('article_text')

    if title == '' or article_text == '':
        return render_template('lab8/edit_article.html', article=article, error='Заполните все поля')

    article.title = title
    article.article_text = article_text
    db.session.commit()
    return redirect('/lab8/articles/')


@lab8.route('/lab8/delete/<int:article_id>', methods=['POST'])
@login_required
def delete_article(article_id):
    article = articles.query.get_or_404(article_id)

    if article.login_id == current_user.id:
        db.session.delete(article)
        db.session.commit()
    return redirect('/lab8/articles/')

