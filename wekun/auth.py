import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response
)
from wekun import app, db
from sqlalchemy import func
from wekun.models import Users, Answers
from wekun.data import IMAGES
import random


bp = Blueprint('auth', __name__)

@bp.route('/')
def index():

    ## Primero se revisa que exista la Cookie 'userid' y que corresponda a un id en la Tabla Users
    username = request.cookies.get('userid')
    counter = 1 
    # counter  = db.session.query(func.count()).filter(Users.id == username).all()[0][0]

    ## En caso de cumplirse ambos criterios, se redirige a la pagina home
    if username and counter > 0:
        # print("Hay cookies")
        return redirect(url_for('auth.survey'))

    # # En caso contrario se redirige a la pagina de registro
    # print("No hay cookies")
    return redirect(url_for('auth.welcome'))

@bp.route('/about_us', methods=('GET', 'POST'))
def about_us():
    return render_template('about_us.html')

@bp.route('/contact', methods=('GET', 'POST'))
def contact():
    return render_template('contact.html')

@bp.route('/welcome', methods=('GET', 'POST'))
def welcome():
    return render_template('welcome.html')

@bp.route('/es', methods=('GET','POST'))
def spanish():
    resp = make_response(redirect('/'))
    resp.set_cookie('languaje', 'es', max_age=60*60*24*365)
    return resp

@bp.route('/en', methods=('GET','POST'))
def english():
    resp = make_response(redirect('/'))
    resp.set_cookie('languaje', 'en', max_age=60*60*24*365)
    return resp


## select from data 2 random images
def get_photos(source):
    p1 = random.choice(source)
    p2 = random.choice(source)

    ## Revisar que no sea la misma imagen
    if p1["id"] == p2["id"]:
        return get_photos(source)
    return p1["id"], p2["id"]

@bp.route('/survey', methods=('GET', 'POST'))
def survey():
    if request.method == 'GET':
        url_1, url_2= get_photos(IMAGES)
        url_1 = "{}".format(url_1)
        url_2 = "{}".format(url_2)
        category = session.get('category')
        # print(category)
        if category == None:
            ## randint(a,b) returns a random integer N such that a <= N <= b.
            category = str(random.randint(1,4))


    elif request.method == 'POST':
        ## Extraer vairables
        choice = request.form.get('answer')
        category = request.form.get('category')
        print(choice)
        if choice == None:
            session['category'] = category
            print("Cambio de pregunta")
            return redirect(url_for('auth.index'))
        else:
            author = request.cookies.get('userid')
            id_1 = request.form.get('image_1')
            id_2 = request.form.get('image_2')
            session['category'] = category

            ## Instertar en la Base de Datos
            answer = Answers(user_id=author, img_1=id_1, img_2=id_2, choice=choice, question=category)
            db.session.add(answer)
            db.session.commit()
            print("Respuesta guardada")
            return redirect(url_for('auth.index'))
    return render_template('survey.html', photo1 = url_1, photo2 = url_2, category=category)


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        ## Request de las variables del form
        gender = request.form['gender']
        age = str(request.form['age'])
        country = request.form['country']
        region = request.form['state']
        comuna = request.form['comuna']
        education = request.form['study']
        transport = request.form['transportation']
        userid = db.session.query(func.count(Users.id)).all()[0][0] + 1 ## Falta generar un id secreto
        ip_address = request.remote_addr

        ## Insrtar la columna en la Base de Datos
        user = Users(gender=gender, age=age, country=country, region=region, comuna=comuna, ip_address=ip_address,
                    education=education, transport=transport)
        db.session.add(user)
        db.session.commit()

        ## Crear el diccionario Cookie key:'userid', value:str(userid), con vigencia de 365 dias
        resp = make_response(redirect('/'))
        resp.set_cookie('userid', str(userid), max_age=60*60*24*365)
        return resp

    return render_template('register.html')
