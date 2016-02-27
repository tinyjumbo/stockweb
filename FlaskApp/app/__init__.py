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
