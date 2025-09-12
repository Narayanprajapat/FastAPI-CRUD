# FastAPI-CRUD

FastAPI & PostgreSQL DB

## Key Features & Benefits

- **CRUD Operations:** Implements Create, Read, Update, and Delete operations for book management.
- **Health Check Endpoint:** Provides a health check endpoint for monitoring application status.
- **API Key Authentication:** Secure API access using API key authentication.
- **Dockerized Deployment:** Easy deployment using Docker.
- **Asynchronous Operations:** Leverages FastAPI's asynchronous capabilities for efficient performance.
- **Database Integration:** Uses SQLAlchemy and asyncpg for database interaction.
- **Configuration Management:** Utilizes environment variables for configuration.

## Prerequisites & Dependencies

Before you begin, ensure you have met the following requirements:

- **Python:** Version 3.12 or higher.
- **Poetry:** A tool for dependency management and packaging.
- **Docker:** For containerization.
- **PostgreSQL:** Database to store books data

## Installation & Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Narayanprajapat/FastAPI-CRUD
    cd FastAPI-CRUD
    ```

2.  **Install Poetry:**

    ```bash
    pip install poetry
    ```

3.  **Install dependencies:**

    ```bash
    poetry shell
    poetry install
    ```

4. **Set up Environment Variables**
    Create a `.env` file based on the example below. Replace the placeholders with your actual values.

    ```
    HOST='localhost'
    USERNAME='postgres'
    PASSWORD='1999'
    PORT='5432'
    ```

5.  **Run Migrations (Optional - If using Alembic):**

    ```bash
    <!-- Already setup with server as well if do not wanted to setup alembic -->
    alembic upgrade head
    alembic revision --autogenerate -m "add table" # if you modify anything in db
    alembic upgrade head # 
    ```

6.  **Without Docker:**

    ```bash
    uvicorn app.server:app --reload --port 9000
    ```


7.  **Run the application using Docker:**

    ```bash
    docker build -t fastapi-crud .
    docker run -p 8000:8000 fastapi-crud
    ```
    Or you can use docker compose

    ```bash
    docker-compose up -d
    ```

## Usage Examples & API Documentation

### API Endpoints:

#### Health Check

-   **Endpoint:** `api/v1/health`
-   **Method:** `GET`
-   **Description:** Checks the health status of the application.
-   **Example Response:**

    ```json
    {
        "status_code": 200,
        "message": "Success"
    }
    ```

#### Books

-   **Base URL:** `/api/v1/books`

##### Create a Book

-   **Endpoint:** `/`
-   **Method:** `POST`
-   **Description:** Creates a new book.
-   **Request Body:**

    ```json
    {
        "title":"NLP with Python",
        "description": "NLP"
    }
    ```

-   **Example Response:**

    ```json
    {
        "title": "NLP with Python",
        "description": "NLP",
        "id": 17,
        "created_at": "2025-09-10T15:15:43.603551",
        "updated_at": "2025-09-10T15:15:43.603551"
    }
    ```

##### Get all Book

-   **Endpoint:** `/`
-   **Method:** `GET`
-   **Description:** Get all book.
-   **Request Params:**

    ```string
    page_no=1&last_book_id=0 #
    ```

-   **Example Response:**

    ```json
    [{
        "title": "NLP with Python",
        "description": "NLP",
        "id": 1,
        "created_at": "2025-09-10T15:15:43.603551",
        "updated_at": "2025-09-10T15:15:43.603551"
    }]
    ```

##### Get Book by id

-   **Endpoint:** `/{book_id}`
-   **Method:** `GET`
-   **Description:** Get a book by id.
-   **Request Params:**

    ```string
    book_id=1
    ```

-   **Example Response:**

    ```json
    {
        "title": "NLP with Python",
        "description": "NLP",
        "id": 1,
        "created_at": "2025-09-10T15:15:43.603551",
        "updated_at": "2025-09-10T15:15:43.603551"
    }
    ```



##### Update a Book

-   **Endpoint:** `/{book_id}`
-   **Method:** `PUT`
-   **Description:** Updates an existing book.
-   **Request Body:**

    ```json
    {
        "description": "NLP with Python"
    }
    ```
-   **Example Response:**

    ```json
    {
        "title": "NLP",
        "description": "NLP with Python",
        "id": 15,
        "created_at": "2025-09-10T15:11:18.615660",
        "updated_at": "2025-09-10T15:16:49.078606"
    }
    ```

##### Delete a Book

-   **Endpoint:** `/books/{book_id}`
-   **Method:** `DELETE`
-   **Description:** Deletes a book.

*Note: You will need to include the `X-API-Key` header with your API key for authenticated endpoints.*

## Configuration Options

## Contributing Guidelines

We welcome contributions! To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes.
4.  Write tests for your changes.
5.  Submit a pull request.

## Acknowledgments

-   FastAPI: For providing a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
-   SQLAlchemy: For providing a powerful and flexible SQL toolkit and Object Relational Mapper.
