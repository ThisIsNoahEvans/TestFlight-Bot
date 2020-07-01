# TestFlight Bot
The code for my Twitter bot [@TestFlightBot](https://twitter.com/TestFlightBot)

# What does this bot do?
**In a sentence:**
*It Tweets every public TestFlight link in existence. Hopefully.*

**In a more detailed set of sentences:**
This bot, developed in Python and hosted from my Rapsberry Pi, uses [this](https://github.com/tasos-py/Search-Engines-Scraper) Python module to find every public TestFlight beta link, and Tweets it.

The program starts with Google, then uses Startpage, and then Ask. This is to collect the largest amount of public links on the web. All engines use the **site** prefix to find only pages on that website.

Then, it finds every entry on that page and Tweets it. Simple and easy.

I would like to implement a check if the beta is closed / full in the future. That would be pretty easy, but I'm happy with this by now.

I should also mention that Tweepy is used to Tweet the final output.

# Please Note
Don't steal this code and make another Twitter bot doing the same thing because....why? Feel free to fork this project and use the source code for anything else, but you might as well go straight to the [module](https://github.com/tasos-py/Search-Engines-Scraper) as there isn't much code specific to the TestFlight bot here. It literally runs a request through a module and Tweets the output.
