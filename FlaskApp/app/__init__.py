from flask import Flask
app = Flask(__name__)
#--CONFIG SETTING BEGIN-------on test uncommend test mode -----on server uncommend server mode--------------------
#test mode
from app import views
#server mode 
#from Flask.app import views
#--CONFIG SETTING END---------on test uncommend test mode -----on server uncommend server mode--------------------
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure



# all init should goes here file settings db settings



#----DB SETTINGS BEGIN---------------------------------------------

MONGO_HOST = 'localhost'
MONGO_PORT = 27017

#Try to connect to MongoDB
try:
	client = MongoClient(MONGO_HOST, MONGO_PORT)
	db = client.tinyjumbo
	tweet_collection = db.google
	print "Sucees connect to DB"
	#print tweet_collection.find_one()

except ConnectionFailure:
	LOGGER.error('Could not connect to MongoDB, aborting Flask app...')
	sys.exit(-1)
#----DB SETTINGS END---------------------------------------------
