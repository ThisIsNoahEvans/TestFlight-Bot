# TestFlight Bot
The code for my Twitter bot [@TestFlightBot](https://twitter.com/TestFlightBot)

# What does this bot do?
**In a sentence:**
*It Tweets every public TestFlight link in existence.*

**In a more detailed set of sentences:**
This bot, developed in Python and hosted from my Rapsberry Pi (for now), uses Google Search to find every public TestFlight beta link, and Tweets it.

The program visits [this Google Search](https://www.google.com/search?q=site:testflight.apple.com) which uses Google's **site** prefix to find only pages on that website. For example, if you searched for *site:itsnoahevans.co.uk* you'd find every page, even on subdomains, on that domain. [Try it.](https://www.google.com/search?q=site:itsnoahevans.co.uk)

Then, it finds every entry on that page and works with it. *(The current code only looks through the first page of the search, but I will be fixing that and relaunching the bot soon.)*

The title and link are saved to a variable. The program next visits the TestFlight page and tries to look for some text. It adds the beta app name - which it finds from the title on Google - to the sentence displayed at the top of the TestFlight page (if the beta is accepting testers / not full). If that text is found, it Tweets the beta app name and the URL. If the text can't be found, it first checks to see if the page is TestFlight's home page (testflight.apple.com). If that's the case, it moves to the next URL on the Google Search page. If the text is not found on the TestFlight web page and the URL is not TestFlight's home page, it adds *[FULL]* to the front of the Tweet, and Tweets as normal. Some beta web pages do say *'This beta is full'*, but others say *'This beta isn't accepting any new testers right now.'*. I did want the program to check if the page says 'full' or 'isn't accepting', but that wouldn't work for some very strange reason (it should be almost the same code?!). It also checks if the beta has been Tweeted before, although this is not necessary unless the program has been restarted from a crash.

I should also mention that Tweepy is used to Tweet the final output.

# Thanks To
**Google** for existing. The amazing search part of it, not the creepy side that stalks everything you do on the internet. Well, I guess Search does stalk you too...

**GetLinkSC** for creating [this repository](https://github.com/getlinksc/scrape_google) which provided the basis of the code for getting Google Search results into Python.

**PythonProgramming.net** for the article/video explaining how to get the source code of the web page into Python ([here](https://pythonprogramming.net/parse-website-using-regular-expressions-urllib))

**The people of Twitter** I can't name everyone, but a handful of people helped with small issues via my Tweets.
