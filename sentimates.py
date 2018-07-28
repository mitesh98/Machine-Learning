import tweepy
from textblob import TextBlob

consumer_key="qEcmdmB1ljpmn9prtTySPujDv"
consumer_secret="oK9XGArKtalGJGdhckNWABu47iW9LRJXUqxKHlaWnXByXyiFBb"

access_token="847439552339890177-fxniAFXcNqe8aFKL7dRXq1AjWQeLVYJ"
access_token_secrete="vaNSO9R0UwPadqRxQ5whaF4lVykRHaYQGsqjOvVsL7Jci"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secrete)

api=tweepy.API(auth)

public_tweet=api.search("modi")

for tweet in public_tweet:
    print(tweet.text.encode("utf-8"))
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
