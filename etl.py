import tweepy
import requests
from birdy.twitter import UserClient
import pandas as pd

from settings import SETTINGS
# from twython import Twython


ACCESS_KEY = SETTINGS.ACCESS_KEY
ACCESS_SECRET = SETTINGS.ACCESS_SECRET
CONSUMER_KEY = SETTINGS.CONSUMER_KEY
CONSUMER_SECRET = SETTINGS.CONSUMER_SECRET


def run_twitter_etl():


    client = UserClient(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

    response = client.api.statuses.user_timeline.get(screen_name='@openai', count=100, include_rts=False, tweet_mode='extended')
    tweets = response.data

    list_tweets = []
    for tweet in tweets:
        refined_tweet = {
            "user": tweet.user.screen_name,
            'text': tweet.full_text,
            'favorite_count': tweet.favorite_count,
            'retweet_count': tweet.retweet_count,
            'created_at': tweet.created_at
        }
        list_tweets.append(refined_tweet)

    df = pd.DataFrame(list_tweets)
    df.to_csv('openai_tweets.csv')

run_twitter_etl()

