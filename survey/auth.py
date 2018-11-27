import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from survey import app, db
from survey.models import User, Answer
# from werkzeug.security import check_password_hash, generate_password_hash
from survey.data import ACTORS
import random


bp = Blueprint('auth', __name__)

@bp.route('/')
def index():
    if 'userid' in session:
        print(session['userid'])
        return redirect(url_for('auth.home'))
    return redirect(url_for('auth.register'))


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        gender = request.form['gender']
        age = request.form['age']
        country = request.form['country']
        session['userid'] = country
        error = None
        if error is None:

            user = User(gender=gender, age=age, country=country)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('auth.home'))

        flash(error)

    return render_template('register.html')

## select from data 2 random images
def get_photos(source):
    p1 = random.choice(source)
    p2 = random.choice(source)
    return p1["id"], p2["id"]

# @bp.route('/hello', methods=('GET', 'POST'))
# def hello():
# 	return "Hello world!"

@bp.route('/home', methods=('GET', 'POST'))
def home():
    if request.method == 'GET':
        url_1, url_2= get_photos(ACTORS)
        url_1 = "{}".format(url_1)
        url_2 = "{}".format(url_2)

    elif request.method == 'POST':
        author = session['userid'] ## Aqui deberia rgeistrar el ID del usuario guardado en las coockies
        category = request.form.get('category')
        choice = request.form.get('submit')
        id_1 = request.form.get('image_1')
        id_2 = request.form.get('image_2')

        answer = Answer(user_id=author, img_1=id_1, img_2=id_2, choice=choice)
        db.session.add(answer)
        db.session.commit()

        return redirect(url_for('auth.home'))
#     # if error is None:
#     # session.clear()
#     # session['user_id'] = user['id']

#         # flash(error)
#     # url_1, url_2, id_1, id_2= get_photos(ACTORS)
    return render_template('home.html', photo1 = url_1, photo2 = url_2)
