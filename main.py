import os

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def message():
    message = request.json['message']
    response = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": message})
    return jsonify(response.json())

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8081))
    app.run(host='0.0.0.0', port=port)

