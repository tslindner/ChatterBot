# Dependencies
import tweepy
import time
import json
import os

consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')

# Create a function that tweets
def TweetOut(tweet_number):
    
    # Setup Tweepy API Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    api.update_status(
        "Chatterbot Jr. %s" % tweet_number)

# Create a function that calls the TweetOut function every minute
counter = 0

# Infinite loop
while counter < 10:

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1

    print(counter)

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(30)

