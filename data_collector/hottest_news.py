#!/usr/bin/env python

import tweepy
import time, datetime
from pymongo import MongoClient
import unicodedata
from twitter_oauth import CUSTOMER_KEY, CUSTOMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET

# connection
auth = tweepy.OAuthHandler(CUSTOMER_KEY, CUSTOMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# limit per hour is 350
resetTS = api.rate_limit_status()['resources']['moments']['/moments/permissions']['reset']
resetDT = datetime.datetime.fromtimestamp(resetTS).strftime('%Y-%m-%d %H:%M:%S')
limit = api.rate_limit_status()['resources']['moments']['/moments/permissions']['limit']
remaining = api.rate_limit_status()['resources']['moments']['/moments/permissions']['remaining']
print 'For moments, you have {}/{}, API calls remaining until next reset time {}'.format(remaining, limit, resetDT)

# advanced twitter search operators
done = time.time()
start = time.time() - 7 * 24 * 3600
done2 = datetime.datetime.fromtimestamp(done).strftime('%Y-%m-%d')
start2 = datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d')
query_v0 = 'amazon OR amzn -amazing'
query_v1 = 'amazon OR amzn -amazing since:{} until:{}'.format(start2, done2)
# searching "amazon" OR "amzn", exclude "amazing", exclude retweets, only includes original tweets. retweets#>=10, faves#>10, time-window: last week
query_v2 = 'amazon OR amzn -amazing Filter:news -Filter:nativeretweets min_retweets:10 min_faves:10 since:{} until:{}'.format(start2, done2)
max_tweets = 1000

# fetch data from twitter search api with memory optimization
searched_tweets = []
last_id = -1
while len(searched_tweets) < max_tweets:
    count = max_tweets - len(searched_tweets)
    try:
        new_tweets = api.search(q=query_v2, count=max_tweets, max_id=str(last_id - 1), result_type="recent", lang="en")
        if not new_tweets:
            break
        searched_tweets.extend(new_tweets)
        last_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        # depending on TweepError.code, one may want to retry or wait
        # to keep things simple, we will give up on an error
        break

# sanity check
for item in searched_tweets[:10]:
    print item.text, item.user.followers_count, item.user.statuses_count, item.favorite_count, item.retweet_count

# write to file
with open('FILE_DIR_YOUR_WANT_TO_WRITE', 'a') as thefile:
    for item in searched_tweets:
        text = unicodedata.normalize('NFKD', item.text).encode('ascii', 'ignore')
        thefile.write("followers:{0}, statuses:{1}, favorites:{2}, retweeted:{3}, text:{4}\n".format(
            item.user.followers_count, item.user.statuses_count, item.favorite_count, item.retweet_count, text))

# write to mongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.tinyjumbo
for item in searched_tweets:
    simple = {
        # user
        "user_screen_name": item.user.screen_name,
        "user_followers_count": item.user.followers_count,
        "user_statuses_count": item.user.statuses_count,
        "user_friends_count": item.user.friends_count,
        "user_favourites_count": item.user.favourites_count,
        # tweet
        "tweet_time": str(datetime.datetime.now()),
        "tweet_text": unicodedata.normalize('NFKD', item.text).encode('ascii', 'ignore'),
        "tweet_retweet_count": item.retweet_count,
        "tweet_favorite_count": item.favorite_count
    }
    db.amazon_hot.insert_one(simple)
