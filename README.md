# News Service Application

This is a simple RESTful API application built with FastAPI for managing news articles and their comments.

### Clean Architecture

This application follows the principles of clean architecture, which emphasizes separation of concerns and independence of frameworks. The codebase is organized into distinct layers - repository, service, and router - each responsible for specific functionalities. This separation allows for better maintainability, testability, and scalability of the application. Additionally, the use of dependency injection ensures loose coupling between components, making it easier to replace or modify individual parts of the system without affecting the overall functionality. Overall, clean architecture promotes a clear and modular design, facilitating easier understanding and development of complex software systems.

## Technology Stack

- **Python 3.12.2:** Programming language used for development.
- **FastAPI:** Web framework used to build the RESTful API.
- **Pydantic:** Data validation and parsing library used for defining schemas and parsing data.
- **Docker Compose:** Tool used for defining and running multi-container Docker applications.
- **Ruff:** Code formatting and linting tool for Python.

## Running the Application

### Prerequisites

Make sure you have Docker and Docker Compose installed on your machine.

### Docker Compose

To run the application using Docker Compose, follow these steps:

1. Clone this repository to your local machine:
```console
git clone https://github.com/stirk1337/cyberlympha-test-task
```
2. Navigate to the root directory of the project:
```console
cd cyberlympha-test-task
```
3. Start the application using Docker Compose and Makefile:
```consoleg
make dev
```
4. Once the containers are up and running, you can access the API at `http://localhost:8000`.
Additionally, you can explore the interactive documentation provided by Swagger UI by navigating to `http://localhost:8000/docs`

### Makefile for Development

A Makefile is provided with useful commands for development tasks:

- **dev:** Start the application using Docker Compose.
- **lint:** Run code formatting and linting checks using Ruff.

To run these commands, simply execute `make <command>` in your terminal.
