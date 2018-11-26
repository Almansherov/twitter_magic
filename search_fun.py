import tweepy
from textblob import TextBlob

consumer_key = "Q8ExpQ04I0zx2wc5pSzQIFyvE"
consumer_secret = "fCu92ZdAi2WJP01Azt7Q7iQAQwFPWDswRk9SaNiazKGhIY1YDI"

access_token = "4105250062-iDdgSzJQLPapTrRTCqHoey4HOpLpGWXnKbzMQpQ"
access_token_secret = "EcKP5A1Rn9UcupltykbmY4eYLCtQrPNGcSGDUGO0LGfuV"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Naruto')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)