# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob 
import TwitterTokens #importing my Twitter passwords from a seperate file that I did not want to publish to GitHub

print('\nName: Zoe Halbeisen\nUnique name: zoeanne\nUnique ID: 84194416\nSection Day/Time: Wednesday 5:30-6:30\n')

access_token = TwitterTokens.access_token #storing my Twitter tokens 
access_token_secret = TwitterTokens.access_token_secret
consumer_key = TwitterTokens.consumer_key
consumer_secret = TwitterTokens.consumer_secret

#I got started with this code from the Tweepy documentation http://tweepy.readthedocs.io/en/v3.5.0/getting_started.html
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

public_tweets = api.search('Pugs')

subjectivity = 0 #initiating counter variables 
polarity = 0
count = 0

for tweet in public_tweets: #I got started with this code from Colleen's Twitter code
	print(tweet.text)
	count += 1
	analysis = TextBlob(tweet.text)
	subjectivity += analysis.sentiment.subjectivity #I found these methods on the Textblob documentation website https://textblob.readthedocs.io/en/dev/
	polarity += analysis.sentiment.polarity

print("\n")

print("Average subjectivity is " + str(subjectivity/count)) #dividing subjectivity and polarity by count to print average
print("Average polarity is " + str(polarity/count))