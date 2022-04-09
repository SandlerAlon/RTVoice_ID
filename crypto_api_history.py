import requests

#  daily historical time series for a digital currency (e.g., BTC) traded on USD (may give another market)
url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=OBD3CVJOK6ZZAJ48'
r = requests.get(url)
data = r.json()
# TODO save where ?
print(data["Time Series (Digital Currency Daily)"]['2022-04-02']['4a. close (USD)'])


