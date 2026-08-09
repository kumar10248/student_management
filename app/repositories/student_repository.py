from app.database.mongodb import students_collection

from app.schemas.student import Student

def clean_student(student):
    if student is None:
        return None

    return {
        key: value
        for key, value in student.items()
        if key != "_id"
    }


def get_all_students():
    students=students_collection.find()
    return  [clean_student(student) for student in students]


def get_student_by_id(student_id: int):
    student=students_collection.find_one({"id":student_id})

    return clean_student(student)

def create_student(student:Student):
    student_exist=students_collection.find_one({"id":student.id})
    if student_exist:
        return None
    students_collection.insert_one(
        student.model_dump()
    )
    return student.model_dump()

def update_student_by_id(student_id:int, student:Student):
    result = students_collection.update_one(
        {"id":student_id},
        {"$set":student.model_dump()}
    )
    if result.matched_count==0:
        return None
    updated_student=students_collection.find_one({"id":student_id})
    return clean_student(updated_student)

def delete_student_by_id(student_id: int):

    student = students_collection.find_one({
        "id": student_id
    })

    if student is None:
        return None

    students_collection.delete_one({
        "id": student_id
    })

    return clean_student(student)