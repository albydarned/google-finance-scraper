import urllib

base = 'https://www.google.com/finance/historical?q='
options = '&startdate=Jun+2%2C+2016&enddate=Dec+31%2C+2016&num=30&ei=Wcx3WKj4Gcn_jAHphIqQBg'
csv = '&output=csv'

tickers = ['AAPL', 'AMZN', 'BBY', 'BKS', 'BP', 'C', 'CBS', 'CMCSA', 'COP', 'COST', 'DIS', 'F', 'GE', 'GM', 'GT', 'HON', 'HPQ', 'HSY', 'INTC', 'IPG', 'JBLU', 'JMBA', 'JWN', 'KMX', 'KO', 'LUV', 'MAR', 'MCD', 'MGM', 'MSFT', 'NKE', 'OCR', 'ORCL', 'PG', 'RL', 'SBUX', 'SHW', 'STR', 'TGT', 'TWX', 'WFC', 'WFM', 'WMT', 'XOM']
print "Fetching ", len(tickers), " files"

for ticker in tickers:
    url = base + ticker + options + csv
    name = ticker + '.csv'
    print ticker
    stock_data = urllib.URLopener()
    stock_data.retrieve(url, name)
    print "OK \n"

