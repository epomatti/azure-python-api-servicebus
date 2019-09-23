# Python API

## Infrastructure

You'll need a storage account with a blob container, and a Service Bus with a queue.

```
az storage account create -n MyStorageAccountName -g MyResourceGroupName
az servicebus namespace create -n MyServiceBusName -g MyResourceGroupName
```

## Application

Prepare environment:

```
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install python3-venv
```

Install dependencies:

```
pip3 install pylint
python3 -m venv env
pip3 install -r requirements.txt
pip3 install azure-storage-blob --pre
```

Run it:

```
python3 start.py
```

## References

[Azure Storage Blobs client library for Python](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob)

[How to use Service Bus queues with Python](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-python-how-to-use-queues)