import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response
)
from survey import app, db
from sqlalchemy import func
from survey.models import Users, Answers, Images
from survey.data import IMAGES
import random


bp = Blueprint('auth', __name__)

@bp.route('/')
def index():
    ## Primero se revisa que exista la Cookie 'userid' y que corresponda a un id en la Tabla Users
    username = request.cookies.get('userid')
    counter  = db.session.query(func.count()).filter(Users.id == username).all()[0][0]

    ## En caso de cumplirse ambos criterios, se redirige a la pagina home
    if username and counter > 0:
        # print("Hay cookies")
        return redirect(url_for('auth.home'))

    # # En caso contrario se redirige a la pagina de registro
    # print("No hay cookies")
    return redirect(url_for('auth.register'))


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        ## Request de las variables del form
        gender = request.form['gender']
        age = str(request.form['age'])
        country = 'Chile'
        region = request.form['region']
        comuna = request.form['comuna']
        education = request.form['study']
        transport = request.form['transportation']
        userid = db.session.query(func.count(Users.id)).all()[0][0] + 1 ## Falta generar un id aleatorio
        print(userid)
        # session['username'] = userid
        session['category'] = 'None'
        
        ## Insrtar la columna en la Base de Datos
        user = Users(gender=gender, age=age, country=country, region=region, comuna=comuna, 
                    education=education, transport=transport)
        db.session.add(user)
        db.session.commit()

        ## Crear el diccionario Cookie key:'userid', value:str(userid), con vigencia de 365 dias
        resp = make_response(redirect('/'))
        resp.set_cookie('userid', str(userid), max_age=60*60*24*365)

        return resp

    return render_template('register.html')

## select from data 2 random images
def get_photos(source):
    p1 = random.choice(source)
    p2 = random.choice(source)

    ## Revisar que no sea la misma imagen
    if p1["id"] == p2["id"]:
        return get_photos(source)
    return p1["id"], p2["id"]

@bp.route('/home', methods=('GET', 'POST'))
def home():
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
        author = request.cookies.get('userid')
        category = request.form.get('category')
        choice = request.form.get('submit')
        id_1 = request.form.get('image_1')
        id_2 = request.form.get('image_2')

        session['category'] = category

        ## Instertar en la Base de Datos
        answer = Answers(user_id=author, img_1=id_1, img_2=id_2, choice=choice, question=category)
        db.session.add(answer)
        db.session.commit()

        return redirect(url_for('auth.index'))
    return render_template('home.html', photo1 = url_1, photo2 = url_2, category=category)



@bp.route('/about_us', methods=('GET', 'POST'))
def about_us():
    return "Hello world"


###############################################################################

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