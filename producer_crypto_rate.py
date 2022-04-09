# realtime exchange rate for pair of digital currency (e.g., Bitcoin) and physical currency (e.g., USD)
import requests

from time import sleep
from random import random

from pyspark import SparkContext


class CryptoApiRate:
    def __init__(self):
        self._set_params()
        self.sc = SparkContext.getOrCreate()

    def _set_params(self):
        self.apikey = 'OBD3CVJOK6ZZAJ48'
        self.url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'

    def retrieve_crypto_rate(self, crypto):
        url = f'{self.url}&from_currency={crypto}&to_currency=USD&apikey={self.apikey}'
        r = requests.get(url)
        data = r.json()
        if 'Realtime Currency Exchange Rate' in data:
            exch_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        else:
            exch_rate = [-1]

        exch_rdd = self.sc.parallelize(exch_rate).take(1)
        return exch_rdd.take(1)


