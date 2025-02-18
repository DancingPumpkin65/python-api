from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import httpx

app = FastAPI(title="Main API Service")

class Todo(BaseModel):
    name: str
    completed: bool

# URL for the Todo database service (adjust the port if necessary)
DATABASE_SERVICE_URL = "http://localhost:8001/todos"

@app.get("/", response_model=List[Todo])
async def get_todos():
    async with httpx.AsyncClient() as client:
        response = await client.get(DATABASE_SERVICE_URL)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error retrieving todos")
    return response.json()

@app.post("/", response_model=Todo)
async def post_todo(todo: Todo):
    async with httpx.AsyncClient() as client:
        response = await client.post(DATABASE_SERVICE_URL, json=todo.dict())
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error creating todo")
    return response.json()

@app.get("/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{DATABASE_SERVICE_URL}/{todo_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Todo not found")
    return response.json()

@app.put("/{todo_id}", response_model=Todo)
async def put_todo(todo_id: int, todo: Todo):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{DATABASE_SERVICE_URL}/{todo_id}", json=todo.dict())
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error updating todo")
    return response.json()

@app.delete("/{todo_id}", response_model=Todo)
async def delete_todo(todo_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{DATABASE_SERVICE_URL}/{todo_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error deleting todo")
    return response.json()
