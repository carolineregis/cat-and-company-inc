import requests;

import urllib.parse;
import ssl;
 
from flask import Flask, request, jsonify;

# sending request to an API;
response = requests.get("https://http.cat/status/100");
print (response.status_code);

# building a backend
app = Flask(__name__)
@app.route('/process', methods=['POST'])
def process():
  data = request.get_json()
  name = data['name']
  worries = data['worries']

  # here we can process the data or perform
  # any backend tasks

  # here we return a response to front end
  response = {
    "status": "success",
    "message": "data received sucessfully!",
    "diagnosis": ""
  }

  return jsonify(response)

if __name__ == '__main__':
  app.run();
