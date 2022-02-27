from matplotlib.pyplot import text
import tweepy
import os
from dotenv import load_dotenv
import time

load_dotenv()

api_key = os.getenv('API_KEY')
api_key_secret = os.getenv('API_KEY_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')


try:    
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_key_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )
except Exception as err:
    print(err)
        
try:
    unclebeedy = client.get_user(username="unclebeedy", user_auth=True)
    unclebeedy_id = unclebeedy[0].id
except:
    print("Unable to find user")

tweet = client.create_tweet(text="This is a test tweet sent FROM the twitter API v2", user_auth=True)
print('tweet sent')
tweet_id = tweet[0].get('id')
print(f'tweet id: {tweet_id}')
print("waiting 30 seconds")
time.sleep(30)
client.delete_tweet(id=tweet_id, user_auth=True)
print("tweet deleted")
# public_tweets = client.get_users_tweets(id=unclebeedy_id, user_auth=True)
# for tweet in public_tweets[0]:
#     print(tweet)