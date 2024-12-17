from flask import Blueprint, render_template

lab8 = Blueprint('lab8', __name__)


@lab9.route('/lab9/')
def lab():
    return render_template('lab9/lab9.html')