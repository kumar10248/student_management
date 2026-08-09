from app.database.mongodb import students_collection

print(students_collection.find_one())