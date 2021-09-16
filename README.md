# Web-Scraping-Bot-Quotes-to-Scrape-
A data collection bot from https://quotes.toscrape.com using python.

# What it does?
This bot collects all quotes from an author in addition to collecting their personal information. (output: print on terminal)

# How to run?
Download the repository.
Make sure you have python3.6.x or superiror installed.
Make sure you have the "urllib", "selenium" and "json" libraries.
Regarding selenium: this bot uses the Chrome webdriver, make sure you have it or change it to the one of your choice (line 5 main.py).

# Configuration
The "conf.json" file is responsible for some settings:
If you want to change the author, just put a new name in "author".
If you want the bot not to use all pages on the site (maximum and default = 10), just change "pages_number".
