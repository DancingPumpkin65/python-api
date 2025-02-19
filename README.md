# Python FastAPI

This repository contains a Python API project built using FastAPI and SQLAlchemy. The project includes two main services: `main_api` and `todo_db_service`. The `main_api` service handles HTTP requests and interacts with the `todo_db_service` to manage a todo list stored in a MySQL database.

## Project Structure

```text
    python-api
    ├── .env                   # Environment variables
    ├── main_api.py            # The main API service that handles HTTP requests
    ├── todo_db_service.py     # The database service that interacts with the MySQL database
    ├── test_api.py            # Contains premade database test.
    ├── requirements.txt       # Project dependencies
    └── README.md              # Project documentation
```

## Setup

1. Clone the repository:
```sh
    git clone https://github.com/DancingPumpkin65/python-api.git
    cd python-api
```

2. Create and activate a virtual environment:
```sh
    python -m venv env
    source env/Scripts/activate  # On Windows
    source env/bin/activate      # On Unix or MacOS
```

3. Install the dependencies:
```sh
    pip install -r requirements.txt
```

## Connecting to the MySQL Database

Create a .env file in the root directory of the project.

Add the following line to the .env file, replacing `<username>`, `<password>`, `<host>`, `<port>`, and `<database>` with your MySQL database credentials:
```sh
    DATABASE_URL=mysql+pymysql://<username>:<password>@<host>:<port>/<database>
```

## Running the API

1. Start the `todo_db_service`:
```sh
    uvicorn todo_db_service:app --reload
```

2. Start the `main_api` service:
```sh
    uvicorn main_api:app --reload
```

## API Endpoints

### [main_api.py]

- `GET /`: Retrieve all todos.
- `POST /`: Create a new todo.
- `GET /{todo_id}`: Retrieve a specific todo by ID.

### [todo_db_service.py]

- `GET /todos`: Retrieve all todos from the database.
- `POST /todos`: Create a new todo in the database.
- `GET /todos/{todo_id}`: Retrieve a specific todo by ID from the database.
- `PUT /todos/{todo_id}`: Update a specific todo by ID.
- `DELETE /todos/{todo_id}`: Delete a specific todo by ID.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.