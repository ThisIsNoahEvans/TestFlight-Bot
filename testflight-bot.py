#Import Libraries
import urllib
import requests
from bs4 import BeautifulSoup
import tweepy
import time

#Sets Font For Print
class colour:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

#Connect To Twitter APIs
auth = tweepy.OAuthHandler("API", "API")
auth.set_access_token("API", "API")
api = tweepy.API(auth)

#Define User Agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

#Define query and URL
query = "site:testflight.apple.com"
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}"

def testflight_bot():
    #Get results from Google
    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        #Define results list
        results = []
        for g in soup.find_all('div', class_='r'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text
                item = {
                    "title": title,
                    "link": link
                }
                #Add title and link to result list
                results.append(item)
            #Remove text from page title
            title = title.replace('Join the ', '')
            title = title.replace(' - TestFlight - Apple', '')
            #Get beta code
            betaCode = link.replace('https://testflight.apple.com/join/', '')
            print(colour.BOLD, colour.YELLOW, 'Beta Code:', betaCode)
            #Check to see if '/join/ is in URL
            if 'join' in link:
                #Open used file
                with open('used.txt') as usedRead:
                    #Check if beta code in file
                    if betaCode in usedRead:
                        print(colour.BOLD, colour.RED, 'Beta already Tweeted, restarting...')
                        #Run program again
                        testflight_bot()
                print(colour.BOLD, colour.RED, 'Found genuine TestFlight link', colour.END)
                #Print title
                print(colour.BOLD, colour.PURPLE, 'TITLE:', title, colour.END)
                #Print URL
                print(colour.BOLD, colour.PURPLE, 'URL:', link, colour.END)
                #Create final Tweet
                finalTweet = title + ': ' + link
                #Open used file
                usedWrite = open('used.txt', 'a')
                #Save beta code to file
                usedWrite.write(betaCode + '\n')
                print(colour.BOLD, colour.BLUE, 'Added Used Link To Used List', colour.END)
                #Tweet
                api.update_status(finalTweet)
                #Print Tweet
                print(colour.BOLD, colour.GREEN, 'TWEETED:', finalTweet, colour.END)
                #Wait 14mins 58secs to run again
                time.sleep(898)

#Run Program
testflight_bot()
