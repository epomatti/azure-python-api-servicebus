from configparser import ConfigParser
from azure.servicebus import QueueClient, Message

def enqueue(message):
    parser = ConfigParser()
    parser.read('config.ini')
    queue_name = parser.get('AZURE', 'SERVICE_BUS_QUEUE_NAME')
    connection_string = parser.get('AZURE', 'SERVICE_BUS_CONNECTION_STRING')

    # Create the QueueClient
    queue_client = QueueClient.from_connection_string(
        connection_string, queue_name)

    # Send a test message to the queue
    msg = Message(message)
    queue_client.send(msg)