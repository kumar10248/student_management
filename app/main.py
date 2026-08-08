from fastapi import FastAPI
# from app.database.student_db import students
# from app.schemas.student import Student
from app.routes.students import router as student_router

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to Student Management API"
    }

app.include_router(student_router)