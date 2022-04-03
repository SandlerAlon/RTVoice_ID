from azure.storage.blob import BlobServiceClient
import json


class AzureBlob:
    def __init__(self):
        self.connect_str = 'DefaultEndpointsProtocol=https;AccountName=voice4identification;AccountKey=AvVM5qTpY+VW0EAN6MTrGqsjmVQ5fsX9il070e36TRfVJW6vzvFyenZeXVAQrnRjUwzPvjYKxjqmekBIGIyS+g==;EndpointSuffix=core.windows.net'
        self.container_name = 'raw-data'
        self.crypto_list_blob = 'crypto_list'

    def _get_blob_service_client(conn_str):
        return BlobServiceClient.from_connection_string(conn_str)

    def list_blob_in_container(blob_svc, cont_name):
        blob_container = blob_svc.get_container_client(cont_name)
        blob_list = blob_container.list_blobs()
        for blob in blob_list:
            print(blob.name)

    def upload_jsonlist_to_blob(json_lst, blob_svc, cont_name, blob_name):
        try:
            blob_client = blob_svc.get_blob_client(container=cont_name, blob=blob_name)

            blob_client.upload_blob(json.dumps(json_lst), overwrite=False)
        except Exception as e:
            print(e.args)


blob_service_client = _get_blob_service_client(self.connect_str)
list_blob_in_container(blob_service_client, self.container_name)
upload_jsonlist_to_blob('test', blob_service_client, container_name, crypto_list_blob)
