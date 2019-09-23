from configparser import ConfigParser
from azure.storage.blob import BlobClient

parser = ConfigParser()
parser.read('config.ini')
connection_string = parser.get('AZURE', 'STORAGE_CONNECTION_STRING')
container_name = parser.get('AZURE', 'STORAGE_CONTAINER')
    
blob = BlobClient.from_connection_string(connection_string, container=container_name, blob="output.json")

with open("./output.json", "wb") as my_blob:
    blob_data = blob.download_blob()
    my_blob.write(blob_data.content_as_bytes())