import tweepy
import os
from dotenv import load_dotenv
import database as db

load_dotenv()

api_key = os.getenv('API_KEY')
api_key_secret = os.getenv('API_KEY_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

def connectTwitter():
    """connects to the twitter api and returns the client object"""
    
    try:    
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_key_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        return client
    except Exception as err:
        print(err)

# user fetch
def fetch_user_id(username):
    """takes in a username and returns the user id for the user"""
    client = connectTwitter()
    try:
        user = client.get_user(username=username, user_auth=True)
        user_id = user[0].id
        return user_id
    except:
        return f"Unable to find user: {username}"


# creates a tweet from content tweet_text and returns the tweet id
def create_tweet(tweet_text):
    """Creates a tweet from tweet content and returns the tweet id for the created tweet and a message for the gui"""
    client = connectTwitter()
    try:
        tweet = client.create_tweet(text=tweet_text, user_auth=True)
        message = 'tweet sent'
        tweet_id = tweet[0].get('id')
        print(f"created tweet: {tweet_text}")
        db.addTweet(tweet_id, tweet_text)
        return tweet_id, message
    except Exception as e:
        message = "failed to send"
        tweet_id = None
        print(e)
        return tweet_id, message

def delete_tweet(tweet_text):
    """Deletes a tweet from tweet text and returns a message for the gui"""
    client = connectTwitter()
    try:
        tweet_id = db.deleteTweet(tweet_text)
        client.delete_tweet(id=tweet_id, user_auth=True)
        message = "tweet deleted"
        return message
    except:
        message = 'failed to delete'
        return message