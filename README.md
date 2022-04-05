# Python API - Service Bus, Blob Storage

A sample Python API using Flask to integrate with Azure Storage and Azure Service Bus.

## Infrastructure

You'll need a storage account with a blob container, and a Service Bus with a queue.

```sh
group='rg-myproj'
location='eastus2'
storage='stmyproj'
namespace='bus-myproj'

az group create -n $group -l $location
az storage account create -n $storage -g $group -l $location
az storage container create -n 'files' --account-name $storage

az servicebus namespace create -n $namespace -g $group -l $location
az servicebus queue create -n 'inQueue' --namespace-name $namespace -g $group
az servicebus queue create -n 'outQueue' --namespace-name $namespace -g $group
```

## Running it


Install dependencies:

```sh
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

Create the configurations file and temp directory:

```sh
mkdir files
cp example.config.ini config.ini
```

Generate the data and serve the application:

```sh
# Generate the sample data
python3 src/data_generator.py

# Run the program
python3 src/main.py
```

With Docker:

```sh
docker build -t python-api .
docker run -it --rm --name python-api python-api
```
