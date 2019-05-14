import os

CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'

print(CONSUMER_KEY)
print(CONSUMER_SECRET)

