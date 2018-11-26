import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['postgres://rpvhhvddjfxgnq:508f6ee01161c48c8f320ab07949e225febd2fc35a60a61653c3b5e67d39dc1e@ec2-54-225-110-156.compute-1.amazonaws.com:5432/de9brngo4iedlo']
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Initializing the manager
db = SQLAlchemy(app)

# Import and register the blueprint
from survey import auth
app.register_blueprint(auth.bp)
app.add_url_rule('/', endpoint='register')
