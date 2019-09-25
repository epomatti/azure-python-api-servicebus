from storage import download, delete
from servicebus import dequeue_loop, enqueue
import os
import json

def callback(message):
    json_msg = json.loads(message.__str__())    
    file = json_msg['filename']
    print(file)
    download(file)
    enqueue('processou', 'SERVICE_BUS_OUTPUT_QUEUE')
    os.remove(file)

dequeue_loop(callback)