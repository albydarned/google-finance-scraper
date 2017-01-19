# google-finance-scraper
A simple python program that scrapes historical data of a certain stock from Google Finance in a given time period.

scrape.py fetches the historical stock data indicated in the "tickers" list from Google Finance and then appends the ticker symbol and industry category. The step by step actions on the files downloaded are stored in directories nested in "temp"

top-500.py fetches the historical stock data from the S&P 500 (Scrapes the data from http://en.wikipedia.org/wiki/List_of_S%26P_500_companies) and concatenates/appends them to a file titled "output.csv"
