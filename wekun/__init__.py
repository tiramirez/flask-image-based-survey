import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__, instance_relative_config=True, static_url_path='/static')
application.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'	

## Change this when runnign on local/external serve

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
 

# Initializing the manager
db = SQLAlchemy(application)

# Import and register the blueprint
from wekun import auth
application.register_blueprint(auth.bp)
application.add_url_rule('/', endpoint='index')