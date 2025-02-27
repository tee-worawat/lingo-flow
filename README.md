# AI Block Software Development

This project is a frontend application for AI block software development, similar to NodeRED for IoT developments. Each block provides the concept of functionalities, and developers write prompts instead of actual code. The code is generated based on those prompts and then performs input/output calls to the connected blocks.

## Prerequisites

- Docker

## Building the Docker Image

To build the Docker image for this project, run the following command in the root directory of the project:

```sh
docker build -t ai-block-software-dev .
```

## Running the Docker Container

To run the Docker container, use the following command:

```sh
docker run -p 5000:5000 ai-block-software-dev
```

This will start the application and make it accessible at `http://localhost:5000`.

## Development

For development purposes, you can run the application locally using the following commands:

1. Install dependencies:

    ```sh
    npm install
    ```

2. Start the development server:

    ```sh
    npm start
    ```

This will start the application and make it accessible at `http://localhost:3000`.