import redis
import json
import uuid
from fastapi import FastAPI
from fastapi.responses import FileResponse # Добавили это
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

class TodoItem(BaseModel):
    id: str = None
    title: str
    completed: bool = False

@app.get("/")
def read_index():
    return FileResponse("index.html")

@app.get("/todos")
def get_todos():
    todos = []
    keys = r.keys("todo:*")
    for key in keys:
        todo_data = r.get(key)
        todos.append(json.loads(todo_data))
    return todos

@app.post("/todos")
def create_todo(todo: TodoItem):
    todo_id = str(uuid.uuid4())
    todo.id = todo_id
    r.set(f"todo:{todo_id}", todo.json())
    return todo

@app.put("/todos/{todo_id}")
def update_todo(todo_id: str, todo: TodoItem):
    todo.id = todo_id
    r.set(f"todo:{todo_id}", todo.json())
    return {"message": "Updated"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):
    r.delete(f"todo:{todo_id}")
    return {"message": "Deleted"}

