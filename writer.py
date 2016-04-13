# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = 'xxxxx'
ACCESS_SECRET = 'xxxxx'
CONSUMER_KEY = 'xxxxx'
CONSUMER_SECRET = 'xxxxx'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.filter(track='#refugee,#greece')

for tweet in iterator:

    line = json.dumps(tweet)
    data = json.loads(line.strip())

    name = data['user']['name']
    user = data['user']['screen_name']
    text = data['text'] 
    
    with open("tweet_file.JSON", "a") as outfile:
    	json.dump({'data':[user,name,text]},outfile, sort_keys=True, indent=4)
    	continue
