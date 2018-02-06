#January 31 2018

#print("running on GIT")

#ls = [i for i in range(10)]

#for l in ls:
#    print(l)
import tweepy
consumer_key = 'BCftDrlG6PZLlm60HezW6xchj'
consumer_secret = 'BDOBTnwu2I9Zo7R6ZOX8pyWZ1758UDQsPlOvST6P0qvSdd6TGD'
access_token = '958103738299834368-PnI1AumMlVZK41aBzrbIxPPmeCvqYQ5'
access_token_secret = 'YGqcBxxBf4oPzUwRxEBxEtttLgwrvZng5LklSIegd5GU4'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
tweet = "Lauren Duca's biggest friend!"
api.update_status(status=tweet)