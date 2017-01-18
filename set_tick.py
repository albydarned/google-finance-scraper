import csv

tickers = ['AAPL', 'AMZN', 'BBY', 'BKS', 'BP', 'C', 'CBS', 'CMCSA', 'COP', 'COST', 'DIS', 'F', 'GE', 'GM', 'GT', 'HON', 'HPQ', 'HSY', 'INTC', 'IPG', 'JBLU', 'JMBA', 'JWN', 'KMX', 'KO', 'LUV', 'MAR', 'MCD', 'MGM', 'MSFT', 'NKE', 'OCR', 'ORCL', 'PG', 'RL', 'SBUX', 'SHW', 'STR', 'TGT', 'TWX', 'WFC', 'WFM', 'WMT', 'XOM']
industries = ['Tech', 'Internet Services', 'Retail', 'Retail', 'Oil and Gas', 'Money', 'Entertainment', 'Television', 'Oil and Gas', 'Retail', 'Entertainment', 'Automotive', 'Electric', 'Auto Manufacturers', 'Automotive', 'Aerospace', 'Tech', 'Food', 'Tech', 'Advertising', 'Airlines', 'Food', 'Retail', 'Automotive', 'Food', 'Airline', 'Hotels/Resorts', 'Food', 'Hotels and Resorts', 'Tech', 'Retail', 'Healthcare', 'Tech', 'Household Products', 'Retail', 'Beverages', 'Chemicals', 'Gas/Oil', 'Retail', 'Entertainment', 'Money', 'Food', 'Retail', 'Oil and Gas']

i = 0
while i < len(tickers):
    ticker = tickers[i]
    name_in = ticker + '.csv'
    name_out = ticker + '-tick.csv'

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
