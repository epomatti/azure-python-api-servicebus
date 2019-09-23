from azure.servicebus import QueueClient, Message
from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.ini')
connection_string = parser.get('AZURE', 'SERVICE_BUS_CONNECTION_STRING')
queue_name = parser.get('AZURE', 'SERVICE_BUS_QUEUE_NAME')

# Create the QueueClient
queue_client = QueueClient.from_connection_string(
    connection_string, queue_name)

# Receive the message from the queue
with queue_client.get_receiver() as queue_receiver:
    messages = queue_receiver.fetch_next(timeout=3)
    for message in messages:
        print(message)
        message.complete()
