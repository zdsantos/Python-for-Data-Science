import tweepy
from textblob import TextBlob

consumer_key = '7FpYhZOS9VqQ1dKbWDVSXp9qa'
consumer_secret = 'k9fOywYWlfWILZHfmJxQOIRzsQHLnxtmeJ19mzRqSDJMaivdVz'

access_token = '239504345-puZQuqvE4U7V6Ob2nm61cWSHVYe1okPU6tq36fxO'
access_token_secret = 'dKg0SzP6S3PW0DMHh3Ygkux1yZIPyht5cLkfZZxoYTnXK'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

