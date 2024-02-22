#!/bin/bash

# Set the tag to the current timestamp
export TAG=$(date +%s)
echo "TAG is set to $TAG"

# Build the Docker image
podman build -t mwc-genai-my-apache-ubi8 .

# Tag the Docker image
podman tag mwc-genai-my-apache-ubi8 quay.io/marzquay/mwc-genai-my-apache-ubi8:$TAG

# Push the Docker image to the registry
podman push quay.io/marzquay/mwc-genai-my-apache-ubi8:$TAG

# Replace the $TAG variable in the deployment.yaml file and apply the configuration
envsubst < deployment.yaml | oc apply -f -
echo "Applied deployment.yaml with TAG=$TAG"

# Apply the Service
oc apply -f service.yaml
echo "Applied service.yaml"

# Apply the route
oc apply -f route.yaml
echo "Applied route.yaml"