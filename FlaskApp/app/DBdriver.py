# all DB control goes here.
import collections
from datetime import datetime, timedelta
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import config
from app.models.tcount import tcount


# barchar reader
class DBdriver():
    def __init__(self):
        self.client = MongoClient(config.MONGO_HOST, config.MONGO_PORT)
        self.db = self.client.tinyjumbo

    def read_barchar(self):
        # future will not be hardcode time
        

        tweet_collection = self.db.tcount
        # read from DB and store it
        print "start to get collections"
        count_set = collections.defaultdict(list)
        print "create an empty set"      
       	db_read_num = tweet_collection.find().count()/3
        print db_read_num
        count = 1
        while(count < db_read_num):
            
            end = datetime.now().today() - timedelta(days=count)
            print end
            start = end - timedelta(days=1)
            print start
            db_read = tweet_collection.find({'date': {'$gte': start, '$lt': end}}).sort([("company", pymongo.ASCENDING)])
            num = tweet_collection.find({'date': {'$gte': start, '$lt': end}}).count()
            print num
            if(num == 3):
                for record in db_read:
                    tcount_obejct = tcount(company=record["company"], count=record["count"], date=record["date"])
                    key = record["date"].strftime('%m/%d/%Y')
                    count_set[key].append(tcount_obejct.count)
            count = count+1
        # db_read = tweet_collection.find_one()
        print "succeed to read"
		
        return count_set
