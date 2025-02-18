# Python FastAPI

This is a simple FastAPI-based project that provides a basic API for managing todos and levels.

## Project Structure


## Setup

1. Clone the repository:
```sh
    git clone https://github.com/yourusername/python-api.git
    cd python-api
```

2. Create a virtual environment and activate it:
```sh
    python -m venv env
    source env/Scripts/activate  # On Windows
    source env/bin/activate      # On Unix or MacOS
```

3. Install the dependencies:
 ```sh
    pip install fastapi httpx uvicorn
```

## Running the Application

To run the FastAPI application, use the following command:
```sh
    uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

## Endpoints

### Todos

`GET /` - Retrieve all todos
`POST /{todo_id}` - Create a new todo
`GET /{todo_id}` - Retrieve a specific todo
`PUT /{todo_id}` - Update a specific todo
`DELETE /{todo_id}` - Delete a specific todo

### Levels

POST /level/add - Add a new level

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.