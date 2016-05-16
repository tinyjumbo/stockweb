#test mode
from app import app
from datetime import datetime, timedelta
from flask import render_template, redirect, url_for, request
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import logging
from logging import Formatter, FileHandler
from DBdriver import DBdriver



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





















