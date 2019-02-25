import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response
)
from wekun import app, db
from sqlalchemy import func
# from wekun.models import Users, Answers, Images
# from survey.data import IMAGES
import random


bp = Blueprint('auth', __name__)

@bp.route('/')
def index():
    return render_template('survey.html')

@bp.route('/about_us', methods=('GET', 'POST'))
def about_us():
    return "Hello world"
