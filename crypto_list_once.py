from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

import json

# from azure_blob import AzureBlob


class CryptoApis:
    def __init__(self):
        self._set_params()
        self.startBatch = 1

    def _set_params(self):
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        self.headers = {
                      'Accepts': 'application/json',
                      'X-CMC_PRO_API_KEY': '9ee28416-43a1-437d-97de-43d385c8df2d',
                    }
        self.end_batch = 20
        self.limit_batch = 5

    def set_url_parameter(self, start_batch):
        parameters = {
            'start': start_batch,
            'limit': self.limit_batch,
            'convert': 'USD',
            'price_max': 1
        }
        return parameters

    def retrieve_crypto_list(self):
        session = Session()
        session.headers.update(self.headers)
        try:
            cont_list = True
            batch_min_id = self.startBatch
            crypto_lst = []
            while cont_list and batch_min_id < self.end_batch:
                param = self.set_url_parameter(batch_min_id)
                response = session.get(self.url, params=param)
                data = json.loads(response.text)
                if data:
                    print(batch_min_id, len(data))
                    crypto_lst.extend(data['data'])
                    batch_min_id += self.limit_batch
                else:
                    cont_list = False
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
        print('asd')


if __name__ == '__main__':
    CryptoApis.retrieve_crypto_list()
    # AzureBlob.upload_jsonlist_to_blob()
