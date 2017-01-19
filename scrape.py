import urllib2
import csv
import os
import shutil
import sys
import subprocess

if not os.path.exists('temp'):
    os.makedirs('temp')
    os.makedirs('temp\\orig')
    os.makedirs('temp\\tick')
    os.makedirs('temp\\ind')
    os.makedirs('temp\\rem')
else:
    print "Temp directory already exists! Move or delete temp directory and run again."
    sys.exit()


wd = os.path.dirname(__file__)

base = 'https://www.google.com/finance/historical?q='
options = '&startdate=Jun+2%2C+2016&enddate=Dec+31%2C+2016&num=30&ei=Wcx3WKj4Gcn_jAHphIqQBg'
format = '&output=csv'

tickers = ['AAPL', 'AMZN', 'BBY', 'BKS', 'BP', 'C', 'CBS', 'CMCSA', 'COP', 'COST', 'DIS', 'F', 'GE', 'GM', 'GT', 'HON', 'HPQ', 'HSY', 'INTC', 'IPG', 'JBLU', 'JMBA', 'JWN', 'KMX', 'KO', 'LUV', 'MAR', 'MCD', 'MGM', 'MSFT', 'NKE', 'OCR', 'ORCL', 'PG', 'RL', 'SBUX', 'SHW', 'STR', 'TGT', 'TWX', 'WFC', 'WFM', 'WMT', 'XOM']
industries = ['Tech', 'Internet Services', 'Retail', 'Retail', 'Oil and Gas', 'Money', 'Entertainment', 'Television', 'Oil and Gas', 'Retail', 'Entertainment', 'Automotive', 'Electric', 'Auto Manufacturers', 'Automotive', 'Aerospace', 'Tech', 'Food', 'Tech', 'Advertising', 'Airlines', 'Food', 'Retail', 'Automotive', 'Food', 'Airline', 'Hotels/Resorts', 'Food', 'Hotels and Resorts', 'Tech', 'Retail', 'Healthcare', 'Tech', 'Household Products', 'Retail', 'Beverages', 'Chemicals', 'Gas/Oil', 'Retail', 'Entertainment', 'Money', 'Food', 'Retail', 'Oil and Gas']



for ticker in tickers:
    url = base + ticker + options + format
    name = ticker + '.csv'
    print ticker
    stock_data = urllib.URLopener()
    stock_data.retrieve(url, "temp/orig/" + name)
    print "OK \n"



i = 0
while i < len(tickers):
    ticker = tickers[i]
    name_in = 'temp\\orig\\' + ticker + '.csv'
    name_out = 'temp\\tick\\' + ticker + '-tick.csv'

    with open(name_in, 'r') as csvinput:
        with open(name_out, 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)

            all = []
            row = next(reader)
            row.append('TickerSymbol')
            all.append(row)

            for row in reader:
                row.append(ticker)
                all.append(row)

            writer.writerows(all)
    i = i + 1

i = 0
while i < len(industries):
    name = tickers[i]
    industry = industries[i]
    name_in = 'temp\\tick\\' + name + '-tick.csv'
    name_out = 'temp\\ind\\' + name + '.csv'

    with open(name_in, 'r') as csvinput:
        with open(name_out, 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)

            all = []
            row = next(reader)
            row.append('Industry')
            all.append(row)

            for row in reader:
                row.append(industry)
                all.append(row)

            writer.writerows(all)
    i = i + 1

i = 0
while i < len(industries):
    name = tickers[i]
    industry = industries[i]
    name_in = 'temp\\ind\\' + name + '.csv'
    name_out = 'temp\\rem\\' + name + '-rem.csv'

    with open(name_in,'r') as f_input:
        with open(name_out,'w') as f_output:
            f_input.next() # skip header line
            for line in f_input:
                f_output.write(line)

    i = i + 1

print "Script success!"
print "Run \'copy temp\\rem\\*.csv merged.csv\' from this directory to merge all the files into one."
print "Headers and additional formatting may be necessary."
