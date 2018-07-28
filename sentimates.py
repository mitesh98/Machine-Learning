import tweepy
from textblob import TextBlob

consumer_key="*******************"
consumer_secret="*************************************"

access_token="***************************************************"
access_token_secrete="***************************************************"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secrete)

api=tweepy.API(auth)

public_tweet=api.search("modi")

for tweet in public_tweet:
    print(tweet.text.encode("utf-8"))
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
