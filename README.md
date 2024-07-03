# Hackett App

This project is a Python application that runs inside a Docker container.

## Prerequisites

- Docker installed on your machine.

## Getting Started

Follow these steps to build and run the Docker container for this project.

### Build the Docker Image

Run the following command to build the Docker image:

```sh
docker build -t hackett-app .
```

### Run the Docker Container

After building the image, run the following command to start the Docker container:

```sh
docker run -p 8000:8000 hackett-app
```

This command maps port 8000 on your host to port 8000 on the container.

## Accessing the Application

Once the container is running, you can access the application by navigating to `http://localhost:8000` in your web browser.

## Stopping the Container

To stop the running container, you can use the following command:

```sh
docker ps
```

Find the container ID of your running container and then stop it using:

```sh
docker stop <container_id>
```

Replace `<container_id>` with the actual container ID.

