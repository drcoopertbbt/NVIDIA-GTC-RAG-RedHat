#!/bin/bash

# Apply the ConfigMap
oc apply -f configmap.yaml
echo "Applied configmap.yaml"

# Apply the Deployment
oc apply -f deployment.yaml
echo "Applied deployment.yaml"

# Apply the Service
oc apply -f service.yaml
echo "Applied service.yaml"

# Apply the route
oc apply -f route.yaml
echo "Applied route.yaml"