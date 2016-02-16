#test mode
from app import app
#server mode
#from FlaskApp.app import app

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

	#----DB INIT BEGIN---------------------------------------------

	MONGO_HOST = 'localhost'
	MONGO_PORT = 27017

	#Try to connect to MongoDB
	try:
		client = MongoClient(MONGO_HOST, MONGO_PORT)
		db = client.tinyjumbo
		tweet_collection = db.google
		print "Sucees connect to DB"

	except ConnectionFailure:
		LOGGER.error('Could not connect to MongoDB, aborting Flask app...')
		sys.exit(-1)
	#----DB INIT END---------------------------------------------


	#read from DB and store it to Tweets_sche object
	db_read = tweet_collection.find_one()
	tweet= Tweets_sche(db_read["time"],db_read["text"],db_read["hashtages"])


	return render_template('index.html',info=tweet)




















