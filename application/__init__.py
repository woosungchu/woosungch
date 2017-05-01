from flask import Flask, render_template
import os

#init
application = Flask(__name__)

#Global Variables
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT,'static/')

@application.route('/')
def hello():
    return render_template('index.html')
