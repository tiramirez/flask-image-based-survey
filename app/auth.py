import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response
)
from app import app, db
from sqlalchemy import func
from app.models import Users, Answers
from app.data import IMAGES
import random
import uuid 
# from mod_python import apache



bp = Blueprint('auth', __name__)

@bp.route('/')
def index():
    page = session.get('page')

    if page == None:
        ## Primero se revisa que exista la Cookie 'userid' y que corresponda a un id en la Tabla Users
        user_name = request.cookies.get('user_id')
        # counter = 1 
        counter  = len(db.session.query(Users).filter(Users.user_id == user_name).all())

        ## En caso de cumplirse ambos criterios, se redirige a la pagina home
        if user_name and counter > 0:
            # print("Hay cookies")
            return redirect(url_for('auth.survey'))

        # # En caso contrario se redirige a la pagina de registro
        # print("No hay cookies")
        return redirect(url_for('auth.welcome'))    
    elif page == "survey":
        ## Primero se revisa que exista la Cookie 'userid' y que corresponda a un id en la Tabla Users
        user_name = request.cookies.get('user_id')
        # counter = 1 
        counter  = len(db.session.query(Users).filter(Users.user_id == user_name).all())

        ## En caso de cumplirse ambos criterios, se redirige a la pagina home
        if user_name and counter > 0:
            # print("Hay cookies")
            return redirect(url_for('auth.survey'))

        # # En caso contrario se redirige a la pagina de registro
        # print("No hay cookies")
        return redirect(url_for('auth.register'))

    elif page == "welcome":
        return redirect(url_for('auth.welcome'))
    elif page == "psicometrico":
        return redirect(url_for('auth.psicometrico'))
    elif page == "register":
        return redirect(url_for('auth.register'))
    elif page == "contact":
        return redirect(url_for('auth.contact'))
    elif page == "about_us":
        return redirect(url_for('auth.about_us'))
    else:
        return redirect(url_for('auth.welcome'))        

@bp.route('/about_us', methods=('GET', 'POST'))
def about_us():
    session['page'] = "about_us"
    return render_template('about_us.html')

@bp.route('/contact', methods=('GET', 'POST'))
def contact():
    session['page'] = "contact"
    return render_template('contact.html')

