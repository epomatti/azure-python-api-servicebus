from storage import download
from servicebus import dequeue_loop, enqueue
import os
import json

def callback(message):
    data = next(message.body)
    print(data)
    json_msg = json.loads(data)    
    file = json_msg['filename']
    download(file)
    enqueue('processed', 'SERVICE_BUS_OUTPUT_QUEUE')
    os.remove('./files/{}'.format(file))

dequeue_loop(callback)