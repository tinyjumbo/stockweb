# all DB control goes here.
from datetime import datetime, timedelta
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import config





#barchar reader
class DBdriver():

	def __init__(self):
		self.client = MongoClient(config.MONGO_HOST, config.MONGO_PORT)
		self.db = self.client.tinyjumbo


	def read_barchar(self):

		self.tweet_collection = self.db.tcount
		 #read from DB and store it
		print "start to get collections"
		self.data_set = []
		self.count_set = []
		print "create an empty set"


		self.now = datetime.now()
		self.start = datetime(2016, 2, 18, 20, 01, 01)
		self.end = datetime(2016, 2, 19,20 , 01, 04)
		self.db_read = self.tweet_collection.find({'date': {'$gte': self.start, '$lt': self.end}}).sort([("company",pymongo.ASCENDING)])
		self.db_read_num = self.tweet_collection.find({'date': {'$gte': self.start, '$lt': self.end}}).count()
		#db_read = tweet_collection.find_one()
		print self.db_read
		print self.db_read_num
		print "succeed to read"
		for i in self.db_read:
			self.count_set.append(i["count"])

		return self.count_set


