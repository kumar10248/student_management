from app.repositories.student_repository import create_student

class InvalidStudentError(Exception):
    pass

def create_student_service(student):

    if not 0<=student.cgpa<=10:
        raise InvalidStudentError("CGPA must be between 0 and 10")
    return create_student(student)
