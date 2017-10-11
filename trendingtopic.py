from token import *
import twitter
import json

auth = twitter.oauth.OAuth(accesstoken, accesstokensecret, consumerkey, consumersecret)
twitter_api = twitter.Twitter(auth=auth)
WORLD_WOE_ID = 1
US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

with open('data.txt', 'w') as outfile:
    json.dump(world_trends, outfile)

"""
print(json.dumps(world_trends, indent=1))
print()
print(json.dump(us_trends, indent=1))
"""