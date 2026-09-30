from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


tasks = {}
next_task_id = 1


@app.get("/tasks")
def list_tasks():
    # TODO: Return all tasks.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: Return the task or raise HTTPException with status code 404.
    pass


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    global next_task_id

    # TODO: Create and store a task, then increment next_task_id.
    pass
