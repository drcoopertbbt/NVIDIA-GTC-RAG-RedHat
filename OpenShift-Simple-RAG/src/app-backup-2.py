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

    # Pretty-print the JSON data
    pretty_json = json.dumps(response_data, indent=4)

    # Define a simple HTML template with MDB styling
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <!-- Google Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" rel="stylesheet">
        <!-- MDB -->
        <link href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/7.1.0/mdb.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container my-5">
            <h1 class="mb-5">Hello, from NVIDIA NVAIE - Triton Inference Server on Red Hat OpenShift</h1>
            <pre class="border rounded bg-light p-3">{{ pretty_json }}</pre>
        </div>
    </body>
    </html>
    """

    # Render the template with the pretty-printed JSON data
    return render_template_string(template, pretty_json=pretty_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)