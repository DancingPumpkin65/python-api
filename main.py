# Baic Flask API
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/get-user/<user_id>')
# def get_user(user_id):
#     user_data = {
#           'user_id': user_id,
#             'name': 'John Doe',
#             'email': 'john.doe@example.com'
#     }

#     extra = request.args.get('extra')
#     if extra:
#         user_data['extra'] = extra
    
#     return jsonify(user_data), 200

# if __name__ == '__main__':
#         app.run(debug=True)

# API: Application Programming Interface, a web service that allows interaction between two systems.
# Fast API advantages:
#     -Data validation: Enforces types in function signatures, and data schemas using Pydantic. 
#    Perform data validation, serialization, and documentation.
#     -Auto documentaion: Swagger UI / ReDoc automatically generated and API documentation updated.
#     -Auto completion and code suggestions: PyCharm, Visual Studio Code, and other editors 
#    support FastAPI.

# Our first FastAPI API
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Endpoint: the point of entry in a communication channel when two systems are interacting.
# For example: '/hello' in localhost:8000/hello
# Mthods: GET(returns information), POST(sends informations), PUT(updates informations), 
# DELETE(deletes informations), PATCH, OPTIONS, HEAD

# @app.get('/')
# def home():
#     return {'Data': 'Testing FastAPI'}

# @app.get('/about')
# def aboout():
#     return {'Data': 'About page'}

class Todo(BaseModel):
    name: str
    completed: bool

# Mock data
todos = {}

@app.get('/', response_model=List[Todo])
async def read_todos():
    return list(todos.values())

@app.post('/{todo_id}', response_model=Todo)
async def create_todo(todo: Todo):
    todo_id = str(len(todos) + 1)
    todos[todo_id] = todo
    return todo

@app.get('/{todo_id}', response_model=Todo)
async def read_todo(todo_id: str):
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail='Todo not found')
    return todo

@app.put('/{todo_id}', response_model=Todo)
async def update_todo(todo_id: str, updated_todo: Todo):
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail='Todo not found')
    todos[todo_id] = updated_todo
    return updated_todo

@app.delete('/{todo_id}', response_model=Todo)
async def delete_todo(todo_id: str):
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail='Todo not found')
    del todos[todo_id]
    return todo
