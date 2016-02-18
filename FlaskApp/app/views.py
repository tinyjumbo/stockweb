#test mode
from app import app
#server mode
#from FlaskApp.app import app

from flask import render_template, redirect, url_for, request
# this file should works as part of controllers for routes
# if we have more actions later we can have a folder for controllers later but now lets keep it here.
# all routes should go here
@app.route("/")
def index():
    return render_template('index.html')
