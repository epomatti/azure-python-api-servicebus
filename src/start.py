from flask import Flask, request
from azure.storage.blob import BlobClient
from servicebus import enqueue
app = Flask(__name__)

@app.route("/detect", methods=['POST'])
def detect():
    enqueue('my message', 'SERVICE_BUS_INPUT_QUEUE')
    return 'OK'
    
if __name__ == "__main__":
    app.run()