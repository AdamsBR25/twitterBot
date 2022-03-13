import pymongo
import os
from dotenv import load_dotenv
import certifi
ca = certifi.where()

load_dotenv()

db_uri = os.getenv('DB_URI')

def connectMongo():
    """Connects to the mongodb atlas cluster and returns the tweets collection"""
    try:
        mongo = pymongo.MongoClient(db_uri, tlsCAFile=ca)
        db = mongo.get_database('TwitterBot')
        tweets = db.get_collection('tweets')
        return tweets
    except Exception as e:
        print(e)
        quit()

def addTweet(tweet_id, tweet_text):
    """Adds a tweet to the database"""
    tweet = {
        'id': tweet_id,
        'text': tweet_text
    }
    tweets = connectMongo()
    tweets.insert_one(tweet)

def deleteTweet(tweet_text):
    """Removes a tweet from the database"""
    tweets = connectMongo()
    tweet = tweets.find_one({'text': tweet_text})
    tweet_id = tweet['id']
    tweets.delete_one(tweet)
    return tweet_id

def getTweets():
    """Gets and returns a list of the tweet content in the database"""
    tweets = connectMongo()
    tweet_list = []
    for tweet in tweets.find():
        tweet_list.append(tweet['text'])
    return tweet_list
