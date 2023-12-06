# Detectify

A simple Flask app with a single endpoint that receives a POST request containing a photo and returns the bounding boxes of objects detected inside the image. The purpose of this repository is to learn how to deploy such an application in a Kubernetes cluster.

## Table of Contents

- [Run with Docker](#Docker)
- [Run in Kubernetes](#Kubernetes)

## Docker

1. Build docker image:

    ```bash
    docker build -t detectify:v1.0 .
    ```

2. Run in a container:

    ```bash
    docker compose up -d 
    ```

3. Install dependencies:

    ```bash
    python scripts/upload.py
    ```

## Kubernetes

1. Create ConfigMap:

    ```bash
    kubectl create -f detectify_configmap.yaml
    ```

2. Create Deployment:

    ```bash
    kubectl create -f detectify_deployment.yaml
    ```

3. Create Service:

    ```bash
    kubectl create -f detectify_service.yaml
    ```

4. Create Service:

Wait until all pods are running, you can check their status with:

    ```bash
    kubectl get all
    ```

Once pods are running, get the ip address of the service:

    ```bash
    kubectl describe service <service name>
    ```

Finally, replace the ip address in scripts/upload.py with that of the service and run the script:

    ```bash
    python scripts/upload.py
    ```
