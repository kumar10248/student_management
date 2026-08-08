from fastapi import APIRouter

from app.schemas.student import Student
from app.database.student_db import students

router=APIRouter()

@router.get("/students")
def get_students():
    return students

@router.get("/students/{student_id}")
def get_student(student_id:int):
    return students.get(student_id)

@router.post("/students")
def create_student(student:Student):
    students[student.id]=student
    return student

@router.delete("/students/{student_id}")
def remove_student(student_id:int):
    return students.pop(student_id,"Student Id not found")

@router.put("/students/{student_id}")
def update_student(student_id:int,student:Student):
    if student_id not in students:
        return "Student id not found"
    students[student_id]=student.model_dump()
        
    return students[student_id]
