from azure.storage.blob import BlobClient
from config import get_config

def download(file):
    connection_string = get_config('AZURE', 'STORAGE_CONNECTION_STRING')
    container_name = get_config('AZURE', 'STORAGE_CONTAINER')

    blob = BlobClient.from_connection_string(
        conn_str=connection_string, container_name=container_name, blob_name=file)

    local_file = "./files/{}".format(file)
    with open(local_file, "wb") as my_blob:
        blob_data = blob.download_blob()
        my_blob.write(blob_data.content_as_bytes())


def upload(local_file, remote_file_name):
    connection_string = get_config('AZURE', 'STORAGE_CONNECTION_STRING')
    container_name = get_config('AZURE', 'STORAGE_CONTAINER')

    blob = BlobClient.from_connection_string(
        conn_str=connection_string, container_name=container_name, blob_name=remote_file_name)

    with open(local_file, "rb") as data:
        blob.upload_blob(data)


def delete(blob_name):
    connection_string = get_config('AZURE', 'STORAGE_CONNECTION_STRING')
    container_name = get_config('AZURE', 'STORAGE_CONTAINER')

    blob = BlobClient.from_connection_string(
        conn_str=connection_string, container_name=container_name, blob_name=blob_name)
    blob.delete_blob()
