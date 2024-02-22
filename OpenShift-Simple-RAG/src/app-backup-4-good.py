from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    # Triton Inference Service Endpoint
    API_URL = "http://triton-inference-service.edge-inference.svc.cluster.local:8000/v2/models/llamav2/infer"
    
    # Extract prompt from the incoming request
    # Expecting JSON payload with a 'prompt' field
    prompt_data = request.json.get('prompt', '')
    
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
    
    # Parse and return the response
    response_data = response.json()
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
