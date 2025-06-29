from fastapi import FastAPI
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()

@app.get("/")
async def root():
    return {"message": "Welcome to To-Do App!"}

@app.get("/about")
async def about():
    return {"message": "This is a To-Do App"}