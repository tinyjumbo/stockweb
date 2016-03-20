#test mode
from app import app
#server mode
#from FlaskApp.app import app
# dude these schema things should not be in the view.. this basically means
# everytime when you refresh the page you have to reconnect the server??
# I believe this should be in init file and the you shoudl find a way to maintain through model.
from datetime import datetime, timedelta
from flask import render_template, redirect, url_for, request
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import logging
from logging import Formatter, FileHandler
from DBdriver import DBdriver


#Setup the logger
LOGGER = logging.getLogger('streamer_logger')
file_handler = FileHandler('streamer.log')
handler = logging.StreamHandler()
file_handler.setFormatter(Formatter(
        '%(thread)d %(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
))
handler.setFormatter(Formatter(
        '%(thread)d %(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
))
LOGGER.addHandler(file_handler)
LOGGER.addHandler(handler)
LOGGER.setLevel(logging.DEBUG)




@app.route("/")
def index():
    db=DBdriver()
    barchar_data=db.read_barchar()
    g_data=db.read_linechart('google')
    a_data=db.read_linechart('amazon')
    fb_data=db.read_linechart('facebook')
    print g_data
    print a_data
    print fb_data
    print barchar_data
    return render_template('index.html',info=barchar_data, line=g_data, line2=a_data, line3=fb_data)





















