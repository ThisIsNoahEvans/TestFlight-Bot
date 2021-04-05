from search_engines import Google
from search_engines import Startpage
from search_engines import Ask

import tweepy
import time

auth = tweepy.OAuthHandler('-', '-')
auth.set_access_token('-', '-')
api = tweepy.API(auth)

engine = Google()
results = engine.search('site:testflight.apple.com')
links = results.links()

for link in links:
    print('Starting Google link loop')
    #api.update_status(link)
    print('Tweeted link:', link)
    time.sleep(3600)

print("Out of Google links.")
api.update_status('Service one exhausted - switching to service two. You may see links that have been posted before.')

engine = Startpage()
results = engine.search('site:testflight.apple.com')
links = results.links()

for link in links:
    print('Starting Startpage link loop')
    api.update_status(link)
    print('Tweeted link:', link)
    time.sleep(3600)

print("Out of Startpage links.")
api.update_status('Service two exhausted - switching to service two. You may see links that have been posted before.')

engine = Ask()
results = engine.search('site:testflight.apple.com')
links = results.links()

for link in links:
    print('Starting Ask link loop')
    #api.update_status(link)
    print('Tweeted link:', link)
    time.sleep(3600)

print("Out of Ask links.")
api.update_status('All links have been exausted. The bot will be restarted soon, and you may see links that have been posted before.')
print('Out of all links!')
