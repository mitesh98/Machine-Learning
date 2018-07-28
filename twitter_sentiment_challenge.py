import tweepy
from textblob import TextBlob
import csv

#twitter api
consumer_key="********************"
consumer_secret="***************************************"

access_token="******************************"
access_token_secrete="**********************"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secrete)

api=tweepy.API(auth)

with open('modi1.csv','w',newline='') as csvfile:
    fieldnames=['tweet','polarity']
    filewriter=csv.DictWriter(csvfile,fieldnames=fieldnames)

    filewriter.writeheader();



    public_tweet=api.search("@narendramodi")

    for tweet in public_tweet:
        analysis=TextBlob(tweet.text)
        if(analysis.sentiment.polarity>=0.5):
            filewriter.writerow({'tweet':tweet.text.encode("utf-8")
            ,'polarity':'Negative'})
        else:
            filewriter.writerow({'tweet':tweet.text.encode("utf-8")
            ,'polarity':'Positive'})
