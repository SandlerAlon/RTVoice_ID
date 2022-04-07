from azure.storage.blob import BlobServiceClient
# from azure.storage.blob.app import AppendBlobService

import json


class AzureBlob:
    def __init__(self):
        self.connect_str = 'DefaultEndpointsProtocol=https;AccountName=voice4identification;AccountKey=AvVM5qTpY+VW0EAN6MTrGqsjmVQ5fsX9il070e36TRfVJW6vzvFyenZeXVAQrnRjUwzPvjYKxjqmekBIGIyS+g==;EndpointSuffix=core.windows.net'
        self.container_name = 'test1'  # 'raw-data'  #
        self.crypto_list_blob = 'crypto_list'
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connect_str)


    # def list_blob_in_container(self, cont_name):
    #     blob_container = self.blob_service_client
    #     blob_list = blob_container.list_blobs()
    #     for blob in blob_list:
    #         print(blob.name)

    def upload_jsonlist_to_blob(self, json_lst, cont_name, blob_name):
        try:
            blob_client = self.blob_service_client.get_blob_client(container=cont_name,
                                                                   blob=blob_name)
            blob_client.upload_blob(json.dumps(json_lst), blob_type="AppendBlob")  # overwrite=False)
            # blob_client.create_append_blob()
            # blob_client.append_blob(json.dumps(json_lst))
        except Exception as e:
            print(e.args)

#   list_blob_in_container(self.container_name)
#   upload_jsonlist_to_blob('test', blob_service_client, self.container_name, self.crypto_list_blob)

