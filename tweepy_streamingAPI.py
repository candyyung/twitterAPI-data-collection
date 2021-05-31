# Setup and install necessary packages
# Please make sure to install the package Tweepy 
# pip install tweepy

# Load the library
import tweepy
from tweepy.auth import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

# This part is responsible of getting the data, and printing the data.
# It's a basic listener, writing tweets to the output file (filename).
class StdOutListener(StreamListener):
    def on_data(self, data):
        #print data
        with open(filename,'a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print(status)

l = StdOutListener()

# Set up the credentials, hashtags, and filename here
# Please add your Twitter API user credentials here. 
# The tokens and keys below are invalid.

access_token = "11231679747556123683-4s6jMP8Tdqc3mgGXFEqztffhSJPRpm"
access_token_secret = "sq2J3rIaNna4BiS4VpjKH4i7HLdA3iXRPUlVkIAP8CS2r"
api_key = "OXHxsfNZtmPgNcptFJ5T2lJd7"
api_secret_key = "A9fVqdkG53i0Hdx4t2CV8nCEcb6GGcKXNcUP23gXSKDMcdRNfh"

# Define a list of trackable hash tags or character strings
# that you would like to get data on.

tracking = ['#fortnite', '#TravisScott','#travisscott','#travisscottfortnite','#fortnitetravisScott','#astronomical','#astroworld'] 
#tracking multiple keywords/hashtags

# Define file in which to write the Tweets 
filename = 'fortnite_stream.json'

# Start your data collection

print('Writing to...' + filename)

while True:
    try:
        auth = OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)
        stream.filter(track=tracking)
    except:
        print('Error in data collection; check internet connection and API retrieval limit. If this error persists, please restart Jupyter Notebook.')


