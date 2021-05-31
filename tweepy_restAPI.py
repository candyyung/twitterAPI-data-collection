
# ## Setup and install necessary packages

# %%
#Load the library
import tweepy
import json

# Set up credentials  
# Input your own token and API key below
# The tokens and keys below are invalid.

access_token = "1231467974755655683-4s6jMP8Tdqc3mgGXFEqztffhSJPRpm" 
access_token_secret = "sq1J23rIaNna4BiS4VpjKH4i7HLdA2iXRPUlVkIAP8CS2r" 
api_key = "OXHxsfNZtmPgNcptFJ4T5lJd5"  
api_secret_key = "A9fVqdkG12i0Hdx4t3CV8nCEcb6GGcKXNcUP91gXSKDMcdRNfh" 

# %% [markdown]
# ## Input the hastags and neccessary settings for Rest API & collect the data

# %%
#REST API - get the historic tweets
auth = tweepy.AppAuthHandler(api_key, api_secret_key)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)
    
filename = 'fortnite25.json' #Save to file name (appends, does not overwrite)
searchQuery = '#fortnite OR #TravisScott OR #travisscott OR #travisscottfortnite OR #fortnitetravisScott OR #astronomical OR #astroworld' #What do you want
maxTweetsTotal = 44900 #Find how many tweets you want
tweetsPerQry = 100 #Max API limit
sinceWhen = '2020-04-25' #From when
untilWhen = '2020-04-26' #Till when (take account of end date)

for tweet in tweepy.Cursor(api.search,
                           q=searchQuery,
                           count=tweetsPerQry,
                           since=sinceWhen,
                           until=untilWhen).items(maxTweetsTotal):
    json_string = json.dumps(tweet._json)
    # print (json_string) # just to test
    with open(filename, 'a') as json_file:
        json_file.write(json_string + '\n')


