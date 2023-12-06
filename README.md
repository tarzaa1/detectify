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
