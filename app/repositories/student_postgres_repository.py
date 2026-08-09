
from sqlalchemy import delete, select, update

from app.database.postgresql import SessionLocal
from app.models.student import Student


def get_all_students():
    db =SessionLocal()
    try:
        stmt=select(Student)
        result=db.execute(stmt)
        return result.scalars().all()
    finally:
        db.close()

def get_students_by_id(student_id:int):
    db =SessionLocal()
    try:
        stmt=select(Student).where(Student.id==student_id)
        result=db.execute(stmt)
        return result.scalar_one_or_none()
    finally:
        db.close()
def add_student(student:Student):
    db=SessionLocal()
    try:
        
        existing=db.execute(select(Student).where(Student.id==student.id)).scalar_one_or_none()
        if existing:
            return None
        db_student = Student(
            id=student.id,
            name=student.name,
            age=student.age,
            cgpa=student.cgpa
        )
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    finally:
        db.close()


def update_in_postgres(student:Student):
    db=SessionLocal()
    try:
        existing=db.execute(select(Student).where(Student.id==student.id)).scalar_one_or_none()
        if existing is None:
            None
                    
        
        existing.name = student.name
        existing.age = student.age
        existing.cgpa = student.cgpa
        db.commit()
        db.refresh(existing)
        return existing
    finally:
         db.close()

def delete_in_postgres(student_id:int):
     db=SessionLocal()
     try:
        existing=db.execute(select(Student).where(Student.id==student_id)).scalar_one_or_none()
        if existing is None:
            return None
            
        db.execute(delete(Student).where(Student.id==student_id))
        db.commit()
        return  existing
     finally:
         db.close()
                   
        


