# TestFlight Bot
The code for my Twitter bot [@TestFlightBot](https://twitter.com/TestFlightBot)

## This bot is no longer in operation. I'm simply keeping the code around here for safekeeping purposes, and with the hope that it could help somebody one day.
Please note that I haven't tested the code since roughly July 2020, so it may not work at all.

# What did this bot do?
**In a sentence:**
*It Tweets every public TestFlight link in existence. Hopefully.*

**In a more detailed set of sentences:**
This bot, developed in Python and hosted from my Rapsberry Pi, uses [this](https://github.com/tasos-py/Search-Engines-Scraper) Python module to find every public TestFlight beta link, and Tweets it.

The program starts with Google, then uses Startpage, and then Ask. This is to collect the largest amount of public links on the web. All engines use the **site** prefix to find only pages on that website.

Then, it finds every entry on that page and Tweets it. Simple and easy.

I would like to implement a check if the beta is closed / full in the future. That would be pretty easy, but I'm happy with this by now.

I should also mention that Tweepy is used to Tweet the final output.
