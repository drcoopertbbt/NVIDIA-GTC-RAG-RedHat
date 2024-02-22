# First stage: build the Node.js application
FROM node:14 as node-builder

WORKDIR /node-app
COPY ./frontend/package*.json ./
RUN npm install
COPY ./frontend/ ./
RUN npm run build

# Second stage: build the Python application
FROM registry.redhat.io/ubi8/python-311 as python-builder

# Copy your application's source code
COPY ./src /app

# Copy your application's data
COPY ./data /data

# Install your application's Python dependencies
WORKDIR /app
RUN pip install -r requirements.txt

# Copy the built Node.js application from the first stage
COPY --from=node-builder /node-app/build /app/node-app

# The run script uses standard ways to run the application
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]