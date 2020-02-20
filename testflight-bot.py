#Import Libraries
import urllib.request, urllib.error, urllib.parse
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
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:65.0) Gecko/20100101 Firefox/65.0"

#Define query and URL
query = "site:testflight.apple.com"
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}"

#Define main code - this was a function so it could relaunch itself when a condition was made, but I scrapped that idea and couldn't be bothered with changing indentation again. Have a nice day.
def testflight_bot():
    #Get results from Google
    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)

    #Check if response status code is 200
    if resp.status_code == 200:
        #Define soup
        soup = BeautifulSoup(resp.content, "html.parser")
        #Define results list
        results = []
        #Start for loop
        for g in soup.find_all('div', class_='r'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text
                #Define page title and URL
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
            betaCode = str(betaCode)
            #Print beta code
            print(colour.BOLD, colour.YELLOW, 'Beta Code:', betaCode, colour.END)
            print(colour.BOLD, colour.RED, 'Found genuine TestFlight link', colour.END)
            #Print title and URL
            print(colour.BOLD, colour.PURPLE, 'TITLE:', title, colour.END)
            print(colour.BOLD, colour.PURPLE, 'URL:', link, colour.END)
            #Check If Beta Is Full
            #Get webpage source code
            response = urllib.request.urlopen(link)
            webContent = response.read()
            #Define text that will be displayed if the beta link is valid
            workingBetaLinkText = str('To join the ' + title + ', tap the link on your iPhone or iPad after you install TestFlight.')
            print(colour.BOLD, workingBetaLinkText, colour.END)
            #Make webContent a string so it can be easily searched
            webContent = str(webContent)
            #Create final Tweet - add title and link
            tweet = title + ': ' + link
            #Open used file to write to
            usedWrite = open('used.txt', 'a')
            #Get data to write to file
            usedWriteText = betaCode + '||' + title + '\n'
            #Write data to file
            usedWrite.write(usedWriteText)
            print(colour.BOLD, colour.BLUE, 'Added Used Link To Used List', colour.END)
            #Check if page contains 'to join' text
            if workingBetaLinkText in webContent:
                #Open used file to read from
                with open('used.txt') as usedRead:
                    #Check if previously written text is in file
                    #(this is weird because it is written already for this current 'run', so it should always be true - but this code works and that's all I care about)
                    if usedWriteText in usedRead:
                        print(colour.BOLD, colour.RED, 'Beta already Tweeted, restarting...', colour.END)
                        print(tweet)
                        #Return to start of for loop
                        continue
                #Tweet
                try:
                    api.update_status(tweet)
                #Just in case something goes wrong...
                except:
                    print(colour.BOLD, colour.RED, 'Something went wrong with the Tweet. Moving to the next link...', colour.END)
                    #Print divider to make the output beautiful
                    print('-----------------------------------------')
                    continue
                #Print Tweet
                print(colour.BOLD, colour.GREEN, 'TWEETED:', tweet, colour.END)
                #Print divider to make the output beautiful
                print('-----------------------------------------')
                #Wait 14mins 58secs to run again
                time.sleep(898)
            #Check if the betaCode is the TestFlight home page - this shouldn't work as the URL is removed when betaCode is created, but again it does work so I don't care
            elif betaCode == 'https://testflight.apple.com/':
                print(colour.RED, colour.BOLD, 'TestFlight home page, restarting...', colour.END)
                #Print divider to make the output beautiful
                print('-----------------------------------------')
                #Return to start of for loop
                continue
            #If it's not a verified link and if it's not the TF home page, it's probably a closed/full beta
            else:
                print(colour.RED, colour.BOLD, 'Found beta link that doesn\'t work', colour.END)
                #Add full to beta - this ideallly would check if the webpage says 'beta full' or 'beta not accepting testers' but that wouldn't work for some strange reason (these darn computers)
                tweet = '[FULL] ' + tweet
                #Tweet
                try:
                    api.update_status(tweet)
                #Just in case something goes wrong...
                except:
                    print(colour.BOLD, colour.RED, 'Something went wrong with the Tweet. Moving to the next link...', colour.END)
                    #Print divider to make the output beautiful
                    print('-----------------------------------------')
                    #Return to start of loop
                    continue
                #Print Tweet
                print(colour.BOLD, colour.GREEN, 'TWEETED:', tweet, colour.END)
                #Wait 14mins 58secs to run again
                time.sleep(898)
                #Return to start of loop
                continue
                

#Run Program
testflight_bot()
