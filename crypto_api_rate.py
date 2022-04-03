import requests

# realtime exchange rate for pair of digital currency (e.g., Bitcoin) and physical currency (e.g., USD)
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=OBD3CVJOK6ZZAJ48'
r = requests.get(url)
data = r.json()

exch_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

print('Exchange Rate in USD: ', str(exch_rate))

