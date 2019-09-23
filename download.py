from configparser import ConfigParser
from azure.storage.blob import BlobClient

parser = ConfigParser()
parser.read('config.ini')
connection_string = parser.get('AZURE', 'STORAGE_CONNECTION_STRING')
    
blob = BlobClient.from_connection_string(connection_string, container="bottledetector", blob="config.ini")

with open("./config.ini", "wb") as my_blob:
    blob_data = blob.download_blob()
    my_blob.writelines(blob_data.content_as_bytes())