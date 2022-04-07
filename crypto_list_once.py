from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

import json

from azure_blob import AzureBlob


class CryptoApis:
    def __init__(self):
        self._set_params()

    def _set_params(self):
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        self.headers = {
                      'Accepts': 'application/json',
                      'X-CMC_PRO_API_KEY': '9ee28416-43a1-437d-97de-43d385c8df2d',
                    }
        self.start_batch = 1
        self.num_of_batches = 50
        self.batch_size = 200

    def set_url_parameter(self, start_batch):
        parameters = {
            'start': start_batch,
            'limit': self.batch_size,
            'convert': 'USD',
            'market_cap_min': 5000000000
        }
        return parameters

    def retrieve_crypto_list(self):
        session = Session()
        session.headers.update(self.headers)
        try:
            cont_list = True
            batch_min_id = self.start_batch
            batch_cnt = 0
            crypto_lst = []

            data = {}
            data['data'] = []
            data['data'] = [{"id": 1, "name": "Bitcoin", "symbol": "BTC"},{"id": 2010, "name": "Cardano", "symbol": "ADA"}]
            azureInst.upload_jsonlist_to_blob(data['data'],
                                              azureInst.container_name,
                                              azureInst.crypto_list_blob)

            data['data'] = [{"id": 3717, "name": "Wrapped Bitcoin", "symbol": "WBTC"},{"id": 1975, "name": "Chainlink", "symbol": "LINK"}]
            azureInst.upload_jsonlist_to_blob(data['data'],
                                              azureInst.container_name,
                                              azureInst.crypto_list_blob)

            # while 'data' in data:  # cont_list # and batch_cnt < self.num_of_batches:
            #     # param = self.set_url_parameter(batch_min_id)
            #     # response = session.get(self.url, params=param)
            #     # data = json.loads(response.text)
            #     if 'data' in data:
            #         print(batch_min_id, len(data))
            #         # crypto_lst.extend(data['data'])
            #         batch_min_id += self.batch_size
            #         azureInst.upload_jsonlist_to_blob(data['data'],
            #                                           azureInst.container_name,
            #                                           azureInst.crypto_list_blob)
            #         batch_cnt += 1
            #     else:
            #         cont_list = False
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)


if __name__ == '__main__':
    crypto_inst = CryptoApis()
    azureInst = AzureBlob()
    crypto_inst.retrieve_crypto_list()
