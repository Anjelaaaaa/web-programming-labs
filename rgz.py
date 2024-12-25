from flask import Blueprint, redirect, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash
from db import db
from db.models import users, books
from flask_login import login_user, login_required, current_user, logout_user

rgz = Blueprint('rgz', __name__)


@rgz.route('/rgz/')
def lab():
    if current_user.is_authenticated:
        return render_template('rgz/rgz.html', login=current_user.login)
    return render_template('rgz/rgz.html')


@rgz.route('/rgz/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return render_template('rgz/register.html', message='Вы не можете зарегистрироваться, находясь в аккаунте. Хотите выйти?', login=current_user.login)
    
    if request.method == 'POST':
        login_form = request.form['login']
        password_form = request.form['password']

        if login_form == '':
            return render_template('rgz/register.html', error='Заполните имя пользователя')

        if password_form == '':
            return render_template('rgz/register.html', error='Заполните пароль')

        login_exists = users.query.filter_by(login=login_form).first()
        if login_exists:
            return render_template('rgz/register.html', error='Такой пользователь уже существует')

        password_hash = generate_password_hash(password_form)
        new_user = users(login=login_form, password=password_hash)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user, remember=False)
        return redirect('/rgz/login')

    return render_template('rgz/register.html')


@rgz.route('/rgz/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return render_template('rgz/success_login.html', login=current_user.login)
    
    if request.method == 'POST':
        login_form = request.form['login']
        password_form = request.form['password']

        if login_form == '':
            return render_template('rgz/login.html', error='Заполните имя пользователя')

        if password_form == '':
            return render_template('rgz/login.html', error='Заполните пароль')

        user = users.query.filter_by(login=login_form).first()
        if user and check_password_hash(user.password, password_form):
            login_user(user)
            return redirect('/rgz/login')

        return render_template('rgz/login.html', error='Неверный логин или пароль')

    return render_template('rgz/login.html')


@rgz.route('/rgz/logout')
@login_required
def logout():
    logout_user()
    return redirect('/rgz/')


@rgz.route('/rgz/books', methods=['GET'])
def book_list():
    page = request.args.get('page', 1, type=int)
    title_filter = request.args.get('title')
    author_filter = request.args.get('author')
    pages_min = request.args.get('pages_min', type=int)
    pages_max = request.args.get('pages_max', type=int)
    publisher_filter = request.args.get('publisher')

    query = books.query

    if title_filter:
        query = query.filter(books.title.ilike(f'%{title_filter}%'))
    if author_filter:
        query = query.filter(books.author.ilike(f'%{author_filter}%'))
    if pages_min is not None:
        query = query.filter(books.pages >= pages_min)
    if pages_max is not None:
        query = query.filter(books.pages <= pages_max)
    if publisher_filter:
        query = query.filter(books.publisher.ilike(f'%{publisher_filter}%'))

    paginated_books = query.paginate(page=page, per_page=20, error_out=False)

    if current_user.is_authenticated:
        return render_template('rgz/book_list.html', books=paginated_books, login=current_user.login)
    return render_template('rgz/book_list.html', books=paginated_books)


@rgz.route('/rgz/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    if current_user.login != 'Admin':
        return redirect('/rgz/books')

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages = request.form['pages']
        publisher = request.form['publisher']
        cover_image = request.form['cover_image']

        new_book = books(title=title, author=author, pages=pages, publisher=publisher, cover_image=cover_image)
        db.session.add(new_book)
        db.session.commit()
        return redirect('/rgz/books')

    return render_template('rgz/add_book.html', login=current_user.login)


@rgz.route('/rgz/edit_book/<int:book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    if current_user.login != 'Admin':
        return redirect('/rgz/books')

    book = books.query.get(book_id)

    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.pages = request.form['pages']
        book.publisher = request.form['publisher']
        book.cover_image = request.form['cover_image']

        db.session.commit()
        return redirect('/rgz/books')

    return render_template('rgz/edit_book.html', book=book, login=current_user.login)


@rgz.route('/rgz/delete_book/<int:book_id>', methods=['POST'])
@login_required
def delete_book(book_id):
    if current_user.login != 'Admin':
        return redirect('/rgz/books')

    book = books.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect('/rgz/books')

