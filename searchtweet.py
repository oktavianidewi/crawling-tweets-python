import twitter, json
from token import *

auth = twitter.oauth.OAuth(accesstoken, accesstokensecret, consumerkey, consumersecret)
twitter_api = twitter.Twitter(auth=auth)
query = '%India'
count = 100

search_result = twitter_api.search.tweets(query=query, count=count)
statuses = search_result['statuses']

for _ in range(5):
    print("Length of statuses", len(statuses))
    try:
        next_result = search_result['search_metadata']['next_results']
    except KeyError, e:
        break

    kwargs = dict([kv.split('=') for kv in next_result[1:].split("&")])
    search_result = twitter_api.search.tweets(**kwargs)
    statuses += search_result['statuses']

print(json.dumps(statuses[0], indent=1))