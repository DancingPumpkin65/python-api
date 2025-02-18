from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("No DATABASE_URL set for the application")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class TodoModel(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    completed = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)

# --- FastAPI App ---
app = FastAPI(title="Todo Database Service")

# --- Pydantic Schemas ---
class Todo(BaseModel):
    name: str
    completed: bool

    class Config:
        orm_mode = True

class TodoOut(Todo):
    id: int

# --- Dependency: Database Session ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/todos", response_model=List[TodoOut])
def read_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoModel).all()
    return todos

@app.post("/todos", response_model=TodoOut)
def create_todo(todo: Todo, db: Session = Depends(get_db)):
    todo_db = TodoModel(**todo.dict())
    db.add(todo_db)
    db.commit()
    db.refresh(todo_db)
    return todo_db

@app.get("/todos/{todo_id}", response_model=TodoOut)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/todos/{todo_id}", response_model=TodoOut)
def update_todo(todo_id: int, updated_todo: Todo, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in updated_todo.dict().items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo

@app.delete("/todos/{todo_id}", response_model=TodoOut)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return todo
