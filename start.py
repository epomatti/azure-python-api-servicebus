from flask import Flask, request
from azure.storage.blob import BlobClient
from enqueue import enqueue
app = Flask(__name__)

@app.route("/detect", methods=['POST'])
def detect():
    enqueue('my message')
    return 'OK'
    
if __name__ == "__main__":
    app.run()