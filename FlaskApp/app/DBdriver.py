# all DB control goes here.
from datetime import datetime, timedelta
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import config
from app.models.tcount import tcount





#barchar reader
class DBdriver():

	def __init__(self):
		self.client = MongoClient(config.MONGO_HOST, config.MONGO_PORT)
		self.db = self.client.tinyjumbo


	def read_barchar(self):

		#future will not be hardcode time
		start = datetime(2016, 2, 18, 20, 01, 01)
		end = datetime(2016, 2, 19,20 , 01, 04)

		tweet_collection = self.db.tcount
		 #read from DB and store it
		print "start to get collections"
		count_set = []
		print "create an empty set"


		
		db_read = tweet_collection.find({'date': {'$gte': start, '$lt': end}}).sort([("company",pymongo.ASCENDING)])
		#db_read_num = tweet_collection.find({'date': {'$gte': start, '$lt': end}}).count()
		#db_read = tweet_collection.find_one()
		print "succeed to read"
		for record in db_read:
			tcount_obejct=tcount(company=record["company"],count=record["count"],date=record["date"])
			count_set.append(tcount_obejct.count)
		return count_set


