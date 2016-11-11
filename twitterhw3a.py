# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

# print("""No output necessary although you 
# 	can print out a success/failure message if you want to.""")

print('\nName: Zoe Halbeisen\nUnique name: zoeanne\nUnique ID: 84194416\nSection Day/Time: Wednesday 5:30-6:30\n')

import TwitterTokens #importing my Twitter passwords from a seperate file that I did not want to publish to GitHub
access_token = TwitterTokens.access_token #storing my twitter tokens into variables 
access_token_secret = TwitterTokens.access_token_secret
consumer_key = TwitterTokens.consumer_key
consumer_secret = TwitterTokens.consumer_secret

import tweepy #I got started with this code from the Tweepy documentation http://tweepy.readthedocs.io/en/v3.5.0/getting_started.html
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

api.update_with_media("pug.jpg", status="I love pugs<3 #UMSI-206 #Proj3") #I got this method from the documentation here http://tweepy.readthedocs.io/en/v3.5.0/api.html?highlight=tweet%20image#API.update_with_media

print("Status update successful!")

