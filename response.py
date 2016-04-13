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
CONSUMER_SECRET = 'yxxxxx'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

t = Twitter(auth=oauth)

t.statuses.update(status="I think @chalkley_larry smells")