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

# user fetch
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
# public_tweets = client.get_users_tweets(id=unclebeedy_id, user_auth=True)
# for tweet in public_tweets[0]:
#     print(tweet)