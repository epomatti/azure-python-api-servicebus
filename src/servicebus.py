from azure.servicebus import ServiceBusClient, ServiceBusMessage
from config import get_config


def enqueue(message, queue_param_name):
    connection_string = get_config('AZURE', 'SERVICE_BUS_CONNECTION_STRING')
    queue_name = get_config('AZURE', queue_param_name)

    with ServiceBusClient.from_connection_string(connection_string) as client:
        with client.get_queue_sender(queue_name) as sender:
            # Sending a single message
            single_message = ServiceBusMessage(message)
            sender.send_messages(single_message)


def dequeue():
    connection_string = get_config('AZURE', 'SERVICE_BUS_CONNECTION_STRING')
    queue_name = get_config('AZURE', 'SERVICE_BUS_INPUT_QUEUE')

    with ServiceBusClient.from_connection_string(connection_string) as client:
        with client.get_queue_receiver(queue_name, max_wait_time=30) as receiver:
            for msg in receiver:  # ServiceBusReceiver instance is a generator.
                print(str(msg))


def dequeue_loop(callback):
    connection_string = get_config('AZURE', 'SERVICE_BUS_CONNECTION_STRING')
    queue_name = get_config('AZURE', 'SERVICE_BUS_INPUT_QUEUE')

    with ServiceBusClient.from_connection_string(connection_string) as client:
        with client.get_queue_receiver(queue_name, max_wait_time=30) as receiver:
            for msg in receiver:  # ServiceBusReceiver instance is a generator.
                callback(msg)
