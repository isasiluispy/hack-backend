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

## Updating the Frontend Files

To update the frontend files, follow these steps:

1. In the frontend app, run the following command to build the Angular project:

    ```sh
    ng build
    ```

2. Move the resulting files to the appropriate directories in your Django project:

    ```
    your_django_project/
    ├── static/
    │   └── angular/  # Static files like JS, CSS, etc.
    ├── templates/
    │   └── angular/
    │       └── index.html
    ├── your_django_app/
    ├── manage.py
    └── ...
    ```

3. In the `index.html` file, replace every use of the CSS, JS, and image files with the Django static tag like this:

    ```html
    {% static 'angular/file_name' %}
    ```

This ensures that Django correctly serves the static files.
