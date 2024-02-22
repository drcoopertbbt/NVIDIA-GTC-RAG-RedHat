from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # Import CORS
import requests
import json
import os
from datetime import datetime

app = Flask(__name__, static_folder='node-app')
CORS(app)  # Enable CORS on the Flask app

@app.route('/ask', methods=['POST'])
def ask():
  # Triton Inference Service Endpoint
  API_URL = "http://triton-inference-service.edge-inference.svc.cluster.local:8000/v2/models/llamav2/infer"
  
  # Extract prompt from the incoming request
  prompt_data = request.json.get('prompt', '')

  # Save the prompt data to a file in /data/prompt-data
  prompt_data_filename = os.path.join('/data/prompt-data', f'prompt_{datetime.now().strftime("%Y%m%d%H%M%S")}.json')
  with open(prompt_data_filename, 'w') as file:
    json.dump({'prompt': prompt_data}, file, indent=4)
  
  # Define the headers and data for the API request to Triton
  headers = {"Content-Type": "application/json"}
  data = {
    "inputs": [
      {
        "name": "prompt",
        "shape": [1],
        "datatype": "BYTES",
        "data": [prompt_data]
      }
    ]
  }
  
  # Make the API request to the Triton inference service
  response = requests.post(API_URL, headers=headers, json=data)
  
  # Parse the response
  response_data = response.json()

  # Save the response data to a file in /data/response-data
  response_data_filename = os.path.join('/data/response-data', f'response_{datetime.now().strftime("%Y%m%d%H%M%S")}.json')
  with open(response_data_filename, 'w') as file:
    json.dump(response_data, file, indent=4)
  
  return jsonify(response_data)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
  if path != "" and os.path.exists(app.static_folder + '/' + path):
    return send_from_directory(app.static_folder, path)
  else:
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)