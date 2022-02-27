import pymongo
import json
import certifi
ca = certifi.where()

import time

def connectMongo():
    try:
        mongo = pymongo.MongoClient(f"mongodb+srv://brady:Kristi0866@cluster0.qamfk.mongodb.net/TwitterBot?retryWrites=true&w=majority", tlsCAFile=ca)
        db = mongo.get_database('TwitterBot')
        tweets = db.get_collection('tweets')
        return tweets
    except Exception as e:
        print(e)
        quit()

def addTweet(tweet_id, tweet_text):
    tweet = {
        'id': tweet_id,
        'text': tweet_text
    }
    tweets = connectMongo()
    tweets.insert_one(tweet)

def deleteTweet(tweet_text):
    tweets = connectMongo()
    tweet = tweets.find_one({'text': tweet_text})
    tweet_id = tweet['id']
    tweets.delete_one(tweet)
    return tweet_id

def getTweets():
    tweets = connectMongo()
    tweet_list = []
    for tweet in tweets.find():
        tweet_list.append(tweet['text'])
    return tweet_list
