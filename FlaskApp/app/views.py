#test mode
from app import app
#server mode
#from FlaskApp.app import app
# dude these schema things should not be in the view.. this basically means
# everytime when you refresh the page you have to reconnect the server??
# I believe this should be in init file and the you shoudl find a way to maintain through model.
from datetime import datetime, timedelta
from flask import render_template, redirect, url_for, request
from app.schema.tweets import Tweets_sche
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
# this file should works as part of controllers for routes
# if we have more actions later we can have a folder for controllers later but now lets keep it here.
# all routes should go here
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/barchart")
def bar():
    #----DB INIT BEGIN---------------------------------------------

    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017

    #Try to connect to MongoDB
    try:
        client = MongoClient(MONGO_HOST, MONGO_PORT)
        db = client.testdb
        tweet_collection = db.mycollection
        print "Successfully connect to DB ---"

    except ConnectionFailure:
        LOGGER.error('Could not connect to MongoDB, aborting Flask app...')
        sys.exit(-1)
	#----DB INIT END---------------------------------------------


    #read from DB and store it
    print "start to get collections"
    data_set = []
    date_set = []
    count_set = []
    print "create an empty set"
    now = datetime.now()
    three_day_ago = now.today() - timedelta(days=3)
    four_day_ago = now.today() - timedelta(days=4)
    db_read = tweet_collection.find({'date': {'$gte': four_day_ago, '$lt': three_day_ago}}).sort([("company",pymongo.ASCENDING)])
    db_read_num = tweet_collection.find({'date': {'$gte': four_day_ago, '$lt': three_day_ago}}).count()
    #db_read = tweet_collection.find_one()
    print db_read
    print db_read_num
    print "succeed to read"
    for i in db_read:
        count_set.append(i["count"])
    '''
    for data in db_read:
        print "start to reformat data"
        d = Tweets_counter(data["company"],data["count"],data["date"])
        data_set.append(d)
    '''
    return render_template('barchart.html',info=count_set)




















