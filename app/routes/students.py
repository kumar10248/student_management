from fastapi import APIRouter, HTTPException, status

from app.schemas.student import Student
from app.repositories.student_repository import (
    get_all_students as students_list,
    get_student_by_id,
    update_student_by_id,
    delete_student_by_id,

)
from app.repositories.student_postgres_repository import (
    get_all_students,
    get_students_by_id,
    add_student,
    delete_in_postgres,
    update_in_postgres,
                                                          )

from app.services.student_service import (
    create_student_service,
    InvalidStudentError
    )
router=APIRouter()



@router.get("/postgres/students")
def get_postgres_students():
    return get_all_students()

@router.get("/postgres/students/{student_id}")
def get_postgres_students_by_id(student_id:int):
    student=get_students_by_id(student_id)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="student not found"
        )
    return student

@router.post(
        "/postgres/students",
        status_code=status.HTTP_201_CREATED
        )
def create_student_in_postgres(student:Student):
    try:
        created_student=add_student(student)
    except InvalidStudentError as error:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail=str(error)
        )
    if created_student is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Student already exists with id {student.id}"
        )
    return created_student

@router.delete(
        "/students/postgres/{student_id}",
        status_code=status.HTTP_204_NO_CONTENT
        )
def remove_student_in_postgres(student_id:int):
    deleted_student=delete_in_postgres(student_id)
    if deleted_student is None:
        raise HTTPException(
            tatus_code=status.HTTP_404_NOT_FOUND,
            detail="student not found"
        )

@router.put("/students/postgres/{student_id}",response_model=Student,status_code=status.HTTP_200_OK)
def update_student_in_postgres(student_id:int,student:Student):
   if student_id != student.id:
       raise HTTPException(
           status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
           detail="Student ID in URL and request body must match"
       )

   
   updated_student=update_in_postgres(student)
   if updated_student is None:
       raise HTTPException(
           status_code=status.HTTP_404_NOT_FOUND,
           detail="Student not found"
       )
   return updated_student


@router.get("/students",response_model=list[Student])
def get_students():
    
    return students_list()

@router.get("/students/{student_id}",response_model=Student)
def get_student(student_id:int):
    student=get_student_by_id(student_id)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="student not found"
        )
    return student

@router.post(
        "/students",
        status_code=status.HTTP_201_CREATED
        )
def create_student(student:Student):
    try:
        created_student=create_student_service(student)
    except InvalidStudentError as error:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail=str(error)
        )
    if created_student is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Student already exists with id {student.id}"
        )
    return created_student
@router.delete(
        "/students/{student_id}",
        status_code=status.HTTP_204_NO_CONTENT
        )
def remove_student(student_id:int):
    deleted_student=delete_student_by_id(student_id)
    if deleted_student is None:
        raise HTTPException(
            tatus_code=status.HTTP_404_NOT_FOUND,
            detail="student not found"
        )

@router.put("/students/{student_id}",response_model=Student,status_code=status.HTTP_200_OK)
def update_student(student_id:int,student:Student):
   if student_id != student.id:
       raise HTTPException(
           status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
           detail="Student ID in URL and request body must match"
       )
   updated_student=update_student_by_id(student_id,student)
   if updated_student is None:
       raise HTTPException(
           status_code=status.HTTP_404_NOT_FOUND,
           detail="Student not found"
       )
   return updated_student