import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response
)
from survey import app, db
from sqlalchemy import func
from survey.models import User, Answer, Images
from survey.data import IMAGES
import random


bp = Blueprint('auth', __name__)

@bp.route('/')
def index():
    username = request.cookies.get('username')
    if username:
        print("Hay cookies")
        return redirect(url_for('auth.home'))
    print("No hay cookies")
    return redirect(url_for('auth.register'))


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        gender = request.form['gender']
        age = request.form['age']
        country = request.form['country']
        session['userid'] = db.session.query(func.count(User.id)).all()[0][0] + 1
        
        user = User(gender=gender, age=age, country=country)
        db.session.add(user)
        db.session.commit()

        resp = make_response(redirect('/'))
        resp.set_cookie('username', 'Tomas')

        return resp

    return render_template('register.html')

## select from data 2 random images
def get_photos(source):
    p1 = random.choice(source)
    p2 = random.choice(source)
    return p1["id"], p2["id"]

@bp.route('/home', methods=('GET', 'POST'))
def home():
    if request.method == 'GET':
        url_1, url_2= get_photos(IMAGES)
        url_1 = "{}".format(url_1)
        url_2 = "{}".format(url_2)

    elif request.method == 'POST':
        author = session['userid'] ## Aqui deberia registrar el ID del usuario guardado en las coockies
        category = request.form.get('category')
        choice = request.form.get('submit')
        id_1 = request.form.get('image_1')
        id_2 = request.form.get('image_2')

        answer = Answer(user_id=author, img_1=id_1, img_2=id_2, choice=choice, question=category)
        db.session.add(answer)
        db.session.commit()

        return redirect(url_for('auth.home'))
    return render_template('home.html', photo1 = url_1, photo2 = url_2)

def get_one():
    p1 = db.session.query(Images.img_id).filter(Images.category == None).first()
    return p1[0]

@bp.route('/clasificador', methods=('GET', 'POST'))
def clasificador():
    if request.method == 'GET':
        url_1 = get_one()
        
    elif request.method == 'POST':
        img_id = request.form.get('image_1')
        choice = request.form.get('submit')
        Images.query.filter(Images.img_id == img_id).update({"category": choice})
        db.session.commit()

        return redirect(url_for('auth.clasificador'))

        flash(error)

    return render_template('clasificador.html', photo1 = url_1)
