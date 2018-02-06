
from requests_oauthlib import OAuth1Session
import secret
import json

client_key = secret.api_key
client_secret = secret.api_secret

resource_owner_key = secret.access_token
resource_owner_secret = secret.access_token_secret

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)

r_dic = json.loads(r.text)
r_result = r_dic["statuses"]

for item in r_result:
	print(item['user']['name'] + ": ")
	print(item['text'])
	print("--------")
