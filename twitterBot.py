import tweepy
import os
from dotenv import load_dotenv
from database import *

load_dotenv()

api_key = os.getenv('API_KEY')
api_key_secret = os.getenv('API_KEY_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')


global client
global tweet_id

def connectTwitter():
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
def fetch_user():
    while True:
        while True:
            try:
                msg = input("Would you like to fetch a user? (Y/n): ").lower()
                if msg == 'y' or msg == 'n':
                    break
                else:
                    raise Exception
            except Exception:
                print("Please enter y or n")
            except KeyboardInterrupt:
                print("KeyboardInterrupt")
                quit()

        if msg == 'y':
            while True:
                try:
                    username = input("Enter the username of the user you wish to fetch: ")
                    try:
                        user = client.get_user(username=username, user_auth=True)
                        user_id = user[0].id
                        break
                    except KeyboardInterrupt:
                        quit()
                    except:
                        print("Unable to find user")
                        while True:
                            try:
                                msg = input("Continue? (Y/n): ").lower()
                                if msg != 'n' or msg != 'y':
                                    raise
                                if msg == 'n':
                                    break
                            except KeyboardInterrupt:
                                quit()
                            except:
                                print("Enter 'y' or 'n'")
                except KeyboardInterrupt:
                    quit()
                except:
                    print("Invalid entry")
                
            
        elif msg == 'n':
            break

# tweet send
def tweet():
    while True:
        try:
            msg = input("Would you like to send a tweet? (Y/n): ").lower()
            if msg == 'y' or msg == 'n':
                break
            else:
                raise
        except KeyboardInterrupt:
            quit()
        except:
            print("Please enter 'y' or 'n'")

    if msg == 'y':
        while True:
            try:
                tweet_content = input("Enter the text that you want to tweet: ")
                break
            except KeyboardInterrupt:
                quit()
            except Exception as err:
                print(err)
            
        tweet = client.create_tweet(text=tweet_content, user_auth=True)
        print('tweet sent')
        tweet_id = tweet[0].get('id')
        
        while True:
            try:
                msg = input("Would you like to delete the tweet? (Y/n): ").lower()
                if msg == 'y' or msg == 'n':
                    break
                else:
                    raise
            except KeyboardInterrupt:
                quit()
            except:
                print("Please enter 'y' or 'n'")
        
        if msg == 'y':
            client.delete_tweet(id=tweet_id, user_auth=True)
            print("tweet deleted")


def create_tweet(tweet_text):
    client = connectTwitter()
    try:
        tweet = client.create_tweet(text=tweet_text, user_auth=True)
        message = 'tweet sent'
        tweet_id = tweet[0].get('id')
        print(f"creating tweet: {tweet_text}")
        addTweet(tweet_id, tweet_text)
        return tweet_id, message
    except Exception as e:
        message = "failed to send"
        tweet_id = 0
        print(e)
        return tweet_id, message

def delete_tweet(tweet_text):
    client = connectTwitter()
    try:
        tweet_id = deleteTweet(tweet_text)
        client.delete_tweet(id=tweet_id, user_auth=True)
        message = "tweet deleted"
        return message
    except:
        message = 'failed to delete'
        return message