import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__, instance_relative_config=True, static_url_path='/static')
app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Initializing the manager
db = SQLAlchemy(app)

# Import and register the blueprint
from survey import auth
app.register_blueprint(auth.bp)
app.add_url_rule('/', endpoint='register')


