import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
# from werkzeug.security import check_password_hash, generate_password_hash
# from survey.db import get_db
from .data import ACTORS
import random


bp = Blueprint('auth', __name__)

@bp.route('/', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        # username = request.form['username']
        sex = request.form['gender']
        age = request.form['age']
        country = request.form['country']
        # db = get_db()
        error = None

        # if not username:
        #     error = 'Username is required.'
        # elif not sex:
        #     error = 'Information is required.'
        # elif not age:
        #     error = 'Information is required.'

        # if error is None:
        #     db.execute(
        #         'INSERT INTO user (sex, age, country) VALUES (?, ?, ?)',
        #         (sex, age, country)
        #     )
        #     db.commit()
        #     return redirect(url_for('auth.home'))

        flash(error)

    return render_template('register.html')

## select from data 2 random images
def get_photos(source):
    p1 = random.choice(source)
    p2 = random.choice(source)
    print(p2["photo"])
    return p1["photo"], p2["photo"], p1["id"], p2["id"]

# @bp.route('/hello', methods=('GET', 'POST'))
# def hello():
# 	return "Hello world!"

@bp.route('/home', methods=('GET', 'POST'))
def home():
    # global id_1, id_2
    if request.method == 'GET':
        url_1, url_2, id_1, id_2= get_photos(ACTORS)
        url_1 = "{}".format(url_1)
        url_2 = "{}".format(url_2)

    elif request.method == 'POST':
        a = request.values
        print(a)
        author = 1 ## Aqui deberia rgeistrar el ID del usuario guardado en las coockies
        category = request.form.get('category')
        choice = request.form.get('submit')
        id_1 = request.form.get('image_1')
        id_2 = request.form.get('image_2')

        # print(a)

        # db = get_db()

        # error = None
        if choice == 'image_1':
            choice = 1
            pass # do something
        elif choice == 'image_2':
            choice = 2
        else:
            choice = 3
        # db.execute(
        #     'INSERT INTO ans (author_id, category, id_image_1, id_image_2, choice) VALUES (?, ?, ?, ?, ?)',
        #     (author, category, id_1, id_2, choice)
        #     )
        # db.commit()
        return redirect(url_for('auth.home'))
    # if error is None:
    # session.clear()
    # session['user_id'] = user['id']

        # flash(error)
    # url_1, url_2, id_1, id_2= get_photos(ACTORS)
    return render_template('home.html', photo1 = url_1, photo2 = url_2, name1 = id_1, name2 = id_2)

# @bp.before_app_request
# def load_logged_in_user():
#     user_id = session.get('user_id')

#     if user_id is None:
#         g.user = None
#     else:
#         g.user = get_db().execute(
#             'SELECT * FROM user WHERE id = ?', (user_id,)
#         ).fetchone()

# def login_required(view):
#     @functools.wraps(view)
#     def wrapped_view(**kwargs):
#         if g.user is None:
#             return redirect(url_for('auth.login'))

#         return view(**kwargs)

#     return wrapped_view