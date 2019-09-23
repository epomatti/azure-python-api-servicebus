from flask import Flask, request
app = Flask(__name__)

@app.route("/detect", methods=['POST'])
def detect():
    print(request.json)

if __name__ == "__main__":
    app.run()