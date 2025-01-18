# Django Template

This is a template for a Docker container that can be used to run a Django application. The Django project is located in the `src` directory. The Docker container is built using the `Dockerfile` in the root directory.

## Getting Started

To get started with this template, follow these steps:

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Build the Docker image:
    ```sh
    docker build -t django-template .
    ```

3. Run the Docker container:
    ```sh
    docker run -p 8000:8000 django-template
    ```

4. Access the Django application at `http://localhost:8000`.

## Project Structure

- `src/`: Contains the Django project.
- `Dockerfile`: Used to build the Docker image.

## Customization

To customize the Django application, modify the files in the `src` directory and rebuild the Docker image.

## License

This project is licensed under the MIT License.