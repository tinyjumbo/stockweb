#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This code is used for extracting tweets based on key words
the tweets will be stored in local MongoDB.

to pull the info out from DB use folliwng 

mongoexport --host localhost --db tinyjumbo --collection google --csv --out tweets.csv --fields time,text,hashtages
mongoexport --host localhost --db tinyjumbo --collection google --out tweets.json

mongoexport --host  162.243.122.37 --db tinyjumbo --collection google --out tweets.json





mongoimport --host localhost --db tinyjumbo --collection google --file tweets.json
mongoimport --host localhost --db tinyjumbo --collection tcount --file tcount.json


'''




from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pymongo import MongoClient
from sys import exit
import time
import json
import datetime
import unicodedata



#mongoDB setting
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
db=client.tinyjumbo



#consumer key, consumer secret, access token, access secret.
ckey="p3nROxZYmF9aOWvJYkdAMtd96"
csecret="kqePWTGGF2q6O2ITLbAfY5PILUUUJ20oVkquADZORt4oY2wnTp"
atoken="2300498179-IWCFs7kAIbbrH6gS2Yffwg4Sy1Y3ajEwSwNMBYB"
asecret="NWyDoIYqe4UaJbATPHhp7kkoiK2YHjOtshZEzTcaPrzDP"



#init starttime
global starttime
global tweetscount
starttime = time.time()
tweetscount = 0







#listen to twitter Stream API and store tweets with key word Google in to MongoDB.
class listener(StreamListener):
	

	def on_data(self, data):

		#set global variable
		global starttime
		global tweetscount
		tweetscount+=1

		#if program running over 1m then exit
		endtime=time.time()
		#print (endtime-starttime)
		if (endtime - starttime)> 30.0:
			record=str(datetime.datetime.now())
			record= record + " " +str(tweetscount) +" amazon\n"
			with open('/root/data_collector/logfile','a') as f:
				f.write(record)

			exit()


		#reading tweets from API and save to MongoDB
		newdata = json.loads(data)
		text=unicodedata.normalize('NFKD', newdata["text"]).encode('ascii','ignore')
		simple={"time":str(datetime.datetime.now()),"text":text,"hashtages":newdata['entities']['hashtags']}
		result = db.amazon.insert_one(simple)
		#print result.inserted_id
	


		return True

		


	def on_error(self,status):

		print status



auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

twitterStream = Stream(auth,listener())
twitterStream.filter(track=["Amazon","amazon"])













