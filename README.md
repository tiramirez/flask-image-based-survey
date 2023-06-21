# Image-based app example

When working in my graduate thesis I needed to conduct an infinite survey of pair of images. Ok, it was not infinite, but I wanted it to be flexible so I could save the responses regardless of the number of questions the surveyee answered.

The result of this template is here > https://image-based-ex.herokuapp.com/welcome

## Libraries

* Framework: Flask
* Database server: PostgreSQL

My core training is in Transportartion Engineering, so I learnt from scratch to develope the app for my thesis. I hope this basic strutcture is usefull to someone else who need an image-based survey a little bit more customizable than online platformas as Google Forms, Qualtrics or Survey Monkey.

## Install dependencies
```
python -m venv env
env\Scripts\activate 
python -m pip install -r requirements.txt
```


# Run survey Locally
## Set database URI in .\app\__init__.py
```
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
```

## Initialize database
```
python
>>> from app import db
>>> db.create_all()
>>> db.session.commit()
>>> quit()
```
This will create a new file `app/site.db`

## Run app in Localserver
```
set FLASK_APP=app
python -m flask run
```
