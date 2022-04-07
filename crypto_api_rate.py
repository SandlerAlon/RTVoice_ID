# realtime exchange rate for pair of digital currency (e.g., Bitcoin) and physical currency (e.g., USD)
import requests


class CryptoApiRate:
    def __init__(self):
        self._set_params()

    def _set_params(self):
        self.apikey = 'OBD3CVJOK6ZZAJ48'
        self.url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'

    def retrieve_crypto_rate(self, crypto):
        url = f'{self.url}&from_currency={crypto}&to_currency=USD&apikey={self.apikey}'
        r = requests.get(url)
        data = r.json()
        exch_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
        #TODO return RDD
        return exch_rate


