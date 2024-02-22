from flask import Flask, render_template_string
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    # Define the API endpoint
    API_URL = "http://triton-inference-service.edge-inference.svc.cluster.local:8000/v2/models/llamav2/infer"

    # Define the headers for the API request
    headers = {"Content-Type": "application/json"}

    # Define the data for the API request
    data = {
      "inputs": [
        {
          "name": "prompt",
          "shape": [1],
          "datatype": "BYTES",
          "data": ["What is Red Hat OpenShift?"]
        }
      ]
    }

    # Make the API request
    response = requests.post(API_URL, headers=headers, json=data)

    # Parse the response
    response_data = response.json()

    # Define a simple HTML template
    template = """
    <h1>Hello, from NVIDIA NVAIE - Triton Inference Server on Red Hat OpenShift</h1>
    <pre>{{ response_data | tojson(indent=4) }}</pre>
    """

    # Render the template with the response data
    return render_template_string(template, response_data=response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)