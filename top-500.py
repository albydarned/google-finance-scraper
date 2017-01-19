
import urllib2
import csv
from bs4 import BeautifulSoup

WIKI = "http://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

def get_tickers(site):
    """return dictionary {industry:[tickers]}"""
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(site, headers=hdr)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page, "html.parser")

    table = soup.find('table', {'class': 'wikitable sortable'})
    sector_tickers = dict()
    for row in table.findAll('tr'):
        col = row.findAll('td')
        if len(col) > 0:
            sector = str(col[3].string.strip()).lower().replace(' ', '_')
            ticker = str(col[0].string.strip())
            if sector not in sector_tickers:
                sector_tickers[sector] = list()
            sector_tickers[sector].append(ticker)
    return sector_tickers

def get_csv(ticker):
    """
    get a csv from google finance for the ticker
    returns a csv reader object
    """
    base = 'https://www.google.com/finance/historical?q='
    options = '&startdate=Jan+1%2C+2001&enddate=Dec+31%2C+2016&num=30&ei=Wcx3WKj4Gcn_jAHphIqQBg'
    filetype = '&output=csv'

    url = base + ticker + options + filetype
    try:
        stock_data = urllib2.urlopen(url)
        return csv.reader(stock_data)
    except Exception as e:
        print "Invalid url: {}".format(url)
        print "Error: {}".format(e)
        return None

def append_csv(filename, industry, ticker):
    """append csv to output.csv with industry and ticker columns added"""
    print "Fetching {} in {} ...".format(ticker, industry)
    cr = get_csv(ticker)
    if cr == None:
        return
    with open(filename, "a") as csvoutput:
        cr = get_csv("AAPL")
        writer = csv.writer(csvoutput, lineterminator="\n")
        all_rows = []
        #top_row = next(cr)
        #top_row.append("TickerSymbol")
        #top_row.append("Industry")
        #all_rows.append(top_row)
        cr.next() #skip the first row
        for row in cr:
            row.append(ticker)
            row.append(industry)
            all_rows.append(row)
        writer.writerows(all_rows)
    print "Appended {} : {} to {}".format(industry, ticker, filename)

def fetch_append_all(filename):
    """fetches all csv's for the top 500 and appends to output.csv"""
    for industry, tickers in get_tickers(WIKI).iteritems():
        print  "Fetching industry: {}".format(industry)
        for ticker in tickers:
            append_csv(filename, industry, ticker)

if __name__ == "__main__":
    fetch_append_all("temp/output.csv")
