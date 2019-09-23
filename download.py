from azure.storage.blob import BlobClient

cs = "DefaultEndpointsProtocol=https;AccountName=bizidata001;AccountKey=v37Lm6hqV7hBLrtYarjhS8BJiZmmFyQ4tLA6XzwjUPLkkrlFU3FQxj3FBPzaPTydYiDtSDK0XZM9Lm2dwrZOyg==;EndpointSuffix=core.windows.net"
    
blob = BlobClient.from_connection_string(cs, container="bottledetector", blob="config.ini")

with open("./config.ini", "wb") as my_blob:
    blob_data = blob.download_blob()
    my_blob.writelines(blob_data.content_as_bytes())