from configparser import ConfigParser
from azure.storage.blob import BlobClient


def download(file):
    parser = ConfigParser()
    parser.read('config.ini')
    connection_string = parser.get('AZURE', 'STORAGE_CONNECTION_STRING')
    container_name = parser.get('AZURE', 'STORAGE_CONTAINER')

    blob = BlobClient.from_connection_string(
        connection_string, container=container_name, blob=file)
    
    local_file = "./files/{}".format(file)
    with open(local_file, "wb") as my_blob:
        blob_data = blob.download_blob()
        my_blob.write(blob_data.content_as_bytes())


def upload(local_file, remote_file_name):
    parser = ConfigParser()
    parser.read('config.ini')
    connection_string = parser.get('AZURE', 'STORAGE_CONNECTION_STRING')
    container_name = parser.get('AZURE', 'STORAGE_CONTAINER')

    blob = BlobClient.from_connection_string(
        connection_string, container=container_name, blob=remote_file_name)

    with open(local_file, "rb") as data:
        blob.upload_blob(data)

def delete(blob_name):
    parser = ConfigParser()
    parser.read('config.ini')
    connection_string = parser.get('AZURE', 'STORAGE_CONNECTION_STRING')
    container_name = parser.get('AZURE', 'STORAGE_CONTAINER')

    blob = BlobClient.from_connection_string(
        connection_string, container=container_name, blob=blob_name)
    blob.delete_blob()