@bp.route('/welcome', methods=('GET', 'POST'))
def welcome():
    browser = request.user_agent.browser
    session['page'] = "welcome"
    return render_template('welcome.html', browser = browser)

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
        session['page'] = "survey"
        url_1, url_2= get_photos(IMAGES)
        url_1 = "{}".format(url_1)
        url_2 = "{}".format(url_2)
        category = session.get('category')
        answer_psico_after = session.get('answer_psico')
        if category == None:
            ## randint(a,b) returns a random integer N such that a <= N <= b.
            category = str(random.randint(1,5))

        user_name = request.cookies.get('user_id')

        if user_name != None:
            counter  = len(db.session.query(Answers).filter(Answers.user_id == user_name).all())
            psico_boolean =  db.session.query(Users.psico1).filter(Users.user_id == user_name).all()
            if len(psico_boolean) == 0:
                psico_boolean = None
            else:
                psico_boolean = psico_boolean[0][0]
        else:
            counter = 0
            psico_boolean = None

        # print('//////////////')
        # print(psico_boolean)

    elif request.method == 'POST':
        ## Extraer vairables
        choice = request.form.get('answer')
        category = request.form.get('category')
        # print(choice)
        if choice == None:
            session['category'] = category
            print("Cambio de pregunta")
            return redirect(url_for('auth.index'))
        else:
            if choice not in ['image_1','image_2','X','=']:
                session['answer_psico'] = 'continue-after'
                choice = 'X'
            author = request.cookies.get('user_id')
            id_1 = request.form.get('image_1')
            id_2 = request.form.get('image_2')
            session['category'] = category
            if author == None:
                return redirect(url_for('auth.index'))
            else:
                ## Instertar en la Base de Datos
                answer = Answers(user_id=author, img_1=id_1, img_2=id_2, choice=choice, question=category)
                db.session.add(answer)
                db.session.commit()
                # print("Respuesta guardada")
                return redirect(url_for('auth.index'))
    return render_template('survey.html', photo1 = url_1, photo2 = url_2, category=category, counter = counter, psico_boolean = psico_boolean, answer_psico_after = answer_psico_after)


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        userid = str(uuid.uuid1())
        deviceid = request.cookies.get('device_id')
        if deviceid == None:
            deviceid = str(uuid.uuid1())

        ## Request de las variables del form
        gender = request.form['gender']
        age = str(request.form['age'])
        nationality = request.form['country2']
        country = request.form['country']
        region = request.form['state']
        comuna = request.form['comuna']
        education = request.form['study']
        transport = request.form['transportation']
        # userid = db.session.query(func.count(Users.id)).all()[0][0] + 1 ## Falta generar un id secreto
        ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
        browser = request.user_agent.browser
        platform = request.user_agent.platform


        ## Insrtar la columna en la Base de Datos
        user = Users(user_id = userid, device_id = deviceid, gender=gender, age=age, 
                    nationality=nationality, country=country, region=region, comuna=comuna,
                    ip_address=ip_address, education=education, transport=transport, browser=browser, platform=platform)
        db.session.add(user)
        db.session.commit()

        ## Crear el diccionario Cookie key:'userid', value:str(userid), con vigencia de 365 dias
        session['page'] = "survey"
        session['answer_psico'] = ''
        resp = make_response(redirect('/'))
        resp.set_cookie('user_id', str(userid), max_age=60*60*24*365)
        resp.set_cookie('device_id', str(deviceid), max_age=60*60*24*365)
        return resp

    # ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    # print("IP-ADD " + str(ip_address))

    # ip_address2 = request.headers.get('X-Real-IP', request.remote_addr)
    # print("IP-ADD 2 " + str(ip_address2))
    # session['page'] = "register"

    # ip_address3 = ip_address = request.environ.get('HTTP_X_REAL_IP', request.remote_addr) 
    # print("IP-ADD 3 " + str(ip_address3))

    # ip_address4 = ip_address = request.environ['REMOTE_ADDR']
    # print("IP-ADD 4 " + str(ip_address4))
    # print (uuid.uuid1())
    session['page'] = "register"

    return render_template('register.html')


@bp.route('/psicometrico', methods=('GET', 'POST'))
def psicometrico():

    if request.method == 'POST':
        author = request.cookies.get('user_id')
        psico1 = request.form['psico1']
        psico2 = request.form['psico2']
        psico3 = request.form['psico3']
        psico4 = request.form['psico4']
        psico5 = request.form['psico5']
        psico6 = request.form['psico6']
        psico7 = request.form['psico7']
        psico8 = request.form['psico8']
        psico9 = request.form['psico9']
        psico10 = request.form['psico10']
        income = request.form['income']
        email = request.form['email']
        if author == None:
            return redirect(url_for('auth.index'))
        else:
            ## Instertar en la Base de Datos
            db.session.query(Users).filter(Users.user_id == author).update({'psico1': str(psico1),
                'psico2': str(psico2), 'psico3': str(psico3), 'psico4': str(psico4), 'psico5': str(psico5),
                'psico6': str(psico6), 'psico7': str(psico7), 'psico8': str(psico8), 'psico9': str(psico9),
                'psico10': str(psico10), 'income': str(income)})
            db.session.commit()
            # print("Respuesta guardada")
            session['page'] = "survey"
            return redirect(url_for('auth.index'))
    session['page'] = "psicometrico"
    return render_template('psico.html')

@bp.route('/show',methods=('GET','POST'))
def show_img():
	if request.method == 'POST':
		img_id = request.form['ID']
	else:
		img_id = None
	return render_template('show_img.html', photo=img_id)
