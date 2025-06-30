from fastapi import FastAPI, Depends
from dotenv import load_dotenv
from pydantic import BaseModel
from database import get_db
from models import Task
from sqlalchemy import select, result_tuple
from sqlalchemy.ext.asyncio import AsyncSession
import os

load_dotenv()

app = FastAPI()

class TaskCreate(BaseModel):
    title: str
    description: str | None
    completed: bool = False

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool

    class Config:
        from_attributes = True

@app.get("/")
async def root():
    return {"message": "Welcome to To-Do App!"}

@app.get("/about")
async def about():
    return {"message": "This is a To-Do App"}

@app.post("/tasks/", response_model=TaskResponse)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    db_task = Task(title=task.title, description=task.description, completed=task.completed)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

@app.get("/tasks/", response_model=list[TaskResponse])
async def get_tasks(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task))
    tasks = result.scalars().all()
    return tasks