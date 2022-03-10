import tweepy as tp
import time
import os

# Credentials to login to my Twittery='
consumerkey=''
consumersecret=''
clientid = ''
clientsecret=''
access_token = '-'
access_secret=''

# Logging into my Twitter Bot Acoount
auth = tp.OAuth1UserHandler(consumer_key=consumerkey,consumer_secret=consumersecret)
auth.set_access_token(access_token,access_secret)
api=tp.API(auth)
tweet = 'Hi, Try 1'
# api.update_status(tweet)


# To iterate over pictures in Quotes folder
os.chdir('quotes')
for quote_img in os.listdir("."):
    api.update_status_with_media(tweet,quote_img)
    time.sleep(4)

