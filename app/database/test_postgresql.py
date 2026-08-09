from app.database.postgresql import SessionLocal
from app.models.student import Student


db = SessionLocal()

student = Student(
    id=101,
    name="Devashish",
    age=22,
    cgpa=7.9
)

db.add(student)
db.commit()
db.refresh(student)

print(student.id)
print(student.name)
print(student.age)
print(student.cgpa)

db.close()